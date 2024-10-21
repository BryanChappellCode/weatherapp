from current_weather import CurrentWeather
from constants import languages

# init_properties()
# Parameters: path=<Path to properties.cfgfile>
# Function: Opens properties.cfg and parses parameters into a dictionary
# Returns: Dictionary of parameters found in properties.cfg

def init_properties(path="properties.cfg"):

    try:
        with open(path, "r") as props:
            contents = props.read()
            props.close()
    except FileNotFoundError:
        print("ERROR: Properties file was not found at path")
        return "ERROR"
    except PermissionError:
        print("ERROR: You do not have permission to open the properties file")
        return "ERROR"
    except Exception as e:
        print(f"An error has occured: {e}")

    split_props = contents.split("\n")

    properties = {}

    for prop in split_props:
        split_prop = prop.strip().split("=")

        if len(split_prop) == 1:
            properties[split_prop[0]] = ""
        else:
            properties[split_prop[0]] = split_prop[1]

    if "api_key" not in properties or properties["api_key"] == "":
        raise Exception("Missing API key in properties.\nUsage: api_key=<your key here>")
    
    if "language" not in properties or properties["language"] not in languages.keys():
        properties["language"] = None

    if "units" not in properties or properties["units"] == "":
        properties["units"] = "f"

    return properties

def current_weather(properties):

    print("\t\t\t=================================")
    print("\t\t\t==----Enter a City/ZIP Code----==")
    print("\t\t\t=================================")

    user_input = input()

    weather = CurrentWeather(properties["api_key"], user_input, properties["units"], properties["language"])

    weather.get_weather()

    user_input = None

    while user_input != "":

        print(weather)
        

def print_menu():

    print("\t\t\t=================================")
    print("\t\t\t==----------MAIN MENU----------==")
    print("\t\t\t=================================")
    print("\t\t\t==-----1.  Current Weather-----==")
    print("\t\t\t==-----2.  Past Weather--------==")
    print("\t\t\t==-----3.  Hourly Forecast-----==")
    print("\t\t\t==-----4.  7 Day Forecast------==")
    print("\t\t\t==-----5.  Settings------------==")
    print("\t\t\t==-----6.  Exit----------------==")
    print("\t\t\t=================================")

    