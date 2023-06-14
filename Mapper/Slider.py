class Slider:
    def __init__(self, x, y, r, t, num, game):
        self.game = game
        self.x = x
        self.y = y
        self.r = r
        self.t = t
        self.miss = False
        self.timer = 10
        self.num = num
        
        self.x1 = self.r * cos(radians(self.t)) + self.x
        self.y1 = self.r * sin(radians(self.t)) + self.y
        self.x2 = self.r * cos(radians(self.t))
        self.y2 = self.r * sin(radians(self.t)) 
        self.xv = 0
        self.yv = 0

        self.a = 0
        self.xx = self.x + self.r
        self.yy = self.y + self.r
        
    def delete(self):
        self.game.objects.remove(self)
        
    def on_draw(self):
        noStroke()
        
        
        if self.miss:
            fill(255, 20, 50)
            textSize(50)
            text("x", self.x - 15, self.y + 15)
            self.game.hpdrain = 0.75
        else:
            
            
            
        
            fill(100, 100, 100)
            circle(self.x1, self.y1, 115)
            
            
            
        
            stroke(100, 100, 100)
            strokeWeight(115)
            line(self.x, self.y, self.x1, self.y1)
            noStroke()
            
            stroke(30, 30, 30)
            strokeWeight(102.5)
            line(self.x, self.y, self.x1, self.y1)
            noStroke()
            
        
        
       
            
            fill(30, 30, 30)
            circle(self.x1, self.y1, 101)
            
            
        
            img = loadImage("Note.png")
            image(img, self.x, self.y, 130, 130)
            
            
           
        
            fill(255, 255, 255)
            textSize(50)
            text(self.num, self.x, self.y - 7.5)
            
    def on_update(self):
        pass
    
