from dotenv import load_dotenv
load_dotenv()
import os
#Exercise 1 
#Generating the class 
class Genius: 
    def __init__(self, access_token):
        self.access_token = os.environ['ACCESS_TOKEN']

    def get_access_token(self): 
        return self.access_token