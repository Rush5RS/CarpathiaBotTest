import discord
from discord.ext import commands

class hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_role(795362038212984842)
    @commands.check(lambda ctx: ctx.channel.id==1229038944889344081)

    async def hirush(self, ctx):
        guild = self.bot.get_guild(739233428683096144)
        channellog = guild.get_channel(1229053022152167568)
        await ctx.send('fuck off <@327499132900081669>')

    @hirush.error
    async def hirush_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            guild = self.bot.get_guild(739233428683096144)
            channellog = guild.get_channel(1229053022152167568)
            await channellog.send(f'''<@{ctx.author.id}> was a noob and didn't have the right role''')
        elif isinstance(error, commands.CheckFailure):
            guild = self.bot.get_guild(739233428683096144)
            channellog = guild.get_channel(1229053022152167568)
            await channellog.send(f'''<@{ctx.author.id}> was a noob and didn't have the right channel''')

async def setup(bot):
    await bot.add_cog(hello(bot))
