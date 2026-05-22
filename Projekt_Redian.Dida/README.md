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

**3. Hapat Metodologjikë**

1. Ndërtimi i Grafit: Krijimi i një matrice fqinjësie që simulon një rrjet normal me shtimin e
një "link farm" artificial.
2. Llogaritja e PageRank: Përdorimi i metodës iterative me faktor shpërndarjeje d = 0.85.
3. Analiza e Spam-it: Identifikimi i faqeve që kanë densitet të lartë lidhjesh dalëse.
4. Krahasimi: Ballafaqimi i rezultateve midis modelit standard dhe atij me penalizim aktiv.

**4. Strukturimi i Repozitorit**
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
**5. Udhëzime për Ekzekutimin**

​1.Instaloni libraritë e nevojshme:
pip install numpy  dhe matplotlib
ose
pip install -r requirements.txt
2.​Ekzekutoni eksperimentin ne terminal:
python eksperimenti_2.py

**6.Kodi i Implementuar (Python)**
 
import numpy as np
import matplotlib.pyplot as plt
import os
if not os.path.exists('figures'): os.makedirs('figures')

#Eksperimenti 2:Drejtues i renditjes rezistente ndaj spam-it;pergjegjes per eksperimentin link farm.
#Punoi;Redian Dida
#Grupi nr.5

adj = np.array([[0,1,1,0,0],[1,0,1,0,0],[1,1,0,1,0],[0,0,0,0,1],[0,0,0,1,0]])

def calculate_pagerank(M, d=0.85):
    n = len(M)
    v = np.ones(n) / n
    M_norm = M / np.where(M.sum(axis=1)[:, None] == 0, 1, M.sum(axis=1)[:, None])
    for _ in range(50): v = (1 - d) / n + d * (M_norm.T @ v)
    return v

P = calculate_pagerank(adj)
Sp = adj.sum(axis=1) / np.max(adj.sum(axis=1))
S = P - 0.1 * Sp

#Grafiku i Stilizuar

plt.figure(figsize=(10, 6), dpi=100)
faqet = [f"Faqja {i}" for i in range(len(P))]
x = np.arange(len(faqet))

plt.bar(x - 0.2, P, 0.4, label='PageRank (Standard)', color='blue', edgecolor='black', alpha=0.8)
plt.bar(x + 0.2, S, 0.4, label='Me Penalizim', color='red', edgecolor='black', alpha=0.8)
plt.plot(x + 0.2, S, 'ro', markersize=4)

plt.grid(True, linestyle='--', alpha=0.6)
plt.title('Rezistenca ndaj Spam-it (Eksperimenti 2)', fontsize=14, fontweight='bold', family='serif')
plt.xlabel('Faqet e Web-it', fontsize=11, family='serif')
plt.ylabel('Score', fontsize=11, family='serif')
plt.xticks(x, faqet)
plt.ylim(0, 0.45)
plt.legend(loc='upper right', frameon=True, shadow=True)
plt.savefig('figures/eksperimenti_2.png')
plt.show()
     
