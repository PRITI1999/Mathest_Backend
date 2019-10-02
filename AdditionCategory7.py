import random

class AdditionCategory7:
    
    instance_no_list = []
    answer_calculated = 0
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated = 0
        for i in range(0, len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
        
    def is_category_condition_satisfied(cls):
        for i in range(len(cls.instance_no_list)):
            if(cls.instance_no_list[i] % 10 == 0):
                return True
        return False
    
    def generate_answer(cls):
        temp_list = list(cls.instance_no_list)
        for i in range(len(temp_list)):
            while(temp_list[i] % 10 == 0):
                temp_list[i] = temp_list[i] // 10
            cls.answer_calculated = cls.answer_calculated + temp_list[i]
            while(cls.answer_calculated % 10 == 0):
                cls.answer_calculated = cls.answer_calculated // 10
        return cls.answer_calculated
    
    def generate_question(cls, no_of_numbers):
        question_generated = []
        num1 = random.randint(1,9) * 10
        num2 = random.randint(10,99) * 10
        question_generated.append(num1)
        question_generated.append(num2)
        if(no_of_numbers > 2):
            number_left_to_generate = no_of_numbers - 2 
            for i in range(0, number_left_to_generate):
                question_generated.append(random.randint(1, 999))
        return random.sample(question_generated, len(question_generated))

list1 = [1010, 601, 301]
ac1 = AdditionCategory7(list1)
print(ac1.is_category_condition_satisfied())
print(ac1.generate_answer())
print(ac1.generate_question(len(list1)))