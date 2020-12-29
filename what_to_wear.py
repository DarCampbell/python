#This program will help Madison learn what to wear outside

#Create variable temperature to capture user input
temperature = int(input('What is the current temperature'))

#Create if else if statements to compare user input to predecided temperatures
if temperature >=80:
    outfit = 'wear shorts and pack your sunglasses'

elif temperature <=79 and temperature >=60:
    outfit = 'wear a light jacket'

else:
    outfit = 'wear a coat in addition to a hat, gloves, and scarf'

#Print the advice to the screen
advice = (f'Today {outfit}.')
print(advice)
