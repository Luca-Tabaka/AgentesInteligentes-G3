# Grupo tres
Integrantes: Ariel Martin Nuñez, Gabriel Ulises Bianglino, Nicolás Marcelo Cieri Salcedo, Luca Uriel Tabaka, Martina Gonzalo Salvatierra.
---

# Agentes Inteligentes
## ¿Qué es un Agente?

Un **agente** es un programa que puede realizar una acción por sí mismo, sin que
alguien tenga que decirle todo el tiempo qué hacer. Puede interactuar con su
entorno y tomar decisiones.

### Algunos ejemplos pueden ser:

- Un robot que limpia la casa.
- Un programa que recomienda películas.
- Un termostato que ajusta solo la temperatura.

---

## ¿Qué es un Agente Inteligente?
* Un agente inteligente(AI) es un sistema de software creado para poder interactuar con su entorno, percibiendolo mediante sensores con los cuales procesa informacion la cual utiliza para y actuar sobre el con el uso de actuadores.

* Los sensores pueden ser fisicos (Microfonos, medidores de temperatura) o virtuales(Sensor que lee los cambios en una aplicacion).
* Los actuadores son los mecanismos que permiten al AI poder interactuar con el entorno. (Funcion que cambia las rutas dinamicamente en un GPS)
---
### Características de un Agente Inteligente:
Un agente inteligente cuenta con caracteristicas que definen partes de su comportamiento.

* **Autonomía**  
   Puede actuar por su cuenta y controlar su estado interno sin necesidad de intervencion alguna.

* **Reactividad**  
   Analiza el entorno y responde a los cambios.

* **Proactividad**  
   Tiene objetivos propios y toma la iniciativa para cumplirlos sin ser impulsado por ningun evento.

* **Habilidad social**  
   Puede comunicarse con otros agentes o personas.

* **Cooperación**  
   Trabaja junto con otros agentes para alcanzar objetivos.

* **Razonamiento**  
   Puede pensar y sacar conclusiones basado en conocimientos previos.

* **Adaptación**  
   Aprende de la experiencia y mejora su comportamiento.

* **Integridad**  
   Actua de forma honesta buscando el bienestar del usuario.

---

## Clasificacion de Agentes inteligentes

Se pueden clasificar según sus capacidades:

* Agentes simples: programados para seguir reglas predefinidas en un entorno especifico.
* Agentes basados en modelos: programados teniendo un estado interno que refleja elementos que no son visibles, este estado interno es llamado modelo de mundo y se usa para realizar cambios en estado actual.
* Agentes basados en objetivos: programados teniendo en cuenta las caracteristicas de los agentes anteriores, tienen objetivos especificos los cuales logran mediante distintas acciones.
* Agentes basados en el aprendizaje:

---

## Ejemplo simple:

Un agente inteligente podría ser el asistente de Spotify (Sistema de recomendación):

- Aprende tus gustos musicales.
- Te recomienda nuevas canciones.
- Se adapta si un día preferís música más tranquila.
- Habla con otros sistemas para mostrarte eventos en tu ciudad.

---

## Diagrama (explicación)

Imaginá un agente como un ayudante digital que:

- Tiene sus propios objetivos.
- Se comunica con otros ayudantes.
- Aprende de lo que pasa a su alrededor.
- Cambia su comportamiento si algo no funciona bien.

Es como tener un software que trabaja por vos, entiende tus preferencias y se
adapta.

# Práctica - Agente Académico Inteligente

## Objetivo del proyecto

El objetivo principal fue desarrollar una aproximación a agente inteligente
académico que simule asistir a un estudiante en la gestión de sus materias de la
facultad de la carreda de Licenciatura en Informática de la UNAHUR. Este agente
puede:

- Conocer el plan de estudios de la carrera.
- Recordar qué materias tiene aprobadas.
- Validar si puede cursar una materia según las correlativas.
- Recomendar materias para cursar en función del año y las correlativas.
- Avisar que es el principio del cuatrimestre e informar las materias
  recomendadas para anotarse.
- Simular inscripciones automáticas o manuales en la fecha de inscripción.

Más allá de la funcionalidad práctica, que lejos está aun de poder ser usado en
un entorno real, pusimos el foco en evidenciar el uso de Prolog como motor de
inferencia dentro del agente.

## El rol de Prolog

Prolog funciona como el motor de inferencia, osea el responsable de aplicar
reglas lógicas a un conjunto de hechos para tomar decisiones. En este proyecto:

- Las materias y sus correlatividades están definidas como hechos y reglas de
  Prolog.
- Python consulta a Prolog para saber qué materias puede cursar y hasta qué
  materias debería cursar según el estado actual del estudiante.
- La lógica de la decisión académica (qué puede cursar, qué conviene, etc) es
  razonada por Prolog, no por Python.

## Componentes

- `conocimiento.pl`: contiene los hechos sobre las materias, a qué año pertenece
  cada una y las correlatividades.
- `reglas.pl`: contiene el motor lógico del agente. Define reglas que permiten
  verificar si se puede cursar una materia, conocer todas las disponibles,
  conocer solo las aprobadas, agruparlas por año y recomendar materias
  priorizando las de años menores y respetando las correlativas.
- `prolog_interface.py`: Es el nexo entre Python y Prolog. A traves de la
  librería `pyswip` podemos hacer consultas a Prolog encapsuladas en funciones
  de python.
- `main.py`: implementa el agente. Define su comportamiento autónomo, proactivo
  y reactivo.
- `estado.json`: guarda el estado del estudiante (materias aprobadas, flags).

Este enfoque nos permite simular cómo se comportaría un agente y cómo se nutre
de Prolog para poder operar.

## Características del agente

- Autonomía: toma decisiones sin intervención humana, por ejemplo recomendar e
  inscribir en materias o dar avisos.
- Reactividad: Responde al cambio del ambiente, por ejemplo al cambio de fechas
  de inicio de cuatrimestre o de comienzo de inscripción.
- Proactividad: sugiere acciones beneficiosas para el estudiante.
- Basado en modelo: se apoya en un modelo lógico de conocimientos expresado en
  Prolog.

## Cómo correr el proyecto

### Requisitos

- Python
- SWI-Prolog
- pip (gestor de paquetes de Python)

1. Crear entorno virtual

```
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. Instalar dependencias

```
pip install -r requirements.txt
```

3. Ejecutar el agente

```
python agente/main.py
```
