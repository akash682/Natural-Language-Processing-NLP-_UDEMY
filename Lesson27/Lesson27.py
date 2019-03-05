import numpy as np
import pandas as pd

# Series
# pd.Series(self, data=None, index=None, dtype=None, name=None, copy = False, fas

x = pd.Series([1,2,3,4,5])

x + 100

(x ** 2) + 100

x > 2

# any and all
larger_than_2 = x>2
larger_than_2.any()
larger_than_2.all()

# apply
def f(x):
    if x %2 == 0:
        return x **2
    else:
        return x**3

x.apply(f)

x.astype(np.float64)

# Copy
x
y = x
y[0] = 100

x = pd.Series([1,2,3,4,5])
y = x.copy()

y[0] = 100
y

# Dataframes
# pd.DataFrame(self, data = NOne, index=None, columns =None, dtype = None, compy =False)

data = [1,2,3,4,5,6,7,8,9]
df = pd.DataFrame(data, columns = ["x"])

# One column as a series
dataSeries = df["x"]

# Adding more cclumns
df["x_plus_2"] = df["x"] + 2

df["x_square"] = df["x"] **2
df["x_factorial"] = df["x"].apply(np.math.factorial)

df["is_even"] = df["x"]%2

# Dropping/Deleting columns
df = df.drop("is_even", 1)

df[["x","x_plus_2"]]

df.describe()

# Readomg datasets
dataset = pd.read_csv('Demographic_Statistics_By_Zip_Code.csv')