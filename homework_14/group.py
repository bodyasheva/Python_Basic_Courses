from student import Student
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