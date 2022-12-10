class Person:

    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    # all the attributes above are private


## We do not want to have direct access to the properties! If needed use setters.
    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self, value):
        # You have the control to fulfill certain constraints and be safe
        if value == "Bob":
            self.__name = "Default Name"
        else:
            self.__name = value



p1 = Person("Chiara", 27, 'm')
print(p1.Name)

p1.Name = "Bob"
print(p1.Name)