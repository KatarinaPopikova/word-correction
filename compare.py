import string


def split_into_words(file):
    """ Split file into words.

    :param file: file to split
    :return: words
    """
    read_data = file.read()
    return read_data.split()


def compare_files(right_file, compare_file):
    """ Compare 2 files and print the proportion of correct words from the corrected file
     and the original correct file. """
    right_file_words = split_into_words(right_file)
    compare_file_words = split_into_words(compare_file)

    right_words = 0
    for word in range(len(right_file_words)):
        if right_file_words[word].strip(
                string.punctuation).lower() == compare_file_words[word].strip(string.punctuation).lower():
            right_words += 1

    accuracy = right_words / len(right_file_words)
    print('\tTotal Words: %d, right words: %d, accuracy: %f\n' % (len(right_file_words), right_words, accuracy))


if __name__ == '__main__':
    print('Compare original files:')
    compare_files(open("resources/pvstup2.txt", "r", encoding='utf-8-sig'),
                  open("resources/chvstup2.txt", "r", encoding='utf-8-sig'))

    print('Repair file with Longest Common Subsequence:')
    compare_files(open("resources/pvstup2.txt", "r", encoding='utf-8-sig'),
                  open("resources/vystup.txt", "r", encoding='utf-8-sig'))

    print('Repair file with Edit Distance:')
    compare_files(open("resources/pvstup2.txt", "r", encoding='utf-8-sig'),
                  open("resources/vystup2.txt", "r", encoding='utf-8-sig'))

    print('Compare original files:')
    compare_files(open("resources/pvstup.txt", "r", encoding='utf-8-sig'),
                  open("resources/chvstup.txt", "r", encoding='utf-8-sig'))

    print('Repair file with Longest Common Subsequence:')
    compare_files(open("resources/pvstup.txt", "r", encoding='utf-8-sig'),
                  open("resources/vystup3.txt", "r", encoding='utf-8-sig'))

    print('Repair file with Edit Distance:')
    compare_files(open("resources/pvstup.txt", "r", encoding='utf-8-sig'),
                  open("resources/vystup4.txt", "r", encoding='utf-8-sig'))
