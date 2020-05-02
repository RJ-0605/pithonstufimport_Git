
class VotersID:
  
#  Most fundamental changes occur here before merged with master branch 
    next_serial=None 

    personal_infodata=None

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
        return result

    @classmethod
    def compile_userdata(cls,personal_info,age )




    @classmethod
    def age_validator(cls,age):
        if int(age) < 18:
            print ("you are uneligible to vote")

        else: 
            print ("you can go ahead and register")

        return cls(age)

    @classmethod
    def create_empty(cls,personal_infodata):

        return cls (age,personal_infodata=list())

    # @classmethod
    # def create_with_items(cls,owner_code,items):
    #    return cls (owner_code,contents=list(items) )

#    items can store most personal information in a list and can be called from there 
#    or assigned to a variable in the future for the instance or for the staticmethods

    def __init__(self,personal_info,age):
     # self.date_of_birth=date_of_birth
      self.personal_info=personal_info

      self.age=age
      self.personal_infodata=VotersID.personal_infodata
      self.user_info=VotersID._get_next_serial()