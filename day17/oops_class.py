class user:
    def __init__(self,user_id,user_name):
        self.id=user_id
        self.username=user_name
        self.follower=0
        self.following=0
    def follow(self,user):
        user.follower+=1
        self.following+=1
user_1=user("001","Ashish kumar")
user_2=user("002","Yuvraj kumar")
user_3=user("003","shubham kumar")
user_1.follow(user_2)
user_2.follow(user_1)
user_3.follow(user_1)
user_1.follow(user_3)
print(user_2.follower)
print(user_2.following)
print(user_1.follower)
print(user_1.following)