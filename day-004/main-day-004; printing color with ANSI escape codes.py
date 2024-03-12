import sys
import os
import time

GOLDEN = '\033[93m'
GUM_PINK = '\033[95m'
WHITE = '\033[97m'
PURPLE = '\033[94m'
RESET = ' \033[0m'

print(" Welcome dear player")
playerName = input("Who are you? ")

print((playerName + " ") * 17)

print("A name that echoes... ˜”°•.˜”°• in the void •°”˜.•°”˜")
print()

outsiders = input("Any dearest to your heart? ")
print("None other than " + "\033[95m█▓▒░░▒▓█\033[0m, right? .... uh ")

print("")

hate = input("Tell me your hate, what repulses you? ")

print(
    "You will never have to worry about it, because this is the land of your dreams and selfish desires. Want to try what I please?"
)

print()
confirmation = input("Desire to continue?")
os.system('clear')

print("\033[96m== COMPUTER'S DREAMS ==\033[0m")
angel = ("""
.  ...:.-.....-::.......---:.          
....-.:=.::.:-=.:.:......:....::..     
.    .. .... :::::..=-.................:..       
.    ...  . .=:-+::.=......-.:..........-..     
..    .   .....-+:=+###**=:==++:..:..-...:.    
-.. .:::.:=-+*##*=*#####*+++*+-: :-...==::.   
:.=+ .=:..::=.:---+=###*#*+=-=--*--.:=::. ==+*
.:-**+=+==-:==-+++=-:+######******++....-=--::-
.::=*=+++*=-..:*++==+=+*######**+=-+:::..-.   .
...==*+++++*#*:.-=+*+-=++######**+##.*:....... 
--:--. :==****+:+*****=+*#####*=-+*++:.   ..:..
:::-.:-::=-=+*###*++--+=++#####*++++==-.  ::--+
.-==:=.-..=+##*+=.       .=####*+**+-+**=+++*+
..---...--::+#*+:..        ..##*+=+*. :.     . 
.==.===:--=*=:.            .+##*#+++.      :.
.-=:.=--+==+-:...        .:::=**++==+.    :=.
.: ...==-..-:=+ -#-###     #::-#:.-#=:+=++===+.-:
::   +++..++..=                 .***##=-:.---=::
:.::..=*-...===+=               .*#**##*=-:=.:: .
.-:=+***+.::==**+=              -#*+*#****+=+==:.
--::::.+**+=:=*= :.     ..     =####+-+*+.=.::...
-:......:--.=++**+-.   +**:  :*#*=*#*#+*+. :.    
.....     .::+*=.:+:.=-    -+**=..+.==++*...     
.   .    .:-..=:++=-..:--:.==++**-.:.==.:+     . 
.. ......:=.:+**=+=  ......:---**-.=-=....:    ..
....... ..=+*+.  :     .....-.-==:.:- ...     .-
.  .....-.:+:....       . ...:==--. .....      . 
.:...--.    .         ..-=-==.  .    .       
.. . ..: ..      ... .. ....+.-.   :.            
....:-.   .         .-..  . ==:   .-.         :- 
.:...              .   .  .==:   ..      :-   --
.-.                    .  -=-.  ..     .:-=  ..-
.::..      .        ..  ...=:-  ..     .-. .. ...
...::..    .      ...... ..... .-   ..:*+. .... .
......:.    .    .-.   .  .   .. .:.  :==:.:...  
...  ..=:. ..    -     ..    ..     ..: ......   
....   .-.  .  ..   ..-=.:. ..         .......   
""")


def colorize(char, color):
    return f"{color}{char}{RESET}"


for char in angel:
    if char == '#':
        sys.stdout.write(colorize(char + "", GOLDEN))
    else:
        sys.stdout.write(char + " ")

    sys.stdout.flush()
    time.sleep(0.0008)

print("")

print(
    "\033[95mYou are finally here", playerName,
    "... Ah, my \033[1m*beloved* .:: \033[35m░m░i░░░░n░e░...\033[0m always destined, always \033[35myours. There's no escape from this love, is there?"
)

print(
    "\n\033[0mAn unheard voice plays at the distance. The screen flickers, the text blurs, and in the background, a low, haunting melody plays, as if from another world. Your secrets, now shared, echoes endlessly in the digital void safely from everything else..."
)


