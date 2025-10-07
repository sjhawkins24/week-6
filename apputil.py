from dotenv import load_dotenv
load_dotenv()
import os
import requests
import pandas as pd
#Exercise 1 
#Generating the class 
class Genius: 
    def __init__(self, access_token):
        self.access_token = access_token

    def get_access_token(self): 
        return self.access_token
    
    def get_artist_id(self, artist):
        """Function to get the artist ID from the main response"""
        #Get the token
        token = self.get_access_token()
        #Construct the url
        artist_url = f"http://api.genius.com/search?q={artist}&access_token={token}"
        #Parse json
        response = requests.get(artist_url)
        json_data = response.json()
        artist_id = json_data["response"]["hits"][1]["result"]["id"]
        return(artist_id)
    
    def get_artist_name(self, artist):
        """Function to get the artist name from the main response"""
        #Get the token
        token = self.get_access_token()
        #Construct the url
        artist_url = f"http://api.genius.com/search?q={artist}&access_token={token}"
        #Parse json
        response = requests.get(artist_url)
        json_data = response.json()
        artist_names = json_data["response"]["hits"][0]["result"]["artist_names"]
        return(artist_names)
    
    def get_artist_details(self, artist_id):
        """Function to take an artist id and return the details from genius"""
    #Get the token and page length
        per_page = 1
        token = self.get_access_token()

    #Construct the url
        songs_url = f"http://api.genius.com/artists/{artist_id}&per_page={per_page}"

    #Parse json
        response = requests.get(songs_url, 
                            headers={"Authorization": "Bearer " + token})
        json_data = response.json()
        results = json_data["response"]#["artist"]
        return(results)
    
    def get_artist(self, search_term): 
        #Get the artist ID
        artist_id = self.get_artist_id(search_term)
        #Use the ID to get the results
        results = self.get_artist_details(artist_id)
        return(results)
    
    def get_artist_data(self, search_term):
        artist_id = self.get_artist_id(search_term)
        artist_name = self.get_artist_name(search_term)
        follower_count = self.get_artist(search_term)["followers_count"]
        artist_result = [search_term, artist_name, artist_id, follower_count ]
        return(artist_result)
    
    def get_artists(self, search_terms):
        return_data = pd.DataFrame(columns=["search_term", "artist_name", "artist_id", "followers_count"])
        for search_term in search_terms: 
            temp_data = self.get_artist_data(search_term)
            return_data.loc[len(return_data)] = temp_data
        return(return_data)
    