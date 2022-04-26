print("Welcome to my first Python CLI!\n")

# if __name__ == '__main__':
#    print("name is main")
# else:
#    print("name is not main")

# name = input("What is your name?\nYour name: ")

# print("\nHello " + name + "!")

family = ["Taehyung", "Yeontan", "Nyubella", "Carolina", "Rosario", "John", "Victoria"]

accept = input("Are you part of Carolina's family?\n(yes/no): ")

if accept == "yes":
    name = input("\nWhat is your name?\nYour name: ")
    for emp_name in family:
        if name == emp_name:
            print("\nOkay, you can come in.")
            break
    else:
        print("\nYou're a liar. Please leave.")
else:
    print("\nOkay, you can leave.")