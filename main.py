print("welcome to the automatic pizza order machine!!")
# input fields.
size = input("what size of pizza do you want? L, M, S\n")
pepperoni = input("Do you want pepperoni in it? y or n.\n")
cheese = input("Do you want extra cheese? y or n.\n")
# initiate price variable.
price = 0
# If L is inputted do this.
if size == "L":
    # change price to 25.
    price = 25
    if pepperoni == "y":
        # add 3 to the price if pepperoni is y.
        price += 3
# If M is inputted do this.   
elif size == "M":
    price = 20
    if pepperoni == "y":
        price += 3
# If S is Inputted do this.
elif size == "S":
    price += 15
    if pepperoni == "y":
        price += 2
# If cheeses are needed add 1 to the price
if cheese == "y":
        price += 1
print(f'Your final bill is: {price}$')
