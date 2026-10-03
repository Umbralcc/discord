import random

import discord
from discord import app_commands
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="ping", description="Muestra la latencia del bot")
    async def ping(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f"🏓 Pong! {round(self.bot.latency * 1000)} ms")

    @app_commands.command(name="hola", description="El bot te saluda")
    async def hola(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f"¡Hola, {interaction.user.mention}! 👋")

    @app_commands.command(name="dado", description="Tira un dado")
    @app_commands.describe(caras="Número de caras (por defecto 6)")
    async def dado(self, interaction: discord.Interaction, caras: app_commands.Range[int, 2, 1000] = 6) -> None:
        await interaction.response.send_message(f"🎲 Sacaste un **{random.randint(1, caras)}** (d{caras})")

    @app_commands.command(name="usuario", description="Muestra información de un usuario")
    @app_commands.describe(miembro="El usuario (por defecto, tú)")
    async def usuario(self, interaction: discord.Interaction, miembro: discord.Member | None = None) -> None:
        miembro = miembro or interaction.user
        embed = discord.Embed(title=str(miembro), color=miembro.color)
        embed.set_thumbnail(url=miembro.display_avatar.url)
        embed.add_field(name="ID", value=miembro.id)
        embed.add_field(name="Cuenta creada", value=discord.utils.format_dt(miembro.created_at, "D"))
        if isinstance(miembro, discord.Member) and miembro.joined_at:
            embed.add_field(name="Se unió", value=discord.utils.format_dt(miembro.joined_at, "D"))
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="ayuda", description="Lista los comandos disponibles")
    async def ayuda(self, interaction: discord.Interaction) -> None:
        lineas = [f"`/{c.name}` — {c.description}" for c in self.bot.tree.get_commands()]
        embed = discord.Embed(title="Comandos", description="\n".join(lineas), color=discord.Color.blurple())
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member) -> None:
        if member.guild.system_channel:
            await member.guild.system_channel.send(f"¡Bienvenido/a {member.mention} a **{member.guild.name}**! 🎉")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(General(bot))
