from colorama import Fore

color_blue = Fore.BLUE
color_red = Fore.RED
color_magenta = Fore.MAGENTA
color_green = Fore.GREEN
color_white = Fore.WHITE
color_cyan = Fore.CYAN
color_yellow = Fore.YELLOW

def menu():
	main_menu: str = f'''
        {color_yellow}[1] {color_green}Sum
	{color_yellow}[2] {color_green}Subtraction
	{color_yellow}[3] {color_green}Multiplication
	{color_yellow}[4] {color_green}Division

	{color_yellow}V{color_green}1{color_white}.{color_yellow}2{color_white}.{color_green}4{color_white} | {color_yellow}[{color_green}0{color_yellow}]{color_green}Return
	'''

	print(main_menu)