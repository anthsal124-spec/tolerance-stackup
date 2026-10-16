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
| `plots.py` | Plotting module: functions that return a figure; scripts save and show it |
| `plots/` | Generated images (ignored by git; rebuilt by the `step7_*.py` scripts) |
| `tests/test_stackup.py` | pytest tests; run with `python -m pytest` from the project folder |
| `data/` | Input stacks as CSV files (committed; tests build their own data instead) |
| `learning/` | Practice scripts; ones that import `stackup` run with `python -m learning.<name>` or VS Code's ▷ |
| `.vscode/settings.json` | Adds the project folder to `PYTHONPATH` in VS Code's terminal (ignored by git) |
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
- [x] **Step 4: pandas** *(finished 2026-10-06)*
  - [x] 4a: Stack in `data/housing_stack.csv`, loaded into a DataFrame (`step4_pandas.py`)
  - [x] 4b: `calc_wc_contributions()`: tolerance band and % contribution, largest first (`step4_contributions.py`)
  - [x] 4c: Contribution test: sums to 100%, Housing leads at 30.30%, bands = worst-case range, input unchanged
- [x] **Step 5: RSS** *(finished 2026-10-07)*
  - [x] 5a: `calc_rss()`: centered, equal-bilateral method; housing gap 0.3954–0.7046 mm
  - [x] 5b: `calc_rss_contributions()` and its cross-check test
  - [x] 5c: Worst case vs RSS comparison with `pd.merge` (`step5_compare.py`): RSS range is 47% of worst case
- [x] **Step 6: Monte Carlo** *(finished 2026-10-12; 9 tests passing)*
  - [x] 6a: `simulate_gaps()` and `step6_monte_carlo.py`: 100,000 assemblies, mean 0.5499 mm, σ 0.0517 mm, 0.283% outside RSS, 0% outside worst case
  - [x] 6b: `distribution="normal"`/`"uniform"` option and `calc_pct_out_of_spec()` (`step6_yield.py`): requirement 0.35–0.75 mm gives 0.008% (normal) vs 1.866% (uniform)
  - [x] 6c: Convergence experiments (`step6_convergence.py`): error shrinks with √samples
  - [x] 6d: Tests for the simulation: reproducible with a seed, matches RSS within 2%, rejects unknown distributions
- [x] **Step 7: matplotlib plots** *(finished 2026-10-13)*
  - [x] 7a: First histogram of simulated gaps (`step7_histogram.py`)
  - [x] 7b: Requirement, RSS and worst-case limits marked; `plot_gap_histogram()` in the new `plots.py` module
  - [x] 7c: `plot_contributions()`: worst case vs RSS, sorted (`step7_contributions.py`)
  - [x] 7d: `plot_gap_comparison()`: normal vs uniform on shared axes (`step7_comparison.py`)
  - [x] Notebooks (2026-10-16): `step7_what_if.ipynb`, tightening Part C to ±0.05 narrows RSS from 0.395–0.705 to 0.409–0.691 mm
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

### pandas (Step 4)
- CSV: a plain-text table, one row per line, header names on line 1. Header names must match the code's column names exactly. Commit input data; it can't be rebuilt.
- `df = pd.read_csv("data/housing_stack.csv")`. Paths are relative to the folder you run from.
- `df["nominal"]` is a column (Series); `.to_numpy()` makes it an array. `df[["name", "tol_band"]]` selects several columns. New columns: `df["upper"] = df["nominal"] + df["plus_tol"]`.
- `df.sort_values("col", ascending=False)` returns a new sorted table; row labels move with their rows. `.iloc[0]` gets a row by position.
- In a script, a bare expression prints nothing; use `print()`. `print(df.round(2).to_string(index=False))` for a clean table.
- Python searches the script's own folder for imports. `python -m learning.script` (dots, no `.py`) or `PYTHONPATH` lets `learning/` scripts import `stackup`. Proper fix in Step 8: an installable package.
- VS Code puts new files in the highlighted folder; click empty space first. `mv old new` moves or renames in Terminal.
- Functions that take a DataFrame: `result = stack.copy()` first, work only on `result`, never read files inside. Select wanted columns instead of dropping unwanted ones.
- Worst-case contribution = tolerance band / sum of bands. Bands add up to max gap − min gap. The biggest contributor isn't always the one to tighten: check the requirement and the cost first.
- In long tracebacks, skip library files and find the last line in your own file. A SyntaxError stops all tests from loading.
- Tests build their own DataFrame (`pd.DataFrame({...})`) like a gauge block, use `pytest.approx(x, abs=0.01)` to state a tolerance, and stop at the first failing assert. `in` / `not in` check membership.
- `git restore <file>` undoes uncommitted changes to a file.

