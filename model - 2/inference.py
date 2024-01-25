import pickle
from tensorflow.keras.models import load_model

# Load the model
loaded_model = load_model('lstm_model_selected_feature.h5')

# Load the district_index
with open('district_index.pkl', 'rb') as f:
    loaded_district_index = pickle.load(f)

# Load the input feature name list
with open('feature_names_selected_feature.pkl', 'rb') as f:
    loaded_feature_names = pickle.load(f)

# Assuming new_data is the input data for prediction with the selected features
new_data = pd.DataFrame({
    'T2M': [0.325153],
    'T_Fahrenheit': [72.91],
    'TS': [0.336126],
    'T2M_MIN': [0.431715],
    'T2M_MAX': [0.305014],
    'T2MWET': [0.631997],
    'WS10M_RANGE': [0.164191],
    'DISTRICT_INDEX': [10],
})

# Map the 'DISTRICT' column to numerical indices
# new_data['DISTRICT_INDEX'] = new_data['DISTRICT'].map(loaded_district_index)

# Keep only the relevant features
new_data = new_data[loaded_feature_names]

# Normalize the features using the previously fitted scaler
new_data_scaled = scaler.transform(new_data)

# Reshape features for LSTM input
new_data_reshaped = np.reshape(new_data_scaled, (new_data_scaled.shape[0], 1, new_data_scaled.shape[1]))

# Make predictions for HEAT_INDEX
heat_index_prediction = loaded_model.predict(new_data_reshaped)

pred_Heat_index = round(heat_index_prediction.flatten()[0], 2)

# Print predicted HEAT_INDEX
print("Predicted HEAT_INDEX:", pred_Heat_index)


# --------------------------------------------
# Model Accuracy Measure Section
# --------------------------------------------

# Assuming you have the true HEAT_INDEX value for comparison
true_heat_index =  74.71      # Provide the true value here

# Calculate Mean Absolute Error (MAE)
mae = round(np.mean(np.abs(pred_Heat_index - true_heat_index)), 6)

# Print predicted HEAT_INDEX and MAE
print("Predicted HEAT_INDEX:\t", pred_Heat_index)
print("Actual HEAT_INDEX: \t", true_heat_index)
print("\nMean Absolute Error:", mae , "%")


'''
Predicted HEAT_INDEX:	 74.79

Actual HEAT_INDEX: 	 74.71

Mean Absolute Error: 0.080001 %
'''