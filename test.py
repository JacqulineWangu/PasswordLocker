import unittest
import pyperclip # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Argumentss:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

 # Items up here .......

def setUp(self):
     '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("jacqarta1167@gmail.com","0707518860","Jacquline","Wangu") # create user object

        def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        
        self.assertEqual(self.new_user.email,"jaqarta1167@gmail.com")
        self.assertEqual(self.new_user.phone_number,"0707518860")
        self.assertEqual(self.new_user.first_name,"Jacquline")
        self.assertEqual(self.new_user.last_name,"Wangu")
        
        

        def test_save_multiple_user(self):
            '''
            test_save_multiple_contact to check if we can save multiple user
            objects to our contact_list 
            '''
            self.new_user.save_user() #saves the new user
            test_user = User("jaqarta1167@gmail.com","0707518860","MichiganMaine","Jaqarta") # new user
            test_user.save_user()
            # test_user.save_contact()
            self.assertEqual(len(User.user_list),2) 

# setup and class creation up here
def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
User.user_list = []

def test_save_user(self):
        self.new_user.save_user()
self.assertEqual(len(User.user_list),1) 

def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("jaqarta1167@gmail.com","0707518860","MichiganMaine","Jaqarta") # new user
        test_user.save_user()


        self.assertEqual(len(User.user_list),2)
