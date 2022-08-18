             # IF ELSE, ELIF STATEMENT #

a=20
b=30

if a>b:
  print("a is less than b")
elif a==b:
  print("both are equal")
else:
   print("a is greater than b")


# you can print it in a single line also

if a<b : print("a is less than b")

print("a is less than b") if a<b else print("b is less than a")

if a<b and a<5:
  print("yes")
else:
  print("no")

# NESTED IF
if a>5:      # outer if...
  print("above 5")
  if a>20:   # inner if.....
    print("and also above 20")
  else:
    print("but not above")

