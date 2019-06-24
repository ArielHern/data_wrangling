import pandas as pd
from matplotlib import pyplot as plt

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
print(df_pivot)
