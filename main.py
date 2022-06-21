''' Text correction program. If word is not from dictionary, replace it.
https://www.geeksforgeeks.org/python-program-for-longest-common-subsequence/
https://www.geeksforgeeks.org/edit-distance-dp-5/?ref=gcse
'''

import string


def lcs(word1, word2):
    """ Find the Longest Common Subsequence

    :param word1: word from the file
    :param word2: word from the dictionary
    :return: length of the longest common subsequence
    """
    m = len(word1)
    n = len(word2)

    length = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                length[i][j] = 0
            elif word1[i - 1] == word2[j - 1]:
                length[i][j] = length[i - 1][j - 1] + 1
            else:
                length[i][j] = max(length[i - 1][j], length[i][j - 1])

    return length[m][n]


def edit_dist(word1, word2):
    """ How many operations are needed to change one word to another.
    The most suitable word is with the smallest possible operations, ie the smallest edit distance.

    :param word1: word from the file
    :param word2: word from the dictionary
    :return: the smallest count of needed operations
    """
    m = len(word1)
    n = len(word2)

    distance = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty
            if i == 0:
                distance[i][j] = j

            # If second string is empty
            elif j == 0:
                distance[i][j] = i

            elif word1[i - 1] == word2[j - 1]:
                distance[i][j] = distance[i - 1][j - 1]

            else:
                distance[i][j] = 1 + min(distance[i][j - 1],  # Insert
                                         distance[i - 1][j],  # Remove
                                         distance[i - 1][j - 1])  # Replace

    return distance[m][n]


def first_variation(word, dictionary_list):
    """ Go through the words in the dictionary and find out the Longest Common Subsequence.
    If the Longest Common Subsequence is the same as the word length, return the current word from the dictionary.
    Otherwise, return with the best Longest Common Subsequence.

    :param word: word to correct
    :param dictionary_list: acceptable words for a file in list
    :return: word with  best Longest Common Subsequence
    """
    change_word = ""
    best_length = 0
    for dic_word in dictionary_list:
        length = lcs((word.strip(string.punctuation)).lower(), dic_word)
        if length == len(word):
            return dic_word
        if best_length < length:
            change_word = dic_word
            best_length = length
    return change_word


def second_variation(word, dictionary_list):
    """ Go through the words in the dictionary and find out the edit distance.
    If the number of operations required is 0, the word is in the dictionary.
    Otherwise, return the word from the dictionary that requires the least operations.

    :param word: word to correct
    :param dictionary_list: acceptable words for a file in list
    :return: the word that needs the least number of operations
    """
    change_word = ""
    best_length = 100
    for dic_word in dictionary_list:
        file_word = (word.strip(string.punctuation)).lower()
        length = edit_dist(file_word.lower(), dic_word)
        if length == 0:
            change_word = word
            break
        if best_length > length:
            change_word = dic_word
            best_length = length
    return change_word


def main(file, dictionary):
    """ Insert the appropriate (corrected) word into the new corrected file.

    :param file: wrong file
    :param dictionary: acceptable words for a file
    """
    dictionary_list = []
    for line in dictionary:
        dictionary_list.append(line.rstrip('\n'))
    new_file = open("resources/vystup6.txt", "w")
    for line in file:

        for word in line.split():
            change_word = word
            if len(word) > 1:
                change_word = first_variation(word, dictionary_list)
                # change_word = second_variation(word, dictionary_list)

            new_file.write(change_word + " ")


if __name__ == '__main__':
    main(open("resources/file.txt", "r", encoding='utf-8-sig'),
         open("resources/slovnik.txt", "r", encoding='utf-8-sig'))
