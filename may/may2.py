# Akhabar padhake sunao

try:
    # import pywin32
    from win32com.client import Dispatch

    def speak(str):
        speak = Dispatch("SAPI.SpVoice")
        speak.Speak(str)


    if __name__ == '__main__':

        import requests
        import json

        speak("News for today")
        url = r"https://newsapi.org/v2/everything?q=apple&from=2022-05-19&to=2022-05-19&sortBy=popularity&apiKey=8f4762e8f97347239ad9435e197997ec"
        news_dict = requests.get(url).text
        print(news_dict["articles"])
        arts = news_dict['articles']

        for article in arts:
            speak(articles['title'])
            speak("Moving on to the next news....")

except Exception as e:
    print(e)