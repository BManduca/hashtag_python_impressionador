import random

# Lista de nomes da rifa organizados em uma única lista
# nomes_rifa = [
#     "Alice", "Amélia", "Adelaide", "Antonia", "Ana",
#     "Angela", "Andressa", "Aparecida", "Aline", "Alessandra",
#     "Bernadete", "Célia", "Cristiane", "Cláudia", "Camila",
#     "Cleonice", "Cristina", "Clarice", "Daiane", "Denise",
#     "Edna", "Edilene", "Eliane", "Eva", "Eloiza",
#     "Fabiola", "Gisele", "Grazieli", "Hilda", "Ivone",
#     "Jacira", "Joana", "Jaqueline", "Jéssica", "Josiane",
#     "Lúcia", "Lourdes", "Luciana", "Márcia", "Maria",
#     "Neide", "Olga", "Patrícia", "Renata", "Sandra",
#     "Silvia", "Solange", "Tereza", "Tatiane", "Vania"
# ]
nomes_rifa = [
    "Alice", "Angela", "Aparecida", "Cristiane"
]

# Escolher um nome aleatório
sorteado = random.choice(nomes_rifa)
# sorteados = random.sample(nomes_rifa, 3)

print(f'Nome sorteado => {sorteado}')
# print(f'Nome sorteado => {", ".join(sorteados)}')
