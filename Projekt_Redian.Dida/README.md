#Projekti 2: Renditje rezistente ndaj spam-it dhe eksperiment me link farm
Punoi;Redian Dida
Grupi nr.5

1. Qëllimi Shkencor
Ky projekt studion metodat e renditjes së faqeve në web (PageRank) dhe dobësitë e tyre ndaj
teknikave manipuluese të njohura si "Link Farms". Qëllimi është ndërtimi i një sistemi hibrid që
identifikon këto struktura përmes metrikave të rrjetit dhe aplikon penalizime për të ruajtur
integritetin e renditjes.

2. Modeli Matematik Orientues
Renditja finale llogaritet përmes funksionit hibrid:
Si = wP Pi + wR Ri + wQ Qi − wS Spi
Në këtë implementim, fokusi është te faktori Spi (Spam Score), i cili llogaritet si raporti i lidhjeve
dalëse të faqes ndaj maksimumit të lejuar në rrjet. Pesha wS përdoret për të rregulluar ashpërsinë e
penalizimit.

3. Hapat Metodologjikë
1. Ndërtimi i Grafit: Krijimi i një matrice fqinjësie që simulon një rrjet normal me shtimin e
një "link farm" artificial.
2. Llogaritja e PageRank: Përdorimi i metodës iterative me faktor shpërndarjeje d = 0.85.
3. Analiza e Spam-it: Identifikimi i faqeve që kanë densitet të lartë lidhjesh dalëse.
4. Krahasimi: Ballafaqimi i rezultateve midis modelit standard dhe atij me penalizim aktiv.

4. Strukturimi i Repozitorit
project_name/├── README.md
├── requirements.txt
├── src/
│├── ranking/
││├── pagerank.py
││└── hybrid_penalty.py
├── scripts/
│
└── run_link_farm_experiment.py
└── results/
└── figures/
└── eksperimenti_2.png
5. Udhëzime për Ekzekutim
Për të riprodhuar rezultatet, përdorni komandat e mëposhtme:
# Instalimi i varësive
pip install numpy matplotlib
# Ekzekutimi i kodit
python scripts/run_link_farm_experiment.py

6. Diskutimi i Rezultateve dhe Kufizimet
Kufizimet:
• Modeli mund të shfaqë "False Positives" duke penalizuar faqe që janë thjesht direktoritë
legjitime.
• Faktori i spam-it është i thjeshtësuar dhe nuk analizon përmbajtjen semantike të faqeve.
• Mungesa e të dhënave dinamike bën që modeli të jetë efektiv vetëm për rrjete statike.

7.Kodi i Implementuar (Python)
 
import numpy as np
import matplotlib.pyplot as plt# Matrica e fqinjësisë (shembull)
adj = np.array([[0,1,1,0,0],[1,0,1,0,0],[1,1,0,1,0],[0,0,0,0,1],
[0,0,0,1,0]])
def calculate_pagerank(M, d=0.85):
n = len(M)
v = np.ones(n) / n
M_norm = M / np.where(M.sum(axis=1)[:, None] == 0, 1, M.sum(axis=1)[:,
None])
for _ in range(50): v = (1 - d) / n + d * (M_norm.T @ v)
return v
P = calculate_pagerank(adj)
Sp = adj.sum(axis=1) / np.max(adj.sum(axis=1))
S = P - 0.1 * Sp # Aplikimi i penalizimit
