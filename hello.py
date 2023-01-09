# Ask user for their name and remove whitespace from str and capatilize users name
name = input("What's your name? ").strip().title()

#split users name into first name and last name
first, last = name.split(" ")

#Say hello to user
print("Hello,", name)

#Say hello to user with two print lines overrighting the default parameter in the print functions
print("Hello, ",end='')
print(name)

#Say hello to user with overrighting default paramter of sep in the print functions
print("Hello, ", name, sep='')

#Printing "" with using double quotes 
print("Hello, \"friend\"")

#formating string to output user name
print(f'Hello, {name}')

#printing out only the first name of the user inputed information
print(f'Hello, {first}')

