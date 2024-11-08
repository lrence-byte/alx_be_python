size = int(input("Enter the size of the pattern: "))

while size:
    for i in range (0,size):
        print("", end="*")

        for j in range (1,size):
            print("*",end="")
        print()

    break


