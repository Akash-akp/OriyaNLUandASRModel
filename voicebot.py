import requests
import subprocess
from gtts import gTTS
import speech_recognition as sr
from io import BytesIO
from playsound import playsound
from googletrans import Translator
# translator = Translator(service_urls=[
#           'translate.google.com',
#           'translate.google.co.kr',
#         ])

translator = Translator()
translation = translator.translate("Thank you", dest='or')
print(translation.text)


myText = "Samsung Assistant"

language = 'en'

myobj = gTTS(text = myText,lang=language,slow=False)

myobj.save("welcome.mp3")

playsound("welcome.mp3")
# subprocess.call(['mpg123','welcome.mp3'])


bot_message = ""
message = ""
while bot_message != 'Bye':
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak anything :")
        audio = r.listen(source)
        try:
            message = r.recognize_google(audio)
            print("You said : {}".format(message))
        except:
            print("Sorry!! could not recognize your voice....")
    if len(message) == 0:
        continue
    print('Sending message now')

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message":message})

    print("Bot says, ",end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{i['text']}")
    
    # bot_message = translator.translate(bot_message,dest="or").text
    print(translator.translate(bot_message,dest="or").text)
    # print(txt.text)
    myobj = gTTS(text = bot_message,lang='en')
    myobj.save("welcome.mp3")
    playsound("welcome.mp3")
