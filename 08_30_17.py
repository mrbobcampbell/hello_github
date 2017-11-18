#  Checking to see what is in a list use 'in / not in' method
test1 = ['bob', 'margaret', 'max']


for i in range(len(test1)):
    print(str(i) + ' ' + test1[i])


print('mx' in test1)
print('\n\n\n')


#  Multiple vairable assignement from a list
dog = ['bulldog', 'brindle', 1]
type, color, age = dog

print(color)


import random

messages = [' It is certain', 'It is decidedly so',
            'Yes definitely', 'Reply hazy try again',
            'Ask again later', 'Concentrate and ask again',
            'My reply is no', 'Outlook not so good', 'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])
