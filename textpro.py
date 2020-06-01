statement = ""

while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        print(statement)
        break
    elif user_input.startswith(("what","how","who","where","why","when")):
        statement = statement + user_input.capitalize() + "? "
    else:
        statement = statement + user_input.capitalize() + ". "