# **Precise Irrigation: Smart Watering System for Sustainable Farming**

## **Problem Statement**

### Background
Over-irrigation is a prevalent issue in agriculture, causing significant water wastage, soil degradation, and reduced crop yields. Precision irrigation is essential for sustainable farming, particularly in regions with limited water resources. By efficiently utilizing water, farmers can conserve resources and enhance crop productivity.

### Key Statistics
- **70%** of global freshwater withdrawals are attributed to agriculture.
- Inefficient irrigation practices result in **30-60%** water wastage.
- Overwatering contributes to nutrient leaching, soil erosion, and long-term productivity loss.

---

## **Issue**
Farmers often lack precise data about when and how much to irrigate. Current irrigation methods rely on guesswork or outdated schedules that fail to account for soil conditions, weather forecasts, and crop requirements. This leads to:
- Water wastage.
- Poor crop health and yield.
- Increased operational costs.

---

## **Objective**
To develop a smart irrigation system that uses real-time sensor data and weather forecasts to provide precise recommendations for:
- The optimal duration of watering.
- Necessary adjustments based on soil and weather conditions.

---

## **Requirements**
- A model that predicts watering duration using sensor data and weather forecasts.
- Lightweight design for deployment on low-power devices like Raspberry Pi.
- Scalable and adaptable for various crops and field layouts.

---

## **Technical Details**

### **Workflow**
1. **Data Collection:**
   - Sensors capture soil moisture, temperature, and pH levels.
   - Weather data, including rainfall predictions and temperature forecasts, is retrieved via the OpenWeather API.

2. **Data Processing:**
   - Normalize and preprocess sensor and weather data.
   - Integrate real-time sensor readings with weather forecasts.

3. **Model Prediction:**
   - The AI model predicts the optimal watering duration based on processed data.

4. **Recommendations:**
   - Generate actionable insights for farmers through a user-friendly interface.

---

### **Why Regression?**
A regression model was chosen because it provides a continuous prediction of watering duration. This ensures precise, actionable recommendations rather than broad categorical advice.

---

### **Sensors and Inputs**
- **Soil Moisture Sensor**: Measures soil moisture levels (1-100).
- **Temperature Sensor**: Captures current and forecasted temperatures (0-40°C).
- **Rain Prediction**: Probabilities for the next 2, 8, 16 hours, and 1 day.
- **Crop Type**: Encoded as follows:
  - 1 = Rice
  - 2 = Wheat
  - 3 = Barley
  - 4 = Legumes
  - 5 = Sugarcane
- **Rain Volume**: 0-2 (where 2 indicates heavy rainfall).

---

### **Model Used**
The system employs a lightweight regression model to:
- Predict watering duration.
- Dynamically adjust predictions as more data is collected, improving performance over time.

---

### **Challenges Addressed**
- **Data Imbalance**: Mitigated by collecting diverse training samples for different soil and weather conditions.
- **Sensor Noise**: Data is filtered and normalized for reliability.
- **Field Variability**: Model design adapts to various field setups and crop types.

---

## **Future Plans**
- Expand sensor compatibility for broader applications.
- Incorporate additional crop types and soil conditions.
- Develop a mobile app for remote monitoring and recommendations.
- Introduce AI-driven feedback loops for real-time model refinement.

---

## **Installation and Usage**

### **Hardware Setup**
1. Install soil moisture, temperature, and pH sensors in a grid across the field.
2. Connect sensors to a Raspberry Pi or similar device.

### **Software Setup**
1. Clone this repository:
   ```bash
   git clone https://github.com/SparshJainChajjed/S.A.I---Smart-Autonomous-Irrigation-Irrigation-/.git
