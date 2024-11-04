import json
import os
import random
import time

def colored(text, color):
    colors = {
        "red": "\033[1;31;1m",
        "green": "\033[1;32;1m",
        "white": "\033[1;37;1m",
        "reset": "\033[1;37;1m"
    }
    return f"{colors[color]}{text}{colors['reset']}"

def logo():
    colors = [35, 33, 36]
    x = """
   



 
██     ██  █████  ██████      ██████  ██    ██ ██      ███████ ██   ██ 
██     ██ ██   ██ ██   ██     ██   ██ ██    ██ ██      ██       ██ ██  
██  █  ██ ███████ ██████      ██████  ██    ██ ██      █████     ███   
██ ███ ██ ██   ██ ██   ██     ██   ██ ██    ██ ██      ██       ██ ██  
███ ███  ██   ██ ██   ██     ██   ██  ██████  ███████ ███████ ██   ██ 
                                                                       
                                                                       
                                                                       
                                                                          
                                                                          
                                                                          
"""
    for N, line in enumerate(x.split("\n")):
        print(f"\x1b[1;{random.choice(colors)}m{line}\x1b[1;37;1m")
        time.sleep(0.05)

def convert_cookie_to_json(cookie_str):
    cookie_dict = {}
    cookies = cookie_str.split("; ")
    for cookie in cookies:
        key, value = cookie.split("=", 1)
        cookie_dict[key] = value
    return cookie_dict

def cookie_converter():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        logo()
        print('----------------------------------------------------------------------')
        num_cookies = int(input(colored("[+] How many cookies do you want to convert to JSON? ", "white")))
        
        for i in range(num_cookies):
            cookie_str = input(colored(f"[+] Enter cookie {i+1}: ", "white"))
            print('----------------------------------------------------------------------')
            cookie_json = convert_cookie_to_json(cookie_str)
            print(colored(f"[√] Your JSON cookie {i+1}:\n \n{json.dumps(cookie_json, indent=2)}\n", "green"))
            if i < num_cookies - 1:
                print('----------------------------------------------------------------------')

        again = input(colored("[+] Do you want to convert more cookies? (yes/no): ", "white")).strip().lower()
        if again != 'yes':
            break
        print('----------------------------------------------------------------------')

if __name__ == "__main__":
    cookie_converter()