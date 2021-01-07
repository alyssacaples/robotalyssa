import discord
import os 
import requests
import json
import random
from replit import db
#an asynchronous library

client = discord.Client()

api_key = os.getenv('API_KEY')
recipe_key = os.getenv('RECIPE_KEY')
#cat_key = os.getenv('CAT_KEY')

sad_words = ["sad", "depressed", "unhappy", "schwartz", "angry", "miserable", "mad"]
teach_me = ["beep bop"]

def learn(lesson):
  if "knowledge" in db.keys():
    knowledge = db["knowledge"]
    if lesson not in knowledge:
      knowledge.append(lesson)
      db["knowledge"] = knowledge

  else:
    teach_me.append(lesson)
    db["knowledge"] = teach_me

def unlearn(lesson):
  knowledge = db["knowledge"]
  print(lesson)
  if lesson in knowledge:
    print("yeet?")
    print(knowledge.remove(lesson))
    db["knowledge"] = knowledge

def get_inspo():
  url = "https://zenquotes.io/api/random"
  response = requests.get(url)
  json_data = json.loads(response.text)
  print(json_data[0])
  return(json_data[0])

def get_ron_swanson():
  url = "https://ron-swanson-quotes.herokuapp.com/v2/quotes"
  response = requests.get(url)
  json_data = json.loads(response.text)
  return(json_data[0]['q'])

def get_star_wars():
  url = "http://swquotesapi.digitaljedi.dk/api/SWQuote/RandomStarWarsQuote"
  response = requests.get(url)
  json_data = json.loads(response.text)
  return(json_data['starWarsQuote'])

get_star_wars()

def get_recipe(recipe):
  url = "https://recipe-puppy.p.rapidapi.com/"
  query_string = {"p": "1", "i": "", "q":recipe}
  headers =  {
    'x-rapidapi-key': recipe_key,
    'x-rapidapi-host': "recipe-puppy.p.rapidapi.com"
    }
  response = requests.get(url, headers=headers, params=query_string)
  json_data = json.loads(response.text)
  return json_data['results'][0]['href']

def get_kanye_quote():
  url = "https://api.kanye.rest"
  response = requests.get(url)
  json_data = json.loads(response.text)
  return json_data['quote']

def get_dog_image():
  url = "https://dog.ceo/api/breeds/image/random"
  response = requests.get(url,)
  json_data = json.loads(response.text)
  return json_data['message']

  
def get_cat_image():
  #headers {'x-api-key': cat_key}
  url = "https://api.thecatapi.com/v1/images/search"
  response = requests.get(url)
  json_data = json.loads(response.text)
  print(json_data)
  return json_data[0]['url']


@client.event #this is how you register you event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event #the triggering event is getting a message
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('robot alyssa help'):
    await message.channel.send('say cat for cat, dog for dog, kanye for kanye west quotes, star wars for star wars quote, swanson for ron swanson quotes, say "hungry for" + food to search for a recipe')

  options = teach_me
  if "knowledge" in db.keys():
    options = options + db["knowledge"]

  if any (word in message.content for word in sad_words):
    await message.channel.send(get_inspo())
  
  if message.content.startswith('$hello'):
    await message.channel.send('hello! :)')

  if message.content.startswith('$new'):
    add = message.content.replace('$new ', '')
    learn(add)
    current = db["knowledge"]
    words = ', '.join([str(elem) for elem in current]) 
    await message.channel.send('updated word list: ')
    await message.channel.send(words)

  if message.content.startswith('$show'):
    current = db["knowledge"]
    words = ', '.join([str(elem) for elem in current]) 
    await message.channel.send('word list: ')
    await message.channel.send(words)

  if message.content.startswith('$rm'):
      if "knowledge" in db.keys():
        rm = message.content.replace('$rm ', '')
        unlearn(rm)
        await message.channel.send('removed word')

  if message.content.startswith('hungry for'):
    recipe = message.content.replace('hungry for ', '')
    await message.channel.send('here is what i found:')
    await message.channel.send(get_recipe(recipe))

  if message.content.find('robot alyssa') > -1:
    learnings = db["knowledge"]
    await message.channel.send(random.choice(learnings))
    
  if message.content.find('kanye') > -1:
    await message.channel.send(get_kanye_quote())

  if message.content.find('star wars') > -1:
    await message.channel.send(get_kanye_quote())

  if message.content.find('swanson') > -1:
    await message.channel.send(get_ron_swanson())

  if message.content.find('yeet') > -1:
    await message.channel.send('yeet!!!!')

  if message.content.find('dog') > -1:
    await message.channel.send(get_dog_image())

  if message.content.find('cat') > -1:
    await message.channel.send(get_cat_image())

  



client.run(os.getenv('TOKEN'))