### RSS (Step 5)
- Method: center each dimension in its zone (nominal + (plus − minus)/2), half-band = (plus + minus)/2, gap center = Σ direction × center, RSS ± = √(Σ half²).
- Assumptions (in the docstring): normal, centered, independent, tolerance = ±3σ. About 0.27% of assemblies still fall outside. RSS is weak with few contributors, off-center or correlated processes, or Cpk < 1.
- `**` and `np.sqrt` work element by element. Keep a consistent interface: `calc_rss` returns `min_gap, max_gap` like `calc_worst_case`.
- RSS contribution = half² / Σ half². Squaring turns a 2× tolerance into 4× influence (Housing 30% WC → 42% RSS). Tighten the biggest; small ones can often be loosened cheaply.
- Multi-line docstrings: summary line, blank line, details. Lines under about 80 characters.
- Debugging: when a result looks plausible but wrong, check intermediate values against the hand calc. Two bugs can cancel into a believable number.
- A test is only as good as its reference value. Copy-pasted asserts can check the wrong column and never fail.
- Before every commit: `python -m pytest`, then `git status`, then commit code and its test together. Each commit should leave the project working.
- Totals belong in plain variables, not repeated in a column. `print(df.columns)` shows what a table has.
- `pd.merge(a, b, on="name", suffixes=("_wc", "_rss"))` joins tables by a shared column, like VLOOKUP.
- Scripts have no tests, so sanity-check printed numbers against something known.
- Choosing WC or RSS: ask for the requirement, the consequence of a failure, the volume, process data and the number of contributors. The method sets how tight the part tolerances must be.

### Monte Carlo so far (Step 6a)
- `simulate_gaps()` builds 100,000 virtual assemblies: start every gap at `np.zeros(n_samples)`, then for each dimension add `direction × rng.normal(center, sigma, n_samples)`. The loop runs once per dimension; NumPy handles all assemblies in each pass.
- Default parameters (`n_samples=100_000, seed=42`) apply unless the caller overrides them.
- `zip(centers, sigmas, directions)` walks arrays together. Plural arrays go inside `zip`; singular names (created by the loop) go in the body. `sigma` vs `sigmas` is one letter and a different object.
- A shape error like `(100000,)` vs `(5,)`: find the variable with that size.
- `return` inside a loop exits on the first pass.
- In scripts, get limits from the functions and counts from the data (`n_samples` passed in, or `len(gaps)`), never typed-in numbers.
- Turn on File → Auto Save so the files on disk match the screen.
- Matching RSS (0.283% vs 0.27%) is a calibration run. Monte Carlo's value is where RSS can't go: non-normal or shifted distributions, nonlinear stacks, and yield against a requirement.

### Monte Carlo, continued (Steps 6b–6d)
- `if` / `elif` / `else` chooses which lines run; conditions use `==`. `raise ValueError(f"...")` refuses bad input with a clear message.
- Single values combine with `and` / `or`; arrays combine with `&` / `|`.
- Adding a parameter with a default (`distribution="normal"`) adds a feature without breaking existing callers.
- One function, one job: `simulate_gaps` makes gaps, `calc_pct_out_of_spec(gaps, lower, upper)` counts. The second works on any gaps, even measured ones. `calc_...` functions return; scripts print.
- Pass arguments by name (`lower_limit=..., upper_limit=...`) so the order can't be swapped.
- Same tolerances, requirement 0.35–0.75 mm: worst case FAIL, RSS PASS, Monte Carlo 0.008% (normal) vs 1.866% (uniform). Believe neither without process data; report both with their assumptions.
- A `for` line walks through what comes after `in`; call the function once per pass. Loops can nest. Things that don't change go before the loop. `{n:>10,}` adds thousands separators.
- Sampling error shrinks with √n and depends on the number of hits, not samples: aim for 100+ hits. 8 hits in 100,000 (0.008%) was really about 0.0105%.
- "All tests pass" only covers code the tests call. Testing random code: fix the seed (`np.array_equal`), test statistics with a tolerance sized to sampling scatter (`rel=0.02`), test simple cases exactly, and `with pytest.raises(ValueError):` for bad input.
- Test what the code promises, not the exact digits it happened to produce. The `>` marker shows which assert failed.
- A helper like `housing_arrays()` in the test file removes repeated setup. Changing tests can break them; the summary at the bottom of pytest's output is the to-do list.
- `git show HEAD:path/to/file` prints the last committed version; `| grep -A 6 "text"` filters it. `git status` after a deliberate break confirms it's fully undone.

