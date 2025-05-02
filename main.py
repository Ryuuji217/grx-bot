
import discord
from discord.ext import commands
from discord.utils import get
import random
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

WELCOME_CHANNEL_ID = 1234567890  # Ersetze mit deinem Channel
LOG_CHANNEL_ID = 1234567890      # Ersetze mit deinem Mod-Log-Channel
MEMBER_ROLE_NAME = "Mitglied"

BLACKLIST = ["hure", "nazi", "verpiss"]

@bot.event
async def on_ready():
    print(f"GRX-Bot ist online als {bot.user}")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    role = get(member.guild.roles, name=MEMBER_ROLE_NAME)
    if role:
        await member.add_roles(role)
    if channel:
        await channel.send(embed=discord.Embed(title="Willkommen bei Gaming Realm X!", description=f"Hey {member.mention}, schön dass du da bist!", color=0x8e44ad))

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    if any(bad_word in content for bad_word in BLACKLIST):
        await message.delete()
        await message.channel.send(f"{message.author.mention}, deine Nachricht wurde wegen unangebrachter Sprache gelöscht.")
        return

    if content.isupper() and len(content) > 5:
        await message.channel.send(f"{message.author.mention}, bitte nicht schreien!")

    await bot.process_commands(message)

@bot.command()
async def hilfe(ctx):
    embed = discord.Embed(title="GRX-Bot Hilfe", description="Hier sind meine Befehle:", color=0x9b59b6)
    embed.add_field(name="!hilfe", value="Zeigt dieses Hilfemenü.", inline=False)
    embed.add_field(name="!regeln", value="Zeigt die Serverregeln.", inline=False)
    embed.add_field(name="!grx", value="Info über den Server.", inline=False)
    embed.add_field(name="!vibecheck", value="Zufälliger Spruch.", inline=False)
    embed.add_field(name="!galaxy", value="GRX GIF drop.", inline=False)
    embed.add_field(name="!suche [Spiel]", value="Sucht Mitspieler.", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def regeln(ctx):
    await ctx.send("1. Sei respektvoll\n2. Kein Spam\n3. NSFW verboten\n4. Mods haben das letzte Wort")

@bot.command()
async def grx(ctx):
    await ctx.send(embed=discord.Embed(title="Gaming Realm X", description="Dein Ort für Vibes, Games & Galaxy-Energie.", color=0x6c5ce7))

@bot.command()
async def vibecheck(ctx):
    vibes = ["GRX-Energie: 100%", "Du bist heute OP!", "Galaxy-Modus aktiviert", "Einfach nur Ehrenmann"]
    await ctx.send(random.choice(vibes))

@bot.command()
async def galaxy(ctx):
    await ctx.send("https://media.giphy.com/media/QxkfC2gPyzpYY/giphy.gif")

@bot.command()
async def suche(ctx, *, spiel):
    await ctx.send(f"{ctx.author.mention} sucht Mitspieler für **{spiel}**! Reagier, wenn du Bock hast!")

# Bot aktiv halten
keep_alive()

# Token hier einfügen
bot.run("")
