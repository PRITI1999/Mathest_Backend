import random

class AdditionCategory1:
    
    instance_no_list = []
    answer_calculated = 1
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated = 1
        for i in range(0, len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
    
    def generate_answer(cls):
        for i in range(0, len(cls.instance_no_list)):
            cls.answer_calculated = cls.answer_calculated * cls.instance_no_list[i]
        return cls.answer_calculated
    
    def generate_question(cls, no_of_numbers):
        question_generated = []
        for i in range(0, no_of_numbers):
            question_generated.append(random.randint(1, 9))
        return question_generated

list1 = [1, 2, 3]
ac1 = AdditionCategory1(list1)
print(ac1.generate_answer())
print(ac1.generate_question(len(list1)))
