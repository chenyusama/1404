numbers = []
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    username = input("What is your username?: ")
    correct_username = confirm_username(username)
    if correct_username:
        for i in range(5):
            number = int(input("Number: "))
            numbers.append(number)
        print(f"The first number is {numbers[0]}")
        print(f"The last number is {numbers[-1]}")
        print(f"The smallest number is {min(numbers)}")
        print(f"The largest number is {max(numbers)}")
        print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


def confirm_username(username):
    if username in usernames:
        print("Access granted")
        return True
    else:
        print("Access denied")
        return False


main()
