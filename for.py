students = {
    "male":["Tom","Charlie","Harry","Frank"],
    "female":["Sarah", "Huda", "Emily", "Elizabeth","Samantha"]
    }
for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)
