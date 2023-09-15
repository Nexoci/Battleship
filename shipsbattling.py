#Made by: Konnor Kobelka
#Date Start: 9/7/2023
#Name: Battleship
import random, time

global slots
guessed_spots = []
grid = ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"] 
#slots = ["A1","A2","A3","A4","A5","B1","B2","B3","B4","B5","C1","C2","C3","C4","C5","D1","D2","D3","D4","D5","E1","E2","E3","E4","E5",]

ship_hits = 0


def shiplocation():
    global ship1
    global ship2
    ship1 = random.randint(1,10)
    ship2 = random.randint(1,10)
    print(ship1)
    print(ship2) 


     
def intro():     
    print(" _    _      _                            _____      ______       _   _   _           _     _       ")
    time.sleep(0.2)
    print("| |  | |    | |                          |_   _|     | ___ \     | | | | | |         | |   (_)      ")
    time.sleep(0.2)
    print("| |  | | ___| | ___ ___  _ __ ___   ___    | | ___   | |_/ / __ _| |_| |_| | ___  ___| |__  _ _ __  ")
    time.sleep(0.2)
    print("| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \   | |/ _ \  | ___ \/ _` | __| __| |/ _ \/ __| '_ \| | '_ \ ")
    time.sleep(0.2)
    print("\  /\  /  __/ | (_| (_) | | | | | |  __/   | | (_) | | |_/ / (_| | |_| |_| |  __/\__ \ | | | | |_) |")
    time.sleep(0.2)
    print(" \/  \/ \___|_|\___\___/|_| |_| |_|\___|   \_/\___/  \____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ ")
    time.sleep(0.2)
    print("                                                                                             |_|    ")
    time.sleep(0.2)
    print("----------------------------------------------------------------------------------------------------")
    print("                                  a game of ships battling []")
    print("")
    


def board():
    global turns, done
    print("   A   B   C   D   E")
    print(("1"),(grid[0]),(grid[1]),(grid[2]),(grid[3]),(grid[4]))
    print(("2"),(grid[5]),(grid[6]),(grid[7]),(grid[8]),(grid[9]))
    print(("3"),(grid[10]),(grid[11]),(grid[12]),(grid[13]),(grid[14]))
    print(("4"),(grid[15]),(grid[16]),(grid[17]),(grid[18]),(grid[19]))
    print(("5"),(grid[20]),(grid[21]),(grid[22]),(grid[23]),(grid[24]))
    turns=turns+1
    print(f"Move {turns} of 12")


