from colorama import Fore, Back, Style
from random import choice

logo = """
     ____  ____   _____ ______   ____  _____ ____   ____  ___ ___ 
    |    ||    \ / ___/|      | /    |/ ___/|    \ /    ||   |   |
     |  | |  _  (   \_ |      ||  o  (   \_ |  o  )  o  || _   _ |
     |  | |  |  |\__  ||_|  |_||     |\__  ||   _/|     ||  \_/  |
     |  | |  |  |/  \ |  |  |  |  _  |/  \ ||  |  |  _  ||   |   |
     |  | |  |  |\    |  |  |  |  |  |\    ||  |  |  |  ||   |   |
    |____||__|__| \___|  |__|  |__|__| \___||__|  |__|__||___|___| v5"""

def print_logo():
    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Fore.MAGENTA + "      Developers: @arnavos and @david1337x"+ Style.RESET_ALL + Style.BRIGHT)
    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)