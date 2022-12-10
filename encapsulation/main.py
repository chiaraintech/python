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
    
    # annotation not needed but best practice to hint
    # not passing self bc a static method is not related to a specific object
    # method that works without any object in the class directly
    @staticmethod
    def static_method():
        print('hello world')


# it works even if I don't have any object initialised at this point
Person.static_method()

p1 = Person("Chiara", 27, 'm')
print(p1.Name)

# same result as line 32 because the two things are not related
p1.static_method()

p1.Name = "Bob"
print(p1.Name)