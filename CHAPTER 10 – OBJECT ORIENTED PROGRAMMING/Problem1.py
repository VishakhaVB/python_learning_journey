# 1. Create a class “Programmer” for storing information of few programmers 
# working at Microsoft.

class Programmer:
    def __init__(self, name, language, experience_years, company='Microsoft'):
        self.name = name
        self.language = language
        self.experience_years = experience_years
        self.company = company

    def __repr__(self):
        return f"Programmer(name={self.name}, language={self.language}, exp={self.experience_years}, company={self.company})"


# Demo: create a few programmers and store in a list
team = [
    Programmer('Alice', 'Python', 3),
    Programmer('Bob', 'C#', 5),
    Programmer('Charlie', 'JavaScript', 2)
]

for p in team:
    print(p)
