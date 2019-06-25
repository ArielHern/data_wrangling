import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# contained all the car information
filename = 'clean_df.csv'

df = pd.read_csv(filename)
plt.style.use('fivethirtyeight')

"""
posituve linerar relationship - As the engine-size goes up, the
price goes up: this indicates a positive direct correlation between
these two variables. Engine size seems like a pretty good predictor of
price since the regression line is almost a perfect diagonal line.
"""
sns.regplot(x='engine-size', y='price', data=df)
plt.ylim(0)
plt.show()

"""
As the highway-mpg goes up, the price goes down: this indicates an
inverse/negative relationship between these two variables. Highway
mpg could potentially be a predictor of price.
"""
sns.regplot(x='highway-mpg', y='price', data=df)
plt.show()

""" Peak rpm does not seem like a good predictor of the price at all
since the regression line is close to horizontal. """
sns.regplot(x="peak-rpm", y="price", data=df)
plt.show()
