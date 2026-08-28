import argparse
import datetime
import logging
import sys
import time
from dataclasses import dataclass
from pathlib import Path

from src import configure, files, html_reporting, planner

logger = logging.getLogger(__name__)


@dataclass
class Statistics:
    files_per_category: dict[str, int]
    files_moved: int = 0
    directories_created: int = 0
    extensions_found: int = 0
    types_found: int = 0
    def add_file_count_per_category(self, file_count: int, files_category: str):
        self.files_per_category[files_category] = file_count


def create_parser() -> argparse.ArgumentParser:
    created_parser = argparse.ArgumentParser()
    created_parser.add_argument(
        "-d", "--directory", help="directory to organize or list", type=Path
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
        "--html",
        help="makes the program make an HTML report",
        action="store_true",
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


def main():
    # setup
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    parser = create_parser()
    args = parser.parse_args()
    this_session_stats = Statistics({})

    # verbose mode
    if args.verbose or args.dry_run:
        logger.setLevel(logging.DEBUG)
        logger.debug("logging level set to debug")
        logger.debug(args)

    if args.command == "configure":
        configure.configure_cli()

    # listing files in user directory
    user_file_list = files.list_files_in_directory(directory=args.directory)
    if not user_file_list:
        logger.warning(
            "no user files found  - no organizing can be done - terminating program"
        )
        sys.exit(0)
    # mapping plan based on category
    mapped_plan = {}
    if args.category == "extensions":
        mapped_plan = planner.map_files_to_extensions(
            raw_file_list=user_file_list, verbose_mode=args.verbose
        )
    if args.category == "types":
        mapped_plan = planner.map_files_to_file_types(
            raw_file_list=user_file_list, verbose_mode=args.verbose
        )
    if args.category == "date":
        files_with_dates_list = [
            files.map_file_to_date(args.directory / file) for file in user_file_list
        ]
        mapped_plan = planner.map_files_to_dates(
            raw_file_list=files_with_dates_list, verbose_mode=args.verbose
        )
    if args.command == "organize":
        print_plan(plan=mapped_plan, showoff=args.showoff)
        if input("Do you wish to apply the suggested plan? y/n: ") == "y":
            logger.debug("categories list sent to directories creator")
            files.create_directories_for_categories(
                categories=planner.list_categories_from_plan(mapped_plan),
                directory=args.directory,
                verbose_mode=args.verbose,
                dry_run=args.dry_run,
                showoff=args.showoff,
            )
            # Statistics on amount of extensions and types found, dirs made
            if args.category == "types":
                this_session_stats.types_found = len(list(planner.list_categories_from_plan(mapped_plan)))

            this_session_stats.extensions_found = len(list(planner.list_extensions(user_file_list)))
            this_session_stats.directories_created = len(list(planner.list_categories_from_plan(mapped_plan)))

            for category, file_list in mapped_plan.items():
                logger.debug(
                    f"file list sent for category: ' {category} ' for organizing."
                )
                # Statistics on amount of files moved
                this_session_stats.files_moved += len(file_list)
                # Statistics on files per category moved
                this_session_stats.add_file_count_per_category(len(file_list), category)
                files.move_files_to_category_dir(
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
            if args.html or (
                input("Do you wish to have an HTML report made? y/n: ") == "y"
            ):
                organizing_title = f"Report for: {args.directory}, date: {datetime.datetime.now(tz=datetime.UTC).date()}"
                organizing_data: dict = {
                    # General: total files moved, total directories created, total extensions found, total types found
                    "Overall statistics": [
                        f"total files moved: {this_session_stats.files_moved}",
                        f"total directories created: {this_session_stats.directories_created}",
                        f"total different extensions found: {this_session_stats.extensions_found}",
                    ],
                    # Data per category
                    "Total files per category": [
                        f"{files_category} : {files_count}"
                        for files_category, files_count in this_session_stats.files_per_category.items()
                    ],
                }
                if args.category == "types":
                    organizing_data["Overall statistics"].append(
                        f"total types of data found: {this_session_stats.types_found}"
                    )
                # Drawing the overall map onto Markdown
                organizing_data["Detailed map of organizing : "] = []

                for file_category, file_list in mapped_plan.items():
                    category_string = f"' {file_category} ' category file list : \n"
                    for file in file_list:
                        category_string += f"    - {file}\n"
                    organizing_data["Detailed map of organizing : "].append(
                        category_string
                    )

                organizing_data_md = html_reporting.rewrite_data_in_markdown(
                    organizing_data, organizing_title
                )
                organizing_data_html = html_reporting.rewrite_markdown_into_html(
                    organizing_data_md
                )

                with open(args.directory / "report.html", "w", encoding="utf-8") as f:
                    f.write(organizing_data_html)

                logger.info(
                    "The HTML file has been made and can be found in the organized directory folder"
                )

        else:
            logger.info("Files organizing has been terminated. No changes will be made")
    if args.command == "suggest":
        print_plan(plan=mapped_plan, showoff=args.showoff)

if __name__ == "__main__":
    main()
