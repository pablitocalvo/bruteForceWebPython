import urllib
import urllib2

#TODO : ottimizzare con controlli ecc.

url = 'http://pablitocalvo.altervista.org/bucaquestosito/controlloPassword.php'
values = {'utente' : 'paolo',
          'password' : 'chiave',
           }					# prepara un oggetto in notazione JSON

data = urllib.urlencode(values)   #"Convert a mapping object or a sequence of two-element tuples to a “percent-encoded” string, suitable to pass to urlopen()"
req = urllib2.Request(url, data)  # prepara la richiesta 	
response = urllib2.urlopen(req)   # apre la connessione richiesta 
the_page = response.read()        
print the_page

