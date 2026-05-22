import numpy as np
import matplotlib.pyplot as plt
import os
import sys

script_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(script_dir)

from src.ranking import calculate_pagerank, get_spam_score, calculate_hybrid_score
# --- Eksperimenti 2: Drejtues i renditjes rezistente ndaj spam-it ---
# Punoi: Redian Dida
# Grupi nr.5

figures_dir = os.path.join(script_dir, 'figures')
if not os.path.exists(figures_dir):
    os.makedirs(figures_dir)

# Matrica e fqinjësisë 
adj = np.array([[0,1,1,0,0],[1,0,1,0,0],[1,1,0,1,0],[0,0,0,0,1],[0,0,0,1,0]])

def main():
    P = calculate_pagerank(adj)

    Sp = get_spam_score(adj)

    S = calculate_hybrid_score(P, Sp, weight=0.1)

    # --- Grafiku i Stilizuar ---
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

    # Ruajtja e grafikut
    plt.savefig(os.path.join(figures_dir, 'eksperimenti_2.png'))
    print(f"Grafiku u ruajt me sukses te dosjen '{figures_dir}'.")
    plt.show()

if __name__ == "__main__":
    main()
