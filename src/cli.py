import argparse

from files import *
from planner import *

logger = logging.getLogger(__name__)


def create_parser() -> argparse.ArgumentParser:
    created_parser = argparse.ArgumentParser()
    created_parser.add_argument(
        "-d", "--directory", help="directory to organize or list", type=str
    )
    created_parser.add_argument(
        "command", help="command to execute", choices=["organize", "suggest"]
    )
    created_parser.add_argument(
        "--category",
        help="category for how to organize the files",
        choices=["extensions", "types"],
    )
    created_parser.add_argument(
        "--verbose",
        help="verbose mode - logging level set to debug",
        action="store_true",
    )
    created_parser.add_argument(
        "--dry-run",
        help="dry run mode - logging level set to debug, no changes will be made",
        action="store_true",
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
    # setup
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    parser = create_parser()
    args = parser.parse_args()

    # verbose mode
    if args.verbose or args.dry_run:
        logger.setLevel(logging.DEBUG)
        logger.debug("logging level set to debug")
        logger.debug(args)

    # listing files in user directory
    user_file_list = list_files_in_directory(directory=args.directory)

    # mapping plan based on category
    mapped_plan = {}
    if args.category == "extensions":
        mapped_plan = map_files_to_extensions(
            file_list=user_file_list, verbose_mode=args.verbose
        )
    if args.category == "types":
        mapped_plan = map_files_to_file_types(raw_file_list=user_file_list)

    if args.command == "organize":
        print_plan(mapped_plan)
        if input("Do you wish to apply the suggested plan? y/n: ") == "y":
            logger.debug("extensions list sent to directories creator")
            create_directories_for_categories(
                categories=list_categories(mapped_plan),
                directory=args.directory,
                verbose_mode=args.verbose,
                dry_run=args.dry_run,
            )
            for category, file_list in mapped_plan.items():
                logger.debug(
                    f"file list sent for category: ' {category} ' for organizing."
                )
                move_files_to_category_dir(
                    file_list=file_list,
                    category=category,
                    directory=args.directory,
                    verbose_mode=args.verbose,
                    dry_run=args.dry_run,
                )
            logger.info("the files have been successfully organized")
        else:
            logger.info("Files organizing has been terminated. No changes will be made")
    if args.command == "suggest":
        print_plan(mapped_plan)