### matplotlib (Step 7)
- `fig, ax = plt.subplots(figsize=(8, 4.5), layout="constrained")`: `fig` is the sheet, `ax` is one plot on it. `layout="constrained"` keeps everything (including an outside legend) on the sheet.
- `ax.hist(gaps, bins=60, color="#2a78d6")`. Too few bins hide the shape; too many show sampling noise.
- `ax.axvline(x, color=..., linestyle=..., label=...)` for limits; `ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1), frameon=False)` puts the legend outside. The legend lists what has been drawn so far, so call it after the lines.
- Always label axes with units and give a title that says what and how many. Build labels from variables (`{n_samples:,}`), not typed-in numbers. Sentence case.
- Two cues per series (color and line style); each method keeps its color in every plot: Monte Carlo blue `#2a78d6`, RSS orange `#eb6834`, worst case green `#1baf7a`, requirement near-black.
- `ax.spines[["top", "right"]].set_visible(False)` removes ink that carries no data. `\n` starts a new line in a string.
- `fig.savefig("plots/name.png", dpi=150, bbox_inches="tight")`, then `plt.show()`. The pop-up window is not the saved file.
- `plots/` is generated output, so it's ignored. README images get committed separately in Step 8.
- Bars: `ax.barh(positions ± bar_height / 2, values, height=bar_height)`, `np.arange(n)` for slots, `ax.set_yticks(positions, labels=names)`, `ax.invert_yaxis()`, `ax.bar_label(bars, fmt="%.1f%%", padding=3)`, `ax.margins(x=0.1)`. Sort by what the reader needs to see first.
- Plot functions take data and return `fig, ax`; they don't load, simulate, save or show. A module holds only imports and functions.
- Optional parameter: `ax=None` with `if ax is None:` lets a function draw on a plot it's given. `if show_legend:` runs a line only when a flag is true.
- `plt.subplots(2, 1, sharex=True, sharey=True)` gives stacked plots on the same scales; `axes[0]` is the top one. `fig.suptitle(title)` titles the sheet. Comparing plots with different scales misleads.
- Once one argument is passed by name, all later ones must be. An argument should be a value (`ax=axes[0]`), never a `set_...()` call, which returns `None`.
- Code after a `return` never runs (VS Code dims it). After copying an example, check every line, label and unit ("kg" on a % chart).
- Look at the saved image every time. A script can run without errors and still produce a wrong plot.
- `rm <file>` deletes permanently.

### Notebooks
- A notebook (`.ipynb`) is cells: code cells show their output underneath; Markdown cells hold notes. Like a calc package or a MATLAB live script.
- Scripts and modules hold the reusable, tested code; notebooks import it for exploring, what-ifs and explaining an analysis. Never copy a function into a notebook.
- Setup: VS Code's Jupyter extension, `ipykernel` in `requirements.txt` (then `pip install -r requirements.txt`), the `.venv` kernel, and `"jupyter.notebookFileRoot": "${workspaceFolder}"` so it runs from the project folder.
- Shift + Enter runs a cell. The last line of a cell is displayed automatically (`df` shows a table). Plots appear without `plt.show()`.
- `df.loc[row, ["col1", "col2"]] = value` changes cells. A misspelled column name silently creates a new column.
- Hidden state: the kernel remembers values from every cell run, in the order actually run. Restart → Run All before trusting, sharing or committing; execution numbers 1, 2, 3 in order show a clean run.
- Give each name one meaning per notebook; don't overwrite the original arrays with what-if values.

## Next step

**Step 8: make it a real project.** Turn the code into an installable package (`pyproject.toml`, `pip install -e .`), add a command-line interface, write a README with the plots, and tidy the git history.
