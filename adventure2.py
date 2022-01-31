#from re import A
#from this import d
#from turtle import pos
from colorama import Fore, Style
import keyboard
from tabulate import tabulate
# from win32con import BROADCAST_QUERY_DENY
#map                                                                                                                                       #print(tabulate(map, headers='firstrow', tablefmt='grid'))
map = [["a","b","c","d","e","f","g","h","i",""],
["desert", "desert", "desert", "desert","plains","plains","plains","plains","abandoned house","1"], 
["desert", "desert", "desert", "plains","plains","plains","plains","muddy dirt","muddy dirt","2"],
["desert", "desert", "mountain", "mountain","plains","plains","muddy dirt","lake","lake","3"], 
["snow", "snow", "snow", "river","bridge","river","woods","woods","woods","4"],
["snow", "snow", "snow", "muddy road","muddy road","muddy road","woods","woods","woods","5"],
["road", "road", "road", "road","start","road","road","woods","woods","6"]]
answer = 0
game = "alive"
health = 100

Introduction = "Welcome to the game your objective is to kill the final boss you move by typing where would you like to go for example 'left' or 'right' the choice is yours and if you type the letter 'm' it will show you the map and it will say where you are. Also there are items that you can use for example 'gun' 'sword', there are enemies like 'goblin' 'aligator'.So lets start good luck and don't die."

MapPrint = (tabulate(map, headers='firstrow', tablefmt='grid'))

inventory = {"gun":False,"axe":False,"HealingPots":False,"rock": False,"sword":False,"stick":True}

enemies = {"aligator":False,"person":False,"goblin":False,"village":False,"zombie":False}

alive ={"aligator":True,"person":True,"goblin":True,"village":True,"zombie":True}

A1 = {"text":"You are in an abandoned house.You just find a gun. there is plains on your left muddy dirt behind you. Where would you like to go?(left/backwards)",
"item":"gun","moves":"0011","enemies":False,"letter":"A","number":"1"
}

A2 = {"text":"You are in muddy dirt.To your left there is more muddy dirt forward there is an abandoned house and backwards there is a lake. Where would you like to go?(left/backwards/forwards)"
,"item":False,"moves":"1011","enemies":False,"letter":"A","number":"2"
}

A3 = {"text":"you are in the lake there is a 30 present chance that the aligator will attack you.there is muddy dirt in front of you woods behind you and lake left from you. Where would you like to go?(left/forwards/backwards)"
,"item":False,"moves":"1011","enemies":"aligator","letter":"A","number":"3"
}

A4 = {"text":"You are in woods. To your left there is more woods backwards there is more woods and forward there is a lake. Where would you like to go?(left/forward/backwards)"
,"item":False,"moves":"1011","enemies":False,"letter":"A","number":"4"
}

A5 = {"text":"you are in woods. There is woods to your right forwards and backwards. Where would you like to go?(left/forward/backwards)"
,"item":False,"moves":"1011","enemies":False,"letter":"A","number":"5"
}

A6 = {"text":"you are in woods. There is woods to your right and in front of you .Where would you like to go?(left/forward)"
,"item":False,"moves":"1001","enemies":False,"letter":"A","number":"6"
}

B1 = {"text":"you are in plains.To your right there is an abandoned house to your left is more plains and backwards there is muddy dirt .Where would you like to go?(left/right/backwards)"
,"item":False,"moves":"0111","enemies":False,"letter":"B","number":"1"
}

B2 = {"text":"You are in muddy dirt there is more muddy dirt to your right there is plains to your left and in front of you and a lake behind you.Where would you like to go?(left/right/backwards/forwards)"
,"item":False,"moves":"1111","enemies":False,"letter":"B","number":"2"
}

B3 = {"text":"you are in the lake there is a 30 present chance that the aligator will attack you.there is muddy dirt in front of you woods behind you and muddy dirt to your left. Where would you like to go?(left/forwards/backwards)"
,"item":False,"moves":"1111","enemies":"aligator","letter":"B","number":"3"
}

B4 = {"text":"You got an axe. You are in woods , there is woods on your left ,right and behind you and a lake in front of you.Where would you like to go?(left/right/backwards/forwards)"
,"item":"axe","moves":"1111","enemies":False,"letter":"B","number":"4"
}

B5 = {"text":"You are in woods. There is woods in every direction.Where would you like to go?(left/right/backwards/forwards)"
,"item":False,"moves":"1111","enemies":False,"letter":"B","number":"5"
}

