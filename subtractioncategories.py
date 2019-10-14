import random

class SubtractionCategory1:
    instance_no_list = []
    answer_calculated = 0
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated = 0
        for i in range(0, len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
    
    def generate_answer(cls):
        for i in range(0, len(cls.instance_no_list)):
            cls.answer_calculated = cls.answer_calculated + cls.instance_no_list[i]
        return cls.answer_calculated
    
    def generate_question(cls):
        question_generated = []
        num1 = random.randint(10, 99)
        num2 = random.randint(1, 9)
        question_generated.append(num1)
        question_generated.append(num2)
        return question_generated
        
"""list1 = [45, 7, 5]
sc1 = SubtractionCategory1(list1)
print(sc1.generate_answer())
print(sc1.generate_question())"""
