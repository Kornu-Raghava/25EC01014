import numpy as np
import matplotlib.pyplot as plt

IS = 1e-12       # A, reverse saturation current (fixed)
Vt = 0.02585        # V, thermal voltage at room temperature
n_list = [1.0, 1.5, 2.0]

vd = np.arange(0, 0.8 + 1e-9, 0.01)  # 0 to 0.8 V in 0.01 V steps

diode_data = {}
for n in n_list:
    id_ = IS * (np.exp(vd / (n * Vt)) - 1)
    diode_data[n] = id_

plt.figure(1, figsize=(8, 6))
for n in n_list:
    plt.plot(vd, diode_data[n] * 1e3, linewidth=2, label=f'$n$ = {n}')

plt.title('Diode $I_D$-$V_D$ Characteristics (Linear Scale)',
          fontsize=14, fontweight='bold')
plt.xlabel('Diode Voltage, $V_D$ (V)', fontsize=12)
plt.ylabel('Diode Current, $I_D$ (mA)', fontsize=12)
plt.legend(title='Ideality factor')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('diode_iv_linear.png', dpi=300)
plt.show()
