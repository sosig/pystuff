#script to check status of ssh server
host = #host that has the ssh server 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
prs = connect_ex((host,22))
s.close()
if prs:
    return
else:
    print host + ":22"
