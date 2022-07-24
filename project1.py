print("  ______")
print(" /|_||_\`.__")
print("(   _    _ _\ ")
print("=`-(_)--(_)-' ")
print("welcome to the game!")
while 0 < 1 :
    a = input("enter your order(start,stop,help,quit): ").lower()
    if a == "start":
        print("\t\t       ______")
        print("\t\t      /|_||_\`.__")
        print("\t\t     (   _    _ _\ ")
        print("\t\t     =`-(_)--(_)-' ")
        print("car moved")
    elif a == "stop": print("car stopped")
    elif a == "help":
        print("start = moving car \n stop = stopping car\n quit = exit the game ")
    elif a == "quit":
        print("goodbye")
        break
