## Archivo para dejar funciones de ambito general.
import logging
from enum import Enum
from datetime import datetime, timedelta

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

def filtrar_equals(params, class_):
    coleccion = class_.objects.all()
    for param in params:
        if params[param] != '':
            kwargs = {
                (param): params[param],
            }
            coleccion = class_.objects.filter(**kwargs)
    return coleccion

def generar_fecha(delta=0, formato='%d/%m/%Y'):
    hoy = datetime.now()

    fecha_delta = hoy + timedelta(days=delta)
    fecha_formateada = fecha_delta.strftime(formato)   
    
    return fecha_formateada

def precioAsInt(precio):
    return int(precio.replace(".",""))

########### ENUMERACIONES
class ComunasRM(Enum):
    Cerrillos = 'Cerrillos'
    CerroNavia = 'Cerro Navia'
    Conchali = 'Conchalí'
    ElBosque = 'El Bosque'
    EstacionCentral = 'Estación Central'
    Huechuraba = 'Huechuraba'
    Independencia = 'Independencia'
    LaCisterna = 'La Cisterna'
    LaFlorida = 'La Florida'
    LaGranja = 'La Granja'
    LaPintana = 'La Pintana'
    LaReina = 'La Reina'
    LasCondes = 'Las Condes'
    LoBarnechea = 'Lo Barnechea'
    LoEspejo = 'Lo Espejo'
    LoPrado = 'Lo Prado'
    Macul = 'Macul'
    Maipu = 'Maipú'
    nunoa = 'Ñuñoa'
    PedroAguirreCerda = 'Pedro Aguirre Cerda'
    Penalolen = 'Peñalolén'
    Providencia = 'Providencia'
    Pudahuel = 'Pudahuel'
    Quilicura = 'Quilicura'
    QuintaNormal = 'Quinta Normal'
    Recoleta = 'Recoleta'
    Renca = 'Renca'
    Santiago = 'Santiago'
    SanJoaquin = 'San Joaquín'
    SanMiguel = 'San Miguel'
    SanRamon = 'San Ramón'
    Vitacura = 'Vitacura'
    PuenteAlto = 'Puente Alto'
    Pirque = 'Pirque'
    SanJosedeMaipo = 'San José de Maipo'
    Colina = 'Colina'
    Lampa = 'Lampa'
    Tiltil = 'Tiltil'
    SanBernardo = 'San Bernardo'
    Buin = 'Buin'
    CaleradeTango = 'Calera de Tango'
    Paine = 'Paine'
    Melipilla = 'Melipilla'
    Alhue = 'Alhué'
    Curacavi = 'Curacaví'
    MariaPinto = 'María Pinto'
    SanPedro = 'San Pedro'
    Talagante = 'Talagante'
    ElMonte = 'El Monte'
    IsladeMaipo = 'Isla de Maipo'
    PadreHurtado = 'Padre Hurtado'
    Penaflor = 'Peñaflor'

class Sucursales(Enum):
    Maipu = 'Maipú'
    LaReina = 'La Reina'