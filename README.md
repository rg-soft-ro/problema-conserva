# Algoritm genetic pentru problema cu cutia de conservă

Acest program utilizează un algoritm genetic pentru a determina dimensiunile optime ale conservelor ce pot fi fabricate dintr-o foaie de tablă, maximizând astfel numărul de conserve ce pot fi produse.

### Funcții principale

- **`optimizare_conserve`**: Funcția principală a programului, care rulează algoritmul genetic pentru a căuta soluția optimă. Această funcție primește următorii parametri:
  - `L` și `I` reprezintă dimensiunile foii de tablă (lungime și lățime).
  - `raza_min` și `raza_max` sunt limitele pentru raza conservelor.
  - `inaltime_min` și `inaltime_max` sunt limitele pentru înălțimea conservelor.
  - `numar_generatii` specifică numărul de generații ale algoritmului genetic.
  - `numar_indivizi` reprezintă numărul de indivizi în fiecare generație a populației.
  - `rata_de_mutatie` este probabilitatea de mutație pentru trăsăturile individuale.


### Procesul algoritmului genetic

Algoritmul genetic începe cu o populație inițială de indivizi, fiecare cu dimensiuni aleatorii pentru conserve. Apoi, urmează următoarele etape:

1. **Calculul fitness-ului (`fitness`)**: Se evaluează eficiența fiecărui individ în funcție de numărul maxim de conserve ce pot fi fabricate din foaia de tablă cu dimensiunile date.
2. **Încrucișarea (Crossover)**: Se combină trăsăturile a doi "părinți" pentru a produce noi "copii" în funcție de funcția `crossover`.
3. **Mutația (`mutatie`)**: Se introduc variații aleatorii în trăsăturile indivizilor pentru a asigura diversitatea genetică în populație.
4. Algoritmul evoluează pe mai multe generații, îmbunătățind treptat soluțiile. La final, programul identifică cel mai eficient set de dimensiuni pentru fabricarea conservelor.

**Programul calculează întâi aria totală necesară pentru a fabrica o singură conservă, luând în calcul atât capetele, cât și suprafața laterală cilindrică. Acest lucru se face folosind formula ariei unui cilindru.
Apoi, se împarte aria totală a foii de tablă (produsul dintre lungime și lățime) la aria necesară pentru o conservă. Rezultatul acestui calcul este numărul de conserve ce pot fi produse din foaia respectivă, dată fiind dimensiunea specifică a unei conserve.**

## Utilizare

Pentru a utiliza programul se ruleaza cu comanda `python conserva.py`, apoi introduce dimensiunile foii de tablă și intervalul dimensiunilor conservelor.
Programul acceptă orice valori și calculează cea mai bună soluție în funcție de datele introduse

Exemplu de utilizare:

```plaintext
PS C:\Users\rober\Desktop\SI - problema conserve> & C:/Users/rober/AppData/Local/Microsoft/WindowsApps/python3.11.exe "c:/Users/rober/Desktop/SI - problema conserve/conserva.py"
Introduceți lungimea foii de tablă (cm): 200
Introduceți lățimea foii de tablă (cm): 100
Introduceți raza minimă a conservelor (cm): 5
Introduceți raza maximă a conservelor (cm): 5
Introduceți înălțimea minimă a conservelor (cm): 10
Introduceți înălțimea maximă a conservelor (cm): 10
Cea mai bună soluție: Raza = 5 cm, Înălțimea = 10 cm, Numărul maxim de conserve: 42
```
``` plaintext
PS C:\Users\rober\Desktop\SI - problema conserve> & C:/Users/rober/AppData/Local/Microsoft/WindowsApps/python3.11.exe "c:/Users/rober/Desktop/SI - problema conserve/conserva.py"
Introduceti lungimea foii de tabla (cm): 200
Introduceti latimea foii de tabla (cm): 100
Introduceti raza minima a conservelor (cm): 5
Introduceti raza maxima a conservelor (cm): 10
Introduceti înaltimea minima a conservelor (cm): 7
Introduceti înaltimea maxima a conservelor (cm): 11
Cea mai buna solutie: Raza = 5 cm, Înaltimea = 7 cm, Numarul maxim de conserve: 53
```
