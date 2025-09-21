
def add_contacts(name, phone, email, contacts_list):
    new_contact = {'name': name, 'phone': phone, 'email': email}
    contacts_list.append(new_contact)

def search_contact(name, contacts_list):
    found_contacts = []
    for contact in contacts_list:
        if contact['name'] == name:
            found_contacts.append(contact)
    return found_contacts

def delete_contact(name, contacts_list):
    for contact in contacts_list:
        if contact['name'] == name:
            contacts_list.remove(contact)

def update_contact(name, phone, email, contacts_list):
    for contact in contacts_list:
        if contact['name'] == name:
            contact['phone'] = phone
            contact['email'] = email

def main():
    contacts = []  # Initialize an empty list to store contacts
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Update Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            add_contacts(name, phone, email, contacts)
            print("Contact added successfully.")

        elif choice == '2':
            name = input("Enter the name to search: ")
            found_contacts = search_contact(name, contacts)
            print_contacts(found_contacts)

        elif choice == '3':
            name = input("Enter the name to delete: ")
            delete_contact(name, contacts)
            print("Contact deleted successfully.")

        elif choice == '4':
            name = input("Enter the name to update: ")
            phone = input("Enter the new phone number: ")
            email = input("Enter the new email address: ")
            update_contact(name, phone, email, contacts)
            print("Contact updated successfully.")

        elif choice == '5':
            print("Exiting Contact Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

def print_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

if __name__ == "__main__":
    main()














1. ans

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
values = [ ]
for key in person:    
    values.append(person[key])
print(values)

2.ANS
x = int(input("enter a number"))
if x%2 ==0:
    print("even")
else:    
    print("odd")

marks = 100
if marks >= 90:
    print("first class")
elif marks >= 35:
    print("pass")
else:
    print("fail")

3.ANS
SELECT * FROM customers
WHERE age > 22 AND country = 'Sri Lanka';

def customer_name():
    name = "Naveen"   
    print(name)
customer_name  ()

4.ANS
def average_speed(distance, time):
    if time == 0:
        return "Time cannot be zero."
    return distance / time
    
dist = 120  # km
time_taken = 2  # hours
speed = average_speed(dist, time_taken)
print("Average speed:", speed, "km/h")

5.ANS
people = [
    {"name": "sidhya", "age": 24},
    {"name": "madhu", "age": 35},
    {"name": "chari", "age": 40},
    {"name": "meena", "age": 30}
]
names_over_31 = [ ]  
for person in people:
    if person["age"] > 31:    
        names_over_31.append(person["name"])  
print(names_over_31)

6.ANS
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
people = [
    Person("Alice", 28),
    Person("Bob", 35),
    Person("Charlie", 40),
    Person("Diana", 30)
]
ages = [ ]  # empty list to store ages

for person in people:
    ages.append(person.age)

print("Ages collected:", ages)


7.ANS
def check_odd(number):
   if number % 2 != 0:
    print(f"{number} is Odd")
else:
    print(f"{number} is Even")
check_odd(7)   # 7 is Odd
check_odd(10)  # 10 is Even

8.ANS
number = 0
while number <= 10:
    number = int(input("Enter a number greater than 10: "))
   print(f"Number {number} has been accepted!")

9.ANS
num = 1
while num <= 5:
    print(num)
    num += 1  # increment the number by 1

10.ANS
class Car:
    def __init__(self, make, model, age):
        self.make = make
        self.model = model
        self.age = age
        if self.age > 5:
            self.condition = "used"
        else:
            self.condition = "new"

# Example usage:
car1 = Car("Toyota", "Camry", 3)
print(car1.condition) # Output: new

car2 = Car("Honda", "Civic", 7)
print(car2.condition) # Output: used

11.ANS
def create_employee_objects(employee_data_list):
    employee_objects = []
    for data in employee_data_list:
        # Assuming data is a tuple or list like (name, designation)
        employee_object = {'name': data[0], 'designation': data[1]}
        employee_objects.append(employee_object)
    return employee_objects

# Example usage:
raw_employee_info = [("Alice", "Manager"), ("Bob", "Developer")]
employees = create_employee_objects(raw_employee_info)
print(employees)

12.ANS
def create_product_object(name, price):
    return {'name': name, 'price': price}

def apply_discount(product_object, has_discount):
    if has_discount:
        product_object['discounted_price'] = product_object['price'] * 0.90
    else:
        # Optionally, handle non-discounted products here or in a separate function
        product_object['discounted_price'] = product_object['price'] # No discount
    return product_object

def process_all_products(product_data_list):
    processed_products = []
    for name, price, has_discount in product_data_list:
        product = create_product_object(name, price)
        processed_product = apply_discount(product, has_discount)
        processed_products.append(processed_product)
    return processed_products

15.ANS
def analyze_number(N):
    # Calculate factorial
    factorial = 1
    for i in range(1, N + 1):
        factorial *= i

    # Calculate sum of even and odd numbers
    sum_even = 0
    sum_odd = 0
    for i in range(1, N + 1):
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i

    return factorial, sum_even, sum_odd
    
16.ANS
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)




