import os
from typing import Final

from discord import Intents, Client, Message
from dotenv import load_dotenv

from responses import get_responses

# load token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# set up bot
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


# message functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("(Message was empty because intents were not enabled probably)")
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_responses(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# handling startup
@client.event
async def on_ready() -> None:
    print(f'{client.user} has connected to Discord!')


# handling incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}]  {username}: "{user_message}"')
    await send_message(message, user_message)


# main entry point
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
