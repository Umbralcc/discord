# Bot de Discord

Bot en Python con [discord.py](https://discordpy.readthedocs.io/) y slash commands.

## Comandos

| Comando | Qué hace |
|---|---|
| `/ping` | Latencia del bot |
| `/hola` | Te saluda |
| `/dado [caras]` | Tira un dado |
| `/usuario [miembro]` | Info de un usuario |
| `/ayuda` | Lista de comandos |

También da la bienvenida a los miembros nuevos en el canal del sistema del servidor.

## Puesta en marcha

1. **Crea la aplicación** en el [Discord Developer Portal](https://discord.com/developers/applications) → *New Application*.
2. En **Bot**: pulsa *Reset Token* y copia el token. Activa **Server Members Intent**.
3. En **OAuth2 → URL Generator**: marca `bot` y `applications.commands`, y en permisos `Send Messages` y `Embed Links`. Abre la URL generada para invitar el bot a tu servidor.
4. Instala y configura:

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env           # y pon tu DISCORD_TOKEN
   ```

   Opcional: pon `GUILD_ID` (clic derecho en tu servidor → *Copiar ID*, con el modo desarrollador activado) para que los comandos aparezcan al instante.

5. Arranca:

   ```bash
   python bot.py
   ```

## Añadir comandos

Crea un archivo nuevo en `cogs/` siguiendo el modelo de `cogs/general.py`; se carga solo al iniciar.

> ⚠️ Nunca subas tu `.env` ni compartas el token. Si se filtra, regénéralo en el portal.
