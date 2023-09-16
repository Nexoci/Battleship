#Made by: Konnor Kobelka
#Date Start: 9/7/2023
#Name: Battleship

#Import necessary libraries
import random, time
#Define global variables
global ship_hits
global slots
#List of grids
guessed_spots = []
grid = ["[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"] 
#slots = ["A1","A2","A3","A4","A5","B1","B2","B3","B4","B5","C1","C2","C3","C4","C5","D1","D2","D3","D4","D5","E1","E2","E3","E4","E5",]

ship_hits = 0

#Function to randomly generate ship locations
def shiplocation():
    global ship1
    global ship2
    ship1 = random.randint(1,10)
    ship2 = random.randint(1,10)
    #Ensure ship locations are different
    if ship1 ==ship2 or ship2==ship1:
        ship1 = random.randint(1,10)
        ship2 = random.randint(1,10)
    print(ship1)
    print(ship2) 


#Function to display game introduction 
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
    


#Function to display the game board
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

#Function for the player's guess
def guess():
    global turns,done,ship_hits
    
    gridvalues = dict({"A":0, "B":1, "C":2, "D":3, "E":4, "a":0, "b":1, "c":2, "d":3, "e":4})
    playerguess= input("Enter Guess: ")
    # Check if the input is in the correct format (e.g., "A1")
    if len(playerguess) != 2 or not playerguess[1].isdigit() or int(playerguess[1]) < 1 or int(playerguess[1]) > 5:
        print("Invalid guess. Please enter a valid guess in the format like 'A1', 'B2', etc.")
        turns=turns-1
        time.sleep(1)
        return
    if len(playerguess) == 2:
        column = playerguess[0]
        row = int(playerguess[1])
    finalguess = gridvalues[column] + (row-1)*5
    #Check if player guessed spot already
    if finalguess in guessed_spots:
        print("You already guessed this spot. Try again.")
        turns=turns-1
    else:
        guessed_spots.append(finalguess)
        
    #Check if the guess hits a ship or not and update the grid    
    if finalguess == 0:
        if ship1==6 or ship2 ==6:
            grid[0] = "[X]"
            print("HIT!")
            ship_hits = ship_hits+1
        else:
            grid[0] = "[O]"
            print("Miss")
    elif finalguess == 1:
        if ship1==9 or ship2 ==9:
            grid[1] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
        else:
            grid[1] = "[O]"
            print("Miss")
    elif finalguess == 2:
        if ship1==9 or ship2 ==9:
            grid[2] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
        else:
            grid[2] = "[O]"
            print("Miss")
    elif finalguess == 3:
        if ship1==4 or ship2 ==4:
            grid[3] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
        else:
            grid[3] = "[O]"
            print("Miss")
    elif finalguess == 4:
        if ship1==3 or ship2 ==3:
            grid[4] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
        else:
            grid[4] = "[O]"
            print("Miss")
    elif finalguess == 5:
        if ship1==6 or ship2 ==6:
            grid[5] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
        else:
            grid[5] = "[O]"
            print("Miss")
    elif finalguess == 6:
        if ship1==1 or ship2 ==1:
            grid[6] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
        else:
            grid[6] = "[O]"
            print("Miss")
    elif finalguess == 7:
        if ship1==1 or ship2 ==1:
            grid[7] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
        else:
            grid[7] = "[O]"
            print("Miss")
    elif finalguess == 8:
        if ship1==4 or ship2 ==4:
            grid[8] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
        else:
            grid[8] = "[O]"
            print("Miss")
    elif finalguess == 9:
        if ship1==3 or ship2 ==3:
            grid[9] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
        else:
            grid[9] = "[O]"
            print("Miss")
    elif finalguess == 10:
        if ship1==7 or ship2 ==7:
            grid[10] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
        else:
            grid[10] = "[O]"
            print("Miss")
    elif finalguess == 11:
        if ship1==7 or ship2 ==7:
            grid[11] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
        else:
            print("Miss")
            grid[11] = "[O]"
    elif finalguess == 12:
        if ship1==7 or ship2 ==7:
            grid[12] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
        else:
            grid[12] = "[O]"
            print("Miss")
    elif finalguess == 13:
        if ship1==7 or ship2 ==7:
            grid[13] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
        else:
            grid[13] = "[O]"
            print("Miss")
    elif finalguess == 14:
        if ship1==3 or ship2 ==3:
            grid[14] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
        else:
            grid[14] = "[O]"
            print("Miss")
    elif finalguess == 15:
        if ship1==2 or ship2 ==2:
            grid[15] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
        else:
            grid[15] = "[O]"
            print("Miss")
    elif finalguess == 16:
        if ship1==10 or ship2 ==10:
            grid[16] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
        else:
            grid[16] = "[O]"
            print("Miss")
    elif finalguess == 17:
        if ship1==10 or ship2 ==10:
            grid[17] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
        else:
            grid[17] = "[O]"
            print("Miss")
    elif finalguess == 18:
        if ship1==10 or ship2 ==10:
            grid[18] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
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
            ship_hits =ship_hits+1
        else:
            grid[20] = "[O]"
            print("Miss")
    elif finalguess == 21:
        if ship1==8 or ship2 ==8:
            grid[21] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
        else:
            grid[21] = "[O]"
            print("Miss")
    elif finalguess == 22:
        if ship1==8 or ship2 ==8:
            grid[22] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
        else:
            grid[22] = "[O]"
            print("Miss")
    elif finalguess == 23:
        if ship1==5 or ship2 ==5:
            grid[23] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
        else:
            grid[23] = "[O]"
            print("Miss")
    elif finalguess == 24:
        if ship1==5 or ship2 ==5:
            grid[24] = "[X]"
            print("HIT!")
            ship_hits =ship_hits+1
        else:
            grid[24] = "[O]"
            print("Miss")
             
    #Check for win or game over conditions
    if ship_hits == 4 and ((ship1 == 1 or ship1 == 2 or ship1 == 4 or ship1 == 5 or ship1 == 6 or ship1 == 8 or ship1 == 9) and (ship2 == 1 or ship2 == 2 or ship2 == 4 or ship2 == 5 or ship2 == 6 or ship2 == 8 or ship2 == 9)):
        board()
        print("You WIN!")
        if turns == 4:
            print(f"Flawless Victory in {turns} tries")
        else:
            print(f"It took you only {turns} tries to Win!")
        done= True
        
    if ship_hits == 5 and ((ship1 == 1 or ship1 == 2 or ship1 == 4 or ship1 == 5 or ship1 == 6 or ship1 == 8 or ship1 == 9) and (ship2 == 10 or ship2 == 3)):
        board()
        print("You WIN!")
        if turns == 5:
            print(f"Flawless Victory in {turns} tries")
        else:
            print(f"It took you only {turns} tries to Win!")
        done= True
        
    if ship_hits == 5 and ((ship2 == 1 or ship2 == 2 or ship2 == 4 or ship2 == 5 or ship2 == 6 or ship2 == 8 or ship2 == 9) and (ship1 == 10 or ship1 == 3)):
        board()
        print("You WIN!")
        if turns == 5:
            print(f"Flawless Victory in {turns} tries")
        else:
            print(f"It took you only {turns} tries to Win!")
        done= True
        
    if ship_hits == 6 and ((ship2 == 1 or ship2 == 2 or ship2 == 4 or ship2 == 5 or ship2 == 6 or ship2 == 8 or ship2 == 9) and (ship1 == 7)):
        board()
        print("You WIN!")
        if turns == 6:
            print(f"Flawless Victory in {turns} tries")
        else:
            print(f"It took you only {turns} tries to Win!")
        done= True
        
    if ship_hits == 6 and ((ship1 == 1 or ship1 == 2 or ship1 == 4 or ship1 == 5 or ship1 == 6 or ship1 == 8 or ship1 == 9) and (ship2 == 7)):
        board()
        print("You WIN!")
        if turns == 6:
            print(f"Flawless Victory in {turns} tries")
        else:
            print(f"It took you only {turns} tries to Win!")
        done= True
    
    if ship_hits == 7 and ((ship2 == 10 or ship2 == 3) and (ship1 == 7)):
        board()
        print("You WIN!")
        if turns == 7:
            print(f"Flawless Victory in {turns} tries")
        else:
            print(f"It took you only {turns} tries to Win!")
        done= True
    
    if ship_hits == 7 and ((ship1 == 10 or ship1 == 3) and (ship2 == 7)):
        board()
        print("You WIN!")
        if turns == 7:
            print(f"Flawless Victory in {turns} tries")
        else:
            print(f"It took you only {turns} tries to Win!")
        done= True
    
    if turns == 11:
        print("GAME OVER!")
        print(f"Unfortunately you used all {turns} tries and lost")
        done = True
        
    

    
    time.sleep(1)
   
#Call the introduction and ship location functions
intro()
time.sleep(1)
turns=0
shiplocation()

done = False
while not done:    
    board()
    guess()
    #print('\x1bc')
