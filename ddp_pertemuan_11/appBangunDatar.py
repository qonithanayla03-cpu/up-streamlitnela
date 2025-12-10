import streamlit as st 

# halaman utama
st.title('aplikasi perhitungan luas bangun datar')
st.header('ini buatan anak SI')

menu = st.sidebar.selectbox('pilih aplikasi',['luas persegi', 'luas segitiga', 'luas lingkaran', 'luas persegi panjang'])

if menu == 'luas persegi':
    st.write('ini halaman untuk menghitung luas persegi')
    st.image('https://www.doyanblog.com/wp-content/uploads/2021/12/rumus-persegi.jpg.webp', caption='gambar persegi')
    sisi = st.number_input('silahkan masukan sisi', min_value=0)
    if st.button('hitung'):
        luas = sisi * sisi
        st.write(f'luas persegi adalah {luas}')

elif menu == 'luas segitiga':
    st.write('ini halaman untuk menghitung luas segitiga')
    st.image('https://thumb.viva.co.id/media/frontend/thumbs3/2022/04/11/6253d9e7da7f4-rumus-luas-segitiga_1265_711.jpg', caption='rumus luas segitiga', width=400)
    def luas_segitiga(alas, tinggi):
        return 0.5 * alas * tinggi
    alas = st.number_input('Masukkan panjang alas segitiga', min_value=0, )
    tinggi = st.number_input('Masukkan tinggi segitiga', min_value=0, )
    if st.button('Hitung Luas Segitiga'):
        luas = luas_segitiga(alas, tinggi)
        st.success(f'Luas Segitiga adalah: {luas}')

elif menu == 'luas lingkaran':
    st.write(':blue[ini halaman untuk menghitung luas lingkaran]:balloon::balloon:')
    st.image('https://www.doyanblog.com/wp-content/uploads/2023/06/rumus-luas-lingkaran.jpg', caption='gambar lingkaran')
    def luaslingkaran(r):
        return 3.14*r*r
    jari_jari = st.number_input('masukan jari-jari lingkaran', min_value=0)
    
    if st.button('hitung'):
        luas = luaslingkaran(jari_jari)
        st.write(f'luas lingkaran adalah {luas}')

elif menu == "Luas Persegi Panjang":
    st.write(':blue[ini halaman untuk menghitung Luas Persegi Panjang]:balloon::balloon:')
    st.image('https://www.doyanblog.com/wp-content/uploads/2023/05/rumus-luas-persegi-panjang.jpg.webp', caption='gambar persegi panjang')
    def luaspersegipanjang(p, l):
        return p*l
    panjang = st.number_input('masukan panjang persegi panjang', min_value=0)
    lebar = st.number_input('masukan lebar persegi panjang', min_value=0)

    if st.button('hitung'):
        luas = luaspersegipanjang(panjang, lebar)
        st.write(f'luas persegi panjang adalah {luas}')
