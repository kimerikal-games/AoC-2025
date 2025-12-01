import pathlib
import statistics
import subprocess
import time

import pandas as pd
from tqdm.auto import tqdm

REPEATS = 5

interpreters = [
    ("Python 3.14", ["uv", "run", "--python", "cpython3.14"]),
    ("PyPy 3.11", ["uv", "run", "--python", "pypy3.11"]),
]


# -------------------------------------------------------------------
# Interpreter utilities
# -------------------------------------------------------------------
def print_interpreter_versions(interpreters_list: list[tuple[str, list[str]]]) -> None:
    print("Interpreters:")
    for name, cmd in interpreters_list:
        out = subprocess.run(
            cmd + ["python", "--version"],
            check=True,
            capture_output=True,
            text=True,
        )
        print("-", name)
        print(out.stdout.strip())
    print()


def get_interpreter_markdown(interpreters_list: list[tuple[str, list[str]]]) -> str:
    """Return a markdown bullet list with interpreter versions."""
    md = ""
    for name, cmd in interpreters_list:
        out = subprocess.run(
            cmd + ["python", "--version"],
            check=True,
            capture_output=True,
            text=True,
        )
        md += f"- {name}: {out.stdout.replace('\n', ' ').strip()}\n"
    md += "\n"
    return md


# -------------------------------------------------------------------
# Measurement core
# -------------------------------------------------------------------
def measure_interpreter_on_day(
    day: int,
    day_path: pathlib.Path,
    name: str,
    cmd: list[str],
    repeats: int,
    pbar: tqdm,
) -> tuple[bool, float | None, float | None]:
    """
    Run a day's program with a given interpreter multiple times.

    Returns (ok, avg_time_ms, avg_memory_kb).
    If ok is False, averages are None.
    """
    times_ms: list[float] = []
    memories_kb: list[float] = []

    # Use a single opened stdin file per interpreter/day
    in_path = day_path / "in.txt"
    with in_path.open("r") as stdin_f:
        for i in range(repeats):
            pbar.set_description_str(f"Day {day:02d} {name:>8s} {i+1}/{repeats}")
            pbar.update()


            stdin_f.seek(0)
            proc = subprocess.run(
                ["time", "-f", "%S %U %M"] + cmd + [str(day_path / "program.py")],
                stdin=stdin_f,
                capture_output=True,
                text=True,
            )

            if proc.returncode != 0:
                print(f"Day {day:02d} {name} failed")
                return False, None, None

            parts = proc.stderr.split()
            if len(parts) < 3:
                print(f"Day {day:02d} {name} produced unexpected time output")
                return False, None, None

            sys_t = float(parts[0])
            usr_t = float(parts[1])
            mem_kb = float(parts[2])

            runtime_ms = 1000 * (sys_t + usr_t)

            # Stop if a run takes more than 10 seconds
            if runtime_ms > 10_000:
                print(f"Day {day:02d} {name} exceeded 10 seconds")
                return False, None, None

            times_ms.append(runtime_ms)
            memories_kb.append(mem_kb)

    avg_time_ms = statistics.fmean(times_ms)
    avg_memory_kb = statistics.fmean(memories_kb)
    return True, avg_time_ms, avg_memory_kb


def measure_day(
    day_path: pathlib.Path,
    interpreters_list: list[tuple[str, list[str]]],
    repeats: int,
    pbar: tqdm,
) -> dict | None:
    """
    Measure one day for all interpreters.

    Returns a result dict if all interpreters succeed,
    otherwise returns None.
    """
    day_name = day_path.name
    if not day_name.isdigit():
        return None

    day = int(day_name)
    if day == 0:
        return None

    result: dict[str, float | None] = {"Day": day}

    # Count lines, words, bytes
    wc = subprocess.run(
        ["wc", str(day_path / "program.py")],
        check=True,
        capture_output=True,
        text=True,
    )
    lines, words, chars = map(int, wc.stdout.split()[:3])
    result["Lines"] = lines
    result["Words"] = words
    result["Bytes"] = chars

    # Measure for each interpreter
    for name, cmd in interpreters_list:
        ok, avg_time_ms, avg_mem_kb = measure_interpreter_on_day(
            day=day,
            day_path=day_path,
            name=name,
            cmd=cmd,
            repeats=repeats,
            pbar=pbar,
        )
        if not ok:
            return None

        result[f"{name} Time [ms]"] = avg_time_ms
        result[f"{name} Memory [KB]"] = avg_mem_kb

    return result


def collect_measurements(
    root: pathlib.Path,
    interpreters_list: list[tuple[str, list[str]]],
    repeats: int,
) -> pd.DataFrame:
    """Walk all day directories, run measurements, return a DataFrame."""
    paths = sorted((root / "day").iterdir())
    # Only count numeric, non-zero day dirs in progress total
    day_paths = [p for p in paths if p.name.isdigit() and int(p.name) > 0]
    pbar_total = len(day_paths) * len(interpreters_list) * repeats

    results: list[dict] = []

    with tqdm(
        total=pbar_total,
        bar_format="{l_bar}|{bar}| {n_fmt}/{total_fmt}{postfix}",
    ) as pbar:
        for day_path in day_paths:
            result = measure_day(day_path, interpreters_list, repeats, pbar)
            if result is not None:
                results.append(result)

    if not results:
        return pd.DataFrame()

    df = pd.DataFrame(results).set_index("Day").sort_index()
    return df


# -------------------------------------------------------------------
# README update
# -------------------------------------------------------------------
def update_readme_with_measurements(
    readme_path: pathlib.Path,
    markdown_block: str,
    start_marker: str = "<!-- region measurements -->",
    end_marker: str = "<!-- endregion measurements -->",
) -> None:
    """Replace content between markers in README with the given markdown."""
    readme = readme_path.read_text()

    start_index = readme.index(start_marker)
    end_index = readme.index(end_marker)

    new_readme = readme[: start_index + len(start_marker)] + "\n" + markdown_block + "\n" + readme[end_index:]

    readme_path.write_text(new_readme)


# -------------------------------------------------------------------
# Main
# -------------------------------------------------------------------
def main() -> None:
    root = pathlib.Path(".").resolve()

    # 1. Show interpreter versions
    print_interpreter_versions(interpreters)

    # 2. Collect measurements
    df = collect_measurements(root, interpreters, REPEATS)

    # 3. Print DataFrame to stdout
    if df.empty:
        print("No measurement results produced.")
        return

    print(df)

    # 4. Build markdown
    md = get_interpreter_markdown(interpreters)
    md += df.to_markdown()

    # 5. Update README
    readme_path = root / "README.md"
    update_readme_with_measurements(readme_path, md)


if __name__ == "__main__":
    main()
