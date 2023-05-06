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
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(43), u"Оценки".ljust(20), u"средняя оценка".ljust(20))
    for student in students:
        print(student["Name"].ljust(15), student["Surname"].ljust(10), str(student["Exams"]).ljust(30), str(student["Marks"]).ljust(20), str(student["Middle"]).ljust(20))
def searchMiddle(groupmates):
    search = float(input("средняя оценка"))
    new_group = []
    for students in groupmates:
        middle = sum(students['Marks'])/len(students['Marks'])
        if(middle > search):
            students['Middle'] = middle
            new_group.append(students)
    print_students(new_group)

searchMiddle(groupmates)