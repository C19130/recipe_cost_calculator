# Functions Go Here


def not_blank(question):
  valid = False

  while not valid:
    response = input(question)

    if response == "":
      print("Sorry - This can't be blank")
    else:
      return response 


# Main routine goes here
name = not_blank("Name of recipe: ")