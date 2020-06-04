# Duckingmovies Django

<h4 align = 'center'>Proyecto final de la clase de sistemas y tecnologías web, 1er semestre de 2020</h4>

<h4 align = 'center'> Desarrollado por Andy Castillo y Marco Fuentes </h4>

# MONTAR ENTORNO VIRTUAL

```bash
# Montar entorno
python3 -m venv venv
# Inicializar entorno
souce venv/bin/activate
```

# Instalar dependencias

```bash
# Instalar todas las dependencias con un solo comando
pip3 install -r requirements.txt
```

# CARGAR DATOS A LA BD

Poner credenciales en archivo **credentials.py**

```bash
#ejemplo
DEVELOPMENT_DATABASE = {
    'NAME': 'duckingmovies',
    'USER': 'administrador',
    'PASSWORD': 'gamecube',
    'HOST': 'localhost',
    'PORT': '5430',
    'CONNECTION': 'postgres',
}
```
Correr el archivo **load_data.py**:

```bash
#Seleccionar opcion 1
Create or Reset DB

#Seleccionar opcion 3
Migrations

#Seleccionar opcion 4
Exit
```

Iniciar server de django:

```bash
python manage.py runserver
```

Copiar el link en donde está corriendo el servidor en el navegador
```bash
#Normalmente es
http://127.0.0.1:8000/
```
 y agregarle
```bash
admin/initial-data/

#Ejemplo
http://127.0.0.1:8000/admin/initial-data/
```
Si sale de mensaje: **{"Status": "Ok", "Data": "Data imported"}**
Ya hay data en la bd


