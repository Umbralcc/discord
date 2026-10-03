import asyncio
import logging
import os
from pathlib import Path

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("bot")


class Bot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.members = True  # para el mensaje de bienvenida
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self) -> None:
        # Carga automáticamente todos los archivos de la carpeta cogs/
        for file in sorted(Path(__file__).parent.joinpath("cogs").glob("*.py")):
            if not file.name.startswith("_"):
                await self.load_extension(f"cogs.{file.stem}")
                log.info("Cargado: cogs.%s", file.stem)

        # Sincroniza los slash commands. Con GUILD_ID aparecen al instante en ese servidor;
        # sin él se registran globalmente (puede tardar hasta 1 hora).
        if GUILD_ID:
            guild = discord.Object(id=int(GUILD_ID))
            self.tree.copy_global_to(guild=guild)
            synced = await self.tree.sync(guild=guild)
        else:
            synced = await self.tree.sync()
        log.info("Sincronizados %d slash commands", len(synced))

    async def on_ready(self) -> None:
        log.info("Conectado como %s (ID: %s)", self.user, self.user.id)
        await self.change_presence(activity=discord.Game(name="/ayuda"))


async def main() -> None:
    if not TOKEN:
        raise SystemExit("Falta DISCORD_TOKEN. Copia .env.example a .env y pon tu token.")
    async with Bot() as bot:
        await bot.start(TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
