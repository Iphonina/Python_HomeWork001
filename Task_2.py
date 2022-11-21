# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

x = int(input('введите значение X '))
y = int(input('введите значение Y '))
z = int(input('введите значение Z '))

left = not (x or y or z)
right = not x and not y and not z
if left == right:
    print('Утверждение верно!')
else:
    print('Утверждение НЕ верно!')
