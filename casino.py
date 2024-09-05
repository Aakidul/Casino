

import random
import os
import time
import json

"""
Copyright (c) 2024 Aakidul. All rights reserved.
This code is the original work of Aakidul and may not be copied,
modified, or redistributed without permission.
Unauthorized use, including the creation of derivative works or other games based on this code, is strictly prohibited.

"""

os.system("clear")

print('''

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
   print("How Many Rows Game Do You Want?")
   print("Win Price Also Double with greater Rows Luck Game 🤑💸")
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
                print(f"YOU WON {b} 🤑💸")
                print("Your Money Has Been Withdrawn To Your Account 💸🏦🤑")
                withdraw = int(b)
                reward = {"balance": withdraw}
                with open('balance.json', 'w') as file:
                     json.dump(reward, file, indent=4)


             else:
                print("YOU LOOSE !! 🤡😭🤣💸✖️ ")
                print(matches)
                print("\n")
                print("Wanna Play Again ?? ;) ")
                play_again = input("Enter Y/Yes OR N/no to Exit:  ")

                if play_again.lower() == "y" or play_again.lower() == "yes":
                   os.system("python3 casino.py")
                elif play_again.lower() == "n" or play_again.lower() == "no" or play_again.lower() == "exit":
                    print("Byee !!!")
                    exit()

   else:
      print("Please Enter A Number!!")


main()
