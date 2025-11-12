## Import Kivy and its add-ons
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.clock import Clock
## Import external modules
import func, manager


class WindowManager(ScreenManager):
    pass

class startScreen(Screen):
    reader = ObjectProperty(None)
    
    def on_pre_enter(self):
        res = manager.ResourceManager()
        self.reader = func.FactReader(res.path("json\\facts.json"))
    
    def on_enter(self):
        fact = self.reader.get_random_fact()
        self.ids.fact_label.text = fact

class levelSelectionScreen(Screen):
    pass

class levelScreenVE(Screen):
    equation_text = StringProperty("")
    option_a = StringProperty("")
    option_b = StringProperty("")
    option_c = StringProperty("")
    option_d = StringProperty("")
    correct_answer = NumericProperty(0)

    points = NumericProperty(0)
    multiplier = NumericProperty(1)
    streak = NumericProperty(0)

    is_correct = NumericProperty(0)

    def on_pre_enter(self, *args):
        self.generate_question()
    
    def generate_question(self):    
        """Generate a new equation and assign answers to buttons"""
        qgen = func.AdditionSubtraction()
        equation, answer, correct = qgen.generateQuestion()
        
        self.correct_answer = correct
        self.equation_text = equation
        self.option_a, self.option_b, self.option_c, self.option_d = map(str, answer)

    def check_answers(self, selected_text):
        if int(selected_text) == self.correct_answer:
            print("Correct")
            self.is_correct = 1
            self.streak += 1
            self.points += 10 * self.multiplier
            App.get_running_app().play_correct()
        else:
            print("Wrong!")
            self.streak = 0
            self.multiplier = 1
            self.is_correct = 0
            App.get_running_app().play_error()

        if self.streak > 0 and self.streak % 5 == 0:
            self.multiplier += 1
            print(f"Multiplier increased to x{self.multiplier}!")

        print(f"Points: {self.points}, Streak: {self.streak}")
        self.generate_question()

class levelScreenES(Screen):
    equation_text = StringProperty("")
    option_a = StringProperty("")
    option_b = StringProperty("")
    option_c = StringProperty("")
    option_d = StringProperty("")
    correct_answer = NumericProperty(0)


    points = NumericProperty(0)
    multiplier = NumericProperty(1)
    streak = NumericProperty(0)


    def on_pre_enter(self, *args):
        self.generate_question()
    def generate_question(self):
        """Generate a new equation and assign answers to buttons"""
        qgen = func.AdditionSubtractionWithBrackets()
        equation, answers, correct = qgen.generateQuestion()
        self.correct_answer = correct
        self.equation_text = equation
        self.option_a, self.option_b, self.option_c, self.option_d = map(str, answers)


    def check_answers(self, selected_text):
        if int(selected_text) == self.correct_answer:
            print("Correct")
            self.is_correct = 1
            self.streak += 1
            self.points += 10 * self.multiplier
            App.get_running_app().play_correct()   # <-- play correct
        else:
            print("Wrong!")
            self.streak = 0
            self.multiplier = 1
            self.is_correct = 0
            App.get_running_app().play_error()     # <-- play error

        if self.streak > 0 and self.streak % 5 == 0:
            self.multiplier += 1
            print(f"Multiplier increased to x{self.multiplier}!")

        print(f"Points: {self.points}, Streak: {self.streak}")
        self.generate_question()

class levelScreenNM(Screen):
    equation_text = StringProperty("")
    option_a = StringProperty("")
    option_b = StringProperty("")
    option_c = StringProperty("")
    option_d = StringProperty("")
    correct_answer = NumericProperty(0)


    points = NumericProperty(0)
    multiplier = NumericProperty(1)
    streak = NumericProperty(0)

    def on_pre_enter(self, *args):
            self.generate_question()
    def generate_question(self):
        """Generate a new equation and assign answers to buttons"""
        qgen = func.AdditionSubtractionMultiplication()
        equation, answers, correct = qgen.generateQuestion()
        self.correct_answer = correct
        self.equation_text = equation
        self.option_a, self.option_b, self.option_c, self.option_d = map(str, answers)


    def check_answers(self, selected_text):
        if int(selected_text) == self.correct_answer:
            print("Correct")
            self.is_correct = 1
            self.streak += 1
            self.points += 10 * self.multiplier
            App.get_running_app().play_correct()
        else:
            print("Wrong!")
            self.streak = 0
            self.multiplier = 1
            self.is_correct = 0
            App.get_running_app().play_error()

        if self.streak > 0 and self.streak % 5 == 0:
            self.multiplier += 1
            print(f"Multiplier increased to x{self.multiplier}!")

        print(f"Points: {self.points}, Streak: {self.streak}")
        self.generate_question()

