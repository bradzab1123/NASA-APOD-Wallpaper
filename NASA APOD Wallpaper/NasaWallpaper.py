#Imports module for doing OS functions
import os
#Imports sys module
import sys
#Imports module for API calls
import requests
#Imports module for reading .env files. Structured this way instead of import dotenv & dotenv.load_dotenv()
from dotenv import load_dotenv

#Function to call load_dotenv. Import just makes it available
load_dotenv()

#NASA API Key stored in a variable. load_dotenv function grabbed the values from the .env and os.getenv pulls that value.
api_key = os.getenv("NASA_API_KEY")

#Checks if api_key variable exists and exits the script if it doesn't
if api_key is None:
    sys.exit("No NASA API key found!")

#Base URL for NASA API
base_url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"
#Dictionary to store API key
api_params = {"api_key": api_key}

#This makes calls the get module from the requests module and uses the stored parameters in the call, then the output is stored in the "response" variable
response = requests.get(base_url, api_params)

#Stores API response as JSON into a variable
data = response.json()

print(type(data[0]))
print(len(data))

print(data[0].keys())