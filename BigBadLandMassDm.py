import os
import discord
import asyncio
from pystyle import Colors, Colorate
from datetime import datetime

os.system('cls' if os.name == 'nt' else 'clear')
async def massdm(token, target, message):
    messagec = 500
    try:
        intents = discord.Intents.default()
        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            game = discord.Game("PAG-IBIG")
            await client.change_presence(status=discord.Status.dnd, activity=game)
            
            try:
                target_user = await client.fetch_user(int(target))

                for i in range(messagec):
                    try:
                        await target_user.send(message)
                        time = Colorate.Horizontal(Colors.rainbow, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        print(f"[{time}] Message successfully sent to {target_user.name}")
                    except discord.Forbidden:
                        time = Colorate.Horizontal(Colors.rainbow, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        print(f"[{time}] Failed to send message. The user may have disabled direct messages or blocked the bot")
                        break
                    except Exception as error:
                        time = Colorate.Horizontal(Colors.rainbow, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        print(f"[{time}] Error man : {error}")
                        break
            finally:
                await client.close()
        await client.start(token)
    except Exception as error:
        time = Colorate.Horizontal(Colors.rainbow, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print(f"[{time}] Error man : {error}")

async def main():
    try:
        with open('tokens.txt', 'r') as file:
            tokens = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        time = Colorate.Horizontal(Colors.rainbow, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print(f"[{time}] tokens.txt not found")
        return
    
    print("""
                __       __                      _______                       __  __  __            __       
               |  \     /  \                    |       \                     |  \|  \|  \          |  \      
               | $$\   /  $$  ______   _______  | $$$$$$$\  ______  __     __  \$$| $$ \$$  _______ | $$____  
               | $$$\ /  $$$ /      \ |       \ | $$  | $$ /      \|  \   /  \|  \| $$|  \ /       \| $$    \ 
               | $$$$\  $$$$|  $$$$$$\| $$$$$$$\| $$  | $$|  $$$$$$\\$$\ /  $$| $$| $$| $$|  $$$$$$$| $$$$$$$\
                           | $$\$$ $$ $$| $$  | $$| $$  | $$| $$  | $$| $$    $$ \$$\  $$ | $$| $$| $$ \$$    \ | $$  | $$
               | $$ \$$$| $$| $$__/ $$| $$  | $$| $$__/ $$| $$$$$$$$  \$$ $$  | $$| $$| $$ _\$$$$$$\| $$  | $$
               | $$  \$ | $$ \$$    $$| $$  | $$| $$    $$ \$$     \   \$$$   | $$| $$| $$|       $$| $$  | $$
                \$$      \$$  \$$$$$$  \$$   \$$ \$$$$$$$   \$$$$$$$    \$     \$$ \$$ \$$ \$$$$$$$  \$$   \$$

                                discord.gg/revshit | discord.gg/xtazy |discord.gg/ransomx
""")
    while True:
        target = input(f"Discord User ID (or type 'exit' to quit): ")
        if target.lower() == 'exit':
            break
        message = input(f"Message (or type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        tasks = [massdm(token, target, message) for token in tokens]

        try:
            await asyncio.gather(*tasks)
        except KeyboardInterrupt:
            time = Colorate.Horizontal(Colors.rainbow, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            print(f"[{time}] Stopped")
            break

if __name__ == "__main__":
    asyncio.run(main())
