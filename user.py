import pyperclip


class User:


    user_list = [] # Empty user list

    def __init__(self, email, number,first_name,last_name,password):

         self.email = email
         self.phone_number = number
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

   