import pandas as pd
import matplotlib.pyplot as plt

# Застосування стилю для графіків
plt.style.use('ggplot') 
plt.rcParams['figure.figsize'] = (15, 5)

# Читання даних із CSV
file_path = "data.csv"  
column_names = [
    "Date", "Rachel / Papineau", "Berri1", "Maisonneuve_1", "Maisonneuve_2", "Brebeuf", "Parc",
    "PierDup", "CSC (Cote Sainte-Catherine)", "Pont_Jacques_Cartier", "Totem_Laurier", "Notre-Dame",
    "Rachel / Hotel de Ville", "Saint-Antoine", "Rene-Levesque", "Viger", "Boyer", "Maisonneuve_3",
    "University", "Saint-Urbain"
]

# Завантаження даних
bike_data = pd.read_csv(
    file_path,
    names=column_names,
    header=0,
    parse_dates=["Date"],  
    dayfirst=True,
    index_col="Date"       
)
print(bike_data.head(3))

bike_data.index = pd.to_datetime(bike_data.index)
bike_data["Month"] = bike_data.index.month
bike_data = bike_data.dropna(axis=1, how="all")

# Обчислення загальної кількості велосипедистів за день
bike_data["Total"] = bike_data.iloc[:, :-1].sum(axis=1)

# Групування даних за місяцями
monthly_data = bike_data.groupby("Month")["Total"].sum()

# Визначення найпопулярнішого місяця
most_popular_month = monthly_data.idxmax()
most_popular_month_count = monthly_data.max()
print(f"Найпопулярніший місяць: {most_popular_month}, кількість велосипедистів: {most_popular_month_count}")

# Створення DataFrame із даними за рік
annual_data = pd.DataFrame({
    "Month": monthly_data.index,
    "Total Cyclists": monthly_data.values
})

# Виведення зведених даних
print("Дані використання велодоріжок за 2014 рік:")
print(annual_data)

# Побудова графіка для щоденних даних
bike_data["Total"].plot(figsize=(15, 10), title="Щоденне використання велодоріжок")
plt.xlabel("Дата")
plt.ylabel("Загальна кількість велосипедистів")
plt.show()

# Побудова графіка для місячних даних
monthly_data.plot(kind="bar", color="skyblue", figsize=(15, 5), title="Відвідування велодоріжок за місяцями")
plt.xlabel("Місяць")
plt.ylabel("Загальна кількість велосипедистів")
plt.xticks(range(0, 12), labels=range(1, 13))  
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
