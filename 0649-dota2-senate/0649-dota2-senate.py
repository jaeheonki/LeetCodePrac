class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = []
        dire = []
        n = len(senate)

        for i in range(n) : 
            if senate[i] == 'R' :
                radiant.append(i)
            elif senate[i] == 'D' :
                dire.append(i)
            else : 
                print("Unvalid Literal")
                return
            
        while radiant and dire :
            r = radiant.pop(0)
            d = dire.pop(0)

            if r > d :
                radiant.append(r + n)
            else :
                dire.append(d + n)

        return 'Radiant' if radiant else 'Dire'