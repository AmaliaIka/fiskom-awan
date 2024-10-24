import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import random
from matplotlib.patches import Circle

# Title
st.title(':sparkles: UTS Fisika Komputasi Awan :sparkles:')

# Header
st.header('Amalia Ika Sriyani/210322607258')

# Membuat lingkaran utama dengan radius 1
circle = Circle((0, 0), 1, color = 'black', fill = False, linewidth = 3, linestyle = '-', alpha = 0.3)

# Inisialisasi list untuk menyimpan titik
x = [0]
y = [0]
color = [0.0, 0.7, 0.0]
size = [371]

# Membuat tombol untuk menghasilkan data acak
if st.button("Data"):
    for i in range(111):
        # Menghasilkan x, y acak dalam rentang [-1, 1]
        x0 = 2*(random.random() - .5)
        y0 = 2*(random.random() - .5)
        # Memeriksa apakah titik berada di dalam lingkaran utama 
        if ((x0**2+y0**2) > 1.):
            if y0 > 0:
                y0 = np.sqrt(1-x0**2)
            else:
                y0 = -1*(np.sqrt(1-x0**2))
                
        # Menambahkan titik baru    
        x.append(x0)
        y.append(y0)
        color.append((random.random(), random.random(), random.random()))
        size.append(3713*random.random() )

# Membuat figure
fig, ax = plt.subplots(figsize = (16, 16))
ax.add_patch(circle)

# Menggambar garis dari pusat ke titik
for i in range(1, len(x)):
    ax.plot([0, x[i]], [0, y[i]], color = 'black', linestyle = '--', alpha = 0.3)

# Plot scatter untuk titik
ax.scatter(x, y, c=color, s=size, alpha=0.5) 

# Membuat plot 
ax.set_ylabel("y")
ax.set_xlabel("x")
ax.tick_params(axis = 'y', labelsize = 20)
ax.tick_params(axis = 'x', labelsize = 20)
ax.set_title('Data Acak yang Berubah Setiap Tombol Ditekan')
ax.grid(True, linestyle = '-.')
ax.tick_params(labelcolor = 'r', labelsize = 'medium', width = 3)
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
st.pyplot(fig)
st.caption("Lingkaran dengan ukuran dan warna acak dan tersebar didalam lingkaran dengan radius 1")
