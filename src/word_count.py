import argparse
import sys
import utility


def parse_command_line() -> argparse.Namespace:
    """
    Parse the command line arguments using argparse
    :return: the parsed command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('word',
                        help='a word to display the total occurrences of')
    parser.add_argument('filename',
                        help='a comma separated value unigram file')
    return parser.parse_args()


def main():
    """
    The function counts the number of times that a specific word
    appears in the specified filename. If the count is 0, it will
    write an error message stating that the word did not appear.
    Otherwise, it will print the word and count.
    :return: None
    """
    args = parse_command_line()
    word = args.word
    filename = args.filename
    line_list = utility.check_file(filename)
    count = 0
    for line in line_list:
        if word in line:
            count += int(line[2])
    if count == 0:
        sys.stderr.write("Error: " + word + " does not appear!")
    else:
        print(word + ": " + str(count))


if __name__ == '__main__':
    main()