


from __future__ import division, print_function
import arcade
import Note
import Slider
import SliderBF
import ArcSlider
import ArcSlider2
import os
WIDTH = 1920
HEIGHT = 1080 # height of screen in pixels

BACKGROUND_COLOR = color(30)  # (0black), 255(white)


class Window:    
    def __init__(self):
        self.x = 400
        self.y = 400
        self.num = 0
        self.beat = 0
    
        self.hold = False
        self.r = 100
        self.t = 90
        self.e = 0
        self.r1 = 100
        self.t1 = 0
        self.e1 = 90
        self.r2 = 100
        self.t2 = 90
        self.r2 = 100
        self.t2 = 0
        self.slidermode = False
        self.objects = []
        self.Note = False
        self.Slider = False
        self.SliderBF = False
        self.ArcSlider = False
        self.ArcSlider2 = False
        self.message = 0
        self.angle = 0
        self.v = 0
        self.va = 4
        self.va2 = -4
        self.sv = 3
        self.vm = "Velocity:"
        self.spacing = 0.4
    
    
        
    

        
    def on_draw(self):
        noStroke()
        fill(210, 185, 171)
        rect(175, 95, 1755, 1005)
        fill(30, 30, 30)
        rect(180, 100, 1750, 1000)
        
        fill(12, 156, 232)
        rect(25, 25, 150, 75, 30)
        fill(23, 67, 90)
        rect(30, 30, 145, 70, 25)
        
        fill(214, 19, 91)
        rect(25, 85, 150, 135, 30)
        fill(90, 23, 48)
        rect(30, 90, 145, 130, 25)
        
        fill(149, 229, 30)
        rect(175, 25, 350, 75, 30)
        fill(39, 62, 6)
        rect(180, 30, 345, 70, 25)
        
        fill(140, 62, 245)
        rect(375, 25, 570, 75, 30)
        fill(28, 6, 57)
        rect(380, 30, 565, 70, 25)
        
        fill(255, 120, 82)
        rect(595, 25, 800, 75, 30)
        fill(65, 16, 2)
        rect(600, 30, 795, 70, 25)
        
        fill(252, 124, 255)
        rect(825, 25, 1000, 75, 30)
        fill(65, 16, 2)
        rect(830, 30, 995, 70, 25)
        
        fill(252, 124, 255)
        rect(1010, 25, 1060, 75, 30)
        fill(65, 16, 2)
        rect(1015, 30, 1055, 70, 25)
        
        fill(252, 124, 255)
        rect(1070, 25, 1120, 75, 30)
        fill(65, 16, 2)
        rect(1075, 30, 1115, 70, 25)
        
        textSize(22)
        fill(255, 255, 255)
        text("-", 1035, 47.5)
        text("+", 1095, 47.5)
        
        textSize(22)
        fill(255, 255, 255)
        text(self.vm, 890, 47.5)
        text(str(self.v), 960, 47.5)
        
        textSize(22)
        fill(255, 255, 255)
        text("Angle:", 650, 47.5)
        text(str(self.angle)+" deg", 740, 47.5)
        
        textSize(22)
        fill(255, 255, 255)
        text("Length:", 430, 47.5)
        text(str(self.message)+"px", 515, 47.5)
        
        textSize(22)
        fill(255, 255, 255)
        text("Time:", 225, 47.5)
        text(str(float(self.num))+"s", 290, 47.5)
        
        
    
    
        textSize(22)
        fill(255, 255, 255)
        text("X:", 55, 47.5)
        fill(255, 255, 255)
        text("Y:", 55, 107.5)
        
        textSize(22)
        fill(255, 255, 255)
        text(mouseX, 100, 47.5)
        fill(255, 255, 255)
        text(mouseY, 100, 107.5)
        
        textSize(30)
        fill(210, 185, 171)
        rect(25, 200, 150, 275, 30)
        fill(80, 72, 71)
        rect(30, 205, 145, 270, 25)
        fill(255, 255, 255)
        text("Note", 85, 235)
        
        fill(210, 185, 171)
        rect(25, 300, 150, 375, 30)
        fill(80, 72, 71)
        rect(30, 305, 145, 370, 25)
        fill(255, 255, 255)
        text("Slider", 85, 335)
        
        fill(210, 185, 171)
        rect(25, 400, 150, 475, 30)
        fill(80, 72, 71)
        rect(30, 405, 145, 470, 25)
        fill(255, 255, 255)
        textSize(22)
        text("RevSlider", 85, 435)
        textSize(30)
        
        fill(210, 185, 171)
        rect(25, 500, 150, 575, 30)
        fill(80, 72, 71)
        rect(30, 505, 145, 570, 25)
        fill(255, 255, 255)
        textSize(20)
        text(" ArcSlider", 85, 535)
        textSize(30)
        
        fill(210, 185, 171)
        rect(25, 600, 150, 675, 30)
        fill(80, 72, 71)
        rect(30, 605, 145, 670, 25)
        fill(255, 255, 255)
        textSize(20)
        text("ArcSlider2", 85, 635)
        textSize(30)
        
        fill(210, 185, 171)
        rect(25, 700, 150, 775, 30)
        fill(80, 72, 71)
        rect(30, 705, 145, 770, 25)
        fill(255, 255, 255)
        text("Skip", 85, 735)
        
        fill(210, 185, 171)
        rect(25, 800, 150, 875, 30)
        fill(80, 72, 71)
        rect(30, 805, 145, 870, 25)
        fill(255, 255, 255)
        text("Clear", 85, 835)
        textSize(20)
        fill(255, 255, 255)
        text("Press P", 85, 935)
        text("to delete", 85, 955)
        textSize(30)
        
        if self.Slider:
            self.vm = "Velocity:"
            self.v = self.sv
            self.message = self.r
            self.angle = self.t
            self.Note = False
            self.SliderBF = False
            self.ArcSlider = False
            self.ArcSlider2 = False
            fill(142, 226, 255)
            rect(25, 300, 150, 375, 30)
            fill(80, 72, 71)
            rect(30, 305, 145, 370, 25)
            fill(255, 255, 255)
            text("Slider", 85, 335)
                
            stroke(100, 100, 100)
            strokeWeight(115)
            line(mouseX, mouseY, self.r * cos(radians(self.t)) + mouseX, self.r * sin(radians(self.t)) + mouseY)
            noStroke()
            
            stroke(30, 30, 30)
            strokeWeight(102.5)
            line(mouseX, mouseY, self.r * cos(radians(self.t)) + mouseX, self.r * sin(radians(self.t)) + mouseY)
            noStroke()
            
            img = loadImage("Note.png")
            image(img, mouseX, mouseY, 130, 130)
            
            if keyPressed and key == 's':
                self.r -= 2
            if keyPressed and key == 'w':
                self.r += 2
            if keyPressed and key == 'd':
                self.t -= 2
            if keyPressed and key == 'a':
                self.t += 2
            """
            if keyPressed and key == ENTER:
                self.x = mouseX
                self.y = mouseY
                self.num += 0.2
                self.beat += 1
                self.objects.append(Slider.Slider(self.x, self.y, self.r, self.t, self.beat, self))
            """
            
            
            #self.objects.append(Slider.Slider(self.x, self.y, self.r, self.t, self))
            
        
        if self.SliderBF:
            self.vm = "Velocity:"
            self.v = self.sv
            self.message = self.r
            self.angle = self.t
            self.Note = False
            self.Slider = False
            self.ArcSlider = False
            self.ArcSlider2 = False
            fill(142, 226, 255)
            rect(25, 400, 150, 475, 30)
            fill(80, 72, 71)
            rect(30, 405, 145, 470, 25)
            fill(255, 255, 255)
            textSize(22)
            text("RevSlider", 85, 435)
                
            stroke(100, 100, 100)
            strokeWeight(115)
            line(mouseX, mouseY, self.r * cos(radians(self.t)) + mouseX, self.r * sin(radians(self.t)) + mouseY)
            noStroke()
            
            stroke(30, 30, 30)
            strokeWeight(102.5)
            line(mouseX, mouseY, self.r * cos(radians(self.t)) + mouseX, self.r * sin(radians(self.t)) + mouseY)
            noStroke()
            
            pushMatrix()
            translate(self.r * cos(radians(self.t))+ mouseX, self.r * sin(radians(self.t)) + mouseY)
            rotate(radians(self.t))
            Arrow = loadImage("Arrow.png")
            image(Arrow, 0, 0, -75, -75)
            popMatrix()
            
            img = loadImage("Note.png")
            image(img, mouseX, mouseY, 130, 130)
            
            if keyPressed and key == 's':
                self.r -= 2
            if keyPressed and key == 'w':
                self.r += 2
            if keyPressed and key == 'd':
                self.t -= 2
            if keyPressed and key == 'a':
                self.t += 2
            """
            if keyPressed and key == ENTER:
                self.x = mouseX
                self.y = mouseY
                self.num += 0.2
                self.beat += 1
                self.objects.append(Slider.Slider(self.x, self.y, self.r, self.t, self.beat, self))
            """
            
        if self.Note:
            self.vm = "Spacing:"
            self.v = self.spacing
            self.message = 0
            self.angle = 0
            self.Slider = False
            self.SliderBF = False
            self.ArcSlider = False
            self.ArcSlider2 = False
                
            fill(142, 226, 255)
            rect(25, 200, 150, 275, 30)
            fill(80, 72, 71)
            rect(30, 205, 145, 270, 25)
            fill(255, 255, 255)
            text("Note", 85, 235)
            
            nt = loadImage("Note.png")
            image(nt, mouseX, mouseY, 130, 130)
            """
                self.num += 0.2
                self.beat += 1
                print("if frameCount == 60 *", str(self.num)+":")
                print("    self.objects.append(Note.Note("+str(mouseX)+",",str(mouseY)+", 130, 230, 3,",str(self.beat)+",","self))")
                print()
            """
                
        

            
        
        for object in self.objects:
            object.on_draw()
            object.on_update()
            object.frameCount = frameCount
            
            
    
            
        if self.ArcSlider:
            self.vm = "Velocity:"
            self.v = self.va
            self.angle = self.t - self.e
            self.message = self.r
            self.Note = False
            self.Slider = False
            self.SliderBF = False
            self.ArcSlider2 = False
            
            fill(142, 226, 255)
            rect(25, 500, 150, 575, 30)
            fill(80, 72, 71)
            rect(30, 505, 145, 570, 25)
            fill(255, 255, 255)
            textSize(20)
            text(" ArcSlider", 85, 535)
            textSize(30)
    
            noFill()
            stroke(100, 100, 100)
            strokeWeight(115)
            arc(mouseX, mouseY, 2*self.r, 2*self.r, radians(self.e), radians(self.t))
            noStroke()
            noFill()
            stroke(30, 30, 30)
            strokeWeight(102.5)
            arc(mouseX, mouseY, 2*self.r, 2*self.r, radians(self.e), radians(self.t))
            noStroke()
            nt = loadImage("Note.png")
            image(nt, self.r * cos(radians(self.t)) + mouseX, self.r * sin(radians(self.t)) + mouseY, 130, 130)
            
            if keyPressed and key == 's':
                self.r -= 2
            if keyPressed and key == 'w':
                self.r += 2
            if keyPressed and key == 'a':
                self.t -= 2
            if keyPressed and key == 'd':
                self.t += 2
            if keyPressed and key == 'e':
                self.e -= 2
            if keyPressed and key == 'q':
                self.e += 2
                """
                self.num += 0.2
                self.beat += 1
                print("if frameCount == 60 *", str(self.num)+":")
                print("    self.objects.append(ArcSlider.ArcSlider("+str(mouseX)+",",str(mouseY)+",",str(self.r)+",",str(self.t)+",",str(self.e)+",","130, 230, 3, 0, 5,",str(self.beat)+",","self))")
                print()
                self.num += 0.2
                """
    
        if self.ArcSlider2:
            self.vm = "Velocity:"
            self.v = self.va2
            self.angle = self.e1 - self.t1
            self.message = self.r1
            self.Note = False
            self.Slider = False
            self.SliderBF = False
            self.ArcSlider = False
            
            fill(142, 226, 255)
            rect(25, 600, 150, 675, 30)
            fill(80, 72, 71)
            rect(30, 605, 145, 670, 25)
            fill(255, 255, 255)
            textSize(20)
            text("ArcSlider2", 85, 635)
            textSize(30)
            
            noFill()
            stroke(100, 100, 100)
            strokeWeight(115)
            arc(mouseX, mouseY, 2*self.r1, 2*self.r1, radians(self.t1), radians(self.e1))
            noStroke()
            noFill()
            stroke(30, 30, 30)
            strokeWeight(102.5)
            arc(mouseX, mouseY, 2*self.r1, 2*self.r1, radians(self.t1), radians(self.e1))
            noStroke()
            nt = loadImage("Note.png")
            image(nt, self.r1 * cos(radians(self.t1)) + mouseX, self.r1 * sin(radians(self.t1)) + mouseY, 130, 130)
            
            if keyPressed and key == 's':
                self.r1 -= 2
            if keyPressed and key == 'w':
                self.r1 += 2
            if keyPressed and key == 'a':
                self.t1 -= 2
            if keyPressed and key == 'd':
                self.t1 += 2
            if keyPressed and key == 'e':
                self.e1 -= 2
            if keyPressed and key == 'q':
                self.e1 += 2
                """
                self.num += 0.2
                self.beat += 1
                print("if frameCount == 60 *", str(self.num)+":")
                print("    self.objects.append(ArcSlider2.ArcSlider2("+str(mouseX)+",",str(mouseY)+",",str(self.r1)+",",str(self.t1)+",",str(self.e1)+",","130, 230, 3, 0, -5,",str(self.beat)+",","self))")
                print()
                self.num += 0.2
                """
            
            
            
            
            
        
            
        if keyPressed and key == 'p':
            f = open("Levels.txt", "w")
            f.write("")
            f.close()
            self.num = 0
        

    
    
        
    
        
    def on_update(self):
       pass
        

        
    def on_mouse_clicked(self, mouseX, mouseY):
        
        if 30 < mouseX < 145 and 205 < mouseY < 270:
            self.Note = not self.Note
        if self.Note and 180 < mouseX < 1750 and 100 < mouseY < 1000 and mouseButton == LEFT:
            self.x = mouseX
            self.y = mouseY
            self.num += self.spacing
            self.beat += 1
            self.objects.append(Note.Note(self.x, self.y, self.beat, self))
            f = open("Levels.txt", "a")
            f.write(
                    "1, "+str(self.num)+", "+str(mouseX)+", "+str(mouseY)+", 130, 350, 5, "+str(self.beat)+"\n"
                    )
            f.close()
            
           
        
        if 30 < mouseX < 145 and 305 < mouseY < 370:
            self.Slider = not self.Slider
        if self.Slider and 180 < mouseX < 1750 and 100 < mouseY < 1000 and mouseButton == LEFT:
            self.x = mouseX
            self.y = mouseY
            self.num += 0.4
            self.beat += 1
            self.objects.append(Slider.Slider(self.x, self.y, self.r, self.t, self.beat, self))
            f = open("Levels.txt", "a")
            f.write(
                    "2, "+str(self.num)+", "+str(mouseX)+", "+str(mouseY)+", "+str(self.r)+", "+str(self.t)+", 130, 350, 5, "+str(self.sv)+", "+str(self.beat)+"\n"
                    )
            f.close()
            
            
            
        if 30 < mouseX < 145 and 405 < mouseY < 470:
            self.SliderBF = not self.SliderBF
        if self.SliderBF and 180 < mouseX < 1750 and 100 < mouseY < 1000 and mouseButton == LEFT:
            self.x = mouseX
            self.y = mouseY
            self.num += 0.4
            self.beat += 1
            self.objects.append(SliderBF.SliderBF(self.x, self.y, self.r, self.t, self.beat, self))
            f = open("Levels.txt", "a")
            f.write(
                    "3, "+str(self.num)+", "+str(mouseX)+", "+str(mouseY)+", "+str(self.r)+", "+str(self.t)+", 130, 350, 5, "+str(self.sv)+", "+str(self.beat)+"\n"
                    )
            f.close()
            
            self.num += 0.4
    
        if 30 < mouseX < 145 and 505 < mouseY < 570:
            self.ArcSlider = not self.ArcSlider
        if self.ArcSlider and 180 < mouseX < 1750 and 100 < mouseY < 1000 and mouseButton == LEFT:
            self.x = mouseX
            self.y = mouseY
            self.num += 0.4
            self.beat += 1
            self.objects.append(ArcSlider.ArcSlider(self.x, self.y, self.r, self.t, self.e, self.beat, self))
            f = open("Levels.txt", "a")
            f.write(
                    "4, "+str(self.num)+", "+str(mouseX)+", "+str(mouseY)+", "+str(self.r)+", "+str(self.t)+", "+str(self.e)+", 130, 350, 5, 0, "+str(self.va)+", "+str(self.beat)+"\n"
                    )
            f.close()
            

            
        if 30 < mouseX < 145 and 605 < mouseY < 670:
            self.ArcSlider2 = not self.ArcSlider2
        if self.ArcSlider2 and 180 < mouseX < 1750 and 100 < mouseY < 1000 and mouseButton == LEFT:
            self.x = mouseX
            self.y = mouseY
            self.num += 0.4
            self.beat += 1
            self.objects.append(ArcSlider2.ArcSlider2(self.x, self.y, self.r1, self.t1, self.e1, self.beat, self))
            f = open("Levels.txt", "a")
            f.write(
                    "5, "+str(self.num)+", "+str(mouseX)+", "+str(mouseY)+", "+str(self.r1)+", "+str(self.t1)+", "+str(self.e1)+", 130, 350, 4, 0, "+str(self.va2)+", "+str(self.beat)+"\n"
                    )
            f.close()
            
            
            
        if 30 < mouseX < 145 and 705 < mouseY < 770:
            self.num += 0.2
    
        if 30 < mouseX < 145 and 805 < mouseY < 870:
            self.objects = []
            self.beat = 0
            
        if 1010 < mouseX < 1060 and 25 < mouseY < 75:
            if self.Slider or self.SliderBF:
                self.sv -= 1
            if self.ArcSlider:
                self.va -= 1
            if self.ArcSlider2:
                self.va2 -= 1
            if self.Note:
                self.spacing -= 0.05
            else:
                self.num -= 0.05
        if 1070 < mouseX < 1120 and 25 < mouseY < 75:
            if self.Slider or self.SliderBF:
                self.sv += 1
            if self.ArcSlider:
                self.va += 1
            if self.ArcSlider2:
                self.va2 += 1
            if self.Note:
                self.spacing += 0.05
            else:
                self.num += 0.05
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
           
        
        
        
        
            
        
        
    
  



            
      

        
    
            
        
