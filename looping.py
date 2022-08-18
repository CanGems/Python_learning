                       # LOOPING STATEMENT #
""" 
                 # WHILE LOOP #
a=10
while a<=20 :
   print('hello jesus')
   a=a+1

   if a==15:
      # break  ( you can give the break statement not depend upon condition).
      #continue  if you give the continue statement then it dont obey 2nd con.
else:
  print('my lord') # after printing while statement it come to the else.

"""

                # FOR LOOP #
"""
# for loop is using to iterate over a sequence of data. 
a=[1,2,3,4,5]

for b in "subhalaxmi" :
  if b=='l': #break
     continue   #( here the perticular character cannot be print.i.e 'l')
  print(b)

for b in range(2,5,2):  # you can start with some range..2 to 5,and incre by 2
  print(b)

          # NESTED FOR LOOP #
x=[1,2,3,4,5]
y=[6,7,8,9]
 
for a in x:      # outer for loop
   for b in y:   # inner for loop
     print(a,b)  # here you can also print (b,a)
"""


                        # FUNCTIONS #
"""
# its a block of code.. we trying to paas the parameters in function.(def)

def school() :
  print('functions')
school()  # function call...you can call the function more times.

def college(a) : # here paas the variable
  print(a)
college(" i have completed my college") # whatever paremeter you paased.

def shop(a,b,c,d):
   print(a,b,c,d)
shop('toy',3,4,5) # you can pass any type of value. defult paas the paramet

def sch(*a) :  # due to this ashtriks mark it will behave like a tuple.
  print(a)
sch(1,2,3,4,5,6,7,8)

def ss(a,b):
  print(a,b)
ss(b=10,a=20)

def cc(**a):  # its behave as a key value pair.
  print(a)
cc(b=2,c=3)   # here its behave like a key value pair. 

def dd(a="subha"):  # defult parameter pass.
  print(a)
dd()  # when you not pass any parameter here then you should paas difult.

def double(a):
  return a*2
print(double(2))  # it return the values. or you can do it-> b=double(2)
                   # and then-> print(b)


                   

                       # RECURSION  #
# You have to mention base conditions. othewise it show stack overflow.

def abc(n):  # calling function
  if(n>1):
    t=n+abc(n-1)
    print(t)
    return t
    
  else:
    return 1   # base condition.
  
abc(4)      # caller function


                  # SCOPE IN PYTHON #

a=10     # Global variable you can access it everywhere
 
def abc():
   print(a)

abc()


def abc():
  a=13     # local variable we cannot acess it outside the function
  print(a)
abc()
#print(a)


global z     # this global is a key word use in python
def ab():    # outer funtion 
  a=33
  z=5         # here it acst as local z=5
  def cc():   # inner function (it can access the outer variable)
    print(z)
  cc()
z=9         # here it act as a global
print(z)
ab()

"""


                  







 



