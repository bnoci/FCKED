import random
import time

art = r"""
░░░░░░░░▌░░░░░░░▐
░░░░█░░▄▌░░░░▌░░░█░░░▄▄
░░░░▐▄░▌░░░░▐▄▌░░░▀▄█▄
░░░░░▐█░░░░░░░▌░▄█▀░░░▀█
░░░▌░░▐░░░░░▄▀▀▀░░░░░░░░
░░░▐░░░▀▄░█▀▄▄▄▄░░░░░░░░
▌░░█▄░░░▐▄█░░░░▌▀▄░░░░░░
█░░░▐░░░██░░░░░█░░▄░█▀░░
▐░░░█░░░▐█░░░░░░░░▌▀░░░░
░▌░░▌░░░▐█▄░░░░▄▄█▄▄▄░░░
▄▄▀▄█░░░░██░▄█▀░█▄▄░▐▄▄░
░░░░▀█▄░▄███░░░░░░░░░░░░
░░░░░░█████░░░░░░░░░░░░░
░░░░░░░▐███░░░░░░░░░░░░░
░░░░░░░▐███░░░░░░░░░░░░░
░░░░░░░▐████░░░░░░░░░░░░
░░▒▒▒▒▒█████▒▒░░░░░░░░░░
▒▒▒▒▒▒▄██████▒▒▒▒▒▒▒▒▒▒▒
▒▒▄▄▄█▀▒█▀▐▀▀██▄▄▄▒▒▒▒▒▒
█▀▐▒█▒▒▒▌▒▒▐▒▒▒▒▒▌▀▀▄▒▒▒
"""


print(r"""
                 _..._                                               
              .-'_..._''.                              _______       
            .' .'      '.\    .           __.....__    \  ___ `'.    
     _.._  / .'             .'|       .-''         '.   ' |--.\  \   
   .' .._|. '             .'  |      /     .-''"'-.  `. | |    \  '  
   | '    | |            <    |     /     /________\   \| |     |  ' 
 __| |__  | |             |   | ____|                  || |     |  | 
|__   __| . '             |   | \ .'\    .-------------'| |     ' .' 
   | |     \ '.          .|   |/  .  \    '-.____...---.| |___.' /'  
   | |      '. `._____.-'/|    /\  \  `.             .'/_______.'/   
   | |        `-.______ / |   |  \  \   `''-...... -'  \_______|/    
   | |                 `  '    \  \  \                               
   |_|                   '------'  '---'                                                                                                                                                
     """)

print(r"""
.-. .-')                       .-') _  ('-.      _ (`-.  .-') _               (`-.                      
\  ( OO )                     (  OO) )( OO ).-. ( (OO  )(  OO) )            _(OO  )_                    
 ;-----.\  ,--.   ,--.      ,(_)----. / . --. /_.`     \/     '._       ,--(_/   ,. \ .---.    .----.   
 | .-.  |   \  `.'  /       |       | | \-.  \(__...--''|'--...__)      \   \   /(__//_   |   /  ..  \  
 | '-' /_).-')     /        '--.   /.-'-'  |  ||  /  | |'--.  .--'       \   \ /   /  |   |  .  /  \  . 
 | .-. `.(OO  \   /         (_/   /  \| |_.'  ||  |_.' |   |  |           \   '   /,  |   |  |  |  '  | 
 | |  \  ||   /  /\_         /   /___ |  .-.  ||  .___.'   |  |            \     /__) |   |  '  \  /  ' 
 | '--'  /`-./  /.__)       |        ||  | |  ||  |        |  |             \   /     |   |.-.\  `'  /  
 `------'   `--'            `--------'`--' `--'`--'        `--'              `-'      `---'`-' `---''                                                       
      """)

print("====================================")
print("1. USERNAME GEN")
print("2. PASSWORD GENERATOR")
print("3. PHONE PASS GEN")
print("4. EXIT")
print("====================================")

choice = 0


choice = int(input(":"))

if choice == 1: 
    for line in art.splitlines():
        print(line)
        time.sleep(0.05) 

    
    adjectives = ["Epic", "Swift", "Shadow", "Neon", "Cool", "Lone", "Dark", "Ultra"]
    nouns = ["Wolf", "Ghost", "Coder", "Knight", "Rider", "Dragon", "Hacker", "Viper"]

    word1 = random.choice(adjectives)
    word2 = random.choice(nouns)
    num = random.randint(10, 99) 

  
    username = word1 + word2 + str(num)
    
    print("Home/FCKED/:" + username)
    input("Press/Enter/To/Exit/:")


elif choice == 2:
 
    for line in art.splitlines():
        print(line)
        time.sleep(0.05) 

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*"

    p1 = random.choices(letters, k=6)
    p2 = random.choices(numbers, k=2)
    p3 = random.choices(symbols, k=3)

    password = "".join(p1 + p2 + p3)

    print("Home/FCKED/:" + password)
    
    input("Press/Enter/To/Exit/:")

elif choice == 3:
    for line in art.splitlines():
        print(line)
        time.sleep(0.05) 

    numbers = "0123456789"
    p1 = random.choices(numbers, k=6)

    phonepas = "".join(p1)

    print("Home/FCKED/:" + phonepas)

    input("Press/Enter/To/Exit/:")

elif choice == 4:
    for line in art.splitlines():
        print(line)
        time.sleep(0.05) 

    print("Goodbye.......")

    time.sleep(0.1)


    















