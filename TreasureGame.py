print("Welcome to Treasure Island!!\n")
print("Your goal is to find the treasure!!\n")
decide=input("Which direction do you decide? may it be left or it be right?!?\n")
if decide=="right":
  print("Oops!You fell into a hole ;( ITS GAME OVER! ")
if decide=="left":
    new_decide=input("Do you decide to swim or to wait?!\n ")
    if new_decide=="swim":
      print("NOO! You got bitten by a shark :( ITS GAME OVER\n")
    if new_decide=="wait":
      new2_decide=input("Whichever door thy open has there faith checked.\n Alas pick a door may it be red , blue or yellow?!\n")
      if new2_decide=="red":
        print("HOT HOT!! You were burned to death :0 ITS GAME OVER\n")
      elif new2_decide=="blue":
        print("AHNOO!! You were eaten by beasts :| ITS GAME OVER\n")
      elif new2_decide=="yellow":
        print("CLICK!! You found the treasure!! Yay!\n YOU WON THE GAME!!")
      else:
        print("RIP BOZO!")
        
    


