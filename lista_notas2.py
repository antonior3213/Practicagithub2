def media(lista_notas):
    """Devuelve la media aritmética de una lista de notas."""
    if not lista_notas:
        raise ValueError("La lista de notas no puede estar vacía")
    return sum(lista_notas) / len(lista_notas)


if __name__ == "__main__":
    notas = [6.5, 7, 8.25, 5]
    print(f"Media: {media(notas):.2f}")