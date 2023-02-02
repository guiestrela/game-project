print("welcome to my first Project in py!!")
name = str(input("What is your name? ")).upper()
age = int(input("What is your age? "))

health = 15

if age >= 18:
    print("You are old enough")

    wants_to_play = str(input(f"{name} Do you wanna play? [YES/NO]")).upper()
    if wants_to_play == "YES":
        print("Let's play!")
        
        left_or_right = str(input("First choice... Left or Right(left/right)? "))
        if left_or_right == "left":
            ans = str(input("Nice, you follow the path a lake... Do swim across or go around?(across/around)? "))
            
            if ans == "around":
                print("You went around and reached te other side of the lake.")
            elif ans == "across":
                print("you managed to get across, but were bit by a snake and lost 5 of health.")
                health -= 5
                
            ans = str(input("You notice a house and a river. Which do you go to(river/house)? "))
            if ans == "house":
                print("You go to the house and got shot on the army by the owner...and you lose 5 health.")
                health -= 5
                 
                if health <= 0:
                    print("You now have 0 health You lose...") 
                else:
                    print("You have survived.")
                                
            else:
                print("You fell in the river and die...")        
       
        else:
            print("you fell dow and die")
    else:
        print("Cya...")
else:
    print("You are not old enough to play...")
