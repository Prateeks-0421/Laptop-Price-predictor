import streamlit as st
import numpy as np 

import pickle

pipe = pickle.load(open("pipe.pkl", "rb"))
df = pickle.load(open("df.pkl", "rb"))

st.title("Laptop price predictor")

st.write("Enter the required specifications :  ")

company = st.selectbox("Brand", df["Company"].unique())

type = st.selectbox("Type", df["TypeName"].unique())

ram = st.selectbox("RAM (in GB)", df["Ram"].unique())

weight = st.number_input("Weight of the laptop")

touchscreen = st.selectbox("Touchscreen", ["Yes", "No"])

ips = st.selectbox("IPS", ["Yes", "No"])

screen_size = st.number_input("Screen Size")

resolution = st.selectbox("Screen Resolution", [ '1920*1080', '1366*768', '2560*1440', '3840*2160' ])

cpu = st.selectbox("CPU ", df["Cpu brand"].unique())

hdd = st.selectbox("HDD (in GB)", df["HDD"].unique())

ssd = st.selectbox("SSD (in GB)", df["SSD"].unique())

gpu = st.selectbox("GPU", df["Gpu brand"].unique())

os = st.selectbox("Operating System", df["Operating System"].unique())


if st.button("Predict Price"):
    resolution_x = int(resolution.split("*")[0])
    resolution_y = int(resolution.split("*")[1])
    ppi = ((resolution_x**2) + (resolution_y**2))**0.5/screen_size
    if touchscreen == "Yes":
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == "Yes":
        ips = 1
    else:
        ips = 0
    query = np.array([company, type, ram, weight, touchscreen, ips ,ppi, cpu, hdd, ssd, gpu, os])
    
    query = query.reshape(1, 12)

    st.title("The Predicted Price of the laptop with these requirements is " + str(np.exp(pipe.predict(query)[0]).round(2))  )

    # st.title("The predicted price of the laptop with these requirements is " + str(np.exp(pipe.predict(query)[0]).round(2)))

 
    st.write("Note: The price is in Indian Rupees (INR) and is an estimate based on the specifications provided. Actual prices may vary based on market conditions and other factors.")



# Custom footer using HTML + CSS

footer = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #0E1117;
    color: white;
    text-align: center;
    padding: 10px;
}
</style>
<div class="footer">
    <p>© Developer - Prateek singh  |  NIT Jalandhar</p>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)

# st.markdown("Developed by : Prateek Singh - IT 3rd Year , NIT Jalandhar ")



