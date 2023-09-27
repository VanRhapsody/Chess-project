import pygame

class kardinal_bily():
   
    

    def __init__(self, image):
        self.image=image
        self.kardinal_bily=pygame.image.load(self.image)
        self.kardinal_bily_rect=self.kardinal_bily.get_rect()
        self.kardinal_bily_rect.center=(780,120)

    def draw(self, screen, figurka, figurka_rect):
        screen.blit(figurka,figurka_rect)


    def move(self, screen,figurka, ctverce):
            for event in pygame.event.get():
                
                if figurka.collidepoint(event.pos):
                        for ctverec in ctverce:
                            if (ctverec.right > 1440 or ctverec.left < 475) or (ctverec.bottom > 850 or ctverec.top < 60):
                                continue
                            else:
                                pygame.draw.rect(screen,(0,0,0),ctverec,5)
                        figurka.centerx=event.pos[0]
                        figurka.centery=event.pos[1]



    def update(self,figurka):
        krok=120

        self.ctverce_kardinal_bily=[]

        rect_kar_x1=figurka.centerx+krok
        rect_kar_y1=figurka.centery-krok
        rect_kar_1=pygame.Rect(rect_kar_x1-30,rect_kar_y1-30,60,60)
        self.ctverce_kardinal_bily.append(rect_kar_1)

        rect_kar_x2=figurka.centerx-krok
        rect_kar_y2=figurka.centery-krok
        rect_kar_2=pygame.Rect(rect_kar_x2-30,rect_kar_y2-30,60,60)
        self.ctverce_kardinal_bily.append(rect_kar_2)

        rect_kar_x3=figurka.centerx+krok
        rect_kar_y3=figurka.centery+krok
        rect_kar_3=pygame.Rect(rect_kar_x3-30,rect_kar_y3-30,60,60)
        self.ctverce_kardinal_bily.append(rect_kar_3)

        rect_kar_x4=figurka.centerx-krok
        rect_kar_y4=figurka.centery+krok
        rect_kar_4=pygame.Rect(rect_kar_x4-30,rect_kar_y4-30,60,60)
        self.ctverce_kardinal_bily.append(rect_kar_4)






                 

    

    


                

           
