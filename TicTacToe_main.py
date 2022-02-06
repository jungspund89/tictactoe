class Player:
    def __init__(self, ID, turn, number):
        self.ID = ID
        self.turn = turn
        self.number = number


class Grid:
    def __init__(self):
        self.dict = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}
        self.winningCombi = ([1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7])

    def setField(self, field, playerID):
        self.dict.update({field: playerID})

    def isFull(self):
        if " " in self.dict.values():
            return False
        else:
            return True

    def isWinner(self, playerobj):
        # alle Felder, die der Spieler besetzt hat finden und in owned-Liste speichern
        owned = []
        for field, ID in self.dict.items():
            if ID == playerobj.ID:
                owned.append(field)
        # jede mögliche Gewinnerkombination mit owned-Liste abgleichen
        for combi in self.winningCombi:
            result =  all(elem in owned for elem in combi)
            if result: return True


# program starts here
def main():
    player1 = Player("X", True, 1)
    player2 = Player("O", False, 2)
    game = Grid()

    # Begrüßung
    print("\n")
    print("TicTacToe START")
    print("Spieler 1 setzt X")
    print("Spieler 2 setzt O")

    # Anzeige Konsole: Einmalige Anzeige, welches Feld welches ist
    for y in range(0,3):
        print(" " + str(1+3*y) + " | "
                  + str(2+3*y) + " | "
                  + str(3+3*y) + " ")
        print(11*"-") if y<2 else print(11*" ")

    # TEST
    # game.setField(7,"O")
    # game.setField(5,"O")
    # game.setField(9,"O")

    while True:
        print(40*"*")

        # Spieler gewonnen?
        if game.isWinner(player1):
            print("GLÜCKWUNSCH")
            print("Spieler " + str(player1.number) + " hat gewonnen!")
            break
        elif game.isWinner(player2):
            print("GLÜCKWUNSCH")
            print("Spieler " + str(player2.number) + " hat gewonnen!")
            break

        # Grid voll?
        if game.isFull():
            print("Spielfeld voll - Unentschieden!!!")
            break

        # Anzeige Konsole: Wer ist an der Reihe, welche Felder verfügbar
        if player1.turn:
            print("Spieler " + str(player1.number) + " mit " + player1.ID + " ist an der Reihe")
        else:
            print("Spieler " + str(player2.number) + " mit " + player2.ID + " ist an der Reihe")

        print("Freie Felder:")
        free = []
        for field, ID in game.dict.items():
            if ID == " ":
                free.append(field)
        print(free)

        # Spieler setzt
        while True:
            occupyField = input()
            try:
                occupyField = int(occupyField)
            except ValueError:
                print("Bitte Zahl zwischen 1 und 9 eingeben")
            else:
                if occupyField in free:
                    break
                else:
                    print("Feld nicht verfügbar!")

        # Feld besetzen und Spielerreihenfolge wechseln
        if player1.turn:
            game.setField(occupyField, player1.ID)
            player1.turn = False
            player2.turn = True
        else:
            game.setField(occupyField, player2.ID)
            player1.turn = True
            player2.turn = False

        # Anzeige Konsole: Aktualisiertes Grid
        for x in range(0,3):
            print(" " + game.dict.get(1+(x*3)) + " | "
                      + game.dict.get(2+(x*3)) + " | "
                      + game.dict.get(3+(x*3)) + " ")
            print(11*"-") if x<2 else print(11*" ")



if __name__ == "__main__":
    main()
