def traductor_inclusivo(frase):
    """
    Convierte palabras masculinas o femeninas a su versión neutra, reemplazando 'o' o 'a' por 'e'
    en el último o anteúltimo carácter de cada palabra.

    Args:
    frase (str): La frase a traducir.

    Returns:
    str: La frase con las palabras convertidas a lenguaje neutro.
    """
    if not frase:
        return ""

    # Tu código aquí

    # return frase_traducida

# Ejemplo de uso
if __name__ == "__main__":
    frase = input("Ingrese una frase: ")
    resultado = traductor_inclusivo(frase)
    print("Frase traducida:", resultado)