B6 = {"text":"you are in woods there is woods to your right and forwards and a road to your left.Where would you like to go?(left/right/forwards)"
,"item":False,"moves":"1101","enemies":False,"letter":"B","number":"6"
}

C1 = {"text":"you are in plains. There is plains in your right ,left and behind you.Where would you like to go?(left/right/backwards)"
,"item":False,"moves":"0111","enemies":False,"letter":"C","number":"1"
}

C2 = {"text":"you are in plains.There are plains to your left an in front of you and muddy dirt on your right and behind you.Where would you like to go?(left/right/backwards/forwards)"
,"item":False,"moves":"1111","enemies":False,"letter":"C","number":"2"
}

C3 = {"text":"You are in muddy dirt.To your left and in front of you there are plains to your right there is a lake and behind you there are woods.Where would you like to go?(left/right/backwards/forwards)"
,"item":False,"moves":"1111","enemies":False,"letter":"C","number":"3"
}

C4 = {"text":"You are in woods.To your left there is a river to your right there is woods forwards there is muddy dirt and behind there is woods.Where would you like to go?(right/backwards/forwards)"
,"item":False,"moves":"1110","enemies":False,"letter":"C","number":"4"
}

C5 = {"text":"You are in woods. There are woods to your right and in front of you and roads behind an to your left.Where would you like to go?(left/right/backwards/forwards)"
,"item":False,"moves":"1111","enemies":False,"letter":"C","number":"5"
}

C6 = {"text":"You are in a road there are woods to your right and in front of you and there is a road to your left.Where would you like to go (left/right/forwards)"
,"item":False,"moves":"1101","enemies":False,"letter":"C","number":"6"
}

D1 = {"text":"you got a healing pots. there are plains to your right behind you and to your left.Where would you like to go(right/back/left)"
,"item":"HealingPots","moves":"0111","enemies":False,"letter":"D","number":"1"
}

D2 = {"text":"There is a person would you like to attack to him or ignore him?There are plains in all directions.What would you like to do(attack/left/right/backwards/forwards)"
,"item":False,"moves":"1111","enemies":"person","letter":"D","number":"2"
}

D3 = {"text":"You are in muddy dirt.There is plains to your right and in front of you and muddy dirt.Where would you like to go?(left/forwards/right)"
,"item":False,"moves":"1101","enemies":"person","letter":"D","number":"3"
}

D5 = {"text":"You are in a road. there is a muddy road to your left a road behind you and woods to your right.Where would you like to go(left/right/backwards)?"
,"item":False,"moves":"0111","enemies":"person","letter":"D","number":"5"
}

D6 = {"text":"You are in a road. There are roads to your right and in front of you and the start to your left. Where would you like to go?(left/right/forwards)"
,"item":False,"moves":"1101","enemies":False,"letter":"D","number":"6"
}

E1 = {"text":"You are in plains there are plains to your right and behind you and desert to your left.Where wold you like to go?(right/left/backwards)"
,"item":False,"moves":"0111","enemies":False,"letter":"E","number":"1"
}

E2 = {"text":"You are in plains.There are plains in all directions.Where would you like to go?(left/right/farwards/backwards)"
,"item":False,"moves":"1111","enemies":False,"letter":"E","number":"2"
}

E3 = {"text":"Your in plains.There are plains to your left and in front of you, a mountain to your left and a bridge behind you.Where would you like to go?(left/right/backwards/forwards)"
,"item":False,"moves":"1111","enemies":False,"letter":"E","number":"3"
}

E4 = {"text":"You are in a bridge don't worry the bridge is safe.There is muddy road behind you and plains in front of you.Where would you like to go?(backwards/forwards)"
,"item":False,"moves":"1010","enemies":False,"letter":"E","number":"4"
}

E5 = {"text":"You are in a muddy road.There are roads to your left and right , bridge in front of you and the start behind you.Where would you like to go?(left/right/backwards/forwards)"
,"item":False,"moves":"1111","enemies":False,"letter":"E","number":"5"
}

E6 = {"text":"You are at the start there are roads to your left and right and a muddy road in front of you.Where would you like to go?(left/right/forwards)"
,"item":False,"moves":"1101","enemies":False,"letter":"E","number":"6"
}

