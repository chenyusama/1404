def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        check_name = input("Is your name {}? (Y/n) ".format(name))
        if check_name.upper() != "Y" and check_name != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for key, value in email_to_name.items():
        print("{} ({})".format(value, key))


def get_name(email):
    fullname = email.split('@')[0]
    part_of_name = fullname.split('.')
    name = " ".join(part_of_name).title()
    return name


main()