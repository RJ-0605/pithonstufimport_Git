
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
        # remember to remove the chicken just for a test

       
        self.otherinfos=otherinfos
        self.serial=VotersID._get_next_serial()  
        


# >>> from elisha_subinherit import *
# >>> r7=VotersA("bread",["orange"],length=25,celsius=-30)
# >>> r7=VotersID("bread",["orange"],length=25)
# >>> r7.volume
# 19550

# OR sthrough subclass all the same the property getter volume is inherited


# >>> from elisha_subinherit import *
# >>> r7=VotersA("bread",["orange"],length=25,celsius=-30)
# >>> r7.volume_ft3
# 19550


    @property
    def volume(self):
        return VotersID.width*VotersID.height*self.length





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

       

        # setting a value to the setter at hte beginning, validating ths setter at the instanciation of the class
        self.celsius=celsius

        

    @property
    def celsius(self):

        return self._celsius + 1


    @celsius.setter
    def celsius(self,value):
        if value>VotersA.Max_Celsius:
            raise ValueError( "Temperature too hot")

        self._celsius = value 



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

    @property
    def volume(self):

        return super().volume-VotersA.Fridge_volume

   
 
   
   #     instead of typing the whole thing below we can just type what is above , it should work because the we calling from the immediate super function the volume getter 

#       return VotersID.width*VotersID.height*self.length - VotersA.Fridge_volume




    
# setting another class to show overiding of setter  

class VotersB(VotersA):

    Min_celsius=-34



    @VotersA.celsius.setter
    def celsius(self,value):
        if not(VotersB.Min_celsius<=value):
          raise ValueError("Temperature too cold ") 

        # this is the object of the setter function being wrapped for celsius setter
        VotersA.celsius.fset(self,value)


# we are going to hash the code below because it repeats something in earlier code which might work but goes against python code of ethics
#    @VotersA.celsius.setter
#    def celsius(self,value):
 #       if not(VotersB.Min_celsius<=value<=VotersA.Max_Celsius):
  #        raise ValueError("Temperature out of range ") 
   #     self._celsius=value

# because VotersA.Max_celsius could have been many hierarchies of classes up and we will have to write all that



    





  