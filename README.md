# Sistema de Gestion Ferreteria Ferme

# Instalacion

## Requerimientos
- Oracle 18c
- Python 3.8
- Dependencias de Python en requirements.txt (ver preparación)

## Instalación de la Base de datos

FERME funciona con python 3.8 y Oracle Express 18c. Para instalar, primero descarguelo del siguiente [link](https://www.oracle.com/database/technologies/xe-downloads.html) extraiga el archivo y ejecute el instalador. Siga las instrucciones de instalación.

Una vez instalado es importante anotar estos valores: la ip será **127.0.0.1 o localhost**, el puerto **1521** y el nombre de la base de datos **XE**, estos datos
serán útiles si prefiere usar su propio [gestor de base de datos](https://dbeaver.io/). 
FERME usará estos valores para conectarse a la base de datos.

### Creación del Usuario

FERME utiliza un usuario específico para manejar sus tablas, para crear este usuario debe correr el script de creación de usuario (`crear_usuario.sql`) desde un gestor de bases de datos o utilizando `sqlplus`

## Preparación del Ambiente Python

Clone el repositorio o extraiga el zip que se le ha entregado. Los siguientes pasos deben ser realizados en una línea de comandos (cmd.exe en windows)

Para los siguientes pasos asumiremos que el repositorio se encuentra clonado/descomprimido en C:\FERME

### 1. Creación del Ambiente Virtual

1. Ingrese al Directorio:
  `cd C:\Ferme`
2. Cree un ambiente virtual:
  `python -m venv venv` (python venv <nombre>)\
    Esto creará una carpeta llamada `venv`
3. Cargue el ambiente virtual
  `venv/scripts/activate.bat` (en linux `source venv/bin/source`)
4. Si ha cargado el ambiente correctamente aparecerá `(venv)` al comienzo de la línea
  
### 2. Instalación de los requerimientos

1. Dentro del ambiente virtual instale los requerimientos con pip\
    `(venv) python pip install -r requirements.txt`

## Carga de datos

## Ejecución
