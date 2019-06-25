import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# contained all the car information
filename = 'clean_df.csv'

df = pd.read_csv(filename)
# print(df.head(10))

# x = df['engine-size']
# y = df['price']
# plt.style.use('bmh')

# plt.scatter(x, y)
# plt.title('Scatter plot of Engine vs Price')
# plt.xlabel('Engine-size')
# plt.ylabel('Price')

# plt.show()
# print(plt.style.available)
df_test = df[['drive-wheels', 'body-type', 'price']]

df_grp = df_test.groupby(['drive-wheels', 'body-type'], as_index=False).mean()
# print(df_grp)
# using pivot for readability
df_pivot = df_grp.pivot(index='drive-wheels', columns='body-type')


# create heat map
fig, ax = plt.subplots()
im = ax.pcolor(df_pivot, cmap='RdBu')

# label names
row_labels = df_pivot.columns.levels[1]
col_labels = df_pivot.index

# move ticks and labels to the center
ax.set_xticks(np.arange(df_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(df_pivot.shape[0]) + 0.5, minor=False)

# insert labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

# rotate label if too long
plt.xticks(rotation=90)

fig.colorbar(im)
plt.show()
