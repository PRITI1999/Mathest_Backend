import random

class AdditionCategory3:
    
    instance_no_list = []
    answer_calculated = 0
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated = 0
        for i in range(0, len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
    
    def is_category_condition_satisfied(cls):
        for i in range(len(cls.instance_no_list)):
            s = set(str(cls.instance_no_list[i]))
            if('6' in s or '9' in s):
                return True
        return False
    
    def generate_answer(cls):
        temp_list = list(cls.instance_no_list)
        for i in range(0, len(temp_list)):
            num =  str(temp_list[i])
            for i in range(len(num)):
                if(num[i] == '6'):
                    num  = num[:i] + '9' + num[i+1:]
                elif(num[i] == '9'):
                    num  = num[:i] + '6' + num[i+1:]
            cls.answer_calculated = cls.answer_calculated + int(num)
        cls.answer_calculated = str(cls.answer_calculated)
        for i in range(len(cls.answer_calculated)):
            if(cls.answer_calculated[i] == '6'):
                cls.answer_calculated = cls.answer_calculated[:i] + '9' + cls.answer_calculated[i+1:]
            elif(cls.answer_calculated[i] == '9'):
                cls.answer_calculated  = cls.answer_calculated[:i] + '6' + cls.answer_calculated[i+1:]
        cls.answer_calculated = int(cls.answer_calculated)
        return cls.answer_calculated
    
    def generate_question(cls, no_of_numbers):
        question_generated = []
        no_of_digits = random.randint(1, 3)
        if(no_of_digits == 1):
            num1 = 6
            num2 = 9
        elif(no_of_digits == 2):
            num1 = 60 + random.randint(1, 9)
            num2 = 90 + random.randint(1, 9)
        else:
            num1 = 600 + random.randint(1, 99)
            num2 = 900 + random.randint(1, 99)
        
        question_generated.append(num1)
        question_generated.append(num2)
        
        if(no_of_numbers > 2):
            number_left_to_generate = no_of_numbers - 2 
            for i in range(0, number_left_to_generate):
                question_generated.append(random.randint(1, 999))
        return random.sample(question_generated, len(question_generated))

list1 = [16, 45, 5]
ac1 = AdditionCategory3(list1)
print(ac1.is_category_condition_satisfied())
print(ac1.generate_answer())
print(ac1.generate_question(len(list1)))





