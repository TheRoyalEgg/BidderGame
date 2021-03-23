import random

class Game:
    def __init__(self,plnum,winreq,startmon):
        self.playerup = 0
        self.winreq = winreq
        self.plist = []
        self.lotslist = []
        self.plnum = plnum
        for i in range(plnum):
            self.plist.append(Player(i,startmon))
        total = 0
        while total < plnum * winreq:
            temp = random.randint(1,3)
            total += temp
            self.lotslist.append(temp)
           
    def gameround(self):
        self.plist.append(self.plist.pop(0))
        passes = 0
        highbid = -1
        highplayer = -1
        while True:
            for p in self.plist:
                bid = p.bid(self)
                if bid <= highbid or bid == 0:
                    print('passing passing beep boop')
                    passes +=1
                    if passes == self.plnum -1 and highplayer != -1:
                        self.plist.append(self.plist.pop(0))
                        return(highbid,highplayer,self.lotslist.pop(0))
                else:   
                    highbid = bid
                    highplayer = p
                    passes = 0
   
    def playgame(self):
        while True:
            highbid,highplayer,tokenamt = self.gameround()
            if highplayer.wonround(tokenamt,highbid,self.winreq):
                print(f'{highplayer} won. Good job!!!')
                return
           
                   
               
class Player:
    def __init__(self,p_id,startmon):
        self.p_id = p_id
        self.money = startmon
        self.tokens = 0
       
    def bid(self,game):
        print(f'You have {self.money} moneys and {self.tokens} tokens.')
        print(f'{game.lotslist} are the token lots, {game.lotslist[0]} is the next lot.')
        return int(input(f'Player{self.p_id}, what is your bid? 0 to pass'))

    def wonround(self,tokens,money,req):
        self.money -= money
        self.tokens += tokens
        return True if self.tokens >= req else False
   
      
       
def main():
    g = Game(int(input('Number of Players')),int(input('How Many Tokens to Win')),int(input('Starting Money')))
    g.playgame()
