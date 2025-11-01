class person:

    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display(self):
        print(self.name)
        print(self.id_number)

class employee(person):
    
    def __init__(self, name, id_number, salary, post):
        self.salary = salary
        self.post = post

        person.__init__(self, name, id_number)
obj = employee("Raj", 7809, 400, 8095)
obj.display()