# Progress Log

Tolerance stack-up calculator: worst-case, RSS and Monte Carlo, with plots.

## How to resume a session

Open Terminal and run:

```bash
cd ~/Documents/Projects/tolerance-stackup
source .venv/bin/activate
```

Your prompt should start with `(.venv)`.

## My setup

| Item | Value |
|---|---|
| Computer | MacBook Air, Intel chip (x86_64), macOS 13.7 |
| Shell | bash (prompt ends in `$`), startup file is `~/.bash_profile` |
| Python | 3.14.8 from python.org, at `/Library/Frameworks/Python.framework/Versions/3.14/` |
| Editor | VS Code 1.140 (Intel build) with the Microsoft Python extension; `code` command works in Terminal |
| git | 2.39.2 (from Apple's command line developer tools) |
| Anaconda | Still installed at `/opt/anaconda3` (old, Python 3.8), auto-start turned off. Not used for this project. |

## Project layout

| Path | What it is |
|---|---|
| `stackup.py` | The calculator module: functions only, imported by tests and scripts |
| `tests/test_stackup.py` | pytest tests; run with `python -m pytest` from the project folder |
| `learning/` | Practice scripts from Steps 1–2 |
| `requirements.txt` | Packages to install into `.venv` |

## Roadmap

- [x] **Step 0: Setup** *(finished 2026-10-02, first commit `1e237db`)*
  - [x] 0a: Terminal basics, check what's installed
  - [x] 0b: Install Python 3.14 and VS Code, turn off Anaconda auto-start
  - [x] 0c: Project folder, virtual environment, install numpy 2.5.3, pandas 3.0.6, matplotlib 3.11.2, pytest 9.1.1
  - [x] 0d: git setup, `.gitignore`, first commit
- [x] **Step 1: Just enough Python** *(finished 2026-10-05, scripts in `learning/`)*
  - [x] 1a: Running Python, variables, types, f-strings, reading errors (`step1_variables.py`)
  - [x] 1b: Lists and loops (`step1_lists.py`)
  - [x] 1c: Dictionaries; a list of dictionaries as a stack-up table (`step1_dicts.py`)
  - [x] 1d: Functions; one function reused on two stacks (`step1_functions.py`)
- [x] **Step 2: NumPy basics** *(finished 2026-10-05)*
  - [x] 2a: Arrays and math on whole columns (`step2_arrays.py`)
  - [x] 2b: Random sampling: normal vs uniform, seeds, counting out-of-spec (`step2_random.py`)
- [x] **Step 3: Worst-case stack** *(finished 2026-10-06)*
  - [x] 3a: Hand calc, then `calc_worst_case()` in the `stackup.py` module
  - [x] 3b: First pytest tests (`tests/test_stackup.py`): housing stack 0.22–0.88 mm, slot stack 0.10–0.30 mm
- [ ] Step 4: pandas: load stack from CSV, contribution table
- [ ] Step 5: RSS
- [ ] Step 6: Monte Carlo
- [ ] Step 7: matplotlib plots
- [ ] Step 8: Make it a real project (module, CLI, tests, README)

Commit to git at the end of every step.

## What I've learned

### Terminal
- `pwd`: print working directory (where am I?)
- `ls`: list files. `ls -a` also shows hidden files.
- `cd <folder>`: change directory. `cd ..` goes up one level.
- `mkdir <name>`: make a new folder
- `which <command>`: show which copy of a command will run
- `echo $PATH`: print the PATH variable
- `cat <file>`: print a file's contents
- `open <file>`: same as double-clicking in Finder
- Up arrow recalls the last command. Ctrl + C stops a stuck command.
- Commands and file names are case-sensitive.
- Spaces separate the pieces of a command, so names with spaces need quotes. Folder names use hyphens (`tolerance-stackup`); Python file names use underscores (`stack_calc.py`), because Python reads `-` as minus.
- A `--flag` like `--version` is an option that changes what a command does.
- Error messages are information. `command not found` means nothing with that name is on the PATH.

### Concepts
- **PATH**: the list of folders the terminal searches, left to right, when you type a command. The first match wins (like pulling a bolt from the first bin with the right part number).
- **`~/.bash_profile`**: a startup file bash runs every time Terminal opens. Installers add lines to it to change the PATH. That's why you have to reopen Terminal after installing things.
- **Chip architecture**: apps are built for a specific chip family. `arm64` = Apple Silicon, `x86_64`/`x64` = Intel. Intel Macs can't run Apple Silicon-only apps.
- **Code signing**: macOS checks a digital signature on downloaded apps (like a certificate of conformance). A half-copied app fails the check and is reported as "damaged."
- **Hidden files**: names starting with `.` are hidden from `ls` and Finder. Used for support files you don't edit day to day (`.bash_profile`, `.venv`, `.git`).
- **`.` and `..`**: `.` means "this folder" (`code .`), `..` means "the parent folder" (`cd ..`).
- **Virtual environment (`.venv`)**: a private set of packages for one project, so other projects can't break it. Activating it puts `.venv/bin` at the front of the PATH, but only in that Terminal window and only until it closes. That's why every new window needs `source .venv/bin/activate`.
- **requirements.txt**: the project's bill of materials. `pip install -r requirements.txt` rebuilds the environment from it.
- **Text files end with a newline.** git flags files that don't.
- **Markdown (`.md`)**: plain text where `#` is a heading, `-` is a bullet and `|` builds a table. GitHub shows it formatted.
- **Test, don't guess.** If unsure what a command did, check it (`which`, `echo $PATH`, `git status`).

### git
| git | What it is | PDM equivalent |
|---|---|---|
| repository | Project folder plus its full history (in the hidden `.git` folder) | The vault |
| commit | A saved snapshot with a message | A released revision with its ECO description |
| staging (`git add`) | Choosing which changes go into the next commit | Putting together the ECO package |
| `.gitignore` | Files git should never track | |

- `git config --global ...`: one-time setup (name, email, default branch `main`), saved in `~/.gitconfig`
- `git init`: start tracking a folder
- `git status`: what's changed and what's staged. Check it before every commit.
- `git add .`: stage everything that isn't ignored
- `git commit -m "Message"`: save the snapshot. Messages are short and imperative ("Add X", "Fix Y"). Always use `-m`; if an editor opens anyway, type `:q!` and Enter.
- `git log --oneline`: list the history, one commit per line with its ID (hash)
- What to ignore: anything that can be rebuilt from something else (`.venv/`, `__pycache__/`) or is personal to you or this Mac (`.claude/`, `.DS_Store`). Be explicit in `.gitignore` even if something is already ignored another way.
- Ignored files are never backed up to GitHub.

### Python basics (Step 1)
Full notes are in the reference doc: [Python for Engineering: Learning Reference](https://claude.ai/code/artifact/c7e06e4e-c58b-475e-9236-5f4b79f67acf).

- Run a script with `python learning/file.py`. It runs top to bottom and stops at the first error.
- `=` stores; `==` compares. Types: `int` (counts, signs), `float` (measurements), `str` (text). `50.0` carries no precision; tolerances are stored separately.
- `**` is power; `^` is not. `//` floor division, `%` remainder. Floats can't store 0.1 exactly, so never compare floats with `==`.
- f-strings: `f"{gap:.3f} mm"`; columns with `{name:<10}` and `{value:>10.3f}`. Label every printed number.
- Read tracebacks bottom-up. The error shows where it failed, not always where the mistake is.
- Lists: `[0]` is first, `[-1]` is last, `len()`, `sum()`. Loops need indentation. Running total starts at 0 before the loop.
- Dictionaries look values up by key (`dim['nominal']`). A list of dictionaries is a stack-up table: one dictionary per row.
- Functions: `def`, docstring first, `return` the result. Define them once at the top, not inside loops. Parameters are labels for whatever is passed in. Variables inside a function are local. Name functions with verbs (`calc_nominal_gap`), variables with nouns (`housing_gap`).
- Python can't catch wrong logic (a sign error, a copy-paste name). That's what tests are for (Step 3).

### NumPy (Step 2)
- `import numpy as np`. Packages only import if the `.venv` Python runs the script.
- Lists repeat and join with `*` and `+`; arrays do element-wise math. Two same-length arrays multiply position by position, like a spreadsheet column.
- Use NumPy's own functions on arrays (`np.sum`, `np.mean`, `np.std`), not Python's built-in `sum`.
- `:.3f` works on single numbers, not arrays. `np.set_printoptions(precision=3, floatmode="fixed")` formats printed arrays.
- Parallel arrays can get out of step like parallel lists; pandas (Step 4) binds columns into one table.
- `rng = np.random.default_rng(seed=42)`. `rng.normal(mean, sigma, n)` and `rng.uniform(low, high, n)` return arrays of samples.
- Normal with σ = tolerance/3: about 0.27% outside the limits. Uniform: never outside, but σ about 1.7 times larger. The assumed distribution changes a Monte Carlo answer.
- Comparisons give True/False arrays; `np.sum` counts them and `np.mean` gives the fraction. Use `|` (or) and `&` (and), with each comparison in parentheses.
- A seed makes results repeatable, not more correct. Pick it once; don't shop for a nice answer.
- Don't name variables after built-ins (`min`, `max`, `sum`).

### Worst case and testing (Step 3)
- A module (`stackup.py`) holds only imports and functions; importing runs the file, so no top-level prints. `if __name__ == "__main__":` runs a block only when the file is run directly.
- `return min_gap, max_gap` returns a tuple; `min_gap, max_gap = calc_worst_case(...)` unpacks it. Importing a function doesn't run it, and its local variables don't exist outside; store what it returns.
- `np.where(condition, if_true, if_false)` is an IF filled down a column. Max gap: openers at upper limit, closers at lower limit; min gap is the reverse.
- Edit `stackup.py`, then restart `python` to see changes at the `>>>` prompt.
- Tests: files `test_*.py`, functions `test_*()` with no parameters, ending in `assert`. Structure: set up inputs, call, compare to the hand calc.
- Compare floats with `pytest.approx` (±1 part per million by default), never plain `==`.
- `python -m pytest` uses the `.venv` Python and lets tests import `stackup` from the project folder. `.` = pass, `F` = fail; read failures bottom-up (`Expected` vs `Obtained`).
- Break the code on purpose to see each test fail. A test that has never failed might not be checking anything.
- Ignore `.pytest_cache/` (rebuilt every run) like `__pycache__/`.

## Next step

**Step 4: pandas.** Load a stack from a CSV file into a DataFrame (a table whose columns are NumPy arrays and whose rows stay together), feed it to `calc_worst_case`, and build a contribution table showing how much each dimension adds to the worst-case spread.
