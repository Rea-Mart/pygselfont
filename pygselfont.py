import pygame

class PygselFont():
    def __init__(self, file:str, fill:tuple, thickness:int=0,outline:tuple=(0,0,0),alphabet:str="abcdefghijklmnopqrstuvwxyz"):
        """ Make a PygselFont from a (.png) `file`, with a 
        `fill` (text color), 
        `thickness`(0=no outline, 1=pixel perfect, 2=square),
        `outline` (outline color),
        `alphabet` (the order of letters)"""


        font_image = pygame.image.load(file)
        seperator = font_image.map_rgb((0, 0, 255))
        source_pixarray = pygame.PixelArray(font_image)
        source_pixarray.replace((255,0,0),fill)
        if thickness == 0:
            source_pixarray.replace((100,100,100),(0,0,0))
            source_pixarray.replace((0,0,0),(0,0,0,0))
        elif thickness == 1:
            source_pixarray.replace((100,100,100),(0,0,0,0))
            source_pixarray.replace((0,0,0),outline)
        elif thickness == 2:
            source_pixarray.replace((100,100,100),(0,0,0))
            source_pixarray.replace((0,0,0),outline)
        
        self.alphabet = alphabet
        self.font_dict = {}
        for letter in self.alphabet:
            self.font_dict[letter] = {}

        last_seperator = 0
        seperator_count = 0
        self.height = source_pixarray.shape[1]-1
        for x in range(source_pixarray.shape[0]):
            if source_pixarray[x, 0] == seperator:
                self.font_dict[alphabet[seperator_count]]["width"] = x - last_seperator
                self.font_dict[alphabet[seperator_count]]["img"] = source_pixarray[last_seperator:x, 1:self.height+1].make_surface()
                last_seperator = x
                seperator_count += 1
        
    def render(self,text:str) -> pygame.Surface:
        """Returns a Surface with the rendered text on it, like pygame.Font.render()"""
        inputwidth = 0
        for letter in text:
            if letter in self.alphabet:
                inputwidth += self.font_dict[letter]["width"]
            else:
                inputwidth += 6
        strsurf = pygame.Surface((inputwidth+1,self.height),pygame.SRCALPHA)

        width_used = 0
        for letter in text:
            if letter in self.alphabet:
                strsurf.blit(self.font_dict[letter]["img"],(width_used,0))
                width_used += self.font_dict[letter]["width"]
            else:
                width_used += 6
        return strsurf