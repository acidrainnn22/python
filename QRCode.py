import qrcode
img = qrcode.make("https://www.facebook.com/profile.php?id=100024090734370")
type(img)
img.save("fbhoanganh.png")