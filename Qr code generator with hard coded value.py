import qrcode as qr

img = qr.make("https://chat.openai.com/")
img.save("Chatgpt_Qr.png")

img = qr.make("https://prepinstaprime.com/")
img.save("Prepinsta_QR.png")