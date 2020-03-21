import Laws
import math


time = 1

class Charge:
    def __init__(self, postition, ch, mass, vel):
        self.position = postition
        self.ch = ch
        self.mass = mass
        self.vel = vel
        
    

def main():

    goodcharge = Charge([-1, -5], -40, 2, [0,0])

    badcharge = Charge([-1, 10], 50, 2, [0,0])


    for i in range(3):

        t = Laws.coulombLaw(goodcharge.ch, badcharge.ch, 1, dfun(goodcharge.position,badcharge.position))
        
        # print("The force is : ",t)

        if dir(goodcharge.position, badcharge.position) == "Undefined":
            if goodcharge.ch < 0 and badcharge.ch < 0 or goodcharge.ch > 0 and badcharge.ch > 0:
                d = -1 * abs(math.pi/2)
            else:
                d = abs(math.pi/2)
        else: 
            d = -1 * abs((math.atan(dir(goodcharge.position, badcharge.position))))

        

        a1 = t/goodcharge.mass
        a2 = t/badcharge.mass
        
 
        
        # print(badcharge.position)




        print("good charge vel: ", goodcharge.vel)
        # print("Bad charge velocit:", badcharge.vel)

        goodcharge.position[0] = goodcharge.position[0] + goodcharge.vel[0]
        goodcharge.position[1] = goodcharge.position[1] + goodcharge.vel[1]

        badcharge.position[0] = badcharge.position[0] + badcharge.vel[0]
        badcharge.position[1] = badcharge.position[1] + badcharge.vel[1]

        goodcharge.vel[0] = math.cos(d)*a1 + goodcharge.vel[0]
        goodcharge.vel[1] = math.sin(d)*a1 + goodcharge.vel[1]

        badcharge.vel[0] = (-1 * math.cos(d)*a2) + badcharge.vel[0]
        badcharge.vel[1] = (-1 * math.sin(d)*a2) + badcharge.vel[1]

        
        
    print("Final position 1", goodcharge.position)
    print("Final position 2", badcharge.position)



    


def dfun(pos1, pos2):

    return math.sqrt(((pos1[0] - pos2[0])**2) + (pos1[1] - pos2[1])**2)


def dir(pos1, pos2):

    try:
        val = (pos1[1] - pos2[1]) / (pos1[0] - pos2[0])
        return val
    except:
        return "Undefined"




if __name__ == "__main__":
    main()