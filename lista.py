def estaEnRango(valor, minimo, maximo):
    """Devuelve True o False determinando que valor se encuentra entre el mínimo y el máximo."""
    return minimo <= valor <= maximo


def estaEnLista(valor, lista):
    """Devuelve True o False determinando si el valor está en la lista."""
    return valor in lista


def main():
    # Obtenemos el número del usuario
    numero = int(input("Introduce un número del 1 al 20: "))

    # Comprobamos que el número está en el rango
    if not estaEnRango(numero, 1, 20):
        print("El número no está en el rango.")
        return

    # Comprobamos que el número está en la lista
    if estaEnLista(numero, [6, 14, 11, 3, 2, 1, 15, 19]):
        print("El número está en la lista.")
    else:
        print("El número no está en la lista.")


if __name__ == "__main__":
    main()