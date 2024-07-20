import tkinter as tk
from tkinter import messagebox
import datetime

class MenstrualCycleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculateur de Cycle Menstruel")

        # Variables
        self.cycle_type = tk.StringVar(value="Regulier")
        self.cycle_length = tk.IntVar(value=28)
        self.period_length = tk.IntVar(value=5)
        self.last_period_date = tk.StringVar()

        # Interface
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Type de cycle:").grid(row=0, column=0, padx=10, pady=10)
        tk.OptionMenu(self.root, self.cycle_type, "Regulier", "Irregulier").grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Longueur du cycle (jours):").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.cycle_length).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Durée des règles (jours):").grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.period_length).grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Date des dernières règles (AAAA-MM-JJ):").grid(row=3, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.last_period_date).grid(row=3, column=1, padx=10, pady=10)

        tk.Button(self.root, text="Calculer", command=self.calculate_cycle).grid(row=4, column=0, columnspan=2, pady=20)

    def calculate_cycle(self):
        try:
            last_period = datetime.datetime.strptime(self.last_period_date.get(), '%Y-%m-%d')
            cycle_length = self.cycle_length.get()
            period_length = self.period_length.get()

            ovulation_start = last_period + datetime.timedelta(days=(cycle_length // 2) - 2)
            ovulation_end = ovulation_start + datetime.timedelta(days=4)
            next_period_start = last_period + datetime.timedelta(days=cycle_length)

            result = f"Période des règles : {last_period.date()} - {(last_period + datetime.timedelta(days=period_length-1)).date()}\n"
            result += f"Période d'ovulation : {ovulation_start.date()} - {ovulation_end.date()}\n"
            result += f"Prochaine période : {next_period_start.date()}\n"

            self.show_result(result, last_period, period_length, ovulation_start, ovulation_end, next_period_start)
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer une date valide (AAAA-MM-JJ)")

    def show_result(self, result, period_start, period_length, ovulation_start, ovulation_end, next_period_start):
        result_window = tk.Toplevel(self.root)
        result_window.title("Résultats")

        tk.Label(result_window, text=result, font=("Helvetica", 12)).pack(padx=10, pady=10)

        canvas = tk.Canvas(result_window, width=400, height=100)
        canvas.pack()

        # Période des règles en rouge
        canvas.create_rectangle(50, 50, 50 + period_length * 10, 70, fill="red")
        # Période d'ovulation en vert
        canvas.create_rectangle(50 + (ovulation_start - period_start).days * 10, 50,
                                50 + (ovulation_end - period_start).days * 10, 70, fill="green")
        # Prochaine période en rouge (hypothétique, juste une indication)
        canvas.create_rectangle(50 + (next_period_start - period_start).days * 10, 50,
                                50 + (next_period_start - period_start).days * 10 + period_length * 10, 70, fill="red", stipple='gray25')

if __name__ == "__main__":
    root = tk.Tk()
    app = MenstrualCycleApp(root)
    root.mainloop()
