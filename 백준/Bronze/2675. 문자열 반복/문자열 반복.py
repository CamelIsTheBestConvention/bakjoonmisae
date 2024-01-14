count = int(input())
wordsplit = []


for i in range(count):
    inputs = input().split()
    incount = int(inputs[0])
    word = inputs[1]
    wordsplit = list(word)
    wordtotal = ''

    for j in range(0, len(wordsplit)):
        for k in range(0, incount):
            wordtotal += wordsplit[j]

    
    # print(inputs, '-',incount,'-',wordsplit,'-',wordtotal)
    print(wordtotal)