import random
import math

def optimizare_conserve(L, W, V, numar_generatii=50, numar_indivizi=10, rata_de_mutatie=0.1):
    aria_maxima = L * W

    # Functie pentru calcularea inaltimii pe baza razei si volumului dat
    def calculeaza_inaltime(raza, volum):
        return volum / (math.pi * raza**2)

    # Functie pentru calcularea ariei unei conserve
    def calculeaza_arie(raza, inaltime):
        return 2 * math.pi * raza**2 + 2 * math.pi * raza * inaltime

    # Functia de fitness
    def fitness(raza):
        inaltime = calculeaza_inaltime(raza, V)
        A_conserve = calculeaza_arie(raza, inaltime)
        if A_conserve > aria_maxima:
            return 0  # Conserva este prea mare pentru a se incadra in foaia de tabla
        return math.floor(aria_maxima / A_conserve)

    # Crearea populatiei initiale
    populatie = [random.uniform(1, math.sqrt(V / math.pi)) for _ in range(numar_indivizi)]

    # Functia de crossover
    def crossover(raza1, raza2):
        return (raza1 + raza2) / 2

    # Functia de mutatie: introduce variatii aleatorii in trasaturile unui individ
    def mutatie(raza):
        return raza + random.uniform(-raza/10, raza/10)

    # Algoritmul genetic
    for generatie in range(numar_generatii):
        # Evaluarea fitness-ului pentru fiecare individ din populatie
        fitness_populatie = [fitness(raza) for raza in populatie]

        # Selectarea celor mai buni indivizi pentru reproducere
        selectie_pentru_reproducere = sorted(zip(populatie, fitness_populatie), key=lambda x: x[1], reverse=True)
        selectie_pentru_reproducere = [raza for raza, _ in selectie_pentru_reproducere[:numar_indivizi//2]]

        # Crearea noii generatii prin crossover si mutatie
        urmasi = []
        while len(urmasi) < numar_indivizi:
            raza1, raza2 = random.sample(selectie_pentru_reproducere, 2)
            urmasi.append(mutatie(crossover(raza1, raza2)))

        populatie = urmasi

    # Determinarea celui mai bun individ dupa ultima generatie
    cea_mai_buna_raza = sorted(zip(populatie, fitness_populatie), key=lambda x: x[1], reverse=True)[0][0]
    cea_mai_buna_inaltime = calculeaza_inaltime(cea_mai_buna_raza, V)
    cel_mai_bun_fitness = fitness(cea_mai_buna_raza)

    return cea_mai_buna_raza, cea_mai_buna_inaltime, cel_mai_bun_fitness

# Datele de intrare
L = int(input("\nIntroduceti lungimea foii de tabla (cm): "))
W = int(input("Introduceti latimea foii de tabla (cm): "))
V = float(input("Introduceti volumul conservei (cm^3): "))

raza, inaltime, numar_conserve = optimizare_conserve(L, W, V)
print(f"\nCea mai buna solutie: \nRaza = {raza:.2f} cm \nInaltimea = {inaltime:.2f} cm \nNumarul maxim de conserve: {numar_conserve}\n")
