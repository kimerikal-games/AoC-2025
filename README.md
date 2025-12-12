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
            <td align="center"><a href="https://github.com/kimerikal-games/AoC-2025/blob/master/day/08/program.py">8</a></td>
            <td align="center"><a href="https://github.com/kimerikal-games/AoC-2025/blob/master/day/09/program.py">9</a></td>
            <td align="center"><a href="https://github.com/kimerikal-games/AoC-2025/blob/master/day/10/program.py">10</a></td>
            <td align="center"><a href="https://github.com/kimerikal-games/AoC-2025/blob/master/day/11/program.py">11</a></td>
            <td align="center"><a href="https://github.com/kimerikal-games/AoC-2025/blob/master/day/12/program.py">12</a></td>
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

|   Day |   Lines |   Words |   Bytes |   Python 3.14 Time [s] |   Python 3.14 Memory [KB] |   PyPy 3.11 Time [s] |   PyPy 3.11 Memory [KB] |
|------:|--------:|--------:|--------:|-----------------------:|--------------------------:|---------------------:|------------------------:|
|     1 |      66 |     160 |    1525 |                  0.020 |                   22529.6 |                0.034 |                 62994.4 |
|     2 |      82 |     209 |    2042 |                  0.174 |                   22424.8 |                0.060 |                 63232.0 |
|     3 |      68 |     160 |    1417 |                  0.050 |                   22388.0 |                0.040 |                 63435.2 |
|     4 |      80 |     239 |    1979 |                  0.242 |                   22380.0 |                0.096 |                 63929.6 |
|     5 |      49 |     126 |    1105 |                  0.020 |                   22576.0 |                0.052 |                 65395.2 |
|     6 |      71 |     186 |    1570 |                  0.020 |                   22631.2 |                0.050 |                 64574.4 |
|     7 |      67 |     171 |    1641 |                  0.020 |                   22405.6 |                0.030 |                 63286.4 |
|     8 |     104 |     298 |    2487 |                  0.370 |                   94306.4 |                0.254 |                126604.0 |
|     9 |     110 |     401 |    2790 |                  0.286 |                   22433.6 |                0.150 |                 69014.4 |
|    10 |      96 |     256 |    2736 |                  0.646 |                   98602.4 |              -     |                   -   |
|    11 |      72 |     183 |    1585 |                  0.018 |                   22508.0 |                0.040 |                 63180.0 |
|    12 |      74 |     213 |    2030 |                  0.020 |                   22501.6 |                0.040 |                 63248.0 |

*Note: Day 10 uses CPython 3.13 with Google OR-Tools due to complexity of the problem and OR-Tools compatibility issues with Python 3.14.*
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
│   └── 12
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
