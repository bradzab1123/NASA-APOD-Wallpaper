#Imports module for doing OS functions
import os
#Imports sys module for sys.exit to close script
import sys
#Imports platform module for getting OS information
import platform
#Imports subprocess module for running terminal commands like osascript inside python
import subprocess
#Imports ctypes module for setting Windows desktop wallpaper
import ctypes
#Imports module for API calls and downloading files
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

#Gets media_type to see if APOD is image or video
media_type = data[0]["media_type"]
#If APOD is not an image, exits script and prints
if media_type != "image":
    sys.exit("APOD is not an image, skipping today.")
print("APOD is an image. Storing URL")
#data[0] is the newest post in the list. ["hdurl"] is the name of the field for the image url and I am grabbing from the dictionary storing the post
image_url = data[0]["hdurl"]

#Sets the path where the image will be saved by using ~ for the user's home directory, then join to be platform-agnostic
image_path = os.path.expanduser(os.path.join("~", "Pictures", "APOD", "apod.jpg"))
#Prints the image path
print(image_path)
#Makes directories for image to be stored in. os.path.dirname grabs only the folder part of the path so it doesnt create folder called "apod.jpg"
os.makedirs(os.path.dirname(image_path), exist_ok=True)

#Stores response object for the image request
image_response = requests.get(image_url)
# "with" closes the file automatically when we are done with it. The image is stored in memory so we want to write it to a file with Open. wb says we are writing a binary file(image).
with open(image_path, "wb") as file:
    file.write(image_response.content)

#You have to use AppleScript to set the wallpaper so this is the script. ''' is for multi-line,f allows variable inside string, and {} is to reference variable inside python
apple_wallpaper_script = f'''
tell application "System Events"
    tell desktop 1
        set picture to "{image_path}"
    end tell
end tell
'''

#Function to change Desktop wallpaper in Windows to image in path
def change_wallpaper(image_path):
    # Constants for setting the wallpaper
    SPI_SETDESKWALLPAPER = 20  # Action to change wallpaper
    SPIF_UPDATEINIFILE = 0x01  # Update user profile
    SPIF_SENDWININICHANGE = 0x02  # Notify change to system

    try:
        # Call Windows API to change wallpaper
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path,
                                                   SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
        return True
    except Exception as e:
        # Print error message if wallpaper change fails
        print(f"Error changing wallpaper: {e}")
        return False

#Gets the platform the computer is on and stores it in computer_os variable
computer_os = platform.system()
print(computer_os)
#Checks if computer_os variable is Windows or Mac and runs wallpaper set depending on answer
if computer_os == "Windows":
    print("OS is Windows")
    #Runs change_wallpaper function defined above
    change_wallpaper(image_path)
elif computer_os == "Darwin":
    print("OS is MacOS")
    try:
        #Calls run function from subprocess module and then runs terminal commands like osascript in MacOS. Runs the apple wallpaper script
        subprocess.run(["osascript", "-e", apple_wallpaper_script], check=True)
    except:
        sys.exit("Setting Desktop Wallpaper Failed!")