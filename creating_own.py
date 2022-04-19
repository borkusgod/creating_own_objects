#oop

class PlayerCharacter:
    def __init__(self, name=None, age=0):  # default param
        self.name = name
        self.age = age

    def run(self):
        print(f'{Player1.name} is running')
        return 'function done'


Player1 = PlayerCharacter('Ryan', 44)
Player2 = PlayerCharacter('Cindy')

print('Exercise from course')
print(Player1.name)
print(Player2.name)
print(Player1.age)
print(Player2.age)
print(Player2.run())

# another example of making classes
# using this for making employee data sets that have name, email address,
# pay and also actions they can perform. This


class Employee:
    def __init__(self, first, last, email1, pay):
        self.first = first
        self.last = last
        self.email1 = email1
        self.pay = pay


emp_1 = Employee('first', 'last', 'email', 'pay')  # assign placeholders
emp_2 = Employee('first', 'last', 'email', 'pay')  # same as above

print('\nExpanded practice from Youtube')
print(emp_1)
print(emp_2)

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email1 = 'Corey.Schafter@company.com'
emp_1.pay = 50000

emp_2.first = 'Bill'
emp_2.last = 'Bork'
emp_2.email1 = 'user@gmail.com'
emp_2.pay = 50000

print(emp_1.email1)
print(emp_2.email1)
print(f'The second user\'s email address is: {emp_2.email1}.')


# Astrology App practice by

class GenericAppUser:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


user1 = AstrologyAppUser('William', 'Bork', 50000)
user2 = AstrologyAppUser('Steven', 'Bork', 55000)

user1.fullname()
print('\nPractice for astrology app')
print(AstrologyAppUser.fullname(user1))


# using input from the user
class Employee:
    def __init__(self, first, last, email2, pay):
        self.first = first
        self.last = last
        self.email2 = email2
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('first', 'last', 'email', 'pay')  # assign placeholders
print('\nHello and welcome.')
print('Could I have your first name please?')
first_n = input()
emp_1.first = first_n
print(f'\nThank you {emp_1.first}')
print('And what is your last name?')
last_n = input()
emp_1.last = last_n
# name_combined = f'{emp_1.first} {emp_1.last}'
print(emp_1.fullname())
print(f'\nThank you for your full name {emp_1.fullname()}.')
print('Now what is your email address that we can associate with the account?')
email = input()
emp_1.email2l = email
print('\nAnd finally, how much are you looking to be paid in this role?')
pay_ex = input()
pay_ex_to_float = float(pay_ex)
pay_currency = '${:,.2f}'.format(pay_ex_to_float)
emp_1.pay = pay_currency
print('Excellent. So let\'s go over the information that I have gathered '
      'from you.')
print(f'I have that your name is {emp_1.fullname()},\n'
      f'and your email address is {emp_1.email2}\n'
      f'and the pay range you are requesting is {emp_1.pay} per year.')

# OOP

class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('run')


player1 = PlayerCharacter('Bill')

print(player1)
print(player1.name)


class DiabloSlayer:
    def __init__(self, name=None, age=0):
        self.name = name
        self.age = age

    def run(self):
        print('run')


# greeting call for player
def diablo_slayer_intro():
    print(f'The player {player2.name} is {player2.age} years old.')


player2 = DiabloSlayer('Tom', 45)
print(player2.age)
print(player2.name)


diablo_slayer_intro()

# try to make an interactive environment
# func for greeting


class NewGame:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def np_greeting():
    print(f'Welcome {new_player.name}... You are an old one at {new_player.age} '
          f'years of age.')


print('Hello new player. Let\'s get you started on making your character.')
print('Please tell me the name you would like for your character:')
np_name = input()
print('Please give me the age that you would like for your character:')
np_age = int(input())
np_age_format = "{:,}".format(np_age)

new_player = NewGame(np_name, np_age_format)
np_greeting()
