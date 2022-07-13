def main():
    print("running...")
    start_game()
    


def start_game():
    while True:
        print("you want to load a game or start a new one?")
        print("type: [new] or [load]")
        income = input()
        if income == "new":
            choose_name()
            break
        elif income == "load":
            print("NOT implemnted yet")
            #TODO load game
        else:
            print("wrong input")

    

    
 

def choose_name():
    print("To beginn our adventure first")
    print("choose your name")
    new_name = input()
    if new_name != None:
        print("your name is",new_name)



if __name__ == '__main__':
    main()
 