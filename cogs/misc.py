from discord.ext import commands
from random import randint
import datetime

class Misc(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  #say--------------------------------------------------------------------------
  @commands.command(aliases=['falar', 'fala']) #say
  async def say(self, ctx: commands.Context, *,texto):
    await ctx.message.delete()
    await ctx.send(texto)


  #dado-------------------------------------------------------------------------
  @commands.command(aliases=['dado', 'rolar'])
  async def dice(self, ctx:commands.Context, r=6, time=1):
    if time > 20:
      return await ctx.reply("Número máximo de rolagens é 20!")
    if time != 1:
      msg = ""
      for i in range(0,time):
        n = randint(1,r)
        msg += f'{i+1}° :game_die: | Você rolou um d{r}... e conseguiu {n}!\n'
      return await ctx.reply(msg)
    n = randint(1,r)
    await ctx.reply(f':game_die: | Você rolou um d{r}... e conseguiu {n}!')

  @dice.error
  async def dice_error(self, ctx, error):
    if isinstance(error, commands.BadArgument):
      await ctx.reply("Argumentos incorretos! utilize o exemplo:`.dice <número_dado> <qtd_vezes>`")


  #hoje-------------------------------------------------------------------------
  @commands.command(aliases=['today', 'data'])
  async def hoje(self, ctx:commands.Context):
    data = datetime.datetime.now()
    data_formatado = data.strftime("%d/%m/%Y %H:%M:%S")
    await ctx.reply(data_formatado)

async def setup(bot):
    await bot.add_cog(Misc(bot))