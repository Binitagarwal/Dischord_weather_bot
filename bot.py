import discord
from discord import state
import requests
import math

client = discord.Client()

#getting the woeid value of the city
def url1(city):
    url = "https://www.metaweather.com/api/location/search/?query={}".format(city)
    response = requests.get(url)
    y = response.json()
    print(y[0]['woeid'])
    return(str(y[0]['woeid']))

#getting the weather value of the city
def url2(cityno):
    urle = "https://www.metaweather.com/api/location/{}".format(cityno)
    response2 = requests.get(urle)
    datae = response2.json()
    return(datae)


#the bot functioning
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('%hello'):
        await message.channel.send("Hello There!")
    if message.content.startswith('%weather_'): 
        texter = message.content
        texter = texter.split('_')
        text = texter[1]
        print(text)
        value = url1(text)
        data = url2(value)
        #print(weather)
        max_temp = str(math.trunc(data['consolidated_weather'][0]['max_temp']))
        min_temp = str(math.trunc(data['consolidated_weather'][0]['min_temp']))
        the_temp = str(math.trunc(data['consolidated_weather'][0]['the_temp']))
        date = str(data['consolidated_weather'][0]['applicable_date'])
        weather = str(data['consolidated_weather'][0]['weather_state_name'])
        statement = "On "+ str(date) + " " + str(text) + " weather is: " + str(weather)
        await message.channel.send(statement)
        await message.channel.send("Current temperatute: "+ the_temp +" °c")
        await message.channel.send("The maximum temperature: "+max_temp+" °c \nThe minmum: "+min_temp+" °c")
    
client.run('<Enter your bot token here')