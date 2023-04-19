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
    font = ImageFont.truetype('arial.ttf', 40)  # Cambiamos el tamaño de la fuente
    text = 'Texto animado'
    text_width, text_height = draw.textsize(text, font)
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    draw.text((x, y), text, font=font, fill=colors[i])

    # Agregamos la imagen a la lista
    images.append(image)

# Creamos el archivo GIF animado
imageio.mimsave('animacion1.gif', images, duration=0.5)

# Abre el archivo GIF y extrae cada cuadro
#with Image.open('animacion.gif') as im:
#    frames = []
#    for frame in range(im.n_frames):
#        im.seek(frame)
#        frames.append(im.copy())

# Guarda la animación en formato WebP
#frames[0].save('animacion.webp', format='webp', append_images=frames[1:], save_all=True, duration=im.info['duration'], loop=0)
