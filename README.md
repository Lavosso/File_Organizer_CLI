# File Organizer CLI
Python file organizer - organize messy folders through grouping by date, extension or file type.

## Installation

```commandline
mkdir File_Organizer_CLI
cd File_Organizer_CLI
git clone https://github.com/Lavosso/File_Organizer_CLI.git
py -m venv .venv
.venv\Scripts\Activate.ps1 
pip install requests
```

## Launching and features

#### Lauching
1. src/cli.py suggest -d (directory) 
   - returns suggested organizing plan for the directory
2. src/cli.py organize -d (directory)
   - prints suggested organizing plan
   - asks user for confirmation to execute the plan
   - y/n : executes the plan / finishes without making changes

#### Features
1. DEBUG: --verbose flag sets logging level to debug.
2. SAFETY: program checks if a folder with category
name already exists, and if so does happen,
terminates the program before any changes to the files.
3. CONTROL: --dry-run flag makes the script go 
through every step of standard organizing, 
without making any changes to the actual files.
## Quality control

`ruff check .`

`ruff format .`

`mypy src`

`pytest -q -s`

## Concept

user → **_PARSER (cli)_** → folder path

folder path → **_FOLDER READER (files)_** → file list

file list → **_CATEGORY DATA READER (planner)_** → file categories list

file list + file categories list → **_MAPPER (planner)_** → organizer plan

organizer plan → **_CONSOLE I/O (cli)_** → confirm

file categories list + confirm → **_DIRECTORY CREATOR (files)_** → folder creation

organizer plan + confirm → **_FILE MOVER (files)_** → organized files 


## To-Do

#### FUNDAMENTALS (0.1)
-[x] FILE MAPPING
  -  IN:  list of file names, set of extensions
  -  OUT: dict: {extension: (list of files)}

-[x] CATEGORY DATA READER
  - IN: list of file names
  - OUT: set of extensions

-[x] CONSOLE I/O
    - OUT: readable organizing plan
    - IN: confirmation

-[x] FOLDER READER
  - IN: directory path
  - OUT: list of file names in directory / list of directories in directory

-[x] PARSER (takes path of directory to organize)

-[x] DIRECTORY CREATOR (takes extension list and path, creates directories in path)

-[x] FILES MOVER (takes directory and list of files to move)

#### FUNCTIONALITIES
-[x] add verification to border situations, such as dir replacing

-[x] add more testing

-[x] add logging

-[ ] add another category of grouping (file type)

-[x] add --dry-run

#### COSMETICS
-[ ] add "showoff mode" with timestamps between moving

-[ ] add console summary

-[ ] add grouping by date of file creation

-[ ] add HTML reporting
