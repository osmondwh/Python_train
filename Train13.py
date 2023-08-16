#隨機挑選key並取值

import random
students = {
    "小白": {
        "age": 23,
        "height": 170.5,
        "weight": 60
    },
    "小黃": {
        "age": 30,
        "height": 160.5,
        "weight": 38
    },
    "小綠": {
        "age": 15,
        "height": 160.5,
        "weight": 38
    }
}
student_random = random.randint(0, len(list(students.keys()))-1)
student = list(students.keys())[student_random]
print(f"抽到的是：{student}")
print(f"年紀：{students[student]['age']}")
print(f"身高：{students[student]['height']}")
print(f"體重：{students[student]['weight']}")


