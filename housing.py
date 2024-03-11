import csv
from helperfunctions import *

if __name__ == "__main__":
    players = []

    #get predictions
    with open("predictions.csv", mode = "r") as file:
        csvFile = csv.reader(file)
        next(csvFile)
        for line in csvFile:
            newplayer = player(line[2])
            newplayer.saveguesses(line)
            newplayer.getscore()
            players.append(newplayer)

    players.sort(key = lambda x: x.score, reverse = True)
    results = [[player.name, player.score] for player in players]

    file = open('results.txt','w')
    file.write("Here are the results for the housing game\n")
    for i in range(len(results)):
        place = results[i]
        file.write("Place: " + str(i+1) + ", Player: " + place[0] + ", Score: " + str(place[1]) + "\n")
    file.close()