class Test:


    @classmethod
    def get_data(cls,personal_infodata):
            
    
        print (personal_infodata)

        personal_infodata = list()
        print ("enter date in this format ,dd/mm/yyyy")
        prompt = ">"
        date_of_birth=input(prompt)
        personal_infodata.append(date_of_birth)

        
        return print(personal_infodata)

    def __init__(self,personal_infodata,age):

        self.age=age
        
        self.get_data=Test.get_data(personal_infodata=personal_infodata)