def guess():
    global turns,done
    gridvalues = dict({"A":0, "B":1, "C":2, "D":3, "E":4, "a":0, "b":1, "c":2, "d":3, "e":4})
    playerguess= input("Enter Guess: ")
    if len(playerguess) == 2:
        column = playerguess[0]
        row = int(playerguess[1])
    finalguess = gridvalues[column] + (row-1)*5
    print(ship_hits)
    if finalguess in guessed_spots:
        print("You already guessed this spot. Try again.")
    else:
        # Add the guessed spot to the list
        guessed_spots.append(finalguess)
        
    if finalguess == 0:
        if ship1==6 or ship2 ==6:
            grid[0] = "[X]"
            print("HIT!")
            
        else:
            grid[0] = "[O]"
            print("Miss")
    elif finalguess == 1:
        if ship1==9 or ship2 ==9:
            grid[1] = "[X]"
            print("HIT!")
        else:
            grid[1] = "[O]"
            print("Miss")
    elif finalguess == 2:
        if ship1==9 or ship2 ==9:
            grid[2] = "[X]"
            print("HIT!")
        else:
            grid[2] = "[O]"
            print("Miss")
    elif finalguess == 3:
        if ship1==4 or ship2 ==4:
            grid[3] = "[X]"
            print("HIT!")
        else:
            grid[3] = "[O]"
            print("Miss")
    elif finalguess == 4:
        if ship1==3 or ship2 ==3:
            grid[4] = "[X]"
            print("HIT!")
        else:
            grid[4] = "[O]"
            print("Miss")
    elif finalguess == 5:
        if ship1==6 or ship2 ==6:
            grid[5] = "[X]"
            print("HIT!")
        else:
            grid[5] = "[O]"
            print("Miss")
    elif finalguess == 6:
        if ship1==1 or ship2 ==1:
            grid[6] = "[X]"
            print("HIT!")
        else:
            grid[6] = "[O]"
            print("Miss")
    elif finalguess == 7:
        if ship1==1 or ship2 ==1:
            grid[7] = "[X]"
            print("HIT!")
        else:
            grid[7] = "[O]"
            print("Miss")
    elif finalguess == 8:
        if ship1==4 or ship2 ==4:
            grid[8] = "[X]"
            print("HIT!")
        else:
            grid[8] = "[O]"
            print("Miss")
    elif finalguess == 9:
        if ship1==3 or ship2 ==3:
            grid[9] = "[X]"
            print("HIT!")
        else:
            grid[9] = "[O]"
            print("Miss")
    elif finalguess == 10:
        if ship1==7 or ship2 ==7:
            grid[10] = "[X]"
            print("HIT!")
        else:
            grid[10] = "[O]"
            print("Miss")
    elif finalguess == 11:
        if ship1==7 or ship2 ==7:
            grid[11] = "[X]"
            print("HIT!")
        else:
            print("Miss")
            grid[11] = "[O]"
    elif finalguess == 12:
        if ship1==7 or ship2 ==7:
            grid[12] = "[X]"
            print("HIT!")
        else:
            grid[12] = "[O]"
            print("Miss")
    elif finalguess == 13:
        if ship1==7 or ship2 ==7:
            grid[13] = "[X]"
            print("HIT!")
        else:
            grid[13] = "[O]"
            print("Miss")
    elif finalguess == 14:
        if ship1==3 or ship2 ==3:
            grid[14] = "[X]"
            print("HIT!")
        else:
            grid[14] = "[O]"
            print("Miss")
    elif finalguess == 15:
        if ship1==2 or ship2 ==2:
            grid[15] = "[X]"
            print("HIT!")
        else:
            grid[15] = "[O]"
            print("Miss")
    elif finalguess == 16:
        if ship1==10 or ship2 ==10:
            grid[16] = "[X]"
            print("HIT!")
        else:
            grid[16] = "[O]"
            print("Miss")
    elif finalguess == 17:
        if ship1==10 or ship2 ==10:
            grid[17] = "[X]"
            print("HIT!")
        else:
            grid[17] = "[O]"
            print("Miss")
    elif finalguess == 18:
        if ship1==10 or ship2 ==10:
            grid[18] = "[X]"
            print("HIT!")
        else:
            grid[18] = "[O]"
            print("Miss")
    elif finalguess == 19:
        grid[19] = "[O]"
        print("Miss")        

    elif finalguess == 20:
        if ship1==2 or ship2 ==2:
            grid[20] = "[X]"
            print("HIT!")
        else:
            grid[20] = "[O]"
            print("Miss")
    elif finalguess == 21:
        if ship1==8 or ship2 ==8:
            grid[21] = "[X]"
            print("HIT!")
        else:
            grid[21] = "[O]"
            print("Miss")
    elif finalguess == 22:
        if ship1==8 or ship2 ==8:
            grid[22] = "[X]"
            print("HIT!")
        else:
            grid[22] = "[O]"
            print("Miss")
    elif finalguess == 23:
        if ship1==5 or ship2 ==5:
            grid[23] = "[X]"
            print("HIT!")
            grid[23] = "[O]"
        else:
            print("Miss")
    elif finalguess == 24:
        if ship1==5 or ship2 ==5:
            grid[24] = "[X]"
            print("HIT!")
        else:
            grid[24] = "[O]"
            print("Miss")
    if turns == 11:
        print("GAME OVER!")
        done = True
    

    
    time.sleep(1)
   

intro()
time.sleep(1)
turns=0
shiplocation()

done = False
while not done:    
    board()
    guess()
    #print('\x1bc')
