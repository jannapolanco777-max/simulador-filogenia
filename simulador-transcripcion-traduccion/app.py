import streamlit as st

st.set_page_config(page_title="Transcripción y traducción del ADN", page_icon="🧬", layout="centered")

st.markdown("""
<style>
    .stButton button {
        background-color: #7B4B94;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 8px 20px;
    }
    .stButton button:hover {
        background-color: #5f3a73;
        color: white;
    }
    h1 {
        color: #7B4B94;
    }
    h3 {
        color: #2E8B57;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧬 Transcripción y traducción del ADN")
st.write("Convierte una secuencia de ADN en ARN mensajero, y después en una proteína, paso a paso.")

with st.expander("❓ ¿Cómo funciona este simulador? (Ayuda guiada)"):
    st.write("""
    Este simulador reproduce el proceso real que ocurre dentro de una célula para fabricar proteínas.

    **Paso 1:** Escribe una secuencia de ADN usando solo las letras A, T, C y G, o deja la secuencia de ejemplo.

    **Paso 2:** El simulador transcribe tu ADN a ARN mensajero, cambiando cada letra T por U.

    **Paso 3:** El simulador traduce el ARN mensajero en una proteína, leyendo la secuencia de tres en tres
    letras (codones), y buscando qué aminoácido corresponde a cada codón según el código genético.

    **Un dato importante:** el proceso se detiene automáticamente cuando encuentra un codón de "Stop",
    que le indica a la célula que ahí termina la proteína.
    """)

st.subheader("🔤 1. Ingresa tu secuencia de ADN")
adn = st.text_input("Secuencia de ADN (solo A, T, C, G)", value="ATGGCTAAACGTTAG")

codigo_genetico = {
    "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
    "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "UAU": "Tyr", "UAC": "Tyr", "UAA": "Stop", "UAG": "Stop",
    "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
    "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
    "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
    "UGU": "Cys", "UGC": "Cys", "UGA": "Stop", "UGG": "Trp",
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
}


def validar_adn(secuencia):
    bases_validas = set("ATCG")
    secuencia = secuencia.upper()
    for base in secuencia:
        if base not in bases_validas:
            return False
    return True


def transcribir(secuencia):
    secuencia = secuencia.upper()
    return secuencia.replace("T", "U")


def traducir(arn):
    proteina = []
    for i in range(0, len(arn) - 2, 3):
        codon = arn[i:i + 3]
        aminoacido = codigo_genetico.get(codon, "?")
        if aminoacido == "Stop":
            break
        proteina.append((codon, aminoacido))
    return proteina


st.subheader("🎯 2. Autoevaluación")
st.write("Antes de continuar, ¿a qué aminoácido crees que corresponde el primer codón de tu ARN?")
opciones_aminoacidos = sorted(set(codigo_genetico.values()))
prediccion = st.selectbox("Tu predicción:", opciones_aminoacidos)

if st.button("🧬 Transcribir y traducir"):
    if not validar_adn(adn):
        st.error("Tu secuencia contiene letras que no son A, T, C o G. Revísala e inténtalo de nuevo.")
    else:
        arn = transcribir(adn)
        proteina = traducir(arn)

        st.subheader("📊 3. Progreso del proceso")
        total_codones = len(proteina)
        for i, (codon, aminoacido) in enumerate(proteina, start=1):
            progreso = i / total_codones
            st.progress(progreso)
            st.markdown(
                f"<div style='background-color:#7B4B9420; padding:10px; border-radius:8px; border-left: 5px solid #7B4B94;'>"
                f"Codón {i} de {total_codones}: <b>{codon}</b> se traduce como <b>{aminoacido}</b>"
                f"</div>",
                unsafe_allow_html=True
            )
            st.write("")

        st.subheader("🧬 4. Resultado completo")
        st.write("**ADN:**")
        st.code(adn)
        st.write("**ARN mensajero:**")
        st.code(arn)
        st.write("**Proteína:**")
        st.code(" - ".join([a for _, a in proteina]))

        st.success("🎉 ¡Proceso completado! Así es como tu secuencia de ADN se convirtió en una proteína.")

        primer_aminoacido = proteina[0][1]
        if prediccion == primer_aminoacido:
            st.balloons()
            st.success(f"¡Acertaste! El primer codón se traduce como {primer_aminoacido}.")
        else:
            st.warning(f"No acertaste esta vez. El primer codón se traduce como {primer_aminoacido}, no {prediccion}. ¡Inténtalo con otra secuencia!")