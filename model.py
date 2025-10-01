# 0. Import necessary libraries
import pandas as pd
import numpy as np

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# 1. Get dataset from sklearn
data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['MedHouseVal'] = data.target

# 2. Data exploration

# i skipped it cuz i'm lazy😴

# 3. Prepare data for training
X = df.drop('MedHouseVal', axis=1)
y = df['MedHouseVal']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the model
lm = LinearRegression()
lm.fit(X_train, y_train)

# 5. Model evaluation
Y_pred = lm.predict(X_test)

mae = metrics.mean_absolute_error(y_test, Y_pred)
rmse = np.sqrt(metrics.mean_absolute_error(y_test, Y_pred))
r2 = metrics.r2_score(y_test, Y_pred)

print(f'Sai số tuyệt đối trung bình (MAE): {mae:.2f}')
print(f'Sai số bình phương trung bình (RMSE): {rmse:.2f}')
print(f'Hệ số xác định (R-squared): {r2:.2f}')


# 6. Save the model
import joblib
joblib.dump(lm, 'linear_regression_model.pkl')
model_columns = list(X.columns)
joblib.dump(model_columns, 'model_columns.pkl')
print("Đã lưu mô hình và các cột thành công!")