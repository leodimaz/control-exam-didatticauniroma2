# control-exam-didatticauniroma2
Basta fare il refresh delle pagine su didattica, da oggi puoi essere avvisato via email

# istruzioni

1) Installare python dal sito ufficiale: http://www.python.it/download/<br />
2) Installare le seguenti repository:<br />
<b>requests</b> (http://docs.python-requests.org/en/master/user/install/#install) <br />
<b>BeautifulSoup</b> (https://www.crummy.com/software/BeautifulSoup/) <br />
3) Modificare il file control.py con i dati relativi alla propria casella di posta gmail<br />
4) In ambiente Linux o OsX lanciare i seguenti comandi:<br />
<b>crontab -e</b><br />
aggingere la seguente riga e salvare<br />
<b>*/10 * * * * /usr/bin/python /path/del/file/esame.py</b><br />

Ogni 10 minuti il sistema eseguirà il programma e controllerà se è stato aggiunto un nuovo file sul link di didatticaweb. In caso di esito positivo arriverà un'email di notifica relativa al nuovo file inserito<br />

Ci tengo a precisare che lo script è stato creato per necessità personali e che quindi per ora funziona solamente con caselle di posta gmail e siti web del tipo http://didattica.uniroma2.it/files/index/insegnamento/nomedelcorso

