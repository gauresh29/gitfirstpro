#akhabar padhake sunao
import json
import requests
def speak(str):
    from win32com.client import Dispatch
    speak= Dispatch("SAPI.SpVoice")
    speak.speak(str)

if __name__ == '__main__':
    speak("this is way you talk")
    news = requests.get("https://newsapi.org/v2/top-headlines?q=trump&apiKey=32419d46f3294a7b8729fdd910392ae0")
    predict = news.text
    #print(type(predict))
    setw = json.loads(predict)
    #print(typ(setw))
    newss= setw['articles']
    print(newss)
    for article in newss:
        print(article['title'])
        speak(article['title'])
    speak("Ajake samachar khatam ")