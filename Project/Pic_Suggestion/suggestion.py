import requests as r
from bs4 import BeautifulSoup
import random

urls={
    'happy':'https://www.dreamstime.com/photos-images/vacation-grassland.html',
    'sad':'https://www.dreamstime.com/photos-images/family-vacation.html',
    'suprise':'https://www.dreamstime.com/photos-images/scary-places.html',
    'neutral':'https://www.dreamstime.com/photos-images/scenary.html',
    'angry':'https://www.dreamstime.com/search.php?securitycheck=4327fd1aec8957a902653beb616d4540&srh_field=calm%20nature&lastsearchvalue=calm%20nature&s_all=n&s_ph=y&s_il=n&s_video=n&s_audio=n&s_ad=n&s_wp=y&s_sl0=y&s_sl1=y&s_sl2=y&s_sl3=y&s_sl4=y&s_sl5=y&s_rf=y&s_ed=y&s_orp=y&s_orl=y&s_ors=y&s_orw=y&s_clc=y&s_clm=y&s_rsf=0&s_rst=7&sortcriteria=2',
    'disgust':'https://www.dreamstime.com/search.php?securitycheck=4327fd1aec8957a902653beb616d4540&srh_field=pleasant%20places&lastsearchvalue=musical%20places&s_all=n&s_ph=y&s_il=n&s_video=n&s_audio=n&s_ad=n&s_wp=y&s_sl0=y&s_sl1=y&s_sl2=y&s_sl3=y&s_sl4=y&s_sl5=y&s_rf=y&s_ed=y&s_orp=y&s_orl=y&s_ors=y&s_orw=y&s_clc=y&s_clm=y&s_rsf=0&s_rst=7&sortcriteria=2',
    'fear':'https://www.dreamstime.com/photos-images/baby-smiling.html'
    
}

def get_images(emo):
    global urls
    url = urls[emo]
    img = []
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    result = r.get(url, headers=headers)
    print(result.status_code)
    soup = BeautifulSoup(result.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
    for i in soup.find_all('img'):
        
            img.append(i.get('data-src'))

            print(img)
        
    random.shuffle(img)
    return img