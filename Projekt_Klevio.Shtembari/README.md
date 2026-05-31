%%writefile README.md
# Dy Popullata në Konkurrencë me Kapacitet Mbajtës dhe Sezonshmëri
## Kursi: Modelim në Fizikë

### 1. Qëllimi Shkencor
Ky projekt studion dinamikën ekologjike të dy specieve nën konkurrencë për burime të përbashkëta. Analizohet ndikimi i faktorëve periodikë mjedisorë (sezonshmëria) në kushtet e stabilitetit, bashkëjetesës dhe përjashtimit të njërës specie.

### 2. Ekuacionet Kryesore të Modelit
Evolucioni kohor i popullatave përcaktohet nga sistemi i ekuacioneve diferenciale ordinere (ODE):

$$\frac{dN_1}{dt} = r_1 N_1 \left(1 - \frac{N_1 + \alpha_{12}N_2}{K_1(t)}\right)$$
$$\frac{dN_2}{dt} = r_2 N_2 \left(1 - \frac{N_2 + \alpha_{21}N_1}{K_2}\right)$$

Ku kapaciteti mbajtës sezonal është i formës:
$$K_1(t) = K_{1,0} \cdot \left(1 + A \cdot \sin\left(\frac{2\pi t}{T}\right)\right)$$

### 3. Udhëzimet e Instalimit dhe Ekzekutimit
Instaloni varësitë kryesore shkencore:
```bash
pip install numpy scipy matplotlib pandas
