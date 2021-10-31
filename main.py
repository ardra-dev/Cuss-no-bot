
import os
import discord
from content_filter import Filter
from keep_alive import keep_alive

filter=Filter()
response = ('')

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
    await message.channel.send('What cause you do this? Stop swearing, go read your books')
    return  

  if message.content.startswith('hey cuss-no-bot'):
    await message.channel.send('Yo! What up (dont say the sky or ceiling it cheesy) ')

  

my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)

