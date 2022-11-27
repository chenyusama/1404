count = 0

out_file = open("name.txt", "w")
name = input("please enter your name:")
print("{}".format(name), file=out_file)

out_file.close()

in_file_1 = open("name.txt")
name_2 = in_file_1.read()
print("Your name is {}".format(name_2))

in_file_1.close()

in_file_2 = open("numbers.txt")
number_1 = in_file_2.readline()
number_2 = in_file_2.readline()
total = int(number_1) + int(number_2)

print(total)

in_file_2.close()

in_file_3 = open("numbers.txt")
for line in in_file_3:
    count += 1
print("There are {} lines in total".format(count))


in_file_3.close()
