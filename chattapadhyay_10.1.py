# Author: Kausik Chattapadhyay
# DSC 510 Assignment 10.1
# Date 08/10/2022
# Prompt the user for their city or zip code and request weather forecast data from OpenWeatherMap
# and print the weather data in a pretty way.

import requests
from datetime import datetime


def oauth():
    """
    Register on https://openweathermap.org/ to get api_key.
    :return: api_key
    """
    # Enter your API key here
    # api_key = "Your_API_Key"
    api_key = '3965d8b2a63d399e75251813f9f3e975'
    return api_key


def input_check():
    """
    Valid user input checks for City Name, State and country. Also checks for valid units for temp.
    :return: city_name, state_name, country_name, units
    """
    city_name = input("Please enter the city name: ").strip()
    while city_name is None or len(str(city_name).strip()) == 0:
        print("City name can not be empty.")
        city_name = input("Please enter the city name: ").strip()

    state_name = input("Please enter the state abbreviation: ").strip()
    while state_name is None or len(str(state_name).strip()) == 0:
        print("State name can not be empty.")
        state_name = input("Please enter the state abbreviation: ").strip()

    country_name = input("Please enter the country abbreviation: ").strip()
    while country_name is None or len(country_name) == 0:
        print("Country name can not be empty.")
        country_name = input("Please enter the country abbreviation: ").strip()

    units = input("Would you like to view temps in Fahrenheit, Celsius, or Kelvin.Enter 'F' for "
                  "Fahrenheit, "
                  "'C' for Celsius,"" 'K' for Kelvin: ").strip()

    while units.upper() not in ('F', 'C', 'K'):
        print("Units must be valid like C/F/K")
        units = input(
            "Would you like to view temps in Fahrenheit, Celsius, or Kelvin.Enter 'F' for Fahrenheit, "
            "'C' for Celsius, 'K' for Kelvin: ").strip()

    return city_name, state_name, country_name, units


def input_check_zip():
    """
    Checks the user input zip code for validity along with temp units.
    :return: zip, units
    """
    zip = input("Please enter the zip code: ").strip()

    while zip is None or len(str(zip).strip()) == 0:
        print("Zip code can not be empty.")
        zip = input("Please enter the zip code: ").strip()
    try:
        zip = int(zip)
    except ValueError:
        print("Zip code is invalid. Please enter valid zip codes.")
        zip = input("Please enter the zip code: ")

    units = input("Would you like to view temps in Fahrenheit, Celsius, or Kelvin."
                  "Enter 'F' for Fahrenheit,'C' for Celsius, 'K' for Kelvin: ")
    while units.upper() not in ('F', 'C', 'K'):
        print("Units must be valid like C/F/K")
        units = input(
            "Would you like to view temps in Fahrenheit, Celsius, or Kelvin.Enter 'F' for Fahrenheit, "
            "'C' for Celsius, 'K' for Kelvin: ").strip()

    return zip, units


def extract_lat_lon(city_name, state_name, country_name, units='K'):
    """
    This function with take city, state, country names and temp units from user and call GEO api
    http://api.openweathermap.org/geo/1.0/ to return lat and lon for that location.
    :param city_name:
    :param state_name:
    :param country_name:
    :param units:
    :return: lat, lon
    """
    # EXTRACT LAT, LON BY PASSING CITY NAME
    api_key = oauth()
    limit = 1
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_name},{country_name}" \
          f"&limit={limit}&appid={api_key}"

    response = requests.request("GET", url)
    #response.raise_for_status()

    if response.status_code == 200:
        response_json = response.json()
        try:
            lat = response_json[0]['lat']
            lon = response_json[0]['lon']
        except Exception:
            print(f"No record found. See you next with valid city, state and country.Bye!!")
            quit()

        return lat, lon
    else:
        print(f"No record found. HTTP status is {response.status_code}!!")
        print("See you next with valid city, state and country.Bye!")
        quit()