F1 = {"text":"You are in a desert.There are plains to your right and behind you and desert to your left.Where would you like to go?(left/right/backwards)"
,"item":False,"moves":"0111","enemies":False,"letter":"F","number":"1"
}

F2 = {"text":"You are in plains.There are plains to your right,mountain behind you and desert to your left and in front of you.Where would you like to go?(left/right/backwards/forwards)"
,"item":False,"moves":"1111","enemies":False,"letter":"F","number":"2"
}

F3 = {"text":"You are in a mountain. there are plains to your left and in front of you and the mountain goes also to your left.Where would you like to go?(left/right/forwards)"
,"item":False,"moves":"1101","enemies":False,"letter":"F","number":"3"
}

F5 = {"text":"You are in a road there is muddy road to your left,road behind you and snow to your left.Where would you like to go?(left/right/backwards)"
,"item":False,"moves":"0111","enemies":False,"letter":"F","number":"5"
}

F6 = {"text":"You are in a road you just got a boat!.there are roads to your left and in front of you and the start to your right.Where would you like to go?(left/right/forwards)"
,"item":"boat","moves":"1101","enemies":False,"letter":"F","number":"6"
}

G1 = {"text":""
,"item":False,"moves":"0111","enemies":"zombie","letter":"G","number":"1"
}

G2 = {"text":""
,"item":False,"moves":"1111","enemies":False,"letter":"G","number":"2"
}

G3 = {"text":""
,"item":False,"moves":"1111","enemies":False,"letter":"G","number":"3"
}

G4= {"text":""
,"item":False,"moves":"1011","enemies":False,"letter":"G","number":"4"
}

G5 = {"text":""
,"item":False,"moves":"1111","enemies":False,"letter":"G","number":"5"
}

G6 = {"text":""
,"item":False,"moves":"1101","enemies":False,"letter":"G","number":"6"
}

H1 = {"text":""
,"item":False,"moves":"0111","enemies":False,"letter":"H","number":"1"
}

H2 = {"text":""
,"item":False,"moves":"1111","enemies":False,"letter":"H","number":"2"
}

H3 = {"text":""
,"item":False,"moves":"1111","enemies":"goblin","letter":"H","number":"3"
}

H4 = {"text":""
,"item":False,"moves":"1111","enemies":False,"letter":"H","number":"4"
}

H5 = {"text":""
,"item":False,"moves":"1111","enemies":"village","letter":"H","number":"5"
}

H6 = {"text":""
,"item":False,"moves":"1101","enemies":False,"letter":"H","number":"6"
}

I1 = {"text":""
,"item":"sword","moves":"0110","enemies":False,"letter":"I","number":"1"
}

I2 = {"text":""
,"item":False,"moves":"1110","enemies":False,"letter":"I","number":"2"
}

I3 = {"text":""
,"item":False,"moves":"1110","enemies":False,"letter":"I","number":"3"
}

I4 = {"text":""
,"item":False,"moves":"1110","enemies":False,"letter":"I","number":"4"
}

I5 = {"text":""
,"item":False,"moves":"1110","enemies":False,"letter":"I","number":"5"
}

I6 = {"text":""
,"item":False,"moves":"1100","enemies":False,"letter":"I","number":"6"
}

#{"text":,"item":False,"moves":"1111","enemies":False}




##start
#Example movement:
#answer = input(position["text"])
# TODO:make start posiosion random?!
position = E6
StringPos = position["letter"],position["number"]
print(Fore.RED + Introduction + Fore.WHITE)


def moveOptions(pos):
    answer = input(pos["text"])
    print("Your answer was: " + answer)
    if answer=="left":
        newPos = (chr(ord(pos["letter"]) - 1) + pos["number"])
        print(globals()[newPos])
        moveOptions(globals()[newPos])
    if answer=="right":
        newPos = (chr(ord(pos["letter"]) + 1) + pos["number"])
        print(globals()[newPos])
        moveOptions(globals()[newPos])
    if answer=="forwards":
        newPos = pos["letter"] + (chr(ord( pos["number"]) - 1))
        print(globals()[newPos])
        moveOptions(globals()[newPos])
    if answer=="backwards":
        newPos = pos["letter"] + (chr(ord( pos["number"]) + 1))
        print(globals()[newPos])
        moveOptions(globals()[newPos])
    

moveOptions(E6) #first move












# while game == "alive":
#     while keyboard.is_pressed("m") == True:
#         print(MapPrint)
#         print("you are in:",Fore.BLUE,StringPos,Fore.WHITE)
#         break

