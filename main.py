i = 0
inputDate = []
inputTask = []

while i < 3:
  i += 1
  inputDate.append(input("Введите дату: "))
  inputTask.append(input("Введите задачу: "))

while len(inputDate) > 0:
  print(inputDate.pop(0), inputTask.pop(0))
