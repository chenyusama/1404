"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_details(data)

def display_details(data):
    for subject in range(len(data)):
        print(f"{data[subject][0]} is taught by {data[subject][1]:<12} and has {data[subject][2]:>3} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_details = []
    input_file = open(FILENAME)
    for line in input_file:
        parts = line.strip().split(',')
        parts[2] = int(parts[2])
        subject_details.append(parts)
    input_file.close()
    return subject_details


main()