class user:
    def __init__(self,first_name,last_name,email,age,is_rewards_member = False,gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email= email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
    
    def display_info(self):
        print ( f"\n{self.first_name} {self.last_name} {self.email} {self.age} {self.is_rewards_member} {self.gold_card_points}")
        return self

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
        self.gold_card_points += 200
        return self
    
    def spent(self,amount):
        if self.gold_card_points >= amount :
            self.gold_card_points -= amount
        if self.gold_card_points < amount:
            print("you over spent your points")
        return self
    

    

john = user("John","doe","johndoe@flux.xyz",22,True,50)
ash = user("ash","katchum","ashkatchum@flux.xyz",21,True,80)
barney = user("barney","stenson","barneystensen@flux.xyz",22,True,40)


#chaining methods

john.display_info().enroll().spent(40).display_info()


