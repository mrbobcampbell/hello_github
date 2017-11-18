
def div_3(x):
    y = x % 3
    if y == 0:
        return "Divisible by 3."
    else:
        return "Nope."


loop = 1


while loop == 1:
    r = int(input("what is your number? "))
    print(div_3(r))
