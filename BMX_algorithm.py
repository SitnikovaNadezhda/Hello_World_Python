# алгоритм Бойера-Мура-Хопспула
t = "данные"
# этап 1 формирования таблицы смещений
S = set()    # уникальные символы
M = len(t)   # число символов в образе
d = {}       # словарь смещений
for i in range(M-2, -1, -1):  # интерации с предпоследнего символа
    if t[i] not in S:         # если символ еще не добавлен в таблицу
        d[t[i]] = M-i-1
        S.add(t[i])
if t[M-1] not in S:     # отдельно формируем смещение для последнего символа
    d[t[M-1]] = M
d['*'] = M      # смещение для прочих символов
print(d)

# этап 2 поиск образа в строке

a = "большие метеоданные"
N = len(a)

if N >= M:
    i = M-1  # счетчик проверяемого символа строки

    while (i < N):
        k = 0

        for j in range(M-1, -1, -1):

            if a[i-k] != t[j]:

                if j == M-1:     # смещение, если не равен последний символ образа
                    off = d[a[i]] if d.get(a[i], False) else d['*']
                else:            # смещение, если не равен последний символ образа
                    off = d[t[j]]

                i += off  # смещение счетчика строки
                break

            k += 1     # смущение для сравниваемого символа в строке

        if j == 0:     # Если дошли до этой строки, образы совпали
            print(f"образ найден по индексу {i-k+1}")
            break
    else:
        print("образ не найден")
else:
    print("образ не найден")
