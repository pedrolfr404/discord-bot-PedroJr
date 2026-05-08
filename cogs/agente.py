from discord.ext import commands
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('agent_key'))
model = genai.GenerativeModel('gemini-2.5-flash')

class IA(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['pergunta', 'ia'])
    async def agente(self, ctx: commands.Context, *, msg):
        async with ctx.typing():
            try:
                prompt = f"Você é um assistente em um servidor de amigos no Discord. Responda de forma curta e amigável: {msg}"
                
                response = model.generate_content(prompt)

                resposta_texto = response.text
                if len(resposta_texto) > 2000:
                    resposta_texto = resposta_texto[:1990] + "..."

                await ctx.reply(resposta_texto)

            except Exception as e:
                print(f"Erro no Gemini: {e}") # Isso ajuda VOCÊ a ler o erro no console
                await ctx.reply('Erro ao processar sua pergunta.')

async def setup(bot):
    await bot.add_cog(IA(bot))