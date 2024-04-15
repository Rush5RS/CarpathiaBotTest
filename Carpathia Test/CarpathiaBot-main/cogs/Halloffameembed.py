import discord
from discord.ext import commands
from datetime import datetime

class embeds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.perms = [327499132900081669, 364558577194631170]
        print(self.perms)

    @commands.command()
    @commands.check(lambda ctx: ctx.author.id in ctx.cog.perms)
    async def postembed(self, ctx):
        guild = self.bot.get_guild(739233428683096144)
        channel = guild.get_channel(1229038944889344081)
        embed = discord.Embed(title="Carpathia self-assign tool",
                        description='''Looks cool below huh
                        \n
                        \nhttps://automatic.links
                        \n> Block Quotes
                        \n```
                        \nReact to this message to be assigned a role
                        \n```
                        \n<:oldge:1057979436533813258> Oldge
                        \n<:HUH:1088176661318606958> Huh
                        \n<:PESXMas_Pray:979179040172814397> PesXmasPray
                        \n
                        \n<@&795362038212984842>
                        \n<@&1229062444471681106>
                        \n<@&1229062397944270858>
                        \n
                        \n||Spoilers||
                        \n~~Strikethrough~~
                        \n**Strong**
                        \n__Underline__''',
                        colour=0xb70101,
                        timestamp=datetime.now())

        embed.add_field(name="Test field",
                    value="This is the field value.",
                    inline=False)
        embed.add_field(name="The first inline field.",
                        value="This field is inline.",
                        inline=True)
        embed.add_field(name="The second inline field.",
                        value="Inline fields are stacked next to each other.",
                        inline=True)
        embed.add_field(name="The third inline field.",
                        value="You can have up to 3 inline fields in a row.",
                        inline=True)
        embed.add_field(name="Even if the next field is inline...",
                        value="It won't stack with the previous inline fields.",    
                        inline=True)

        embed.set_image(url="https://upload.wikimedia.org/wikipedia/commons/c/ce/RMS-Carpathia.jpg")

        embed.set_footer(text="Self-assign")

        message = await ctx.send(embed=embed)
        await message.add_reaction('<:oldge:1057979436533813258>')
        await message.add_reaction('<:HUH:1088176661318606958>')
        await message.add_reaction('<:PESXMas_Pray:979179040172814397>')


    
    @commands.command()
    @commands.has_role(795362038212984842)
    async def updateembed(self, ctx, messageID):
        channel = ctx.channel
        message = await channel.fetch_message(messageID)
        embed = message.embeds[0]
        embed.title = 'Lets see if this works'
        await message.edit(embed=embed)


    @postembed.error
    async def postembed_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            guild = self.bot.get_guild(739233428683096144)
            channellog = guild.get_channel(1229053022152167568)
            await channellog.send(f'''<@{ctx.author.id}> was a noob and didn't have the right role''')
        elif isinstance(error, commands.CheckFailure):
            guild = self.bot.get_guild(739233428683096144)
            channellog = guild.get_channel(1229053022152167568)
            await channellog.send(f'''<@{ctx.author.id}> was a noob and didn't have the right channel''')

async def setup(bot):
    await bot.add_cog(embeds(bot))
