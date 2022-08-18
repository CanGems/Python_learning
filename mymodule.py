       # PYTHON FUNCTIONS  #
def odd_even(x):
   if x%2==0:
      print(x,"is even")
   else:
      print(x,"odd")
odd_even(5)
"""
# LAMBDA FUNCTION
 g=lambda x:x*x 
    print(g(5))
"""
"""
l1=[25,36,47,59]
 final_l1=list(filter(lambda x:(x%2!=0),l1))
  final_l1
"""

             # TRY EXCEPT BLOCK( Exception handeling ) #
try:        # it will text  the error if present
  print(s)
except NameError :
   print("variable x is not defined") # it handle the exception of try block.
except:
   print("something else went wrong")


print("abcdefghi")

    # ELSE BLOCK IS PRINT ALL STATEMENT IF ITS NOT ERROR..
try:
 print("subha")
except:
  print("something went wrong")
else:
  print("no error")

# FINALLY BLOCK (its run all the code )

finally:
  print('finally block executed sucessfuly') 

# ********

a=4
b=0

try:
  
  c=a/b
#except ZeroDivisionError:
    #print('ZeroDivisionError')
#except ValueError :
   #print('invalid literal for int() with base 10')

except Exception :         #(exception super class-> except:)
    print("exception handeld")

print("done")


   # BUILD IN MATHEMATICS  ##


print(min(10,2,30))
print (max(10,3,45))
print(abs(-9))   # absolute value(+ve value)

x=2
y=3
print(pow(x,y))  # power 2^3

import math       # module

print(math.sqrt(45))    # squre root

print(math.ceil(2.35))  # 2.35 upper value ie 3
print(math.floor(2.35))  # 2.35 floor value means lower value ie 2
print(math.pi)            # return pi value
print(math.factorial(5))   # find factorial
print(math.sin(5))          #
print(math.cos(5))
print(math.tan(5))

     




