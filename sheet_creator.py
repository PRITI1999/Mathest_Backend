#author : Priti Chattopadhyay
import gspread
from oauth2client.service_account import ServiceAccountCredentials 

#class to create a sheet
#Requires uid of the user
class SheetCreator:
    scope =  ""
    creds = ""
    gc = ""

    #constructor to initialize the necessary components
    def __init__(self):
        self.scope =  ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('*******.json', self.scope)
        self.gc = gspread.authorize(self.creds) 

    #function to be called to create a sheet, return id of the sheet
    #The sheet title would be of the form MSU<UID_sent> 
    def create_sheet(cls, uid):
        print(uid)
        original_sheet = cls.gc.open('Main_Sheet')
        sheet_title = 'MSU' + str(uid)
        new_sheet = cls.gc.copy(file_id = original_sheet.id, title = sheet_title, copy_permissions = True)
        new_sheet.share('cse.mobilecomputingforum@gmail.com', perm_type = 'user', role = 'writer')
        return new_sheet.id

