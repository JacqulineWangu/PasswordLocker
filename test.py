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

        self.assertEqual(self.new_user.account,"Facebook")
        self.assertEqual(self.new_user.username,"MichiganMaine")
        self.assertEqual(self.new_user.password,"wawoodz")
