import tkinter as tk
import requests
import time
from dotenv import load_dotenv  # used to import API_KEY from .env
import os
from PIL import Image, ImageTk
from tkinter import messagebox
import ttkbootstrap  # Import ttkbootstrap for theming (optional)

# Define API key and base URL for OpenWeatherMap API
load_dotenv()  # loads the value from .env
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def weather_calc(place):
    """
    This function fetches weather data from the OpenWeatherMap API for a given city.

    """

    request_url = f"{BASE_URL}?appid={os.getenv('API_KEY')}&q={place}"
    response = requests.get(request_url)

    if response.status_code == 404:  # Check for "City not found" error (status code 404)
        messagebox.showerror("Error", "City not found")
        return None

    data = response.json()
    weather = data['weather'][0]["description"]
    temp = round(data["main"]["temp"] - 273.15, 1)  # Convert Kelvin to Celsius
    icon_code = data['weather'][0]['icon']
    city = data['name']
    country = data['sys']['country']
    min_temp = round(data["main"]["temp_min"] - 273.15, 1)
    max_temp = round(data["main"]["temp_max"] - 273.15, 1)
    press = data["main"]["pressure"]
    humid = data["main"]["humidity"]

    sunrise_tp = data["sys"]["sunrise"]
    sunset_tp = data["sys"]["sunset"]
    # Convert timestamps to human-readable format
    sunrise_time = time.strftime('%H:%M:%S %p', time.localtime(sunrise_tp))
    sunset_time = time.strftime('%H:%M:%S %p', time.localtime(sunset_tp))

    icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
    return icon_url, temp, weather, city, country, data, min_temp, max_temp, press, humid, sunrise_time, sunset_time


# Function to search weather for a city entered by the user
def search():
    """
    This function retrieves weather data for the city entered by the user and updates the GUI.
    """

    place = city_entry.get()  # Get the city name from the entry field

    result = weather_calc(place)  # Call weather_calc function to fetch data

    if result is None:
        return  # Exit the function if city not found

    # Unpack the returned values from weather_calc
    icon_url, temp, weather, city, country, data, min_temp, max_temp, press, humid, sunrise_time, sunset_time = result

    location_lable.configure(text=f"{city}, {country}")  # Update location label

    temp_res.configure(text=f"{temp}°C")  # Update temperature label

    image = Image.open(requests.get(icon_url, stream=True).raw)  # Download and open weather icon
    icon = ImageTk.PhotoImage(image)  # Convert image to format usable by Tkinter
    weather_image.configure(image=icon)  # Update weather image label
    weather_image.image = icon

    weather_res.configure(text=f"{weather}")  # Update weather description label

    min_max.configure(text=f"Min Temp: {min_temp}°C  Max Temp: {max_temp}°C")

    press_humid.configure(text=f"Pressure: {press}  Humidity: {humid}")

    suntime.configure(text=f"Sunrise: {sunrise_time}  Sunset: {sunset_time}")


# Create the main application window
root = ttkbootstrap.Window(themename="morph")  # Optional theming using ttkbootstrap
root.title("Weather Application")
root.minsize(900, 700)  # Set minimum window size

# Create GUI elements
city_entry = tk.Entry(root, width=30, font=("Helvetica", 18))
city_entry.pack(pady=10)

check_button = tk.Button(root, text="Check Weather", command=search)
check_button.pack(pady=5)

location_lable = tk.Label(root, font="Helvetica, 25")
location_lable.pack(pady=20)

temp_res = tk.Label(root, text="", font=("Helvetica", 40))
temp_res.pack()

weather_image = tk.Label(root)
weather_image.pack()

weather_res = tk.Label(root, text="", font=("Helvetica", 25))
weather_res.pack(pady=20)

min_max = tk.Label(root, text="", font=("Helvetica", 13))
min_max.pack(pady=5)

press_humid = tk.Label(root, text="", font=("Helvetica", 13))
press_humid.pack()

suntime = tk.Label(root, text="", font=("Helvetica", 13))
suntime.pack()
# Start the main event loop
root.mainloop()
