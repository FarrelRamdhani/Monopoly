#Check Prison
        if self.prisonStatus == True:
            if self.jailPreference == 1:
                if self.jailCard == 0:
                    self.DiceRandom()
                    if self.dice1 == self.dice2:
                        self.prisonStatus = False
                        self.runAgainStatus = False
                        self.position = self.dice1 + self.dice2

                        self.jailTime = 0
                    elif self.jailTime == 2:
                        
                    else:
                        self.jailTime += 1

            elif self.jailPreference == 2:
                if self.jailCard == 0:
                    self.money -= 50
                    self.prisonStatus == False
                else:
                    self.jailCard -= 1
                    self.prisonStatus == False
            elif self.jailPreference == 3


class Monopoly:
    def __init__(self, jailPreference, totalPlayer):
        self.position = 1
        self.money = 2000
        self.jailCard = 0

        self.prisonStatus = False
        self.runAgainStatus = False

        self.jailPreference = jailPreference
        self.jailTime = 0

        self.totalPlayer = totalPlayer

    def DiceRandom(self):
        self.dice1 = random.randrange(1, 7)
        self.dice2 = random.randrange(1, 7)

    def Run(self):
         self.DiceRandom()
          self.position = self.dice1 + self.dice2

           if self.position >= 41:
                self.position = self.position - 40
                self.money += 200

            #Monopoly Map Rules
            #Prison
            if self.position == 31:
                self.position = 11
                self.prisonStatus = True

            #Comunity Chest
            elif self.position == 3 or self.position == 18 or self.position == 34:
                i = random.randrange(1, 17)
                if i == 1:
                    self.position = 1
                    self.money += 200
                elif i == 2:
                    self.money += 200
                elif i == 3 or i == 11 or i == 12:
                    self.money -= 50
                elif i == 4:
                    self.money += 50
                elif i == 5:
                    self.jailCard += 1
                elif i ==

            if self.position

    def getData(self):
        return(self.position, self.resultDice, self.lastResultDice)
