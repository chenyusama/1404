MENU = """(H)ello
(G)oodbye
(Q)uit"""
user_name = input("Enter name:")
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello {}".format(user_name))
    elif choice == "G":
        print("Goodbye {}".format(user_name))
    else:
        print("Invalid option")
    print("-------")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")
