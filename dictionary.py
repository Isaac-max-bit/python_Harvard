# Variables Globales
# El conjunto (set) global que almacenará todas las palabras del diccionario.
words = set()

# ----------------------------------------------------------------------

# Funciones del Diccionario

def check(word):
    """
    Verifica si una palabra está en el diccionario.
    
    Toma la palabra de entrada, la convierte a minúsculas y la busca
    en el conjunto 'words'. La conversión a minúsculas permite que
    la verificación no sea sensible a mayúsculas o minúsculas.
    
    :param word: La palabra a verificar (string).
    :return: True si la palabra está en el diccionario, False en caso contrario.
    """
    # 💡 Aprendizaje: Convertir a .lower() es clave para un corrector
    # ortográfico, ya que "Palabra" y "palabra" deberían considerarse iguales.
    return word.lower() in words

def load(dictionary):
    """
    Carga un diccionario de un archivo de texto en la memoria.
    
    Abre el archivo de diccionario, lee todas las líneas (palabras) y las
    añade al conjunto 'words'.
    
    :param dictionary: El nombre del archivo de diccionario (string).
    :return: True si la carga fue exitosa.
    """
    try:
        # Abrir el archivo de forma segura con 'with'
        with open(dictionary, 'r') as file:
            # Leer el contenido, dividirlo en líneas (splitlines) y actualizar el conjunto
            # .splitlines() elimina los caracteres de nueva línea (\n)
            words.update(file.read().splitlines())
        print(f"✅ Diccionario cargado desde '{dictionary}'.")
        return True
    except FileNotFoundError:
        print(f"❌ Error: El archivo '{dictionary}' no fue encontrado.")
        return False
    except Exception as e:
        print(f"❌ Ocurrió un error al cargar el diccionario: {e}")
        return False

def size():
    """
    Devuelve el número de palabras cargadas actualmente en el diccionario.
    
    :return: El número de elementos en el conjunto 'words' (integer).
    """
    return len(words)

def unload():
    """
    Libera la memoria utilizada por el diccionario.
    
    En este caso, simplemente vaciamos el conjunto 'words'.
    
    :return: True indicando que la "descarga" fue exitosa.
    """
    # 💡 Aprendizaje: En Python, vaciar el set() es suficiente para liberar
    # la memoria utilizada por las palabras. Si usáramos memoria dinámica
    # en un lenguaje como C, esta función sería crucial.
    words.clear() 
    print("🗑️ Diccionario descargado. Memoria liberada.")
    return True

# ----------------------------------------------------------------------

# Sección de Pruebas y Uso

if __name__ == "__main__":
    
    # 1. Cargar el Diccionario
    print("--- Iniciando la carga ---")
    nombre_archivo = "diccionario.txt"
    if load(nombre_archivo):
        
        # 2. Verificar el Tamaño
        print("\n--- Verificando el tamaño ---")
        num_palabras = size()
        print(f"Total de palabras cargadas: {num_palabras}") # Debería ser 7
        
        # 3. Comprobar Palabras
        print("\n--- Comprobando palabras (check) ---")
        
        palabra1 = "perro"
        print(f"¿'{palabra1}' está en el diccionario? -> {check(palabra1)}") # True
        
        palabra2 = "PYTHON"
        print(f"¿'{palabra2}' está en el diccionario? -> {check(palabra2)}") # True (gracias a .lower())
        
        palabra3 = "gata"
        print(f"¿'{palabra3}' está en el diccionario? -> {check(palabra3)}") # False
        
        # 4. Descargar el Diccionario
        print("\n--- Descargando el diccionario ---")
        unload()
        
        # 5. Comprobar que se descargó
        print(f"Tamaño después de descargar: {size()}") # Debería ser 0
        
    else:
        print("\nNo se pudo continuar con las pruebas debido al error de carga.")