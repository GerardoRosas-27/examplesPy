from PIL import Image, ImageDraw, ImageFont
import imageio

# Tamaño de la imagen
width = 256
height = 256

# Creamos una lista de colores
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Creamos una lista de imágenes, cada una con el texto de un color diferente
images = []
for i in range(len(colors)):
    # Creamos una nueva imagen en blanco
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))

    # Dibujamos el texto en la imagen
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', 20)  # Tamaño de fuente inicial
    text = 'Texto animado'
    text_width, text_height = draw.textsize(text, font)
    x = (width - text_width) / 2
    y = (height - text_height) / 2

    # Animamos el cambio de tamaño del texto
    for j in range(10):
        # Incrementamos el tamaño de fuente
        font_size = 20 + j * 4
        font = ImageFont.truetype('arial.ttf', font_size)

        # Redibujamos el texto en la imagen con el tamaño de fuente actual
        text_width, text_height = draw.textsize(text, font)
        x = (width - text_width) / 2
        y = (height - text_height) / 2
        draw.text((x, y), text, font=font, fill=colors[i])

        # Agregamos la imagen a la lista
        images.append(image.copy())

    # Animamos la reducción del tamaño del texto
    for j in range(10, 0, -1):
        # Disminuimos el tamaño de fuente
        font_size = 20 + j * 4
        font = ImageFont.truetype('arial.ttf', font_size)

        # Redibujamos el texto en la imagen con el tamaño de fuente actual
        text_width, text_height = draw.textsize(text, font)
        x = (width - text_width) / 2
        y = (height - text_height) / 2
        draw.text((x, y), text, font=font, fill=colors[i])

        # Agregamos la imagen a la lista
        images.append(image.copy())

# Creamos el archivo GIF animado
imageio.mimsave('animacion2.gif', images, duration=0.1)
