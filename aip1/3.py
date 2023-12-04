import sys


cnt, ox, fir, sec = int(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4]

print(cnt, ox, fir, sec)

ox_list = []

with open (ox, 'rt', encoding='UTF8') as file:
    lines = [x.strip() for x in file.readlines()]
    for line in lines:
        ox_list.append(line)

def getallword(file_name, already):
    """
    Retrieve and count unique words in a text file excluding specified words
    file_name is a string and already is a list.
    Return a list containing tuples of words and their respective 
    counts, sorted in descending order based on their frequency.
    The list contains tuples with the word as the first element and its count as the second element.
    Only words not present in the 'already' list and having a length greater than or equal to 6 characters are considered.
    Any punctuation characters are removed before counting.
    E.g., if the file has following contents, 
    apples
    bananas
    apples
    peaches
    apples
    bananas
    bananas
    bananas
    and the list of words that should be excluded has apples, it will return [('bananas', 4), ('peaches', 1)]"""
    words = {}
    with open(file_name, 'rt', encoding='UTF8') as file:
        lines = [x.strip() for x in file.readlines()]
        for line in lines:
            refined_line = line.replace(',',' ').replace("'",' ').replace('"',' ').replace('.',' ').replace(';',' ').replace(':',' ').replace('`',' ').replace('?',' ').replace('(',' ').replace(')',' ').replace('-',' ').replace('“', ' ').replace('™', ' ').replace('’', ' ')
            for word in refined_line.split():
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1
                if word in ox_list or word in already or len(word) < 6:
                    del words[word] 
        sorted_dict = sorted(words.items(), key = lambda item: item[1], reverse = True)
        return sorted_dict[:cnt]

firWords = getallword(fir, [])
alreadyWord = [x[0] for x in firWords]
secWords = getallword(sec, alreadyWord)

print(f' {fir} : {firWords}, {sec} : {secWords}')