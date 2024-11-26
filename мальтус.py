import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

start_year = 1960
end_year = 2010
initial_population = 118
birth_rate = 0.025
death_rate = 0.012
growth_rate = 1 + birth_rate - death_rate
years = list(range(start_year, end_year + 1))
population = [initial_population]
for i in range(1, len(years)):
    next_population = population[-1] * growth_rate
    population.append(next_population)
for year, pop in zip(years, population):
    print(f"Год: {year}, Численность населения: {int(pop)}")
plt.figure(figsize=(10, 6))
plt.plot(years, population, label="Численность населения")
plt.xlabel("Год")
plt.ylabel("Численность населения")
plt.title("Прогноз численности населения по модели Мальтуса")
plt.grid(True)

plt.show()