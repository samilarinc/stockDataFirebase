import urllib.request as urllib2
import json
import pyrebase

config = {
	  "apiKey": "APIkey",
    "authDomain": "domain-1111111111111.firebaseapp.com",
    "databaseURL":"https://appname-1111x-default-rtdb.server-location.firebasedatabase.app",
    "projectId": "appname-1111x",
    "storageBucket": "appname-1111x.appspot.com",
    "messagingSenderId": "1111111111111,
    "appId": "1:111111111111:android:f1f111d111e11df11e1111",
    "measurementId": "G-AAAAAAAAAA",
    "serviceAccount": "C://path/serviceAccount.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

def loader(url, tip):
    temp = urllib2.urlopen(url).read()
    temp = json.loads(temp)
    temp = json.loads(json.dumps(temp['mainEntity']['itemListElement']))
    dict1 = dict()
    eski = db.child(f'database/{tip}').get().val()
    flag = (tip == 'Parite' or tip == 'Menkul' or tip == 'Altin')
    for i in temp:
        if flag:
            u = i['currency'].split('/')
            u = '-'.join(u)            
        else:
            u = i['currency']
        dict1[u] = i['currentExchangeRate']['price']
    db.child(f'database/{tip}').set(dict1)
    db.child(f'database/eski{tip}').set(eski)
    
borsaURL = "https://canlidoviz.com/borsa.jsonld"
kriptoURL = "https://canlidoviz.com/kripto-paralar.jsonld"
dovizURL = "https://canlidoviz.com/doviz-kurlari.jsonld"
pariteURL = "https://canlidoviz.com/pariteler.jsonld"
menkulURL = "https://canlidoviz.com/emtia-fiyatlari.jsonld"
altinURL = "https://canlidoviz.com/altin-fiyatlari.jsonld"

loader(borsaURL, "Borsa")
loader(kriptoURL, "Crypto")
loader(dovizURL, "Doviz")
loader(menkulURL, "Menkul")
loader(pariteURL, "Parite")
loader(altinURL, "Altin")
