my_name = 'Bob Campbell'

#	Update variable in print statement - with 'format' method
x1 = 'Hello, my name is {}.'
print(x1.format(my_name))

#	Update variable itself with 'format' method
x1 = x1.format(my_name)
print(x1)
print("\n\n\n\n")


#	This is equivalent to the above sequence, but uses 'f-strings'
print(f'Hello, my name is {my_name}.')
print("\n\n\n\n")


print('''Giving multi-line a try.

So far so good.''')
