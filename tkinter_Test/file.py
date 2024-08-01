from tkinter import *
import tkinter as tk
import json as js
from tkinter import messagebox

# Récupération du fichier json
with open("biblio.json", 'r', encoding='utf-8') as fichier:
    donnees = js.load(fichier)

# Création de la fenêtre principale
window = tk.Tk()
window.title("Quiz Application")
window.geometry("600x300")


# Création de la classe Quiz
class Quiz:
    def __init__(self, total_questions):
        self.score = 0
        self.incorrect = 0
        self.number_question = 0
        self.total_questions = total_questions
        self.question_label = tk.Label(window, text="")
        self.question_label.pack(pady=20)
        self.option_entry = tk.Entry(window)
        self.option_entry.pack(pady=10)
        self.submit_button = tk.Button(window, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)
        self.feedback_label = tk.Label(window, text="")
        self.feedback_label.pack(pady=10)
        self.next = tk.Button(window, text="Suivant", command=self.nextWindow, default='disable')
        self.next.pack(padx=5)
        self.exit = tk.Button(window, text="Quitter", command=self.quitter)
        self.exit.pack(pady=5)
        self.display_question()

    def display_question(self):
        if self.number_question < len(self.total_questions):
            question_data = self.total_questions[self.number_question]
            question = question_data['question']
            options = question_data['option']
            self.reponse = question_data['reponse']
            
            self.question_label.config(text=f"{self.number_question + 1} : {question}\nOptions: {', '.join(options)}")
            self.option_entry.delete(0, tk.END)
            self.number_question += 1
        else:
            pass

    def check_answer(self):
        proposition = self.option_entry.get().strip().lower()
        if proposition == self.reponse.lower():
            self.feedback_label.config(text="Bravo, votre réponse est correcte")
            self.score += 1
        else:
            self.feedback_label.config(text=f"Faux, la bonne réponse est {self.reponse}")
            self.incorrect += 1
            
        self.display_question()
        

    def show_result(self):
        self.option_entry.pack_forget()
        self.submit_button.pack_forget()
    
    def quitter(self):
        window.destroy()
        messagebox.showinfo(message =f"Quiz terminé! Votre score est {self.score} sur {self.number_question} \n le nombre de bonne réponse est {self.score} \n le nombre de mauvaise réponse est {self.incorrect} ")

    def nextWindow(self):
        self.display_question()
        
        

# Initialisation du quiz avec les données du fichier json
    
quiz = Quiz(donnees['questionnaire'])

window.mainloop()
