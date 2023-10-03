import csv

class NameCheck:
    def __init__(self, check_title, check_alpha):
        self.check_title = check_title
        self.check_alpha = check_alpha

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, name_student):
        setattr(instance, self.param_name, self._validate(name_student))

    def _validate(self, name_student: str):
        if not self.check_title(name_student) or not self.check_alpha(name_student):
            raise ValueError('Имя содержит не допустимые данные либо не начинается с заглавной буквы')
        return name_student


class Student:
    first_name = NameCheck(str.istitle, str.isalpha)
    last_name = NameCheck(str.istitle, str.isalpha)

    def __init__(self, name, subjects_file):
        self.first_name, self.last_name = name.split(' ')
        self.subject = subject = {}

        with open(subjects_file, 'r', encoding='utf-8') as file:
            csv_file = list(csv.reader(file, dialect='excel-tab'))
            for line in csv_file:
                sub_list = line[0].split(',')
                for sub in sub_list:
                    self.subject.setdefault(sub)



    # def add_subject(self, subject, grade, test_score):
    #     pass
    #
    # def get_average_grade(self):
    #     pass
    #
    # def get_subjects(self):
    #     pass
    #
    # def get_average_grades(students):
    #     pass
    #
    # def get_subject_average(students, subject):
    #     pass
    #
    # def get_top_student(students, subject):
    #     pass


student = Student("Иван Иванов", "subjects.csv")
print(student.__dict__)