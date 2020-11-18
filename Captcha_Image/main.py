from captcha.image import ImageCaptcha

image = ImageCaptcha()

image.write(input("Enter digits or alphabet: "), "saveas.png")
print("Captcha is created!!!")
