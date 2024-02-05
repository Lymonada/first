list = input('Enter a list of strings: ')
new_list = []

def shortened(list):
    list = list.replace('’', '').replace('[','').replace(']','').replace(' ','').split(',')
    for word in list:
        if len(word) > 3:
            new_list.append(word[-3:])

    return new_list

print(shortened(list))
