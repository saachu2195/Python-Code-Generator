import qrcode

img = qrcode.make('Hi, Sachin here')
type(img)
img.save("sample.png")

## Some Advanced Feature
import qrcode
img2 = qrcode.QRCode(version=1,
                    error_correction=qrcode.ERROR_CORRECT_M,
                    box_size=10, border=1
)

img2.add_data("This is custom format of QR Code")
img2.make(fit=True)

final_image = img2.make_image(fill_color = "blue", back_color = "white")
final_image.save("Final_Image.png")

## Saving the QR Code into SVG format
import qrcode.image.svg

final_image.save("Final2_image.png")

