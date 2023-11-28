agent.teleport_to_player()
agent.move(FORWARD, 3)

# mai jos este functia care salveaza codul care construieste un patrat
def fa_un_patrat():
    for j in range(4): # aici trebuie sa fie nr. 4 pentru ca sunt 4 pereti
        for i in range(6): # aici in loc de 6 alege cat de larga e casa ta
            agent.place(LEFT)
            agent.move(FORWARD, 1)
        agent.turn(TurnDirection.LEFT)
        agent.move(FORWARD, 1)
        agent.place(LEFT)



for i in range(5): # aici in loc de 5 poti pune inaltimea dorita pentru casa ta
    fa_un_patrat()
    agent.move(UP, 1)
