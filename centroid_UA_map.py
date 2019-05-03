# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:33:54 2019

@author: CWaldoch
"""

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl

plt.close()
mpl.rcdefaults()
# set figure size in inches
mpl.rcParams['figure.figsize'] = 16, 11
mpl.rcParams['font.size'] = 16

df = pd.read_csv(r"C:\Users\cwaldoch\Desktop\urban_area_centroids.csv")

df['size'] = df['POP']**0.35

plt.scatter(df['x'], df['y'], s=df['size'], alpha=0.5)
plt.xlim()
plt.axis('off')
plt.tight_layout()
plt.savefig('UA_centroid.png', dpi=300)