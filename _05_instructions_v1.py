import os
import time

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