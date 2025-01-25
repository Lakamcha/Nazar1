users_age_groups = {
    "Андрій": "18-25",
    "Марія": "26-35",
    "Олександр": "36-45",
    "Ірина": "46-60",
    "Петро": "60+"
}

name = input()

if name in users_age_groups:
    print(users_age_groups[name])
else:
    print("Ім'я не знайдено.")


