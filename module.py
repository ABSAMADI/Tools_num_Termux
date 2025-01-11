import random
import cowsay
from colorama import Fore, Style, init

init()

cowsay.tux("im named abolfazl enter your num to a and b")

a = int(input("a:"))
b = int(input("b:"))
   
while True:
    print(Fore.GREEN + str(random.randint(a, b)) + Style.RESET_ALL)
