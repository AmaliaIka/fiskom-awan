import streamlit as st

x = st.number_input('Masukkan angka')
sx = st.text_input('Satuan', 'C')
st.write("Anda memasukkan", x, ' ', sx)
sy = st.text_input('Dikonversi ke', 'C')

def konversi( ):
	if (dari=='C'):
		if (ke=='C'):
			print(x)
		elif (ke=='R'):
			print (x*4/5)
		elif (ke=='F'):
			print ((x+32)*5/9)
		elif (ke=='K'):
			print (x+273)
		else:
			print('masukkan nya salah')	
	elif (dari=='R'):
		if (ke=='C'):
			print(x*5/4)
		elif (ke=='R'):
			print(x)
		elif (ke=='F'):
			print((x+32)*4/9)
		elif (ke=='K'):
			print(x*5/4+273)
		else:
			print('masukkan nya salah')	
	elif (dari=='F'):
		if (ke=='C'):
			print((x+32)*9/5)
		elif (ke=='R'):
			print((x+32)*4/5)
		elif (ke=='F'):
			print(x)
		elif (ke=='K'):
			print(((x+32)*5/9)+273)
		else:
			print('masukkan nya salah')
	elif (dari=='K'):
		if (ke=='C'):
			print(x-273)
		elif (ke=='R'):
			print((x-273)*4/5)
		elif (ke=='F'):
			print((x-273)*9/5+32)
		elif (ke=='K'):
			print(x)
		else:
			print('masukkan nya salah')
	else:
			print('masukkan nya salah')
		
#def penutup( ):
	#print('selesai')
  
st.write(x, ' ', sx, '= ...', sy)
