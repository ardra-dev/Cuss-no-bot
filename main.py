
import os
import discord
from content_filter import Filter
from keep_alive import keep_alive
import random 

filter=Filter()
response = ('What cause you do this? Stop swearing, go read your books','Swearing is not good so shutup and stop','bla bla bla stop swearing , I can ban u','My creator can see  wht you swore so better not unless u wanna get banned.')

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format (client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if filter.check(message.content).as_bool:
    await message.delete()
    print (message.author.name+':'+ message.content)
    response_num=random.randint(0,3)
    await message.channel.send(response[response_num])
    return  

  if message.content.startswith('hey cuss-no-bot'):
    await message.channel.send('Yo! What up (dont say the sky or ceiling it cheesy) ')

  

my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)

