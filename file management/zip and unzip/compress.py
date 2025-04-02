from zipfile import *
f = ZipFile('image.zip','w',ZIP_DEFLATED)

f.write('Errors.png')

f.close()