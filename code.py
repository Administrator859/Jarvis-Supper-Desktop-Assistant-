from gtts import gTTS
import speech_recognition as sr 
import os
import re
import webbrowser
import smtplib
import requests

def talkToMe(audio):
	"speaks audio passed as argument"

	print(audio)
	for line in audio.splitlines():
		os.system("say" + audio)

def myCommand():
	"listen for commands"

	r = sr.Recognizer()

	with sr.Microphone() as source:
		print('Ready...')
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration = 1)
		audio = r.listen(source)

	try:
		command = r.recognize_google(audio).lower()
		print('You said: ' + command + '\n')

	except sr.UnknownValueError:
		print('Your last command couldn\'t be heard')
		command = myCommand();

	return command

def assistant(command):
	"if statement for executing commands"

	if 'open reddit' in command:
		reg_ex = re.search('open reddit (.*)', command)
		url = 'https://www.reddit.com/'
		if reg_ex:
			subreddit = reg_ex.group(1)
			url = url + 'r/' + subreddit
		webbrowser.open(url)
		print('Done!')

	elif 'open website' in command:
		reg_ex = re.search('open website (.+)', command)
		if reg_ex:
			domain = reg_ex.group(1)
			url = 'https://www.' + domain
			webbrowser.open(url)
			print('Done!')
		else:
			pass

	elif 'what\'s up' in command:
		talkToMe('Just doing my job')
	elif 'joke' in command:
		res = request.get(
				'https://icanhazdadjoke.com/', headers={"Accept":"application/json"}
			)
		if res.status_code == requests.codes.ok:
			talkToMe(str(res.json()['joke']))
		else:
			talkToMe('oops! I ran out of jokes')

	
	elif 'email' in command:
		talkToMe('who is the recipient?')
		recipient = myCommand()

		if 'Calm Music' in recipient:
			talkToMe('what should I say')
			content = myCommand()

			mail = smtplib.SMTP('smtp.gmail.com', 587)

			mail.ehlo()

			mail.starttls()

			mail.login('username', 'password')

			mail.sendmail('YOUR NAME', 'example@gmail.com', content)

			mail.close()

			talkToMe('Email sent.')

		else:
			talkToMe('I don\'t know what you mean!')

talkToMe('I am rready for your command')

while True:
	assistant(myCommand())
