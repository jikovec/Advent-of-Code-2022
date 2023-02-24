def main():
    file = open('input.txt', 'r')
    a = 0
    b = 0
    c = []
    for i in file.readlines():
        if i == "\n":
            c.append(a)
            if a > b:
                b = a
            a = 0
        else:
            a += int(i)
    f = sum(sorted(c)[-3:])
    print("1 - " + str(b))
    print("2 - " + str(f))
if __name__ == "__main__":
    main()
