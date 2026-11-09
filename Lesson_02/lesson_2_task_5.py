def month_to_season(month):
    seasons = {
        12: "Зима",
        1: "Зима",
        2: "Зима",
        3: "Весна",
        4: "Весна",
        5: "Весна",
        6: "Лето",
        7: "Лето",
        8: "Лето",
        9: "Осень",
        10: "Осень",
        11: "Осень"
    }
    return seasons.get(month, "Ошибка! Неверный номер месяца.")

for m in range(1, 13):
    print(m, "→", month_to_season(m))