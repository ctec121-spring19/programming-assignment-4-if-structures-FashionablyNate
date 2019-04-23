# Module 3
#   Programming Assignment 4
#     Prob-3.py

# Nathan Spelts

def letterGrade(score):
    # your code here
    if score >= 5:
        grade = "A"
    if score < 5:
        grade = "B"
    if score < 4:
        grade = "C"
    if score < 3:
        grade = "D"
    if score < 2:
        grade = "F"

    return grade

def unitTest():
    # your test code here
    print()
    print("With a score of", 0, "your letter grade is an", letterGrade(0))
    print("With a score of", 1, "your letter grade is an", letterGrade(1))
    print("With a score of", 2, "your letter grade is a", letterGrade(2))
    print("With a score of", 3, "your letter grade is a", letterGrade(3))
    print("With a score of", 4, "your letter grade is a", letterGrade(4))
    print("With a score of", 5, "your letter grade is an", letterGrade(5))
    print()
if __name__ == "__main__":
    unitTest()