# agree.py

answer = input("Do you agree? ").lower()  # convierte la respuesta a minúsculas

if answer in ["y", "yes"]:
    print("Agreed.")
elif answer in ["n", "no"]:
    print("Not agreed.")
else:
    print("Invalid input.")
