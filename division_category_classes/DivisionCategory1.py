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
        
list1 = [100, 4]
dc1 = DivisionCategory1(list1)
print(dc1.generate_answer())
print(dc1.generate_question())