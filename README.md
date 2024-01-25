# District-HeatIndex-Predication-using-LSTM
District-HeatIndex-Predication-using-LSTM


# Model Compare Table:

| Model | Feature No. | Test Loss | Test Accuracy | Predicted HEAT_INDEX | Actual HEAT_INDEX | Mean Absolute Error |
|-------|-------------|-----------|---------------|----------------------|-------------------|---------------------|
| **1** | 8  | 1.52 | 90.45 | 73.28 | 74.71 | 1.43% |
| **2** | 4  | 1.50 | 90.16 | 74.79 | 74.71 | 0.08% |
| **3** | 25 | 0.34 | 40.56 | 73.9 | 74.71 | 0.91% |

- model 2 shows best performance as its Mean Absolute Error is very less than Model 1 and Model 3...

# Features for each Model:

- **Model 1** : 
    `['T2M', 'T_Fahrenheit', 'TS', 'T2M_MIN', 'T2M_MAX', 'T2MWET', 'WS10M_RANGE', 'DISTRICT_INDEX']`
- **Model 2** : 
    `['T2M','RH2M', 'T2MDEW', 'WD10M']`
- **Model 3** : 
    `['T2M', 'T_Fahrenheit', 'TS', 'T2M_MIN', 'T2M_MAX', 'T2MWET', 'WS10M_RANGE', 'WD50M', 'WD10M', 'WS10M_MAX', 'RH2M', 'MO', 'WS10M', 'T2MDEW', 'QV2M', 'WS50M', 'LON', 'DISTRICT_INDEX', 'LAT', 'PS', 'PRECTOTCORR', 'YEAR', 'T2M_RANGE', 'DY', 'WS10M_MIN']`



## Project Overview:

### Title:
HeatIndex Prediction using LSTM

### Description:
LSTM models predict Heat Index with varying feature sets. Model 2 excels, showcasing superior performance with fewer features.

### Problem Statement:
Predict Heat Index based on meteorological features for improved understanding of weather conditions and human comfort.

### Abstract:
This project utilizes LSTM models to predict Heat Index, comparing performance with different feature sets. Model 2, with 4 selected features, outperforms others.

### Application:
- Weather Forecasting
- Urban Planning
- Health and Safety
- Agriculture
- Energy Consumption
- Outdoor Event Planning

### Advantages:
- Accurate Heat Index Prediction
- Reduced Model Complexity (Model 2)
- Better Interpretability (Model 2)
- Faster Training and Inference (Model 2)
- Improved Resource Efficiency

### Limitations:
- Limited Feature Set
- Potential Overfitting
- Sensitivity to Input Data Quality
- Lack of External Factors
- Model Generalization Challenges

### Future Scope:
- Include Additional Relevant Features
- Explore Advanced LSTM Architectures
- Fine-Tune Hyperparameters
- Integrate External Data Sources
- Develop Real-time Prediction Capability

## About Dataset:

### Features:
- **T2M** : Temperature at 2 meters (in degrees Celsius).
- **T_Fahrenheit** : Temperature at 2 meters converted to Fahrenheit.
- **TS** : Surface temperature (in degrees Celsius).
- **T2M_MIN** : Minimum temperature at 2 meters (in degrees Celsius).
- **T2M_MAX** : Maximum temperature at 2 meters (in degrees Celsius).
- **T2MWET** : Wet-bulb temperature at 2 meters (in degrees Celsius).
- **WS10M_RANGE** : Wind speed at 10 meters range (difference between maximum and minimum) (in meters per second).
- **WD50M** : Wind direction at 50 meters (in degrees).
- **WD10M** : Wind direction at 10 meters (in degrees).
- **WS10M_MAX** : Maximum wind speed at 10 meters (in meters per second).
- **RH2M** : Relative humidity at 2 meters (percentage).
- **MO** : Month.
- **WS10M** : Wind speed at 10 meters (in meters per second).
- **T2MDEW** : Dew point temperature at 2 meters (in degrees Celsius).
- **QV2M** : Specific humidity at 2 meters (in grams per kilogram).
- **WS50M** : Wind speed at 50 meters (in meters per second).
- **LON** : Longitude.
- **DISTRICT_INDEX** : Numerical index representing the district.
- **LAT** : Latitude.
- **PS** : Surface pressure (in pascals).
- **PRECTOTCORR** : Corrected total precipitation (in millimeters).
- **YEAR** : Year.
- **T2M_RANGE** : Temperature range at 2 meters (in degrees Celsius).
- **DY** : Day.
- **WS10M_MIN** : Minimum wind speed at 10 meters (in meters per second).

