
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


    def calc_volume(self):
        
        return (VotersID.width*VotersID.height*self.length)


    @property
    def volume(self):
        return self.calc_volume()

    

    





class VotersA(VotersID):
    
    Max_Celsius=4.0

    
    Fridge_volume=100



    @staticmethod
    def c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod 
    def f_to_c(fahrenheit):

        return (fahrenheit-32) * 5/9 






    def __init__(self,personal_infodata,otherinfos,length,celsius):
        super().__init__(personal_infodata,otherinfos,length)

       


        self.celsius=celsius

        

    @property
    def celsius(self):

        return self._celsius + 1



    def set_celsius(self,value):

        if value>VotersA.Max_Celsius:
            raise ValueError( "Temperature too hot")
        self._celsius = value

    @celsius.setter
    def celsius(self,value):
       
        self.set_celsius(value) 




    @property
    def fahrenheit(self):
        return VotersA.c_to_f(self.celsius)


    @fahrenheit.setter
    def fahrenheit(self,value):
        self.celsius = VotersA.f_to_c(value)



#   test format used uptil now 
# >>> from elishatest_subclass import *
# r7=VotersA("bread",["orange"],length=25,celsius=-30) 
# >>> r7.celsius
# -29


    # we can override the property getter "volume" in immediate superclass from here 

    
    def calc_volume(self):

        return super().calc_volume()-VotersA.Fridge_volume

   
 
  

class VotersB(VotersA):

    Min_celsius=-34



    
    def set_celsius(self,value):
        if not(VotersB.Min_celsius<=value):
          raise ValueError("Temperature too cold ") 
 
 #       no need for self._celsius=value 
 # as this class has already inherited that
 #  it just adds the necessary upgrades thats all
 # no need to point where the value is 


      #  this inclusion below just adds the checker for the maximum celsius
        super().set_celsius(value)






    

#  so we now know how to overide the ff.in asubclasses 
# although  inherited from superclasses 
# 
# A.  overide getters
# B. overide setters
# C. overide methods in getters
# D. overide methods in setters
# E. overide methods which belongs to a setter with same method in another class
#    so as to enable adding of more functionalities or check for duplicate information