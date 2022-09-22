def report():
    import requests, json
    city="Delhi"
    api_key="68bf9a180bf784cbc9004b41eef278b7"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    url=base_url+"appid="+api_key+"&q="+city
    response=requests.get(url)
    x=response.json()
    print(x)
    if x['cod']!=401:
        print("city name: ",x['name'])
        print("weather: ",x['weather'])
        print("weather: ",x['weather'][0]['main'])
        print("temperature: ",x['main']['temp'])
        print("minimum temp: ",x['main']['temp_min'])
        print("maximum temp: ",x['main']['temp_max'])
    else:
        print("city not found")