for i in range(9):
  if i == 3:
    continue
  print(i)

#2
i = 0
while i < 9:
  i += 1
  if i == 3:
    continue
  print(i)

#3
i = 0
while i < 7:
    i += 1
    if i == 4:
        continue
    print(i)

#4
number = 1
while number <= 10:
    if number % 2 == 0:
        number += 1
        continue
    print(number)
    number += 1

#5
count = 0
while count < 6:
    count += 1
    if count == 2 or count == 5:
        continue
    print(count)

