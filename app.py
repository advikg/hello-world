# First Lesson:
# print("Advik Garg")
# print('o----')
# print(' ||||')

# Variables:
# price = 10
# rating = 4.9
# name = 'Advik'
# is_published = True
# print(price)

# full_name = 'John Smith'
# age = 20
# new_patient = True

# Getting Input:
# name = input('What is your name? ')
# print('Hi ' + name)

# name = input('What is your name? ')
# favorite_color = input('What is your favorite color? ')
# print(name + ' likes ' + favorite_color)

# Type Conversion

# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2019 - int(birth_year)
# print(type(age))
# print(age)

# weight_lbs = input('How many pounds do you weigh? ')
# weight_kg = float(weight_lbs) * 0.45
# print('You weigh ' + str(weight_kg) + ' kilograms')

# Strings
# course = 'Python for Beginners'
# print(course[0:])
# print(course[:5])
# print(course[0])
# print(course[0:3])
# print(course[:])

# name = 'Jennifer'
# print(name[1:-1])
# letter = '''
# Hi John,

# How are you? I'd like to invite you to my house.

# From, Bob
# '''
# print(letter)

# Formatted Strings

# first = 'John'
# last = 'Smith'
# message = first + ' [' + last + '] is a coder'
# msg = f'{first} [{last}] is a coder'
# print(message)
# print(msg)

# String Methods
# course = 'Python for Beginners'
# print(len(course))
# print(course.upper())
# print(course.find('Beg'))
# print(course.lower())
# print(course.replace('Beginners', 'Absolute Beginners'))
# print('Python' in course)

# Arithmetic Operations

# print(10 / 3)
# print(10 // 3)
# print(10 ** 3)
# print(10 % 3)
# x = 10
# x -= 3
# print(x)
# x += 3
# print(x)

# Math Functions

# import math

# x = 2.9
# print(math.ceil(x))
# print(math.floor(x))
# print(round(x))
# print(abs(x))

# If Statements

# is_hot = False
# is_cold = False
# if is_hot:
#    print("It's a hot day")
#    print('Drink plenty of water')
# elif is_cold:
#    print("It's a cold day")
#    print('Wear warm clothes')
# else:
#    print("It's a lovely day")
# print("Enjoy your day")

# price = 1000000
# good_credit = True
# not_good_credit = False
# if good_credit:
#    down_payment = price * 0.1
# elif not_good_credit:
#    down_payment = price * 0.2
# print(f'You have to pay ${ down_payment } first')

# Logical Operators(and,not,or)
# has_high_income = True
# has_criminal_record= False

# if has_high_income and not has_criminal_record:
#    print('Eligible for loan')

# Comparison Operators(<,==,>,!=)
# temperature = 30
# if temperature == 30:
#    print("It's a hot day")
# else:
#    print("It's not a hot day")

# name = input("Type in your name: ")
# if len(name) < 3:
#    print("Name must be at least 3 characters")
# elif len(name) > 50:
#    print("Name must be a maximum of 50 characters")
# else:
#    print("Name looks good")

# weight = float(input('Weight: '))
# lb_or_kg = input('(L)bs or (K)g: ')
# if lb_or_kg.lower() == "l":
#    weight *= 0.45
#    print(f'You are {weight} kilograms')
# elif lb_or_kg.lower() == "k":
#    weight /= 0.45
#    print(f'You are {weight} pounds')

# While Loops
# i = 1
# while i <= 5:
#    print('*' * i)
#    i = i + 1
# print('Done')

# Guessing Game

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#    guess = int(input('Guess: '))
#    guess_count += 1
#    if guess == secret_number:
#        print('You won!')
#        break
# else:
#    print('GAME OVER')

# Car Game
# command = input('>')
# quit = False
# started = False
# while not quit:
#    if command.lower() == 'help':
#        print('''
# start - to start the car
# stop - to stop the car
# quit - to exit
#        ''')
#        command = input('>')
#    elif command.lower() == 'start':
#        if started:
#            print('The car is already started!')
#            command = input('>')
#        else:
#            print('Car started...Ready to go!')
#            command = input('>')
#            started = True
#    elif command.lower() == 'stop':
#        if not started:
#            print('Car is already stopped!')
#            command = input('>')
#        else:
#            print('Car stopped.')
#            command = input('>')
#            started = False
#    elif command.lower() == 'quit':
#        quit = True
#    else:
#        print("I don't understand that...")
#        command = input('>')

# For Loops

# for item in range(5, 10, 2):
#    print(item)

# prices = [10, 20, 30]
# total=0
# for price in prices:
#    total= total+price
# print(f'Total: {total}')

# Nested Loops
