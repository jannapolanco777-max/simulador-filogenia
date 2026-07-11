import streamlit as st
from stmol import showmol
import py3Dmol
from Bio.PDB import PDBList, PDBParser
import os

# ------------------------------------------------------------------
# Configuración general de la página
# ------------------------------------------------------------------
st.set_page_config(page_title="Modelado estructural de proteínas", layout="wide")

st.title("🧬 Modelado estructural de proteínas")
st.write(
    "Este simulador te deja explorar en 3D la hemoglobina, la proteína que "
    "transporta el oxígeno en la sangre, y ver con tus propios ojos cómo el "
    "cambio de un solo aminoácido puede desencadenar la anemia falciforme."
)

with st.expander("ℹ️ ¿Cómo se usa este simulador?"):
    st.write(
        "1. A la izquierda vas a ver la hemoglobina normal.\n\n"
        "2. A la derecha vas a ver la misma proteína, pero con el residuo 6 "
        "de la cadena beta resaltado en rojo. Ahí es justo donde ocurre la "
        "mutación que causa la anemia falciforme.\n\n"
        "3. Usa los controles de abajo para cambiar el estilo, el color y "
        "activar la rotación automática.\n\n"
        "4. Al final puedes poner a prueba lo que aprendiste con una pregunta "
        "rápida."
    )

PDB_ID = "1A00"  # Hemoglobina humana normal (oxihemoglobina)


# ------------------------------------------------------------------
# Descarga y análisis de la proteína con BioPython
# ------------------------------------------------------------------
@st.cache_data(show_spinner="Descargando y analizando la estructura desde el PDB...")
def obtener_cadenas_con_mutacion(pdb_id):
    """
    Descarga la estructura desde el Protein Data Bank y usa BioPython para
    identificar en qué cadena(s) se encuentra el residuo 6, confirmando que
    corresponde a un ácido glutámico (GLU). Esa es la posición exacta donde,
    en la hemoglobina S, aparece la mutación Glu6Val.
    """
    os.makedirs("pdb_files", exist_ok=True)
    pdbl = PDBList()
    archivo = pdbl.retrieve_pdb_file(
        pdb_id, pdir="pdb_files", file_format="pdb", overwrite=False
    )

    parser = PDBParser(QUIET=True)
    estructura = parser.get_structure(pdb_id, archivo)

    cadenas_glu6 = []
    for modelo in estructura:
        for cadena in modelo:
            for residuo in cadena:
                if residuo.id[1] == 6 and residuo.resname == "GLU":
                    cadenas_glu6.append(cadena.id)
        break  # con el primer modelo es suficiente

    return cadenas_glu6


try:
    cadenas_beta = obtener_cadenas_con_mutacion(PDB_ID)
except Exception as e:
    st.error(
        "No se pudo descargar la estructura desde el PDB. Revisa tu conexión "
        f"a internet e intenta de nuevo. Detalle: {e}"
    )
    st.stop()

if not cadenas_beta:
    st.warning(
        "No se encontró un GLU en la posición 6 en ninguna cadena. "
        "Se continuará mostrando la proteína completa sin resaltar la mutación."
    )

st.success(
    f"BioPython confirmó que el residuo 6 es un ácido glutámico (GLU) en "
    f"la(s) cadena(s) {', '.join(cadenas_beta) if cadenas_beta else '—'}. "
    "Esa es justo la posición donde ocurre la mutación en la hemoglobina S."
)

# ------------------------------------------------------------------
# Controles del visor
# ------------------------------------------------------------------
st.subheader("🎛️ Controles de visualización")
col_a, col_b, col_c = st.columns(3)

with col_a:
    estilo = st.selectbox("Estilo de la proteína", ["cartoon", "stick", "sphere"], index=0)
with col_b:
    color = st.selectbox("Esquema de color", ["spectrum", "chain", "residue"], index=0)
with col_c:
    girar = st.checkbox("Girar automáticamente", value=False)

st.caption(
    "Con el mouse también puedes rotar, acercar y desplazar la proteína "
    "directamente dentro del visor."
)


def crear_visor(resaltar_mutacion=False):
    visor = py3Dmol.view(query=f"pdb:{PDB_ID}", width=550, height=450)

    if color == "spectrum":
        visor.setStyle({estilo: {"color": "spectrum"}})
    elif color == "chain":
        visor.setStyle({estilo: {"colorscheme": "chain"}})
    else:
        visor.setStyle({estilo: {"colorscheme": "amino"}})
    if resaltar_mutacion and cadenas_beta:
        for cadena_id in cadenas_beta:
            visor.setStyle(
                {"chain": cadena_id, "resi": "6"},
                {"stick": {"colorscheme": "redCarbon"}, "sphere": {"scale": 0.5, "color": "red"}},
            )
            visor.addLabel(
                "Glu6 → Val (mutación)",
                {
                    "backgroundColor": "red",
                    "fontColor": "white",
                    "fontSize": 12,
                },
                {"chain": cadena_id, "resi": "6"},
            )

    visor.zoomTo()
    if girar:
        visor.spin(True)
    return visor


# ------------------------------------------------------------------
# Visualización lado a lado: normal vs. mutación resaltada
# ------------------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"Hemoglobina normal ({PDB_ID})")
    showmol(crear_visor(resaltar_mutacion=False), height=450, width=550)

with col2:
    st.subheader("Hemoglobina con la mutación resaltada")
    showmol(crear_visor(resaltar_mutacion=True), height=450, width=550)

# ------------------------------------------------------------------
# Explicación biológica
# ------------------------------------------------------------------
st.subheader("🔬 ¿Qué está pasando aquí?")
st.write(
    "La hemoglobina normal tiene un ácido glutámico en la posición 6 de su "
    "cadena beta. En la hemoglobina S, ese ácido glutámico es reemplazado por "
    "una valina. Ese cambio parece pequeño, pero la valina es hidrofóbica, "
    "mientras que el ácido glutámico no lo es. Esa diferencia crea un punto "
    "pegajoso en la superficie de la proteína."
)
st.write(
    "Cuando la hemoglobina libera el oxígeno, las moléculas mutadas empiezan "
    "a engancharse entre sí a través de ese punto pegajoso y forman fibras "
    "largas dentro del glóbulo rojo. Esas fibras deforman la célula y le dan "
    "la forma de hoz que le da nombre a la enfermedad, además de volverla "
    "más rígida y de vida más corta."
)

# ------------------------------------------------------------------
# Autoevaluación
# ------------------------------------------------------------------
st.subheader("🧠 Ponte a prueba")
respuesta = st.radio(
    "¿Qué aminoácido reemplaza al ácido glutámico en la posición 6 de la "
    "hemoglobina S?",
    ["Alanina", "Valina", "Leucina", "Treonina"],
    index=None,
)

if respuesta is not None:
    if respuesta == "Valina":
        st.success("¡Correcto! El ácido glutámico es reemplazado por valina.")
        st.balloons()
    else:
        st.error(
            "No es esa. Fíjate en el residuo resaltado en rojo en el visor "
            "de la derecha y vuelve a intentarlo."
        )

st.divider()
st.caption("🧬 Simulador creado por Janna Polanco y Yenifer Silverio")