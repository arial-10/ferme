## Archivo para dejar funciones de ambito general.

def formatear_numero_miles(entero):
    """Formatea un número entero con separadores de miles.

    Args:
        entero (int): entero a formatear
    Returns:
        String del entero con formato
    """
    numero_formateado = f"{entero:,}"

    resultado = format(numero_formateado).replace(',', '.')

    return resultado
