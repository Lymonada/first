import sys

def most_common_word():
    """Takes in txt file and since one line and one word, it will interpret each line
    and check which word appear the most.
    No variables are taken. txt file is taken.
    E.g., if the file has the following contents,
    apple
    banna
    apple
    peach
    It will return 'apple appears 2 times' """
    with open(sys.argv[1]) as file:
        lines = [x.strip() for x in file.readlines()]
        word_count = {}
        for word in lines:
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1

        max_count = lines[0]
        for w in word_count:
            if word_count[w] > word_count[max_count]:
                max_count = w

        return f"{max_count} appears {word_count[max_count]} times"

print(most_common_word())