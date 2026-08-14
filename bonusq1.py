import numpy as np
import matplotlib.pyplot as plt

IS = 1e-12       # A, reverse saturation current (fixed)
Vt = 0.02585        # V, thermal voltage at room temperature
n_list = [1.0, 1.5, 2.0]

vd = np.arange(0, 0.8, 0.01)  # 0 to 0.8 V in 0.01 V steps

diode_data = {}
for n in n_list:
    id_ = IS * (np.exp(vd / (n * Vt)) - 1)
    diode_data[n] = id_

print(diode_data)
