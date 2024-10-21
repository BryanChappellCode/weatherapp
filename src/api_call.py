
class API_Call():

    def __init__(self, api_key, endpoint):

        self.api_key = api_key
        self.endpoint = endpoint
        self.url = "https://api.weatherstack.com"        

    def __repr__(self):

        return f"Key: {self.api_key}\nEndpoint: {self.endpoint}\nURL: {self.url}"