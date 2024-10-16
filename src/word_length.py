import argparse
import sys
import matplotlib.pyplot as plt
import utility


def parse_command_line() -> argparse.Namespace:
    """
    Parse the command line arguments using argparse
    :return: the parsed command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('start',
                        help='the starting year range')
    parser.add_argument('end',
                        help='the ending year range')
    parser.add_argument('filename',
                        help='a comma separated value unigram file')
    parser.add_argument('-o', "--output", action='store_true',
                        help='display the average word lengths over years')
    parser.add_argument('-p', "--plot", action='store_true',
                        help=' plot the average word lengths over years')
    return parser.parse_args()


def output(word_average: dict) -> None:
    """
    The function prints each year in the range and the average word length
    for each year.
    :param word_average: a dictionary containing the average word length for each year
    :return: None
    """
    for year, average in word_average.items():
        print(str(year) + ": " + str(average))


def plot(filename: str, start: str, end: str, word_average: dict) -> None:
    """
    The function uses the key and value of the word_average dictionary
    to create a line plot. The years are on the x-axis while the
    average word length is on the y-axis.
    :param filename: the name of the specified file
    :param start: the starting year range
    :param end: the ending year range
    :param word_average: a dictionary containing the average word length for each year
    :return: None
    """
    plt.title("Average word lengths from " + start + " to " + end + " : " + filename.split("/")[1])
    plt.xlabel("Year")
    plt.ylabel("Average word length")
    x = list(word_average.keys())
    y = list(word_average.values())
    plt.plot(x, y)
    plt.show()


def main():
    """
    The function creates the word_length and word_count dictionaries.
    If the starting year range is greater than the ending year range,
    it will write an error stating that the start year must be less than
    or equal to the end year. Otherwise, with a for loop, it adds all the
    years within the range as keys for both dictionaries. The word_length
    dictionary will have its values as total word length for each year
    while the word_count will have its value as the total word for each year.
    Using the two dictionaries, another dictionary is created to record the
    average word length by dividing the word length by word count for each year.
    Lastly, the function will run the output and/or plot function based on the argument.
    :return: None
    """
    word_length = dict()
    word_count = dict()
    args = parse_command_line()
    filename = args.filename
    if int(args.start) > int(args.end):
        sys.stderr.write("Error: start year must be less than or equal to end year!")
    else:
        for i in range(int(args.start), int(args.end) + 1):
            word_length[i] = 0
            word_count[i] = 0
        line_list = utility.check_file(filename)
        for line in line_list:
            year = int(line[1])
            if year in word_count:
                word_length[year] += len(line[0]) * int(line[2])
                word_count[year] += int(line[2])
        word_average = dict()
        for year, length in word_length.items():
            word_average[int(year)] = length / word_count[year]
        if args.output:
            output(word_average)
        if args.plot:
            plot(filename, args.start, args.end, word_average)


if __name__ == '__main__':
    main()