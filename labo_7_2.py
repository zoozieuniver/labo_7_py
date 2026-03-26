n=int(input("Введіть число для послідовності Коллатца: "))

def collatz(value):
    while True:
        if value % 2 == 0: #перевірка на парність
            value //= 2
            print(value)
        else:
            value = (value * 3) + 1
            print(value)
        if value == 1:
            break

collatz(n)