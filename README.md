# AoC-2025

My solutions for [Advent of Code 2025](https://adventofcode.com/2025).

## Advent Calendar

<div align="center">
<table>
    <thead>
        <tr>
            <th colspan="7"><div align="center">December 2025</div></th>
        </tr>
        <tr>
            <th align="center">S</th>
            <th align="center">M</th>
            <th align="center">T</th>
            <th align="center">W</th>
            <th align="center">T</th>
            <th align="center">F</th>
            <th align="center">S</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center"></td>
            <td align="center"><a href="https://github.com/kimerikal-games/AoC-2025/blob/master/day/01/program.py">1</a></td>
            <td align="center"><a href="https://github.com/kimerikal-games/AoC-2025/blob/master/day/02/program.py">2</a></td>
            <td align="center"><a href="https://github.com/kimerikal-games/AoC-2025/blob/master/day/03/program.py">3</a></td>
            <td align="center"><a href="https://github.com/kimerikal-games/AoC-2025/blob/master/day/04/program.py">4</a></td>
            <td align="center"><a href="https://github.com/kimerikal-games/AoC-2025/blob/master/day/05/program.py">5</a></td>
            <td align="center"><a href="https://github.com/kimerikal-games/AoC-2025/blob/master/day/06/program.py">6</a></td>
        </tr>
        <tr>
            <td align="center"><a href="https://github.com/kimerikal-games/AoC-2025/blob/master/day/07/program.py">7</a></td>
            <td align="center">8</td>
            <td align="center">9</td>
            <td align="center">10</td>
            <td align="center">11</td>
            <td align="center">12</td>
            <td align="center">13</td>
        </tr>
        <tr>
            <td align="center">14</td>
            <td align="center">15</td>
            <td align="center">16</td>
            <td align="center">17</td>
            <td align="center">18</td>
            <td align="center">19</td>
            <td align="center">20</td>
        </tr>
        <tr>
            <td align="center">21</td>
            <td align="center">22</td>
            <td align="center">23</td>
            <td align="center">24</td>
            <td align="center">25</td>
            <td align="center">26</td>
            <td align="center">27</td>
        </tr>
        <tr>
            <td align="center">28</td>
            <td align="center">29</td>
            <td align="center">30</td>
            <td align="center">31</td>
            <td align="center"></td>
            <td align="center"></td>
            <td align="center"></td>
        </tr>
    </tbody>
</table>
<small>
    Note: The link always points to the code in <code>master</code> branch.
</small>
</div>

## Measurements

<!-- region measurements -->
- Python 3.14: Python 3.14.0
- PyPy 3.11: Python 3.11.13 (413c9b7f57f5, Jul 03 2025, 18:03:56) [PyPy 7.3.20 with GCC 10.2.1 20210130 (Red Hat 10.2.1-11)]

|   Day |   Lines |   Words |   Bytes |   Python 3.14 Time [ms] |   Python 3.14 Memory [KB] |   PyPy 3.11 Time [ms] |   PyPy 3.11 Memory [KB] |
|------:|--------:|--------:|--------:|------------------------:|--------------------------:|----------------------:|------------------------:|
|     1 |      66 |     160 |    1525 |                      10 |                   21905.6 |                    30 |                 62951.2 |
|     2 |      82 |     208 |    2032 |                     156 |                   21788.8 |                    52 |                 63184.8 |
|     3 |      67 |     157 |    1406 |                      40 |                   21827.2 |                    32 |                 63371.2 |
|     4 |      79 |     243 |    1931 |                     228 |                   21852   |                    82 |                 63649.6 |
|     5 |      40 |     121 |    1057 |                      10 |                   21915.2 |                    30 |                 62246.4 |
|     6 |      72 |     180 |    1532 |                      10 |                   21794.4 |                    40 |                 64412.8 |
|     7 |      74 |     194 |    1809 |                      10 |                   21920   |                    24 |                 63257.6 |
<!-- endregion measurements -->

## Structure

```plain
.
├── config.toml         # Current year, name, and email
├── generate.py         # Prepare directory for new puzzle
├── measure.py          # Measure code length, running time/memory
├── day
│   ├── 00              # Template directory
│   │   ├── in.txt
│   │   ├── out.txt
│   │   └── program.py
│   ├── 01
│   │   ├── in.txt      # Full input text
│   │   ├── out.txt     # Puzzle answer
│   │   └── program.py  # Solution code
│   ├── ...
│   └── 25
│       ├── in.txt
│       ├── out.txt
│       └── program.py
├── LICENSE
└── README.md
```

`in.txt` files are visible only in local.

## Usage

For the first time, set up `config.toml`.

```bash
# Generate a directory
$ python3 generate.py <day>

# Measure performance
$ python3 measure.py
```

Running measure.py will automatically update *Measurements* section in this `README.md` file.

## Other helpful tools

- [Visual Studio Code](https://code.visualstudio.com/)
- [Competitive Programming Helper (cph)](https://marketplace.visualstudio.com/items?itemName=DivyanshuAgrawal.competitive-programming-helper)

## License

See `LICENSE` file.
