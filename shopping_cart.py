#This project will document to help Alex determine the quantity of each supply she could purchase that would be within a $25 budget.

#Items cost

flowerpot_price = 4.00
flowerseeds_price = 1.00
soil_price = 5.00
tax_rate = 0.06

#Inputting amount of items
flowerpot = int(input('How many flowerpots? '))
flower_seeds = int(input('How many packs of flower seeds? '))
soil = int(input('How many bags of soil? '))

#Equation to calculate the cost of the items in Alex's shopping cart
cost_of_items = (flowerpot * flowerpot_price) + (flower_seeds * flowerseeds_price) + (soil * soil_price)

#Total cost with taxes
total_cost = (cost_of_items *tax_rate) + cost_of_items

#print the total cost
print(f"The total cost of these items would be ${total_cost}.")
