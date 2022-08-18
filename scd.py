"""
#STRING FUNCTIONS()

z="i like sour foods"
print(z.upper());

y=" I PLAY BADMINTON  "
print(y.lower())

#TO REMOVE WHITE SPACE BETWEEN THE WORDS

print(y.strip())
print(y.replace("I","A"))
print(z.split("s"))

#IF YOU WANT TO CONCACT AN INTEGER WITH A STRING THEN WE HAVE TO GIVE A CURLY
#BRACKET END OF THE STRING {} EX-(V="SUBHA {} ") you can place the integer 
#wherevever you want.ex -(q="{} candyy")

w="{0} sub {1} ha {2} "
r=5
p=10
q=13
print(w.format(r,p,q))

"""
"""
# PYTHON OPERATORS
# if you work with an operands then we need operators

a=10
b=20
c=0
print ("arithmetic operators")
c=a+b
print(c)

c=a-b
print(c)

c=a*b
print(c)

c=a%b
print(c)

c=a/b
print(c)

c=a**b #(is use for exponential calculaton) i.e (a^b)

print(c)

c=a//b  #(it is use for quotient calculation but it gives the decimal                        #         before values) ex-( 12/5=2.4 )but the result is (2)
print(c)

# COMPARISION OPERATOR

print ("comparison operators ")
if(a==b):
  print("both are equal")
else:
  print("both are not equal")
# LIKE THAT WE CAN DO (<,>,!=,<=,>=)


# ASSIGNMENT OPERATORS
print("assignment operators")
a=10
b=2
c=a+b
print(c)
c += a #(c=c+a)
print(c)

# LIKE THAT YOU CAN DO (-=,*=,/=,**=,//=) its so easy to use....

# BITWISE OPERATOR (&, |, ^, ~, <<, >>)

print ("bitwise operators") #(...32 16 8 6 4 2 1)values based on this...
a=11 #(10011)
b=3 #(0011)
c=a & b
print (c) #(0011)-> 3
c=a|b
print((c==a|b))
print(c) #(10011)->11
c=a^b
print(c) #(xor is for 1-1->0, 0-0->0) ans(100000)->10
c=~a
print(c)  
#(not is use to change 1->0, 0->1)here using 2s #complement->that # means 1st find out the 1s comlement(change 1->0,0->1) then add 1 in ans) 
c= a<<2 #(it is left shift by two)
print (c)
c=a>>2  #(right shift)
print(c)

# MEMBESHIP OPERATORS (in,not in)

abc="i love you jesus"
if "love" in abc:
  print('yes')
else:
  print('not present')

#IDENTITY OPERATORS(is, is not)*it compares objects based on there identity
# it shows the same memory location (returns boolean values)

x=134
y=134
print(id(x),id(y))
print(x is y)
print(x is not y)

"""
           #      LIST []     #
"""

a=[1,"subha",2,3,2]
b=list(('candy','gems'))  # by using list constructor
print(a,b)

#LIST HAS SO MANY FEATURES ->IT FOLLOWS SOME ORDER
#->ITS CHANGABLE -> DUPLICATION ARE ALLOWED

#LIST METHODS/function()
print(len(a))
print(len(b))

# c=[true,false]  # you can put whatever you want data type values...
print(a[3]) # put the index  in the[].->it gives the values...
print(a[1:4])  # it will show you from which index to which index you want.
               # 1st index included but last index excluded....
print(a[:2])

# NEGATIVE INDEXING 

print(a[-5:-1])
a[1]=11  # single index element replace
print(a)
a[1:3]=[23,12]  # replace itoms in a perticular range..
print(a)
a.append(15)   # this method is use add vlaue at end position..
print(a)

a.insert(1,"subhaa")  # insert at a perticular position
print(a)

a.remove(15)  # remove() is use to remove perticular value.
a.pop(1)  # but if you pass some index value with that then it only remove
print (a)
a.pop() # this method only remove the last index...
print(a)

del b[0]  # this del keyword also use to delete perticular index value
print(b)

#del a  # it completely delete the list.
print(a)

# a.clear()  # it clear all the elements from the list.
print(a)

a.sort()  # this sort() is use to sorting in ascending orders.
print(a)
a.sort(reverse= True)  #this syntax use for descending orders..
print(a)

#IN CASE OF STRINGS THE SORTING ARE CASE SENSITIVE. WE USE ONLY sort()
# if we want to a perticular case sesnisitive then we use #sort(key=str.lower)..

a=['subha', 'gagul','papu','Hari']
a.sort()
print(a)
a.sort(key=str.lower)
print(a)

c=a.copy() # its use to copy one list element to another list element..
print(c)
z=list(c)  # this also use to copy the list elements...
print(z)

h= c+z   #THIS METHOD IS USING TO JOIN TWO LIST..
print(h)

c.extend(z)  # THIS METHOD IS ALSO JOIN TWO STRINGS.. 
print(c)
 
"""

                        # TUPPLES () #
a=(1,2,3,4)
b=tuple(('a','b','c','c'))
print(a,b)
z=("s")  # this variable type is string..
z=('s',)  # after adding  comma it is behave as a tupple..
print(type(z),z) # this will show that the type as well as tuple elements..

# THE FEATURES OF TUPLE IS THE ITOMS ARE (UNCHANGABLE)...
# ITS IN OREDERD MANNER..-> DUPLICATES ARE ALLOWED..

print(len(a))

