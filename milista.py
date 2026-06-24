import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="MILista",
    page_icon="🛒",
    layout="centered",
)

if "historial" not in st.session_state:
    st.session_state.historial = []

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #e8f5f0 !important;
        color: #0f172a !important;
    }

    .stApp {
        background-color: #e8f5f0 !important;
    }

    .block-container {
        padding-top: 2rem;
        max-width: 720px;
        background-color: #e8f5f0 !important;
    }

    .milista-header {
        background: #1D9E75;
        border-radius: 14px;
        padding: 18px 24px;
        margin-bottom: 6px;
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .milista-title {
        font-size: 26px;
        font-weight: 600;
        color: #ffffff;
        margin: 0;
        letter-spacing: -0.5px;
    }

    .milista-subtitle {
        color: #2d6a4f;
        font-size: 14px;
        margin: 0 0 2rem 0;
        font-weight: 500;
    }

    p, label, span, div {
        color: #0f172a;
    }

    /* Inputs blancos sobre fondo verde */
    .stSelectbox > div > div,
    .stNumberInput > div > div > input {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #b7dfc9 !important;
        border-radius: 10px !important;
    }

    .stSelectbox svg {
        fill: #1D9E75 !important;
    }

    .stNumberInput button {
        background: #ffffff !important;
        color: #1D9E75 !important;
        border: 1px solid #b7dfc9 !important;
    }

    label, .stSelectbox label, .stNumberInput label {
        color: #0f172a !important;
        font-size: 13px !important;
        font-weight: 600 !important;
    }

    .stButton > button {
        background: #1D9E75 !important;
        color: white !important;
        font-weight: 500 !important;
        font-size: 15px !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 2rem !important;
        width: 100% !important;
    }

    .stButton > button:hover {
        background: #0F6E56 !important;
        color: white !important;
    }

    .metric-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        border: 1px solid #b7dfc9;
    }

    .metric-label {
        font-size: 11px;
        color: #2d6a4f;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 4px;
    }

    .metric-value {
        font-size: 22px;
        font-weight: 700;
        color: #0f172a;
    }

    .metric-card-green {
        background: #1D9E75;
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        border: none;
    }

    .metric-label-green {
        font-size: 11px;
        color: #d4f5e9;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 4px;
    }

    .metric-value-green {
        font-size: 22px;
        font-weight: 700;
        color: #ffffff;
    }

    .metric-card-red {
        background: #ffffff;
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        border: 1px solid #fca5a5;
    }

    .metric-label-red {
        font-size: 11px;
        color: #b91c1c;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 4px;
    }

    .metric-value-red {
        font-size: 22px;
        font-weight: 700;
        color: #b91c1c;
    }

    .category-header {
        background: #1D9E75;
        padding: 10px 16px;
        border-radius: 10px 10px 0 0;
        font-weight: 600;
        font-size: 13px;
        color: #ffffff;
        margin: 1rem 0 0 0;
    }

    .product-list {
        background: #ffffff;
        border: 1px solid #b7dfc9;
        border-radius: 0 0 12px 12px;
        overflow: hidden;
        margin-bottom: 12px;
    }

    .product-row {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 10px 16px;
        border-bottom: 1px solid #f1f5f9;
        font-size: 14px;
    }

    .product-row:last-child {
        border-bottom: none;
    }

    .product-check {
        color: #1D9E75;
        font-weight: 700;
        font-size: 15px;
        flex-shrink: 0;
    }

    .product-name-text {
        flex: 1;
        color: #1e293b;
        font-size: 14px;
    }

    .product-meta {
        color: #94a3b8;
        font-size: 12px;
        min-width: 70px;
        text-align: right;
    }

    .product-price-text {
        font-weight: 600;
        font-size: 13px;
        color: #0f172a;
        min-width: 70px;
        text-align: right;
    }

    .rec-box {
        background: #ffffff;
        border: 1px solid #b7dfc9;
        border-radius: 12px;
        padding: 18px 20px;
        margin-top: 1.5rem;
    }

    .rec-title {
        font-size: 14px;
        font-weight: 700;
        color: #0F6E56;
        margin-bottom: 12px;
    }

    .rec-item {
        font-size: 13px;
        color: #1e293b;
        margin-bottom: 8px;
        line-height: 1.6;
    }

    .badge-green {
        background: #e8f5f0;
        color: #0F6E56;
        font-size: 11px;
        font-weight: 500;
        padding: 3px 10px;
        border-radius: 999px;
    }

    .badge-blue {
        background: #eff6ff;
        color: #1d4ed8;
        font-size: 11px;
        font-weight: 500;
        padding: 3px 10px;
        border-radius: 999px;
    }

    .section-title {
        font-size: 15px;
        font-weight: 700;
        color: #0f172a;
        margin: 1.5rem 0 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)


