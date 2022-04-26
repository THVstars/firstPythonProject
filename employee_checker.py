import re

COMPANY_NAME = "Tech Inc."

EMPLOYEES = ["Alice", "Bob", "Cameron", "Dan", "Ellen", "Frank", "Grace", "Harry"]

# Welcome message + employee names listed out
print("\nWelcome to the "+COMPANY_NAME+" employee check-in\n")
print("We at " + COMPANY_NAME + " are very proud of our employees: ")
for emp_name in EMPLOYEES:
    print("-- "+emp_name)
print("\n")

# user input section (buggy code)

accept = input("Do you work for " + COMPANY_NAME + "?\n(yes/no): ")

if re.search("y", accept[0]) is not None: # bonus: checks if the input starts with y and accepts it if it does
    name = input("What is your name?\nName: ")
    for emp_name in EMPLOYEES:
        if name.casefold().replace(" ", "") == emp_name.casefold(): # bonus: case-insensitive and ignores empty spaces
            print("Thank you " + emp_name + ", you are now checked in.")
            break
    else: # only prints out once, after checking every name
        print("You're not an employee")
elif accept.casefold() == "no": # bonus: case-insensitive
    print("This service is not for you. Exiting program...")
    exit()
