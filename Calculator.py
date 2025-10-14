# Calculator.py
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

x = get_int("x: ")
y = get_int("y: ")

print(f"{x + y}")
print(f"{x - y}")
print(f"{x * y}")
if y != 0:
    print(f"{x / y}")
else:
    print("Error: División por cero no permitida.")
    
