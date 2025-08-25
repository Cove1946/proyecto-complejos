# Proyecto: Librería de Números Complejos en Python

Este proyecto implementa una librería en Python para realizar operaciones con números complejos **sin utilizar el tipo de datos `complex` de Python**.  
Los números complejos se representan como tuplas, donde se tiene: `(parte_real, parte_imaginaria)` en forma cartesiana y `(módulo, ángulo)` en forma polar.
De esta forma se busca hacer diferentes operaciones con complejos 

## Getting Started

Las siguientes instrucciones permitiran obtener una copia del proyecto y ejecutarlo en tu máquina local para diferentes propósitos como desarrollo y pruebas.


### Prerequisites
Necesitas tener instalado:

- [Python 3](https://www.python.org/downloads/)
- Un editor de texto o IDE (ejemplo: [PyCharm](https://www.jetbrains.com/pycharm/) o VSCode)

### Installing

1. Clonar el repositorio:
git clone https://github.com/usuario/proyecto-complejos.git

2. Acceder a la carpeta del proyecto:
cd proyecto-complejos

3. Ya puedes ejecutar el código y las pruebas.

## Running the tests

Este proyecto incluye pruebas automáticas usando el framework unittest de Python.

Para ejecutarlas:

python -m unittest test_Libcplx.py

### Break down into end to end tests

Las pruebas verifican:

Operaciones básicas (suma, resta, multiplicación, división)

Propiedades de los complejos (módulo, fase, conjugado)

Conversión entre coordenadas cartesianas y polares

Example
import Libcplx
print(Libcplx.cplx_sum((3,4), (1,2)))   # Se espera como resultado (4,6)

## Deployment

Este proyecto es educativo y está diseñado para ser ejecutado en entornos locales.
No requiere despliegue en servidores externos.

## Built With

* Python 3 - Lenguaje de programación

* unittest - Framework de pruebas

## Contributing

Si se desea contribuir, crea un fork del repositorio y envía un pull request con posibles mejoras

## Versioning

Este proyecto sigue el esquema de versionado SemVer.
Puedes ver las versiones disponibles en la sección de tags del repositorio

## Authors

* Cristian Guerrero - Trabajo inicial - Cove1946

## License

Este proyecto está licenciado bajo la licencia MIT

## Acknowledgments

Inspirado en el curso de CNYT Escuela Colombiana de Ingenieria Julio Garavito


