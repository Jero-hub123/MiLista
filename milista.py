import streamlit as st

# ── Configuración de página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="MILista",
    page_icon="🛒",
    layout="centered",
)

# ── Estilos personalizados ───────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Nunito', sans-serif;
    }

    .main-title {
        font-size: 3rem;
        font-weight: 900;
        color: #1a1a2e;
        letter-spacing: -1px;
        margin-bottom: 0;
    }

    .subtitle {
        color: #6b7280;
        font-size: 1rem;
        margin-top: 0;
        margin-bottom: 2rem;
    }

    .category-header {
        background: linear-gradient(90deg, #f0fdf4, #ffffff);
        border-left: 4px solid #22c55e;
        padding: 8px 14px;
        border-radius: 0 8px 8px 0;
        font-weight: 700;
        font-size: 1rem;
        color: #15803d;
        margin: 1.2rem 0 0.5rem 0;
    }

    .item-row {
        display: flex;
        justify-content: space-between;
        padding: 5px 14px;
        border-bottom: 1px solid #f3f4f6;
        font-size: 0.93rem;
        color: #374151;
    }

    .item-row:last-child {
        border-bottom: none;
    }

    .item-qty {
        color: #9ca3af;
        font-size: 0.85rem;
    }

    .tip-box {
        background: #f0f9ff;
        border: 1px solid #bae6fd;
        border-radius: 12px;
        padding: 14px 18px;
        margin-top: 1rem;
    }

    .tip-box p {
        margin: 4px 0;
        color: #0369a1;
        font-size: 0.9rem;
    }

    .stButton > button {
        background: linear-gradient(135deg, #22c55e, #16a34a);
        color: white;
        font-weight: 700;
        font-size: 1.1rem;
        border: none;
        border-radius: 12px;
        padding: 0.7rem 2rem;
        width: 100%;
        cursor: pointer;
        transition: opacity 0.2s;
    }

    .stButton > button:hover {
        opacity: 0.9;
    }

    div[data-testid="metric-container"] {
        background: #f9fafb;
        border-radius: 12px;
        padding: 12px 16px;
        border: 1px solid #e5e7eb;
    }
</style>
""", unsafe_allow_html=True)


# ── Base de datos de productos (precios en pesos uruguayos) ──────────────────
PRODUCTOS_BASE = {
    "🥦 Frutas y verduras": [
        {"nombre": "Tomate", "unidad": "kg", "base": 0.5, "precio": 90, "tag": []},
        {"nombre": "Lechuga", "unidad": "unidad", "base": 0.5, "precio": 50, "tag": []},
        {"nombre": "Zanahoria", "unidad": "kg", "base": 0.3, "precio": 60, "tag": []},
        {"nombre": "Manzana", "unidad": "kg", "base": 0.5, "precio": 90, "tag": []},
        {"nombre": "Banana", "unidad": "kg", "base": 0.5, "precio": 60, "tag": []},
        {"nombre": "Papa", "unidad": "kg", "base": 0.5, "precio": 55, "tag": []},
        {"nombre": "Cebolla", "unidad": "kg", "base": 0.3, "precio": 50, "tag": []},
    ],
    "🥩 Proteínas": [
        {"nombre": "Pechuga de pollo", "unidad": "kg", "base": 0.3, "precio": 380, "tag": []},
        {"nombre": "Carne picada", "unidad": "kg", "base": 0.25, "precio": 520, "tag": []},
        {"nombre": "Huevos", "unidad": "docena", "base": 0.5, "precio": 260, "tag": []},
        {"nombre": "Atún en lata", "unidad": "lata", "base": 0.5, "precio": 130, "tag": []},
    ],
    "🥛 Lácteos": [
        {"nombre": "Leche entera", "unidad": "litro", "base": 1, "precio": 90, "tag": ["lactosa"]},
        {"nombre": "Yogur", "unidad": "unidad", "base": 1, "precio": 75, "tag": ["lactosa"]},
        {"nombre": "Queso fresco", "unidad": "200g", "base": 0.5, "precio": 180, "tag": ["lactosa"]},
        {"nombre": "Leche sin lactosa", "unidad": "litro", "base": 1, "precio": 130, "tag": ["sin_lactosa"]},
        {"nombre": "Yogur sin lactosa", "unidad": "unidad", "base": 1, "precio": 110, "tag": ["sin_lactosa"]},
    ],
    "🛒 Almacén": [
        {"nombre": "Arroz", "unidad": "kg", "base": 0.4, "precio": 95, "tag": []},
        {"nombre": "Fideos (trigo)", "unidad": "paquete", "base": 0.5, "precio": 95, "tag": ["gluten"]},
        {"nombre": "Fideos sin TACC", "unidad": "paquete", "base": 0.5, "precio": 180, "tag": ["sin_gluten"]},
        {"nombre": "Aceite girasol", "unidad": "litro", "base": 0.25, "precio": 190, "tag": []},
        {"nombre": "Sal fina", "unidad": "kg", "base": 0.1, "precio": 45, "tag": []},
        {"nombre": "Azúcar", "unidad": "kg", "base": 0.2, "precio": 60, "tag": []},
        {"nombre": "Pan lactal", "unidad": "paquete", "base": 0.3, "precio": 140, "tag": ["gluten"]},
        {"nombre": "Pan sin TACC", "unidad": "paquete", "base": 0.3, "precio": 260, "tag": ["sin_gluten"]},
        {"nombre": "Lentejas", "unidad": "kg", "base": 0.2, "precio": 130, "tag": []},
    ],
}

TIPS = {
    "Ahorrar dinero": [
        "🏷️ Comprá marcas propias del supermercado, suelen ser igual de buenas.",
        "📅 Planificá el menú de la semana antes de ir al super para evitar compras impulsivas.",
        "🔖 Aprovechá las ofertas de productos no perecederos (arroz, fideos, aceite).",
        "🥚 Los huevos y las legumbres son proteínas económicas y nutritivas.",
    ],
    "Comer más saludable": [
        "🥗 Intentá que la mitad del plato siempre sea verduras o ensalada.",
        "💧 Reemplazá las bebidas azucaradas por agua o infusiones sin azúcar.",
        "🍗 Preferí proteínas magras: pollo, pavo, legumbres y huevo.",
        "🌾 Elegí versiones integrales de arroz, fideos y pan cuando sea posible.",
    ],
    "Equilibrado": [
        "⚖️ Variá las proteínas durante la semana: pollo, carne, huevos y legumbres.",
        "🥦 Incluí al menos 2 frutas y 2 verduras diferentes por día.",
        "🛒 Comprá lo justo para la semana para reducir el desperdicio de alimentos.",
        "🍽️ Un presupuesto equilibrado también te permite darte algún gustito ocasional.",
    ],
}


# ── Lógica principal ─────────────────────────────────────────────────────────
def calcular_multiplicador(personas_grupo):
    return {"1-2 personas": 1.0, "3-4 personas": 2.0, "5+ personas": 3.2}[personas_grupo]


def filtrar_productos(restriccion):
    excluir = []
    incluir_extra = []
    if restriccion == "Sin gluten":
        excluir = ["gluten"]
        incluir_extra = ["sin_gluten"]
    elif restriccion == "Sin lactosa":
        excluir = ["lactosa"]
        incluir_extra = ["sin_lactosa"]

    resultado = {}
    for categoria, items in PRODUCTOS_BASE.items():
        filtrados = []
        for item in items:
            tags = item["tag"]
            if any(t in tags for t in excluir):
                continue
            if tags and all(t in ["sin_gluten", "sin_lactosa"] for t in tags):
                if not any(t in incluir_extra for t in tags):
                    continue
            filtrados.append(item)
        if filtrados:
            resultado[categoria] = filtrados
    return resultado


def generar_lista(personas_grupo, presupuesto, restriccion, objetivo):
    mult = calcular_multiplicador(personas_grupo)
    productos = filtrar_productos(restriccion)

    lista_final = {}
    costo_total = 0

    for categoria, items in productos.items():
        lista_final[categoria] = []
        for item in items:
            cantidad = round(item["base"] * mult, 2)
            costo_item = round(cantidad * item["precio"], 0)
            lista_final[categoria].append({
                "nombre": item["nombre"],
                "cantidad": cantidad,
                "unidad": item["unidad"],
                "costo": costo_item,
            })
            costo_total += costo_item

    return lista_final, round(costo_total, 0)


# ── UI ───────────────────────────────────────────────────────────────────────
st.markdown('<p class="main-title">🛒 MILista</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Tu lista de supermercado semanal, lista en segundos.</p>', unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns(2)
with col1:
    personas = st.selectbox("👨‍👩‍👧 Personas en el hogar", ["1-2 personas", "3-4 personas", "5+ personas"])
    restriccion = st.selectbox("🚫 Restricción alimenticia", ["Ninguna", "Sin gluten", "Sin lactosa"])
with col2:
    presupuesto = st.number_input("💰 Presupuesto semanal ($U)", min_value=500, max_value=100000, value=5000, step=500)
    objetivo = st.selectbox("🎯 Objetivo", ["Equilibrado", "Ahorrar dinero", "Comer más saludable"])

st.markdown("")
generar = st.button("✨ Generar Lista")

# ── Resultado ────────────────────────────────────────────────────────────────
if generar:
    lista, costo_estimado = generar_lista(personas, presupuesto, restriccion, objetivo)
    diferencia = presupuesto - costo_estimado

    st.divider()
    st.subheader("📊 Resumen financiero")

    m1, m2, m3 = st.columns(3)
    m1.metric("💳 Presupuesto", f"$U {presupuesto:,.0f}")
    m2.metric("🧾 Costo estimado", f"$U {costo_estimado:,.0f}")
    if diferencia >= 0:
        m3.metric("✅ Te sobra", f"$U {diferencia:,.0f}", delta=f"+$U {diferencia:,.0f}")
    else:
        m3.metric("⚠️ Te falta", f"$U {abs(diferencia):,.0f}", delta=f"-$U {abs(diferencia):,.0f}", delta_color="inverse")

    if diferencia < 0:
        st.warning(f"⚠️ Tu presupuesto no alcanza para cubrir la lista estimada. Te recomendamos revisar algunas categorías o ajustar las cantidades.")

    st.divider()
    st.subheader("📋 Tu lista de compras")

    for categoria, items in lista.items():
        st.markdown(f'<div class="category-header">{categoria}</div>', unsafe_allow_html=True)
        for item in items:
            st.markdown(
                f'<div class="item-row">'
                f'<span>{"✓"} {item["nombre"]}</span>'
                f'<span class="item-qty">{item["cantidad"]} {item["unidad"]} · <b>$U {item["costo"]:,.0f}</b></span>'
                f'</div>',
                unsafe_allow_html=True,
            )

    st.divider()
    st.subheader(f"💡 Recomendaciones para: {objetivo}")
    tips = TIPS.get(objetivo, [])
    tip_html = "".join(f"<p>{'  '}{t}</p>" for t in tips)
    st.markdown(f'<div class="tip-box">{tip_html}</div>', unsafe_allow_html=True)

    st.markdown("")
    st.caption("_Los precios son estimados de referencia basados en datos del SIPC Uruguay y pueden variar según el supermercado._")