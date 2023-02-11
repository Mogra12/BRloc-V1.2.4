from colorama import Fore

color_blue = Fore.BLUE
color_red = Fore.RED
color_magenta = Fore.MAGENTA
color_green = Fore.GREEN
color_white = Fore.WHITE
color_cyan = Fore.CYAN
color_yellow = Fore.YELLOW

def installer_menu():
    menu_installer: str = f"""
    {color_yellow}[1]  {color_green}OpenVPN               {color_yellow}[7]  {color_green}Steam
    {color_yellow}[2]  {color_green}VSCodium              {color_yellow}[8]  {color_green}Hyper terminal
    {color_yellow}[3]  {color_green}Google Chrome         {color_yellow}[9]  {color_green}Wireshark
    {color_yellow}[4]  {color_green}OperaGX               {color_yellow}[10] {color_green}Whatsapp
    {color_yellow}[5]  {color_green}Visual Studio Code    {color_yellow}[11] {color_green}VMware Player
    {color_yellow}[6]  {color_green}Discord               {color_yellow}[12] {color_green}VLC media player


    {color_yellow}V{color_green}1{color_white}.{color_yellow}2{color_white}.{color_green}4{color_white} | {color_yellow}[{color_green}0{color_yellow}]{color_green}Return
    """
    print(menu_installer)
