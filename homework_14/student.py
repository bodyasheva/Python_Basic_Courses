from human import Human
class Student(Human):
    def __init__(self, gender, age, first_name, second_name, record_book):
        super().__init__(gender, age, first_name, second_name)

        self.record_book = record_book

    def __str__(self):
        return f"{self.firs_name} {self.second_name}( Record Book: {self.record_book} )"