import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def addRecord(List):

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('RL Uni scrims-0b71f7800558.json', scope) # get email and key from creds
    file = gspread.authorize(credentials) # authenticate with Google
    sheet = file.open("Scrims results").worksheet("Game results") # open sheet
    sheet.append_row(List)

def abc():
    print("Hi")
