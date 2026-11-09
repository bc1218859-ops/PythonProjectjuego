import os
import random
import time


def limpiar_pantalla():
  os.system("cls" if os.name == "nt" else "clear")


def jugar_contabilidad():
  # Variables Financieras Iniciales (Balance General)
  efectivo = 5000.0
  inventario = 2000.0
  activo_fijo = 10000.0
  pasivos_deudas = 3000.0

  patrimonio = (efectivo + inventario + activo_fijo) - pasivos_deudas
  mes = 1
  reputacion = 100
  juego_activo = True

  print("🏢 ¡BIENVENIDO A CORPORATE TYCOON: EL JUEGO CONTABLE! 🏢")
  print("Tu objetivo: Gestionar los estados financieros y hacer crecer tu empresa.")
  print("Evita que tu Efectivo o tu Reputacion lleguen a 0.")
  input("\nPresiona ENTER para iniciar tu primer mes como CFO...")

  while juego_activo and mes <= 12:
    limpiar_pantalla()

    # Calcular Patrimonio Neto actual
    patrimonio = (efectivo + inventario + activo_fijo) - pasivos_deudas

    print(f"==================================================")
    print(f" 📅 MES: {mes} / 12   |   ⭐ Reputación: {reputacion}%")
    print(f"==================================================")
    print(f" 💰 Efectivo (Liquidez): ${efectivo:,.2f}")
    print(f" 📦 Inventario (Mercancía): ${inventario:,.2f}")
    print(f" 🏭 Activos Fijos (Maquinaria/Local): ${activo_fijo:,.2f}")
    print(f" 💳 Pasivos (Deudas/Préstamos): ${pasivos_deudas:,.2f}")
    print(f" 📊 PATRIMONIO NETO (Capital): ${patrimonio:,.2f}")
    print(f"==================================================")
    print("\n¿Qué acción financiera deseas realizar este mes?")
    print(" [1] 📈 Realizar Ventas masivas (Ingresos de efectivo)")
    print(" [2] 📦 Comprar Inventario a Proveedores (Gasta efectivo)")
    print(" [3] 💳 Pagar cuota de Préstamo / Deuda")
    print(" [4] 💰 Solicitar Préstamo Bancario (Liquidez inmediata)")
    print(" [5] ⏭️ Pasar al siguiente mes (Cierre contable regular)")
    print(" [q] 🚪 Salir del juego")

    opcion = input("\nSelecciona una opción [1-5 o q]: ").strip().lower()

    if opcion == "q":
      print("¡Partida guardada y cerrada por el usuario!")
      break

    evento_extra = ""

    if opcion == "1":
      # Ventas
      if inventario < 500:
        print(
            "\n⚠️ No tienes suficiente inventario para vender. ¡Compra más"
            " mercancía!"
        )
        time.sleep(2)
        continue
      else:
        ingreso = random.randint(1500, 3500)
        costo_venta = ingreso * 0.6
        efectivo += ingreso
        inventario -= costo_venta
        beneficio = ingreso - costo_venta
        evento_extra = (
            f"✅ ¡Ventas exitosas! Ingresaron ${ingreso:,.2f} a caja."
            f" Beneficio neto: +${beneficio:,.2f}"
        )

    elif opcion == "2":
      # Comprar inventario
      gasto = 1200.0
      if efectivo >= gasto:
        efectivo -= gasto
        inventario += 1500.0  # El inventario se valora un poco más por margen comercial
        evento_extra = (
            f"✅ Compraste inventario por valor de ${gasto:,.2f} en efectivo."
        )
      else:
        print("\n❌ Efectivo insuficiente para comprar inventario.")
        time.sleep(2)
        continue

    elif opcion == "3":
      # Pagar deuda
      pago = 500.0
      if pasivos_deudas <= 0:
        print("\n🎉 ¡Felicidades! No tienes deudas pendientes.")
        time.sleep(2)
        continue
      elif efectivo >= pago:
        efectivo -= pago
        pasivos_deudas -= pago
        reputacion = min(100, reputacion + 5)
        evento_extra = (
            f"✅ Pagaste ${pago:,.2f} de tu pasivo. Tu crédito mejora."
        )
      else:
        print("\n❌ No tienes suficiente efectivo para abonar a la deuda.")
        time.sleep(2)
        continue

    elif opcion == "4":
      # Pedir préstamo
      prestamo = 3000.0
      pasivos_deudas += prestamo
      efectivo += prestamo
      evento_extra = (
          f"💰 El banco aprobó un préstamo de ${prestamo:,.2f}. Aumentó tu"
          " pasivo y liquidez."
      )

    elif opcion == "5":
      # Pasar mes (Gastos fijos de nómina, alquiler e impuestos)
      gastos_fijos = 1000.0
      efectivo -= gastos_fijos
      evento_extra = (
          f"⏳ Cierre de mes completado. Se descontaron gastos fijos (Nómina y"
          f" Alquiler): ${gastos_fijos:,.2f}"
      )

      # Eventos aleatorios corporativos
      azar = random.random()
      if azar < 0.3:
        multa = 400
        efectivo -= multa
        reputacion -= 10
        evento_extra += (
            f"\n⚠️ ¡Auditoría fiscal! Sanción por ajuste menor: -${multa}."
        )
      elif azar < 0.6:
        subsidio = 600
        efectivo += subsidio
        reputacion += 5
        evento_extra += (
            f"\n🎉 ¡Beneficio fiscal! Devolución de impuestos por +${subsidio}."
        )

      mes += 1
    else:
      print("\n❌ Opción no válida. Intenta de nuevo.")
      time.sleep(1.5)
      continue

    # Si se escoge una opción que gasta un turno de mes (como 1, 2 o 3)
    if opcion in ["1", "2", "3", "4"]:
      # Gastos operativos mensuales automáticos al realizar movimientos
      efectivo -= 300  # Costes operativos
      mes += 1

    # Verificaciones de bancarrota
    if efectivo <= 0 or reputacion <= 0:
      limpiar_pantalla()
      print(" bankrupt 💀 ¡QUIEBRA CORPORATIVA! 💀")
      print(
          "Tu empresa se ha quedado sin liquidez o su reputación llegó a cero."
      )
      print(f"Mes alcanzado: {mes} | Patrimonio final: ${patrimonio:,.2f}")
      juego_activo = False
      break

    if evento_extra:
      print(f"\n{evento_extra}")
      input("\nPresiona ENTER para continuar al siguiente reporte...")

  if mes > 12:
    limpiar_pantalla()
    print("🏆 ¡FELICIDADES! HAS COMPLETADO EL AÑO FISCAL CON ÉXITO 🏆")
    print(f"Patrimonio Neto Final: ${patrimonio:,.2f}")
    print(f"Reputación Corporativa Final: {reputacion}%")
    print("¡Has demostrado ser un maestro de la contabilidad empresarial!")


if __name__ == "__main__":
  jugar_contabilidad()