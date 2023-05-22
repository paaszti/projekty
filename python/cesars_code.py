def CC(keys, words):
    list=['Your encrypted word is: ']
    lengh=len(word)
    for i in range(0, lengh):
        z=chr((int(ord(word[i]))+key))
        list.append(z)
    print("".join(list))
key=int(input('Key of Cesars Shift: '))
word=input('Enter the word to encrypted: ')
CC(key, word)


