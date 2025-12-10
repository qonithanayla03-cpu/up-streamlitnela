import streamlit as st 

# halaman utama
st.title('aplikasi perhitungan luas bangun datar')
st.header('ini buatan anak SI')

menu = st.sidebar.selectbox('pilih aplikasi',['luas persegi', 'luas segitiga', 'luas lingkaran'])

if menu == 'luas persegi':
    st.write('ini halaman untuk menghitung luas persegi')
    st.image('https://www.doyanblog.com/wp-content/uploads/2021/12/rumus-persegi.jpg.webp', caption='gambar persegi')
    sisi = st.number_input('silahkan masukan sisi', min_value=0)
    if st.button('hitung'):
        luas = sisi * sisi
        st.write(f'luas persegi adalah {luas}')

             

elif menu == 'luas segitiga':
    st.write('ini halaman untuk menghitung luas segitiga')