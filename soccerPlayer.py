# This program uses the markov process
# to simulate the outcome of each person trying out for soccer
from SimulateNonePlayers import *
# This player class creates a simple Player
#################
#               #
# Each placer ###
class Player:
    def __init__(self, position='N'):
        self.position = position
        self.stats ={ "skill": 0,
                      "speed": 0,
                      "strength": 0
                      }
    def Position(self):
        return self.position
    def Stats(self):
        return(self.stats)
    def SetSkill(self, value):
        self.stats["skill"] += value
    def SetSpeed(self, value):
        self.stats["speed"] += value
    def SetStrength(self, value):
        self.stats["strength"] += value
    def SetPos(self, value):
        self.position = value

trials = 1000000
p = list(range(trials))
for i in range(trials):
    p[i] = Player()
    
            
a =[]
        
for i in range(trials):
    test = SimulateNonePlayers(p[i],5,25,30)
    test.promote()
    a.append(p[i].Position())

j =0
n =0
for x in a:
    if(x == "JV"):
        j +=1
    else:
        n +=1

print("the ratio of JV to Not on the team is [{}:{}] for {} trials".format(j,n,trials))
    

