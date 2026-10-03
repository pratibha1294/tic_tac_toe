
def add_person():
    name= input("name: ")
    age= input("age: ")
    email= input("email: ")

    person={"name": name, "age": age, "email": email}
    return person
def display_people(people):
    for i, person in enumerate(people):
        print(i+1, "-", person["name"], "|", person["age"],"|", person["email"])

def delete_contact(people):
    display_people(people)

    while True:
        number= input("Enter the number to delete: ")
        try:
            number=int(number)
            if number<=0 or number> len(people):
                print("Invalid number, Out of range!")
            else:
                break
        except:
            print("Invalid number")
    people.pop(number-1)
    print("person deleted")
def search(people):
    search_name= input("Search the name: ").lower()
    results=[]

    for person in people:
        name= person["name"]
        if search_name in name.lower():
            results.append(person)
    display_people(results)



print("Hi Welcome to Contact management system")
print()
people = [{"name": "Tim", "age": "23","email": "tim12@gmail.com"},
          {"name": "tina", "age": "24","email": "tim@gmail.com"},
          {"name": "Ttinyim", "age": "26","email": "tim3@gmail.com"}]



while True:
    print("Contact list size:", len(people))
    command = input("You can 'Add', 'Search', 'Delete': ").lower()
    if command == "add":
        person = add_person()
        people.append(person)
        print("Person added!")
    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        search(people)
    elif command == "q":
        break
    else:
        print("Invalid command")
