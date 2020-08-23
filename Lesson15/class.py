class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__grades = []

    def __str__(self):
        return '{name} - {age}: {grades}'.format(
            name=self.__name,
            age=self.__age,
            grades=' '.join('' + str(grade) + '' for grade in self.__grades)
        )

    def __set_name(self, name):
        if self.__name != name:
            self.__name = name

    def __get_name(self):
        return self.__name

    def set_age(self, age):
        if age >= 16:
            self.__age = age

    def get_age(self):
        return self.__age

    def add_grades(self, *grades):
        for grade in grades:
            if 1 <= grade <= 12:
                self.__grades.append(grade)

    def get_grades(self):
        return self.__grades


class Group:
    def __init__(self, name):
        self.__name = name
        self.__students = []

    def add_students(self, *students):
        for student in students:
            self.__students.append(student)

    def show_group(self):
        for student in self.__students:
            print(student)

    def get_group(self):
        return self.__students


group = Group('PythonIntro07')

stud1 = Student('Ivanova Ekaterina', 29)
stud2 = Student('Smirnov Artem', 27)
stud3 = Student('Kolbasa Ariadna', 28)
stud4 = Student('Yurkov Devid', 25)
stud5 = Student('Dubak Timofey', 30)
group.add_students(stud1, stud2, stud3, stud4, stud5)

students = group.get_group()
students[0].add_grades(12, 4, 6, 10, 11)
students[1].add_grades(6, 10, 11, 4, 8)
students[2].add_grades(5, 4, 8, 9, 10)
students[3].add_grades(4, 7, 8, 3, 9)
students[4].add_grades(11, 10, 11, 12, 11)
group.show_group()
