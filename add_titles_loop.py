
# Создаём список для хранения заголовков
note = {"titles":[]}

# Запрос ввода заголовков заметки
print("Добавьте заголовки к заметке(для завершения оставьте поле пустым)")

# Создаём цикл
while True:
    title = input("Заголовок: ")

# Команда завершения
    if title.strip() == "":
        break

# Проверяем уникальность заголовков
    if title in note["titles"]:
        print(f"Заголовок '{title}' уже существует. Придумайте другой.")
        continue

# Добавляем вписанные заголовки в список
    note["titles"].append(title)

# Выводим заголовки заметки, которые ввёл пользователь
print(f"Заголовки заметки: ")
for title in note["titles"]:print(title)

