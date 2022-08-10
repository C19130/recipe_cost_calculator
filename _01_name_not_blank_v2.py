# Functions Go Here


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