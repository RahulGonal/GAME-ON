import qrcode
qr=qrcode.QRCode(
	version=1,
	box_size=10,
	border=5

	)

data=(str(input('Enter Data or Link to be stored in the QrCode: ')))
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("QrVideo.png") 