from gtts import gTTS

# Lista de textos a convertir a audio
textos = ["The developer fixed a bug the customer",    "The project met the deadline the stakeholders",    "The tester reported an issue the development team",    "The user set a preference the account settings",    "The application loaded the user interface the browser",
          "The team lead presented the project status the management",    "The server handled the request the client",    "The program initialized the variables the memory",    "The API returned a JSON object the requestor",    "The website redirected the user a different page",    "The software installed a plugin the user"]


# Iterar sobre la lista de textos y crear un archivo de audio diferente para cada uno
for i, texto in enumerate(textos):
    # Crear objeto gTTS y convertir texto a audio
    tts = gTTS(text=texto, lang='en', slow=True)

    # Guardar archivo de audio con nombre diferente
    tts.save(f"audioLento3{i}.mp3")
