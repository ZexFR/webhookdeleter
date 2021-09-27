import requests
import os
import time
from colorama import Fore

def icon():
    print(Fore.RED + """

░██╗░░░░░░░██╗███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗  ██████╗░███████╗██╗░░░░░███████╗████████╗███████╗██████╗░
░██║░░██╗░░██║██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝  ██╔══██╗██╔════╝██║░░░░░██╔════╝╚══██╔══╝██╔════╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██████╦╝███████║██║░░██║██║░░██║█████═╝░  ██║░░██║█████╗░░██║░░░░░█████╗░░░░░██║░░░█████╗░░██████╔╝
░░████╔═████║░██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔═██╗░  ██║░░██║██╔══╝░░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗  ██████╔╝███████╗███████╗███████╗░░░██║░░░███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚══════╝╚══════╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝    """ + Fore.RESET)


def icon2():
    print(Fore.GREEN + """
    
░██╗░░░░░░░██╗███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
░██║░░██╗░░██║██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██████╦╝███████║██║░░██║██║░░██║█████═╝░  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
░░████╔═████║░██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔═██╗░  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""" + Fore.RESET)



def webhookchecker():
    os.system("cls")
    icon2()
    print("What is the webhook you want to check > ")
    webhook = str(input(Fore.GREEN + "#root~zex~ " + Fore.RESET))
    r = requests.get(webhook)

    if r.status_code == 200:
        print(Fore.GREEN + "Webhook Working" + Fore.RESET)
        input(Fore.GREEN + 'Press Enter to return to the main menu.')
        menu()
        
    else:
        print(Fore.RED + "Webhook Not Working" + Fore.RESET)
    
        print(" ")
        input(Fore.GREEN + 'Press Enter to return to the main menu.')
        menu()
        

def webhookdeleter():
    os.system("cls")
    icon()
    
    webhook = str(input(Fore.GREEN + "#root~zex~ " + Fore.RESET))
    requests.delete(webhook)
    print("Webhook Deleted")
    print(" ")
    input(Fore.GREEN + 'Press Enter to return to the main menu.')
    menu()


def menu():
    os.system('cls')
    banner()
    print("1. Webhook Checker")
    print("2. Webhook Deleter")
    def askChoice():
        print("What tool do you want to use")
        option = int(input(Fore.GREEN + "#root~zex~ " + Fore.RESET))
        if option == 1:
            webhookchecker()
        elif option == 2:
            webhookdeleter() 
        
        else:
       
            
            print("Invalid option.")    
            
    askChoice()

def banner():
    print(Fore.LIGHTBLUE_EX + """
   _____                            _ _           _______          _     
  / ____|                          (_) |         |__   __|        | |    
 | (___   ___ _ __ ___   __ _ _ __  _| |_ _   _     | | ___   ___ | |___ 
  \___ \ / _ \ '_ ` _ \ / _` | '_ \| | __| | | |    | |/ _ \ / _ \| / __|
  ____) |  __/ | | | | | (_| | | | | | |_| |_| |    | | (_) | (_) | \__ \\
 |_____/ \___|_| |_| |_|\__,_|_| |_|_|\__|\__, |    |_|\___/ \___/|_|___/
                                           __/ |                         
                                          |___/                          
               Developed by Zex#2222
          """ + Fore.RESET)

if __name__ == "__main__":
    menu()
