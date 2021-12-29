print("Taschenrechner:")
print()


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


while True:
    value_1 = float(input("Geben Sie die erste Zahl ein: "))
    operator = input("Wählen Sie den gewünschten Operator(+, -, *, /): ")
    value_2 = float(input("Geben Sie die zweite Zahl ein: "))

    if operator == "+":
        print(add(value_1, value_2))
        run = input("Noch einmal (j/n) ? ")
        if run == "n":
            break
    elif operator == "-":
        print(subtract(value_1, value_2))
        run = input("Noch einmal (j/n) ? ")
        if run == "n":
            break
    elif operator == "*":
        print(multiply(value_1, value_2))
        run = input("Noch einmal (j/n) ? ")
        if run == "n":
            break
    elif operator == "/":
        print(divide(value_1, value_2))
        run = input("Noch einmal (j/n) ? ")
        if run == "n":
            break
    else:
        print("Falsche Eingabe...")
        run = input("Noch einmal (j/n) ? ")
        if run == "n":
            break
