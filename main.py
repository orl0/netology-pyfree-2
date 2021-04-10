HELP = """Доступные команды: 
  help  - Напечатать данную справку
  add   - Добавить задачу в список
  print - Напечатать все задачи из списка
  exit  - Завершить программу"""

print(HELP)

tasks = {
  # 'today': [],
  # 'tomorrow': [],
  # 'other': []
}

while True:
  command = input('Введите команду: ').strip().lower()
  if command == 'help':
    print(HELP)
  elif command == 'add':
    inputDate = input("> Введите дату: ").strip().lower()
    inputTask = input("> Введите задачу: ")

    listName = 'other'

    if inputDate == 'today' or inputDate == 'сегодня':
      listName = 'today'
    elif inputDate == 'tomorrow' or inputDate == 'завтра':
      listName = 'tomorrow'

    if listName in tasks:
      tasks[listName].append(inputTask)
    else:
      tasks[listName] = [inputTask]

    print(f'Задача \'{inputTask}\' добавлена в список \'{listName}\'.')
  elif command == 'print':
    for date, tasklist in tasks.items():
      print(f'📅 {date.upper()}:')
      for task in tasklist:
        print(f'- {task}')
  elif command == 'exit':
    print('Спасибо за использование! До свидания!')
    break
  else:
    print('(!) Неизвестная команда')
