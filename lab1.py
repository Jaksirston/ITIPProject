# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

groupmates = [
    {
    "Name": "Илья",
    "Surname": "Антоненко",
    "Exams": ["Метрология", "ОБЖ", "ИТИП", "МИСПИСИТ"],
    "Marks": [3, 2, 5, 3]
    },
    {
    "Name": "Иван",
    "Surname": "Человеков",
    "Exams": ["Метрология", "ОБЖ", "ИТИП", "МИСПИСИТ"],
    "Marks": [4, 5, 5, 4]
    },
    {
    "Name": "Константин",
    "Surname": "Держанов",
    "Exams": ["Метрология", "ОБЖ", "ИТИП", "МИСПИСИТ"],
    "Marks": [4, 3, 4, 4]
    },
    {
    "Name": "Полина",
    "Surname": "Вершкова",
    "Exams": ["Метрология", "ОБЖ", "ИТИП", "МИСПИСИТ"],
    "Marks": [5, 4, 3, 4]
    },
    {
    "Name": "Аркадий",
    "Surname": "Гусевешвилли",
    "Exams": ["Метрология", "ОБЖ", "ИТИП", "МИСПИСИТ"],
    "Marks": [5, 4, 5, 5]
    },
]
def print_students(students):
    print(u"Имя".ljust(12), u"Фамилия".ljust(12), u"Экзамены".ljust(43), u"Оценки".ljust(20), u"средняя оценка".ljust(20))
    for student in students:
        print(student["name"].ljust(12), student["surname"].ljust(12), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20), str(student["sredn"]).ljust(20))
def searchSredn():
    poisk = float(input("средняя оценка"))
    new_group = []
    for students in groupmates:
        sredn = sum(students['marks'])/len(students['marks'])
        if(sredn > poisk):
            students['sredn'] = sredn
            new_group.append(students)
    print_students(new_group)

searchSredn()