### Dataset Information:
- Rows: 125,060
- Columns: 25
- Memory Usage: 23.9 MB



## About LSTM Algo:

### Explaination
LSTM (Long Short-Term Memory) is a type of recurrent neural network (RNN) designed for sequence prediction. In our project, LSTM is applied to time-series meteorological data to learn patterns and predict heat index.

### Application
- Meteorological Forecasting
- Public Health Planning
- Urban Planning for Heat Resilience
- Agriculture Heat Stress Monitoring
- Energy Consumption Forecasting
- Outdoor Event Planning

### Advantages
- Captures Long-Term Dependencies
- Handles Time-Series Data Effectively
- Suitable for Complex Patterns
- Avoids Vanishing Gradient Problem
- Allows End-to-End Learning

### Limitations
- Requires Sufficient Data
- May Overfit with Limited Data
- Computationally Intensive
- Hyperparameter Sensitivity
- Limited Interpretability

### Future Scope
- Enhance Model Robustness
- Incorporate Additional Features
- Explore Ensemble Approaches
- Integrate Real-Time Data
- Extend to Multiple Locations


# --------------------------------------------------------------

# Model 1: (8 Feature)

- selected_features :
` ['T2M', 'T_Fahrenheit', 'TS', 'T2M_MIN', 'T2M_MAX', 'T2MWET', 'WS10M_RANGE', 'DISTRICT_INDEX']`

- input_data :
`pd.DataFrame({
    'T2M': [0.325153],
    'T_Fahrenheit': [72.91],
    'TS': [0.336126],
    'T2M_MIN': [0.431715],
    'T2M_MAX': [0.305014],
    'T2MWET': [0.631997],
    'WS10M_RANGE': [0.164191],
    'DISTRICT_INDEX': [10],
})`

- Output
`Predicted HEAT_INDEX:	 73.28
Actual HEAT_INDEX: 	 74.71
Mean Absolute Error: 1.430001 %`

# Model 2: (4 Feature)

- selected_features :
`['T2M','RH2M', 'T2MDEW', 'WD10M']`

- input_data :
`pd.DataFrame({
    'T2M': [0.325153],
    'RH2M': [0.733267],
    'T2MDEW': [0.766538],
    'WD10M': [0.614839],
})`

- Output
`Predicted HEAT_INDEX:	 74.79
Actual HEAT_INDEX: 	 74.71
Mean Absolute Error: 0.080001 %`


# Model 3: (25 Feature)

- selected_features :
`['T2M', 'T_Fahrenheit', 'TS', 'T2M_MIN', 'T2M_MAX', 'T2MWET', 'WS10M_RANGE', 'WD50M', 'WD10M', 'WS10M_MAX', 'RH2M', 'MO', 'WS10M', 'T2MDEW', 'QV2M', 'WS50M', 'LON', 'DISTRICT_INDEX', 'LAT', 'PS', 'PRECTOTCORR', 'YEAR', 'T2M_RANGE', 'DY', 'WS10M_MIN']`

- input_data :
`pd.DataFrame({
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
})`

- Output
`Predicted HEAT_INDEX:	 73.8
Actual HEAT_INDEX: 	 74.71
Mean Absolute Error: 0.909997 %`