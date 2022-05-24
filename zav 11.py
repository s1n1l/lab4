"""11. Дано список. Вивести спочатку всі негативні елементи, а потім всі інші.
"""


def sp(dl):
    negative = []
    positive = []
    for i in dl:
        if i < 0:
            negative.append(i)
        else:
            positive.append(i)
    return negative + positive


n = []

while True:
    m = input("Введите число или букву чтобы закончить список 'n' ")
    if m == "n":
        break
    else:
      m = int(m)
      n.append(m)
      m = None


print(sp(n))