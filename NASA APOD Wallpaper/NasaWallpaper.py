#Imports module for doing OS functions
import os
#Imports sys module for sys.exit to close script
import sys
#Imports module for API calls
import requests
#Imports module for reading .env files. Structured this way instead of import dotenv & dotenv.load_dotenv()
from dotenv import load_dotenv

#Calls load_dotenv to read the .env file. Import just makes it available
load_dotenv()

#NASA API Key stored in a variable. load_dotenv function copies values from .env into environment variable and os.getenv reads from environment variable.
api_key = os.getenv("NASA_API_KEY")

#Checks if the NASA_API_KEY is set and exits the script if it doesn't
if api_key is None:
    sys.exit("No NASA API key found!")

#Base URL for NASA API
base_url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic"
#Dictionary to store API key
api_params = {"api_key": api_key}

#This calls the get function from the requests module and uses the stored parameters in the call, then the output is stored in the "response" variable
response = requests.get(base_url, api_params)

#Stores API response into a variable called "data". Parses the JSON response into Python objects (a list of dicts)
data = response.json()

#data[0] is the newest post in the list. ["hdurl"] is the name of the field for the image url and I am grabbing from the dictionary storing the post
image_url = data[0]["hdurl"]

print(image_url)