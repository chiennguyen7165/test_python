def ex4(chuoi):
    chuoiAscii = ""
    for item in chuoi:
        chuoiAscii += str(ord(item))
    return chuoiAscii

def main():
    vao = input("nhap chuoi: ")
    r = ex4(vao)
    print(r)

if __name__ == "__main__":
    main()