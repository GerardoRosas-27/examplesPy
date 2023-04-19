from PIL import Image, ImageDraw, ImageFont

# Descarga la imagen de fondo
import urllib.request
url = "https://images.rawpixel.com/image_1000/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvdjM1Mi1udW5vb24tNDAtcGxhbm5pbmctZWxlbWVudF8yLmpwZw.jpg"
urllib.request.urlretrieve(url, "background.jpg")

# Cargar la imagen de fondo
background_img = Image.open('background.jpg')

# Crear un objeto ImageDraw para agregar el texto
draw = ImageDraw.Draw(background_img)

# Definir la fuente y el texto que se va a agregar
font = ImageFont.truetype("arial.ttf", 36)
text = "Texto sobre la imagen"

# Obtener el tamaño del texto
text_width, text_height = draw.textsize(text, font)

# Calcular la posición en la que se va a agregar el texto
x = (background_img.width - text_width) // 2
y = (background_img.height - text_height) // 2

# Agregar el texto a la imagen
draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))

# Guardar la imagen con el texto agregado
background_img.save("image_with_text.jpg")
print('termino')