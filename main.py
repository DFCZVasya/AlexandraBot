import discord

def get_token():
    with open("C:/ds_token/TOKEN.txt", 'r') as f:
        TOKEN = f.read()
    return TOKEN

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    print(message.content)
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        print(message.author.mention)
        await message.channel.send(msg)

    if 'С' in message.content and 'А' in message.content and 'Н' in message.content and 'Я' in message.content:
        print(message.author.mention)
        if message.author.mention == '<@283512075974606849>' or if message.author.mention == '<@!291879094864576512>':
            msg = 'ДаДаЯЯЯЯЯЯЯЯЯЯЯ'
            await message.channel.send(msg)
        else:
            msg = 'Ты вообще кто, чтобы меня так звать? Только Александра и никак иначе :rage:'
            await message.channel.send(msg)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(get_token())
