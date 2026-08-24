import argparse
from dataclasses import dataclass

from .configure import *
from .files import *
from .planner import *

logger = logging.getLogger(__name__)


@dataclass
class Statistics:
    files_moved: int = 0
    directories_created: int = 0
    extensions_found: int = 0
    types_found: int = 0

    def count_moved_files(self, entire_file_list: list):
        self.files_moved += len(entire_file_list)

    def count_created_directories(self, directories_list: list):
        self.directories_created += len(directories_list)

    def count_extensions_found(self, extensions_list: list):
        self.extensions_found += len(extensions_list)

    def count_types_found(self, types_list: list):
        self.types_found += len(types_list)


def create_parser() -> argparse.ArgumentParser:
    created_parser = argparse.ArgumentParser()
    created_parser.add_argument(
        "-d", "--directory", help="directory to organize or list", type=str
    )
    created_parser.add_argument(
        "command",
        help="command to execute",
        choices=["organize", "suggest", "configure"],
    )
    created_parser.add_argument(
        "--category",
        help="category for how to organize the files",
        choices=["extensions", "types", "date"],
    )
    created_parser.add_argument(
        "--showoff", help="adds timestamps for ASMR file moving", action="store_true"
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


def print_plan(plan: dict[str, list], showoff: bool = False) -> None:
    print("suggested plan of organizing:")
    for plan_category, plan_file_list in plan.items():
        if showoff:
            time.sleep(1)
        print(f"---- category: {plan_category} ----")
        for file in plan_file_list:
            if showoff:
                time.sleep(0.2)
            print(f"-> {file}")
        print()


if __name__ == "__main__":
    # setup
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    parser = create_parser()
    args = parser.parse_args()
    this_session_stats = Statistics()
    # verbose mode
    if args.verbose or args.dry_run:
        logger.setLevel(logging.DEBUG)
        logger.debug("logging level set to debug")
        logger.debug(args)

    if args.command == "configure":
        configure_cli()

    # listing files in user directory
    user_file_list = list_files_in_directory(directory=args.directory)

    # mapping plan based on category
    mapped_plan = {}
    if args.category == "extensions":
        mapped_plan = map_files_to_extensions(
            raw_file_list=user_file_list, verbose_mode=args.verbose
        )
    if args.category == "types":
        mapped_plan = map_files_to_file_types(
            raw_file_list=user_file_list, verbose_mode=args.verbose
        )
    if args.category == "date":
        files_with_dates_list = [
            map_file_to_date(args.directory + "/" + file) for file in user_file_list
        ]
        mapped_plan = map_files_to_dates(
            raw_file_list=files_with_dates_list, verbose_mode=args.verbose
        )
    if args.command == "organize":
        print_plan(plan=mapped_plan, showoff=args.showoff)
        if input("Do you wish to apply the suggested plan? y/n: ") == "y":
            logger.debug("categories list sent to directories creator")
            create_directories_for_categories(
                categories=list_categories_from_plan(mapped_plan),
                directory=args.directory,
                verbose_mode=args.verbose,
                dry_run=args.dry_run,
                showoff=args.showoff,
            )
            # Statistics on amount of extensions and types found, dirs made
            if args.category == "types":
                this_session_stats.count_types_found(
                    list(list_categories_from_plan(mapped_plan))
                )
            this_session_stats.count_extensions_found(
                list(list_extensions(user_file_list))
            )
            this_session_stats.count_created_directories(
                list(list_categories_from_plan(mapped_plan))
            )

            for category, file_list in mapped_plan.items():
                logger.debug(
                    f"file list sent for category: ' {category} ' for organizing."
                )
                # Statistics on amount of files moved
                this_session_stats.count_moved_files(file_list)
                move_files_to_category_dir(
                    file_list=file_list,
                    category=category,
                    directory=args.directory,
                    verbose_mode=args.verbose,
                    dry_run=args.dry_run,
                    showoff=args.showoff,
                )
            logger.info("the files have been successfully organized")
            logger.info(
                f"statistics: {this_session_stats.files_moved} total moved files"
            )
            logger.info(
                f"statistics: {this_session_stats.directories_created} total directories created"
            )
            logger.info(
                f"statistics: {this_session_stats.extensions_found} total extensions found"
            )
            if args.category == "types":
                logger.info(
                    f"statistics: {this_session_stats.types_found} total types found"
                )
        else:
            logger.info("Files organizing has been terminated. No changes will be made")
    if args.command == "suggest":
        print_plan(plan=mapped_plan, showoff=args.showoff)