#     while health > 0:
#         for i in range(1000000000):
#             if answer == "right":
#                 if position == A1:
#                     position = B1
#                 elif position == A2:
#                     position = B2
#                 elif position == A3:
#                     position = B3
#                 elif position == A4:
#                     position = B4
#                 elif position == A5:
#                     position = B5    
#                 elif position == A6:
#                     position = B6
#                 elif position == B1:
#                     position = C1
#                 elif position == B2:
#                     position = C2
#                 elif position == B3:
#                     position = C3
#                 elif position == B4:
#                     position = C4
#                 elif position == B5:
#                     position = C5    
#                 elif position == B6:
#                     position = C6
#                 elif position == C1:
#                     position = D1
#                 elif position == C2:
#                     position = D2
#                 elif position == C3:
#                     position = D3
#                 elif position == C5:
#                     position = D5    
#                 elif position == C6:
#                     position = D6        
#                 elif position == D1:
#                     position = E1
#                 elif position == D2:
#                     position = E2
#                 elif position == D3:
#                     position = E3
#                 elif position == D5:
#                     position = E5    
#                 elif position == D6:
#                     position = E6
#                 elif position == E1:
#                     position = F1
#                 elif position == E2:
#                     position = F2
#                 elif position == E3:
#                     position = F3
#                 elif position == E5:
#                     position = F5    
#                 elif position == E6:
#                     position = F6
#                 elif position == F1:
#                     position = G1
#                 elif position == F2:
#                     position = G2
#                 elif position == F3:
#                     position = G3
#                 elif position == F5:
#                     position = G5    
#                 elif position == F6:
#                     position = G6
#                 elif position == G1:
#                     position = H1
#                 elif position == G2:
#                     position = H2
#                 elif position == G3:
#                     position = H3
#                 elif position == G4:
#                     position = H4
#                 elif position == G5:
#                     position = H5    
#                 elif position == G6:
#                     position = H6
#                 elif position == H1:
#                     position = I1
#                 elif position == H2:
#                     position = I2
#                 elif position == H3:
#                     position = I3
#                 elif position == H4:
#                     position = I4
#                 elif position == H5:
#                     position = I5    
#                 elif position == H6:
#                     position = I6
#                 answer = input(position["text"])
                

#             elif answer == "left":
#                 if position == B1:
#                     position = A1
#                 elif position == B2:
#                     position = A2
#                 elif position == B3:
#                     position = A3
#                 elif position == B4:
#                     position = A4
#                 elif position == B5:
#                     position = A5    
#                 elif position == B6:
#                     position = A6
#                 elif position == C1:
#                     position = B1
#                 elif position == C2:
#                     position = B2
#                 elif position == C3:
#                     position = B3
#                 elif position == C4:
#                     position = B4
#                 elif position == C5:
#                     position = B5    
#                 elif position == C6:
#                     position = B6
#                 elif position == D1:
#                     position = C1
#                 elif position == D2:
#                     position = C2
#                 elif position == D3:
#                     position = C3
#                 elif position == D5:
#                     position = C5    
#                 elif position == D6:
#                     position = C6        
#                 elif position == E1:
#                     position = D1
#                 elif position == E2:
#                     position = D2
#                 elif position == E3:
#                     position = D3
#                 elif position == E5:
#                     position = D5    
#                 elif position == E6:
#                     position = D6
#                 elif position == F1:
#                     position = E1
#                 elif position == F2:
#                     position = E2
#                 elif position == F3:
#                     position = E3
#                 elif position == F5:
#                     position = E5    
#                 elif position == F6:
#                     position = E6
#                 elif position == G1:
#                     position = F1
#                 elif position == G2:
#                     position = F2
#                 elif position == G3:
#                     position = F3
#                 elif position == G5:
#                     position = F5    
#                 elif position == G6:
#                     position = F6
#                 elif position == H1:
#                     position = G1
#                 elif position == H2:
#                     position = G2
#                 elif position == H3:
#                     position = G3
#                 elif position == H4:
#                     position = G4
#                 elif position == H5:
#                     position = G5    
#                 elif position == H6:
#                     position = G6
#                 elif position == I1:
#                     position = H1
#                 elif position == I2:
#                     position = H2
#                 elif position == I3:
#                     position = H3
#                 elif position == I4:
#                     position = H4
#                 elif position == I5:
#                     position = H5    
#                 elif position == I6:
#                     position = H6

