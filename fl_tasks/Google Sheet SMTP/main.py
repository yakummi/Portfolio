from googleapiclient.discovery import build
from google.oauth2 import service_account
from config_gs import NAME_SHEET, SAMPLE_SPREADSHEET_ID
from config_mail import check_mail
import time

class GoogleSheet:

    def read_file(self):

        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = 'keys.json'

        creds = None
        creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=f"""{NAME_SHEET}!A1:G100000000""").execute()

        values = result.get('values', [])

        for e, value in enumerate(values):
            print(e)
            try:
                if value[4] == 'Да' and value[5] == '-':
                    new_value_data_yes = value
                    smtp_no = check_mail(new_value_data_yes[3], 'Да')
                    new_value_data_yes[5] = 'Отправлено'
                    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                    range=f"{NAME_SHEET}!{'A' + str(e+1)}",
                                                    valueInputOption="USER_ENTERED",
                                                    body={"values": [new_value_data_yes]}).execute()
                    request.update()
                    print(request)
                    time.sleep(3)


                elif value[4] == 'Нет' and value[5] == '-':
                    new_value_data_no = value
                    smtp_no = check_mail(new_value_data_no[3], 'Нет')
                    new_value_data_no[5] = 'Отправлено'
                    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                    range=f"{NAME_SHEET}!{'A' + str(e+1)}",
                                                    valueInputOption="USER_ENTERED", body={"values": [new_value_data_no]}).execute()
                    request.update()

                    print(request)
                    time.sleep(3)

                time.sleep(3)

            except Exception as ex:
                time.sleep(3)
                continue

gs = GoogleSheet()

while True:
    gs.read_file()




