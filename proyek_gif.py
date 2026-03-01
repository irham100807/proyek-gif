import imageio.v3 as iio

fileNames =['gambar-1.jpeg','gambar-2.jpeg']
images=[]

for filename in fileNames:
    images.append(iio.imread(filename))

iio.imwrite('imup.gif', images, duration=500, loop=0)

print('GIF berhasil dibuat')