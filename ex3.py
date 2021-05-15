def ex3(tupA, tupB):
    answer = ""
    if set(tupB).issubset(tupA) == True:
        answer = "YES"
    else:
        answer = "NO"
    return answer

def main():
    dayA = tuple(input("Nhap phan tu tuple A (canh nhau boi dau cach): ").split(" "))
    dayB = tuple(input("Nhap phan tu tuple B (cach nhau boi dau cach): ").split(" "))
    a = ex3(dayA, dayB)
    print(a)

if __name__ == "__main__":
    main()