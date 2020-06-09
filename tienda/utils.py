## Archivo para dejar funciones de ambito general.
import logging

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

def filtrar_icontains(params, class_):
	coleccion = class_.objects.all()
	for param in params:
		if params[param] != '':
			kwargs = {
				'{0}__{1}'.format(param, 'icontains'): params[param],
			}
			coleccion = class_.objects.filter(**kwargs)
	return coleccion