"""
class school:
   a=4      # class variable/static variable
   def_init_(self,m,s)
    self.m= m     # inastance variables (which are present in init())
    self.s = s    # init functions call by automatically
    
c1=school(80,90)
print(c1.m)
print(c1.s)
print(c1.a)
print(school.a) # you can access this variable using this two methods.

   # VARIABLES
# THERE ARE TWO TYPES OS VARIABLE  - class VARIABLE / STATIC VARIABLE
# instance variable are object specific -Instance variable
# class variables are present inside the class but outside the init functions.
"""

                 # METHODS  #
"""
# THERE ARE THREE TYPES OF METHODS IN PYTHON - INSTANCE METHODS
 # another one is class method and Static method..
class school:
     a=3           # class variable which canot directly access
    def_init_(jesus,m,s):    #init method
       jesus.m=m
       jesus.s=s

    def output(jesus):      # instance method
       print(jesus.m,jesus.s)

    @classmethod
    def output2(cls):       # class method which access class variables
        print(cls.a)        # you can access it by cls
    @staticmethod
    def output():            # static method  
        print('this is static method')

c1=school(70,80)  

c1.output()
c1.output2()
c1.output3()

"""
                   # INHERITANCE #

class school:                  # parent class
  def__init__(self,schoolname):
     self.schoolname=schoolname
  
  def name(self):
     print(self.schoolname)

class student(school):   # here child class it inherit from school class
    
   def__init__(self,f,l,schoolname)   # it override the parent init method
       self.f=f
       self.l=l
     school.__init__(self,schoolname)  # here we can access init of parent.
   
   def name(self):         # here is the method override
     print(self.f)        # here i am using this to print the first name.
     school.name(self) # here you can access your parent class same method

x=student("xyz"," abc","schname")     # here we initialize the object of                 
                                      # child class
print(x.f,x.l)                        # call the methods of child class
x.name()                              # call the methods of parent class

                   # SUPER METHOD  #

# Here you can use super() keyword to access the parent class objects.


class school:                  # parent class
  def__init__(self,schoolname):
     self.schoolname=schoolname
  
  def name(self):
     print(self.schoolname)

class student(school):   
    
   def__init__(self,f,l,schoolname)   
       self.f=f
       self.l=l
     super().___init_(schoolname)  # by the use of super().
   
   def name(self):        
     print(self.f)        
     super().name() 

x=student("xyz"," abc","schname")                     
                                      
print(x.f,x.l)                        
x.name()                         











       