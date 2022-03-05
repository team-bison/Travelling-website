
# Define user class
class User:
    '''list to store users' full name and their unique id'''
    users = []
    '''iterable count of users to give each user a unique id'''
    idCounter = 1

    def __init__(self, first, last, nationality, age, gender):

        '''initializing first name, last name, nationality, age and gender
        User have a dictionary to store full name as key and their id as value
        Users are given unique id
        '''

        if (type(first) is not str):
            raise TypeError("first name must be a string")
        if (type(last) is not str):
            raise TypeError("surname must be a string")
        if (type(nationality) is not str):
            raise TypeError("Nationality must be a string")
        if (type(int(age)) is not int):
            raise TypeError("Age must be an integer")
        if int(age) < 10 or int(age) > 70:
            raise ValueError("No special accomodations for babies and adults")
        if (type(gender) is not str):
            raise TypeError("gender must be a string")

        self.first = first
        self.last = last
        self.nationality = nationality
        self.age = age
        self.gender = gender
        self.userid = User.idCounter
        self.fullname = self.first+" "+self.last
        User.users.append[self.fullname, self.userid]
        User.idCounter += 1

'''Define Useraccount class'''
class Useraccount:
    users_account = []

    def __init__(self, username, password):
        '''initializing username and password
        Useraccount has a dictionary to store username as key and their password as value
        Users cannot use email that doesnot have a valid domain
        their email should end up using @gmail.com
        '''
        if (type(username) is not str):
            raise TypeError("Username must be a string")
        
        
        if username[len(username)-10:] != "@gmail.com":
            raise TypeError("Username should have valid domain @gmail.com")


        if len(password) < 10:
            raise TypeError("Password length should be atleast 10.")

        if password.isalpha() or password.isdigit():
            raise TypeError("Password should atleast be combination of strings and digits. To make it more strong, use special characters.")
        
        self.username = username
        self.password = password
        
        Useraccount.users_account.append[self.username, self.password]
