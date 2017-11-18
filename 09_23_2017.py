import random


# Adjust pattern length you are looking for here
pattern_length = 2
random_integers = 2



mylist = []
success = 0
failure = 0

while len(mylist) < 100000:
    mylist.append(random.randint(1, random_integers))

print(mylist)
print(len(mylist))
# print('\n\n')


for i in range(len(mylist) - (pattern_length - 1)):
    chunk = mylist[i:i + pattern_length]
    if len(set(chunk)) == 1:
        print(chunk, 'success')
        success += 1
    else:
        print(chunk, 'failure')
        failure += 1


print("Success: ", success, (success / (success + failure)) * 100)
print('Falure: ', failure, (failure / (success + failure)) * 100)