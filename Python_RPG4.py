# The RPG Game

import sys, os, random

strength = 5
dext     = 5
intell   = 5

HP    = 0
MP    = 0
EVADE = 0

coins = 200
diamonds = 0

rewardXP = 5
rewardCoins = 200

chosen = False
enemyDOT = 0

XP = 0
level = 1

enemies = [
    # name, HP, DMG, XP, COINS
    ['Slime', 20, 10, 300, 150], # Easy Enemy
    ['Golblin', 30, 15, 500, 250], # Normal Enemy
    ['Elder Dragon', 150, 25, 1500, 2000] # Hard Enemy
]

# Inventory Variable(s)
healthPotion = 5
strengthPotion = 5
poisonBomb = 5
regenStim = 5

def saveData(player_name, strength, dexterity, intelligence, HP, MP, EVADE, excessPoints, coins,
             diamonds, level, xp, healthPotion, poisonBomb, strengthPotion, regenStim):
    
    f = open("save.txt", "w")
    f.write(str(player_name + "." + str(strength)))
    f.write("." + str(dexterity))
    f.write("." + str(intelligence))
    f.write("." + str(HP))
    f.write("." + str(MP))
    f.write("." + str(EVADE))
    f.write("." + str(excessPoints))
    f.write("." + str(coins))
    f.write("." + str(diamonds))
    f.write("." + str(level))
    f.write("." + str(xp))
    f.write("." + str(healthPotion))
    f.write("." + str(poisonBomb))
    f.write("." + str(strengthPotion))
    f.write("." + str(regenStim))
    f.close()

def create_account():
    print("Welcome to Coding Lab's RPG!")
    player_name = input("What's your name? ")
    print("Hi " + player_name + "!")
    print("")
  
    player_type = ""
    print("Choose your character: ")
    print("1. Warrior")
    print("2. Archer")
    print("3. Wizard")
    choice = input("Choice (1-3): ") 
  
    if choice == "1":
        playerType = "Warrior"
        HP = (strength * 9) + (dexterity * 2)
        MP = intelligence * 7
        EVADE = (dexterity * 5)
  
    elif choice == "2":
        playerType = "Archer"
        HP = (strength * 7) + (dexterity * 2)
        MP = intelligence * 7
        EVADE = (dexterity * 8)
  
    elif choice == "3":
        playerType = "Wizard"
        HP = (strength * 5) + (dexterity * 2)
        MP = intelligence * 10
        EVADE = (dexterity * 4)
  
    print("")
    print("You choose " + player_type + "!")
    print(f"Stats - HP: {HP}, MP: {MP}, EVADE: {EVADE}% Chance")

def loadData():
    # username = input("Enter username to load: ")
    global player_name
    global strength
    global dexterity
    global intelligence

    f = open("save.txt", "r")
    data = f.read()
    list_data = data.split(".")
    print(list_data)
    player_name = list_data[0]
    strength = int(list_data[1])
    dexterity = int(list_data[2])
    intelligence = int(list_data[3])
    HP = int(list_data[4])
    MP = int(list_data[5])
    EVADE = int(list_data[6])
    excessPoints = int(list_data[7])
    coins = int(list_data[8])
    diamonds = int(list_data[9])
    level = int(list_data[10])
    xp = int(list_data[11])
    healthPotion = int(list_data[12])
    poisonBomb = int(list_data[13])
    strengthPotion = int(list_data[14])
    regenStim = int(list_data[15])
    print("\nSave Loaded!")

def probability(chance):
    return random.random() < chance

os.system('cls')
print('Note: For the best experience, run this program in the terminal.')
print()

username = str(input('Hello, what is your name? '))
print(f'Hi {username}, welcome to The RPG Game!')

f = open('progress.txt')

print('\nChoose your characters:')
print('1. Warrior')
print('2. Archer')
print('3. Wizzard')