PRODUCTOS_BASE = {
    "🥦 Frutas y verduras": [
        {"nombre": "Tomate", "unidad": "kg", "base": 0.5, "precio": 90, "tag": [], "costo_relativo": "bajo", "saludable": True},
        {"nombre": "Lechuga", "unidad": "unidad", "base": 0.5, "precio": 50, "tag": [], "costo_relativo": "bajo", "saludable": True},
        {"nombre": "Zanahoria", "unidad": "kg", "base": 0.3, "precio": 60, "tag": [], "costo_relativo": "bajo", "saludable": True},
        {"nombre": "Manzana", "unidad": "kg", "base": 0.5, "precio": 90, "tag": [], "costo_relativo": "bajo", "saludable": True},
        {"nombre": "Banana", "unidad": "kg", "base": 0.5, "precio": 60, "tag": [], "costo_relativo": "bajo", "saludable": True},
        {"nombre": "Papa", "unidad": "kg", "base": 0.5, "precio": 55, "tag": [], "costo_relativo": "bajo", "saludable": True},
        {"nombre": "Cebolla", "unidad": "kg", "base": 0.3, "precio": 50, "tag": [], "costo_relativo": "bajo", "saludable": True},
        {"nombre": "Espinaca", "unidad": "atado", "base": 0.5, "precio": 65, "tag": [], "costo_relativo": "bajo", "saludable": True},
        {"nombre": "Brócoli", "unidad": "kg", "base": 0.3, "precio": 95, "tag": [], "costo_relativo": "bajo", "saludable": True},
        {"nombre": "Naranja", "unidad": "kg", "base": 0.4, "precio": 70, "tag": [], "costo_relativo": "bajo", "saludable": True},
    ],
    "🥩 Proteínas": [
        {"nombre": "Pechuga de pollo", "unidad": "kg", "base": 0.3, "precio": 380, "tag": [], "costo_relativo": "medio", "saludable": True},
        {"nombre": "Carne picada", "unidad": "kg", "base": 0.25, "precio": 520, "tag": [], "costo_relativo": "alto", "saludable": False},
        {"nombre": "Huevos", "unidad": "docena", "base": 0.5, "precio": 260, "tag": [], "costo_relativo": "bajo", "saludable": True},
        {"nombre": "Atún en lata", "unidad": "lata", "base": 0.5, "precio": 130, "tag": [], "costo_relativo": "bajo", "saludable": True},
        {"nombre": "Lentejas", "unidad": "kg", "base": 0.2, "precio": 130, "tag": [], "costo_relativo": "bajo", "saludable": True},
        {"nombre": "Garbanzos", "unidad": "kg", "base": 0.2, "precio": 140, "tag": [], "costo_relativo": "bajo", "saludable": True},
        {"nombre": "Merluza", "unidad": "kg", "base": 0.25, "precio": 310, "tag": [], "costo_relativo": "medio", "saludable": True},
    ],
    "🥛 Lácteos": [
        {"nombre": "Leche entera", "unidad": "litro", "base": 1, "precio": 90, "tag": ["lactosa"], "costo_relativo": "bajo", "saludable": True},
        {"nombre": "Yogur", "unidad": "unidad", "base": 1, "precio": 75, "tag": ["lactosa"], "costo_relativo": "bajo", "saludable": True},
        {"nombre": "Queso fresco", "unidad": "200g", "base": 0.5, "precio": 180, "tag": ["lactosa"], "costo_relativo": "medio", "saludable": False},
        {"nombre": "Leche sin lactosa", "unidad": "litro", "base": 1, "precio": 130, "tag": ["sin_lactosa"], "costo_relativo": "medio", "saludable": True},
        {"nombre": "Yogur sin lactosa", "unidad": "unidad", "base": 1, "precio": 110, "tag": ["sin_lactosa"], "costo_relativo": "medio", "saludable": True},
    ],
    "🛒 Almacén": [
        {"nombre": "Arroz", "unidad": "kg", "base": 0.4, "precio": 95, "tag": [], "costo_relativo": "bajo", "saludable": True},
        {"nombre": "Fideos (trigo)", "unidad": "paquete", "base": 0.5, "precio": 95, "tag": ["gluten"], "costo_relativo": "bajo", "saludable": False},
        {"nombre": "Fideos sin TACC", "unidad": "paquete", "base": 0.5, "precio": 180, "tag": ["sin_gluten"], "costo_relativo": "medio", "saludable": False},
        {"nombre": "Aceite girasol", "unidad": "litro", "base": 0.25, "precio": 190, "tag": [], "costo_relativo": "medio", "saludable": False},
        {"nombre": "Sal fina", "unidad": "kg", "base": 0.1, "precio": 45, "tag": [], "costo_relativo": "bajo", "saludable": True},
        {"nombre": "Azúcar", "unidad": "kg", "base": 0.2, "precio": 60, "tag": [], "costo_relativo": "bajo", "saludable": False},
        {"nombre": "Pan lactal", "unidad": "paquete", "base": 0.3, "precio": 140, "tag": ["gluten"], "costo_relativo": "bajo", "saludable": False},
        {"nombre": "Pan sin TACC", "unidad": "paquete", "base": 0.3, "precio": 260, "tag": ["sin_gluten"], "costo_relativo": "medio", "saludable": False},
        {"nombre": "Avena", "unidad": "kg", "base": 0.2, "precio": 110, "tag": [], "costo_relativo": "bajo", "saludable": True},
        {"nombre": "Aceite de oliva", "unidad": "500ml", "base": 0.1, "precio": 280, "tag": [], "costo_relativo": "alto", "saludable": True},
    ],
    "🧴 Limpieza e higiene": [
        {"nombre": "Jabón de manos", "unidad": "unidad", "base": 0.3, "precio": 95, "tag": [], "costo_relativo": "bajo", "saludable": True},
        {"nombre": "Detergente", "unidad": "unidad", "base": 0.3, "precio": 120, "tag": [], "costo_relativo": "bajo", "saludable": True},
        {"nombre": "Papel higiénico", "unidad": "paquete x4", "base": 0.5, "precio": 160, "tag": [], "costo_relativo": "bajo", "saludable": True},
        {"nombre": "Shampoo", "unidad": "unidad", "base": 0.2, "precio": 210, "tag": [], "costo_relativo": "medio", "saludable": True},
    ],
}


