import argparse

from .files import *
from .planner import *


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
    for plan_category, plan_file_list in plan.items():
        print(f"---- category: {plan_category} ----")
        for file in plan_file_list:
            print(f"-> {file}")
        print()


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()

    user_file_list = list_files_in_directory(directory=args.directory)
    categories_set = list_extensions(user_file_list)

    mapped_plan = map_files_to_categories(user_file_list, categories_set)

    if args.command == "organize":
        print_plan(mapped_plan)
        if input("Do you wish to apply the suggested plan? y/n: ") == "y":
            create_directories_for_categories(categories_set, args.directory)
            for category, file_list in mapped_plan.items():
                move_files_to_category_dir(file_list, args.directory + "/" + category)
            print("the files have been successfully organized")
        else:
            print("Files organizing has been terminated. No changes will be made")
    if args.command == "suggest":
        print_plan(mapped_plan)
