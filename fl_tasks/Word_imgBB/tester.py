from googleapiclient.discovery import build
from google.oauth2 import service_account
from file.config_gs import SAMPLE_SPREADSHEET_ID, NAME_SHEET
import io
from googleapiclient.http import MediaIoBaseDownload

class GoogleDocs:

    def read_file(self):
        DOCUMENT_ID = '10-Xa5HoaI-zUX4Xb3Qq2v6oV5_YjSdYWNM7_7acem3I'

        SCOPES = ['https://www.googleapis.com/auth/drive']
        SERVICE_ACCOUNT_FILE = 'file/keys.json'

        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('drive', 'v3', credentials=credentials)

        # document = service.documents().get(documentId=DOCUMENT_ID).execute()

        # results = service.files().list(pageSize=10,
        #                                fields="nextPageToken, files(id, name, mimeType)").execute()

        request = service.files().export_media(fileId=DOCUMENT_ID,
                                               mimeType='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        filename = 'name.docx'
        fh = io.FileIO(filename, 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%." % int(status.progress() * 100))

        # sheet = service.spreadsheets()
        # result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
        #                         range=f"""{NAME_SHEET}!A1:E1000000""").execute()
        #
        # values = result.get('values', [])

        # return document
    # aoa = [["1/1/2020", 4000], ["3/1/2020", 200], ["1/2/2020", 12]]

    # request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="sales!A9",
    #                             valueInputOption="USER_ENTERED", body={"values": aoa}).execute()



    # print(request) # сколько записей len

#     def write_file(self, data, sheet_number):
#         SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
#         SERVICE_ACCOUNT_FILE = 'keys.json'
#
#         creds = None
#         creds = service_account.Credentials.from_service_account_file(
#             SERVICE_ACCOUNT_FILE, scopes=SCOPES
#         )
#
#         service = build('sheets', 'v4', credentials=creds)
#
#         sheet = service.spreadsheets()
#
#         request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=f"{NAME_SHEET}!{'A'+str(sheet_number)}",
#                                     valueInputOption="USER_ENTERED", body={"values": data}).execute()
#
#
#         print(request)
#


gs = GoogleDocs()
print(gs.read_file())