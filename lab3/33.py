class Person:
    def __init__(self ,name ,age):
        self.name = name
        self.age =age
        self.birthday = "16.09.2005"
    def selebration(self ,day):
        if day == self.birthday:
            print (f"Happy birthday {self.name} ! you are {self.age + 1}")
        
person = Person("Madiyar" , 18)
person.selebration("16.09.2005")