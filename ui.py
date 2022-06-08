from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizzInterface:

    def __init__(self, quiz_text: QuizBrain):
        self.quiz = quiz_text
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score:0", fg='white', bg=THEME_COLOR, font=("Arial", 15))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150,
                                                     120,
                                                     width=250,
                                                     text="Some Question Text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20))
        self.canvas.grid(row=1, column=0, columnspan=2)


        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def true_pressed(self):
        if self.quiz.check_answer("True") == 0:
            self.canvas.config(bg='green')
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg='red')
            self.window.after(1000, self.get_next_question)

    def false_pressed(self):
        if self.quiz.check_answer("False") == 0:
            self.canvas.config(bg='green')
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg='red')
            self.window.after(1000, self.get_next_question)