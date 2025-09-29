

import datetime
import sys

FORMATO_FECHA = "%d/%m/%Y"
fecha_actual = datetime.datetime.now().date()

clientes = {}  # clave: [apellidos, nombre]
salas = {}     # clave: [nombre, cupo]
reservas = {}  # folio: {cliente, sala, fecha, turno, evento}
disponibilidad = {}  # (sala, fecha, turno): folio

def generar_folio():
    return max(reservas.keys(), default=1000) + 1

def mostrar_clientes():
    if not clientes:
        print("Todavía no hay clientes registrados.")
        return False
    else:
        print("CLAVE\tAPELLIDO\tNOMBRE")
        print("-" * 40)
        for clave, datos in sorted(clientes.items(), key=lambda item: (item[1][0], item[1][1])):
            print(f"{clave:<8}{datos[0]:<16}{datos[1]}")
        return True

def mostrar_salas_disponibles(fecha, turno):
    disponibles = []
    print("CLAVE\tNOMBRE\t\tCUPO")
    print("-" * 40)
    for clave, (nombre, cupo) in salas.items():
        if (clave, fecha, turno) not in disponibilidad:
            print(f"{clave:<8}{nombre:<16}{cupo}")
            disponibles.append(clave)
    return disponibles
#Opcion 1
def reservacion():
    try:
        if not mostrar_clientes():
            return
        while True:
            clave_cliente = input("Dime tu clave de cliente (enter para salir): ").strip()
            if clave_cliente == "":
                print("Saliendo...\n")
                return
            if not clave_cliente.isdigit() or int(clave_cliente) not in clientes:
                print("Clave inválida. Intenta de nuevo.")
                mostrar_clientes()
                continue
            clave_cliente = int(clave_cliente)
            break

        while True:
            fecha_str = input("Fecha de reservación (dd/mm/aaaa): ").strip()
            try:
                fecha = datetime.datetime.strptime(fecha_str, FORMATO_FECHA).date()
                if (fecha - fecha_actual).days < 2:
                    print("La fecha debe ser al menos dos días después de hoy.")
                    continue
                break
            except ValueError:
                print("Formato de fecha incorrecto.")
                continue
            except Exception:
                print(f"Ocurrió un problema: {sys.exc_info()[0:2]}")
                continue

        turnos = ["Mañana", "Tarde", "Noche"]
        print("Turnos disponibles: 1) Mañana 2) Tarde 3) Noche")
        while True:
            turno_op = input("Selecciona turno (1-3): ").strip()
            if turno_op not in ["1", "2", "3"]:
                print("Turno inválido.")
                continue
            turno = turnos[int(turno_op)-1]
            break

        disponibles = mostrar_salas_disponibles(fecha, turno)
        if not disponibles:
            print("No hay salas disponibles para ese turno y fecha.")
            return
        while True:
            clave_sala = input("Clave de sala a reservar: ").strip()
            if not clave_sala.isdigit() or int(clave_sala) not in disponibles:
                print("Clave de sala inválida.")
                continue
            clave_sala = int(clave_sala)
            break

        while True:
            evento = input("Nombre del evento: ").strip()
            if not evento or evento.isspace():
                print("El nombre del evento no puede estar vacío.")
                continue
            break

        folio = generar_folio()
        reservas[folio] = {
            "cliente": clave_cliente,
            "sala": clave_sala,
            "fecha": fecha,
            "turno": turno,
            "evento": evento
        }
        disponibilidad[(clave_sala, fecha, turno)] = folio
        print(f"Reservación registrada con folio: {folio}")
    except ValueError:
        print("Hubo un error al intentar ingresar un valor incorrecto")
        return
    except Exception:
        print(f"Error en reservación: {sys.exc_info()[0:2]} ")

