import joblib

model = joblib.load('Model_RF_PRICE')

model.predict([[2020,5000000,70,45,6000,1.1,0,1]])