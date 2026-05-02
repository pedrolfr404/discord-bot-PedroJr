import discord
from discord.ext import commands
import aiohttp
import os
from dotenv import load_dotenv


load_dotenv()
weather_key = os.getenv('chave_clima')

class clima(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['weather', 'clima','tempo'])
  async def weather_get(self, ctx: commands, *, city):
    # obter latitude e longitude pelo nome da cidade
    async with aiohttp.ClientSession() as session: 
      async with session.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}code&limit=1&appid={weather_key}') as response:
        if response.status != 200:
          return ctx.reply('ERRO')
        
        dados = await response.json()

        if not dados:
          return ctx.reply('Nao encontrei essa cidade.')
        
        lat = dados[0]['lat']
        lon = dados[0]['lon']
        async with session.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_key}&units=metric&lang=pt_br') as info_tempo:

          if info_tempo.status != 200:
            return ctx.reply('ERRO')
        
          dados = await info_tempo.json()

          if not dados:
            return ctx.reply('ERRO ao encontrar informações')      
          
          pais = dados['sys']['country']
          ceu = dados['weather'][0]['description']
          main = dados['main']
          vento = dados['wind']['speed']

          embed = discord.Embed(
            title=f'Previsão do tempo para {city}',
            color=discord.Colour.blue(),
            description=f'{ceu}',
          )
          embed.add_field( #temperatura
            inline=True,
            name=':thermometer: temperatura',
            value=f"Atual:{main['temp']:.2f}ºC\nMáxima:{main['temp_max']:.2f}ºC\nMínima:{main['temp_min']:.2f}ºC"
          )
          embed.add_field( #umidade
            inline=True,
            name=':sweat_drops: Umidade',
            value=f"{main['humidity']:.2f} %"
          )
          embed.add_field( #vento km/h
            inline=True,
            name=':wind_blowing_face: Vel. do Vento',
            value=f"{vento:.2f} km/h"
          )
          embed.add_field( #pressao ar
            inline=True,
            name=':person_lifting_weights: Pressão do ar',
            value=f"{main['sea_level']:.2f} kPa"
          )

          await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(clima(bot))