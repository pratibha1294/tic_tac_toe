
def add_person():
    name= input("name: ")
    age= input("age: ")
    email= input("email: ")

    person={"name": name, "age": age, "email": email}
    return person

print("Hi Welcome to Contact management system")
command= input("You can 'Add', 'Search', 'Delete': ")
people=[]

if command == "add":
    person=add_person()
    people.append(person)
    print("person added")
elif command=="delete":
    pass
elif command=="Search":
    pass
else:
    print("Invalid command")

print(people)