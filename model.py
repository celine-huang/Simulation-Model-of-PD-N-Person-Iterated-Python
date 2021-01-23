import random as rd
import matplotlib.pyplot as plt

class person:
    def __init__(self, strategy):
        self.isAlive = True
        self.strategy = strategy
        self.action = ""
        self.payoff = 0
        self.totalpayoff = 0
        self.hatchChance = 0
        self.dieChance = 0
        self.isPartnered = False
        self.partner = self
        self.partnerId = -1
        self.partnerHistory = []

def calcPopulation():
    trusterPopulation.append(len(truster) / len(all) * 100)
    exploitativeEgoistPopulation.append(len(exploitativeEgoist) / len(all) * 100)
    titForTatPopulation.append(len(titForTat) / len(all) * 100)
    unforgivingPopulation.append(len(unforgiving) / len(all) * 100)
    trueBelieverPopulation.append(len(trueBeliever) / len(all) * 100)
    winStayLoseShiftPopulation.append(len(winStayLoseShift) / len(all) * 100)
    discriminatingAltruistPopulation.append(len(discriminatingAltruist) / len(all) * 100)
    opportunistPopulation.append(len(opportunist) / len(all) * 100)
    reclusePopulation.append(len(recluse) / len(all) * 100)
    randomPopulation.append(len(random) / len(all) * 100)

def getPayoff(person, partner):
    if partner.action == "cooperating":
        if person.action == "cooperating":
            person.payoff = C
        if person.action == "cheating":
            person.payoff = R
    if partner.action == "cheating":
        if person.action == "cooperating":
            person.payoff = -R
        if person.action == "cheating":
            person.payoff = -F*P
        if person.action == "appeasementWithCheating":
            person.payoff = -A*R
    if partner.action == "appeasementWithCooperating" or person.action == "appeasementWithCooperating":
        person.payoff = A*C
    if partner.action == "appeasementWithCheating":
        person.payoff = A*R
    if partner.action == "noReaction" or person.action == "noReaction":
        person.payoff = 0

#initial variable data
initialPopulation = 10
round = 10000
C = 2.5 #reward gained from cooperation
R = 5.0 #amount received/lost from exploiting/being exploited
P = 7.5 #penalty from being punished
A = 0.5 #fraction offered to appease another player
F = 5 #multiplier associated with a punishment escalating into a feud
#limitations: C<R<P, A<1<F

all = []
truster = []
exploitativeEgoist = []
titForTat = []
unforgiving = []
trueBeliever = []
winStayLoseShift = []
discriminatingAltruist = []
opportunist = []
recluse = []
random = []

for i in range(initialPopulation):
    truster.append(person("truster"))
    all.append(truster[i])
for i in range(initialPopulation):
    exploitativeEgoist.append(person("exploitativeEgoist"))
    all.append(exploitativeEgoist[i])
for i in range(initialPopulation):
    titForTat.append(person("titForTat"))
    all.append(titForTat[i])
for i in range(initialPopulation):
    unforgiving.append(person("unforgiving"))
    all.append(unforgiving[i])
for i in range(initialPopulation):
    trueBeliever.append(person("trueBeliever"))
    all.append(trueBeliever[i])
for i in range(initialPopulation):
    winStayLoseShift.append(person("winStayLoseShift"))
    all.append(winStayLoseShift[i])    
for i in range(initialPopulation):
    discriminatingAltruist.append(person("discriminatingAltruist"))
    all.append(discriminatingAltruist[i])
for i in range(initialPopulation):
    opportunist.append(person("opportunist"))
    all.append(opportunist[i])
for i in range(initialPopulation):
    recluse.append(person("recluse"))
    all.append(recluse[i])
for i in range(initialPopulation):
    random.append(person("random"))
    all.append(random[i])
for i in range(len(all)):
    for j in range(len(all)):
        all[i].partnerHistory.append("false")

trusterPopulation = []
exploitativeEgoistPopulation = []
titForTatPopulation = []
unforgivingPopulation = []
trueBelieverPopulation = []
winStayLoseShiftPopulation = []
discriminatingAltruistPopulation = []
opportunistPopulation = []
reclusePopulation = []
randomPopulation = []

calcPopulation()
pair = all.copy()

