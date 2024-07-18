import qrcode

# img = qrcode.make("Hello world!! The first QR code generated")


qr = qrcode.QRCode( # creates a new QR Code that allows for further customization
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10, #size of each pixels inside the created qr code
    border=4 #space from the link to the qr code

)

qr.add_data('https://github.com/Clinton-John')
qr.make(fit=True)

img = qr.make_image(fill_color='black', black_color="white")
img.save("Githublink.png")