from django.shortcuts import render ,redirect
import json
import urllib.request
# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=97f476dee0cf24a3fd18a19988b3242c').read()
        json_data = json.loads(res)
        data ={
             'country': str(json_data['sys']['country']),
             'cordinates': str(json_data['coord']['lon'])+''+str(json_data['coord']['lat']),
             'temp':str( json_data['main']['temp'])+'k',
             'pressure':str(json_data['main']['pressure']),
             'humidity':str(json_data['main']['humidity']),
 
          }
    else:
        city=''
        data={}    
    return render(request, 'index.html',{ "data":data ,"city":city})    
