try:
    rows = int(input("Enter number of rows: "))
    number = 1
    if rows>0:
        for i in range(1, rows+1):
            for j in range(1, i+1):
                print(number, end=" ")
                number += 1
            print()
    else:
        print("invalid")
except ValueError:
    print("invalid")
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
