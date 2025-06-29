from utils import cargar_estado, agregar_aprobadas, guardar_estado
from prolog_interface import puede_cursar, recomendar_materias, materias_disponibles_por_anio
from datetime import datetime

from datetime import date

INICIO_CUATRIMESTRE = date(2025, 7, 1)
INICIO_INSCRIPCION = date(2025, 7, 5)
FIN_INSCRIPCION = date(2025, 7, 10)

# hoy = date.today()
# hoy = datetime(2025, 7, 1).date() # Inicio cuatrimestre
hoy = datetime(2025, 7, 5).date() # Inicio inscripción

def chequear_inicio_cuatrimestre():
    estado = cargar_estado()

    if hoy == INICIO_CUATRIMESTRE and not estado.get("aviso_cuatrimestre_enviado", False):
        print("📢 Comienza un nuevo cuatrimestre.")
        disponibles = materias_disponibles_por_anio(estado["aprobadas"])

        if disponibles:
            print("Estas son las materias que podrías cursar:")
            for anio, materias in disponibles:
                if materias:
                    print(f"Año {anio}:")
                    for m in materias:
                        print(f"   - {m}")
        else:
            print("No hay materias disponibles por ahora.")
        estado["aviso_cuatrimestre_enviado"] = True
        guardar_estado(estado)

def chequear_inscripcion_automatica():
    estado = cargar_estado()

    if INICIO_INSCRIPCION <= hoy <= FIN_INSCRIPCION and not estado.get("inscripcion_registrada", False):
        rec = recomendar_materias(estado["aprobadas"])
        if rec:
            print("📝 El agente te inscribió automáticamente a:")
            for m in rec:
                print(f"  - {m}")
            estado["inscripcion_registrada"] = True
            guardar_estado(estado)
        else:
            print("📝 No hay materias para inscribirse este cuatrimestre.")

            



def mostrar_menu():
    print("\n--- Agente Académico ---")
    print("1. Ver materias aprobadas")
    print("2. Agregar materias aprobadas")
    print("3. Consultar si puedo cursar una materia")
    print("4. Ver materias disponibles por año")
    print("5. Ver materias recomendadas")
    print("6. Salir")

def main():
    estado = cargar_estado()

    chequear_inicio_cuatrimestre()
    chequear_inscripcion_automatica()

    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ").strip()
        estado = cargar_estado()

        if opcion == "1":
            print("Aprobadas:")
            if estado["aprobadas"]:
                for m in estado["aprobadas"]:
                    print(f"   - {m}")
            else:
                print("No tenés materias aprobadas.")

        elif opcion == "2":
            nuevas = input("Ingresá materias aprobadas (separadas por coma): ").strip().split(",")
            nuevas = [n.strip() for n in nuevas if n.strip()]
            agregar_aprobadas(nuevas)
            print("Aprobadas actualizadas.")

        elif opcion == "3":
            mat = input("Nombre de la materia: ").strip()

            print(f"Materia consultada: {mat}")
            if puede_cursar(mat, estado["aprobadas"]):
                print(f"Podés cursar {mat}")
            else:
                print(f"No podés cursar {mat} todavía.")

        elif opcion == "4":
            materias_por_anio = materias_disponibles_por_anio(estado["aprobadas"])

            if materias_por_anio:
                print("\nMaterias disponibles para cursar agrupadas por año:\n")
                for anio, materias in materias_por_anio:
                    if materias:
                        print(f"Año {anio}:")
                        for m in materias:
                            print(f"   - {m}")
            else:
                print("No hay materias disponibles para cursar.")

        elif opcion == "5":
            rec = recomendar_materias(estado["aprobadas"])
            print("Recomendadas:")
            if rec:
                for m in rec:
                    print(f"   - {m}")
            else:
                print("No hay materias recomendadas.")

        elif opcion == "6":
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()

