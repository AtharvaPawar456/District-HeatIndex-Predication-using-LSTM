# District-HeatIndex-Predication-using-LSTM
District-HeatIndex-Predication-using-LSTM


# Model Compare Tabel:

| Model | Feature No. | Predicted HEAT_INDEX | Actual HEAT_INDEX | Mean Absolute Error |
|--------------|----------------------|----------------------|----------------------|
| **1** | 8  | 73.28 | 74.71 | 1.43% |
| **2** | 4  | 74.79 | 74.71 | 0.08% |
| **3** | 24 | 73.78 | 74.71 | 0.93% |



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