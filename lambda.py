people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# lamdba replaces the example dictionary sort function below with a single line call
# def f(person):
#     return person["name"]

# people.sort(key=f)

people.sort(key=lambda person: person["name"])
print(people)