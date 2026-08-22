# File Organizer CLI
Python file organizer - organize messy folders through grouping by date, extension or file type.

Nothing more here yet :)

## Quality control

`ruff check .`
`ruff format .`
`mypy src`
`pytest -q -s`

## Concept

user → **PARSER** → folder path

folder path → **FOLDER READER** → file list

file list → **CATEGORY DATA READER (planner)** → file categories list

file list + file categories list → **MAPPER (planner)** → organizer plan

organizer plan → **CONSOLE I/O (main)** → confirm

file categories list + confirm → **DIRECTORY CREATOR** → folder creation

organizer plan + confirm → **FILE MOVER** → organized files 


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
-[ ] add "showoff mode" with timestamps between moving

-[ ] add verification to directory creator (user decide what if a folder with name exists)

-[ ] add verification to file mover (user decide if file exists already in directory)

-[ ] add other categories of grouping (date and file type)

-[ ] add testing

-[ ] add --dry-run and check for enough logging

-[ ] add HTML reporting