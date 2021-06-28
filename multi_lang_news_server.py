#voice news server
import requests
import json
from win32com.client import Dispatch
def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
if __name__=='__main__':
    speak("welcome to the voice news server")
    print("welcome to the voice news server")
    url = ('http://newsapi.org/v2/top-headlines?'
        'country=in&'
        'apiKey=32660387c6c64430a69dc51ccca9624d')
    news_request = requests.get(url).text

    news_diction = json.loads(news_request)
    Article = news_diction['articles']
    for article in Article:
        print(article['title'])
        speak(article['title'])
        speak("to know more about the news, click on the mentioned link.")
        print(article['url'])
        speak("starting next news.")