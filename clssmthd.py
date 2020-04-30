
class VotersID:

    next_serial=2469

    @classmethod

    def _get_next_serial(cls):
        result=cls.next_serial
        cls.next_serial += 1
        # return result  we will only add this when we wantit to run automatically
        # i am adding this text because i am running test on changes with github
       #  hello we will be gerting you some chicken


    
    @classmethod
    def create_empty(cls,owner_code):

        return cls (owner_code,contents=None)

    @classmethod
    def create_with_items(cls,owner_code,items):
        return cls (owner_code,contents=list(items) )


    def __init__(self,owner_code,contents):
        self.owner_code=owner_code
        self.contents=contents
        self.serial=VotersID._get_next_serial()     