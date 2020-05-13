
class VotersID:

#  Most fundamental changes occur here before merged with master branch 
    next_serial=None 

    height=23
    width=34

    @classmethod

    def _get_next_serial(cls):

        
        if cls.next_serial is None:
            

            cls.next_serial=1
            return cls.next_serial

        else:
            cls.next_serial += 1
        
        result = cls.next_serial 
        
        return result

        








       
        # return result  we will only add this when we want it to run automatically
        # i am adding this text because i am running test on changes with github
       #  hello we will be gerting you some chicken
       # checking to see if main branch affects branch help
        #return result
    
    @classmethod
    def create_empty(cls,personal_infodata,*args,**kwargs):

        return cls (personal_infodata,otherinfos=None,*args,**kwargs)





    @classmethod
    def create_with_items(cls,personal_infodata,length,items,*args,**kwargs):
        return cls (personal_infodata,otherinfos=list(items),*args,**kwargs)


    def __init__(self,personal_infodata,otherinfos,length):
        self.personal_infodata=personal_infodata
        self.length=length

        self.otherinfos=otherinfos
        self.serial=VotersID._get_next_serial()   



    @property
    def volume_ft3(self):
        return VotersID.width*VotersID.height*self.length





class VotersA(VotersID):
    
    Max_Celsius=4.0

    




    @staticmethod
    def c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod 
    def f_to_c(fahrenheit):

        return (fahrenheit-32) * 5/9 






    def __init__(self,personal_infodata,otherinfos,length,celsius):
        super().__init__(personal_infodata,otherinfos,length)

       


##############################################################################
      
# or we can put this parameter in a #### class property #### whichmakes its able for us to aassign values to 
# this relation , by the help of the setter which will enable us to do that  
#   if this relation is not set before the self.celsius relation or self._celsius relation 
#  which is to enable us pick from the instance it woiuld be quite tough 
# and wont execute 

      #  if celsius >VotersA.Max_Celsius:
         #   raise ValueError( "Temperature too hot")

#####################################################################

# this triggers the setters called celsuis and sets  if there is any (which there is is this case
#  so it assigns the celsuis argument value to the celsuis setter to work on it ,
#  the setter function now assigns the value to the self._celsius as its value , 
#   all this happens during instanciating of a class  )
#  other than that if there is not it creates an instance of the argument celsuis 
# to be used in the future 
        self.celsius=celsius

        
# we can see from the result of this getter property 
# that the class instance picks its value of self.celsius ,or for eg. r7.celsius
# as the value of this getter function celsius

    @property
    def celsius(self):

        return self._celsius + 1


    @celsius.setter
    def celsius(self,value):
        if value>VotersA.Max_Celsius:
            raise ValueError( "Temperature too hot")

        self._celsius = value 

# so currently when the class is initialised the value of the setter function is 
#     is currently holding the 


# anytime this gettter is called in just this manner   eg. kofi.fahrenheit it checks the value of self.celsuis
#  before returning it or woking on the value of self.celsuis
#  before returning the outcome 

#  Note because we have validated ,or called the setter function celsius at the beginning as self.celsius
# this setter celsius contains a specific value which is thrown everytime we call it  
# note the value can be gotten when we call the getter function of celsius ,
#  which might add modifications to the value b4 returning ,it depends on what you functions you placed at the recieving end of the celsius getter, and what they are doing to the value.
# the fahrenheit getter when executed immediately after instanciating class
# , without setting a new value using the fahrenheit setter , returns and works with the original value of the self.celsius getter
# thus the self.celsius getter is acting as an attribute of the class which stores a value and can be called

    @property
    def fahrenheit(self):
        return VotersA.c_to_f(self.celsius)

        # def fahrenheit(self):
        #  
        

 #   this setter is called when the setter function is assigned a value to work on
 #  in this manner eg. kofi.fahrenheit(23)
    @fahrenheit.setter
    def fahrenheit(self,value):
        self.celsius = VotersA.f_to_c(value)



#   test format used uptil now 
# >>> from elishatest_subclass import *
# r7=VotersA("bread",["orange"],length=25,celsius=-30) 
# >>> r7.celsius
# -29



    



    





  