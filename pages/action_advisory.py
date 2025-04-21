import streamlit as st
import requests
from transformers import pipeline, GPT2LMHeadModel, GPT2Tokenizer

# --- Weather API Key ---
weather_api_key = "f354473f1f7e5f9023ed7cc4659fab5f"
base_url = "http://api.openweathermap.org/data/2.5/weather"

# --- State & City Mapping ---
state_city_map = {
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Agra"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
    "Delhi": ["New Delhi"]
}

# --- Weather-Based Advice ---
def get_weather_advice(temperature, humidity, description, wind_speed):
    advice = []
    if temperature > 35:
        advice.append("☀️ High temperature: Prefer evening/morning irrigation.")
    if humidity < 30:
        advice.append("💧 Low humidity: Increase irrigation frequency.")
    if "clear" in description:
        advice.append("🌞 Clear sky: Great for pesticide spraying or harvesting.")
    if wind_speed > 10:
        advice.append("💨 High wind: Avoid spraying pesticides/fertilizers.")
    return advice

# --- Load GPT2 Model (Stable) ---
@st.cache_resource
def load_model():
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    return pipeline("text-generation", model=model, tokenizer=tokenizer)

text_gen_pipe = load_model()

# --- Streamlit UI ---
st.title("🌾 Farmify: Weather & AI Crop Advisory")

selected_state = st.selectbox("Select State", list(state_city_map.keys()))
selected_city = st.selectbox("Select City", state_city_map[selected_state])

if st.button("Get Weather & Advisory"):
    params = {
        "q": selected_city,
        "appid": weather_api_key,
        "units": "metric"
    }
    res = requests.get(base_url, params=params)

    if res.status_code == 200:
        data = res.json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        hum = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        st.subheader(f"✅ Weather in {selected_city}, {selected_state}")
        st.markdown(f"🌡️ Temperature: **{temp}°C**")
        st.markdown(f"🌥️ Description: **{desc.title()}**")
        st.markdown(f"💧 Humidity: **{hum}%**")
        st.markdown(f"💨 Wind Speed: **{wind} m/s**")

        st.subheader("📋 Manual Advice")
        advice = get_weather_advice(temp, hum, desc, wind)
        for point in advice:
            st.markdown(f"- {point}")

        st.subheader("🤖 AI Recommendation")
        prompt = (
            f"Suggest crops and farming advice for a region with temperature {temp}°C, "
            f"{desc}, humidity {hum}%, wind speed {wind} m/s in {selected_city}, {selected_state}.\n"
            f"Give advice in bullet points:\n"
        )

        result = text_gen_pipe(prompt, max_length=150, num_return_sequences=1)[0]['generated_text']
        for line in result.split("\n"):
            if line.strip():
                st.markdown(f"- {line.strip()}")

    else:
        st.error("Failed to fetch weather data.")
