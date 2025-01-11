# okay ill admit, i made this bot in the span of ~2-3 hours at midnight, running off of half a single sugar free monster energy.
# first project ive made in a few months, too. the code's probably messier than my closet, so yeah...
# i tried my best to make the documentation and comments straightforward, but if you need help dm me, @bugsync on discord
# good luck if you try and edit anything besides the more simple variables..
# HUGE thanks to Xtr4F for the pycharacterai library, they're what made this bot possible

import discord
import asyncio
from PyCharacterAI import get_client
from PyCharacterAI.exceptions import SessionClosedError, ActionError



# set up intents
intents = discord.Intents.default()
intents.messages = True  
intents.message_content = True  
client = discord.Client(intents=intents)

# replace with your tokens
discord_token = 'dctoken'
ai_token = "caitoken"  
# discord token is acquired via dev portal, c.ai token you gotta inspect page, networking, yada yada.. look at the readme <3



# global variables to manage ai client and chat session
ai_client = None
ai_chat = None
character_id = "ZgTZeeaUnm2ifc4pzNlk02yPIJGUvVKw-H0Da9E5Pl8"  # default character id, feel free 2 change

async def setup_ai_client():
    # initializes the ai client and chat session
    global ai_client, ai_chat
    ai_client = await get_client(token=ai_token)
    ai_chat, _ = await ai_client.chat.create_chat(character_id)


async def is_valid_character_id(character_id_to_validate):
    # validates a character id by attempting to create a chat session
    test_client = await get_client(token=ai_token)
    try:
        await test_client.chat.create_chat(character_id_to_validate)
        return True
    except ActionError:
        return False


@client.event
async def on_ready():
    # prints when the bot connects to discord and/or connects to the ai client
    print(f"Logged in as {client.user}")
    await setup_ai_client()
    print("AI client setup complete")


@client.event
async def on_message(message):
    # handles incoming messages, prints to shell for logging/debugging
    global ai_client, ai_chat, character_id
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
    print(f"{username} says: {user_message} --- ((CHANNEL: {channel}))")

    # ignore messages from the bot itself to prevent loops
    if message.author == client.user:
        return
    # ooc keyword for when you dont want a reply (but moving channels can also work... ya lazy bum)
    if user_message.startswith("((OOC))"):
        return

    # handle id submissions in the "character-id-submissions" channel, change the first if statement if you wanna use a different channel
    if channel == "character-id-submissions":
        new_character_id = user_message.strip()
        if new_character_id:  # ensure the message isn't empty
            if await is_valid_character_id(new_character_id):
                character_id = new_character_id
                await setup_ai_client()  # reinitialize ai client with new character id
                await message.channel.send(
                    f"Character ID updated to `{character_id}` and AI session restarted successfully!"
                )
            else:
                await message.channel.send(
                    f"Invalid Character ID `{new_character_id}`. Please provide a valid one."
                )
        return

    # handle chat messages in the "chat" channel, again, change the first if statement if you wanna use a different channel
    if channel == "chat":
        formatted_message = f"{username} says: {user_message}"
        try:
            ai_response = await ai_client.chat.send_message(
                character_id, ai_chat.chat_id, formatted_message
            )
            response_text = ai_response.get_primary_candidate().text
            await message.channel.send(response_text)
            # handles ai crashing/going down so everything doesn't get absolutely kablabberfucked...
        except SessionClosedError:
            print("ai session closed. restarting session...")
            await setup_ai_client()
            await message.channel.send("Oops, something went wrong. Try again! If the problem persists, DM @bugsync with the logs!")
            


client.run(discord_token)
