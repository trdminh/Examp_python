import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def data_preprocessing_pipeline(data):

    numeric_features = data.select_dtypes(include=['float', 'int']).columns
    categorical_features = data.select_dtypes(include=['object']).columns


    data[numeric_features] = data[numeric_features].fillna(data[numeric_features].mean())


    for feature in numeric_features:
        Q1 = data[feature].quantile(0.25)
        Q3 = data[feature].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - (1.5 * IQR)
        upper_bound = Q3 + (1.5 * IQR)
        data[feature] = np.where((data[feature] < lower_bound) | (data[feature] > upper_bound),
                                 data[feature].mean(), data[feature])


    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data[numeric_features])
    data[numeric_features] = scaler.transform(data[numeric_features])


    data[categorical_features] = data[categorical_features].fillna(data[categorical_features].mode().iloc[0])

    return data
data = pd.read_csv("data.csv")
cleaned_data = data_preprocessing_pipeline(data)

print("Preprocessed Data:")
print(cleaned_data)