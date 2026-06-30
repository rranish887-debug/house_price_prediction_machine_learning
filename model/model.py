# run this at end of the day 19.2.ipynb to make predictions 
# Random Forest Regressor is the best among the 3 models

# Random Forest Regressor

import joblib

joblib.dump(rf_pipeline, "random_forest_model.pkl")

print("Model saved successfully")

import joblib

model = joblib.load("random_forest_model.pkl")

# Make predictions
predictions = model.predict(X_test)
print(predictions[:5])

# run this at end of the day 19.2.ipynb to make predictions 
# Random Forest Regressor is the best among the 3 models
