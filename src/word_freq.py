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
    parser.add_argument('word',
                        help=' a word to display the overall ranking of')
    parser.add_argument('filename',
                        help='a comma separated value unigram file')
    parser.add_argument('-o', "--output",
                        help='display the top OUTPUT (#) ranked words by number of occurrences')
    parser.add_argument('-p', "--plot",
                        help='plot the word rankings from top to bottom based on occurrences', action='store_true')
    return parser.parse_args()


def output(word: str, ranking: str, output_num: str, words: dict) -> None:
    """
    The function states the ranking for a specific word and then prints
    the top ranking words and counts according to the output_num variable.
    :param word: the word to display the overall ranking of
    :param ranking: the ranking of the specified word
    :param output_num: the number that states how many rankings needs to be displayed
    :param words: a dictionary containing all the words in the file
    :return: None
    """
    print(word + " is ranked #" + ranking)
    for word, count in words.items():
        if output_num == str(list(words).index(word)):
            break
        print("# " + str(list(words).index(word) + 1) + ": " + word + " -> " + str(count))


def plot(filename: str, word: str, ranking: str, words: dict) -> None:
    """
    The function uses the value of the words dictionary and its length
    to create a log-log plot. The ranking numbers are on the x-axis while the
    frequency is on the y-axis. The specified word is also marked with a star
    and labeled on the plot.
    :param filename: the name of the specified file
    :param word: the word to display the overall ranking of
    :param ranking: the ranking of the specified word
    :param words: a dictionary containing all the words in the file
    :return: None
    """
    plt.title("Word Frequencies: " + filename.split("/")[1])
    plt.xlabel("Rank of word(\"" + word + "\" is rank " + ranking + ")")
    plt.ylabel("Number of occurrences")
    x = list(range(1, len(words) + 1))
    y = list(words.values())
    plt.loglog(x, y, marker='.')
    plt.plot(float(ranking), float(words.get(word)), marker='*', mec='r')
    plt.annotate(word, (float(ranking), float(words.get(word))))
    plt.show()


def main():
    """
    The function creates the words dictionary and counts the frequency
    for each word. The dictionary is then sorted by the frequency in
    descending order. It the specified word is not in the dictionary,
    it will write an error message saying the word doesn't appear in
    the file. Otherwise, it will calculate the ranking for the specified
    word and run the output and/or plot function based on the argument.
    :return: None
    """
    words = dict()
    args = parse_command_line()
    filename = args.filename
    line_list = utility.check_file(filename)
    for line in line_list:
        if line[0] not in words:
            words[line[0]] = 0
        words[line[0]] += int(line[2])
    words = dict(sorted(words.items(), key=lambda x: x[1], reverse=True))
    if args.word not in words:
        sys.stderr.write("Error: " + args.word + " does not appear in " + filename)
    else:
        ranking = str(list(words).index(args.word) + 1)
        if args.output:
            output(args.word, ranking, args.output, words)
        if args.plot:
            plot(filename, args.word, ranking, words)


if __name__ == '__main__':
    main()
