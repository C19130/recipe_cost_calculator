""" Recipe Cost Calculator, Cade Young, 18/09/22, allow the user to calculate the toatal cost of a recipe aswell as cost per serving"""

import os
import time

# Instructions, print the instructions for the user to view for 30 seconds before clearing the output and continuing with the outcome
def instructions():
  print(">>>>>Instructions<<<<<")
  print("Input the name of your recipe and the serving size.")
  print("Input the items of your recipe, and once prompted") 
  print("input the price of the item and the measurements")
  print("Once you have completed your list press the Enter Key")
  print("And the screen will wipe. Once the screen has wiped")
  print("it will print the calculationsfor the individual items,")
  print("and finally the price of the entire recipe as a whole and per serving")
  time.sleep(30)
  os.system('clear')
  return ""

instructions()

# Name Not Blank, version 2, ask user to input the name of their recipe, and provide an error if the input is blank
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



# Price Loop, version 2, custom error message to be used throughoput the outcome whenever numbers are involved to provide an error to users when they have inputted a word or a number less than zero when asked to provide a number
def int_check(question):

  error = "Please Make sure you have entered a number that is more than 0"

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



# Start of the loop

# Initialise loop so that it runs at least once
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

time.sleep(1)
os.system('clear')

# Ingredient Loop, version 3, ask user to input their items and item measurements to their recipe list and storing inputs into appropriate lists for later output and calculations
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
    
    
    


os.system('clear')
print()
print("This is the list of ingredients needed: ")
print()

# Cost Calculator, version 2, calculate and output the total and per serving costs of the users recipe aswell as a price breakdown of the individual ingredients
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19, 20, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]:
  if i == list_num:
    break
  
  print("*** {} ***".format(shoplist[i]) , "This item weighs {}g/ml".format(weightlist[i]) , "at ${}/{}g/ml,".format(pricelist[i], weightlist[i]), "for the recipe this costs ${}".format(pricelist[i] / weightlist[i] * needweightlist[i]))
  print()
  finalcost += (pricelist[i] / weightlist[i] * needweightlist[i])

print("The total cost of this recipe is {},".format(finalcost), "The cost per serving is {}".format(finalcost / serving))