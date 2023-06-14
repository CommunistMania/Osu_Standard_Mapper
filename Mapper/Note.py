class Note:
    def __init__(self, x, y, number, game):
        self.game = game
        self.miss = False
        self.missframe = 0
        self.x = x
        self.y = y
        self.number = number
        
        self.a = 0
       
        
    def delete(self):
        self.game.objects.remove(self)
        
    def on_draw(self):
        if self.miss:
            fill(255, 20, 50)
            textSize(50)
            text("x", self.x - 15, self.y + 15)
        else:
            img = loadImage("Note.png")
            image(img, self.x, self.y, 130, 130)
        
        
            fill(255, 255, 255)
            textSize(50)
            text(self.number, self.x, self.y - 7.5)
        
    def on_update(self):
        pass
        
