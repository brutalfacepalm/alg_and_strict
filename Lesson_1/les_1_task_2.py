# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг
# вправо и влево на два знака.

n1 = 5
n2 = 6
b_and = n1 & n2
b_or = n1 | n2
b_right = n1 >> 2
b_left = n1 << 2

print(b_and, b_or, b_right, b_left)
