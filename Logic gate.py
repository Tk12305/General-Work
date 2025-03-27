def menu():
    print("1.AND GATE/n2.OR GATE/n3.NOT GATE")
    choice = int(input("Enter 1,2 or 3:"))
    if choice == 1:
        logic_and()
    elif choice == 2:
        logic_or()
    elif choice == 3:
        logic_not()
    else:
        print("incorrect number")


def logic_and():
    a = int(input("Enter 1 or 0:"))
    b = int(input("Enter 1 or 0:"))
    if a == 1 and b == 1:
        print("1")
    elif a == 1 and b == 0:
        print("0")
    elif a == 0 and b == 1:
        print("0")
    elif a == 0 and b == 0:
        print("0")
    else:
        print("incorrect number")


def logic_or():
    a = int(input("Enter 1 or 0:"))
    b = int(input("Enter 1 or 0:"))
    if a == 1 or b == 1:
        print("1")
    elif a == 1 or b == 0:
        print("0")
    elif a == 0 or b == 1:
        print("0")
    elif a == 0 or b == 0:
        print("0")
    else:
        print("incorrect number")


def logic_not():
    a = int(input("Enter 1 or 0:"))
    if a == 1:
        print("0")
    elif a == 0:
        print("1")
    else:
        print("incorrect number")


menu()
