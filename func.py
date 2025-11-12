import manager
import json 
from random import randint as rint, choice as rchoice, shuffle as rshuffle
from kivy.clock import Clock


class FactReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.fact_data = None
    
    def load_json(self):
        res = manager.ResourceManager()
        path = res.path(self.file_path)
        with open(path, "r", encoding="utf-8") as f:
            self.fact_data = json.load(f)
    
    def get_random_fact(self):
        try:
            if self.fact_data is None:
                self.load_json()
            
            ## Access the facts array from the JSON structure
            facts_list = self.fact_data["math_history_facts"]
            
            ## Get a random fact object
            random_fact_obj = rchoice(facts_list)
            
            ## Return just the fact text
            return random_fact_obj["fact"]
            
        except (FileNotFoundError, KeyError) as e:
            print(f"Error: {e}")
            return "Fact not available"

class AdditionSubtraction: ## Very easy diff
    def __init__(self):
        pass

    def generateQuestion(self):
        operation_chioce = rchoice(['+', '-'])
        a = rint(1,40)
        b = rint(1,40)
        if operation_chioce == '+':
            result = a + b
        else:
            if a < b:
                a, b = b, a
            result = a - b
        answers = {result}
        while len(answers) < 4:
            fake = result + rint(-10, 10)
            if fake >= 0:
                answers.add(fake)
        answer_list = list(answers)
        rshuffle(answer_list)
        ## Return 3 values: equation string, shuffled answers, correct answer
        return f"{a}{operation_chioce}{b} = ", answer_list, result

class AdditionSubtractionWithBrackets: ## Easy diff
    def __init__(self):
        pass

    def generateQuestion(self):
        # Generate three numbers in range 1-40
        a, b, c = [rint(1, 40) for _ in range(3)]

        form = rchoice([0, 1])


        if form == 0:
            # a ± (b ± c)
            op1 = rchoice(["+", "-"])
            op2 = rchoice(["+", "-"])
            equation = f"{a}{op1}({b}{op2}{c})"
            result = eval(equation)
        else:
            # (a ± b) ± c
            op1 = rchoice(["+", "-"])
            op2 = rchoice(["+", "-"])
            equation = f"({a}{op1}{b}){op2}{c}"
            result = eval(equation)


        # Ensure non-negative result
        if result < 0:
            return self.generateQuestion()


        # Generate answers set including the correct one
        answers = {result}
        while len(answers) < 4:
            fake = result + rint(-10, 10)
            if fake >= 0:
                answers.add(fake)
        answer_list = list(answers)
        rshuffle(answer_list)

        return f"{equation} = ", answer_list, result

class AdditionSubtractionMultiplication: ## Normal diff
    def __init__(self):
        pass
    
    def generateQuestion(self):
        operation_choice = rchoice(['+', '-', '×'])
        
        # Random values for addition/subtraction
        a = rint(1, 40)
        b = rint(1, 40)

        # Random values for multiplication
        aMult = rint(1, 10)
        bMult = rint(1, 10)
        
        if operation_choice == '+':
            result = a + b
            equation = f"{a} + {b} = "
        elif operation_choice == '-':
            if a < b:
                a, b = b, a
            result = a - b
            equation = f"{a} - {b} = "
        elif operation_choice == '×':
            result = aMult * bMult
            equation = f"{aMult} × {bMult} = "
        
        # Build unique answer set with correct result
        answers = {result}
        while len(answers) < 4:
            fake = result + rint(-10, 10)
            if fake >= 0:
                answers.add(fake)
        
        answer_list = list(answers)
        rshuffle(answer_list)
        
        ## Return 3 values: equation string, shuffled answers, correct answer
        return equation, answer_list, result

class AdditionSubtractionMultiplicationDivision: ## Hard diff
    def __init__(self):
        pass

    def generateQuestion(self):
        operation_choice = rchoice(['+', '-', '×', '÷'])

        # Random values for addition/subtraction
        a = rint(1, 40)
        b = rint(1, 40)

        # Random values for multiplication
        aMult = rint(1, 10)
        bMult = rint(1, 10)

        # Random values for division
        aDiv = rint(2, 10)
        bDiv = rint(1, 10)  # divisor, not zero

        if operation_choice == '+':
            result = a + b
            equation = f"{a} + {b} = "
        elif operation_choice == '-':
            if a < b:
                a, b = b, a
            result = a - b
            equation = f"{a} - {b} = "
        elif operation_choice == '×':
            result = aMult * bMult
            equation = f"{aMult} × {bMult} = "
        elif operation_choice == '÷':
            # Make division exact
            dividend = aDiv * bDiv
            result = dividend // bDiv
            equation = f"{dividend} ÷ {bDiv} = "

        # Generate 3 fake answers in addition to the correct one
        answers = {result}
        while len(answers) < 4:
            fake = result + rint(-10, 10)
            if fake >= 0:
                answers.add(fake)

        answer_list = list(answers)
        rshuffle(answer_list)

        return equation, answer_list, result

