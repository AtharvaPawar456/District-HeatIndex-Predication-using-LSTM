import pickle
from tensorflow.keras.models import load_model

# Load the model
loaded_model = load_model('lstm_model_all_feature.h5')

# Load the district_index
with open('district_index.pkl', 'rb') as f:
    loaded_district_index = pickle.load(f)

# Load the input feature name list
with open('feature_names_all_feature.pkl', 'rb') as f:
    loaded_feature_names = pickle.load(f)


# selected_features = ['T2M', 'T_Fahrenheit', 'TS', 'T2M_MIN', 'T2M_MAX', 'T2MWET', 'WS10M_RANGE', 'WD50M', 'WD10M', 'WS10M_MAX', 'RH2M', 'MO', 'WS10M', 'T2MDEW', 'QV2M', 'WS50M', 'LON', 'DISTRICT_INDEX', 'LAT', 'PS', 'PRECTOTCORR', 'YEAR', 'T2M_RANGE', 'DY', 'WS10M_MIN']

new_data_for_inference = pd.DataFrame({
'T2M'             :  [0.325153],
'T_Fahrenheit'       :  [72.91],
'TS'              :  [0.336126],
'T2M_MIN'         :  [0.431715],
'T2M_MAX'         :  [0.305014],
'T2MWET'          :  [0.631997],
'WS10M_RANGE'     :  [0.164191],
'WD50M'           :  [0.609584],
'WD10M'           :  [0.614839],
'WS10M_MAX'       :  [0.175806],
'RH2M'            :  [0.733267],
'MO'    :                   [1],
'WS10M'           :  [0.176881],
'T2MDEW'          :  [0.766538],
'QV2M'            :  [0.549058],
'WS50M'           :  [0.208062],
'LON'               :  [79.293],
'DISTRICT_INDEX'    :      [10],
'LAT'               :  [19.366],
'PS'               :  [0.43377],
'PRECTOTCORR'     :  [0.031997],
'YEAR'            :      [2001],
'T2M_RANGE'       :  [0.367852],
'DY'              :         [1],
'WS10M_MIN'       :  [0.139295],
})




# Normalize the features using the previously fitted scaler
new_data_scaled = scaler.transform(new_data_for_inference)

# Reshape features for LSTM input
new_data_reshaped = np.reshape(new_data_scaled, (new_data_scaled.shape[0], 1, new_data_scaled.shape[1]))

# Make predictions for HEAT_INDEX
heat_index_prediction = model.predict(new_data_reshaped)

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
print('''
# 3. LSTM with All Feature

selected_features = ['T2M', 'T_Fahrenheit', 'TS', 'T2M_MIN', 'T2M_MAX', 'T2MWET', 'WS10M_RANGE', 'WD50M', 'WD10M', 'WS10M_MAX', 'RH2M', 'MO', 'WS10M', 'T2MDEW', 'QV2M', 'WS50M', 'LON', 'DISTRICT_INDEX', 'LAT', 'PS', 'PRECTOTCORR', 'YEAR', 'T2M_RANGE', 'DY', 'WS10M_MIN']

''')
print("Predicted HEAT_INDEX:\t", pred_Heat_index)
print("Actual HEAT_INDEX: \t", true_heat_index)
print("\nMean Absolute Error:", mae , "%")


'''
Predicted HEAT_INDEX:	 73.8

Actual HEAT_INDEX: 	 74.71

Mean Absolute Error: 0.909997 %
'''