from cx_Freeze import Executable, setup

setup(
    name="Spotify Widget",
    version="1.0",
    description="Spotify Discord widget updater",
    executables=[
        Executable("Discord API.py")
    ],
)