'''
Functions
def My_function():
    #Do this 
    #Then do this 
    #Finally do this 

    def My_function(something):
    #Do this something
    #Then do this 
    #Finally do this 

Functions with Outputs

def my_function():
    return 3*2            # output = my_function()


'''
# def format_name(f_name, l_name):
#   print(f_name.title())
#   print(l_name.title())
# print(format_name("nilesh","pandey"))

def format_name(f_name, l_name):
  """ Take a first and last name and format it to return the title case version of the name"""
  
  if f_name == "" or l_name == "":

    return "You didn't provided valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  
  return f"Result: {formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name?"),input("What is your last name ?")))