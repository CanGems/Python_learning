"""
#TUPLE CONTINUED....

a=('d',10,"subha")
b=tuple(("candy",'gagul',True,False)) #constructor
print(a)
print(b)

z=("s")
print(type(z)) #string

z=('subha',)
print(type(z)) #tuple are unchangeable i.e itoms add, substact etc not posble
               # duplicates are allowed
print(len(b),b)
print(a[0])
print(a[1:3]) #last index excluded
#if you want to print the last index you should give one index more than total
# if you not mentioned the first index then it will count from 0.

print(a[-4:-1])

#IF YOU WANT TO CHANGE TUPLE ITOMS YOU HAVE TO CHANGE IT TO LIST..
# then converted it into tuple and print it.

l=list(a)
l[1]='e'
l.append(9)
#l.remove(9)
d=tuple(l)
print(d)

#UNPACKING/packing TUPLE...
# packing means when you create a tuple all elements in a single ().
#unpacking means we are trying to extacting values from packing

v,m,n=a
print(v,m,n) # means here all elements are not enclose in a brackt

IF YOU WANT TO UNPACK ALL ELEMENTS BUT HERE YOU PROVIDE LESS NOO OF VARIABLES THEN NO NEED TO WORRY ABOUT SYNTAX ERROR BCUZ YOU SHOULD PROVIDE THIS SYNTAX EX- IN TUPLE YOU HAVE 5 ELEMENTS AND YOU GIVE 3 VARIABLES FOR UNPACKING THEN LET - print(s,d,*e)
in *e all last 3 elements will come and will not show syntax error..
not necessary you will provide * only before the last variable you can provide anywhere as you wish.

 

#JOIN TWO TUPLES.
f=a+b
print(f)
# if you want to delete the tuple then the syntax is- (del f)

"""
                       # SETS {} # 

"""
ANY DATA TYPE ALLOW IN SETS

set1={1,2,'subha',3,True}
set2={"a",34,False}
print(set1,set2)
set3=set(("candy",1,67,54,32)) #set constructor using to create a set.
print(set3)
print(len(set3)) # set are not following a perticular order./under,unindex 
 # unchangable, but you add and remove elements after set creation.
#USING IN KEYWORD WE CAN FIND THE ELEMENTS PRESENT IN SETS OR NOT.

print(8 in set1) # showing false..

set1.add(90)
print(set1)
set1.remove(1) # you can use discar() method..without giving any error.
print(set1) # remove() show error when we try to remove something that not
            # present in set.  you can use pop() but its danger...
            # clear() is use to clear all elements in set.
           #  del() also use to delete a set.  
# WANT TO JOIN SETS

set1.update(set2)
print(set1)

set1.union(set2)
print(set1)

set1.intersection(set2)
print(set1)
set2.symmetric_difference_update(set3) #it prints except common elements.
print(set2)
set2.intersection_update(set1)
print(set2)

"""
  """                  
                 # DICTIONARY {key:value} #

  #here we can specify the itoms in key value pair
a={"name" : "subha",
"age":22, "pass" : 90}
print(a)

# its are changable..its unorderd. we cants assess using index.
# duplication are not allowed (key) .last will be print.

print(len(a))

print(a["name"])
print(a.get('name')) # here both we can extract the value using key.

print(a.keys())
print(a.values())

print(a.items()) # tuples are using list

a["name"]="candy" #inthis way you can change/update the value.
print(a)

a.update({"name":"subhalaxmi"})  # using update method we can change also.
print(a)

a["branch"]="chemical" #add extra key and value.
print(a)

a.pop("pass") #remove elements from dictionary
print(a)
del a["name"]
print(a)


# for emplty dictionary-> a.clear()
#fully delete dictionary -> del a

#del a
print(a)

b=a.copy() # copy all itoms to another dictionary
print(a)

b=dict(a)  # same here also using to copy
print(b)

       # nexted dictionary #
# here is a outer dictionary and its like nexted loop..

school={
   "sdt1" : {
      "name": "rahul",
      "year": 1998
    },
   "std2": {
       "name": "sambit",
        "year": 1998
   },
   "std3": {
         "name":"cchancal",
         "year":1999
   
   }
}

print(school)

"""


  


                




