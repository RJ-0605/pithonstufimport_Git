class VotersID:
    next_serial=None

    #   next time try to use cache and see how that goes 
    agestatus=None

    j=None

    begin_data=None


# seperate class to learn the use of mutators and accessors
    @classmethod
    def create_empty(cls,personal_infodata,agelist):
        
        return cls(personal_infodata,otherinfos=list(agelist))



        

    @staticmethod
    def compile_userdata(arg1,arg2):
       
        print ('lets begin somewhere, what do you think')

        

     #   if VotersID.dup_present is False:


        VotersID.age_validator(arg2)

        if VotersID.agestatus is True :

            
            VotersID.get_data(arg1)
            print ('success')


        else :

            print ("you are unable to proceed with registration due to wrong age, go home and come try again when you are older ")

            return exit()


        # else :

        #    return print ("profile already exists with same name and age, please crosscheck details and reenter details or proceed to YYY office to verify and obtain card ")



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


    @classmethod
    def get_data(cls,x):
            
    
        
    # this begin data could be finger print which could scan at the beginning to show if the user is already in  the system

        if cls.begin_data is None:
        
        # we will employ lambdas to part of the work 
            print (x)

            cls.begin_data=list()
            

        else :
            for b in cls.begin_data:
                if b == x:
                    print ("this data entry already exist, or this finger print entry already exists")
                    return exit()

                else:
                    print(cls.begin_data)

        cls.begin_data.append(x)
            
        print ("Please wait your details is being evaluated for a likely profile to be created for you")


        if cls.j is None:

            cls.j= list()



       
         # check here if the userdata does not already exist by checking the data_of_birth provided
            
        else:
            print (cls.j)

        print ("enter date in this format ,dd/mm/yyyy")
        prompt = ">"
        date_of_birth=input(prompt)
        cls.j.append(date_of_birth)   
          
        VotersID._get_next_serial()
                    


        


        # if all is well it escapes the checkers and you are brought here 
        


        
        return print(cls.j)





    def __init__(self,personal_infodata,age,otherinfos):
        
        self.personal_infodata=personal_infodata
        self.age=age
        self.otherinfos=otherinfos
        
        

        self.compile_userdata=VotersID.compile_userdata( personal_infodata,age)




class VotersIDsupport(VotersID):

    # this class can have mirror "already initialised functions in main VotersID" which i can just call and replace these functions by setting what these functions use and what combination of functions it can be made of 
    
    @staticmethod
    def compile_userdata(arg1,arg2):
        print("this is personal_infodata " + arg1)
        print ('this is the age'+ arg2)




class VoterAssetsA(VotersID):

    heightlimit=3

    @staticmethod
    def asset_maker(personal_infodata,age):
        print (personal_infodata)


    def __init__(self,personal_infodata,age,otherinfos,height):
        super().__init__(personal_infodata,age,otherinfos)

        if height<heightlimit :
            raise ValueError("your age is too small go and find your daddy")


        self.height=height
       

    


