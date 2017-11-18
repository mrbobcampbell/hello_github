import random


# Adjust pattern length you are looking for here
pattern_length = 2


mylist = []
success = 0
failure = 0

while len(mylist) < 1000:
    mylist.append(random.randint(0, 1))

print(mylist)
print(len(mylist))
# print('\n\n')


for i in range(len(mylist) - (pattern_length - 1)):
    chunk = mylist[i:i + pattern_length]
    if 0 not in chunk:
        print(chunk, 'success')
        success += 1
    else:
        print(chunk, 'failure')
        failure += 1


print("Success: ", success, (success / (success + failure)) * 100)
print('Falure: ', failure, (failure / (success + failure)) * 100)
