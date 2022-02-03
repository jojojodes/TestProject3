def func():
    print('hello world!')  # this is a complete function

func()  # this calls the function above


# func_a()  is simply naming the next function (ie. func_a(), func_b(), func_c(), ..etc..)
def func_a(text):
    print(text)
    
# func_a() # TypeError: func_a() missing 1 required positional argument: 'text'

func_a('hello world!!') # Added text of 'hello world' to the ()


# ______________________________________________________ 

def func_a(text, text2):
    print(text)
    print(text2)

func_a('hello me!', 'hello you!') 

# Prints the argument we gave the function
# hello me!
# hello you!

#________________________________________________________

def func_b(text='default text'):
    print(text)

func_b() # all text entered in this function being called will print to screen over specified in the def func_b() line.
            
func_b('custom text')  # for example func_b('custome text') will print 'custom text' as it is being called over the default.

# All above functions after save and running this file will print the following...
    # hello world!
    # hello world!!
    # hello me!
    # hello you!
    # default text
    # custom text