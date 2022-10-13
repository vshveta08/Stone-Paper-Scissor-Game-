print("\n***** Stone, Paper, Scissor GAME *****\n ")
print("\nINSTRUCTIONS:- \n\n  -> Type one name which you have selected from stone, paper, scissor \n  -> Type stop when u want to quit the game")

print("\n\nYour Turn -")
u = input(" Choose any one:- ")

# imported random library
import random

while u!="stop":

     c = (random.choice(["stone", "paper", "scissor"]))
     print("\n Computer chooses:-",c)
     print("\n")

     if(u!="stop"):
          if(u=="stone" and c=="scissor"):
               print("You won🎉🎉\nBecause stone smashes scissor.\n")
          
               print("\nYour Turn -")
               u = input(" Choose any one:- ")

          elif(u=="scissor" and c=="paper"):
               print("You won🎉🎉\nBecause scissor cuts paper.\n")
           
               print("\nYour Turn -")
               u = input(" Choose any one:- ")

          elif(u=="paper" and c=="stone"):
               print("You won🎉🎉\nBecause paper covers stone.\n")
                     
               print("\nYour Turn -")
               u = input(" Choose any one:- ")

          elif(u=="scissor" and c=="stone"):
               print("Computer won🎉🎉\nBecause stone smashes scissor.\n")
                     
               print("\nYour Turn -")
               u = input(" Choose any one:- ")

          elif(u=="paper" and c=="scissor"):
               print("Computer won🎉🎉\nBecause scissor cuts paper.\n")
                     
               print("\nYour Turn -")
               u = input(" Choose any one:- ")

          elif(u=="stone" and c=="paper"):
               print("Computer won🎉🎉\nBecause paper covers stone.\n")
                     
               print("\nYour Turn -")
               u = input(" Choose any one:- ")

          elif(u==c):
               print("Tie!!\n")
                     
               print("\nYour Turn -")
               u = input(" Choose any one:- ")

          elif(u=="paper" and c=="paper"):
               print("Tie!!\n")
                     
               print("\nYour Turn -")
               u = input(" Choose any one:- ")

          elif(u=="scissor" and c=="scissor"):
               print("Tie!!\n")
                     
               print("\nYour Turn -")
               u = input(" Choose any one:- ")
           
          continue
 
     if(u=="stop"):
          break

