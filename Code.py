import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="white")
# Load data
d = pd.read_csv("data.csv", index_col=0)
# Compute the correlation matrix
corr = d.corr()
# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))
# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))
# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)
# Add correlation coefficients to heatmap
annot_kws = {"fontsize":7,"color":"k"}   #"fontstyle":"italic", "fontweight":"bold"
sns.heatmap(corr, mask=mask, cmap=cmap, annot=True, annot_kws=annot_kws,
            fmt=".2f", center=0, square=True, linewidths=.5,
            cbar_kws={"shrink": .5})
plt.show()






