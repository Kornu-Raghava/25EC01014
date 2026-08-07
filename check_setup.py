# check_setup
import sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

print("Python : ", sys.version.split()[0])
print("numpy : ", np.__version__)
print("pandas : ", pd.__version__)
print("matplotlib : ", matplotlib.__version__)

plt.plot([0, 1, 2, 3], [0, 1, 4, 9], marker="o")
plt.title("Hey people! How are you doing")
plt.xlabel("x")
plt.ylabel("x squared")
plt.grid(True)
plt.show()
