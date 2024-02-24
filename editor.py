#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:13:14 2024

@author: carlgroundstine
"""

import json


def GetMenueChoice():     
    """print the menue out"""
    print("""
          0. exit the game
          1. load default game
          2. load game file
          3. save current game
          4. edit or create a node
          5. play the current game""")
    userChoice = input("please choose options 0-5")
    return userChoice

def main():
    game = defaultGame()
    keepGoing = True
    while keepGoing:
        userChoice = GetMenueChoice()
        if userChoice == 0:
            print("see you later")
            keepGoing = False
        elif userChoice == 1:
                print ("load default game")
        elif userChoice == 2:
                print("load game file")
        elif userChoice == 3:
                print("save current game")
        elif userChoice == 4:
                print("edit or create a node")
        elif userChoice == 5:
                print("Play the current game")
        else:
                print("something went wrong here")
                
def defaultGame():
  #base game
  game = {"start": ["default start node", "Start over", "start", "Quit", "quit"]}
  return game

def playGame(game):
   keepGoing =True
   node = "start"
   while keepGoing:
        node = playGame(game, node)
        if node == "quit":
           print("thanks for playing see you later")
           keepGoing = False
           
           
def playNode(dictionary, node):
    print(f"{dictionary[node][0]}")
    decision = input(f"""please choose one of the following
                     1. {dictionary[node][1]}
                     2. {dictionary[node][3]}
                     3. {dictionary[node][5]}
                     4. {dictionary[node][7]}
                     5. {dictionary[node][9]}""")
    if decision =="1":
        node = dictionary[2]
    elif decision =="2":
        node = dictionary[4]
    elif decision =="3":
        node = dictionary[6]
    elif decision =="4":
        node = dictionary[8]
    elif decision =="5":
        node = dictionary[10]
    
    else: 
        print("please type a number that coensides with your choice")
        
def saveGame(game):
    with open("game.json","w") as file:
        json.dump(game,file,indent=2)
    print("saved game and game.json")
    print(json.dumps(game, indent =2))

def loadGame(game): 
    """ uses JSON module to Load Game from game.json """
    fileIn = open("game.json", "r")
    game = json.load(fileIn)
    fileIn.close()
    return game

def editNode(game)

    print("current status of game:")
    print(json.dumps(game, indent=2))

    print("Existing node names: ")
    for nodeName in game.keys(): 
        print(f"  {nodeName}") 

    newNodeName = input("name of node to edit or create? ")
    if newNodeName in game.keys():
        newContent = game[newNodeName]
    else:
        newContent = ["", "", "", "", ""]
        print("Nodes needed: ")
        
    (desc, menuA, nodeA, menuB, nodeB) = newContent
    
    newDesc = getField("Description", desc)
    newMenuA = getField("Menu A", menuA)
    newNodeA = getField("Node A", nodeA)
    newMenuB = getField("Menu B", menuB)
    newNodeB = getField("Node B", nodeB)
    

    game[newNodeName] = [newDesc, newMenuA, newNodeA, newMenuB, newNodeB]

    return game

def getField(prompt, currentVal):
    """ prompts for a field if
        user presses any key, keep current value """
        
    newVal = input(f"{prompt} ({currentVal}): ")
    if newVal == "":
        newVal = currentVal
        
    return newVal

if __name__ == "__main__":           

   
    main()


    
    