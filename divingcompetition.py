import pickle
class Diver:
    nextDiverID = 1
    
    def __init__(self, newName, newScore):
        self.name = newName
        self.scores = newScore

        for i in range(len(newScore)):
            self.scores[i] = float(self.scores[i])

        print(*self.scores)
        print(self.name)
        self.id = Diver.nextDiverID
        Diver.nextDiverID = Diver.nextDiverID + 1
        
    def getName(self):
        return self.name
    
    def getScores(self):
        return self.scores
    
    def setName(self, newName):
        self.name = newName
        
    def averageScore(self):
        score = self.scores
        score.remove(max(score)) 
        score.remove(min(score))
        avg = sum(score) / len(score)
        return avg
    
    def printScores(self):
        string = "["
        for i in range (len(self.scores)):
            string = string + str(self.scores[i]) + ", "
        string += "]"
        return string
        
    def __str__(self):        
        #return " Name: {} Score: {} Average : {}". format(self.name, self.scores, self.getAverageScore())
        return (self.name + " " + str(self.id) + " "
                +" with scores " 
                + str(self.printScores()) +" and average score "
                    + str(self.averageScore()))
        
class Competition:
    def __init__(self, newNameOfComp):
        self.Divers = []
        self.nameOfComp = newNameOfComp
    
    def register(self, newDiver):
        self.Divers.append(newDiver)
        
    def highestAverageScoreSoFar(self):
        print ("a")
    
    def noOfDivers(self):
        return len(self.Divers)

class DivingCompetition:
    def __init__(self, name):
        self.name = name
        print(" ", self.name)

if __name__ == '__main__':
    competition = Competition
    diving_competition = DivingCompetition
    diver = Diver

    title = input("Enter competition title: ")

    loop = True
    while(loop):
        print(title)
        print("~" * len(title))

        a = ("1 Register diver", "2 Display all divers", "3 Display current leader",
             "4 Update information of diver", "5 Display all divers, sorted according to name or average score",
             "6 Save data to file",
             "7 Load data from file", "\n\n0 Quit")
        print(*a, sep="\n")
        choice = int(input("\nYour choice? "))
        if(choice == 0):
            loop = False
            print("Competition is cancelled due to lack of response.")
        elif(choice == 1):
            print("Adding driver")
            diverName = input("Insert driver's name: ")
            diverScore = []
            for i in range(0, 7):
                d = int(input("Insert driver's score: "))
                diverScore.append(d)
            print("Addition success...")
            diver(diverName, diverScore)
        elif(choice == 2):
            pass
        elif(choice == 3):
            pass
        elif(choice == 4):
            pass
        elif(choice == 5):
            pass
        elif(choice == 6):
            pass
        elif(choice == 7):
            pass
        else:
            exit(1)

