# import streamlit as st
# import requests

# st.title('SmartPhone Model Data')

# # Fetch data on button click
# but = st.button('Fetch Data')

# if but:
#     url = 'https://api.restful-api.dev/objects'
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()

#         # Extract all model names
#         model_names = ['Select a model'] + [item['name'] for item in data if 'name' in item]  # Adds placeholder

#         # Select box for choosing a specific model
#         selected_model = st.selectbox("Smartphone Models", model_names)

#         if selected_model != 'Select a model':  # Ensure user selects a valid model
#             model_data = next((item for item in data if item['name'] == selected_model), None)

#             if model_data:
#                 st.write('Specifications:', model_data)
#             else:
#                 st.error("No matching model found.")
#     else:
#         st.error("Failed to fetch data.")

import streamlit as st
import requests

st.title('SmartPhone Model Data')

# Fetch data only once when the button is clicked
if "data" not in st.session_state:
    if st.button('Fetch Data'):
        url = 'https://api.restful-api.dev/objects'
        response = requests.get(url)

        if response.status_code == 200:
            st.session_state["data"] = response.json()
        else:
            st.error("Failed to fetch data.")

# Ensure data exists before using it
if "data" in st.session_state:
    data = st.session_state["data"]

    model_names = ['Select a model'] + [item['name'] for item in data if 'name' in item]

    # Preserve selection using session state
    selected_model = st.selectbox("Smartphone Models", model_names, key="selected_model")

    if selected_model != 'Select a model':
        model_data = next((item for item in data if item['name'] == selected_model), None)

        if model_data:
            with st.expander(f'Specifications for {selected_model}:'):
                st.write(model_data)
        else:
            st.error("No matching model found.")