def extract_lat_lon_by_zip(zip, units):
    """
    This function will take the zip code and units from user and call the GEO api
    http://api.openweathermap.org/geo/1.0/ and return lat and lon for that location.
    :param zip:
    :param units:
    :return: lat, lon
    """
    # EXTRACT LAT, LON BY PASSING ZIP CODE
    api_key = oauth()
    url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip}&appid={api_key}"

    response = requests.request("GET", url)
    #response.raise_for_status()

    if response.status_code == 200:
        response_json = response.json()
        try:
            lat = response_json['lat']
            lon = response_json['lon']
        except Exception:
            print(f"No record found. See you next with valid zip codes.Bye!!")
        return lat, lon
    else:
        print(f"No record found. HTTP status is {response.status_code}!!")
        print("See you next with valid zip codes.Bye!")
        quit()


def get_weather(lat, lon, units):
    """
    This function will take lat and lon of any location and call the weather api
     http://api.openweathermap.org/data/2.5/weather to get the current weather info.
    :param lat:
    :param lon:
    :param units:
    :return: Current weather
    """
    api_key = oauth()
    if units.upper() == "F":
        units = 'imperial'
    elif units.upper() == "C":
        units = 'metric'
    elif units.upper() == "K":
        units = 'kelvin'
    else:
        print("Invalid units. Please enter valid units(C/F/K)")

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units={units}"

    try:
        response = requests.request("GET", url)
        response.raise_for_status()
        response = response.json()
    except requests.exceptions.HTTPError as error:
        print(f'HTTP error occurred: {error}')
    except requests.ConnectionError as error:
        print(f'Connection error occurred: {error}')
    except Exception as err:
        print(f'Other error occurred: {err}')

    datetime_obj = datetime.now()

    print(51 * "*")
    print(f"Current Weather Conditions For {response['name']}, {response['sys']['country']} on {str(datetime_obj)}")
    print(21 * " ")
    print(f"Current Temp: {response['main']['temp']} degrees")
    print(f"Feels like  : {response['main']['feels_like']} degrees")
    print(f"High Temp   : {response['main']['temp_max']} degrees")
    print(f"Low Temp    : {response['main']['temp_min']} degrees")
    print(f"Pressure    : {response['main']['pressure']} hPa")
    print(f"Humidity    : {response['main']['humidity']} %")
    if response['clouds']['all'] < 30:
        print("Cloud Cover : Minimal Cloud cover")
    elif 30 <= response['clouds']['all'] < 60:
        print("Cloud Cover : Moderate Cloud cover")
    else:
        print("Cloud Cover : High Cloud cover")
    print(f"Description : {response['weather'][0]['description']}")
    print("*****************************************************")


def main():
    """
    Main function to check user options and call all the functions to get the desired current weather info.
    :return:
    """
    print("!!!!Welcome to the current weather forecast app!!!!")
    print("***************************************************")

    while True:
        inp = input("Would you like to lookup weather data by US City or zip code? Enter 1 for US City 2 for zip: "). \
            strip()

        if inp == '1':
            # Check user inputs city_name, state_name, country_code and units
            city_name, state_name, country_name, units = input_check()
            # Extract lat, lon by passing city name, state abbr and country abbr
            lat, lon = extract_lat_lon(city_name, state_name, country_name, units)
            # Extract the current weather
            get_weather(lat, lon, units)
            # Additional check to continue weather look up
            answer = input("Would you like to perform another weather lookup? (Y/N): ")
            if answer in ('N', 'n'):
                print("Thank you for using weather app!! See ya.")
                break
            elif answer in ('Y', 'y'):
                continue
            else:
                print("Invalid input. Y/N is valid.")

        elif inp == '2':
            # Check user input zip and units.
            zip, units = input_check_zip()
            # Extract lat, lon by zip codes
            lat, lon = extract_lat_lon_by_zip(zip, units)
            # Extract current weather
            get_weather(lat, lon, units)
            # Additional check to continue weather look up
            answer = input("Would you like to perform another weather lookup? (Y/N): ")
            if answer in ('N', 'n'):
                print("Thank you for using weather app!! See ya.")
                break
            elif answer in ('Y', 'y'):
                continue
            else:
                print("Invalid input. Y/N is valid.")
        else:
            print("Invalid input. Enter 1 for US City 2 for zip!!")


if __name__ == '__main__':
    # Running main function
    main()
