import configparser
import os

config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")

discord_grp = "DISCORD"
token_key = "Token"
prefix_key = "CommandPrefix"
discord_mentionrole = "mentionrole"

sheets_grp = "SHEETS"
sheets_id = "id"
sheets_worksheet = "worksheet"
six_mans_grp = "SIX_MANS"
use_captains_key = "UseCaptains"


class Config:
    def __init__(self):
        self.config = configparser.RawConfigParser()
        self.read_config()

    def read_config(self):
        if os.path.isfile(config_file):
            self.config.read(config_file)
            return

        self.create_config()

    def create_config(self):
        self.config[discord_grp] = {}
        self.config[discord_grp][token_key] = ""
        self.config[discord_grp][prefix_key] = ">"

        with open(config_file, "w") as f:
            self.config.write(f)

    @property
    def discord_token(self):
        return self.config[discord_grp][token_key]

    @property
    def discord_mentionrole(self):
        return self.config[discord_grp][discord_mentionrole]

    @property
    def discord_prefix(self):
        return self.config[discord_grp][prefix_key]
    
    @property
    def sheets_id(self):
        return self.config[sheets_grp][sheets_id]

    @property
    def sheets_worksheet(self):
        return self.config[sheets_grp][sheets_worksheet]
    