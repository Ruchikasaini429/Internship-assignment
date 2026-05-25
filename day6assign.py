import requests
from datetime import datetime

# Enter your API key here
api_key = "7639da6cf27c65535c4b2c4374f90ab8"

# Enter city name
city = input("Enter city name: ")

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Send request to API
response = requests.get(url)

# Convert response into JSON format
data = response.json()

# Check if city exists
if data["cod"] != 200:
    print("City not found!")
else:
    # Temperature details
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]

    # Humidity and pressure
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

    # Wind speed
    wind_speed = data["wind"]["speed"]

    # Sunrise and sunset time
    sunrise = data["sys"]["sunrise"]
    sunset = data["sys"]["sunset"]

    # Convert UNIX time to readable format
    sunrise_time = datetime.fromtimestamp(sunrise).strftime('%H:%M:%S')
    sunset_time = datetime.fromtimestamp(sunset).strftime('%H:%M:%S')

    # Display output
    print("\n------ Weather Report ------")
    print(f"City: {city}")

    print(f"\nTemperature: {temperature}°C")
    print(f"Feels Like: {feels_like}°C")

    print(f"\nHumidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")

    print(f"\nWind Speed: {wind_speed} m/s")

    print(f"\nSunrise Time: {sunrise_time}")
    print(f"Sunset Time: {sunset_time}")