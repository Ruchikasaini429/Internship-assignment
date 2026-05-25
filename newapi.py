# free apis to work on API	key
#REST Countries	
#JokeAPI	
#OpenWeather	
#Dog API	
#NewsAPI	
#GitHub API	
#TMDB API
import requests

country_name = input("Enter country name: ")

url = f"https://restcountries.com/v3.1/name/{country_name}"

response = requests.get(url)

data = response.json()

# Extract data
country = data[0]["name"]["common"]
capital = data[0]["capital"][0]
population = data[0]["population"]
region = data[0]["region"]

# Display
print("\n------ Country Details ------")
print(f"Country: {country}")
print(f"Capital: {capital}")
print(f"Population: {population}")
print(f"Region: {region}")