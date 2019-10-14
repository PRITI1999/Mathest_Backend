import random

class AdditionCategory6:
    
    instance_no_list = []
    answer_calculated = 0
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated = 0
        for i in range(0, len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
    
    def is_category_condition_satisfied(cls):
        temp_list = list(cls.instance_no_list)
        for i in range(0, len(temp_list)):
            temp_list[i] = temp_list[i] // 10
        if(all(v != 0 for v in temp_list)):
            return True
        return False
    
    def generate_answer(cls):
        temp_list = list(cls.instance_no_list)
        for i in range(0, len(temp_list)):
            temp_list[i] = str(temp_list[i])
            temp_list[i] = temp_list[i][::-1]
            cls.answer_calculated = cls.answer_calculated + int(temp_list[i])
        cls.answer_calculated = str(cls.answer_calculated)
        cls.answer_calculated = cls.answer_calculated[::-1]
        return cls.answer_calculated
    
    def generate_question(cls, no_of_numbers):
        question_generated = []
        for i in range(0, no_of_numbers):
            question_generated.append(100 * random.randint(1, 9) + 10 * random.randint(1,9) + random.randint(1,9))
        return question_generated

list1 = [123, 72]
ac1 = AdditionCategory6(list1)
print(ac1.is_category_condition_satisfied())
print(ac1.generate_answer())
print(ac1.generate_question(len(list1)))