import streamlit as st
import time

st.title('Welcome to Pizza Mania')
st.subheader('Baked with streamlit')
st.text("Your first interactive app.")
st.write("Your favorite pizza.")


def Details():
    
    st.sidebar.write('Login')
    name = st.sidebar.text_input("Enter Your Name")
    age = st.sidebar.number_input("Enter your Age",min_value = 1, max_value = 120)
    sub = st.sidebar.button('Submit')
    if sub:
        return True

if Details:
    order = st.selectbox('You Pizza:',['','Panner Pizza','Veggie Pizza','Chicken Pizza','Capsicum Pizza'])

    if order:

        pizza_size = st.radio('Pizza Size:',['Small','Medium','Large'])

        cheese = st.checkbox('Extra Chesse')
        toppings = st.checkbox('Extra topings')

        confirm = st.button('Confirm Order')

        if confirm:
            messg = st.write(f'You Order: {pizza_size} {order}. Excellent choice!')

        if confirm:
            time.sleep(5)
            st.success("Your pizza is ready to be served!")

if __name__ == '__main__':
    Details()