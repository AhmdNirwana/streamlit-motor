import pickle
import streamlit as st

lrmodel = pickle.load(open('estimasi_motor.sav', 'rb'))

st.title('Estimasi Harga Motor Bekas')

selling_price = st.number_input('Input Harga Jual')
year = st.number_input('Input Tahun Motor')

predict = ''

if st.button('Estimasi Harga') :
    predict = lrmodel.predict(
        [[selling_price,year]]
    )
    st.write ('Estimasi Harga Motor Bekas : ', predict)