def agente_perfil(personas_grupo, presupuesto, restriccion, objetivo):
    mult = {"1-2 personas": 1.0, "3-4 personas": 2.0, "5+ personas": 3.2}[personas_grupo]
    n_personas = {"1-2 personas": "1 a 2", "3-4 personas": "3 a 4", "5+ personas": "5 o más"}[personas_grupo]
    return {"multiplicador": mult, "n_personas": n_personas, "presupuesto": presupuesto, "restriccion": restriccion, "objetivo": objetivo}


def agente_restricciones(restriccion):
    excluir, incluir_extra = [], []
    if restriccion == "Sin gluten":
        excluir, incluir_extra = ["gluten"], ["sin_gluten"]
    elif restriccion == "Sin lactosa":
        excluir, incluir_extra = ["lactosa"], ["sin_lactosa"]

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


def agente_nutricional(productos_filtrados, perfil):
    mult = perfil["multiplicador"]
    objetivo = perfil["objetivo"]
    lista = {}
    for categoria, items in productos_filtrados.items():
        lista[categoria] = []
        for item in items:
            if objetivo == "Ahorrar dinero" and item["costo_relativo"] == "alto":
                continue
            if objetivo == "Comer más saludable" and not item["saludable"] and item["costo_relativo"] != "bajo":
                continue
            cantidad = round(item["base"] * mult, 2)
            if objetivo == "Comer más saludable" and item["saludable"]:
                cantidad = round(cantidad * 1.15, 2)
            elif objetivo == "Ahorrar dinero" and item["costo_relativo"] == "bajo":
                cantidad = round(cantidad * 1.1, 2)
            lista[categoria].append({
                "nombre": item["nombre"],
                "cantidad": cantidad,
                "unidad": item["unidad"],
                "costo": round(cantidad * item["precio"], 0),
                "saludable": item["saludable"],
                "costo_relativo": item["costo_relativo"],
            })
        if not lista[categoria]:
            del lista[categoria]
    return lista


def agente_presupuesto(lista, perfil):
    presupuesto = perfil["presupuesto"]
    costo_total = sum(item["costo"] for cat in lista.values() for item in cat)
    ajustada = False
    if costo_total > presupuesto:
        for categoria in lista:
            for item in lista[categoria]:
                if item["costo_relativo"] == "alto" or not item["saludable"]:
                    factor = 0.8
                    item["costo"] = round(item["costo"] * factor, 0)
                    item["cantidad"] = round(item["cantidad"] * factor, 2)
        costo_total = sum(item["costo"] for cat in lista.values() for item in cat)
        ajustada = True
    return lista, round(costo_total, 0), ajustada


