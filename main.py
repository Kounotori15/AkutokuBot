import discord

client = discord.Client()

@client.event
async def on_ready():
  print("logged in as " + client.user.name)

@client.event
async def on_message(message):
  if message.author != client.user:
    msg = message.author.mention + " Hi."
    await client.send_message(message.channel, msg)

client.run("NTI1MzA5MDg5NzEwOTk3NTI1.Dv0wJA.aLLPPg0BM7PPn--b6oJIL5i9M0U")