class ChallangeEquations:
    def __init__(self):
        self.time_remaining = 300 
        self.timer_event = None


    def start_timer(self):
        """Starts the countdown timer if not already running."""
        if not self.timer_event:
            self.timer_event = Clock.schedule_interval(self._update_timer, 1)

    def _update_timer(self, dt):
        """Internal callback to decrease time each second."""
        self.time_remaining -= 1
        print(f"Time Left: {self.time_remaining}s")

        if self.time_remaining <= 0:
            print("Time's up!")
            self.stop_timer()

    def penalize_time(self):
        self.time_remaining = max(0, self.time_remaining - 10)
        print(f"Incorrect! -10s penalty. Time Left: {self.time_remaining}s")

    def stop_timer(self):
        if self.timer_event:
            self.timer_event.cancel()
            self.timer_event = None



    def generateQuestion(self):
        mode = rint(1, 4)
        if mode == 1:
            return self._add_sub()
        elif mode == 2:
            return self._add_sub_brackets()
        elif mode == 3:
            return self._add_sub_mult()
        elif mode == 4:
            return self._add_sub_mult_div()

    def _generate_answers(self, correct_result):
        answers = {correct_result}
        while len(answers) < 4:
            fake = correct_result + rint(-10, 10)
            if fake >= 0 and fake not in answers:  # ensure unique + non-negative
                answers.add(fake)
        answer_list = list(answers)
        rshuffle(answer_list)
        return answer_list

    def _add_sub(self):
        a, b = rint(1, 100), rint(1, 100)
        op = rchoice(['+', '-'])
        if op == '-':
            if a < b:
                a, b = b, a
            result = a - b
        else:
            result = a + b
        equation = f"{a} {op} {b} = "
        answers = self._generate_answers(result)
        return equation, answers, result

    def _add_sub_brackets(self):
        a, b, c = [rint(1, 50) for _ in range(3)]
        form = rchoice([0, 1])
        op1, op2 = rchoice(['+', '-']), rchoice(['+', '-'])

        if form == 0:
            equation = f"{a} {op1} ({b} {op2} {c})"
        else:
            equation = f"({a} {op1} {b}) {op2} {c}"

        result = eval(equation)
        if result < 0:
            return self._add_sub_brackets()

        answers = self._generate_answers(result)
        return equation + " = ", answers, result

    def _add_sub_mult(self):
        operation = rchoice(['+', '-', '×'])
        a, b = rint(1, 40), rint(1, 40)
        a_mult, b_mult = rint(1, 12), rint(1, 12)

        if operation == '+':
            result = a + b
            equation = f"{a} + {b} = "
        elif operation == '-':
            if a < b:
                a, b = b, a
            result = a - b
            equation = f"{a} - {b} = "
        else:
            result = a_mult * b_mult
            equation = f"{a_mult} × {b_mult} = "

        answers = self._generate_answers(result)
        return equation, answers, result

    def _add_sub_mult_div(self):
        operation = rchoice(['+', '-', '×', '÷'])
        a, b = rint(1, 40), rint(1, 40)
        a_mult, b_mult = rint(1, 12), rint(1, 12)
        a_div, b_div = rint(1, 12), rint(1, 12)

        if operation == '+':
            result = a + b
            equation = f"{a} + {b} = "
        elif operation == '-':
            if a < b:
                a, b = b, a
            result = a - b
            equation = f"{a} - {b} = "
        elif operation == '×':
            result = a_mult * b_mult
            equation = f"{a_mult} × {b_mult} = "
        else:
            dividend = a_div * b_div
            result = dividend // b_div
            equation = f"{dividend} ÷ {b_div} = "

        answers = self._generate_answers(result)
        return equation, answers, result

