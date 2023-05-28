import whisper

import pyaudio
import wave
from pydub import AudioSegment


def converteVoiceToText():
    model = whisper.load_model("base")
    result = model.transcribe("audio1.mp3")
    print(result["text"])


def grabar_audio(nombre_archivo, duracion):
    chunk = 1024
    formato = pyaudio.paInt16
    canales = 2
    tasa_muestreo = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=formato,
                    channels=canales,
                    rate=tasa_muestreo,
                    input=True,
                    frames_per_buffer=chunk)

    print("Grabando audio...")

    frames = []

    for i in range(0, int(tasa_muestreo / chunk * duracion)):
        data = stream.read(chunk)
        frames.append(data)

    print("Grabación finalizada.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    # Guardar el archivo de audio en formato WAV
    wf = wave.open(nombre_archivo, 'wb')
    wf.setnchannels(canales)
    wf.setsampwidth(p.get_sample_size(formato))
    wf.setframerate(tasa_muestreo)
    wf.writeframes(b''.join(frames))
    wf.close()

    # Convertir el archivo WAV a MP3
    audio = AudioSegment.from_wav(nombre_archivo)
    audio.export(nombre_archivo + '.mp3', format='mp3')

    print("El audio se ha guardado como:", nombre_archivo + '.mp3')

# Ejemplo de uso: grabar audio durante 5 segundos y guardarlo como 'grabacion.mp3'
grabar_audio('grabacion', 5)
#converteVoiceToText()

