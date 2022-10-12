import requests
import base64
import urllib
from requests_html import HTMLSession

image_url = "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"
img = open("album/test.jpg",'wb')
img64=base64.b64decode(image_url)
img.write(img64)
img.close()

def main():
    album="La corrida"
    artiste="Francis Cabrel"
    url="https://www.bing.com/images/search?q="+urllib.parse.quote(artiste+" "+album)+"&form=HDRSC2&first=1&tsc=ImageHoverTitle"
    try:
        session = HTMLSession()
        headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0"} 
        response = session.get(url,headers=headers)
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(e)

if __name__=='__main__':
    main()