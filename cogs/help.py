from discord.ext import commands
from discord import Embed, Color


embed_help = Embed(
  title=':books: COMANDOS ATÉ AGORA',
  description='Em breve mais coisas...',
  color=Color.pink(),
)
embed_help.add_field( #prefixo
  name='**Prefixo**',
  value='`É um . talvez depois eu coloque comando pra mudar fodase`',
  inline=False
)
embed_help.add_field( #bdsm
  name='BDSM', 
  value='`.lick <@user>` - Dá uma laimbida em alguém\n`.spank <@user>` - Dá um tapa em alguém\n`.kill <@user>` - Mata alguém\n`.piru <@user>` - Mede o piru de alguém',
  inline=False
)
embed_help.add_field( #outros
  name='Outros',
  value='`.say <mensagem>` - O bot fala alguma coisa\n`.dice <num_dado> <qtd_rolls>` - O dado y é rolados x vezes\n`.hoje` - Comando mais inutil do mundo\n`.ajuda` - O bot exibe painel de ajuda'
)


class Ajuda(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['help', 'ajudar']) #help
  async def ajuda(self, ctx:commands.Context):
    await ctx.reply(embed=embed_help)


async def setup(bot):
    await bot.add_cog(Ajuda(bot))