from colorama import Fore

color_blue = Fore.BLUE
color_red = Fore.RED
color_magenta = Fore.MAGENTA
color_green = Fore.GREEN
color_white = Fore.WHITE
color_cyan = Fore.CYAN
color_yellow = Fore.YELLOW


def menu():
    main_menu:str = f"""
    {color_yellow}[1] {color_green}GeoIP         {color_yellow}[5] {color_green}Speedtest        {color_yellow}[9] {color_green} Traceroute
    {color_yellow}[2] {color_green}Ping          {color_yellow}[6] {color_green}Domain lookup    {color_yellow}[10] {color_green}Backup files
    {color_yellow}[3] {color_green}FakeN         {color_yellow}[7] {color_green}Flush DNS cache  {color_yellow}[11] {color_green}Installer
    {color_yellow}[4] {color_green}FakeAddr      {color_yellow}[8] {color_green}Portscan	   {color_yellow}[12] {color_green}Calculator


    {color_yellow}V{color_green}1{color_white}.{color_yellow}2{color_white}.{color_green}4{color_white} | {color_yellow}[{color_green}0{color_yellow}]{color_green}Exit
"""
    print(main_menu)
