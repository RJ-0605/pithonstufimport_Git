class VotersID:
    next_serial=None

    agestatus=None

    @staticmethod
    def compile_userdata(arg1,arg2):
       
        print ('lets begin somewhere, what do you think')

        VotersID.age_validator(arg2)

        if VotersID.agestatus is True :

            serial
            VotersID.get_data(arg1)
            print ('success')


        else :

            return print ("you are unable to proceed with registration due to wrong age, go home and come try again when you are older ")





    @classmethod

    def _get_next_serial(cls):

        print("a serial will now  be generated for you ")
        
        if cls.next_serial is None:
            
            

            cls.next_serial=1
            

        else:
            cls.next_serial += 1
        
        result=cls.next_serial
        
        
        return print(result)


    @classmethod
    def age_validator(cls,y):
        if int(y) < 18:
            print ("you are uneligible to vote")
            cls.agestatus=False
        else: 
            print ("you can go ahead and register")
            cls.agestatus=True


    @staticmethod
    def get_data(x):
            
         # x   is the personal_infodata
        print (x)

       

        print ("enter date in this format ,dd/mm/yyyy")
        prompt = ">"
        date_of_birth=input(prompt)

        j=list()
        j.append(date_of_birth)

        
        return print(j)





    def __init__(self,personal_infodata,age):
        
        self.personal_infodata=personal_infodata
        self.age=age
        

        self.compile_userdata=VotersID.compile_userdata( personal_infodata,age)