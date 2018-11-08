from sklearn import datasets ## imports datasets from scikit-learn
import pandas as pd
import statsmodels.api as sm
data = datasets.load_boston() ## loads Boston dataset from datasets library


df = pd.DataFrame(data.data, columns=data.feature_names)
target = pd.DataFrame(data.target, columns=["MEDV"])





X = df["RM"]
y = target["MEDV"]
# Note the difference in argument order
model = sm.OLS(y, X).fit()
predictions = model.predict(X) # make the predictions by the model
# Print out the statistics
model.summary()
print(model.summary())