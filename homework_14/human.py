class Human:
    def __init__(self, gender, age, first_name, second_name):
        self.gender = gender
        self.age = age
        self.firs_name = first_name
        self.second_name = second_name

    def __str__(self):
        return f"{self.firs_name} {self.second_name}\nGender: {self.gender}\nAge: {self.age}"