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

#my_examples
i = 0
while i < 7:
    i += 1
    if i == 4:
        continue
    print(i)


number = 1
while number <= 10:
    if number % 2 == 0:
        number += 1
        continue
    print(number)
    number += 1


while count < 6:
    count += 1
    if count == 2 or count == 5:
        continue
    print(count)


x = 0
while x < 6:
    x += 1
    if x == 3:
        continue
    print(x)


values = [1, 2, 3, 4, 5]

for v in values:
    if v == 4:
        continue
    print(v)