for i in range(round):
    #partner      
    rd.shuffle(pair)
    if len(pair) % 2 == 1:
        for j in range(len(pair)-1):
            pair[j].isPartnered = True
    if len(pair) % 2 == 0:
        for j in range(len(pair)):
            pair[j].isPartnered = True
    for j in range(len(pair)):
        if pair[j].isPartnered == True:
            if j % 2 == 0:
                pair[j].partner = pair[j+1]
                pair[j].partnerId = all.index(pair[j+1])
            if j % 2 == 1:
                pair[j].partner = pair[j-1]
                pair[j].partnerId = all.index(pair[j-1])
    #action
    for j in range(len(pair)):
        if pair[j].strategy == "truster":
            pair[j].action = "cooperating"
            getPayoff(pair[j], pair[j].partner)
        if pair[j].strategy == "exploitativeEgoist":
            pair[j].action = "cheating"
            getPayoff(pair[j], pair[j].partner)
        if pair[j].strategy == "titForTat":
            if pair[j].partnerHistory[pair[j].partnerId] == "false":
                pair[j].action = "cooperating"
            else:
                pair[j].action = pair[j].partnerHistory[pair[j].partnerId]
            getPayoff(pair[j], pair[j].partner)
            pair[j].partnerHistory[pair[j].partnerId] = pair[j].partner.action
        if pair[j].strategy == "unforgiving":
            if pair[j].partnerHistory[pair[j].partnerId] == "false":
                pair[j].action = "cooperating"
            else:
                pair[j].action = pair[j].partnerHistory[pair[j].partnerId]
            getPayoff(pair[j], pair[j].partner)
            if pair[j].partner.action == "cheating":
                pair[j].partnerHistory[pair[j].partnerId] = pair[j].partner.action
        if pair[j].strategy == "trueBeliever":
            if pair[j].partnerHistory[pair[j].partnerId] == "false":
                pair[j].action = "cooperating"
            else:
                pair[j].action = pair[j].partnerHistory[pair[j].partnerId]
            getPayoff(pair[j], pair[j].partner)
            if pair[j].partner.action == "cheating":
                pair[j].partnerHistory[pair[j].partnerId] = pair[j].partner.action
        if pair[j].strategy == "winStayLoseShift":
            if pair[j].partnerHistory[pair[j].partnerId] == "false":
                pair[j].action = "cooperating"
            elif pair[j].partnerHistory[pair[j].partnerId][0] >= 0:
                pair[j].action = pair[j].partnerHistory[pair[j].partnerId][1]
            else:
                if pair[j].partnerHistory[pair[j].partnerId][1] == "cooperating":
                    pair[j].action = "cheating"
                elif pair[j].partnerHistory[pair[j].partnerId][1] == "cheating":
                    pair[j].action = "cooperating"
            getPayoff(pair[j], pair[j].partner)
            pair[j].partnerHistory.insert(pair[j].partnerId, [pair[j].payoff, pair[j].action])
        if pair[j].strategy == "discriminatingAltruist":
            if pair[j].partnerHistory[pair[j].partnerId] == "false":
                pair[j].action = "cooperating"
            elif pair[j].partnerHistory[pair[j].partnerId] == "cheating":
                pair[j].action = "noReaction"
            getPayoff(pair[j], pair[j].partner)    
            if pair[j].partner.action == "cheating":
                pair[j].partnerHistory[pair[j].partnerId] = pair[j].partner.action
        if pair[j].strategy == "opportunist":
            if pair[j].partner.action == "cooperating":
                pair[j].action = "cheating"
            if pair[j].partner.action == "cheating":
                pair[j].action = "appeasementWithCheating"
            if pair[j].partner.strategy == "trueBeliever":
                pair[j].action = "appeasementWithCooperating"
            if pair[j].partner.action == "noReaction" or pair[j].partner.strategy == "opportunist":
                pair[j].action = "noReaction"
            getPayoff(pair[j], pair[j].partner)    
        if pair[j].strategy == "recluse":
            pair[j].action = "noReaction"
            pair[j].payoff = 0
        if pair[j].strategy == "random":
            randomNum = rd.randint(1, 99)
            if 1 <= randomNum <= 33:
                pair[j].action = "cooperating"
            elif 34 <= randomNum <= 66:
                pair[j].action = "noReaction"
            else:
                pair[j].action = "cheating"
            getPayoff(pair[j], pair[j].partner)
    #calculate payoff
    for j in range(len(pair)):
        pair[j].totalpayoff += pair[j].payoff
        if pair[j].totalpayoff >= 100:
            pair[j].hatchChance = 100
            pair[j].totalpayoff -= 100
        if pair[j].totalpayoff <= -100:
            pair[j].dieChance = 100
            pair[j].totalpayoff += 100
    #calculate population
    calcPopulation()
    #reset
    for j in range(len(pair)):
        pair[j].isPartnered = False
    #hatch
    originalNum = len(pair)
    for j in range(originalNum):
        if pair[j].hatchChance == 100:
            if pair[j].strategy == "truster":
                truster.append(person("truster"))
                all.append(truster[len(truster)-1])
            if pair[j].strategy == "exploitativeEgoist":
                exploitativeEgoist.append(person("exploitativeEgoist"))
                all.append(exploitativeEgoist[len(exploitativeEgoist)-1])
            if pair[j].strategy == "titForTat":
                titForTat.append(person("titForTat"))
                all.append(titForTat[len(titForTat)-1])
            if pair[j].strategy == "unforgiving":
                unforgiving.append(person("unforgiving"))
                all.append(unforgiving[len(unforgiving)-1])
            if pair[j].strategy == "trueBeliever":
                trueBeliever.append(person("trueBeliever"))
                all.append(trueBeliever[len(trueBeliever)-1])
            if pair[j].strategy == "winStayLoseShift":
                winStayLoseShift.append(person("winStayLoseShift"))
                all.append(winStayLoseShift[len(winStayLoseShift)-1])    
            if pair[j].strategy == "discriminatingAltruist":
                discriminatingAltruist.append(person("discriminatingAltruist"))
                all.append(discriminatingAltruist[len(discriminatingAltruist)-1])
            if pair[j].strategy == "opportunist":
                opportunist.append(person("opportunist"))
                all.append(opportunist[len(opportunist)-1])
            if pair[j].strategy == "recluse":
                recluse.append(person("recluse"))
                all.append(recluse[len(recluse)-1])
            if pair[j].strategy == "random":
                random.append(person("random"))
                all.append(random[len(random)-1])
            for k in range(originalNum):
                all[k].partnerHistory.append("false")
        pair[j].hatchChance = 0
    newNum = len(pair)
    for j in range(newNum):
        for k in range(newNum - originalNum):
            all[k].partnerHistory.append("false")
    #die
    for j in range(len(pair)):
        if pair[j].dieChance == 100:
            pair[j].isAlive = False
            pair.append(pair[j])
    j = len(pair) - 1
    while j >= 0:
        if pair[j].isAlive == False:
            pair.remove(pair[j])
        j -= 1 

