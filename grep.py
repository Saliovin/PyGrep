import re
import os
import argparse


def ini_arguments():
    """
    Initialize and parse arguments.

    :return: Parsed arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("expression", help="Expression to look for.")
    parser.add_argument("file_pattern", help="file name.")
    parser.add_argument("directory", help="Directory to look into.")
    parser.add_argument("-l", "--line_number", action="store_true", help="Print the line number.")
    parser.add_argument("-r", "--recursive", action="store_true", help="Go through subdirectories.")
    parser.add_argument("-i", "--ignore_case", action="store_const", const=re.IGNORECASE, default=0, help="Ignore case.")
    parser.add_argument("-I", "--invert_match", action="store_true", help="Look for lines not containing the expression.")
    parser.add_argument("-c", "--count", action="store_true", help="Print the number of line occurrences.")
    return parser.parse_args()


def grep(regex, pattern, directory, recursive):
    file_list = os.listdir(directory)

    for file in file_list:
        file_path = f"{directory}/{file}"

        if os.path.isfile(file_path):
            if file_pattern.search(file):
                search_file(file_path, regex)
        elif recursive:
            grep(regex, pattern, file_path, recursive)


def search_file(file_path, regex):
    with open(file_path, 'r', encoding="utf8") as file:
        print(file_path)
        count = 0
        str_list = file.read().splitlines()

        for line_i, line in enumerate(str_list):
            if regex.search(line, re.IGNORECASE):
                count += 1

                if args.line_number:
                    print(f"\t{line_i}", end="")
                print(f"\t{line}")

        if args.count:
            print(f"\tCount: {count}")


if __name__ == "__main__":
    args = ini_arguments()
    expression = re.compile(args.expression, args.ignore_case)
    file_pattern = re.compile(args.file_pattern)

    grep(expression, file_pattern, args.directory, args.recursive)
