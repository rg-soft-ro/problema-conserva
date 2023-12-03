import random
import math

def optimizare_conserve(L, W, raza_min, raza_max, inaltime_min, inaltime_max, numar_generatii=50, numar_indivizi=10, rata_de_mutatie=0.1):
    """
    Parametri:
    L (int)- lungimea foii de tabla
    I (int)- latimea foii de tabla
    raza_min, raza_max (int)- intervalul pentru raza conservelor
    inaltime_min, inaltime_max (int) - intervalul pentru Inaltimea conservelor
    """
    aria_maxima = L * I   # Calcularea ariei maxime disponibile bazata pe dimensiunile foii de tabla

    # Functie pentru calcularea fitness-ului unui individ
    def fitness(raza, inaltime):
        A_conserve = 2 * math.pi * raza**2 + 2 * math.pi * raza * inaltime
        N = math.floor(aria_maxima / A_conserve)
        return N  # Fitness-ul este numarul de conserve ce pot fi fabricate

    # Crearea populatiei initiale cu dimensiuni aleatorii pentru conserve
    populatie = [(random.randint(raza_min, raza_max), random.randint(inaltime_min, inaltime_max)) for _ in range(numar_indivizi)]

    # Functia de crossover (Incrucisare): combina trasaturile a doi indivizi pentru a crea noi indivizi
    def crossover(individ1, individ2):
        raza1, inaltime1 = individ1
        raza2, inaltime2 = individ2
        copil1 = (raza1, inaltime2)
        copil2 = (raza2, inaltime1)
        return (copil1, copil2)

    # Functia de mutatie: introduce variatii aleatorii in trasaturile unui individ
    def mutatie(individ):
        raza, inaltime = individ
        if random.random() < rata_de_mutatie:
            raza = random.randint(raza_min, raza_max)
        if random.random() < rata_de_mutatie:
            inaltime = random.randint(inaltime_min, inaltime_max)
        return (raza, inaltime)

    # Algoritmul genetic
    for generatie in range(numar_generatii):
        # Evaluarea fitness-ului pentru fiecare individ din populatie
        fitness_populatie = [fitness(raza, inaltime) for raza, inaltime in populatie]

        # Selectarea celor mai buni indivizi pentru reproducere
        selectie_pentru_reproducere = sorted(zip(populatie, fitness_populatie), key=lambda x: x[1], reverse=True)
        selectie_pentru_reproducere = [individ for individ, _ in selectie_pentru_reproducere[:numar_indivizi//2]]

        # Crearea noii generatii prin crossover si mutatie
        urmasi = []
        while len(urmasi) < numar_indivizi:
            parinte1, parinte2 = random.sample(selectie_pentru_reproducere, 2)
            copil1, copil2 = crossover(parinte1, parinte2)
            urmasi.append(mutatie(copil1))
            urmasi.append(mutatie(copil2))

        populatie = urmasi

    # Determinarea celui mai bun individ dupa ultima generatie
    cel_mai_bun_individ = sorted(zip(populatie, fitness_populatie), key=lambda x: x[1], reverse=True)[0]
    return cel_mai_bun_individ

# Introducerea datelor prin consola
L = int(input("Introduceti lungimea foii de tabla (cm): "))
I = int(input("Introduceti latimea foii de tabla (cm): "))
raza_min = int(input("Introduceti raza minima a conservelor (cm): "))
raza_max = int(input("Introduceti raza maxima a conservelor (cm): "))
inaltime_min = int(input("Introduceti Inaltimea minima a conservelor (cm): "))
inaltime_max = int(input("Introduceti Inaltimea maxima a conservelor (cm): "))

# Rularea algoritmului genetic cu datele introduse
rezultat = optimizare_conserve(L, I, raza_min, raza_max, inaltime_min, inaltime_max)
print(f"Cea mai buna solutie: Raza = {rezultat[0][0]} cm, Inaltimea = {rezultat[0][1]} cm, Numarul maxim de conserve: {rezultat[1]}")
