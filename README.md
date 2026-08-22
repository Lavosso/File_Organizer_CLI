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
   - asks user if to execute the plan
   - y/n : executes the plan / finishes without making changes

#### Features
1. --verbose flag makes all scripts change logging level to debug
2. program checks if a folder with category name already exists, terminates if so 
## Quality control

`ruff check .`

`ruff format .`

`mypy src`

`pytest -q -s`

## Concept

user → **PARSER (cli)** → folder path

folder path → **FOLDER READER (files)** → file list

file list → **CATEGORY DATA READER (planner)** → file categories list

file list + file categories list → **MAPPER (planner)** → organizer plan

organizer plan → **CONSOLE I/O (cli)** → confirm

file categories list + confirm → **DIRECTORY CREATOR (files)** → folder creation

organizer plan + confirm → **FILE MOVER (files)** → organized files 


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

-[ ] add more testing

-[x] add logging

-[ ] add other categories of grouping (date and file type)

-[ ] add --dry-run

#### COSMETICS
-[ ] add "showoff mode" with timestamps between moving

-[ ] add console summary

-[ ] add HTML reporting
