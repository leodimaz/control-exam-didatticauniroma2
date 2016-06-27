from BeautifulSoup import BeautifulSoup
import requests
import os.path

#sezione url
url = "link didattica uniroma2 da controllare" #http://didattica.uniroma2.it/files/index/insegnamento/nomedelcorso
#sezione gmail (per ora funziona solamente con questo provider di posta)
fromaddr = "youremail"
toaddrs  = "youremail"
username = "username"
password = "password"

def sendmail(name, link):
	import smtplib
	msg = "[  ] Potrebbero essere usciti i risultati\n[  ] Titolo delll'ultimo file inserito: "+str(name)+"\n[+] "+str(link)+"\n[+] "+url
	server = smtplib.SMTP("smtp.gmail.com:587")
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()

def check():
	file = open("db.txt","r")
	lines = file.read()[0]
	r=requests.get(url)
	soup = BeautifulSoup(r.text)
	trs = [tr.find("td").find("a") for tr in soup.findAll('tr',attrs={'class':'even'})]
	if len(trs)>int(lines):
		last_insert = trs[0].text
		last_insert_href = "http://didattica.uniroma2.it"+trs[0]['href']
		sendmail(last_insert, last_insert_href)
		first()

def first():
	file = open("db.txt","w")
	r=requests.get(url)
	soup = BeautifulSoup(r.text)
	trs = [tr.text for tr in soup.findAll('tr',attrs={'class':'even'})]
	file.write(str(len(trs)))
	file.close()
	check()

def main():
	if os.path.isfile("db.txt"):
		check()
	else:
		first()

if __name__ == "__main__":
	main()

