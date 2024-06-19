import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta

bot = commands.Bot(command_prefix='-', intents = discord.Intents.all())
status = ["-helpme เพื่อดูวิธีการใช้","ขอให้มีความสุขในวันนี้"]
@bot.command()
async def helpme(ctx):
    embed1 = discord.Embed(title = "วิธีการใช้งาน",description = "พิมพ์ - ตามด้วยคำสั่งต่างๆ",colour =0x99CCFF)
    embed1.add_field(name = " -ACM ",value=" เพื่อดูคำสั่งทั้งหมด", inline = False)
    embed1.set_author(name = "Click to join Bot's server",url = 'ลิงค์เซิร์ฟเวอร์ที่ต้องการ')
    await ctx.send(embed = embed1)

@bot.command()
async def ACM(dm):
    embed2 = discord.Embed(title = "All commands", description = "",colour = 0xFFDEAD)
    await dm.send(embed = embed2)

@tasks.loop(seconds = 5)
async def change_bot_status():
    await bot.change_presence(activity=discord.Game(name=status[0]))
    status.append(status.pop(0))
    
@bot.event
async def on_ready():
    change_bot_status.start()
    print("Link started")

@bot.event
async def on_message(message):
    print(message)
    print(message.content)
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(IDช่องที่ต้องการให้บอทแสดง)
    text = f"ยินดีต้อนรับ คุณ,{member.mention}, ขอให้สนุกกับการทดลองใช้งานบอท"
    emmbed2 = discord.Embed(title = "Welcome to bot's server",
                          description = text,
                          color = 0xCC0033)
    await channel.send(embed = emmbed2)
    

    

  

bot.run("Token")
