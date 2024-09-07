import random
import os
import time
import json
from colorama import Fore, Style, init

"""
Copyright (c) 2024 Aakidul. All rights reserved.
This code is the original work of Aakidul and may not be copied,
modified, or redistributed without permission.
Unauthorized use, including the creation of derivative works or other games based on this code, is strictly prohibited.

"""

os.system("clear")


colors = ["GREEN", "RED", "BLUE", "CYAN", "YELLOW", "MAGENTA", "WHITE"]

color_select = random.choice(colors)
selected_color = getattr(Fore, color_select)

print(selected_color + '''

 ██████╗ █████╗ ███████╗██╗███╗   ██╗ ██████╗
██╔════╝██╔══██╗██╔════╝██║████╗  ██║██╔═══██╗
██║     ███████║███████╗██║██╔██╗ ██║██║   ██║
██║     ██╔══██║╚════██║██║██║╚██╗██║██║   ██║
╚██████╗██║  ██║███████║██║██║ ╚████║╚██████╔╝
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝
Created By Aakidul ^⁠_⁠^

 ''')



user_cash  = []
with open('balance.json', 'r') as f:
      data = json.load(f)
      user_cash.append(data["balance"])

def main():
   init(autoreset=True)
   print(Fore.YELLOW + Style.BRIGHT + "🎰 How Many Rows Would You Like to Play With? 🎰" + Style.RESET_ALL)
   print(Fore.CYAN + "The more rows you play, the bigger the chance to win HUGE! 💰\n" + "Remember: Higher rows mean DOUBLE the winning prize! 💵 Are you feeling lucky?" + Style.RESET_ALL)

   user_input = input("Enter Number: ")
   if user_input.isdigit():

        if int(user_input) < 1:
            print("You Can Only Enter A Number That is greater than 2 OR 2")

        elif int(user_input) == 1:
             print("You Can Only Enter A Number That is greater than 2 OR 2")


        elif int(user_input) == 2 or int(user_input) > 2:
             matches = []
             for luck in range(1, int(user_input) + 1):
                 luck_num = random.randint(1, 2)
                 matches.append(luck_num)

             if len(set(matches)) == 1:
                print(matches)
                b = int(user_cash[0])*len(matches)
                print(f"YOU WON {b}")
                withdraw = int(b)
                reward = {"balance": withdraw}
                with open('balance.json', 'w') as file:
                    json.dump(reward, file, indent=4)

                    x = input("Do You Wanna Play Again? Y/N : ")

                    if x.lower() == "y" or x.lower() == "yes":
                         time.sleep(1)
                         os.system("clear")
                         os.system("python3 casino2.py")

                    if x.lower() == "n" or x.lower() == "no" or x.lower() == "exit":
                        print("\n")
                        print(Fore.YELLOW + "Byee Enjoy Your Money Hehe (⁠◔⁠‿⁠◔⁠) !!")
                        exit()


             else:
                  print("YOU LOSE!!")
                  print(matches)
                  print("\n")
                  print(Fore.RED + "Wanna Play Again ??  ༎ຶ⁠ ⁠෴⁠ ⁠༎ຶ⁠) ")
                  print("\n")
                  play_again = input(Fore.GREEN + "Enter Y/Yes OR N/no to Exit:  ")

                  if play_again.lower() == "y" or play_again.lower() == "yes":
                      os.system("python3 casino2.py")
                  elif play_again.lower() == "n" or play_again.lower() == "no" or play_again.lower() == "exit":
                      print("\n")
                      print(Fore.YELLOW + "Byee !!!")
                      exit()

   else:
      print("\n")
      print(Fore.RED + "Please Enter A Number!!")


main()
