# This program calculates the subtotal for a meal based on
# the number of children and adults, and their respective meal prices.
# it also calculate the tax and the total amount due.

# Get meal prices and number of people.
child_meal = float(input("What is the price of the child's meal? "))
adult_meal = float(input("What is the price of the adult's meal? "))

children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))

# Calculate subtotal. 
subtotal = (child_meal * children) + (adult_meal * adults)
subtotal = print(f"The subtotal is: ${subtotal:.2f}")

# Calculate sales tax.
sales_tax_rate = float(input("What is sales tax rate? (e.g., 6 for 6%) ")) / 100
sales_tax = (child_meal * children + adult_meal * adults) * sales_tax_rate
sales_tax = print(f"The sales tax is: ${sales_tax:.2f}")

# Calculate total amount due.
total = (child_meal * children) + (adult_meal * adults) + (child_meal * children + adult_meal * adults) * sales_tax_rate
total = print(f"The total is: ${total:.2f}")

# Calculate the payment and change due.
payment = float(input("What is the payment amount? "))
change = payment - (child_meal * children + adult_meal * adults + (child_meal * children + adult_meal * adults) * sales_tax_rate)
change = print(f"The change due is: ${change:.2f}")





