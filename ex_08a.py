han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    print('Line:',line)
    wds = line.split()
    print('Words:',wds)
    if line == '' :
        # print('Skip Blank')
        print('Skip Blank')
        continue
    if wds[0] != 'From' :
        # print ('Ignore')
        print('Ignore')
        continue
    print(wds[2])
