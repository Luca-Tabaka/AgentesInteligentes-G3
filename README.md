# Lógica y Programación

# Grupo 3

### Integrantes:

- Ariel Martin Nuñez
- Gabriel Ulises Bianglino
- Nicolás Marcelo Cieri Salcedo
- Luca Uriel Tabaka
- Martin Gonzalo Salvatierra.

---

# Agentes Inteligentes

<img width="6323" alt="Agentes inteligentes (2)" src="https://github.com/user-attachments/assets/61afb348-404d-4a5e-aef3-54585d217a70" />

## ¿Qué es un Agente?

Un **agente** es un sistema de software que analiza e interactua con su entorno que puede realizar una acciones teniendo en cuenta los datos recopilados.

### Algunos ejemplos pueden ser:

- Un robot que limpia la casa.
- Un programa que recomienda películas.
- Un termostato que ajusta solo la temperatura.

---

## ¿Qué es un Agente Inteligente?

- Un agente inteligente(AI) es un sistema de software creado para poder
  interactuar con su entorno, percibiendolo mediante sensores con los cuales
  procesa informacion la cual utiliza para y actuar sobre el con el uso de
  actuadores.

## Estructura básica de un Agente Inteligente

1. Entorno
Es el ambiente en el cual actúa y se desenvuelve el agente. Puede tratarse de un entorno físico (como una fábrica o una casa) o digital (como una aplicación web o un sistema de recomendación). Todo lo que el agente percibe, analiza y modifica ocurre dentro de este entorno.

2. Sensores
Son los instrumentos que permiten al agente percibir el mundo que lo rodea. Estos pueden ser físicos (como cámaras, micrófonos, sensores de temperatura) o digitales (como APIs, entradas de usuario o logs del sistema). A través de los sensores, el agente recolecta información del entorno para poder actuar de forma informada.

3. Actuadores
Son los mecanismos mediante los cuales el agente interactúa con su entorno. En un robot, por ejemplo, los actuadores pueden ser motores o brazos robóticos. En un agente digital, pueden ser interfaces gráficas, respuestas por texto, comandos enviados a otros sistemas, etc.

4. Mecanismo de razonamiento
Este componente es el "cerebro" del agente. Toma la información captada por los sensores, la analiza y decide qué acción realizar utilizando los actuadores. Este proceso de toma de decisiones puede basarse en reglas lógicas, algoritmos de búsqueda, razonamiento probabilístico o técnicas de inteligencia artificial más avanzadas como el aprendizaje automático.

5. Sistema de aprendizaje
Permite que el agente aprenda de su experiencia. A través de técnicas de machine learning, el agente puede mejorar su rendimiento con el tiempo, adaptarse a nuevos entornos y resolver problemas más complejos. Este componente crea un bucle de retroalimentación donde el agente ajusta su comportamiento en base a los resultados obtenidos.

---

### Funcionamiento en pasos

- Sensar entorno en el que se encuentra mediante sensores propios
- Procesa los datos recibidos del analisis del entorno
- Evalua los datos teniendo en base a su programacion
- Genera varios planes de accion para llegar a un objetivo
- Selecciona el plan mas eficiente y lo ejecuta mediante actuadores
- Almacena datos de la ejecucion para tenerlos en cuenta en futuras ejecuciones.

## Características de un Agente Inteligente

Un agente inteligente cuenta con caracteristicas que definen partes de su
comportamiento.

- **Autonomía**  
   Puede actuar por su cuenta y controlar su estado interno sin necesidad de intervencion
  alguna.

- **Reactividad**  
   Analiza el entorno y responde a los cambios.

- **Proactividad**  
   Tiene objetivos propios y toma la iniciativa para cumplirlos sin ser impulsado
  por ningun evento.

- **Habilidad social**  
   Puede comunicarse con otros agentes o personas.

- **Cooperación**  
   Trabaja junto con otros agentes para alcanzar objetivos.

- **Razonamiento**  
   Puede pensar y sacar conclusiones basado en conocimientos previos.

- **Adaptación**  
   Aprende de la experiencia y mejora su comportamiento.

- **Integridad**  
   Actua de forma honesta buscando el bienestar del usuario.

---

## Clasificacion de Agentes inteligentes

Se pueden clasificar según sus capacidades:

- Agentes simples: programados para seguir reglas predefinidas en un entorno
  especifico.
- Agentes basados en modelos: tienen un estado interno que refleja elementos que
  no son visibles, este estado interno es llamado modelo de mundo y se usa para
  realizar cambios en estado actual.
- Agentes basados en objetivos: programados teniendo en cuenta las
  caracteristicas de los agentes anteriores, tienen objetivos especificos los
  cuales logran mediante distintas acciones.
- Agentes basados en el aprendizaje: utilizan tecnicas de aprendizaje para
  mejorar su toma de decisiones.
- Agentes basados en utilidades: tiene un modelo de mundo el cual utiliza junto
  a una funcion de utilidad(calcula preferencias entre estados) para poder
  seleccionar una accion que lleve al mejor estado posible.

---

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

Prolog tiene internamente un motor de inferencia, el cuál es el responsable de
aplicar reglas lógicas a un conjunto de hechos para tomar decisiones. En este
proyecto:

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
