#Choose Your Own Adventure
#Tori Carroll and Jaina Lukose
# Fall semester 2021

def inventory() :
    
    items = {'Snack' : {'description' : 'Always good for a long plane ride!.',
                        'text' : "You eat them right away, you don't know how soon your next meal will come."},
             'Warm Sweatshirt' : {'description' : "You'll need this when you arrive back in Philadelphia for the holidays!",
                                  'text' : "You put on your sweatshirt. Hypothermia won't be as big of a concern."},
             'Book' : {'description' : 'This will make the ride less boring.',
                       'text' : 'You can use the pages to start a fire later.'},
             'First Aid' : {'description' : 'To help you in case of accidents',
                            'text' : 'You got lucky packing this one!'},
             'Phone Charger' : {'description' : 'So you can make sure you can call your family when you arrive!',
                                'text' : 'No outlets on the island unfortunately.'}
                 }
    #Create an empty list named backpack for all
    #valid choices made by the adventurer to be stored
    backpack = []
    #Inventory capacity set to 0
    inventory_space = 0

    #print available items by printing dictionary keys
    print("You are going home to Philly for the holidays! Time to pack your carry-on bag:")
    for key in items :
        print(key)
    print("\nYou can pick 3 items: ")
    #Pick three items
    while inventory_space != 3 :
        #Choice & format choice
        choice = input("Choose: ")
        choice = choice.title()
        #Search to see if choice exists
        if choice in items :
            #Pop method used to return specified key
            #removes the key-value pair to avoid dupe choices
            item = items.pop(choice, 'Not a valid choice')
            #Append to backpack list
            backpack.append(choice)
            #Inventory space accumulator
            inventory_space += 1
            #Message to user confirming item has been added and print
            #that specific keys value
            print("Good choice! {}".format(item['description']))

        #Invalid input or item has been chosen already
        else :
            print("This item is not available")

    #print all selected items taken from items dictionary
    #in the backpack list
    print("\nItems in your inventory: ")
    print("------------------------")
    for items in backpack :
        print(items)
    print()
    #Return adventurers items
    return backpack
##################################################################################################################
#Simple function to ask user if they would like to play again by formatting                                      
#user input and calling 'main()' function.                                                                       
##################################################################################################################
def play_again():
    while True:
            again = input("Would you like to play this adventure again? [Y/N]")
            if again not in ('Y','N','y','n') :
                print("Not a valid input.")
            elif again == 'N' :
                print("Exiting...\n")
                break
            elif again == 'n':
                print("Exiting...\n")
                break
            elif again == 'Y' :
                print("\n")
                main()
            elif again == 'y' :
                print("\n")
                main()
    
##################################################################################################################    
#Simple function passing no arguements but rather the appropriate outcome message                                
##################################################################################################################
def survived() :
    print("You survived!")
##################################################################################################################
#Simple function passing a single arguement 'name' (to be formatted)                                             
#with the appropriate outcome message.                                                                           
##################################################################################################################
def perished(name) :
    name = name.title()
    print("{} you died...".format(name))

