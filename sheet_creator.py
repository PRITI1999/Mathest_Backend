import gspread
from oauth2client.service_account import ServiceAccountCredentials 

class SheetCreator:
    scope =  ""
    creds = ""
    gc = ""
    uid = ""

    def __init__(self, user_uid):
        self.scope =  ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('mathest.json', self.scope)
        self.gc = gspread.authorize(self.creds) 
        self.uid = user_uid
        self.create_sheet()

    def create_sheet(cls):
        print(cls.uid)
        original_sheet = cls.gc.open('Main_Sheet')
        sheet_title = 'MSU' + str(cls.uid)
        new_sheet = cls.gc.copy(file_id = original_sheet.id, title = sheet_title, copy_permissions = True)
        new_sheet.share('cse.mobilecomputingforum@gmail.com', perm_type = 'user', role = 'writer')
        #new_sheet = cls.gc.open(sheet_title)
