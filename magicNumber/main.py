import random

MIN = 1
MAX = 10
MAGIC_NUMBER = random.randint(MIN, MAX)
NB_TRY = 4

print("""

███╗   ███╗ █████╗  ██████╗ ██╗ ██████╗    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
████╗ ████║██╔══██╗██╔════╝ ██║██╔════╝    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
██╔████╔██║███████║██║  ███╗██║██║         ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██║╚██╔╝██║██╔══██║██║   ██║██║██║         ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║╚██████╔╝██║╚██████╗    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝ ╚═════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                 

""")


def ask_number(nb_min, nb_max):
    nbr = 0
    while nbr == 0:
        try:
            nbr = int(input(f"Choose a number between {nb_min} and {nb_max}: "))
        except:
            print(f"ERROR: I need an integer between {nb_min} and {nb_max}")
        else:
            if nbr < nb_min or nbr > nb_max:
                print(f"ERROR: I need an integer between {nb_min} and {nb_max}")
                nbr = 0
    return nbr


nb = 0
i = 0
while nb != MAGIC_NUMBER and i < NB_TRY:
    print(f"You have {NB_TRY-i} try.")
    nb = ask_number(MIN, MAX)
    if nb > MAGIC_NUMBER:
        print('LOWER !')
    elif nb < MAGIC_NUMBER:
        print('HIGHER !')
    elif nb == MAGIC_NUMBER:
        print("You win !")
    i += 1

if i == NB_TRY:
    print(f"You loose ! Magic number was {MAGIC_NUMBER}")