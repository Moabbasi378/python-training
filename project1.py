print("  ______")
print(" /|_||_\`.__")
print("(   _    _ _\ ")
print("=`-(_)--(_)-' ")
print("welcome to the game!")

while 0 < 1 :
    order = input("enter your order(start,stop,help,quit): ").lower()
    if order == "start":
        print("\t\t       ______")
        print("\t\t      /|_||_\`.__")
        print("\t\t     (   _    _ _\ ")
        print("\t\t     =`-(_)--(_)-' ")
        print("car moved")
    elif order == "stop": print("car stopped")
    elif order == "help":
        print("start = moving car \n stop = stopping car\n quit = exit the game ")
    elif order == "quit":
        print("goodbye")
        break
