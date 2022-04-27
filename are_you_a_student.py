students = ["Taehyung", "Yeontan", "Nyubella", "Carolina", "Snowball"]

print("Are you a student? Let's find out.")
question = input("Are you a student?\nPlease enter yes or no.\n")

while question[0].casefold() == "" or question[0].casefold() != "y" and question[0].casefold() != "n":
    question = input("Are you a student?\nPlease enter yes or no.\n")

if question[0].casefold().replace(" ", "") == "y":
    name = input("What is your name?\n")
    for student_name in students:
        if name.casefold().replace(" ", "") == student_name.casefold():
            print("Welcome to class, " + student_name + "!")
            break
    else:
        print("You're not in this class.")
elif question[0].casefold().replace(" ", "") == "n":
    print("Goodbye!")
    exit()
