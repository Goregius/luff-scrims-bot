import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config.config import Config


config = Config()
if not config.sheets_id:
    print("Please set a sheets id in config.ini")
if not config.sheets_worksheet:
    print("Please set a sheets worksheet in config.ini")

def addRecord(List):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope) # get email and key from creds
    file = gspread.authorize(credentials) # authenticate with Google
    sheet = file.open_by_key(config.sheets_id).worksheet(config.sheets_worksheet) # open sheet
    sheet.append_row(List)
