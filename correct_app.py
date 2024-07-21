import streamlit as st
from datetime import datetime, timedelta
import random

def calculate_cycle(start_date, period_length, cycle_length=None, min_cycle_length=None, max_cycle_length=None, regular_cycle=True):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    
    if regular_cycle:
        cycle_length = cycle_length
        ovulation_day = start_date + timedelta(days=(cycle_length // 2))
    else:
        cycle_length = random.randint(min_cycle_length, max_cycle_length)
        ovulation_day = start_date + timedelta(days=(cycle_length // 2))
        
    period_days = [start_date + timedelta(days=i) for i in range(period_length)]
    ovulation_days = [ovulation_day + timedelta(days=i) for i in range(-1, 2)]
    cycle_days = [(start_date + timedelta(days=i)) for i in range(cycle_length)]
    
    return period_days, ovulation_days, cycle_days

def main():
    st.title("Calculateur de Cycle Menstruel")

    # Type de cycle
    regular_cycle = st.radio("Type de cycle", ('Régulier', 'Irrégulier')) == 'Régulier'
    
    # Longueur des règles
    period_length = st.number_input("Longueur des règles (jours)", min_value=1, max_value=10, value=5)
    
    # Date de début des règles
    start_date = st.date_input("Date de début des règles", datetime.today()).strftime('%Y-%m-%d')
    
    if regular_cycle:
        # Longueur du cycle pour les cycles réguliers
        cycle_length = st.number_input("Longueur du cycle (jours)", min_value=21, max_value=35, value=28)
    else:
        # Longueur minimale et maximale du cycle pour les cycles irréguliers
        min_cycle_length = st.number_input("Longueur minimale du cycle (jours)", min_value=21, max_value=35, value=25)
        max_cycle_length = st.number_input("Longueur maximale du cycle (jours)", min_value=21, max_value=35, value=35)
        cycle_length = None  # Not used for irregular cycles
    
    # Bouton de calcul
    if st.button("Calculer"):
        if regular_cycle:
            period_days, ovulation_days, cycle_days = calculate_cycle(start_date, period_length, cycle_length=cycle_length, regular_cycle=True)
        else:
            period_days, ovulation_days, cycle_days = calculate_cycle(start_date, period_length, min_cycle_length=min_cycle_length, max_cycle_length=max_cycle_length, regular_cycle=False)
        
        # Afficher les résultats
        st.write("## Calendrier du cycle")
        for day in cycle_days:
            day_str = day.strftime('%Y-%m-%d')
            if day in period_days:
                st.markdown(f"<span style='color: red;'>{day_str}</span>", unsafe_allow_html=True)
            elif day in ovulation_days:
                st.markdown(f'<span style="color: green;" title="Période d\'ovulation">{day_str}</span>', unsafe_allow_html=True)
            else:
                st.write(day_str)

if __name__ == "__main__":
    main()
