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
        if len(self.group) >= 10:
            raise Exception("Група з десяти людей вже сформована!")
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
st3 = Student('Female', 23, 'Bohdan', 'Shevchenko', 'AN143')
st4 = Student('Male', 23, 'Bohdan', 'Shevchenko', 'AN143')
st5 = Student('Male', 23, 'Bohdan', 'Shevchenko', 'AN143')
st6 = Student('Female', 23, 'Bohdan', 'Shevchenko', 'AN1432')
st7 = Student('Male', 23, 'Bohdan', 'Shevchenko', 'AN1431')
st8 = Student('Male', 23, 'Bohdan', 'Shevchenko', 'AN1453')
st9 = Student('Female', 23, 'Bohdan', 'Shevchenko', 'AN143')
st10 = Student('Male', 23, 'Bohdan', 'Shevchenko', 'AN14334')
gr = Group('PD1')

st11 = Student("Female", 22, "Jane", "Doe", "RB11")
try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)
except Exception as e:
    print(f"An error occurred: {e}")
