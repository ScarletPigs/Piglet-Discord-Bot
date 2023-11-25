from discord.ext import commands
from discord import Member, app_commands
from datetime import datetime

SCHEDULING_PREDICATES = [
    commands.has_role('Mission Maker')
]

# Scheduling Cog
## This is where all scheduling commands will be handled
class Scheduling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.dates = [] # A list of the dates of the 10 next Sundays
        for i in range(10):
            date = datetime.today().date() + datetime.timedelta(days=7*i)
            self.dates.append(app_commands.Choice(date.strftime('%d-%m-%Y'), date))

    
    async def cog_check(self, ctx):
        for predicate in SCHEDULING_PREDICATES:
            if not await predicate(ctx):
                return False
        return True
    
    @app_commands.command()
    @app_commands.choices(['add', 'edit', 'remove'])
    async def reservesunday(self, ctx, date : datetime.date):
        member = member or ctx.author
        
        await ctx.send(f'{member.mention} has reserved Sunday!')
        
    @commands.command()
    async def editsunday(self, ctx, date : commands.parameter(name='date', type=datetime, default=None)):
        member = member or ctx.author
        
        await ctx.send(f'{member.mention} has edited Sunday!')
        
    @commands.command()
    async def removesunday(self, ctx, date : commands.parameter(name='date', type=datetime, default=None)):
        member = member or ctx.author
        
        await ctx.send(f'{member.mention} has deleted Sunday!')