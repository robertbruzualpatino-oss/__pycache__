child_meal = float(input("What is the price of the child's meal? "))
adult_meal = float(input("What is the price of the adult's meal? "))

children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))

subtotal = (child_meal * children) + (adult_meal * adults)
subtotal = print(f"The subtotal is: ${subtotal:.2f}")
