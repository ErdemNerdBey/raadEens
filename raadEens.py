import random


def main(rondeNummer):

    # Print het huidige ronde nummer
    print(f'\nRonde {rondeNummer+1}\n')

    # Maak een random getal
    randomGetal = random.randint(1,1000)

    for i in range(10):

        # Doe een gok
        gok = int(input(' Probeer het nummer te raden!!\n' ))
        
        # Checken of de gok hetzelfde is als de getal
        if gok == randomGetal:
            print('Je hebt geraden!!!')

            # Return true betekent dat je hebt gewonnen
            return True

        elif gok >= (randomGetal -50) and gok <= (randomGetal +50):
            if gok >= (randomGetal -20) and gok <= (randomGetal +20):
                print('je bent heel warm!')
            else: print('je bent warm')

        if gok == randomGetal:
            print()
        elif gok <= randomGetal:
            print('HOGER!!!')
        elif gok >= randomGetal:
            print('LAGER!!!')

    return False
    gokNummer += 1

if __name__ == "__main__":


    print('welkom biiiijjjj....\nGETALLEN RADERRRR.\n U miet een getal raden tussen 1 en 1000. \n U kunt 10 keer raden. als u het binnen 10 x goed heeft gaat u door naar de volgende ronde')
    print('u kunt maximaal 20 rondes spelen.\n als u het na 10x raden niet heeft geraden word u eruit gegoit.\n')

    # Variabel voor het aantal rondes gewonnen
    aantalRondes = 0

    # Eerst checken of het aantal rondes niet boven 20 is en dan de ronde starten
    while aantalRondes < 20 and main(aantalRondes):
        aantalRondes += 1
    
    print(f"Je hebt {aantalRondes} rondes gewonnen")
        