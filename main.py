import PloudosAPI
import nextcord
from nextcord.ext import commands

session = PloudosAPI.login("username", "password")

servers = session.get_servers_with_name("modsgang")
server = servers[0]

bot = commands.Bot()


@bot.slash_command(description="Start de ploudos server")
async def start(interaction: nextcord.Interaction):
    await interaction.send("Server wordt gestart", ephemeral=True)
    server.start()


@bot.slash_command(description="Stopt de ploudos server")
async def stop(interaction: nextcord.Interaction):
    modsgang_server_controls_admin = "modsgang_server_controls_admin"  # Vervang dit door de naam van de rol die beheerdersrechten moet hebben.
    role = nextcord.utils.get(interaction.guild.roles, name=modsgang_server_controls_admin)
    user = interaction.user
    member = await interaction.guild.fetch_member(user.id)  # Use 'await' to correctly fetch the member from the guild.

    if member is None:
        await interaction.send("Je bent geen lid van deze server.", ephemeral=True)
        return

    if role in member.roles:
        await interaction.send("Server wordt gestopt", ephemeral=True)
        server.stop()
    else:
        await interaction.send("Je hebt niet de juiste bevoegdheden")


bot.run(token)
