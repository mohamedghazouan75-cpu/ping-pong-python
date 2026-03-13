from paddles import Paddle
class Scorbord(Paddle):
    def __init__(self, position):
        super().__init__(position)
        self.hideturtle()
        self.color('white')
        self.score1 =0
        self.score2 =0
        self.show_score()
        


    def show_score(self):
       self.write(f' Player(A):{self.score2}          Player(B):{self.score1} ',align = 'center',font = ('Courier',20,'normal'))
    
    def add_score1(self):
        self.score1 += 1
        self.clear()
        self.show_score()
    def add_score2(self):
        self.score2 += 1
        self.clear()
        self.show_score()


