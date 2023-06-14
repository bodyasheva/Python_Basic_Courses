class Human:
    def __init__(self, gender, age, first_name, second_name):
        self.gender = gender
        self.age = age
        self.firs_name = first_name
        self.second_name = second_name

    def __str__(self):
        return f"{self.firs_name} {self.second_name}\nGender: {self.gender}\nAge: {self.age}"

class Student(Human):
    def __init__(self, gender, age, first_name, second_name, record_book):
        super().__init__(gender, age, first_name, second_name)

        self.record_book = record_book

    def __str__(self):
        return f"{self.firs_name} {self.second_name}( Record Book: {self.record_book} )"

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        who = self.find_student(last_name)
        if who:
            self.group.remove(who)

    def find_student(self, last_name):
        for who in self.group:
            if who.second_name == last_name:
                return who
        return None
    def __str__(self):
        all_students = ''
        for who in self.group:
            all_students += f"\n{str(who)}"
        return f'Number:{self.number}{all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 23, 'Bohdan', 'Shevchenko', 'AN143')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
print(gr)
print(gr.find_student('Jobs'))
print(gr.find_student('Jobs2'))
gr.delete_student('Taylor')
print(gr)
