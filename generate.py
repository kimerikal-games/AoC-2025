import argparse
import re
import shutil
import string
import tomllib
from pathlib import Path

import requests
from bs4 import BeautifulSoup


def load_config(path: Path) -> dict:
    try:
        with path.open("rb") as f:
            config = tomllib.load(f)
    except FileNotFoundError as err:
        raise RuntimeError("Please create a config.toml file.") from err
    except tomllib.TOMLDecodeError as err:
        raise RuntimeError("config.toml is not valid TOML.") from err

    required = ["year", "name", "email", "github_owner", "github_repo"]
    missing = [k for k in required if k not in config]
    if missing:
        raise RuntimeError(f"Missing keys in config.toml: {', '.join(missing)}")

    return config


def fetch_title(year: int, day: int, user_agent: str) -> str:
    url = f"https://adventofcode.com/{year}/day/{day}"
    headers = {"User-Agent": user_agent}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise RuntimeError("HTTP error. Check if the day is correct and the puzzle is released.") from err
    except requests.exceptions.RequestException as err:
        raise RuntimeError("Failed to fetch puzzle page.") from err

    soup = BeautifulSoup(response.text, "html.parser")

    heading = soup.select_one("article.day-desc h2")
    if heading is None:
        raise RuntimeError("Could not find the puzzle title. The page structure may have changed.")

    text = heading.text.strip()
    m = re.match(r"--- Day \d+: (?P<title>.+) ---", text)
    if not m:
        raise RuntimeError(f"Unexpected title format: {text!r}")

    return m.group("title")


def initialize_day_directory(template_dir: Path, target_dir: Path) -> None:
    if target_dir.exists():
        raise RuntimeError(f"Target directory {target_dir} already exists.")
    shutil.copytree(template_dir, target_dir)


def substitute_program(path: Path, replacements: dict) -> None:
    with path.open("r") as fr:
        template_str = fr.read()

    substituted = string.Template(template_str).substitute(replacements)

    with path.open("w") as fw:
        fw.write(substituted)


def update_readme(readme_path: Path, owner: str, repo: str, day: int) -> None:
    with readme_path.open("r") as f:
        readme = f.read()

    old = f'<td align="center">{day}</td>'

    new = f'<td align="center"><a href="https://github.com/{owner}/{repo}/blob/master/day/{day:02d}/program.py">{day}</a></td>'

    if old not in readme:
        raise RuntimeError(f"Could not find day {day} cell in README.md")

    readme = readme.replace(old, new, 1)

    with readme_path.open("w") as f:
        f.write(readme)


def main(args: argparse.Namespace, config: dict) -> None:
    year = config["year"]
    day = args.day
    owner = config["github_owner"]
    repo = config["github_repo"]

    base = Path(__file__).resolve().parent
    template_dir = base / "day" / "00"
    target_dir = base / "day" / f"{day:02d}"
    readme_path = base / "README.md"

    ua = f"AoC generate.py script by {config['email']} using {requests.utils.default_user_agent()}"
    title = fetch_title(year, day, ua)
    initialize_day_directory(template_dir, target_dir)

    program_path = target_dir / "program.py"
    substitute_program(
        program_path,
        {
            "year": year,
            "day": day,
            "title": title,
            "name": config["name"],
            "email": config["email"],
        },
    )

    update_readme(readme_path, owner, repo, day)

    print(f"Initialized day {day:02d}: {title}")


if __name__ == "__main__":
    config = load_config(Path("config.toml"))

    parser = argparse.ArgumentParser(description="Initialize the directory for a new puzzle.")
    parser.add_argument("day", help="day number of puzzle", type=int)
    args = parser.parse_args()

    main(args, config)
