
import time
import random
import colorama
from colorama import Fore, Style

# Initialize colorama // ye to bahut importent hai barna itna aacha kese banega ye sab ( bese to mujhe itna nahi pata isse kya hota hhai mene video me dekha tha koi bhi digine karo to importent hai isliye mene bhi use kar liya khikhikhi) 
colorama.init(autoreset=True)

# msg ke liye color ki list phle he bana di khkhikhikhi ...
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

def print_with_color(text):
    for char in text:
        color = random.choice(colors) # color aapne aap daldiye jayenge 
        print(f"{color}{char}", end="", flush=True)
        time.sleep(0.07)  # time to lagna he chihi na ......
    print(Style.RESET_ALL)   # messege ke baad color Reset ho jaye isliye

def diwali_greeting():
    print("\n")
    print_with_color("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
    print_with_color("          🪔 Happy Diwali Mere Jigri Dosto  🪔          ")
    print_with_color("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
    time.sleep(0.5)
    print_with_color("Mere yaar, iss Diwali par sirf roshni hi nahi, \ntumhari zindagi mein dher saari khushiyan bhi aayein.")
    print_with_color("Dosti aur apnapan ka ye safar aise hi roshan rahe. Tum jaise dost ka saath hona,\n meri zindagi ki sabse badi blessing hai.")
    print_with_color("Bas yuhi humari yeh dosti aur khushiyon ki chain kabhi na toote.")
    print_with_color("Dil se tumhe aur tumhare parivaar ko Diwali ki dher saari shubhkaamnayein! 🎇💥")
    print(" 🩷 🩵 💗💞 Mere Pyare Jigri Dosto -=> @ RITESH SAINI, @ PRATIKSHA MISHRA ,\n @ RAJKUMAR KUSHWAHA , @ VISHAKHA KUSHWAHA  'hehehehe' 🩷 🩵 💗💞 ")
    print("\n")

diwali_greeting()
#  function  ka naam bhi to hona chiye kuch aacha isliye greeting rakh diya 
