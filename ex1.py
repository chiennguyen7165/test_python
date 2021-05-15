def ex1(n):
    n1 = 0
    n2 = 1
    count = 0
    while count < n:
        print(n1)
        temp = n1 + n2
        n1 = n2 
        n2 = temp
        count += 1

def main():
    doDai = int(input("Length of the sequence (int): "))
    ex1(doDai)

if __name__ == "__main__":
    main()

