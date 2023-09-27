import pygame

class hades_bily():
   
    

    def __init__(self, image):
        self.image=image
        self.hades_bily=pygame.image.load(self.image)
        self.hades_bily_rect=self.hades_bily.get_rect()
        self.hades_bily_rect.center=(900,120)

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

        self.ctverce_hades_bily=[]

        rect_had_x1=figurka.centerx
        rect_had_y1=figurka.centery-krok
        rect_had_1=pygame.Rect(rect_had_x1-30,rect_had_y1-30,60,60)
        self.ctverce_hades_bily.append(rect_had_1)

        rect_had_x2=figurka.centerx
        rect_had_y2=figurka.centery-krok*2
        rect_had_2=pygame.Rect(rect_had_x2-30,rect_had_y2-30,60,60)
        self.ctverce_hades_bily.append(rect_had_2)

        rect_had_x3=figurka.centerx
        rect_had_y3=figurka.centery-krok*3
        rect_had_3=pygame.Rect(rect_had_x3-30,rect_had_y3-30,60,60)
        self.ctverce_hades_bily.append(rect_had_3)

        rect_had_x4=figurka.centerx+krok
        rect_had_y4=figurka.centery-krok
        rect_had_4=pygame.Rect(rect_had_x4-30,rect_had_y4-30,60,60)
        self.ctverce_hades_bily.append(rect_had_4)

        rect_had_x5=figurka.centerx+krok*2
        rect_had_y5=figurka.centery-krok*2
        rect_had_5=pygame.Rect(rect_had_x5-30,rect_had_y5-30,60,60)
        self.ctverce_hades_bily.append(rect_had_5)

        rect_had_x6=figurka.centerx+krok*3
        rect_had_y6=figurka.centery-krok*3
        rect_had_6=pygame.Rect(rect_had_x6-30,rect_had_y6-30,60,60)
        self.ctverce_hades_bily.append(rect_had_6)

        rect_had_x7=figurka.centerx+krok
        rect_had_y7=figurka.centery
        rect_had_7=pygame.Rect(rect_had_x7-30,rect_had_y7-30,60,60)
        self.ctverce_hades_bily.append(rect_had_7)

        rect_had_x8=figurka.centerx+krok*2
        rect_had_y8=figurka.centery
        rect_had_8=pygame.Rect(rect_had_x8-30,rect_had_y8-30,60,60)
        self.ctverce_hades_bily.append(rect_had_8)

        rect_had_x9=figurka.centerx+krok*3
        rect_had_y9=figurka.centery
        rect_had_9=pygame.Rect(rect_had_x9-30,rect_had_y9-30,60,60)
        self.ctverce_hades_bily.append(rect_had_9)

        rect_had_x10=figurka.centerx+krok
        rect_had_y10=figurka.centery+krok
        rect_had_10=pygame.Rect(rect_had_x10-30,rect_had_y10-30,60,60)
        self.ctverce_hades_bily.append(rect_had_10)

        rect_had_x11=figurka.centerx+krok*2
        rect_had_y11=figurka.centery+krok*2
        rect_had_11=pygame.Rect(rect_had_x11-30,rect_had_y11-30,60,60)
        self.ctverce_hades_bily.append(rect_had_11)

        rect_had_x12=figurka.centerx-krok
        rect_had_y12=figurka.centery-krok
        rect_had_12=pygame.Rect(rect_had_x12-30,rect_had_y12-30,60,60)
        self.ctverce_hades_bily.append(rect_had_12)

        rect_had_x13=figurka.centerx-krok*2
        rect_had_y13=figurka.centery-krok*2
        rect_had_13=pygame.Rect(rect_had_x13-30,rect_had_y13-30,60,60)
        self.ctverce_hades_bily.append(rect_had_13)

        rect_had_x14=figurka.centerx-krok*3
        rect_had_y14=figurka.centery-krok*3
        rect_had_14=pygame.Rect(rect_had_x14-30,rect_had_y14-30,60,60)
        self.ctverce_hades_bily.append(rect_had_14)

        rect_had_x15=figurka.centerx-krok
        rect_had_y15=figurka.centery
        rect_had_15=pygame.Rect(rect_had_x15-30,rect_had_y15-30,60,60)
        self.ctverce_hades_bily.append(rect_had_15)

        rect_had_x16=figurka.centerx-krok*2
        rect_had_y16=figurka.centery
        rect_had_16=pygame.Rect(rect_had_x16-30,rect_had_y16-30,60,60)
        self.ctverce_hades_bily.append(rect_had_16)

        rect_had_x17=figurka.centerx-krok*3
        rect_had_y17=figurka.centery
        rect_had_17=pygame.Rect(rect_had_x17-30,rect_had_y17-30,60,60)
        self.ctverce_hades_bily.append(rect_had_17)

        rect_had_x18=figurka.centerx-krok
        rect_had_y18=figurka.centery+krok
        rect_had_18=pygame.Rect(rect_had_x18-30,rect_had_y18-30,60,60)
        self.ctverce_hades_bily.append(rect_had_18)

        rect_had_x19=figurka.centerx-krok*2
        rect_had_y19=figurka.centery+krok*2
        rect_had_19=pygame.Rect(rect_had_x19-30,rect_had_y19-30,60,60)
        self.ctverce_hades_bily.append(rect_had_19)






                 

    

    


                

           
