import discord
from discord.ext import commands

class reacts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.roles = {
            1057979436533813258: [795362038212984842], # Oldge > Onyx
            1088176661318606958: [1229062444471681106], # Huh > Gamer
            979179040172814397: [1229062397944270858] # Pray > Cutie
            }

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, ctx):
        guild = self.bot.get_guild(739233428683096144)
        channel = guild.get_channel(1229075810774941776)
        message = await channel.fetch_message(1229075845520298065)
        emojiID = ctx.emoji.id
        member = ctx.member
        if message.id == ctx.message_id:
            for roleID in self.roles:
                if emojiID == roleID:
                    role = discord.utils.get(guild.roles, id = self.roles[roleID][0])
                    await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, ctx):
        guild = self.bot.get_guild(739233428683096144)
        channel = guild.get_channel(1229075810774941776)
        message = await channel.fetch_message(1229075845520298065)
        emojiID = ctx.emoji.id
        member = await (guild.fetch_member(ctx.user_id))
        if message.id == ctx.message_id:
            for roleID in self.roles:
                if emojiID == roleID:
                    role = discord.utils.get(guild.roles, id = self.roles[roleID][0])
                    await member.remove_roles(role)

async def setup(bot):
    await bot.add_cog(reacts(bot))