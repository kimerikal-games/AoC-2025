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
|     1 |      66 |     160 |    1525 |                      10 |                   22223.2 |                    30 |                 63025.6 |
|     2 |      82 |     209 |    2042 |                     158 |                   22080   |                    54 |                 63171.2 |
|     3 |      68 |     160 |    1417 |                      40 |                   22339.2 |                    34 |                 63381.6 |
|     4 |      80 |     239 |    1979 |                     246 |                   22180   |                    88 |                 63915.2 |
|     5 |      49 |     126 |    1105 |                      18 |                   22065.6 |                    44 |                 65269.6 |
|     6 |      71 |     186 |    1570 |                      10 |                   22299.2 |                    44 |                 64486.4 |
|     7 |      67 |     171 |    1641 |                      10 |                   22152   |                    26 |                 63263.2 |
|     8 |     104 |     298 |    2487 |                     348 |                   94234.4 |                   234 |                126635   |
|     9 |     110 |     401 |    2790 |                     264 |                   22226.4 |                   146 |                 68972   |
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
