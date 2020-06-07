## Archivo para dejar funciones de ambito general.

def formatear_numero_miles(entero):
    numero_formateado = f"{entero:,}"

    resultado = format(numero_formateado).replace(',', '.')

    return resultado
