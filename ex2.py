def ex2(n):
    r = 0
    for item in n:
        r = r*2 + int(item)
    return r


def main():
    bi = input("A binary string: ")
    de = ex2(bi)
    print(de)

if __name__ == "__main__":
    main()
