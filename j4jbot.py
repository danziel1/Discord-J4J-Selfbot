import discord
from discord.ext import commands, tasks
import random
import asyncio
import datetime


min_age = '14' # minimum account age when doing j4j
response_delay = random.randint(3,8) # delay after responding when someone DMs you
done_delay = random.randint(15,20) # delay between saying your done message after sending your message
msg_delay = random.randint(20,30) # delay between sending j4j messages to servers

done_msg = [
'done',
'dn',
'I joined'
] # message sent after you send your response msg
j4j_msg = [
'j4j',
'j4j fast',
'join 4 join',
'j4j dm fast',
'j4j fast',
'j4j NO BOTS',
'j4j no bots pls',
'j4j old accounts only',
'j4j dm',
'J4J'
] # message sent to server's j4j channels
dm_msg = [
'join my cool server',
'Check out this server!',
'join please!'
] # first message sent when you do j4j with someone

link = '' # server invite link 
token = '' # your token

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!',self_bot=True)
ready = False

@bot.event
async def on_ready():
    print(f"Starting bot as {bot.user}")


@tasks.loop(minutes=msg_delay)
async def j4j():
    for guild in bot.guilds:
        for channel in guild.channels:
            if 'j4j' in channel.name:
                print(channel.name)
                channel = bot.get_channel(channel)
                try:
                    await channel.send(random.choice(j4j_msg))
                    print(f"> Sent message in {channel.name} in {guild.name}")
                except:
                    print(f"> Couldn't send message in {channel.name} in {guild.name}")
@j4j.before_loop
async def before_j4j():
  await bot.wait_until_ready()
j4j.start()


try:
    file = open('data.txt', 'r')
except:
    print("Creating data file, this tracks who you do j4j with so you don't repeat people.")
    file = open('data.txt', 'w')
@bot.event
async def on_message(message):
    if message.author != bot.user:
        if not message.guild:
            file = open('data.txt', 'r').readlines()
            if str(message.author.id)+'\n' in file:
                pass
            else:
                print(f"> Doing J4J with {message.author} ({message.author.id})")
                age = str(datetime.datetime.now()-message.author.created_at)
                age = age.split(' days,')
                age = int(age[0])
                if age >= int(min_age):
                    file = open('data.txt', 'a')
                    file.write(str(message.author.id)+'\n')
                    await asyncio.sleep(response_delay)
                    await message.author.send(random.choice(dm_msg)+'\n'+link)
                    await asyncio.sleep(done_delay)
                    await message.author.send(random.choice(done_msg))
                    
bot.run(token, bot=False)