import requests

class API_Call():

    def __init__(self, api_key, query, endpoint):

        self.api_key = api_key
        self.query = query
        self.endpoint = endpoint
        self.url = "https://api.weatherstack.com"


    def call(self):

        built_url = f"{self.url}/{self.endpoint}?access_key={self.api_key}"

        

    def __repr__(self):

        return f"API Call: "