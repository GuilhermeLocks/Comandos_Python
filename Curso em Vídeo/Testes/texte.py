# Exemplo: gTTS
from gtts import gTTS
texto = "Olá, mundo!"
tts = gTTS(text=texto, lang='pt')
tts.save("ola.mp3")
