# Import discord.py. Allows access to Discord's API.
import discord

# Import the os module.
import os

# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv

# Import commands from the discord.ext module.
from discord.ext import commands

# Loads the .env file that resides on the same level as the script.
load_dotenv()

# Grab the API token from the .env file.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Creates a new Bot object with a specified prefix. It can be whatever you want it to be.
bot = commands.Bot(command_prefix="$")

# on_message() event listener. Notice it is using @bot.event as opposed to @bot.command().
@bot.event
async def on_message(message):
	# Check if the message sent to the channel is "hello".
	if message.content == "hello":
		# Sends a message to the channel.
		await message.channel.send("pies are better than cakes. change my mind.")

	# Includes the commands for the bot. Without this line, you cannot trigger your commands.
	await bot.process_commands(message)

# Command $ping. Invokes only when the message "$ping" is send in the Discord server.
# Alternatively @bot.command(name="ping") can be used if another function name is desired.
@bot.command(
	# Adds this value to the $help ping message.
	help="Uses come crazy logic to determine if pong is actually the correct value or not.",
	# Adds this value to the $help message.
	brief="Prints pong back to the channel."
)
async def ping(ctx):
	# Sends a message to the channel using the Context object.
	await ctx.channel.send("pong")

# Command $print. This takes an in a list of arguments from the user and simply prints the values back to the channel.
@bot.command(
	# Adds this value to the $help print message.
	help="Looks like you need some help.",
	# Adds this value to the $help message.
	brief="Prints the list of values back to the channel."
)
async def print(ctx, *args):
	response = ""

	# Loops through the list of arguments that the user inputs.
	for arg in args:
		response = response + " " + arg

	# Sends a message to the channel using the Context object.
	await ctx.channel.send(response)

# Executes the bot with the specified token. Token has been removed and used just as an example.
bot.run(DISCORD_TOKEN)
