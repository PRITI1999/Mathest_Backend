import random

class DivisionCategory1:
    instance_no_list = []
    answer_calculated = 0
    
    def __init__(self, original_number_list):
        self.answer_calculated = 0
        self.instance_no_list = []
        for i in range(len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])

    def generate_answer(cls):
        #need to be modified for more than two numbers
        for i in range(len(cls.instance_no_list) - 1):
            cls.answer_calculated = cls.instance_no_list[i] * cls.instance_no_list[i+1]
        return cls.answer_calculated
    
    def generate_question(cls):
        question_generated =[]
        num1 = -1
        num2 = -2
        while(num1 % num2 != 0 or num1 == num2):
            num1 = random.randint(2, 999)
            num2 = random.randint(2, 99)
        question_generated.append(num1)
        question_generated.append(num2)  
        return question_generated
        
"""list1 = [100, 4]
dc1 = DivisionCategory1(list1)
print(dc1.generate_answer())
print(dc1.generate_question())"""

class DivisionCategory2:
    instance_no_list = []
    answer_calculated = 0
    
    def __init__(self, original_number_list):
        self.answer_calculated = 0
        self.instance_no_list = []
        for i in range(len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])

    def generate_answer(cls):
        #need to be modified for more than two numbers
        for i in range(len(cls.instance_no_list) - 1):
            cls.answer_calculated = cls.instance_no_list[i] // cls.instance_no_list[i+1]
        reverse_answer = (str(cls.answer_calculated))[::-1]
        return int(reverse_answer)
    
    def generate_question(cls):
        question_generated =[]
        num1 = -1
        num2 = -2
        while(num1 % num2 != 0 or num1 == num2):
            num1 = random.randint(2, 999)
            num2 = random.randint(2, 99)
        question_generated.append(num1)
        question_generated.append(num2)  
        return question_generated
        
"""list1 = [100, 4]
dc2 = DivisionCategory2(list1)
print(dc2.generate_answer())
print(dc2.generate_question())"""

class DivisionCategory3:
    instance_no_list = []
    answer_calculated = 0
    divide_answer = 0
    
    def __init__(self, original_number_list):
        self.answer_calculated = 0
        self.instance_no_list = []
        for i in range(len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
            
    def is_category_condition_satisfied(cls):
        for i in range(len(cls.instance_no_list) - 1):
            cls.divide_answer = cls.instance_no_list[i] // cls.instance_no_list[i+1]
        if ('0' in str(cls.divide_answer)):
            return True
        else:
            return False

    def generate_answer(cls):
        #need to be modified for more than two numbers
        cls.answer_calculated = int((str(cls.divide_answer).replace('0', '')))
        return cls.answer_calculated
    
    def generate_question(cls):
        question_generated =[]
        num1 = -1
        num2 = -2
        while(num1 % num2 != 0 or not('0' in str(num1 // num2)) or num1 == num2):
            num1 = random.randint(2, 9999)
            num2 = random.randint(2, 99)
        question_generated.append(num1)
        question_generated.append(num2)  
        return question_generated
        
"""list1 = [2718, 3]
dc3 = DivisionCategory3(list1)
print(dc3.is_category_condition_satisfied())
print(dc3.generate_answer())
print(dc3.generate_question())"""
