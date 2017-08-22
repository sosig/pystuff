adar = []
ri = os.popen('netstat -r | grep default').read() #routing table contains the interface name
rs = ri.split(" ")
rh = rs[-1].rstrip() #last item in the array is the interface
xs = os.popen('ifconfig ' + rh + ' | grep inet').read() 
xv = xs.split(' ') #turns interface listing into an array...
xd = xv.index('inet') #this is the index prior to the one containing the ip...
xi = xd + 1 #...and plus 1 is the IP
xs = xv[xi] #retrieving ip
if 'addr:' in xs:
    xn = xs[5:]
else:
    xn = xs
print xn
