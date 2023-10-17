fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:
        # if the key is not there the count is  zero
        oldcount = di.get(w,0)
        print(w,'old',oldcount)
        newcount = oldcount + 1
        di[w] = newcount

        print(w,'new',newcount)

print(di)
