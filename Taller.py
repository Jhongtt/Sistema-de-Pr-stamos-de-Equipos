from datetime import date

# ── Inventario inicial ───────────────────────────────────────
# Diccionario anidado: cada equipo tiene su estado y su
# historial de préstamos (lista de tuplas (usuario, fecha))
equipos = {
    "Laptop Dell": {"disponible": True,  "prestamos": []},
    "Laptop HP":   {"disponible": True,  "prestamos": []},
    "Tablet iPad": {"disponible": False, "prestamos": [("Carlos Ruiz", "2025-04-10")]},
    "Proyector":   {"disponible": True,  "prestamos": []},
}


# ── 1. Mostrar equipos ───────────────────────────────────────
def mostrar_equipos():
    """Muestra todos los equipos el estado en que estan."""
    print("\n{'='*44}")
    print(f"{'equipo':<20} {'estado':>20}")
    print("-" * 44)
    for nombre, datos in equipos.items():
        estado = "Disponible " if datos["disponible"] else "Prestado   "
        print(f"{nombre:<20} {estado:>20}")
    print("=" * 44)


# ── 2. Registrar préstamo ────────────────────────────────────
def registrar_prestamo():
    """Registra el préstamo de un equipo disponible."""
    mostrar_equipos()

    equipo = input("\nNombre exacto del equipo a prestar: ").strip()

    # Validar existencia
    if equipo not in equipos:
        print(f"   El equipo '{equipo}' no existe en el sistema.")
        return

    # Validar disponibilidad
    if not equipos[equipo]["disponible"]:
        print(f"   '{equipo}' ya está prestado. No está disponible.")
        return

    usuario = input("Nombre del usuario: ").strip()
    if not usuario:
        print("   El nombre del usuario no puede estar vacío.")
        return

    # Guardar préstamo como tupla inmutable (usuario, fecha)
    hoy = str(date.today())
    registro = (usuario, hoy)
    equipos[equipo]["prestamos"].append(registro)
    equipos[equipo]["disponible"] = False

    print(f"\n  ✔ '{equipo}' prestado a {usuario} el {hoy}.")


# ── 3. Devolver equipo ───────────────────────────────────────
def devolver_equipo():
    """Marca un equipo prestado como devuelto."""
    equipo = input("\nNombre exacto del equipo a devolver: ").strip()

    if equipo not in equipos:
        print(f"  El equipo '{equipo}' no existe en el sistema.")
        return

    if equipos[equipo]["disponible"]:
        print(f"  '{equipo}' ya está en la biblioteca, no estaba prestado.")
        return

    equipos[equipo]["disponible"] = True
    print(f"\n  '{equipo}' devuelto correctamente. Ya está disponible.")


# ── 4. Ver historial ─────────────────────────────────────────
def ver_historial():
    """Muestra el historial completo de préstamos de todos los equipos."""
    print("\n" + "=" * 44)
    print("       HISTORIAL DE PRÉSTAMOS")
    print("=" * 44)

    for nombre, datos in equipos.items():
        print(f" {nombre}")
        if datos["prestamos"]:
            for i, (usuario, fecha) in enumerate(datos["prestamos"], 1):
                print(f"   {i}. {usuario} — {fecha}")
        else:
            print("   Sin préstamos registrados.")

    print("=" * 44)


# ── 5. Agregar equipo ────────────────────────────────────────
def agregar_equipo():
    """Agrega un nuevo equipo al inventario."""
    nombre = input("\nNombre del nuevo equipo: ").strip()

    if not nombre:
        print("   El nombre no puede estar vacío.")
        return

    if nombre in equipos:
        print(f"   '{nombre}' ya existe en el inventario.")
        return

    equipos[nombre] = {"disponible": True, "prestamos": []}
    print(f"   '{nombre}' agregado al inventario correctamente.")


# ── 6. Menú principal ────────────────────────────────────────
def menu():
    """Muestra el menú interactivo y gestiona la navegación."""
    opciones = {
        "1": ("Ver equipos",               mostrar_equipos),
        "2": ("Registrar préstamo",         registrar_prestamo),
        "3": ("Devolver equipo",            devolver_equipo),
        "4": ("Ver historial de préstamos", ver_historial),
        "5": ("Agregar nuevo equipo",       agregar_equipo),
        "6": ("Salir",                      None),
    }

    while True:
        print("\n" + "=" * 44)
        print("   sistema de prestamo de equipos")
        print("=" * 44)
        for clave, (descripcion, _) in opciones.items():
            print(f"  {clave}. {descripcion}")
        print("=" * 44)

        opcion = input("Selecciona una opción: ").strip()

        if opcion not in opciones:
            print("   Opción inválida. Elige un número del 1 al 6.")
            continue

        if opcion == "6":
            print(" Hasta luego care bebe")
            break

        # Llama a la función correspondiente
        _, funcion = opciones[opcion]
        funcion()


# ── Punto de entrada ─────────────────────────────────────────
if __name__ == "__main__":
    menu()