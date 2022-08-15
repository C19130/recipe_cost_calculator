#start of the loop

# initialise loop so that it runs at least once
shoplist = [] 

ingredient = "true"


while ingredient != "":
    ingredient = input("Enter your Item to the List: ")
    shoplist.append(ingredient)
print("That's your Shopping List")
print(shoplist)