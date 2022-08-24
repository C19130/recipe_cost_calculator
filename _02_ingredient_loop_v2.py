#start of the loop

# initialise loop so that it runs at least once
shoplist = [] 

ingredient = "true"
loop_num = 0

while ingredient != "xxx":
  ingredient = input("Enter your Item to the List: ")
  shoplist.append(ingredient)
  loop_num += 1
  if loop_num == 4:
    break
print("This is the list of ingredients needed: ")
print(shoplist)