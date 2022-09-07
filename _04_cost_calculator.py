def int_check(question):

  error = "Please Make sure you have entered a number that is atleast 0"

  valid = False
  while not valid:

    #ask user for number and check it is valid
    try:
      response = float(input(question))

      
      if response < 0:
        print(error)
      else:
        return response

    except ValueError:
      print(error)


      

# main routine goes here



#start of the loop

# initialise loop so that it runs at least once
shoplist = []
pricelist = []
weightlist = []
needweightlist = []
ingredient = "true"

list_num = 0

while ingredient != "":
  
  if ingredient != "":
    ingredient = input("Enter your Item to the List: ")  
    if ingredient == "":
      break
    shoplist.append(ingredient)
    
    price = int_check("What is the price of {}? : $".format(ingredient))
    pricelist.append(price)
    
    weight = int_check("How many grams of {} can you get for ${} :".format(ingredient, price))
    weightlist.append(weight)

    need_weight = int_check("How many grams of {} do you need for the recipe :".format(ingredient))
    needweightlist.append(need_weight)
    
    list_num += 1
    
    
    
    
print()
print("This is the list of ingredients needed: ")
print()


for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19, 20, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]:
  if i == list_num:
    break
  
  print("This item is {}".format(shoplist[i]) , "This item weighs {}g".format(weightlist[i]) , "at ${}/{}g,".format(pricelist[i], weightlist[i]), "for the recipe this costs ${}".format(pricelist[i] / weightlist[i] * needweightlist[i]))
  print()