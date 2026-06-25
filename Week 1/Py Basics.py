# Python Basics Practice
# Topics: variables, lists, dictionaries, loops, functions

name = "Industrial Quality Assurance"
week = 1

print(name)
print("Week:", week)

topics = ["Python", "ML", "Computer Vision"]

for topic in topics:
    print(topic)


project = {
    "name": "Multi-Modal AI System",
    "domain": "Quality Assurance"
}

print(project["name"])


def greet(user):
    return "Hello " + user

print(greet("SoC"))


marks = 80

if marks >= 40:
    print("Passed")
else:
    print("Need improvement")
