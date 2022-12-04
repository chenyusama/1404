import random
MIN_NUMBER = 1
MAX_NUMBER = 45
AMOUNT_OF_RANDOM_NUMBER = 6

pick = int(input("How many quick picks? "))


for i in range(pick):
    numbers = []
    for j in range(AMOUNT_OF_RANDOM_NUMBER):
        random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while random_number in numbers:
            random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        numbers.append(random_number)
        numbers.sort()
    for number in range(AMOUNT_OF_RANDOM_NUMBER):
        print(f"{numbers[number]:>2}", end=" ")
    print()