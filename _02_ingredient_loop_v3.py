#start of the loop

# initialise loop so that it runs at least once
shoplist = []
ingredient = "true"

list_num = 0

while ingredient != "":
  
  if ingredient != "":
    ingredient = input("Enter your Item to the List, or press enter when you have finished: ")

    if ingredient == "":
      break
    
    shoplist.append(ingredient)
    list_num += 1
    
print()
print("***  This is the list of ingredients needed:  ***")
print()


for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
  if i == list_num:
    break
  print(shoplist[i])