from sklearn.datasets import fetch_california_housing

dataset = fetch_california_housing(as_frame=True)
df = dataset.frame

print(df.head())
print(df.shape)
