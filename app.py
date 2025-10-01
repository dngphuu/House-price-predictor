import streamlit as st
import pandas as pd
import joblib

# Load the trained model and model columns
try:
    model = joblib.load('linear_regression_model.pkl')
    model_columns = joblib.load('model_columns.pkl')
except FileNotFoundError:
    st.error("Lỗi: Không tìm thấy file mô hình. Hãy chắc chắn bạn đã chạy script để lưu mô hình trước.")
    st.stop()


def user_input_features():
    med_inc = st.sidebar.slider('Thu nhập trung bình (MedInc)', 1.0, 15.0, 8.3)
    house_age = st.sidebar.slider('Tuổi nhà (HouseAge)', 1.0, 52.0, 25.0)
    avg_rooms = st.sidebar.slider('Số phòng trung bình (AveRooms)', 2.0, 10.0, 5.5)
    avg_bedrms = st.sidebar.slider('Số phòng ngủ trung bình (AveBedrms)', 0.5, 5.0, 1.1)
    population = st.sidebar.slider('Dân số (Population)', 200.0, 10000.0, 1500.0)
    avg_occup = st.sidebar.slider('Số người ở trung bình (AveOccup)', 1.0, 10.0, 2.5)
    latitude = st.sidebar.slider('Vĩ độ (Latitude)', 32.0, 42.0, 34.0)
    longitude = st.sidebar.slider('Kinh độ (Longitude)', -124.0, -114.0, -118.0)

    data = {
        'MedInc': med_inc,
        'HouseAge': house_age,
        'AveRooms': avg_rooms,
        'AveBedrms': avg_bedrms,
        'Population': population,
        'AveOccup': avg_occup,
        'Latitude': latitude,
        'Longitude': longitude
    }
    features = pd.DataFrame(data, index=[0])
    return features


input_df = user_input_features()

# Display the user input features
st.subheader("Thông số bạn đã nhập:")
st.write(input_df)

if st.button("Dự đoán"):
    query = pd.DataFrame(input_df, columns=model_columns)
    prediction = model.predict(query)
    st.success(f"Giá nhà dự đoán là: ${prediction[0] * 100000:,.2f}")