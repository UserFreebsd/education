x = int(input('Введите время сна: '))
h = int(input('Введите час отхода ко сну: '))
m = int(input('Введите минуты отходы ко сну: '))

xh = x // 60
xm = x % 60
hw = h + xh
mw = m + xm

if mw >= 60:
    hw += 1
    mw -= 60
if hw >= 24:
    hw -= 24

print(f'Будильник нужно ставить на {hw} часов {mw} минут')