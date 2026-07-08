from Bio.Seq import Seq

adn = "ATGGCTAAACGTTAG"

secuencia = Seq(adn)
arn = secuencia.transcribe()
proteina = secuencia.translate(to_stop=True)

print(f"ADN:  {adn}")
print(f"ARNm generado por Biopython: {arn}")
print(f"Proteína generada por Biopython: {proteina}")