import random

class AdditionCategory2:
    
    instance_no_list = []
    answer_calculated_list = []
    
    def __init__(self, original_number_list):
        self.instance_no_list = []
        self.answer_calculated_list = []
        for i in range(0, len(original_number_list)):
            self.instance_no_list.append(original_number_list[i])
    
    def is_category_condition_satisfied(cls):
        temp_list = list(cls.instance_no_list)
        while(all(v != 0 for v in temp_list)):
            sum_of_digits = 0
            for i in range(0, len(temp_list)):
                sum_of_digits = sum_of_digits + (temp_list[i] % 10)
                temp_list[i] = temp_list[i] // 10
            if(sum_of_digits > 9):
                return True
        return False
    
    def generate_answer_utility(cls, carry, temp_list, answer_string):
        if(all(v == 0 for v in temp_list)):
            if(carry > 0):
                answer_string = str(carry) + answer_string
            cls.answer_calculated_list.append(int(answer_string))
            answer_string = ''
            return
        sum_of_digits = carry
        for i in range(0, len(temp_list)):
            sum_of_digits = sum_of_digits + (temp_list[i] % 10)
            temp_list[i] = temp_list[i] // 10
        answer_string = str(sum_of_digits % 10) + answer_string
        temp_list_copy = list(temp_list)
        if(sum_of_digits > 9):
            cls.generate_answer_utility(sum_of_digits // 10, temp_list, answer_string)
        cls.generate_answer_utility(0, temp_list_copy, answer_string)
    
    def generate_answer(cls):
        cls.answer_calculated_list = []
        temp_list = list(cls.instance_no_list)
        cls.generate_answer_utility(0, temp_list, '')
        return cls.answer_calculated_list
    
    def generate_question(cls, no_of_numbers):
        
        question_generated = []
        no_of_digits = random.randint(1, 3)
        
        if(no_of_digits == 1):
            num1 = random.randint(5, 9)
            num2 = random.randint(5, 9)
        elif(no_of_digits == 2):
            digit_randomized = random.randint(1, 3)
            if(digit_randomized == 1):
                num1 = random.randint(5, 9) + random.randint(1, 9) * 10;
                num2 = random.randint(5, 9) + random.randint(1, 9) * 10;
            else:
                num1 = random.randint(1, 9) + random.randint(5, 9) * 10;
                num2 = random.randint(1, 9) + random.randint(5, 9) * 10;
        else:
            digit_randomized = random.randint(1, 4)
            if(digit_randomized == 1):
                num1 = random.randint(5, 9) + random.randint(1, 9) * 10 + random.randint(1, 9) * 100;
                num2 = random.randint(5, 9) + random.randint(1, 9) * 10 + random.randint(1, 9) * 100;
            elif(digit_randomized == 2):
                num1 = random.randint(1, 9) + random.randint(5, 9) * 10 + random.randint(1, 9) * 100;
                num2 = random.randint(1, 9) + random.randint(5, 9) * 10 + random.randint(1, 9) * 100;
            else:
                num1 = random.randint(1, 9) + random.randint(1, 9) * 10 + random.randint(5, 9) * 100;
                num2 = random.randint(1, 9) + random.randint(1, 9) * 10 + random.randint(5, 9) * 100;
        
        question_generated.append(num1)
        question_generated.append(num2)
        
        if(no_of_numbers > 2):
            number_left_to_generate = no_of_numbers - 2 
            for i in range(0, number_left_to_generate):
                question_generated.append(random.randint(1, 999))      
        return random.sample(question_generated, len(question_generated))

list1 = [99, 99, 99]
ac1 = AdditionCategory2(list1)
print(ac1.is_category_condition_satisfied())
print(ac1.generate_answer())
print(ac1.generate_question(len(list1)))