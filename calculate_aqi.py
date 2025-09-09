import pandas as pd
import numpy as np

# --- Step 1: Load dataset ---
# Replace with your CSV path
df = pd.read_csv("./AirQualityUCI.csv", sep=';', decimal=',', dayfirst=True)

# --- Step 2: Convert pollutants to numeric ---
pollutants = ['CO(GT)', 'C6H6(GT)', 'NOx(GT)', 'NO2(GT)']
for col in pollutants:
    df[col] = pd.to_numeric(df[col], errors='coerce')  # convert, set invalid as NaN

# --- Step 3: CPCB breakpoints ---
# Format: (Concentration Low, Concentration High, AQI Low, AQI High)
breakpoints = {
    'CO(GT)': [(0,1.0,0,50),(1.1,2.0,51,100),(2.1,10,101,200),(10.1,17,201,300),
                (17.1,34,301,400),(34.1,np.inf,401,500)],
    'NO2(GT)': [(0,40,0,50),(41,80,51,100),(81,180,101,200),(181,280,201,300),
                 (281,400,301,400),(401,np.inf,401,500)],
    'NOx(GT)': [(0,40,0,50),(41,80,51,100),(81,180,101,200),(181,280,201,300),
                 (281,400,301,400),(401,np.inf,401,500)],
    'C6H6(GT)': [(0,1,0,50),(1.1,2,51,100),(2.1,5,101,200),(5.1,10,201,300),
                  (10.1,20,301,400),(20.1,np.inf,401,500)]
}

# --- Step 4: Function to calculate AQI for one pollutant ---
def calc_individual_aqi(pollutant, value):
    for bp_low, bp_high, aqi_low, aqi_high in breakpoints[pollutant]:
        if bp_low <= value <= bp_high:
            aqi = ((aqi_high - aqi_low)/(bp_high - bp_low))*(value - bp_low) + aqi_low
            return round(aqi)
    return None  # if value is outside all breakpoints

# --- Step 5: Function to calculate AQI for one row ---
def calculate_aqi_row(row):
    aqi_values = []
    for p in breakpoints.keys():  # only pollutants with breakpoints
        value = row.get(p, None)
        if pd.notna(value):
            aqi = calc_individual_aqi(p, value)
            if aqi is not None:
                aqi_values.append(aqi)
    if aqi_values:
        return max(aqi_values)  # final AQI = max of all pollutants
    else:
        return np.nan

# --- Step 6: Apply function to all rows ---
df['AQI'] = df.apply(calculate_aqi_row, axis=1)

# --- Step 7: Save to new CSV ---
df.to_csv("AirQualityUCI_with_AQI.csv", index=False)
print("AQI calculation complete! Saved to AirQualityUCI_with_AQI.csv")
