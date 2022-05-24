"""6. Дано рядок. Якщо в цьому рядку буква f зустрічається тільки один раз, виведіть її індекс. Якщо
вона зустрічається два і більше разів, виведіть індекси її першої і останньої появи. Якщо буква f в
цьому рядку не зустрічається, нічого не виводьте."""

def ffind(a: str):
    first = a.find('f')
    last = a.rfind('f')
    if first != -1 and last != -1 and first != last:
        return first, last
    if first != -1 and last!= -1 and first == last:
        return first
    if first != -1 and last == -1:
        return first
    if first == -1 and last != -1:
        return last
    if first == -1 and last == -1:
        return ' '


a = str(input())
print(ffind(a))