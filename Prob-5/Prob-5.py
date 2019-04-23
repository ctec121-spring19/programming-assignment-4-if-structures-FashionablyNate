# Module 3
#   Programming Assignment 4
#     Prob-5.py

# Nathan Spelts

def main():
    try:
        x = eval(1)
        print()
        print("x:", x)
        print()
    except TypeError:
        print()
        print("variable assignment is a statement, not an expression")
        print()
    except:
        print()
        print("something went wrong")
        print()


main()