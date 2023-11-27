def esBinario(strbinario):
    # Comprueba si todos los caracteres son '0' o '1'
    return all(caracter == '0' or caracter == '1' for caracter in strbinario)

def binario_a_decimal(strbinario):
    # Verifica si la cadena es binaria
    if esBinario(strbinario):
        # Convierte el número binario a decimal
        decimal = int(strbinario, 2)
        return decimal
    else:
        return None

#  Preguntar por un número binario
numero_binario = input("Ingrese un número binario: ")

# Convertir el número binario a decimal y mostrar el resultado
resultado_decimal = binario_a_decimal(numero_binario)

if resultado_decimal is not None:
    print(f"El equivalente decimal de {numero_binario} es: {resultado_decimal}")
else:
    print("Entrada no válida. Por favor, ingrese un número binario.")
