for i in range(9):
  if i > 3:
    break
  print(i)

#2
i = 1
while i < 9:
  print(i)
  if i == 3:
    break
  i += 1

#my_examples
i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1


number = 1
while number <= 10:
    print(number)
    if number == 7:
        break
    number += 1


count = 10
while count > 0:
    print(count)
    if count == 3:
        break
    count -= 1


x = 0
while x < 8:
    print(x)
    if x == 4:
        break
    x += 1


numbers = [2, 4, 6, 8, 10]

for n in numbers:
    print(n)
    if n == 6:
        break
