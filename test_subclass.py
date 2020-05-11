
class VotersID:

#  Most fundamental changes occur here before merged with master branch 
    next_serial=None 

    @classmethod

    def _get_next_serial(cls):

        
        if cls.next_serial is None:
            

            cls.next_serial=1
            return cls.next_serial

        else:
            cls.next_serial += 1
        
        result=cls.next_serial
        
        return result 

        








       
        # return result  we will only add this when we want it to run automatically
        # i am adding this text because i am running test on changes with github
       #  hello we will be gerting you some chicken
       # checking to see if main branch affects branch help
        #return result
    
    @classmethod
    def create_empty(cls,owner_code,*args,**kwargs):

        return cls (owner_code,contents=None,*args,**kwargs)





    @classmethod
    def create_with_items(cls,owner_code,items,*args,**kwargs):
        return cls (owner_code,contents=list(items),*args,**kwargs)


    def __init__(self,owner_code,contents):
        self.owner_code=owner_code
        self.contents=contents
        self.serial=VotersID._get_next_serial()   






class VotersA(VotersID):
    
    Max_Celsius=4

    def __init__(self,owner_code,contents,celsius):
        super().__init__(owner_code,contents)
        if celsius >VotersA.Max_Celsius:
            raise ValueError( "Temperature too hot") 
        self.celsius=celsius



  