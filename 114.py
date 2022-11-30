import urllib
import urllib.request

try:
    site=urllib.request.urlopen('http://www.jw.org')
except:
    print('Deu erro')
else:
    print('Tudo okay')
   # print(site.read()) mostra o site inteiro HTML
