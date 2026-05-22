## Projekti 2: Renditje rezistente ndaj spam-it dhe eksperiment me link farm

**Punoi:** Redian Dida

**Grupi:** nr.5

**1. Qëllimi i Eksperimentit**

Ky projekt analizon algoritmin PageRank dhe dobësitë e tij kur përballet me teknika manipuluese si "Link Farms". Fokusimi kryesor është ndërtimi i një modeli hibrid që identifikon këto struktura përmes densitetit të lidhjeve dhe aplikon penalizime për të ruajtur renditjen reale të faqeve.

**2. Modeli Matematik**

Renditja finale llogaritet përmes funksionit hibrid:
Si = wP Pi + wR Ri + wQ Qi − wS Spi
Për këtë implementim:
​Pi: PageRank score standard.
​Spi: Spam Score (llogaritet bazuar në numrin e lidhjeve dalëse).
​wS: Pesha e penalizimit.

**3.Projekti do të;**

1. Llogarisë PageRank standard.
2. Llogarisë një score spam-i për çdo faqe.
3. Llogarisë vlerat e renditjes me penalizim spam.
4. Gjenerojë një grafik dhe ta ruajë në `figures/eksperimenti_2.png`.


**4. Hapat Metodologjikë janë;**

1. Ndërtimi i Grafit: Krijimi i një matrice fqinjësie që simulon një rrjet normal me shtimin e
një "link farm" artificial.
2. Llogaritja e PageRank: Përdorimi i metodës iterative me faktor shpërndarjeje d = 0.85.
3. Analiza e Spam-it: Identifikimi i faqeve që kanë densitet të lartë lidhjesh dalëse.
4. Krahasimi: Ballafaqimi i rezultateve midis modelit standard dhe atij me penalizim aktiv.

**5. Strukturimi i Repozitorit**

├── Projekt_Redian.Dida

│    └──scripts/

│     ├── Eksperimenti_2.py

│     ├── requirements.txt

│     ├──README.md

│    └──src/

│           ├── _init_.py     
│           └── ranking.py  

│    └── figures/

│           └── eksperimenti_2.png

└──README.md

**6. Udhëzime për Ekzekutimin**

​1.Instaloni libraritë e nevojshme:

pip install numpy  dhe matplotlib
ose

pip install -r requirements.txt

2.​Ekzekutoni eksperimentin ne terminal:

python eksperimenti_2.py
