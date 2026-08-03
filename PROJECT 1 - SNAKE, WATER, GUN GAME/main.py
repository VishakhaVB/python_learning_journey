# PROJECT 1: SNAKE, WATER, GUN GAME
#
# Build a simple Snake, Water, Gun game.
# Rules:
# 1. Snake drinks water -> Snake wins.
# 2. Water douses gun -> Water wins.
# 3. Gun kills snake -> Gun wins.
# 4. Same choices -> Draw.
#1 snake
#-1 water
#0 gun

computer=1

you =input("Enter your choice : " )
youdict ={ "s":1, "w":-1,"g":0 }
younum =youdict[you]
print(younum)