def agente_recomendador(perfil, costo_total, lista):
    objetivo = perfil["objetivo"]
    n_personas = perfil["n_personas"]
    presupuesto = perfil["presupuesto"]
    restriccion = perfil["restriccion"]
    diferencia = presupuesto - costo_total
    recs = []

    if diferencia >= 0:
        pct = round((costo_total / presupuesto) * 100)
        recs.append(f"💰 Tu lista usa el {pct}% del presupuesto ($U {costo_total:,.0f} de $U {presupuesto:,.0f}). Con los $U {diferencia:,.0f} restantes podés comprar extras o guardarlos.")
    else:
        recs.append(f"⚠️ Tu lista supera el presupuesto por $U {abs(diferencia):,.0f}. Ajustamos las cantidades automáticamente.")

    if objetivo == "Ahorrar dinero":
        recs.append(f"🏷️ Para {n_personas} personas, huevos, lentejas y atún son tu mejor opción: proteína completa a menos de un tercio del precio de la carne.")
        recs.append(f"📅 Con $U {presupuesto:,.0f}, cocinar en cantidad los domingos evita compras impulsivas durante la semana.")
    elif objetivo == "Comer más saludable":
        recs.append(f"🥗 Aumentamos un 15% verduras y proteínas magras. Para {n_personas} personas, intentá que la mitad del plato siempre sea verdura.")
        recs.append("💧 Reemplazá las bebidas azucaradas por agua o infusiones — el cambio de menor costo y mayor impacto.")
    else:
        recs.append(f"⚖️ Lista balanceada para {n_personas} personas. Variá proteínas: pollo lunes/miércoles, huevos martes, legumbres jueves, pescado viernes.")
        recs.append("🛒 En Uruguay el desperdicio alimentario representa hasta un 20% del gasto del hogar. Tu lista está calibrada para minimizarlo.")

    if restriccion == "Sin gluten":
        recs.append("🌾 Incluimos versiones sin TACC. Verificá el sello en el envase — en Uruguay es obligatorio para productos certificados.")
    elif restriccion == "Sin lactosa":
        recs.append("🥛 Reemplazamos los lácteos por versiones sin lactosa. Complementá el calcio con brócoli y espinaca, ya en tu lista.")
    else:
        recs.append("🌾 Elegí versiones integrales de arroz y fideos cuando puedas — más fibra, te sacian más, precio similar.")

    return recs


def guardar_en_historial(perfil, lista_final, costo_estimado):
    entrada = {
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "personas": perfil["n_personas"],
        "presupuesto": perfil["presupuesto"],
        "objetivo": perfil["objetivo"],
        "restriccion": perfil["restriccion"],
        "costo_total": costo_estimado,
        "lista": lista_final,
    }
    st.session_state.historial.insert(0, entrada)
    if len(st.session_state.historial) > 5:
        st.session_state.historial = st.session_state.historial[:5]


# ── UI ───────────────────────────────────────────────────────────────────────

