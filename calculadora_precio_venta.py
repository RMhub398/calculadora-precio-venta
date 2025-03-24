
import streamlit as st

st.set_page_config(page_title="Calculadora de Precio de Venta", layout="centered")

st.title("🧮 Calculadora de Precio de Venta - Grupo Proservices")

# Entrada de costo
costo = st.number_input("Ingresa el costo del servicio o proyecto ($)", min_value=0, step=1000, format="%d")

# Determinar el margen según tramos
if costo <= 200000:
    margen = 0.40
    tipo = "Micro"
    motivo = "Cubre costos fijos mínimos y mano de obra básica"
elif costo <= 500000:
    margen = 0.37
    tipo = "Pequeño (bajo)"
    motivo = "Proyectos simples con mayor volumen"
elif costo <= 1000000:
    margen = 0.34
    tipo = "Pequeño (medio)"
    motivo = "Equilibrio rentabilidad/competitividad"
elif costo <= 2500000:
    margen = 0.30
    tipo = "Mediano (bajo)"
    motivo = "Riesgos moderados y eficiencia"
elif costo <= 4000000:
    margen = 0.27
    tipo = "Mediano (alto)"
    motivo = "Clientes estables con margen protector"
elif costo <= 6000000:
    margen = 0.24
    tipo = "Grande (bajo)"
    motivo = "Economías de escala"
elif costo <= 8000000:
    margen = 0.21
    tipo = "Grande (alto)"
    motivo = "Clientes estratégicos"
elif costo <= 12000000:
    margen = 0.19
    tipo = "Mega"
    motivo = "Alto volumen y negociaciones"
else:
    margen = 0.17
    tipo = "Corporativo"
    motivo = "Alianzas y flujo recurrente"

# Calcular precio de venta
if costo > 0:
    precio_venta = costo / (1 - margen)
    utilidad = precio_venta - costo

    st.markdown("---")
    st.subheader("Resultado")
    st.write(f"**Margen aplicado:** {int(margen*100)}%")
    st.write(f"**Tipo de proyecto:** {tipo}")
    st.write(f"**Motivo:** {motivo}")
    st.success(f"**Precio de venta sugerido:** ${precio_venta:,.0f}")
    st.caption(f"Utilidad esperada: ${utilidad:,.0f}")
else:
    st.warning("Ingresa un valor de costo mayor a 0 para calcular el precio de venta.")
