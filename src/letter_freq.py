import argparse
import matplotlib.pyplot as plt
import utility


def parse_command_line() -> argparse.Namespace:
    """
    Parse the command line arguments using argparse
    :return: the parsed command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        help='a comma separated value unigram file')
    parser.add_argument('-o', "--output",
                        help='display letter frequencies to standard output', action='store_true')
    parser.add_argument('-p', "--plot",
                        help='plot letter frequencies using matplotlib', action='store_true')
    return parser.parse_args()


def output(alphabet: dict) -> None:
    """
    The function prints each letter of the alphabet and the amount of times
    it appears in the specified file.
    :param alphabet: a dictionary containing all the letters of the alphabet
    :return: None
    """
    for letter, count in alphabet.items():
        print(letter + ": " + str(count))


def plot(filename: str, alphabet: dict) -> None:
    """
    The function uses the values and keys of the alphabet dictionary
    to create a histogram plot. The letters are on the x-axis while the
    frequency is on the y-axis.
    :param filename: the name of the specified file
    :param alphabet: a dictionary containing all the letters of the alphabet
    :return: None
    """
    plt.title("Letter Frequencies: " + filename)
    plt.xlabel("Letters")
    plt.ylabel("Frequency")
    letters = list(alphabet.keys())
    counts = list(alphabet.values())
    plt.bar(letters, counts)
    plt.show()


def main():
    """
    The function creates the alphabet dictionary and count the frequency
    for each letter. The total count for all letters is also stored. Using
    the two counts, the alphabet count is divided by total count to get the
    frequency which is stored as a value in the alphabet dictionary. If the command
    line asks for output, it will run the output function and if it asks for
    plot, it will run the plot function.
    :return: None
    """
    alphabet = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
                "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
                "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
                "y": 0, "z": 0}
    args = parse_command_line()
    filename = args.filename
    line_list = utility.check_file(filename)
    total_count = 0
    for line in line_list:
        for letter in line[0]:
            alphabet[letter] += int(line[2])
            total_count += int(line[2])
    for letter in alphabet:
        alphabet[letter] /= total_count
    if args.output:
        output(alphabet)
    if args.plot:
        plot(filename, alphabet)


if __name__ == '__main__':
    main()