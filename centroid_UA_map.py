# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl

plt.close()
mpl.rcdefaults()
# set figure size in inches
mpl.rcParams['figure.figsize'] = 16, 11
mpl.rcParams['font.size'] = 16

df = pd.read_csv(r"C:\Users\cwaldoch\Desktop\urban_area_centroids.csv")

#df['size'] = df['POP']**0.45
df['size'] = [1 if x <20000 else x**0.45 for x in df['POP'].values]
plt.scatter(df['x'], df['y'], s=df['size'], alpha=0.5)
plt.xlim()
plt.axis('off')
plt.tight_layout()
plt.savefig('UA_centroid_dual_rule.png', dpi=300)
