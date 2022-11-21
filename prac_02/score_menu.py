MENU = """(G)et a valid score
(P)rint result 
(S)how stars 
(Q)uit"""


def main():

    global score
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_number("Enter your score:", 0, 100)
        elif choice == "P":
            result = get_result(score)
            print(result)
        elif choice == "S":
            stars = get_stars(score)
            print(stars)
        else:
            print("Invalid option")
        print("-------------")
        print(MENU)
        choice = input(">>> ").upper()
    print("Finished.")


def get_stars(score):
    return score * "*"


def get_valid_number(prompt, low, high):
    number = int(input(prompt))
    while number < low or number > high:
        print("Invalid input")
        number = float(input(prompt))
    return number


def get_result(score):
    if score < 0:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    elif score <= 100:
        return "Excellent"
    else:
        return "Invalid score"


main()
