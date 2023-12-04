mylist = input('Enter a list of words: ')


def function(mylist):
    dict ={}
    new_list =[]
    mylist = mylist.replace('’','').replace(' ','').replace('[','').replace(']','').split(',')
    for word in mylist:
        if word not in dict:
            dict[word] = 1
        elif word in dict:
            dict[word] += 1
        if dict[word] == 3:
            new_list.append(word)
            
    return new_list

print(function(mylist))
        

    
    