##################################################################################################################
def main() :

   
    #Call inventory function
    myitems = inventory()
    

    #Ask the Adventurer their name from keyboard input and store it to the name variable.
    name = input("What is your name? ")

    #Title
    print()
    print("Welcome to Choose Your Own Adventure!")
    print()
    print("Hello", name,"! You are on your way home to Philadelphia just in time for the holidays! You are coming from the Carribean islands where you decided to study abroad. All is going well for the first half hour of your plane ride until suddenly you begin to experience turbulance.  The plane begins to rapidly descend until... \n"
          "CRASH!! \n"
          "You wake up extremely disoriented but alive.  It seems you are on an island and your plane has crashed.")

        
    print("You get your bearings and decide on next steps.")


    
    print()
    #The first choice in the adventure. The 'choice' variable is used throughout this story in the series
    #of if-else and nested if-else statements. The choice variable stores the user-input as an integer holding the value of 1 or 2. 
    choice = int(input("Choose: \n [1] Look for surviors. \n [2] Try to find supplies to help you survive. \n"))

    #Path 1 : Choice 1
    if choice == 1 :
        print("Okay,", name, "you have decided to look for more surviors.  After about a half mile of walking, you hear a voice! \n"
              "You see someone in the distance! They are trying to get your attention. \n"
              "As you approach, you see that they have sustained a significant injury... \n")
        print()
        choice = int(input("Choose: \n [1] You decide to try and help treat their wounds on your own. \n [2] You decide to go look for help, assuring the person you will be back for them. \n"))
        
        #Path 1 : Choice 2 
        if choice == 1 :
            print(name, "It looks to just be a dislocated shoulder. You're not sure how to help but you have to try!\n"
                  "You close your eyes and wince as you try to pop the strangers arm back in place. They let out a scream followed by a sigh of relief! \n"
                  "You did it! They feel better almost immeadiately.  You decide to team up but what to do next? ")
            print()
            outcome = int(input("Choose: \n [1] Look for food. \n [2] Try finding shelter. \n"))
            
            #Path 1 : Choice 3 : Story Outcome 1
            if outcome == 1 :
                print("You go to look for food.  In no time you stumble across a bush full of berries. \n"
                      "Your new partner tells you the berries are safe and they have had them before.\n"
                      "You take a handful and eat them eagerly.  You hear your partners voice...\n"
                      "This isn't how I remember them tasting...")
                
                #Outcome function call
                perished(name)
                #Restart program function
                play_again()

            #Path 1 : Choice 3 : Story Outcome 2
            elif choice == 2 :
                print("You find a great place to set up camp and use materials around you to make a shelter.\n"
                      "You are safe through the night.  You wake in the morning to the sound of a helicopter! \n"
                      "Rescue has arrived!")
                #Outcome function call                
                survived()
                #Restart program function
                play_again()
                
        #Path 1 : Choice 2
        elif choice ==2 :
            print("You decide to go look for help.  It seems that you have been walking for hours deeper and deeper into the wilderness and away from the beach. \n"
                  "It is getting dark, you hear creatures stirring. You decide to...")
            print()
            outcome = int(input("Choose: \n [1] Stay put for the night. \n [2] Try to find your way out of the woods. \n"))
            
            #Path 1 : Choice 3 : Story Outcome 1
            if outcome == 1 :
                print("You decide to stay put for the night and reevaluate in the light of day. \n"
                      "But when the sun rises in the morning you're waken instead to the sound of a helicopter. \n"
                      "Rescue has arrived!")
                #Outcome function call
                survived()
                #Restart program function
                play_again()
                
            #Path 1 : Choice 3 : Story Outcome 2    
            elif choice == 2 :
                print("You decided to venture deeper into the woods looking for an out. \n"
                      "the animal sounds are getting louder and seemingly more aggressive. You can't see, but all at once you feel teeth sink into you...")
                #Outcome function call
                perished(name)
                #Restart program function
                play_again()
            
    #Path 2 : Choice 1
    elif choice == 2 :
        print("You venture out to look for supplies. \n"
              "You stumble upon your carry-on bag and decide you will look for a place to set up shelter.")
        if 'Book' in myitems :
            print("Maybe you can use the pages of your book to start a fire!")
        if 'First Aid' in myitems :
            print("Use your first aid kit to take care of any wounds you have sustained.")
        if 'Warm Sweatshirt' in myitems:
            print ("Put on your sweatshirt to stay warm.")
        if 'Phone Charger' in myitems:
            print ("Your phone charger won't be much help here!")
        if 'Snack' in myitems:
            print ("That snack you packed will help sustain you if help doesn't come soon!")
        print('But where is the best place to set up shelter?')
            
        print()
        choice = int(input("Choose: \n [1] Walk along the shore for a spot. \n [2] Venture into the woodsy area. \n"))
        
        #Path 2 : Choice 2 
        if choice == 1 :
            print("You decide to look along the shore line, you've always loved an ocean view. \n"
                  "As you walk, you discover a rickety canoe and off in the distance is another island! \n"
                  "Is that what you think it is? \n"
                  "Lights!! Coming from the island!\n"
                  " It can't be more than a few hundred yards away...")
                  
                  
            choice = int(input("Choose: \n [1] Take the boat and try to reach the other island. \n [2] Stay put. \n"))
            
            #Path 2 : Choice 3 : Story Outcome 1
            if choice == 1:
                print ("You have decided to take the risk.  \n"
                       "You take the boat out just as sun begins to set, but the lights from the island guide you. \n"
                       "The currents, however, have other plans. \n"
                       "You are wisked further and further from your destination.  Your boat begins to fill with water.")
              
                perished(name)
                #Restart program function
                play_again()
                
            #Path 2 : Choice 3 : Story Outcome 2    
            elif choice == 2 :
                print("You decide to instead use the boat as your shelter tonight. \n"
                      "Thankfully so, because a storm comes in with the night.  \n"
                      "The boat provides ample protection from the storm.  \n"
                      "In the morning, you wake to find helicopters ahead.  Rescue is here. ")
                #Outcome function call
                survived()
                #Restart program function
                play_again()
                
        #Path 2 : Choice 2
        elif choice ==n2 :
            
            print("You opt for the woods instead of the shore line. \n"
                  "In there, you find a bush full of fruit but you are unsure what kind. \n"
                  "There's a small animal to your right however, there's one you feel as though you could easily catch and eat."
                  "You decide that on tonights menu is ...")
            print()
            choice = int(input("Choose: \n [1] Unkown fruit. \n [2] Meat. \n"))
                     
            #Path 2 : Choice 3 : Story Outcome 1
            if choice == 1 :
                print("Fruit!. \n"
                      "Your mouth waters at the first bite and... \n"
                      "It seems they are just black berries! You feel instantly reguvinated and with a full stomach you watch as a helicopter appears overhead. \n"
                      "Help has arrived. ")
                #Outcome function call
                survived()
                #Restart program function
                play_again()
                
            #Path 2 : Choice 3 : Story Outcome 2
            elif choice == 2 :
                print("Meat! you make a mad dash for the animal but ... \n"
                      "You slip! you hit your head as you hit the ground. The world around you fades to black.")

                perished(name)
                play_again()

##################################################################################################################        
#Program starts here!                                                                                            
##################################################################################################################
main()
    
