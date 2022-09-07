def not_blank(question, error_message):
  valid = False

  while not valid:
    response = input(question)

    if response == "":
       print(error_message)
    else:
     return response 

# Main routine goes here
name = not_blank("Name of recipe: ",
                "Sorry, this can't be blank - "
                "please enter the name of your recipe")




def int_check(question):

  error = "Please Make sure you have entered a number that is more than"

  valid = False
  while not valid:

    #ask user for number and check it is valid
    try:
      response = float(input(question))

      
      if response <= 0:
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
finalcost = 0

list_num = 0

print()
serving = int_check("How many people does this recipe serve? :")
print()

while ingredient != "":
  
  if ingredient != "":
    ingredient = input("Enter your Item to the List: ")  
    if ingredient == "":
      break
    shoplist.append(ingredient)
    
    price = int_check("What is the price of {}? : $".format(ingredient))
    pricelist.append(price)
    
    weight = int_check("How many grams/milliliters of {} can you get for ${} :".format(ingredient, price))
    weightlist.append(weight)

    need_weight = int_check("How many grams/milliliters of {} do you need for the recipe :".format(ingredient))
    needweightlist.append(need_weight)
    print()
    list_num += 1
    
    
    
    
print()
print("This is the list of ingredients needed: ")
print()


for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19, 20, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]:
  if i == list_num:
    break
  
  print("*** {} ***".format(shoplist[i]) , "This item weighs {}g/ml".format(weightlist[i]) , "at ${}/{}g/ml,".format(pricelist[i], weightlist[i]), "for the recipe this costs ${}".format(pricelist[i] / weightlist[i] * needweightlist[i]))
  print()
  finalcost += (pricelist[i] / weightlist[i] * needweightlist[i])

print("The total cost of this recipe is {},".format(finalcost), "The cost per serving is {}".format(finalcost / serving))