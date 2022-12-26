class ProgrammingLanguages:
    def __init__(self, name="", typing="", is_reflection=False, year=""):
        self.name = name
        self.typing = typing
        self.year = year
        self.reflection = is_reflection

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name},{self.typing},Reflection = {self.reflection},First appeared in {self.year}"