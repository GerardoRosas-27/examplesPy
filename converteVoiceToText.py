import speech_recognition as sr
from pydub import AudioSegment

# Convertir el archivo MP3 a WAV
audio_mp3 = "audio.mp3"
audio_wav = "audio_convertido.wav"
sound = AudioSegment.from_mp3(audio_mp3)
sound.export(audio_wav, format="wav")

# Inicializar el reconocedor de voz
r = sr.Recognizer()

# Cargar el archivo WAV y convertirlo a texto
with sr.AudioFile(audio_wav) as source:
    audio_data = r.record(source)
    try:
        # Configurar el idioma a inglés (en-us) y realizar la conversión a texto
        texto = r.recognize_google(audio_data, language="en-US")
        print("Texto convertido: ", texto)
    except sr.UnknownValueError:
        print("Google Speech Recognition no pudo entender el audio")
    except sr.RequestError as e:
        print("No se pudo solicitar resultados a Google Speech Recognition; {0}".format(e))
