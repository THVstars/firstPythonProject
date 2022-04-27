import re

COMPANY_NAME = "Vante Inc." # changed the name to one i like.

EMPLOYEES = ["Taehyung", "Yeontan", "Nyubella", "Carolina", "Rosario", "Victoria", "John", "Snowball"] # changed the names to ones i like.

# Welcome message + employee names listed out
print("\nWelcome to the " + COMPANY_NAME + " employee check-in\n")
print("We at " + COMPANY_NAME + " are very proud of our employees: ")
for emp_name in EMPLOYEES:
    print("-- " + emp_name)
print("\n")

# user input section (buggy code)

accept = input("Do you work for " + COMPANY_NAME + "?\n(yes/no): ")

while accept[0].casefold() == "" or accept[0].casefold() != "y" and accept[0].casefold() != "n":
    accept = input("Do you work for " + COMPANY_NAME + "?\n(yes/no): ")  # bonus: keeps asking this question until an acceptable answer is inputted. acceptable answers begin with y or n, so if the input does not begin with either or is empty, it keeps asking.

if accept[0].casefold().replace(" ", "") == "y":  # bonus: checks if the input starts with y and accepts it if it does.
    name = input("What is your name?\nName: ")
    for emp_name in EMPLOYEES:
        if name.casefold().replace(" ", "") == emp_name.casefold():  # bonus: case-insensitive and ignores empty spaces.
            print("Thank you " + emp_name + ", you are now checked in.")
            break
    else:  # only prints out once, after checking every name.
        print("You're not an employee")
elif accept[0].casefold().replace(" ", "") == "n":  # bonus: case-insensitive.
    print("This service is not for you. Exiting program...")
    exit()
