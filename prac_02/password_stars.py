def main():
    password = input("Enter your password:")
    while len(password) != 10:
        print("Please enter a 10-letter password")
        password = input("Enter your password:")
    result = result_password(password)
    print(result)


def result_password(password):
    if len(password) == 10:
        return len(password) * "*"


main()
