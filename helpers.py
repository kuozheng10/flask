
from pip._vendor.colorama import init, Fore

def display(message,is_warning=False):
    if is_warning:
        print(Fore.RED + 'This is a warning')
    else: 
        print(Fore.BLUE + message)

        
