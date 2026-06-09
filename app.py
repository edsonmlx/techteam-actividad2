#!/usr/bin/env python3
"""
=============================================
 TECHTEAM — app.py
 Actividad #2 | Backend Python
 Edson Mamani Laura & Jose Ventura Poma
=============================================
"""

# --- Lista del equipo del proyecto ---
EQUIPO = [
    {"nombre": "Edson Mamani Laura",  "rol": "Líder del Proyecto",  "rama": "feature/ENCABEZADO"},
    {"nombre": "Jose Ventura Poma",   "rol": "Colaborador 1",       "rama": "feature/CUERPO"},
    {"nombre": "Angel vargas Mamani",   "rol": "Colaborador 2",       "rama": "app.py"},
]


def bienvenida(nombre: str) -> str:
    """Retorna un saludo personalizado."""
    return f"Hola, {nombre}!"


def mostrar_equipo() -> None:
    """Imprime los integrantes del equipo con su información."""
    print("\n" + "=" * 45)
    print("  TECHTEAM — Actividad #2")
    print("=" * 45)
    for miembro in EQUIPO:
        print(f"\n  👤 {miembro['nombre']}")
        print(f"     Rol   : {miembro['rol']}")
        print(f"     Rama  : {miembro['rama']}")
        print(f"     Rama  : {miembro['rama']}")
    print("\n" + "=" * 45)


def calcular_estadisticas(nombres: list) -> dict:
    """
    Calcula estadísticas básicas de una lista de nombres.
    Retorna un diccionario con total, promedio de longitud, etc.
    """
    if not nombres:
        return {"total": 0, "promedio_longitud": 0.0, "mas_largo": "", "mas_corto": ""}

    longitudes = [len(n) for n in nombres]
    return {
        "total":             len(nombres),
        "promedio_longitud": round(sum(longitudes) / len(longitudes), 2),
        "mas_largo":         max(nombres, key=len),
        "mas_corto":         min(nombres, key=len),
    }


def saludar_a_todos() -> None:
    """Saluda a cada integrante del equipo."""
    print("\n  Saludos del equipo:\n")
    for miembro in EQUIPO:
        print(f"  → {bienvenida(miembro['nombre'])}")


def menu_interactivo() -> None:
    """Menú de consola para interactuar con el proyecto."""
    while True:
        print("\n  ¿Qué deseas hacer?")
        print("  [1] Ver equipo del proyecto")
        print("  [2] Saludar a todos")
        print("  [3] Saludar a alguien")
        print("  [4] Estadísticas de nombres")
        print("  [0] Salir")
        opcion = input("\n  Opción: ").strip()

        if opcion == "1":
            mostrar_equipo()
        elif opcion == "2":
            saludar_a_todos()
        elif opcion == "3":
            nombre = input("  Tu nombre: ").strip()
            if nombre:
                print(f"\n  {bienvenida(nombre)}")
            else:
                print("  ⚠ Debes ingresar un nombre.")
        elif opcion == "4":
            nombres = [m["nombre"] for m in EQUIPO]
            stats   = calcular_estadisticas(nombres)
            print(f"\n  Total de integrantes : {stats['total']}")
            print(f"  Promedio de longitud : {stats['promedio_longitud']} caracteres")
            print(f"  Nombre más largo     : {stats['mas_largo']}")
            print(f"  Nombre más corto     : {stats['mas_corto']}")
        elif opcion == "0":
            print("\n  ¡Hasta luego! — TechTeam 👋\n")
            break
        else:
            print("  ⚠ Opción no válida.")


# --- Punto de entrada ---
if __name__ == "__main__":
    mostrar_equipo()
    saludar_a_todos()
    menu_interactivo()
