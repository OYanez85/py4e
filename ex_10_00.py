fhand = open('mbox-short.txt')
counts = dict()
for line in fhand:
    if line.startswith('From'):
        words = line.split()
        if len(words) >= 6:
            time = words[5]
            hour = time.split(':') [0]


    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0 ) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

for val, key in lst[5] :
    print(key,val)
