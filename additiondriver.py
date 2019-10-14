import gspread
import pprint
from oauth2client.service_account import ServiceAccountCredentials
import random
from additioncategories import AdditionCategory1
from additioncategories import AdditionCategory2
from additioncategories import AdditionCategory3
from additioncategories import AdditionCategory4
from additioncategories import AdditionCategory5
from additioncategories import AdditionCategory6
from additioncategories import AdditionCategory7
from additioncategories import AdditionCategory8      

class AdditionErrorClassifier:
    
    sheet_name = ""
    row_number = -1
    number_of_questions_generated = -1
    number_of_numbers_in_each_question = -1
    
    def __init__(self, name, row):
        
        self.sheet_name = name
        self.row_number = row
        self.number_of_questions_generated = 3
        self.number_of_numbers_in_each_question = 2

    def classify(cls):
        
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('mathest.json', scope)
        client = gspread.authorize(creds)
        sheet = client.open(cls.sheet_name).sheet1
        
        pp = pprint.PrettyPrinter()
        
        number1 = int(sheet.cell(cls.row_number, 1).value)
        number2 = int(sheet.cell(cls.row_number, 2).value)
        
        answer_by_user = int(sheet.cell(cls.row_number, 3).value)
        
        pp.pprint(number1)
        pp.pprint(number2)
        pp.pprint(answer_by_user)
        
        category_found = False
        original_list = []
        original_list.append(number1)
        original_list.append(number2)
        
        if category_found == False:
            ac1 = AdditionCategory1(original_list)
            if ac1.generate_answer() == answer_by_user:
                category_found = True
                sheet.update_cell(cls.row_number, 4, "1")
                for i in range(cls.number_of_questions_generated):
                    question_generated = ac1.generate_question(cls.number_of_numbers_in_each_question)
                    sheet.append_row(question_generated)
                    print("Generating 3 a questions macha")
        
        if category_found == False:
            ac2 = AdditionCategory2(original_list)
            if ac2.is_category_condition_satisfied() == True:
                answers = ac2.generate_answer()
                for i in range(len(answers)):
                    if answers[i] == answer_by_user:
                        category_found = True
                if category_found == True:
                    sheet.update_cell(cls.row_number, 4, "2")
                    for i in range(cls.number_of_questions_generated):
                        question_generated = ac2.generate_question(cls.number_of_numbers_in_each_question)
                        sheet.append_row(question_generated)
                        print("Generating 3 b questions macha")
        
        if category_found == False:
            ac3 = AdditionCategory3(original_list)
            if ac3.is_category_condition_satisfied() == True and ac3.generate_answer() == answer_by_user:
                category_found = True
                sheet.update_cell(cls.row_number, 4, "3")
                for i in range(cls.number_of_questions_generated):
                    question_generated = ac3.generate_question(cls.number_of_numbers_in_each_question)
                    sheet.append_row(question_generated)
                    print("Generating 3 c questions macha")
        
        if category_found == False:
            ac4 = AdditionCategory4(original_list)
            if ac4.is_category_condition_satisfied() == True and ac4.generate_answer() == answer_by_user:
                category_found = True
                sheet.update_cell(cls.row_number, 4, "4")
                for i in range(cls.number_of_questions_generated):
                    question_generated = ac4.generate_question(cls.number_of_numbers_in_each_question)
                    sheet.append_row(question_generated)
                    print("Generating 3 d questions macha")
        
        if category_found == False:
            ac5 = AdditionCategory5(original_list)
            if ac5.is_category_condition_satisfied() == True and ac5.generate_answer() == answer_by_user:
                category_found = True
                sheet.update_cell(cls.row_number, 4, "5")
                for i in range(cls.number_of_questions_generated):
                    question_generated = ac5.generate_question(cls.number_of_numbers_in_each_question)
                    sheet.append_row(question_generated)
                    print("Generating 3 e questions macha")
        
        if category_found == False:
            ac6 = AdditionCategory6(original_list)
            if ac6.is_category_condition_satisfied() == True and ac6.generate_answer() == answer_by_user:
                category_found = True
                sheet.update_cell(cls.row_number, 4, "6")
                for i in range(cls.number_of_questions_generated):
                    question_generated = ac6.generate_question(cls.number_of_numbers_in_each_question)
                    sheet.append_row(question_generated)
                    print("Generating 3 f questions macha")
        
        if category_found == False:
            ac7 = AdditionCategory7(original_list)
            if ac7.is_category_condition_satisfied() == True and ac7.generate_answer() == answer_by_user:
                category_found = True
                sheet.update_cell(cls.row_number, 4, "7")
                for i in range(cls.number_of_questions_generated):
                    question_generated = ac7.generate_question(cls.number_of_numbers_in_each_question)
                    sheet.append_row(question_generated)
                    print("Generating 3 g questions macha")
        
        if category_found == False:            
            ac8 = AdditionCategory8(original_list)
            if ac8.is_category_condition_satisfied() == True and ac8.generate_answer() == answer_by_user:
                category_found = True
                sheet.update_cell(cls.row_number, 4, "8")
                for i in range(cls.number_of_questions_generated):
                    question_generated = ac8.generate_question(cls.number_of_numbers_in_each_question)
                    sheet.append_row(question_generated)
                    print("Generating 3 h questions macha")
                    
        if category_found == False:
            random_questions = []
            category_found = True
            sheet.update_cell(cls.row_number, 4, "X")
            for i in range(cls.number_of_questions_generated):
                random_questions.append(random.randint(1, 8))
            for i in range(cls.number_of_questions_generated):
                if random_questions[i] == 1:
                    question_generated = ac1.generate_question(cls.number_of_numbers_in_each_question)
                    sheet.append_row(question_generated)
                    print("Generating 3 a questions macha")
                elif random_questions[i] == 2:
                    question_generated = ac2.generate_question(cls.number_of_numbers_in_each_question)
                    sheet.append_row(question_generated)    
                    print("Generating 3 b questions macha")
                elif random_questions[i] == 3:
                    question_generated = ac3.generate_question(cls.number_of_numbers_in_each_question)
                    sheet.append_row(question_generated)    
                    print("Generating 3 c questions macha")
                elif random_questions[i] == 4:
                    question_generated = ac4.generate_question(cls.number_of_numbers_in_each_question)
                    sheet.append_row(question_generated)    
                    print("Generating 3 d questions macha")
                elif random_questions[i] == 5:
                    question_generated = ac5.generate_question(cls.number_of_numbers_in_each_question)
                    sheet.append_row(question_generated)    
                    print("Generating 3 e questions macha")
                elif random_questions[i] == 6:
                    question_generated = ac6.generate_question(cls.number_of_numbers_in_each_question)
                    sheet.append_row(question_generated)    
                    print("Generating 3 f questions macha")
                elif random_questions[i] == 7:
                    question_generated = ac7.generate_question(cls.number_of_numbers_in_each_question)
                    sheet.append_row(question_generated)    
                    print("Generating 3 g questions macha")
                elif random_questions[i] == 8:
                    question_generated = ac8.generate_question(cls.number_of_numbers_in_each_question)
                    sheet.append_row(question_generated)    
                    print("Generating 3 h questions macha")
                
addition_error_classifier = AdditionErrorClassifier("test_sheet", 3)
addition_error_classifier.classify()