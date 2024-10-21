from api_call import API_Call
from requests import get
from json import loads
from

class CurrentWeather(API_Call):

    def __init__(self, api_key, query, units="f", language=None):
        super().__init__(api_key, "current")
        self.response = None
        self.querystring = {
            "query" : query,
            "units" : units,
        }
        if language is not None: self.querystring["language"] = language

        self.city = None 
        self.region = None 
        self.country = None
        self.time = None
        self.date = None
        self.temp = None
        self.conditions = None
        self.humidity = None
        self.feelslike = None
        self.wind_speed = None
        self.wind_direction = None
        self.cloud_cover = None
        self.uv_index = None
        self.visibility = None
        
    def get_weather(self):

        url = f"{self.url}/{self.endpoint}?access_key={self.api_key}"

        self.response = get(url, params=self.querystring).json()

        if "success" in self.response.keys() and self.response["success"] is False:
            raise Exception("ERROR:", {self.response["error"]["info"]})

        self.city = self.response["location"]["name"]
        self.region = self.response["location"]["region"]
        self.country = self.response["location"]["country"]
        self.time, self.date = time_fix(self.response["location"]["localtime"])
        self.temp = {self.response["current"]["temperature"]}
        self.conditions = self.response["current"]["weather_descriptions"]
        self.humidity = self.response["current"]["humidity"]
        self.feelslike = self.response["current"]["feelslike"]
        self.wind_speed = self.response["current"]["wind_speed"]
        self.wind_direction = self.response["current"]["wind_dir"]
        self.cloud_cover = self.response["current"]["cloudcover"]
        self.uv_index = self.response["current"]["uv_index"]
        self.visibility = self.response["current"]["visibility"]



    def __repr__(self):

        location = f"{self.city}, {self.region}, {self.country}"
        
def time_fix(time):

    split_date_time = time.split()
    split_date = split_date_time[0].split("-")
    split_time = split_date_time[1].split(":")

    day = split_date[2]

    match split_date[1]:
        case "01" : mon = "January"
        case "02" : mon = "February"
        case "03" : mon = "March"
        case "04" : mon = "April"
        case "05" : mon = "May"
        case "06" : mon = "June"
        case "07" : mon = "July"
        case "08" : mon = "August"
        case "09" : mon = "September"
        case "10" : mon = "October"
        case "11" : mon = "November"
        case "12" : mon = "December"
        case _: raise Exception("ERROR: There was an error with the date", split_date[1])

    year = split_date[0]

    hour = int(split_time[0])
    am = True

    if hour > 12:
        hour -= 12
        am = False

    if hour == 0:
        hour = 12
        am = True

    minute = split_time[1]

    return f"{hour}:{minute}", f"{mon} {day}, {year}"
