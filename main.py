import pyxel

HEIGHT = 256
WIDTH = 256
MAP_HEIGHT = 55
MAP_WIDTH = 71

SCREEN_PIXELS = 32 

BG_COLOR = 11


class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, caption="Railroad")

        pyxel.load("./res/img.pyxres", tilemap=True)
        self.x = 0
        self.y = 0   

        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)
        

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btn(pyxel.KEY_RIGHT):
            if self.x <= MAP_WIDTH-SCREEN_PIXELS:
                self.x = self.x + 1
                
        if pyxel.btn(pyxel.KEY_LEFT):
            if self.x > 0:                
                self.x = self.x - 1

        if pyxel.btn(pyxel.KEY_DOWN):
            if self.y <= MAP_HEIGHT-SCREEN_PIXELS:                
                self.y = self.y + 1

        if pyxel.btn(pyxel.KEY_UP):
            if self.y > 0:                
                self.y = self.y - 1


    def text_score(self, x, y, amount_money):
        
        pyxel.rect(x-5, y-5, 27, 13, 7)
        pyxel.text(x, y, f"{amount_money}$", 0)

        

    def draw(self):
        
        pyxel.cls(BG_COLOR)

        #draw map
        pyxel.bltm(0,0,0, self.x, self.y, 71, 55)      
            
        self.text_score(230, 16, 300)
        
        #train 
        pyxel.blt(0, 194, 0, 0, 16, 32, 8)


App()
