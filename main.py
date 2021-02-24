import discord
from flask import Flask
from threading import Thread
import asyncio

app = Flask('')


@app.route('/')
def main():
  return "Your Bot Is Ready"

def run():
  app.run(host="0.0.0.0", port=8000)

def keep_alive():
  server = Thread(target=run)
  server.start()

client = discord.Client()

@client.event
async def on_ready(self):
  print("Bot is ready")

@client.event
async def on_ready():
    client.loop.create_task(status())

    
async def status():
  while True:
    await client.wait_until_ready()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name= " modmails in bot hometown"),)
    await asyncio.sleep(12)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name= " moderators"),)
    await asyncio.sleep(12)

@client.event
async def on_message(message):
    empty_array = []
    modmail_channel = discord.utils.get(client.get_all_channels(), name="mod-mail")

    if message.author == client.user:
        return
    if str(message.channel.type) == "private":
        if message.attachments != empty_array:
            files = message.attachments
            await modmail_channel.send("[" + message.author.display_name + "]")

            for file in files:
                await modmail_channel.send(file.url)
        else:
            await modmail_channel.send("[" + message.author.display_name + "] " + message.content)

    elif str(message.channel) == "mod-mail" and message.content.startswith("<"):
        member_object = message.mentions[0]
        if message.attachments != empty_array:
            files = message.attachments
            await member_object.send("[" + message.author.display_name + "]")

            for file in files:
                await member_object.send(file.url)
        else:
            index = message.content.index(" ")
            string = message.content
            mod_message = string[index:]
            await member_object.send("[" + message.author.display_name + "]" + mod_message)

keep_alive()
client.run('TOKEN')
