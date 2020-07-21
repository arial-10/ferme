from django import template

register = template.Library()

def actualizar_variable(value, arg):
    print(arg)
    value = arg
    return value

register.filter('actualizar_variable', actualizar_variable)