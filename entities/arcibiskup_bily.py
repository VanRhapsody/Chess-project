import pygame

class arcibiskup_bily():
   
    

    def __init__(self, image):
        self.image=image
        self.arcibiskup_bily=pygame.image.load(self.image)
        self.arcibiskup_bily_rect=self.arcibiskup_bily.get_rect()
        self.arcibiskup_bily_rect.center=(660,120)

    def draw(self, screen, figurka, figurka_rect):
        screen.blit(figurka,figurka_rect)


    def move(self, screen,figurka, ctverce):
            for event in pygame.event.get():
                if event.type==pygame.MOUSEMOTION and event.buttons[0]==1: 
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

        self.ctverce_arcibiskup_bily=[]

        rect_arc_x1=figurka.centerx+krok*2
        rect_arc_y1=figurka.centery
        rect_arc_1=pygame.Rect(rect_arc_x1-30,rect_arc_y1-30,60,60)
        self.ctverce_arcibiskup_bily.append(rect_arc_1)

        rect_arc_x2=figurka.centerx+krok*2
        rect_arc_y2=figurka.centery+krok
        rect_arc_2=pygame.Rect(rect_arc_x2-30,rect_arc_y2-30,60,60)
        self.ctverce_arcibiskup_bily.append(rect_arc_2)

        rect_arc_x3=figurka.centerx+krok*2
        rect_arc_y3=figurka.centery-krok
        rect_arc_3=pygame.Rect(rect_arc_x3-30,rect_arc_y3-30,60,60)
        self.ctverce_arcibiskup_bily.append(rect_arc_3)

        rect_arc_x4=figurka.centerx-krok*2
        rect_arc_y4=figurka.centery
        rect_arc_4=pygame.Rect(rect_arc_x4-30,rect_arc_y4-30,60,60)
        self.ctverce_arcibiskup_bily.append(rect_arc_4)

        rect_arc_x5=figurka.centerx-krok*2
        rect_arc_y5=figurka.centery+krok
        rect_arc_5=pygame.Rect(rect_arc_x5-30,rect_arc_y5-30,60,60)
        self.ctverce_arcibiskup_bily.append(rect_arc_5)

        rect_arc_x6=figurka.centerx-krok*2
        rect_arc_y6=figurka.centery-krok
        rect_arc_6=pygame.Rect(rect_arc_x6-30,rect_arc_y6-30,60,60)
        self.ctverce_arcibiskup_bily.append(rect_arc_6)

        rect_arc_x7=figurka.centerx
        rect_arc_y7=figurka.centery+krok*2
        rect_arc_7=pygame.Rect(rect_arc_x7-30,rect_arc_y7-30,60,60)
        self.ctverce_arcibiskup_bily.append(rect_arc_7)

        rect_arc_x8=figurka.centerx+krok
        rect_arc_y8=figurka.centery+krok*2
        rect_arc_8=pygame.Rect(rect_arc_x8-30,rect_arc_y8-30,60,60)
        self.ctverce_arcibiskup_bily.append(rect_arc_8)

        rect_arc_x9=figurka.centerx-krok
        rect_arc_y9=figurka.centery+krok*2
        rect_arc_9=pygame.Rect(rect_arc_x9-30,rect_arc_y9-30,60,60)
        self.ctverce_arcibiskup_bily.append(rect_arc_9)

        rect_arc_x10=figurka.centerx
        rect_arc_y10=figurka.centery-krok*2
        rect_arc_10=pygame.Rect(rect_arc_x10-30,rect_arc_y10-30,60,60)
        self.ctverce_arcibiskup_bily.append(rect_arc_10)

        rect_arc_x11=figurka.centerx+krok
        rect_arc_y11=figurka.centery-krok*2
        rect_arc_11=pygame.Rect(rect_arc_x11-30,rect_arc_y11-30,60,60)
        self.ctverce_arcibiskup_bily.append(rect_arc_11)

        rect_arc_x12=figurka.centerx-krok
        rect_arc_y12=figurka.centery-krok*2
        rect_arc_12=pygame.Rect(rect_arc_x12-30,rect_arc_y12-30,60,60)
        self.ctverce_arcibiskup_bily.append(rect_arc_12)





                 

    

    


                

           
