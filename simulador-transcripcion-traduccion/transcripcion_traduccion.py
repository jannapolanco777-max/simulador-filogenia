# Secuencia de ADN de ejemplo
adn = "ATGGCTAAACGTTAG"


def validar_adn(secuencia):
    bases_validas = set("ATCG")
    secuencia = secuencia.upper()
    for base in secuencia:
        if base not in bases_validas:
            return False
    return True


if validar_adn(adn):
    print(f"La secuencia {adn} es válida")
else:
    print(f"La secuencia {adn} contiene letras que no son A, T, C o G")

def transcribir(secuencia):
    secuencia = secuencia.upper()
    arn = secuencia.replace("T", "U")
    return arn


arn = transcribir(adn)
print(f"ADN:  {adn}")
print(f"ARNm: {arn}")

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


def traducir(arn):
    proteina = []
    for i in range(0, len(arn) - 2, 3):
        codon = arn[i:i + 3]
        aminoacido = codigo_genetico.get(codon, "?")
        if aminoacido == "Stop":
            break
        proteina.append(aminoacido)
    return proteina


proteina = traducir(arn)
print(f"Proteína: {' - '.join(proteina)}")