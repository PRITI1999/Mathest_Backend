import random

class MultiplicationCategory1:
    instance_no_list = []
    answer_calculated_list = []
    product = 1
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated_list = []
        for i in range(len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
    
    def is_category_condition_satisfied(cls):
        cls.product = 1
        for i in range(len(cls.instance_no_list)):
            cls.product = cls.product * cls.instance_no_list[i]
        if(cls.product % 10 == 0):
            return True
        else:
            return False
        
    def generate_answer(cls):
        while cls.product % 10 == 0:
            cls.answer_calculated_list.append(cls.product//10)
            cls.product = cls.product // 10
        return cls.answer_calculated_list
        
    def generate_question(cls, no_of_numbers):
        question_generated = []
        num = 10 * random.randint(1, 99)
        question_generated.append(num)
        for i in range(no_of_numbers - 1):
            num1 = random.randint(1, 99)
            question_generated.append(num1)
        return question_generated
        

list1 = [85, 100]
mc1 = MultiplicationCategory1(list1)
print(mc1.is_category_condition_satisfied())
print(mc1.generate_answer())
print(mc1.generate_question(len(list1)))
        