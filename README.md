# Algoritm genetic pentru problema cu cutia de conservă

Acest program utilizează un algoritm genetic pentru a determina dimensiunile optime ale conservelor ce pot fi fabricate dintr-o foaie de tablă, maximizând astfel numărul de conserve ce pot fi produse.

### Funcții principale

- **`optimizare_conserve`**: Funcția principală a programului, care rulează algoritmul genetic pentru a căuta soluția optimă. Această funcție primește următorii parametri:
  - `L` și `W` reprezintă dimensiunile foii de tablă (lungime și lățime).
  - `V` este volumul dat al conservei.
  - `numar_generatii` specifică numărul de generații ale algoritmului genetic.
  - `numar_indivizi` reprezintă numărul de indivizi în fiecare generație a populației.
  - `rata_de_mutatie` este probabilitatea de mutație pentru trăsăturile individuale.


### Procesul algoritmului genetic

Algoritmul genetic începe cu o populație inițială de indivizi, fiecare cu dimensiuni aleatorii pentru conserve. Apoi, urmează următoarele etape:

1. **Calculul fitness-ului (`fitness`)**: Se evaluează eficiența fiecărui individ în funcție de numărul maxim de conserve ce pot fi fabricate din foaia de tablă cu dimensiunile date.
2. **Încrucișarea (Crossover)**: Se combină trăsăturile a doi "părinți" pentru a produce noi "copii" în funcție de funcția `crossover`.
3. **Mutația (`mutatie`)**: Se introduc variații aleatorii în trăsăturile indivizilor pentru a asigura diversitatea genetică în populație.
4. Algoritmul evoluează pe mai multe generații, îmbunătățind treptat soluțiile. La final, programul identifică cel mai eficient set de dimensiuni pentru fabricarea conservelor.

**Programul calculează înălțimea conservelor pe baza razei și volumului dat și apoi determină aria necesară pentru a fabrica o singură conservă. Se împarte aria totală a foii de tablă la aria unei conserve pentru a determina numărul de conserve ce pot fi produse.**

## Utilizare

Pentru a utiliza programul, se va rula cu comanda `python conserva.py`, apoi se introduce dimensiunile foii de tablă și intervalul dimensiunilor conservelor.
Programul acceptă orice valori și calculează cea mai bună soluție în funcție de datele introduse

Exemplu de utilizare:

```plaintext
PS C:\Users\rober\Desktop\SI - problema conserve> & C:/Users/rober/AppData/Local/Microsoft/WindowsApps/python3.11.exe "c:/Users/rober/Desktop/SI - problema conserve/conserva2.py"

Introduceti lungimea foii de tabla (cm): 200
Introduceti latimea foii de tabla (cm): 100
Introduceti volumul conservei (cm^3): 400

Cea mai buna solutie:
Raza = 3.87 cm
Inaltimea = 8.50 cm
Numarul maxim de conserve: 66
```
``` plaintext
PS C:\Users\rober\Desktop\SI - problema conserve> & C:/Users/rober/AppData/Local/Microsoft/WindowsApps/python3.11.exe "c:/Users/rober/Desktop/SI - problema conserve/conserva2.py"

Introduceti lungimea foii de tabla (cm): 800
Introduceti latimea foii de tabla (cm): 120
Introduceti volumul conservei (cm^3): 500

Cea mai buna solutie:
Raza = 4.14 cm
Inaltimea = 9.30 cm
Numarul maxim de conserve: 274
```
