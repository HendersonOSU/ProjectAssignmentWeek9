def main():
    filename = input("File name: ")
    total, count = 0, 0
    with open(filename, 'r') as f:
        for line in f:
            for num in line.strip().split():
                total += float(num)
                count += 1
    print('\n Average is ' + str(total / count))


main()
