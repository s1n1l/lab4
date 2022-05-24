from operator import sub, truediv

a = list(map(int, input("Введите список значений : ").split()))

def prog(a):
    r = set(map(sub, a[1:], a))
    ou = r.pop() if len(r) == 1 else 0
    return ou

print(prog(a))