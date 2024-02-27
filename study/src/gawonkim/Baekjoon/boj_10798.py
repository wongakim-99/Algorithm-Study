words = []
length = []
for i in range(5):
    word = input()
    words.append(word)
    length.append(len(word))

tmp = ''
for j in range(max(length)):
    for k in range(5):
        if j < length[k]:
            tmp += words[k][j]
    
print(tmp)