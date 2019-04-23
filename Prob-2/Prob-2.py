# Module 3
#   Programming Assignment 4
#     Prob-2.py

# Nathan Spelts

'''
Inputs: Asks users their name, how much they make and how many hours they work.
Process: Overtime must be calculated and seperated from regular pay, tax/insurance withholdings must be calculated.
Outputs: The program must tell the user their: name, regular wages, overtime wages, total wages, withholdings, and take home pay.
'''

def main():
    # your code goes here
    # User inputs
    print()
    userName = input("What's your name?: ")
    userPayrate = float(input("How much do you make an hour?: "))
    userHours = int(input("How many hours do you work on average?: "))
    print()
    # Overtime calculations and regular payrate calculations
    overtimeHours = userHours - 40

    if overtimeHours > 0:
        userHours = userHours - overtimeHours
    else:
        overtimeHours = 0

    regWages = userHours * userPayrate
    userOvertime = userPayrate * 1.5
    overtimeWages = overtimeHours * userOvertime
    preTaxPaycheck = regWages + overtimeWages
    # Tax calculations
    taxWithheld = preTaxPaycheck * 0.20
    medicalWithheld = preTaxPaycheck * 0.10
    
    finalPaycheck = preTaxPaycheck - taxWithheld - medicalWithheld
    #Return information
    print()
    print("Name:\t\t\t", userName)
    print()
    print("Regular wages:\t\t", "$", regWages)
    print("Overtime wages:\t\t", "$", overtimeWages)
    print("Total wages:\t\t", "$", preTaxPaycheck)
    print()
    print("Tax withholding:\t", "$", taxWithheld)
    print("Insurance withholding:\t", "$", medicalWithheld)
    print()
    print("Take home pay:\t\t", "$", finalPaycheck)
    print()


main()