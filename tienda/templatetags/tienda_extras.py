from django import template

register = template.Library()

def actualizar_variable(value, arg):
    print(arg)
    value = arg
    return value
register.filter('actualizar_variable', actualizar_variable)

@register.filter
def multiplicar(multiplicando, multiplicador):
    return multiplicando * multiplicador

@register.filter
def formatear_miles(entero):
	"""Formatea un número entero con separadores de miles.

	Args:
	    entero (int): entero a formatear
	Returns:
	    String del entero con formato
	"""
	numero_formateado = f"{entero:,}"

	resultado = format(numero_formateado).replace(',', '.')

	return resultado

@register.filter
def multiplicar_y_formatear(multiplicando, multiplicador):
	multiplicacion = multiplicando * multiplicador
	numero_formateado = f"{multiplicacion:,}"

	resultado = format(numero_formateado).replace(',', '.')

	return resultado