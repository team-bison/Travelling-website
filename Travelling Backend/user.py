# Define user class
class User:
    users = {}
    idCounter = 1

    def __init__(self, first, last, nationality, age, gender):

        if (type(first) is not str):
            raise TypeError("first name must be a string")
        if (type(last) is not str):
            raise TypeError("surname must be a string")
        if (type(nationality) is not str):
            raise TypeError("Nationality must be a string")
        if (type(age) is not int):
            raise TypeError("Age must be an integer")
        if (type(gender) is not str):
            raise TypeError("gender must be a string")

        self.first = first
        self.last = last
        self.nationality = nationality
        self.age = age
        self.gender = gender
        self.userid = User.idCounter
        User.users[self.first+""+self.last] = [self.userid]
        User.idCounter += 1

      
       