class levelScreenHR(Screen):
    equation_text = StringProperty("")
    option_a = StringProperty("")
    option_b = StringProperty("")
    option_c = StringProperty("")
    option_d = StringProperty("")
    correct_answer = NumericProperty(0)


    points = NumericProperty(0)
    multiplier = NumericProperty(1)
    streak = NumericProperty(0)
    
    def on_pre_enter(self, *args):
            self.generate_question()
    def generate_question(self):
        """Generate a new equation and assign answers to buttons"""
        qgen = func.AdditionSubtractionMultiplicationDivision()
        equation, answers, correct = qgen.generateQuestion()
        self.correct_answer = correct
        self.equation_text = equation
        self.option_a, self.option_b, self.option_c, self.option_d = map(str, answers)


    def check_answers(self, selected_text):
        if int(selected_text) == self.correct_answer:
            print("Correct")
            self.is_correct = 1
            self.streak += 1
            self.points += 10 * self.multiplier
            App.get_running_app().play_correct()   # <-- play correct
        else:
            print("Wrong!")
            self.streak = 0
            self.multiplier = 1
            self.is_correct = 0
            App.get_running_app().play_error()     # <-- play error

        if self.streak > 0 and self.streak % 5 == 0:
            self.multiplier += 1
            print(f"Multiplier increased to x{self.multiplier}!")

        print(f"Points: {self.points}, Streak: {self.streak}")
        self.generate_question()

class accountScreen(Screen):
    pass

class challengeScreen(Screen):
    equation_text = StringProperty("")
    option_a = StringProperty("")
    option_b = StringProperty("")
    option_c = StringProperty("")
    option_d = StringProperty("")
    correct_answer = NumericProperty(0)

    points = NumericProperty(0)
    multiplier = NumericProperty(1)
    streak = NumericProperty(0)

    time_text = StringProperty("05:00")

    def on_pre_enter(self, *args):
        # create equation generator with timer
        self.qgen = func.ChallangeEquations()
        self.qgen.start_timer()

        # sync first time update
        self.update_time_label()
        self.generate_question()

        # schedule UI updates every second
        self._timer_event = Clock.schedule_interval(lambda dt: self.update_time_label(), 1)

    def on_leave(self, *args):
        # stop timer when leaving the screen
        if hasattr(self, "qgen"):
            self.qgen.stop_timer()
        if hasattr(self, "_timer_event") and self._timer_event:
            self._timer_event.cancel()

    def update_time_label(self):
        """Update time_text from qgen timer"""
        mins = self.qgen.time_remaining // 60
        secs = self.qgen.time_remaining % 60
        self.time_text = f"{mins:02}:{secs:02}"

        # End game when time runs out
        if self.qgen.time_remaining <= 0:
            self.end_game()

    def generate_question(self):
        """Generate a new equation and assign answers to buttons"""
        equation, answers, correct = self.qgen.generateQuestion()
        self.correct_answer = correct
        self.equation_text = equation
        self.option_a, self.option_b, self.option_c, self.option_d = map(str, answers)

    def check_answers(self, selected_text):
        if int(selected_text) == self.correct_answer:
            print("Correct")
            self.is_correct = 1
            self.streak += 1
            self.points += 10 * self.multiplier
            App.get_running_app().play_correct()
        else:
            print("Wrong!")
            self.streak = 0
            self.multiplier = 1
            self.is_correct = 0
            App.get_running_app().play_error()
            self.qgen.penalize_time()
            self.update_time_label()

        # multiplier system
        if self.streak > 0 and self.streak % 5 == 0:
            self.multiplier += 1
            print(f"Multiplier increased to x{self.multiplier}!")

        print(f"Points: {self.points}, Streak: {self.streak}")
        self.generate_question()

    def end_game(self):
        """Called when timer hits 0"""
        print("Game Over! Time is up.")
        if hasattr(self, "qgen"):
            self.qgen.stop_timer()
        if hasattr(self, "_timer_event") and self._timer_event:
            self._timer_event.cancel()
        if self.manager:
            self.manager.current = "startScreen"




class NumberNinja(App):
    def build(self):
        sm = WindowManager()
        
        ## ResourceManager usage
        self.rm = manager.ResourceManager()

        ## Load fonts
        self.rm.register_font("CaveatBrush", "fonts\\CaveatBrush.ttf")
        
        ## Load default sounds
        self.rm.load_default_sounds()

        ## Getting Path to font
        self.rm.register_font("CaveatBrush", "fonts\\CaveatBrush.ttf")

        ## Load KV file with safe path
        Builder.load_file(self.rm.path("numberninja.kv"))

        ## Adding screens
        sm.add_widget(startScreen(name="startScreen"))
        sm.add_widget(levelSelectionScreen(name="levelSelectionScreen"))
        sm.add_widget(levelScreenVE(name="levelScreenVE"))
        sm.add_widget(levelScreenES(name="levelScreenES"))
        sm.add_widget(levelScreenNM(name="levelScreenNM"))
        sm.add_widget(levelScreenHR(name="levelScreenHR"))
        sm.add_widget(accountScreen(name="accountScreen"))
        sm.add_widget(challengeScreen(name="challengeScreen"))

        return sm
    def play_click_sound(self):
        self.rm.play_sound('click')
    def play_correct(self):
        self.rm.play_sound('correct')
    def play_error(self):
        self.rm.play_sound('error')

if __name__ == "__main__":
    NumberNinja().run()