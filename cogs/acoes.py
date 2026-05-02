from discord.ext import commands
import discord
from random import choice, randint


gif_spank = [
  'https://c.tenor.com/yuh760_cQAIAAAAC/tenor.gif',
  'https://c.tenor.com/so_JB7XlqfMAAAAC/tenor.gif',
  'https://c.tenor.com/FUasrpVQaKIAAAAC/tenor.gif',
  'https://c.tenor.com/KI2iIP6dFTcAAAAC/tenor.gif',
  'https://media.discordapp.net/attachments/991859250907336796/1499578934852059176/E964FB80-77CC-4D9D-AFE6-6E8075271B1C.gif?ex=69f54f36&is=69f3fdb6&hm=b21452b4113c6c7182b11e21ae9639929e3f23aedce39b48a6034aed49136d13&=',
  'https://media.discordapp.net/attachments/991859250907336796/1499579061981155328/B5F1EBA6-C6A9-490A-AC6D-A109B86A7D59.gif?ex=69f54f55&is=69f3fdd5&hm=f2f2a2fc7fe131179c4f3ff44b68c726c063e44574668898de212293e04b3804&=',
  'https://media.discordapp.net/attachments/991859250907336796/1499578934507995278/DB279EB3-A5D6-45A8-B494-1EE00C0816C3.gif?ex=69f54f36&is=69f3fdb6&hm=c24e534eed367f77ea118a270228506b081af2a897295709693529581a84d138&=',

]

gif_lick = [
  'https://c.tenor.com/1w_SiTTl8joAAAAd/tenor.gif',
  'https://c.tenor.com/Y7hs3Jf5i1EAAAAC/tenor.gif',
  'https://c.tenor.com/zt-J3QJoWbEAAAAC/tenor.gif',  
  'https://c.tenor.com/aompZY0xHZcAAAAd/tenor.gif',
  'https://c.tenor.com/rQDYjWeWzlgAAAAC/tenor.gif',
  'https://cdn.discordapp.com/attachments/991859250907336796/1499578651572703473/9C839885-0A98-4F19-B83D-4FD648096ADE.gif',
  'https://cdn.discordapp.com/attachments/991859250907336796/1499578561051492392/68033085-4B93-4C58-8FC7-4FF602321552.gif',
]

gif_kill = [
  'https://c.tenor.com/8TfmfQv5lqgAAAAC/tenor.gif',
  'https://c.tenor.com/xyIxShJv3n0AAAAC/tenor.gif',
]


embed_piru = discord.Embed(
  color=discord.Colour.dark_green(),
  title='Maquina de piru'
)


class Acoes(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  #lick------------------------------------------------------------------------------------------
  @commands.command(aliases=['lamber', 'lambida', 'leimber']) 
  async def lick(self, ctx:commands.Context, user_licked: discord.Member=None):
    if user_licked is None:
      await ctx.reply('É preciso mencionar o usuario a ser lembido ex: ```.lick @user```')
    else:
      autor = ctx.author.mention
      alvo = user_licked.mention

      if alvo == autor:
        await ctx.reply('Não é possível se leimber, safadeza!')
      
      else:
        gif = choice(gif_lick)
        embed = discord.Embed(
          description=f'**:clap: {autor} leimbeu {alvo}**', 
          color=discord.Color.blue()
        )
        embed.set_image(url=gif)
        await ctx.reply(embed=embed)

  # lick error
  @lick.error 
  async def lick_error(self, ctx, error):
    if isinstance(error, commands.BadArgument):
      await ctx.reply("Não consegui encontrar esse usuário.")


  #spank-----------------------------------------------------------------------------------------
  @commands.command(aliases=['espancar', 'bater']) 
  async def spank(self, ctx:commands.Context, user_spanked: discord.Member=None):
    if user_spanked is None:
      await ctx.reply('É preciso mencionar o usuario a ser spanked ex: ```.spank @user```')
    else:
      alvo = user_spanked.mention
      autor = ctx.author.mention
      
      if alvo == autor:
        await ctx.reply('Não é possível se espancar ta maluco!')
      
      else:

        gif = choice(gif_spank)
        embed = discord.Embed(
          description=f'**:clap: {autor} espancou {alvo}**', 
          color=discord.Color.magenta()
        )
        embed.set_image(url=gif)
        await ctx.reply(embed=embed)

  # spank error
  @spank.error 
  async def spank_error(self, ctx, error):
    if isinstance(error, commands.BadArgument):
      await ctx.reply("Não consegui encontrar esse usuário.")


  #kill------------------------------------------------------------------------------------------
  @commands.command(aliases=['matar']) 
  async def kill(self, ctx:commands.Context, user: discord.Member=None):
    if user is None:
      await ctx.reply('É preciso mencionar o usuario a ser morto ex: ```.kill @user```')
    else:
      alvo = user.mention
      autor = ctx.author.mention

      if alvo == autor:
        await ctx.reply('Não é possível se suicidar! Ainda...')
      
      else:

        gif = choice(gif_kill)
        embed = discord.Embed(
          description=f'**:knife: {autor} matou {alvo}**', 
          color=discord.Color.red()
        )
        embed.set_image(url=gif)
        await ctx.reply(embed=embed)

  # kill error
  @kill.error 
  async def kill_error(self, ctx, error):
    if isinstance(error, commands.BadArgument):
      await ctx.reply("Não consegui encontrar esse usuário.")


  #piru------------------------------------------------------------------------------------------
  @commands.command(aliases=['pp'])
  async def piru(self, ctx:commands.Context, user_piru: discord.Member=None):
    embed_piru.clear_fields()
    autor = ctx.author.name
    pp = randint(0,32)
    if user_piru != None:
      alvo = user_piru.name
      embed_piru.add_field(
        name=f'piru de {alvo}',
        value=f'**8{'='*(pp//4)}D**',
        inline=False
      )
      await ctx.reply(embed=embed_piru)
      return
    
    embed_piru.add_field(
        name=f'piru de {autor}',
        value=f'**8{'='*(pp//4)}D**',
        inline=False
      )
    await ctx.reply(embed=embed_piru)

  #piru error
  @piru.error 
  async def piru_error(self, ctx, error):
    if isinstance(error, commands.BadArgument):
      await ctx.reply("Não consegui encontrar esse usuário.")


async def setup(bot):
    await bot.add_cog(Acoes(bot))