from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceMatrix, DistanceTreeConstructor

# Biopython pide la matriz en un formato triangular
# El orden de las especies es A, B, C, D
nombres = ["A", "B", "C", "D"]
matriz = [
    [0],
    [2, 0],
    [4, 4, 0],
    [6, 6, 6, 0],
]

matriz_distancias = DistanceMatrix(nombres, matriz)

constructor = DistanceTreeConstructor()
arbol = constructor.upgma(matriz_distancias)

print("Arbol generado por Biopython:")
Phylo.draw_ascii(arbol)