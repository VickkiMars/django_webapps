from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import json
import urllib.request
import datetime
from.models import City
from countryinfo import CountryInfo
from geopy.geocoders import Nominatim
import requests
# Create your views here.
#global cities
#cities = ['rio de janeiro','buenos aires', 'london', 'paris', 'boston', 'tokyo', 'kyoto', 'madrid', 'jakarta', 'chongqing', 'delhi', 'seoul', 'mumbai', 'manila', 'shanghai', 'beijing', 'osaka', 'manchester','los angeles', 'texas', 'dar es salaam','belo horizonte','saint petersburg', 'kolkata', 'karachi', 'dhaka', 'manila', 'lagos', 'tianjin', 'kinshasa', 'guangzhou', 'moscow', 'lahore', 'bangalore', 'lima', 'tehran', 'chicago', 'wuhan', 'luanda', 'baghdad', 'santiago', 'houston', 'toronto', 'miami', 'atlanta', 'philadelphia', 'singapore', 'barcelona', 'washington', 'alexandria', 'johannesburg', 'abuja','kabul', 'algiers', 'vienna', 'porto novo', 'berlin', 'accra', 'new delhi', 'jerusalem', 'tel aviv', 'nairobi', 'mexico city', 'damascus', 'kiev', 'tunis', 'dubai', 'doha'] 
#list of cities(non-web-operable) 


def index(request): #home page displaying 68 cities and weather conditions
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=b2da999405939ac8aefe39fae24797b6'

    # new_cities = [] #lists of cities (web-operable)

    # cities = City.objects.all()
    # for city in cities:
    #     if " " in city:
    #         x = city.replace(" ", "%20")
    #         new_cities.append(x)
    #     else:
    #         new_cities.append(city)
    
    weather_data = []
    cities = City.objects.all()
    for city in cities: #looping through new_cities
        data_list = requests.get(url.format(city)).json()

        data = {
        'name': str(data_list['name']).capitalize(),
        "country_code" : str(data_list['sys']['country']),
        "coordinate" : str(data_list['coord']['lon']) + ' ' + str(data_list['coord']['lat']),
        "temp" : str(int((data_list['main']['temp']) -273.15) * 1.8 + 32,)[:4],
        "pressure" : str(data_list['main']['pressure'])  + 'Hg',
        "humidity" : str(data_list['main']['humidity']) + ' g.kg-1 ',
        'icon' : data_list['weather'][0]['icon'],
        'wind_speed': str(data_list['wind']['speed']) + ' metres per second' ,
        'clouds_description': str(data_list['weather'][0]['description']).capitalize()
        }
        weather_data.append(data)

    

    #extra data form the json data

    now = datetime.datetime.now()
    time = (now.strftime("%I:%M:%S %p %A, %d %b %y"))
    #getting current time


    context = {'weather_data': weather_data, 'time':time } 
    return render(request, "wapp/indexs.html", context) #displaying on html

def country(request):
    weather_data = []
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=b2da999405939ac8aefe39fae24797b6'
    if request.method == "POST":
        country_name = request.POST['city_name']
        data_list = requests.get(url.format(country_name)).json()
        data = {
        'name': str(data_list['name']).capitalize(),
        "country_code" : str(data_list['sys']['country']),
        "coordinate" : str(data_list['coord']['lon']) + ' , ' + str(data_list['coord']['lat']),
        "temp" : str(int((data_list['main']['temp']) -273.15) * 1.8 + 32,)[:4],
        "pressure" : str(data_list['main']['pressure'])  + 'Hg',
        "humidity" : str(data_list['main']['humidity']) + ' g.kg-1 ',
        'icon' : data_list['weather'][0]['icon'],
        'wind_speed': str(data_list['wind']['speed']) + ' metres per second' ,
        'clouds_description': str(data_list['weather'][0]['description']).capitalize()
        }
        weather_data.append(data)
        now = datetime.datetime.now()
        time = (now.strftime("%I:%M:%S %p %A, %d %b %y"))

        #####################################################################################COUNTRY DATA

        try:
            geolocator = Nominatim(user_agent = "geoapiExercises")
            location = geolocator.geocode(country_name, language='en')
        except Exception as e:
            print(e)
        finally:
            new_loc = str(location).split(',')
            new_location = new_loc[-1].strip()

        name = new_location
        data = CountryInfo(name)
        country_info = data.info()

        url='https://restcountries.com/v3.1/name/{}'

        data_list = requests.get(url.format(name)).json()

        currency_code= country_info['currencies']

        new_data = {
            'name':data_list[0]['name']['official'],
            'independent': data_list[0]['independent'],
            'UN_member': data_list[0]['unMember'],
            'currency_symbol' : data_list[0]['currencies'][currency_code[0]]['symbol'],
            'Map_link': data_list[0]['maps']['googleMaps'],
            'flag': data_list[0]['flags']['png'],
            'continent': data_list[0]['continents'][0],
            'subregion' : country_info['subregion'],
            'timezones' : data_list[0]['timezones'],
            'capital' : country_info['capital'],
            'wiki' : country_info['wiki']
        }
        
    print(weather_data[0]['clouds_description'])


    context = {'country_data': weather_data[0], 'time':time, 'country_details':new_data, 'cc':currency_code } 

    return render(request, "wapp/country.html", context)

    
