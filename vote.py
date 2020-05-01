
class VotersID:

    index_serial=None

    @classmethod

    def _get_index_serial_increment(cls):
        
        nonlocal index_serial

        if index_serial is None:
            

            index_serial=1
            return None

        cls.index_serial += 1
        result=cls.index_serial
        
        return result 
        #  #we will only add this when we wantit to run automatically
        # i am adding this text because i am running test on changes with github
       #  hello we will be gerting you some chicken
       # checking to see if main branch affects branch help
    
    
    
    @classmethod

    def _getvoters_IDno(cls):
        return None


    @classmethod
    #def create_empty(cls,owner_code):

    #    return cls (owner_code,contents=None)

    @classmethod
    #def create_with_items(cls,owner_code,items):
    #    return cls (owner_code,contents=list(items) )


    def __init__(self,date_of_birth,village_born,parents_name,age):
      self.date_of_birth=date_of_birth
      self.village_born=village_born
      self.age=age
      self._getvoters_IDno=VotersID._getvoters_IDno()     