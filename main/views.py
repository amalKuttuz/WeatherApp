from django.shortcuts import render,HttpResponse
import requests
from bs4 import BeautifulSoup

def home(request):
    city = request.GET.get('city')

    city = city.replace(" ", "+")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE

    html = session.get(f'https://www.google.com/search?q=weather+{city}').text
#  return render(request, "home.html")
    return html


def result(request):
    try:

        cg=None
        if 'city' in request.GET:
            # city=request.GET.get['city']
            html=home(request)
            cg=dict()
            soup=BeautifulSoup(html,'html.parser')
            cg['region'] = soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
            cg['temp_now'] = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text

        return render(request, 'home.html',{'cg':cg})
    except:
        return HttpResponse("No valid city found")
