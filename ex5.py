def ex5(lstVao):
    for item in lstVao:
        if len(item) == 0:
            lstVao.remove(item)

def main():
    vao = [[1, 2, 3], [], [2, 4]]
    ex5(vao)
    print(vao)

if __name__ == "__main__":
    main()