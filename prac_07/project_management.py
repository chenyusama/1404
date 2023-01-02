from prac_07.project import Project

menu = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    print(menu)
    choose = input(">>>").upper()
    while choose != "Q":
        if choose == "L":
            load_projects = get_filename()
        if choose == "S":
            # close_file()
            pass
        if choose == "D":
            display_projects(load_projects)

        print("------------------------")
        print(menu)
        choose = input(">>>").upper()
    print("Thank you for using custom-built project management software.")


def get_filename():
    try:
        filename = input("Enter your filename: ")
        in_file = open(f"{filename}", "r")
        print("File loaded.")
        return in_file
    except FileNotFoundError:
        print("Please enter a correct filename")

# def close_file():
    #try:
        # .close()
        # print("File is closed")
    #except:
        # print("you have not loaded the file")

def display_projects(load_projects):
    complete_project = []
    incomplete_project = []
    for project in projects:
        if p





main()