choice = input('Plese input your choice (1-3): ')
if choice == '1':
    playerType = 'Warrior'
    HP = (strength * 5) + (dext * 2)
    MP = intell * 7
    EVADE = (dext * 5)

elif choice == '2':
    playerType = 'Archer'
    HP = (strength * 3) + (dext * 2)
    MP = intell * 7
    EVADE = (dext * 8)
    
elif choice == '3':
    playerType = 'Wizzard'
    HP = (strength * 3) + (dext * 2)
    MP = intell * 10
    EVADE = (dext * 4)

print(f'You have chosen {playerType}!')
print(f'\nStats - HP: {HP}, MP: {MP}, EVADE: {EVADE}%')
print()

gameRunning = True
excessPoints = 5

while gameRunning:
    os.system('cls')
    print(f'Level {level}')
    print(f'{str(1000 - XP)} more XP to next level')
    print('+-------------------------------------------------+')
    print('|             Commands available                  |')
    print('|                                                 |')
    print('| 1: addstats: Add remaining points to your stats |')
    print('| 2: viewstats: Prints out all stats of player    |')
    print('| 3: compete: Compete against an enemy            |')
    print('| 4: shop: Visit the shop                         |')
    print('| 5: quit: Exits the game                         |')
    print('+-------------------------------------------------+')
    gameChoice = input('\nEnter your choice (1-3): ')

    if gameChoice == '1':
        print('Add remaining points to your stats:')
        print(f'Usable excess points: {str(excessPoints)}')
        print()
        print('===============================================')
        print(f'1. Strength: {str(strength)}')
        print(f'2. Dexterity: {str(dext)}')
        print(f'3. Intelligence: {str(intell)}')
        print('===============================================')
        print()
        statChoice = input('Which stats to upgrade (1-3): ')

        if statChoice == '1':
            os.system('cls')
            usedPoints = int(input('How many points to use? '))

            if usedPoints <= excessPoints:
                excessPoints = excessPoints - usedPoints
                strength = strength + usedPoints

                if playerType == 'Warrior':
                    HP = (strength * 9) + (dext * 2)

                elif playerType == 'Archer':
                    HP = (strength * 3) + (dext * 2)

                elif playerType == 'Wizzard':
                    HP = (strength * 3) + (dext * 2)
                    
                
            else:
                print("You don't have enough points!")

        elif statChoice == '2':
            os.system('cls')
            usedPoints = int(input('How many points to use?'))

            if usedPoints <= excessPoints:
                excessPoints = excessPoints - usedPoints
                dext = dext + usedPoints
                
            else:
                print("You don't have enough points!")

        elif statChoice == '3':
            os.system('cls')
            usedPoints = int(input('How many points to use?'))

            if usedPoints <= excessPoints:
                excessPoints = excessPoints - usedPoints
                intell = intell + usedPoints
                
                saveData(username, strength, dexterity, intell, HP, MP, EVADE, excessPoints, coins,
                     diamonds, level, XP, healthPotion, poisonBomb, strengthPotion, regenStim)
                
            else:
                print("You don't have enough points!")

        else:
            saveData(username, strength, dexterity, intell, HP, MP, EVADE, excessPoints, coins,
                     diamonds, level, XP, healthPotion, poisonBomb, strengthPotion, regenStim)
            os.system('cls')

    elif gameChoice == '2':
        os.system('cls')
        print('===========================================')
        print('Player Stats')
        print('===========================================')
        print()
        print(f'You are a {playerType}!')
        print(f'HP: {HP}, MP: {MP}, EVADE: {EVADE}%')
        print(f'1. Strength: {str(strength)}')
        print(f'2. Dexterity: {str(dext)}')
        print(f'3. Intelligence: {str(intell)}')
        print(f'4. Diamonds: {str(diamonds)}D$')
        print(f'5. Coins: {str(coins)}C$')
        print()
        print('===========================================')
        print('Inventory')
        print('===========================================')
        print()
        print(f'1. Health Potion: {str(healthPotion)}x')
        print(f'2. Strength Potion: {str(strengthPotion)}x')
        print(f'3. Poison Bomb: {str(poisonBomb)}x')
        print(f'4. Regen Stim: {str(regenStim)}x')
        print()
        input('Press enter to continue...')

    elif gameChoice == '3':
        os.system('cls')

        enemyName = ''
        enemyHP = 0
        enemyAttack = 0
        rewardXP = 0
        rewardCoins = 0
        chosen = False

        print('Choose an enemy:')
        print('1. Slime (Easy)')
        print('2. Goblin (Normal)')
        print('3. Elder Dragon (Nightmare)')
        enemyChoice = input('Enemy Choice (1-3): ')

        if enemyChoice == '1':
            enemyName = enemies[0][0]
            enemyHP = enemies[0][1]
            enemyAttack = enemies[0][2]
            rewardXP = enemies[0][3]
            rewardCoins = enemies[0][4]
            chosen = True

        elif enemyChoice == '2':
            enemyName = enemies[1][0]
            enemyHP = enemies[1][1]
            enemyAttack = enemies[1][2]
            rewardXP = enemies[1][3]
            rewardCoins = enemies[1][4]
            chosen = True

        elif enemyChoice == '3':
            enemyName = enemies[2][0]
            enemyHP = enemies[2][1]
            enemyAttack = enemies[2][2]
            rewardXP = enemies[2][3]
            rewardCoins = enemies[2][4]
            chosen = True

        else:
            playerHP = 0

        playerAttack = strength
        playerHP = HP
        playerMP = MP
        
        turn = random.randint(1, 2)
        while enemyHP > 0 and playerHP > 0:
            if turn == 1:
                print('You attack first!')
                print(f'1. Basic Attack ({str(strength)} damage)')
                print(f'2. Skill Attack ({str(strength * 2)} damage)')
                if healthPotion > 0:
                    print(f'3. Use Health Potion (Available: {str(healthPotion)})')
                if strengthPotion > 0:
                    print(f'4. Use Strength Potion (Available: {str(strengthPotion)})')
                if poisonBomb > 0:
                    print(f'5. Use Poison Bomb (Available: {str(poisonBomb)})')
                if regenStim > 0:
                    print(f'6. Use Regen Stim (Available: {str(regenStim)})')
                
                attackType = input('\nAttack Type (1, 2, 3 or 4): ')
                if attackType == '1':
                    enemyHP = enemyHP - strength
                    print(f"You attacked! {enemyName}'s HP is now {enemyHP}")

                elif attackType == '2':
                    if playerMP >= 5:
                        enemyHP = enemyHP - (strength * 2)
                        playerMP = playerMP - 5
                        print(f"You attacked! {enemyName}'s HP is now {enemyHP}")

                    else:
                        print('Not enough MP! Using basic MP instead')
                        enemyHP = enemyHP - strength
                        print(f"You attacked! {enemyName}'s HP is now {enemyHP}")

                elif attackType == '3' and healthPotion > 0:
                    playerHP = HP
                    healthPotion = healthPotion - 1
                    print('Health Potion used! Full HP recovered!')

                elif attackType == '4' and strengthPotion > 0:
                    effects = playerAttack * 0.3
                    playerAttack = round(playerAttack + effects)
                    strengthPotion = strengthPotion - 1
                    print('Strength potion used! Strength increased by 30%')

                elif attackType == '5' and poisonBomb > 0:
                    enemyDOT += round(enemyHP * 0.1)
                    poisonBomb = poisonBomb - 1
                    print(f'Poison Bomb used! The {enemyName} will now be receiving {str(enemyDOT)} per turn!')
                        
                turn = 2
                    
            elif turn == 2:
                if enemyDOT > 0:
                    enemyHP = enemyHP - enemyDOT
                    print(f'The {enemyName} received {str(enemyDOT)} damage')
                    print(f"The {enemyName}'s HP is now {enemyHP}")
                    
                    
                print(f'The {enemyName} attacks first!')
                if probability(EVADE / 100):
                    print('You evaded the attack.')
                    print('No damage taken!')

                else:
                    playerHP = playerHP - enemyAttack
                    print(f'You received {str(enemyAttack)} damage!')
                    
                print(f'Your HP is now {str(playerHP)}!')

                turn = 1

            if enemyHP <= 0:
                excessPoints = excessPoints + 1
                coins = coins + rewardCoins
                XP = XP + rewardXP
                print('You won the battle! Received:')
                print('- 1 status point')
                print(f'- {rewardCoins} reward C$')
                print(f'- {rewardXP} reward XP')

                if XP >= 1000:
                    level = level + 1
                    XP = 0
                    print(f'You have reached level {level}!')

            elif playerHP <= 0:
                print('You lost the battle! Received nothing')

            input('Press enter to continue...')
            os.system('cls')

    elif gameChoice == '4':
        running = True
        
        while running:
            os.system('cls')
            print('Welcome to the shop')
            print()
            print(f'What do you want to buy? You have {str(coins)}C$ and {str(diamonds)}D$')
            print('1. Health potion - 300C$')
            print('2. Strength potion - 890C$')
            print('3. Poison Bomb - 1400C$')
            print('4. Regen Stim - 2000C$')
            print('5. Exchange D$ for C$ - 5000C$/piece')
            print('6. Nothing - exit the shop')
            shopChoice = input('1-3> ')

            if shopChoice == '1':
                quantity = int(input('How many to buy? '))
                if coins >= 300:
                    healthPotion = healthPotion + quantity
                    coins = coins - (quantity * 300)
                    
                    print(f'\nSuccessfully purchased {quantity}x Health Potion')
                    print(f'Coins: {coins}')
                    print()
                    input('Press enter to continue...')

                else:
                    print('Not enough C$')
                    input('Press enter to continue...')

            if shopChoice == '2':
                quantity = int(input('How many to buy? '))
                if coins >= 890:
                    strengthPotion = strengthPotion + quantity
                    coins = coins - (quantity * 890)
                    
                    print(f'\nSuccessfully purchased {quantity} strength potion(s)')
                    print(f'Coins: {coins}')
                    print()
                    input('Press enter to continue...')

                else:
                    print('Not enough C$')
                    input('Press enter to continue...')

            if shopChoice == '3':
                quantity = int(input('How many to buy? '))
                if coins >= 1400:
                    poisonBomb = poisonBomb + quantity
                    coins = coins - (quantity * 1400)
                    
                    print(f'\nSuccessfully purchased {quantity} poison bomb(s)')
                    print(f'Coins: {coins}')
                    print()
                    input('Press enter to continue...')

                else:
                    print('Not enough C$')
                    input('Press enter to continue...')

            if shopChoice == '4':
                quantity = int(input('How many to buy? '))
                if coins >= 2000:
                    regenStim = regenStim + quantity
                    coins = coins - (quantity * 2000)
                    
                    print(f'\nSuccessfully purchased {quantity} regen stims(s)')
                    print(f'Coins: {coins}')
                    print()
                    input('Press enter to continue...')

                else:
                    print('Not enough C$')
                    input('Press enter to continue...')

            if shopChoice == '5':
                if diamonds > 0:
                    amount = int(input('How many to exchange? '))
                    if amount <= diamonds:
                        diamonds = diamonds - amount
                        coins = coins + (amount * 5000)
                        print(f'Coins: {coins}')
                        print(f'Diamonds: {diamonds}')
                        print()
                        print('Press enter to continue...')

            if shopChoice == '6':
                input('Exiting the shop... (Press enter to continue)')
                running = False
                
    elif gameChoice == '5':
        
        print('Thanks for playing!')
        sys.exit()
