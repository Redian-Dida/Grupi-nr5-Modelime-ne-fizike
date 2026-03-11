# Grupi-Modelime-ne-fizike
import numpy as np
import matplotlib.pyplot as plt
import os

# Punuar nga: Grupi (Anëtari 1, 2, 3, 4)
# Ky skript përmbush Detyrën 1 dhe Detyrën 3

def detyra_1_figura():
    # Krijimi i vektorit të kohës
    t = np.linspace(0, 10, 1000)
    
   # Funksioni i zgjedhur: f(t) = sin(t) + cos(2t)
   x = np.sin(t) + np.cos(2*t)
  
   # Stilizimi i figurës (Kërkesat e Detyrës 1)
   plt.figure(figsize=(8, 5))
    plt.plot(t, x, color='teal', linewidth=2, linestyle='--', marker='o', markevery=100)
    
  plt.title("Group Signature Plot", fontsize=14, fontname='serif')
    plt.xlabel("t", fontsize=12)
    plt.ylabel("f(t)", fontsize=12)
    plt.grid(True, linestyle=':')
    
  # Ruajtja e figurës (Detyra 2 kërkon folderin figures/)
  if not os.path.exists('figures'):
        os.makedirs('figures')
    plt.savefig('figures/signature_plot.png')
    plt.show()

def detyra_3_numpy():
# 1. Krijoni një vektor kohe në
intervalin [0, 10]
  t = np.linspace(0, 10, 1000)
    
# 2. Definoni një funksion determinist
  f = np.sin(t) + 0.5 * np.cos(3 * t)
    
   # 3. Operacionet e NumPy
   df = np.gradient(f, t) # derivati
    integral = np.cumsum(f) * (t[1] - t[0]) # integrali kumulativ
    norm = np.linalg.norm(f) # norma e vektorit
    
   # Raportimi i rezultateve (Sipas pikave në faqen 3)
  print(f"Norma e vektorit: {norm}")
    print(f"Maksimumi i funksionit: {np.max(f)}")
    print(f"Minimumi i funksionit: {np.min(f)}")
    print(f"Vlera mesatare: {np.mean(f)}")

if __name__ == "__main__":
    detyra_1_figura()
    detyra_3_numpy()
