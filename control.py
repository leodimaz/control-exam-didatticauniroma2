from BeautifulSoup import BeautifulSoup
import requests
import os.path
#sezione multiurl, includere la parte finale /id/desc/9999
urls = [
'http://didattica.uniroma2.it/files/index/insegnamento/nomeinsegnamento1/id/desc/9999',
'http://didattica.uniroma2.it/files/index/insegnamento/nomeinsegnamento2/id/desc/9999'
]
#section gmail
fromaddr = "tuaemail"
toaddrs  = "tuaemail"
username = "username"
password = "password"

def sendmail(name, link, url):
	import smtplib
	msg = "[  ] Potrebbero essere usciti i risultati\n[  ] Titolo delll'ultimo file inserito: "+str(name)+"\n[+] "+str(link)+"\n[+] "+url
	server = smtplib.SMTP("smtp.gmail.com:587")
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()

def check(url, line):
	file = open("db.txt","r")
	lines = file.read().split("\n")[line]
	r=requests.get(url)
	soup = BeautifulSoup(r.text)
	trs = [tr.find("td").find("a") for tr in soup.findAll('tr',attrs={'class':'even'})]
	#print str(len(trs))+">"+str(int(lines))+"?"
	if len(trs)>int(lines):
		last_insert = trs[0].text
		last_insert_href = "http://didattica.uniroma2.it"+trs[0]['href']
		sendmail(last_insert, last_insert_href, url)
		first(url)

def first(url):
	file = open("db.txt","a")
	r=requests.get(url)
	soup = BeautifulSoup(r.text)
	trs = [tr.text for tr in soup.findAll('tr',attrs={'class':'even'})]
	file.write(str(len(trs))+"\n")
	file.close()

def main():
	current_line = 0
	if os.path.isfile("db.txt"):
		for url in urls:
			check(url, current_line)
			current_line = current_line + 1
	else:
		for url in urls:
			first(url)

if __name__ == "__main__":
	main()
