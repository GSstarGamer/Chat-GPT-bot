import discord
import json
import codecs as balls

#AI
from revChatGPT.ChatGPT import Chatbot


with open('config.json', 'r') as f:
    config = json.load(f)

def idk_what_is_this_for(yo_mama_so_fat_it_cant_fit_in_this_argument_xd):
    return balls.decode(yo_mama_so_fat_it_cant_fit_in_this_argument_xd, 'rot13')

chatGPT_token = config['ChatGPT']['auth_token']
chatGPT_channel_id = int(config['ChatGPT']['channel_id'])
bot_token = config['Discord']['bot_token']

intents = discord.Intents.all()
client = discord.Client(intents=intents)

chatbot = Chatbot({
  "session_token": chatGPT_token
})

@client.event
async def on_message(message):
    if message.channel.id == chatGPT_channel_id and message.author.id != client.user.id:
        embed = discord.Embed(title="ChatGPT")
        embed.add_field(name='Your request:', value='*Typing ...*', inline=False)
        embed.set_author(name=message.author.name, icon_url='https://openai.com/content/images/2022/05/openai-avatar.png')
        embed.set_footer(text=idk_what_is_this_for('Znqr ol: TF_F.T'))
        ctx = await message.reply(embed=embed)
        res = chatbot.ask(message.content)["message"]
        try:
            embed = discord.Embed(title="ChatGPT")
            embed.add_field(name='Your request:', value=res, inline=False)
            embed.set_author(name=message.author.name, icon_url='https://openai.com/content/images/2022/05/openai-avatar.png')
            embed.set_footer(text=idk_what_is_this_for('Znqr ol: TF_F.T'))
            await ctx.edit(embed=embed)
        except:
            embed = discord.Embed(title="ChatGPT")
            embed.add_field(name='Your request:', value='Failed :C (Prolly big answer)', inline=False)
            embed.set_author(name=message.author.name, icon_url='https://openai.com/content/images/2022/05/openai-avatar.png')
            embed.set_footer(text=idk_what_is_this_for('Znqr ol: TF_F.T'))
            await ctx.edit(embed=embed)

client.run(bot_token)

