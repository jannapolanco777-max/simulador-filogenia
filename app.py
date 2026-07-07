import streamlit as st

import matplotlib.pyplot as plt

st.set_page_config(page_title="Simulador de filogenia", page_icon="🫆", layout="centered")

st.markdown("""
<style>
    .stButton button {
        background-color: #2E8B57;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 8px 20px;
    }
    .stButton button:hover {
        background-color: #246b45;
        color: white;
    }
    h1 {
        color: #2E8B57;
    }
    h3 {
        color: #4682B4;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧬 Simulador de filogenia")
st.write("Construye un árbol evolutivo a partir de distancias genéticas, paso a paso.")

with st.expander("❓ ¿Cómo funciona este simulador? (Ayuda guiada)"):
    st.write("""
    Este simulador construye un árbol evolutivo usando el método UPGMA.

    **Paso 1:** Escribe el nombre de cuatro especies, o deja los nombres A, B, C y D si prefieres.

    **Paso 2:** Ingresa qué tan diferentes son entre sí, usando un número para cada par.
    Mientras más chico el número, más parecidas son esas dos especies genéticamente.

    **Paso 3:** Dale clic a "Construir árbol". El simulador va a ir agrupando primero a las especies
    más parecidas, y así hasta formar el árbol completo.

    **Un dato importante:** cada vez que dos especies o grupos se unen, el simulador recalcula
    las distancias hacia los demás usando un promedio. Así es como funciona UPGMA en la vida real.
    """)

st.subheader("🔤 1. Ingresa tus especies y la matriz de distancias")

col1, col2, col3, col4 = st.columns(4)
with col1:
    especie_a = st.text_input("Especie A", value="A")
with col2:
    especie_b = st.text_input("Especie B", value="B")
with col3:
    especie_c = st.text_input("Especie C", value="C")
with col4:
    especie_d = st.text_input("Especie D", value="D")

st.write("Matriz de distancias (puedes usar el ejemplo o cambiar los números):")

col1, col2, col3 = st.columns(3)
with col1:
    dist_ab = st.number_input(f"{especie_a} - {especie_b}", value=2, min_value=0)
    dist_ac = st.number_input(f"{especie_a} - {especie_c}", value=4, min_value=0)
with col2:
    dist_ad = st.number_input(f"{especie_a} - {especie_d}", value=6, min_value=0)
    dist_bc = st.number_input(f"{especie_b} - {especie_c}", value=4, min_value=0)
with col3:
    dist_bd = st.number_input(f"{especie_b} - {especie_d}", value=6, min_value=0)
    dist_cd = st.number_input(f"{especie_c} - {especie_d}", value=6, min_value=0)


def encontrar_par_mas_cercano(distancias):
    par_mas_cercano = min(distancias, key=distancias.get)
    valor_mas_chico = distancias[par_mas_cercano]
    return par_mas_cercano, valor_mas_chico


def unir_par(distancias, par):
    especie1, especie2 = par
    nuevo_grupo = f"({especie1},{especie2})"

    otras_especies = set()
    for a, b in distancias:
        otras_especies.add(a)
        otras_especies.add(b)
    otras_especies.discard(especie1)
    otras_especies.discard(especie2)

    nueva_distancias = {}

    for (a, b), valor in distancias.items():
        if especie1 not in (a, b) and especie2 not in (a, b):
            nueva_distancias[(a, b)] = valor

    for especie in otras_especies:
        d1 = distancias.get((especie1, especie)) or distancias.get((especie, especie1))
        d2 = distancias.get((especie2, especie)) or distancias.get((especie, especie2))
        promedio = (d1 + d2) / 2
        nueva_distancias[(nuevo_grupo, especie)] = promedio

    return nueva_distancias


def construir_arbol(distancias):
    pasos = []
    while len(distancias) > 0:
        especies = set()
        for a, b in distancias:
            especies.add(a)
            especies.add(b)
        if len(especies) <= 1:
            break
        par, dist = encontrar_par_mas_cercano(distancias)
        pasos.append((par, dist))
        distancias = unir_par(distancias, par)
    return pasos

st.subheader("🎯 3. Autoevaluación")
st.write("Antes de construir el árbol, ¿cuál par crees que se va a agrupar primero? Es el par con la distancia más chica.")

opciones = [
    f"{especie_a} y {especie_b}",
    f"{especie_a} y {especie_c}",
    f"{especie_a} y {especie_d}",
    f"{especie_b} y {especie_c}",
    f"{especie_b} y {especie_d}",
    f"{especie_c} y {especie_d}",
]
prediccion = st.radio("Tu predicción:", opciones)

def dibujar_arbol(pasos, especies):
    x_pos = {especie: i for i, especie in enumerate(especies)}
    y_pos = {especie: 0 for especie in especies}

    fig, ax = plt.subplots(figsize=(6, 4))

    for par, dist in pasos:
        x1, y1 = x_pos[par[0]], y_pos[par[0]]
        x2, y2 = x_pos[par[1]], y_pos[par[1]]

        ax.plot([x1, x1], [y1, dist], color="#2E8B57", linewidth=2)
        ax.plot([x2, x2], [y2, dist], color="#2E8B57", linewidth=2)
        ax.plot([x1, x2], [dist, dist], color="#2E8B57", linewidth=2)

        nuevo_nombre = f"({par[0]},{par[1]})"
        nueva_x = (x1 + x2) / 2
        x_pos[nuevo_nombre] = nueva_x
        y_pos[nuevo_nombre] = dist

    for especie in especies:
        ax.text(x_pos[especie], -0.3, especie, ha="center", fontsize=12, fontweight="bold")

    ax.set_ylabel("Distancia genética")
    ax.set_xticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)

    return fig

if st.button("🌳 Construir árbol"):
    distancias = {
        (especie_a, especie_b): dist_ab,
        (especie_a, especie_c): dist_ac,
        (especie_a, especie_d): dist_ad,
        (especie_b, especie_c): dist_bc,
        (especie_b, especie_d): dist_bd,
        (especie_c, especie_d): dist_cd,
    }

    pasos = construir_arbol(distancias)

    st.subheader("📊 2. Progreso del agrupamiento")

    colores = ["#2E8B57", "#4682B4", "#DAA520", "#B22222"]

    total_pasos = len(pasos)
    for i, (par, dist) in enumerate(pasos, start=1):
        progreso = i / total_pasos
        st.progress(progreso)
        color = colores[(i - 1) % len(colores)]
        st.markdown(
            f"<div style='background-color:{color}20; padding:10px; border-radius:8px; border-left: 5px solid {color};'>"
            f"Paso {i} de {total_pasos}: se unieron <b>{par[0]}</b> y <b>{par[1]}</b> con una distancia de {dist}"
            f"</div>",
            unsafe_allow_html=True
        )
        st.write("")

        st.subheader("🌳 Árbol filogenético")
    especies_lista = [especie_a, especie_b, especie_c, especie_d]
    fig = dibujar_arbol(pasos, especies_lista)
    st.pyplot(fig)

    st.success("¡Árbol completado! Así fue como se agruparon tus especies según su parecido genético.")
    primer_par = pasos[0][0]
    respuesta_correcta = f"{primer_par[0]} y {primer_par[1]}"

    if prediccion == respuesta_correcta:
        st.balloons()
        st.success(f"¡Acertaste! El par que se agrupó primero fue {respuesta_correcta}.")
    else:
        st.warning(f"No acertaste esta vez. El par correcto era {respuesta_correcta}, no {prediccion}. ¡Inténtalo de nuevo con otra matriz!")