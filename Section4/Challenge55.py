# ask for name and age
# if over 18 and under 31, welcome them to party
# else advise not allowed
name = input('What is your name?')
age = int(input('Hello {}. What is your age?'))
if(18 <= age < 31):
    print('Welcome to the party')
else:
    print('Sorry you are not welcome')

print('name = {0} age = {1}'.format(name, age))
