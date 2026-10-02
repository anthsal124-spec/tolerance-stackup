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

## Roadmap

- [ ] **Step 0: Setup**
  - [x] 0a: Terminal basics, check what's installed
  - [x] 0b: Install Python 3.14 and VS Code, turn off Anaconda auto-start
  - [ ] 0c: Project folder, virtual environment, install packages *(folder and `.venv` created)*
  - [ ] 0d: git, first commit *(add `.claude/` to `.gitignore`: it holds Claude's local settings and the venv reminder hook)*
- [ ] Step 1: Just enough Python
- [ ] Step 2: NumPy basics
- [ ] Step 3: Worst-case stack (+ first test against a hand calc)
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
- **Virtual environment (`.venv`)**: a private set of packages for one project, so other projects can't break it. Activating it puts `.venv/bin` at the front of the PATH.
- **requirements.txt**: the project's bill of materials. `pip install -r requirements.txt` rebuilds the environment from it.

## Next step

Continue 0c from step 3: activate the virtual environment, create `requirements.txt` in VS Code, `pip install -r requirements.txt`, then verify with `pip list` and the `ready` test.
