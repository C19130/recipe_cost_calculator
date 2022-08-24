#start of the loop

# initialise loop so that it runs at least once
shoplist = []
pricelist = []
ingredient = "true"

list_num = 0

while ingredient != "":
  
  if ingredient != "":
    ingredient = input("Enter your Item to the List: ")  
    if ingredient == "":
      break

    shoplist.append(ingredient)
    price = input("What is the cost of {}? :".format(ingredient))
    pricelist.append(price)
    list_num += 1

print()
print("This is the list of ingredients needed: ")
print()


for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19, 20, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]:
  if i == list_num:
    break
  print(shoplist[i], pricelist[i])