import urllib
import urllib2

url = 'http://pablitocalvo.altervista.org/bucaquestosito/controlloPassword.php'
values = {'utente' : 'paolo',
          'password' : 'chiave',
           }

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page

