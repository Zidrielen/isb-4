import argparse
import logging

from utils.file_manager import FileManager

logging.getLogger().setLevel(logging.INFO)


def console_menu() -> None:
    """
    A function that can iterate over the card number
    by its hash, check the correctness of the card
    number and visualize the file with the
    enumeration statistics
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-set",
        "--settings",
        type=str,
        help="Using your own settings file"
    )
    parser.add_argument(
        "-sts",
        "--statistics",
        action="store_true",
        help="Saves statistics to a file"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-enu",
        "--enumeration",
        type=int,
        help="Entering the number of processes for"
             "selecting the card number by its hash"
    )
    group.add_argument(
        "-luh",
        "--luhn",
        action="store_true",
        help="Checking the correctness of"
             "the received card number"
    )
    group.add_argument(
        "-vis",
        "--visualization",
        action="store_true",
        help="Visualizes data from a"
             "file with statistics"
    )
    args = parser.parse_args()
    file_manager = FileManager(args.settings) if args.settings else FileManager()
    