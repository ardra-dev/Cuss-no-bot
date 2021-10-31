
import os
import discord
from content_filter import Filter
from keep_alive import keep_alive
import random
from replit import db



filter=Filter()
filter.add_exceptions(['Who r u', 'Who are you','I lost it','st it', 'lost','got','wht', 'This is what I typed'])
response = ('What cause you do this? Stop swearing, go read your books','Swearing is not good so shutup and stop','bla bla bla stop swearing , I can ban u','My creator can see  wht you swore so better not unless u wanna get banned     https://tenor.com/view/language-rhino-ryan-burton-love-live-serve-dont-curse-gif-18354364')

hello = ('Yo! What up (dont say the sky or ceiling it cheesy) ', 'Hey! I am Cuss-no-bot , A bot from a far away galaxy destined to stop swearing!', 'Hey , Ughh I an tired of doing this but I am cuss-no-bot here to stop swearing')

client = discord.Client()


@client.event
async def on_ready():
  global admin_user
  print('We have logged in as {0.user}'.format (client))
  admin_user=await client.fetch_user(888002342388121620)
  print('Admin is : '+admin_user.name)

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if filter.check(message.content).as_bool:
    await message.delete()
    print (message.author.name+':'+ message.content)
    response_num=random.randint(0,3)
    await message.channel.send(response[response_num])
    await admin_user.send(message.author.name+' sent this- '+ message.content )
    return  

  if message.content.startswith('hey cuss-no-bot'):
    hello_num=random.randint(0,2)
    await message.channel.send(hello[hello_num])

  

my_secret = os.environ['TOKEN']
keep_alive()
client.run(my_secret)

