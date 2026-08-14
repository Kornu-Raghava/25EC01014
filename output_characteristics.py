import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = r'C:\Users\Satya\Desktop\HANDOUTS\EDA TOOLS\Electrical Data\Electrical Data\MOSFET_ID_VDS.csv'

df = pd.read_csv(file_path)
print("Columns:", df.columns)

plt.figure(1, figsize=(10, 6))

for v_gs, group in df.groupby('V_GS (V)'):
    group = group.sort_values('V_DS (V)')
    plt.plot(group['V_DS (V)'], group['I_D (mA)'], marker='o', linewidth=2,
             label=f'$V_{{GS}}$ = {v_gs} V')

plt.title(
    'MOSFET Output Characteristics ($I_D$ vs $V_{DS}$)', fontsize=14, fontweight='bold')
plt.xlabel('Drain-to-Source Voltage, $V_{DS}$ (V)', fontsize=12)
plt.ylabel('Drain Current, $I_D$ (mA)', fontsize=12)
plt.legend(title='Gate-Source Voltage', loc='upper left')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('id_vds.png', dpi=300)
plt.show()
