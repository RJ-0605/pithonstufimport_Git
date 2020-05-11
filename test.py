class VotersID:
    next_serial=None

    agestatus=None

    @staticmethod
    def compile_userdata(age_val,agestatus,serial,get_data):
       
        print ('lets begin somewhere, what do you think')

        age_val()

        if agestatus is True :

            serial
            get_data
            print ('success')


        else :

            return print ("you are unable to proceed with registration due to wrong age, go home and come try again when you are older ")


    @classmethod

    def _get_next_serial(cls,personal_infodata):

        
        if cls.next_serial is None:
            

            cls.next_serial=1
            return cls.next_serial

        else:
            cls.next_serial += 1
        
            result=cls.next_serial
        
        
        return print (result)
        

    @classmethod
    def get_data(cls,personal_infodata):
            
    
        print (personal_infodata)

        personal_infodata = list()
        print ("enter date in this format ,dd/mm/yyyy")
        prompt = ">"
        date_of_birth=input(prompt)
        personal_infodata.append(date_of_birth)

        
        return print(personal_infodata)


    @classmethod
    def age_validator(cls,age):
        if int(age) < 18:
            print ("you are uneligible to vote")
            VotersID.agestatus=False
        else: 
            print ("you can go ahead and register")
            VotersID.agestatus=True
        








        



    def __init__(self,personal_infodata,age):

       # self.age=age

        self.personal_infodata=personal_infodata
        
        self.serial=VotersID._get_next_serial(personal_infodata)

        self.compile_userdata=VotersID.compile_userdata( serial=VotersID._get_next_serial(personal_infodata),age_val=VotersID.age_validator(age=age),get_data=VotersID.get_data(personal_infodata),            agestatus=VotersID.agestatus
            
            )

