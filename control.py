from BeautifulSoup import BeautifulSoup
import requests
import os.path

#sezione multiurl, includere la parte finale /id/desc/9999
urls = [
'http://didattica.uniroma2.it/files/index/insegnamento/insegnamento1/id/desc/9999',
'http://didattica.uniroma2.it/files/index/insegnamento/insegnamento2/id/desc/9999',
'http://didattica.uniroma2.it/files/index/insegnamento/insegnamento3/id/desc/9999'
]

#sezione gmail/hotmail da modificare con i vostri dati
username = "#"
password = "#"
fromaddr = "#"
toaddrs  = ["email1","email2","email3"]
subject = "Notifica risultati esame"

def sendmail(name, link, url):
	print "[+] Invio email..."
	import smtplib
	import email
	if "@hotmail" in username:
		server = smtplib.SMTP("smtp.live.com:587")
	elif "@gmail" in username:
		server = smtplib.SMTP("smtp.gmail.com:587")
	server.starttls()
	server.login(username,password)
	msg = email.message_from_string("[  ] Potrebbero essere usciti i risultati\n[  ] Titolo delll'ultimo file inserito: "+str(name)+"\n[+] "+str(link)+"\n[+] "+url)
	msg["From"] = fromaddr
	msg["Subject"] = subject
	for email in toaddrs:
		msg["To"] = email
		server.sendmail(fromaddr, email, msg.as_string())
	server.quit()

def check(url, line, aorw):
	file = open("db.txt","r")
	lines = file.read().split("\n")[line]
	r=requests.get(url)
	soup = BeautifulSoup(r.text)
	trs = [tr.find("td").find("a") for tr in soup.findAll('tr',attrs={'class':'even'})]
	#print str(len(trs))+">"+str(int(lines))+"?"
	if len(trs)>int(lines):
		last_insert = trs[0].text.encode('utf-8').strip()
		last_insert_href = "http://didattica.uniroma2.it"+trs[0]['href']
		sendmail(last_insert, last_insert_href, url)
		first(url, aorw)

def first(url, aorw):
	file = open("db.txt",aorw)
	r=requests.get(url)
	soup = BeautifulSoup(r.text)
	trs = [tr.text for tr in soup.findAll('tr',attrs={'class':'even'})]
	file.write(str(len(trs))+"\n")
	file.close()

#main
def main():
	current_line = 0
	if os.path.isfile("db.txt"):
		for url in urls:
			if current_line > 0:
				check(url, current_line, "a")
				current_line = current_line + 1
			else:
				check(url, current_line, "w")
				current_line = current_line + 1
	else:
		for url in urls:
			first(url, "a")

if __name__ == "__main__":
	main()