st.markdown('<div class="milista-header"><p class="milista-title">🛒 MILista</p></div>', unsafe_allow_html=True)
st.markdown('<p class="milista-subtitle">Tu lista de supermercado semanal, lista en segundos.</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    personas = st.selectbox("Personas en el hogar", ["1-2 personas", "3-4 personas", "5+ personas"])
    restriccion = st.selectbox("Restricción alimenticia", ["Ninguna", "Sin gluten", "Sin lactosa"])
with col2:
    presupuesto = st.number_input("Presupuesto semanal ($U)", min_value=500, max_value=100000, value=5000, step=500)
    objetivo = st.selectbox("Objetivo", ["Equilibrado", "Ahorrar dinero", "Comer más saludable"])

st.markdown("<div style='margin-top: 8px'></div>", unsafe_allow_html=True)
generar = st.button("✨ Generar lista")

if generar:
    perfil = agente_perfil(personas, presupuesto, restriccion, objetivo)
    productos_filtrados = agente_restricciones(restriccion)
    lista_base = agente_nutricional(productos_filtrados, perfil)
    lista_final, costo_estimado, fue_ajustada = agente_presupuesto(lista_base, perfil)
    recomendaciones = agente_recomendador(perfil, costo_estimado, lista_final)
    guardar_en_historial(perfil, lista_final, costo_estimado)

    diferencia = presupuesto - costo_estimado

    st.markdown("<div style='margin-top: 1.5rem'></div>", unsafe_allow_html=True)

    if fue_ajustada:
        st.info("Ajustamos algunas cantidades automáticamente para acercarnos a tu presupuesto.")

    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown(f'<div class="metric-card"><div class="metric-label">Presupuesto</div><div class="metric-value">$U {presupuesto:,.0f}</div></div>', unsafe_allow_html=True)
    with m2:
        st.markdown(f'<div class="metric-card"><div class="metric-label">Costo estimado</div><div class="metric-value">$U {costo_estimado:,.0f}</div></div>', unsafe_allow_html=True)
    with m3:
        if diferencia >= 0:
            st.markdown(f'<div class="metric-card-green"><div class="metric-label-green">Te sobra</div><div class="metric-value-green">$U {diferencia:,.0f}</div></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="metric-card-red"><div class="metric-label-red">Te falta</div><div class="metric-value-red">$U {abs(diferencia):,.0f}</div></div>', unsafe_allow_html=True)

    st.markdown("<div style='margin-top: 1.5rem'></div>", unsafe_allow_html=True)

    if objetivo == "Ahorrar dinero":
        st.markdown('<p class="section-title">📋 Tu lista de compras &nbsp;<span class="badge-green">💚 Optimizada para ahorro</span></p>', unsafe_allow_html=True)
    elif objetivo == "Comer más saludable":
        st.markdown('<p class="section-title">📋 Tu lista de compras &nbsp;<span class="badge-blue">💙 Optimizada para salud</span></p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="section-title">📋 Tu lista de compras</p>', unsafe_allow_html=True)

    for categoria, items in lista_final.items():
        st.markdown(f'<div class="category-header">{categoria}</div>', unsafe_allow_html=True)
        rows = ""
        for item in items:
            rows += f"""<div class="product-row">
                <span class="product-check">✓</span>
                <span class="product-name-text">{item['nombre']}</span>
                <span class="product-meta">{item['cantidad']} {item['unidad']}</span>
                <span class="product-price-text">$U {item['costo']:,.0f}</span>
            </div>"""
        st.markdown(f'<div class="product-list">{rows}</div>', unsafe_allow_html=True)

    recs_html = "".join(f'<div class="rec-item">{r}</div>' for r in recomendaciones)
    st.markdown(f'<div class="rec-box"><div class="rec-title">💡 Recomendaciones para tu hogar</div>{recs_html}</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.caption("_Precios estimados basados en datos del SIPC Uruguay. Pueden variar según el supermercado._")

if st.session_state.historial:
    st.markdown("<p class='section-title' style='margin-top:2rem'>🕐 Mis listas anteriores</p>", unsafe_allow_html=True)
    st.caption("Tu historial se mantiene durante esta sesión. Al cerrar el browser se borra automáticamente.")

    if len(st.session_state.historial) > 1:
        ahorros = [e["presupuesto"] - e["costo_total"] for e in st.session_state.historial]
        ahorro_promedio = round(sum(ahorros) / len(ahorros))
        if ahorro_promedio >= 0:
            st.markdown(f'<div class="metric-card-green" style="margin-bottom:1rem"><div class="metric-label-green">Ahorro promedio por lista</div><div class="metric-value-green">$U {ahorro_promedio:,.0f}</div></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="metric-card-red" style="margin-bottom:1rem"><div class="metric-label-red">Exceso promedio por lista</div><div class="metric-value-red">$U {abs(ahorro_promedio):,.0f}</div></div>', unsafe_allow_html=True)
    for i, entrada in enumerate(st.session_state.historial):
        diferencia_hist = entrada["presupuesto"] - entrada["costo_total"]
        estado = "✅ Dentro del presupuesto" if diferencia_hist >= 0 else "⚠️ Superó el presupuesto"
        with st.expander(f"Lista #{len(st.session_state.historial) - i} — {entrada['fecha']} · {entrada['objetivo']}"):
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown(f"**Personas:** {entrada['personas']}")
                st.markdown(f"**Objetivo:** {entrada['objetivo']}")
                st.markdown(f"**Restricción:** {entrada['restriccion']}")
            with col_b:
                st.markdown(f"**Presupuesto:** $U {entrada['presupuesto']:,.0f}")
                st.markdown(f"**Costo total:** $U {entrada['costo_total']:,.0f}")
                st.markdown(f"**{estado}**")
            st.markdown("**Productos:**")
            for categoria, items in entrada["lista"].items():
                nombres = ", ".join(item["nombre"] for item in items)
                st.markdown(f"- {categoria}: {nombres}")
                
