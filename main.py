
from interface.calculator import calc_menu
from interface.calculator import calc_logo
from interface.installer import inst_logo
from interface.installer import inst_menu
from passwordgenerator import pwgenerator
from interface.home import main_logo
from interface.home import main_menu
from modules import ccount
from colorama import Fore
from faker import Faker
from time import sleep
import requests
import pprint
import socket
import time
import sys
import os


color_blue = Fore.BLUE
color_red = Fore.RED
color_magenta = Fore.MAGENTA
color_green = Fore.GREEN
color_white = Fore.WHITE
color_cyan = Fore.CYAN
color_yellow = Fore.YELLOW


key_input: str = str(input('Activation Code> '))
user_input: str = str(input('User: '))
user: str = user_input
keys = [
	'782F413F4428472B4B6250645367566B',
	'34753778214125442A472D4B61506452',
	'6D5A7134743777217A25432A462D4A61',
	'5368566D597133743677397A24432646',
	'6150645367566B597033733676397924']

sleep(1)
os.system('cls')

clock = time.strftime('%H:%M:%S')


class program:
	def return_calc(self):
		print('\n')
		print(f'{color_white}▀' * 81)


	def returnf(self):
		print('\n')
		print(f'{color_white}▀' * 81)
		sleep(1)
		self.main()


	def returnins(self):
		inst_logo.installer_logo()
		inst_menu.installer_menu()


	def otheroption(self):
		print('the selected option does not exist')
		sleep(2)
		os.system('cls')
		self.returnf()


	def req_ip(self):
		try:
			sleep(0.5)
			os.system('cls')
			API_KEY: str = 'kBtOz67nfvQq8t8HN6fA'
			ip_input: str = str(input(f'{color_green}IP{color_yellow}> '))
			req = requests.get(f'https://extreme-ip-lookup.com/json/{ip_input}?key={API_KEY}')
			req_json = req.json()
			sleep(0.5)
			pprint.pprint(req_json)
			self.returnf()
		except KeyboardInterrupt:
			print('Program interrupted')


	def ping(self):
		try:
			sleep(0.5)
			os.system('cls')
			hostname: str = input(f'{color_green}Host{color_yellow}> ')
			response = os.system(f'ping {hostname}')
			if response == 0:
				print(f'{color_white}Status: {color_green}Online')
			else:
				print(f'{color_white}Status: {color_red}Offline')
			self.returnf()
		except KeyboardInterrupt:
			print('Program interrupted')


	def pwgen(self):
		try:
			sleep(0.5)
			os.system('cls')
			passw = pwgenerator.generate()
			sleep(0.5)
			print(f'{color_white}password: {color_green}{passw}')
			self.returnf()
		except KeyboardInterrupt:
			print('Program interrupted')


	def faken(self):
		try:
			sleep(0.5)
			os.system('cls')
			fake = Faker()
			name = fake.name()
			sleep(0.5)
			print(f'{color_white}fake name: {color_green}{name}')
			self.returnf()
		except KeyboardInterrupt:
			print('Program interrupted')


	def fakeaddr(self):
		try:
			sleep(0.5)
			os.system('cls')
			fake = Faker()
			addr = fake.address()
			print(f'{color_white}fake address: {color_green}{addr}')
			self.returnf()
		except KeyboardInterrupt:
			print('Program interrupted')


	def speedt(self):
		sleep(0.5)
		os.system('cls')
		os.system('speedtest --secure')
		self.returnf()


	def dmlookup(self):
		domain = input(f'{color_green}domain{color_yellow}>')
		sleep(0.5)
		os.system('cls')
		os.system(f'nslookup {domain}')
		self.returnf()


	def flushdns(self):
		sleep(0.5)
		os.system('cls')
		os.system('ipconfig /flushdns')
		self.returnf()


	def portscan(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		host: str = input(f'{color_green}IP{color_yellow}> ')
		range_port: int = int(input(f'{color_green}Range{color_yellow}> '))
		for ports in range(range_port):
			connect = s.connect_ex((host, ports))
			if connect == 0:
				print(f'{color_white}Port: {color_green}{ports} opened')
				s.close()
			else:
				print(f'{color_white}Port: {color_yellow}{ports} closed')
				s.close()
		self.returnf()


	def tracing(self):
		host: str = input(f'{color_green}Host{color_yellow}> ')
		sleep(0.5)
		os.system('cls')
		os.system(f'tracert {host}')
		self.returnf()


	def backupf(self):
		archive: str = input(f'{color_green}Archive/folder path{color_yellow}> ')
		new_path: str = input(f'{color_green}Backup path{color_yellow}> ')
		sleep(0.5)
		os.system('cls')
		os.system(f'robocopy {archive} {new_path}')
		self.returnf()


	def exitl(self) :
		os.system('cls')
		confirm: str = input(
			f'{color_white}Are you sure you want to leave? [{color_green}Y{color_white}/{color_yellow}N{color_white}]>'
		).strip().upper()

		if confirm == 'Y':
			print(f'{color_white}departure time: {color_green}{clock}{color_white}')
			sleep(2)
			os.system('cls')
			sys.exit()
		else:
			os.system('cls')
			self.main()

	def main_calc(self):
		print('\n')
		print(f'{color_white}▀' * 81)
		sleep(1)
		self.main()

	def openvpn(self):
		os.system('winget install openvpn')


	def vscodium(self):
		os.system('winget install -e --id VSCodium.VSCodium')


	def chrome(self):
		os.system('winget install -e --id Google.Chrome')


	def operagx(self):
		os.system('winget install -e --id Opera.OperaGX')


	def vscode(self):
		os.system('winget install -e --id Microsoft.VisualStudioCode')


	def discord(self):
		os.system('winget install -e --id Discord.Discord')


	def steam(self):
		os.system('winget install -e --id Valve.Steam')


	def hyper(self):
		os.system('winget install -e --id Zeit.Hyper')


	def wireshark(self):
		os.system('winget install -e --id WiresharkFoundation.Wireshark')


	def whatsapp(self):
		os.system('winget install -e --id WhatsApp.WhatsApp')


	def vmware(self):
		os.system('winget install -e --id VMware.WorkstationPlayer')


	def vlc(self):
		os.system('winget install -e --id VideoLAN.VLC')

	def main(self):
		try:
			if key_input == keys[0] or key_input == keys[1] or key_input == keys[2] or key_input == keys[3] or key_input == keys[4]:
				main_logo.logo()
				main_menu.menu()
				choice = int(input(f'{color_yellow}({color_green}{user}@{user}-PC{color_yellow}){color_yellow}> '))
				match choice:
					case 1:
						self.req_ip()
					case 2:
						self.ping()
					case 3:
						self.faken()
					case 4:
						self.fakeaddr()
					case 5:
						self.speedt()
					case 6:
						self.dmlookup()
					case 7:
						self.flushdns()
					case 8:
						self.portscan()
					case 9:
						self.tracing()
					case 10:
						self.backupf()
					case 11:
						sleep(0.5)
						inst_logo.installer_logo()
						inst_menu.installer_menu()
						choose_installer: int = int(input(f'{color_yellow}({color_green}root@root{color_yellow}){color_yellow}> '))
						match choose_installer:
							case 1:
								self.openvpn()
							case 2:
								self.vscodium()
							case 3:
								self.chrome()
							case 4:
								self.operagx()
							case 5:
								self.vscode()
							case 6:
								self.discord()
							case 7:
								self.steam()
							case 8:
								self.hyper()
							case 9:
								self.wireshark()
							case 10:
								self.whatsapp()
							case 11:
								self.vmware()
							case 12:
								self.vlc()
							case 0:
								os.system('cls')
								self.main()
							case _:
								self.otheroption()
					case 12:
						sleep(0.5)
						calc_logo.logo()
						calc_menu.menu()
						choose_calc: int = int(input(f'{color_yellow}({color_green}root@root{color_yellow}){color_yellow}> '))
						match choose_calc:
							case 1:
								num1 = float(input('Type a number: '))
								num2 = float(input('type another number: '))
								print(f'Result: {ccount.sum(num1, num2)}')
								self.main_calc()
							case 2:
								num1 = float(input('Type a number: '))
								num2 = float(input('type another number: '))
								print(f'Result: {ccount.sub(num1, num2)}')
								self.main_calc()
							case 3:
								num1 = float(input('Type a number: '))
								num2 = float(input('type another number: '))
								print(f'Result: {ccount.mult(num1, num2)}')
								self.main_calc()
							case 4:
								num1 = float(input('Type a number: '))
								num2 = float(input('type another number: '))
								print(f'Result: {ccount.div(num1, num2)}')
								self.main_calc()
							case 0:
								os.system('cls')
								self.main()
							case _:
								self.otheroption()
					case 0:
						self.exitl()
					case _:
						self.otheroption()
			else:
				print(f'{color_yellow} This activation code is invalid!')
		except KeyboardInterrupt:
			print('Program interrupted')

if __name__ == '__main__':
	programm = program()
	programm.main()