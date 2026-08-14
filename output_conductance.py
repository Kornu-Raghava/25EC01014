import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = r"C:\Users\Satya\Desktop\LABS\EDA TASKS\Electrical Data\MOSFET_ID_VDS.csv"

df = pd.read_csv(file_path)
print("Columns:", df.columns)

plt.figure(2, figsize=(10, 6))

highest_vgs = df['V_GS (V)'].max()
ro_kohm = None

for v_gs, group in df.groupby('V_GS (V)'):
    group = group.sort_values('V_DS (V)')
    v_ds = group['V_DS (V)'].values
    i_d = group['I_D (mA)'].values

    gd = np.gradient(i_d, v_ds)  # mA/V = mS

    plt.plot(v_ds, gd, marker='s', linestyle='--', linewidth=2,
             label=f'$V_{{GS}}$ = {v_gs} V')

    if v_gs == highest_vgs:
        # take gd in saturation: average of the last few points (highest V_DS)
        gd_sat = np.mean(gd[-5:])
        ro_kohm = 1 / gd_sat  # mA/V -> kOhm directly (mS <-> 1/kOhm)

plt.title(
    'MOSFET Differential Output Conductance ($g_d = dI_D/dV_{DS}$)', fontsize=14, fontweight='bold')
plt.xlabel('Drain-to-Source Voltage, $V_{DS}$ (V)', fontsize=12)
plt.ylabel('Conductance, $g_d$ (mS)', fontsize=12)
plt.legend(title='Gate-Source Voltage', loc='upper right')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('gd_vds.png', dpi=300)

print(f"\nAt the highest V_GS = {highest_vgs} V:")
print(f"g_d (saturation) = {1/ro_kohm:.4f} mS")
print(f"r_o = 1/g_d = {ro_kohm:.2f} kOhm")

plt.show()
