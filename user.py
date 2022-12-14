
class User():

    def __init__(self):
        self.name =""
        self.card_number = ""
        self.cv=""
        self.card_date=""
        self.last_order=""

    def set_name(self,name):
        self.name=name
        return self.name
    
    def set_card_number(self,card_number):
        self.card_number=card_number
        return self.card_number
    
    def set_cv(self,cv):
        self.cv=cv
        return self.cv
    
    def set_card_date(self,date):
        self.card_date=date
        return self.card_date

    def set_last_order(self,date):
        self.last_order= date
        return self.last_order
    
    

