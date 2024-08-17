import tkinter as tk
import requests
from PIL import Image, ImageTk
from tkinter import messagebox
import ttkbootstrap  # Import ttkbootstrap for theming (optional)

# Define API key and base URL for OpenWeatherMap API
API_KEY = "2457943f2465703ab99e096319928ff7"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def weather_calc(place):
    """
    This function fetches weather data from the OpenWeatherMap API for a given city.

    Args:
        place (str): The city name to fetch weather data for.

    Returns:
        tuple: A tuple containing (icon_url, temp, weather, city, country) if successful, otherwise None.
    """

    request_url = f"{BASE_URL}?appid={API_KEY}&q={place}"
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

    icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
    return icon_url, temp, weather, city, country


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
    icon_url, temp, weather, city, country = result

    location_lable.configure(text=f"{city}, {country}")  # Update location label

    temp_res.configure(text=f"{temp}°C")  # Update temperature label

    image = Image.open(requests.get(icon_url, stream=True).raw)  # Download and open weather icon
    icon = ImageTk.PhotoImage(image)  # Convert image to format usable by Tkinter
    weather_image.configure(image=icon)  # Update weather image label
    weather_image.image = icon

    weather_res.configure(text=f"{weather}")  # Update weather description label


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
weather_res.pack()
# Start the main event loop
root.mainloop()
