#for statement clarification

#when using lists, we should use index like 'i' instead of words[i]
words=['hi', 'hello', 'bye']
print(words)
words.insert(0,'hey')
print(words)
print(len(words))
words[0:2]
for i in words:
    print(i, len(i))
for i in range(5,10,2):
    print(i,end=",")
print('\n',range(10))

#Errors are coming when used the following syntax because Only Curved paranthesis should be used
#list[range(7)]
#list[0:2]

#w(range(5)) - Also throws Error i.e., NameError
#The below one doesn't throw error because 'list' is predefined in Python to get intialized with iterable items.
list(range(6))