import json
import discord
from discord.ext import commands
import aiohttp
from chaves import chave_clima

async def clima(ctx: commands, city, outro):
  async with aiohttp.ClientSession() as session:
    async with session.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city},{outro}code&limit=1&appid={chave_clima}') as response:
      if response.status != 200:
        return ctx.reply('ERRO')
      
      dados = response.json()

      if not dados:
        return ctx.reply('Nao encontrei essa cidade.')
      
      lat = dados[0]['lat']
      lon = dados[0]['lon']
      weather_get(lat, lon)

async def weather_get(lat, lon):

  async with aiohttp.ClientSession() as session:
    async with session.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={chave_clima}&units=metric&lang=pt_br'):
      pass


  embed = discord.Embed(
    title=f'Previsão do tempo para {cdd}, {pais}',
    color=discord.Colour.blue(),
    description=f'{ceu}',
  )
  embed.add_field(
    inline=True,
    name=':thermometer: temperatura',
    value=f'Atual:{atual:.2f}ºC\nMáxima:{maxima:.2f}ºC\nMínima:{minima:.2f}ºC'
  )
  embed.add_field(
    inline=True,
    name=':sweat_drops: Umidade',
    value=f'{umid:.2f} %'
  )
  embed.add_field(
    inline=True,
    name=':wind_blowing_face: Vel. do Vento',
    value=f'{vento:.2f} km/h'
  )
  embed.add_field(
    inline=True,
    name=':person_lifting_weights: Pressão do ar',
    value=f'{pressao:.2f} kPa'
  )