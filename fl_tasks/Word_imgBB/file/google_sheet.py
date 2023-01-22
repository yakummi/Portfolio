from googleapiclient.discovery import build
from google.oauth2 import service_account
from config_gs import SAMPLE_SPREADSHEET_ID, NAME_SHEET

class GoogleSheet:

    def read_file(self):

        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = 'keys.json'

        creds = None
        creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )


        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=f"""{NAME_SHEET}!A1:E1000000""").execute()

        values = result.get('values', [])

        return len(values)

    # aoa = [["1/1/2020", 4000], ["3/1/2020", 200], ["1/2/2020", 12]]

    # request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="sales!A9",
    #                             valueInputOption="USER_ENTERED", body={"values": aoa}).execute()



    # print(request) # сколько записей len

    def write_file(self, data, sheet_number):
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = 'keys.json'

        creds = None
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )

        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()

        request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=f"{NAME_SHEET}!{'A'+str(sheet_number)}",
                                    valueInputOption="USER_ENTERED", body={"values": data}).execute()


        print(request)

gs = GoogleSheet()