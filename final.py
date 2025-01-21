
note = {}
note["titles"] = []

note["username"] = input("Как вас зовут?: ")

title = input("Придумайте заголовок заметки(для завершение нажмите Enter): ")
note["titles"].append(title)

note["content"] = input("Напишите содержание(для завершение нажмите Enter: ")

status_prompt = "Укажите статус, например: Предстоит, В работе, Выполнена, Отложена): "
note["status"] = input(status_prompt)

note["created_date"] = input("Дата начала выполнения - день.месяц.год: ")
note["issue_date"] = input("Дата окончания(дедлайн) - день.месяц.год: ")

print(f"Информация о заметке: " ,
       f"Имя пользователя: {note['username']}",
       f"Статус: {note['status']}",
       f"Содержание заметки: {note['content']}",
       f"Дата начала: {note['created_date'][0:5]}",
       f"Дата окончания: {note['issue_date'][0:5]}",
       sep = '\n'
       )
print("Заголовок заметки: ")
for title in note["titles"]:print(title)