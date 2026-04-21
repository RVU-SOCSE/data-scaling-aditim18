import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, Normalizer


df = pd.read_csv('salary.csv')

print("Original Dataset:")
print(df.head())



X = df.select_dtypes(include=['int64', 'float64'])

print("\nNumerical Data:")
print(X.head())



print("\nStandard Scaled Data:")

scaler = StandardScaler()
X_standard = scaler.fit_transform(X)

df_standard = pd.DataFrame(X_standard, columns=X.columns)
print(df_standard.head())



print("\nMin-Max Scaled Data:")

minmax = MinMaxScaler()
X_minmax = minmax.fit_transform(X)

df_minmax = pd.DataFrame(X_minmax, columns=X.columns)
print(df_minmax.head())



print("\nNormalized Data:")

norm = Normalizer()
X_norm = norm.fit_transform(X)

df_norm = pd.DataFrame(X_norm, columns=X.columns)
print(df_norm.head())
