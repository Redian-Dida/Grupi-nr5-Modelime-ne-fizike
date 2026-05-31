import os
import numpy as np
import matplotlib.pyplot as plt


def model(z, t, r1, r2, a12, a21, K1_0, K2_0, amp):
    N1, N2 = z
    K1 = K1_0 * (1 + amp * np.sin(2 * np.pi * t / 365))
    dN1 = r1 * N1 * (1 - (N1 + a12 * N2) / K1)
    dN2 = r2 * N2 * (1 - (N2 + a21 * N1) / K2_0)
    return [dN1, dN2]


def simulate_population(t, z0, params):
    res = [z0]
    for i in range(len(t) - 1):
        dt = t[i + 1] - t[i]
        d = model(res[-1], t[i], *params)
        next_z = [max(0, res[-1][j] + d[j] * dt) for j in range(2)]
        res.append(next_z)
    return np.array(res)


def plot_population(t, data, output_path):
    plt.figure(figsize=(10, 6), dpi=100)
    plt.plot(t, data[:, 0], label='Popullata N1', color='blue', linewidth=2.5)
    plt.plot(t, data[:, 1], label='Popullata N2', color='red', linewidth=2.5, linestyle='--')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.title('Dinamika e Popullatave (Eksperimenti 1)', fontsize=14, fontweight='bold', family='serif')
    plt.xlabel('Koha (t)', fontsize=11, family='serif')
    plt.ylabel('Madhësia e Popullatës', fontsize=11, family='serif')
    plt.legend(loc='upper right', frameon=True, shadow=True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def run_experiment(
    output_dir='figures',
    output_file='eksperimenti_1.png',
    total_time=500,
    num_steps=1000,
    z0=(2.0, 1.5),
    params=(0.5, 0.5, 0.2, 0.2, 10, 10, 0.1),
):
    os.makedirs(output_dir, exist_ok=True)
    t = np.linspace(0, total_time, num_steps)
    data = simulate_population(t, z0, params)
    output_path = os.path.join(output_dir, output_file)
    plot_population(t, data, output_path)
    return output_path
