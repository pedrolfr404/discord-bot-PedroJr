import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

#carrega o token do bot, do .env
load_dotenv()
bot_token = os.getenv('bot_key')

class MyBot(commands.Bot):
  def __init__(self):  
    intents = discord.Intents.all() #Configura as permissoes do bot (todas)
    super().__init__('.', intents=intents)
  
  async def setup_hook(self):
    for filename in os.listdir('./cogs'): # itera sobre os arquivos dentro do diretorio cogs
      if filename.endswith('.py'): # verifica se é um arquivo .py
        try:
          # Carrega a extensão (ex: cogs.acoes)
          await self.load_extension(f'cogs.{filename[:-3]}')
        except Exception as e:
          print(f'Erro ao carregar {filename}: {e}')
  
    print("Bot inicializado")


bot = MyBot()
bot.remove_command('help') #Remove o comando help default
bot.run(bot_token)