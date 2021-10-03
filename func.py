from colorama import Fore, init
init(autoreset=True)
g = Fore.GREEN
r = Fore.RED
w = Fore.WHITE
y = Fore.YELLOW
def logo():
    print(f'''
{Fore.LIGHTGREEN_EX}       ***** **      *
     ******  ****   **        * 
    **   *  *  ***  **       ***
   *    *  *    *** **        * 
       *  *      ** **                ***  ****       ****
      ** **      ** **  ***   ***      **** **** *   * ***  * ***  ****
      ** **      ** ** * ***   ***      **   ****   *   ****   **** **** *
    **** **      *  ***   ***   **      **         **    **     **   ****
   * *** **     *   **     **   **      **         **    **     **    **
      ** *******    **     **   **      **         **    **     **    **
      ** ******     **     **   **      **         **    **     **    **
      ** **         **     **   **      **         **    **     **    **
      ** **         **     **   **      ***         ******      **    **
      ** **         **     **   *** *    ***         ****       ***   ***
 **   ** **          **    **    ***                             ***   ***
***   *  *                 *      {Fore.CYAN}Author{g}: TEC1sc0 {r}V1.0{g}
 ***    *                 *  {Fore.CYAN}Github{g}: github.com/TEGLITCHER093
  ******                 *
    ***                 *{w}\n
Usage: {g}phiron{w} -u [username] --pass [password list path] -p 21 [domain/ip]\n
Optional Arguments:
 -h                Show Help Menu
 -u                Set Username
 -p                Set Port (Default: 21)
 --pass            Set Password List\n
\n{r}-{w} The Passwordlist should only be Passwords No \"user:pass\"''')