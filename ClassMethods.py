class User_info:
    def __init__(self, username, email_address):
        self.username = username
        self.email_address = email_address

    def check_username(self, username_to_check):
        if username_to_check == self.username:
            return True
        else:
            return False

# We can use the new method (def check_username) to call the object and run the first method (User_info)

user = UserInfo('user123', 'abc@edf.ghi')
 
user.check_username('user123') # returns True
user.check_username('user456') # returns False







