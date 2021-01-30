HELP = """Доступные команды: 
help - Напечатать данную справку
add - Добавить задачу в список
print - Напечатать все задачи из списка
exit - завершить программу"""

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
  elif command == 'print':
    print(tasks)
  elif command == 'exit':
    break
  else:
    print('Неизвестная команда')
