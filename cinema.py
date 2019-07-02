films = {
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,2],
    "Ghost Busters":[12,5]
    }

while True:
    choice = input("What film would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())
        
        #check the age
        if age >= films[choice][0]:
            
            #check enough seats
            if films[choice][1] > 0:
                
                films[choice][1] = films[choice][1] - 1
                print("Enjoy the film!")

            else:
                print("Sorry we are sold out!")

        else:
            print("You are too young to see this film")
        
    else:
        print("We don't have that film...")
    

 
