# #decorators(oops)
# #decorators are used to modify a function
# #DECORATORS ARE FUNCTION WHICH TAKE ANOTHER FUNCTION AS A ARGURMENT
# #function in a function
# #called by @

# #fx=function
# #mfx=modified function
# '''
# *args:takes arguements as tuple
# **kwargs:takes arguements as dictionary
# '''
# #write args anf kwargs everytime when u want to pass any arguements

# def greet(fx):
#     def mfx(*args,**kwargs):
#         print("good morning")
#         fx(*args,**kwargs)
#         print("thanks for using this function")
#     return mfx 

# @greet
# def hello():
#     print("hello world")

# #@greet
# def add(a,b):
#     print(a+b)


# hello()    

# greet(add)(1,2)


#suppose there is a function we want that function to print goodmorning before doing any thing stated in that



"""online code mila hai ye prac implementation in ral life ka"""
import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b