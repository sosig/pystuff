import httplib
import urllib2
#http get request with headers
host = #http server
headers = {"Content-Type":"text/html","Accept-Encoding":"text/plain","User-Agent":"Mozilla/5.0 (x11; Ubuntu; Linux x86_64) like Gecko"}
conn = httplib.HTTPConnection(host)
conn.request("GET"," "," ", headers) #add content/body and parameters here
