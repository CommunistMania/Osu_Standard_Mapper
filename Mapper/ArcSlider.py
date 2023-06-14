class ArcSlider:
    def __init__(self, x, y, r, t, e, number, game):
        self.game = game
        self.miss = False
        self.missframe = 0
    
        self.x = x
        self.y = y
        self.r = r
        self.t = t
        self.e = e
        self.number = number
        
        self.a = 0
    
        self.y1 = self.y + self.r
        self.xv = self.x
        self.yv = self.y1
        
        
        
        
       
        
    def delete(self):
        self.game.objects.remove(self)
        
    def on_draw(self):
        noStroke()
        
        
        if self.miss:
            fill(255, 20, 50)
            textSize(50)
            text("x", self.xv - 15, self.yv + 15)
        else:
            noFill()
            stroke(100, 100, 100)
            strokeWeight(115)
            arc(self.x, self.y, 2*self.r, 2*self.r, radians(self.e), radians(self.t))
            noStroke()
            noFill()
            stroke(30, 30, 30)
            strokeWeight(102.5)
            arc(self.x, self.y, 2*self.r, 2*self.r, radians(self.e), radians(self.t))
            noStroke()
            nt = loadImage("Note.png")
            image(nt, self.r * cos(radians(self.t)) + self.x, self.r * sin(radians(self.t)) + self.y, 130, 130)
            fill(255, 255, 255)
            textSize(50)
            text(self.number, self.r * cos(radians(self.t)) + self.x, self.r * sin(radians(self.t)) + self.y - 7.5)
      
        
    def on_update(self):
        pass
