def printAll(seq):

    if seq:
        printAll(seq[1:])
        print(seq[0])
        print("sequence:",seq)


printAll([1, 2, 3, 4, 5, 6])
