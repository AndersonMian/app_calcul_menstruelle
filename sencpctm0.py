import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import random

class MenstrualCycleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculateur de Cycle Menstruel")
        
        # Variables pour les widgets
        self.cycle_length = tk.IntVar(value=28)
        self.period_length = tk.IntVar(value=5)
        self.start_date = tk.StringVar(value=datetime.today().strftime('%Y-%m-%d'))
        self.regular_cycle = tk.BooleanVar(value=True)
        self.min_cycle_length = tk.IntVar(value=25)
        self.max_cycle_length = tk.IntVar(value=35)
        
        # Créer l'interface utilisateur
        self.create_widgets()
    
    def create_widgets(self):
        # Choix du cycle régulier ou irrégulier
        ttk.Label(self.root, text="Type de cycle:").grid(column=0, row=0, sticky=tk.W)
        ttk.Radiobutton(self.root, text='Régulier', variable=self.regular_cycle, value=True, command=self.toggle_cycle_type).grid(column=1, row=0, sticky=tk.W)
        ttk.Radiobutton(self.root, text='Irrégulier', variable=self.regular_cycle, value=False, command=self.toggle_cycle_type).grid(column=2, row=0, sticky=tk.W)
        
        # Longueur du cycle
        self.cycle_length_label = ttk.Label(self.root, text="Longueur du cycle (jours):")
        self.cycle_length_label.grid(column=0, row=1, sticky=tk.W)
        self.cycle_length_entry = ttk.Entry(self.root, textvariable=self.cycle_length, width=5)
        self.cycle_length_entry.grid(column=1, row=1, sticky=tk.W)
        
        # Longueur des règles
        ttk.Label(self.root, text="Longueur des règles (jours):").grid(column=0, row=2, sticky=tk.W)
        ttk.Entry(self.root, textvariable=self.period_length, width=5).grid(column=1, row=2, sticky=tk.W)
        
        # Date de début
        ttk.Label(self.root, text="Date de début des règles:").grid(column=0, row=3, sticky=tk.W)
        ttk.Entry(self.root, textvariable=self.start_date, width=10).grid(column=1, row=3, sticky=tk.W)
        
        # Longueur minimale et maximale du cycle pour irrégulier
        self.min_cycle_length_label = ttk.Label(self.root, text="Longueur minimale du cycle (jours):")
        self.min_cycle_length_entry = ttk.Entry(self.root, textvariable=self.min_cycle_length, width=5)
        self.max_cycle_length_label = ttk.Label(self.root, text="Longueur maximale du cycle (jours):")
        self.max_cycle_length_entry = ttk.Entry(self.root, textvariable=self.max_cycle_length, width=5)
        
        # Bouton de calcul
        ttk.Button(self.root, text="Calculer", command=self.calculate_cycle).grid(column=0, row=4, columnspan=3)
        
        # Zone de résultat
        self.result_frame = ttk.Frame(self.root, padding="10")
        self.result_frame.grid(column=0, row=5, columnspan=3)
        
        # Initialiser l'état du cycle
        self.toggle_cycle_type()
    
    def toggle_cycle_type(self):
        if self.regular_cycle.get():
            self.cycle_length_label.grid()
            self.cycle_length_entry.grid()
            self.min_cycle_length_label.grid_remove()
            self.min_cycle_length_entry.grid_remove()
            self.max_cycle_length_label.grid_remove()
            self.max_cycle_length_entry.grid_remove()
        else:
            self.cycle_length_label.grid_remove()
            self.cycle_length_entry.grid_remove()
            self.min_cycle_length_label.grid(column=0, row=1, sticky=tk.W)
            self.min_cycle_length_entry.grid(column=1, row=1, sticky=tk.W)
            self.max_cycle_length_label.grid(column=0, row=2, sticky=tk.W)
            self.max_cycle_length_entry.grid(column=1, row=2, sticky=tk.W)
    
    def calculate_cycle(self):
        try:
            period_length = self.period_length.get()
            start_date = datetime.strptime(self.start_date.get(), '%Y-%m-%d')
            regular_cycle = self.regular_cycle.get()
            
            # Clear previous results
            for widget in self.result_frame.winfo_children():
                widget.destroy()
            
            if regular_cycle:
                cycle_length = self.cycle_length.get()
                ovulation_day = start_date + timedelta(days=(cycle_length // 2))
                period_days = [start_date + timedelta(days=i) for i in range(period_length)]
                ovulation_days = [ovulation_day + timedelta(days=i) for i in range(-1, 2)]
                cycle_days = [(start_date + timedelta(days=i)) for i in range(cycle_length)]
            else:
                min_cycle_length = self.min_cycle_length.get()
                max_cycle_length = self.max_cycle_length.get()
                cycle_length = random.randint(min_cycle_length, max_cycle_length)
                ovulation_day = start_date + timedelta(days=(cycle_length // 2))
                period_days = [start_date + timedelta(days=i) for i in range(period_length)]
                ovulation_days = [ovulation_day + timedelta(days=i) for i in range(-1, 2)]
                cycle_days = [(start_date + timedelta(days=i)) for i in range(cycle_length)]
            
            # Afficher les résultats
            ttk.Label(self.result_frame, text="Calendrier du cycle:").grid(column=0, row=0, sticky=tk.W)
            row = 1
            for i in range(len(cycle_days)):
                day = cycle_days[i]
                day_str = day.strftime('%Y-%m-%d')
                
                color = 'white'
                if day in period_days:
                    color = 'red'
                elif day in ovulation_days:
                    color = 'green'
                
                lbl = tk.Label(self.result_frame, text=day_str, bg=color, width=12)
                lbl.grid(column=i % 7, row=row)
                
                if i % 7 == 6:
                    row += 1
        
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue: {e}")

# Créer la fenêtre principale
root = tk.Tk()
app = MenstrualCycleApp(root)
root.mainloop()
