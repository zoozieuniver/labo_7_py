n= [] #змінюю змінну на масив, поскільки з числом не буде зручно визначати довжину послідовності

def collatz(value):
    temp_value=int(input("Введіть число для послідовності Коллатца:"))
    value.append(temp_value)
    i=0
    while True:
        if value[i] % 2 == 0: #перевірка на парність
            value.append(value[i]//2)
            i += 1
            print(value[i])
        else:
            value.append((value[i] * 3) + 1)
            i += 1
            print(value[i])
        if value[i] == 1:
            break

    def collatz_len(value):
        counter=0
        for i in value:
            counter += 1
        print("Кількість кроків було виконано =", counter)
        
    collatz_len(value)

collatz(n)