#                 answer = input(position["text"])
                

#             elif answer == "backwards":
#                 if position == A1:
#                     position = A2
#                 elif position == A2:
#                     position = A3
#                 elif position == A3:
#                     position = A4
#                 elif position == A4:
#                     position = A5
#                 elif position == A5:
#                     position = A6    
#                 elif position == B1:
#                     position = B2
#                 elif position == B2:
#                     position = B3
#                 elif position == B3:
#                     position = B4
#                 elif position == B4:
#                     position = B5
#                 elif position == B5:
#                     position = B6
#                 elif position == C1:
#                     position = C2
#                 elif position == C2:
#                     position = C3    
#                 elif position == C3:
#                     position = C4
#                 elif position == C4:
#                     position = C5
#                 elif position == C5:
#                     position = C6
#                 elif position == D1:
#                     position = D2
#                 elif position == D2:
#                     position = D3        
#                 elif position == D5:
#                     position = D6
#                 elif position == E1:
#                     position = E2
#                 elif position == E2:
#                     position = E3
#                 elif position == E3:
#                     position = E4
#                 elif position == E4:
#                     position = E5
#                 elif position == E5:
#                     position = E6    
#                 elif position == F1:
#                     position = F2
#                 elif position == F2:
#                     position = F3
#                 elif position == F5:
#                     position = F6    
#                 elif position == G1:
#                     position = G2
#                 elif position == G2:
#                     position = G3
#                 elif position == G3:
#                     position = G4
#                 elif position == G4:
#                     position = G5
#                 elif position == G5:
#                     position = G6    
#                 elif position == H1:
#                     position = H2
#                 elif position == H2:
#                     position = H3
#                 elif position == H3:
#                     position = H4
#                 elif position == H4:
#                     position = H5
#                 elif position == H5:
#                     position = H6
#                 elif position == I1:
#                     position = I2    
#                 elif position == I2:
#                     position = I3
#                 elif position == I3:
#                     position = I4
#                 elif position == I4:
#                     position = I5
#                 elif position == I5:
#                     position = I6
                
#                 answer = input(position["text"])

#             elif answer == "forwards":
#                 if position == A2:
#                     position = A1
#                 elif position == A3:
#                     position = A2
#                 elif position == A4:
#                     position = A3
#                 elif position == A5:
#                     position = A4
#                 elif position == A6:
#                     position = A5   
#                 elif position == B2:
#                     position = B1
#                 elif position == B3:
#                     position = B2
#                 elif position == B4:
#                     position = B3
#                 elif position == B5:
#                     position = B4
#                 elif position == B6:
#                     position = B5
#                 elif position == C2:
#                     position = C1
#                 elif position == C3:
#                     position = C2 
#                 elif position == C4:
#                     position = C3
#                 elif position == C5:
#                     position = C4
#                 elif position == C6:
#                     position = C5
#                 elif position == D2:
#                     position = D1
#                 elif position == D3:
#                     position = D2         
#                 elif position == D6:
#                     position = D5
#                 elif position == E2:
#                     position = E1
#                 elif position == E3:
#                     position = E2
#                 elif position == E4:
#                     position = E3
#                 elif position == E5:
#                     position = E4   
#                 elif position == E6:
#                     position = E5
#                 elif position == F2:
#                     position = F1
#                 elif position == F3:
#                     position = F2   
#                 elif position == F6:
#                     position = F5
#                 elif position == G2:
#                     position = G1
#                 elif position == G3:
#                     position = G2
#                 elif position == G4:
#                     position = G3    
#                 elif position == G5:
#                     position = G4
#                 elif position == G6:
#                     position = G5
#                 elif position == H2:
#                     position = H1
#                 elif position == H3:
#                     position = H2
#                 elif position == H4:
#                     position = H3
#                 elif position == H5:
#                     position = H4    
#                 elif position == H6:
#                     position = H5
#                 elif position == I2:
#                     position = I1
#                 elif position == I3:
#                     position = I2
#                 elif position == I4:
#                     position = I3
#                 elif position == I5:
#                     position = I4
#                 elif position == I6:
#                     position = I5
#                 answer = input(position["text"])
# game = "dead"
if game == "s":
    print(Fore.RED + "You failed!" + Fore.WHITE)

# print(position["letter"],position["number"])