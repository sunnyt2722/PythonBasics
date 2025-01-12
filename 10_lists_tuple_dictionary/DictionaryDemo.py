dictionaryTest = {"Sunny": 30, 7117696:"CS_ID", "Company": "PS"}

print(dictionaryTest[7117696])
print(dictionaryTest["Sunny"])


dict = {}
dict["firstName"] = ["Sunny"]
dict["lastName"] = ["Kumar"]

print(dict)

listOfFriends = [
    {"name":"Joe", "age": 30},
    {"name":"Ross", "age": 32},
    {"name":"Chandler", "age": 27}
]

print(listOfFriends[1])

listOfStudents = [
    {"name": "Robert", "grade":90},
    {"name": "Downy", "grade": 84},
    {"name": "Jr.", "grade":31.3}
]

print(len(listOfStudents[1]))
totalMarks = 0
for grades in listOfStudents:
    totalMarks += grades["grade"]

print(totalMarks/len(listOfStudents))