  # FILE HANDLING   ##
"""
a=open ("1.txt", "r")   # read mode of file . store in a variable a
#print(a.read())         # open method is use to open the file .
                        # read() is use to print file text
#print(a.read(10))     # it will return first 5 character from the text file

print(a.readline())    # it will read first line of the text file.

print(a.readline())
a.close()              # close the file

# USING FILE HANDELING WE CAN WRITE SOMETHINGS.
# USING APEND,
"""
"""
a=open ("1.txt", "a")     # here pass the variable..
a.write("file handling")  # here we write something
a.close()

b=open ("1.txt", "r")     # but when the time of open it wil use another var.
print(b.read())
#b.close()
"""
"""
a=open ("1.txt", "w")     # here we pass the w for write.(append)
a.write("file handling")  # here we write something
a.close()

b=open ("1.txt", "r")     # but when the time of open it wil use another var.
print(b.read())
#b.close()
"""

   # IF YOU WANT TO DELETE PERMANENTLY THE FILE THEN USE OS.. #
"""
import os    # modele os should be import..
os.remove("1.txt")

b=open ("1.txt", "r") # but when the time of open it wil use another   var.
print(b.read())
#b.close()

# if you want to create a new empty file then..

a=open ("2.txt", "x")     # here pass the variable x to create empty file

b=open ("2.txt", "r") # but when the time of open it wil use another   var.
print(b.read())
#b.close()
"""

a=open ("2.txt", "w")
a.write("subhalaxmi")
a.close()

b=open ("2.txt", "r") # but when the time of open it wil use another   var.
print(b.read())
#b.close()



                   # CLASS AND OBJECTS  #

x=1
y="s"
z=1.03
a=True

print(type(x))
print(type(y))
print(type(z))
print(type(a))  # all are class

# class is a blue print so using this we can creqte an object.
"""
class subha :  # user defined class
  pass         # it will not show error
s1=subha()     # object of class
"""

class school:     # class ccreation

  def_init_(self,m,s):  #inside a class a function
      self.math = m        # self refers current instance of class..
      self.science = s

c1=school(90,89)         # here also object intialize
print(c1.math)
 