fig = plt.figure()
ax = plt.axes()
plt.xlim(0, round)
plt.ylim(0, 100)
plt.xlabel('rounds')
plt.ylabel('Percent of Population(%)')
x = []
for i in range(round+1):
    x.append(i)
l_truster, = plt.plot(x, trusterPopulation)
l_exploitativeEgoist, = plt.plot(x, exploitativeEgoistPopulation)
l_titForTat, = plt.plot(x, titForTatPopulation)
l_unforgiving, = plt.plot(x, unforgivingPopulation)
l_trueBeliever, = plt.plot(x, trueBelieverPopulation)
l_winStayLoseShift, = plt.plot(x, winStayLoseShiftPopulation)
l_discriminatingAltruist, = plt.plot(x, discriminatingAltruistPopulation)
l_opportunist, = plt.plot(x, opportunistPopulation)
l_recluse, = plt.plot(x, reclusePopulation)
l_random, = plt.plot(x, randomPopulation)
#plt.legend(handles=[l_truster, l_exploitativeEgoist, l_titForTat, l_unforgiving, l_trueBeliever, l_winStayLoseShift, l_discriminatingAltruist, l_opportunist, l_recluse, l_random], labels=['truster', 'exploitative egoist', 'tit for tat', 'unforgiving', 'true believer', 'win stay lose shift', 'discriminating altruist', 'opportunist', 'recluse', 'random'])
plt.savefig("10-10000-2.5-5.0-7.5-0.5-5.png")
