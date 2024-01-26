import segno #First of all, write 'pip install segno' in your terminal, to add the library

qrcode = segno.make_qr('https://github.com/sia0220') #set your link or anything you wana to be search
qrcode.save('Sia0220.ico', scale=20) #set name and size for your qrcode image(.png)

#Note: scale: set size for your qrcode image