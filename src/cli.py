import argparse

import src.files
import src.planner


def create_parser() -> argparse.ArgumentParser:
    created_parser = argparse.ArgumentParser()
    created_parser.add_argument(
        "-d", "--directory", help="directory to organize or list", type=str
    )
    created_parser.add_argument(
        "command", help="command to execute", choices=["organize", "suggest"]
    )
    return created_parser


def print_plan(plan: dict[str, list]):
    print("suggested plan of organizing:")
    for category, file_list in plan.items():
        print(f"---- category: {category} ----")
        for file in file_list:
            print(f"-> {file}")
        print()


parser = create_parser()
args = parser.parse_args()
user_file_list = src.files.list_files_in_directory(directory=args.directory)
extension_list = src.planner.list_extensions(user_file_list)
mapped_plan = src.planner.map_files_to_categories(user_file_list, extension_list)
if args.command == "organize":
    print_plan(mapped_plan)
if args.command == "suggest":
    print_plan(mapped_plan)
