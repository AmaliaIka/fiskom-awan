import streamlit as st

x = st.number_input('Masukkan angka')
sx = st.text_input('Satuan', 'C')
st.write("Anda memasukkan", x, ' ', sx)
sy = st.text_input('Dikonversi ke', 'C')
y = 0
def konversi( ):
	if (sx=='C'):
		if (sy=='C'):
			y = x
		elif (sy=='R'):
			y = (x*4/5)
		elif (sy=='F'):
			y = ((x+32)*5/9)
		elif (sy=='K'):
			y = (x+273)
		else:
			'masukkan nya salah'
	elif (sx=='R'):
		if (sy=='C'):
			y = (x*5/4)
		elif (sy=='R'):
			y = x
		elif (sy=='F'):
			y = ((x+32)*4/9)
		elif (sy=='K'):
			y = (x*5/4+273)
		else:
			'masukkan nya salah'
	elif (sx=='F'):
		if (sy=='C'):
			y = ((x+32)*9/5)
		elif (sy =='R'):
			y = ((x+32)*4/5)
		elif (sy=='F'):
			y = x
		elif (sy=='K'):
			y = (((x+32)*5/9)+273)
		else:
			'masukkan nya salah'
	elif (sx=='K'):
		if (sy=='C'):
			y = (x-273)
		elif (sy=='R'):
			y = ((x-273)*4/5)
		elif (sy=='F'):
			y = ((x-273)*9/5+32)
		elif (sy=='K'):
			y = x
		else:
			'masukkan nya salah'
	else:
			'masukkan nya salah'
		
#def penutup( ):
	#print('selesai')
  
st.write(x, ' ', sx, ' = ', y, sy)
