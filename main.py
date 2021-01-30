HELP = """Доступные команды: 
  help  - Напечатать данную справку
  add   - Добавить задачу в список
  print - Напечатать все задачи из списка
  exit  - Завершить программу"""

print(HELP)

tasks = []

while True:
  command = input('Введите команду: ')
  command = command.strip().lower()
  if command == 'help':
    print(HELP)
  elif command == 'add':
    inputTask = input("Введите задачу: ")
    tasks.append(inputTask)
    print(f'Задача \'{inputTask}\' добавлена.')
  elif command == 'print':
    for task in tasks:
      print(f'- {task}')
  elif command == 'exit':
    break
  else:
    print('(!) Неизвестная команда')