#Opcion 2
def editar_reservacion():
    try:
        print("Editar nombre de evento de una reservación.")
        fecha_ini = input("Fecha inicial (dd/mm/aaaa): ").strip()
        fecha_fin = input("Fecha final (dd/mm/aaaa): ").strip()
        try:
            f_ini = datetime.datetime.strptime(fecha_ini, FORMATO_FECHA).date()
            f_fin = datetime.datetime.strptime(fecha_fin, FORMATO_FECHA).date()
        except ValueError:
            print("Formato de fecha incorrecto.")
            return
        eventos = {folio: datos for folio, datos in reservas.items() if f_ini <= datos["fecha"] <= f_fin}
        if not eventos:
            print("No hay eventos en ese rango.")
            return
        print("FOLIO\tFECHA\t\tEVENTO")
        print("-" * 40)
        for folio, datos in eventos.items():
            print(f"{folio}\t{datos['fecha'].strftime(FORMATO_FECHA)}\t{datos['evento']}")
        while True:
            folio_sel = input("Folio a editar (enter para cancelar): ").strip()
            if folio_sel == "":
                print("Cancelado.")
                return
            if not folio_sel.isdigit() or int(folio_sel) not in eventos:
                print("Folio inválido.")
                continue
            folio_sel = int(folio_sel)
            break
        while True:
            nuevo_evento = input("Nuevo nombre del evento: ").strip()
            if not nuevo_evento or nuevo_evento.isspace():
                print("El nombre del evento no puede estar vacío.")
                continue
            reservas[folio_sel]["evento"] = nuevo_evento
            print("Evento actualizado.")
            break
    except Exception:
        print(f"Error al editar reservación: {sys.exc_info()[0:2]} ")

#Opcion 3
def consultar_reservaciones():
    try:
        fecha_str = input("Fecha a consultar (dd/mm/aaaa): ").strip()
        try:
            fecha = datetime.datetime.strptime(fecha_str, FORMATO_FECHA).date()
        except ValueError:
            print("Formato de fecha incorrecto.")
            return
        print("FOLIO\tSALA\tTURNO\tEVENTO\tCLIENTE")
        print("-" * 60)
        for folio, datos in reservas.items():
            if datos["fecha"] == fecha:
                sala = salas[datos["sala"]][0]
                cliente = ([datos["cliente"]][::-1])
                print(f"{folio}\t{sala}\t{datos['turno']}\t{datos['evento']}\t{cliente}")
    except Exception:
        print(f"Error al consultar reservaciones: {sys.exc_info()[0:2]} ")

#Opcion 4
def new_cliente():
    try:
        clave = max(clientes.keys(), default=100) + 1
        nombre = input("Nombre: ").strip()
        apellidos = input("Apellidos: ").strip()
        if not (nombre.isalpha() or apellidos.isalpha()):
            print("Nombre y apellidos deben contener solo letras.")
            return
        clientes[clave] = [apellidos, nombre]
    except Exception:
        print(f"Error al registrar cliente: {sys.exc_info()[0:2]}")
    else:
        print(f"Cliente registrado con clave: {clave}")

#Opcion 5
def new_sala():
    try:
        clave = max(salas.keys(), default=0) + 1
        nombre = input("Nombre de la sala: ").strip()
        cupo = input("Capacidad de la sala: ").strip()
        if not cupo.isdigit() or int(cupo) <= 0:
            print("El cupo debe ser un número entero positivo.")
            return
        if not nombre.isalpha():
            print("El nombre de la sala debe contener solo letras.")
            return
        salas[clave] = [nombre, int(cupo)]
    except ValueError:
        print("El cupo debe ser un numero entero positivo")
        return
    except Exception:
        print(f"Error al registrar sala: {sys.exc_info()[0:2]}")
    else:
        print(f"Sala registrada con clave: {clave}")

def main():
    while True:
        print("\n--- MENÚ ---")
        print("[1] Registrar reservación")
        print("[2] Editar reservación")
        print("[3] Consultar reservaciones")
        print("[4] Registrar cliente")
        print("[5] Registrar sala")
        print("[6] Salir")
        try:
            op = input("Elige una opción: ").strip()
            if op == "1":
                reservacion()
            elif op == "2":
                editar_reservacion()
            elif op == "3":
                consultar_reservaciones()
            elif op == "4":
                new_cliente()
            elif op == "5":
                new_sala()
            elif op == "6":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida.")
        except ValueError:
            print("La opcion proporcionada no es valida, intente de nuevo...")
            continue
        except Exception:
            print(f"Ocurrió un problema en new_sala: {sys.exc_info()[0:2]}")
            continue


if __name__ == "__main__":
    main()