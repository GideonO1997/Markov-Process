import random
class SimulateNonePlayers:
    def __init__(self, player, speedDur = None, skillDur = None, strengthDur = None):
        self.flag = False
        self.player = player
        self.spD = speedDur
        self.skD = skillDur
        self.stD = strengthDur
        #Checking to make sure none of the vairables are none
        v = [self.skD, self.spD, self.stD]
        vName =["Skill Duration", "Speed Duration", "Strength Duration"]
        if (self.player.Position() != "N"):
            print("You're already on the {} team, pratice with them!".format(self.player.Position()))
            return
        if (sum(v) <= 60):
            pass
        else:
            print("Error: Sum of duration times must not be grater than 60")
            return
        try:
            self.__speedTrain()
            self.__skillTrain()
            self.__strengthTrain()
        except TypeError:
            self.flag = True
            print("Error: {} can't be of type None".format(vName[v.index(None)]))
            print("Class argunents: (playerObject, speedDur = Int, skillDur = Int, strengthDur = Int)")
            return            
        

    def __speedTrain(self):
        if (not self.flag):
            cata = random.randint(0, 3)
            for times in range(self.spD):
                if (cata == 1):
                    self.player.SetSpeed(random.uniform(0, 7))
                elif(cata == 2):
                    self.player.SetSpeed(random.uniform(0, 5.5))
                else:
                    self.player.SetSpeed(1.5)
               
    def __skillTrain(self):
        if (not self.flag):
            cata = random.randint(0, 3)
            for times in range(self.skD):
                if (cata == 1):
                    self.player.SetSkill(random.uniform(0, 7.7))
                elif(cata == 2):
                    self.player.SetSkill(random.uniform(0, 5.5))
                else:
                    self.player.SetSkill(1.5)

    def __strengthTrain(self):
        if (not self.flag):
            cata = random.randint(0, 3)
            for times in range(self.stD):
                if (cata == 1):
                    self.player.SetStrength(random.uniform(0, 7.9))
                elif(cata == 2):
                    self.player.SetStrength(random.uniform(0, 7.5))
                else:
                    self.player.SetStrength(1.5)

    def promote(self):
        if (self.flag == False):
            sp = self.player.Stats().get("speed")
            sk = self.player.Stats().get("skill")
            st = self.player.Stats().get("strength")
            avg = (sp+sk+st)//3
            if( (sp >= 70 and sp <= 90) and (sk >= 70 and sk <= 90) and (st >= 70 and st <= 90) ):
                self.player.SetPos("JV")
            elif ( (sp >= 90 ) and (sk >= 90 ) and (st >= 90 ) ):
                self.player.SetPos("V")
            elif ( avg >= 50):
                self.player.SetPos("JV")
            elif ( avg >= 90):
                self.player.SetPos("V")
##            else:
##                print("try again next time")
