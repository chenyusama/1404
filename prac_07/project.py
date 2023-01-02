class Project:
    def __init__(self, name="", date="", priority=0, cost=0.0, percentage=0):
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.percentage = percentage

    def __str__(self):
        return f"{self.name}, start: {self.date}, priority {self.priority}, estimate: ${self.cost}, completion: {self.percentage}%"

    def is_completed(self):
        return int(self.percentage) == 100



