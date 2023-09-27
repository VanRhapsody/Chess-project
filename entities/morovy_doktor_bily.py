import pygame

class morovy_doktor_bily():
   
    

    def __init__(self, image):
        self.image=image
        self.morovy_doktor_bily=pygame.image.load(self.image)
        self.morovy_doktor_bily_rect=self.morovy_doktor_bily.get_rect()
        self.morovy_doktor_bily_rect.center=(540,120)

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

        self.ctverce_morovy_doktor_bily=[]

        rect_mor_x1=figurka.centerx+krok
        rect_mor_y1=figurka.centery
        rect_mor_1=pygame.Rect(rect_mor_x1-30,rect_mor_y1-30,60,60)
        self.ctverce_morovy_doktor_bily.append(rect_mor_1)

        rect_mor_x2=figurka.centerx+krok*2
        rect_mor_y2=figurka.centery
        rect_mor_2=pygame.Rect(rect_mor_x2-30,rect_mor_y2-30,60,60)
        self.ctverce_morovy_doktor_bily.append(rect_mor_2)

        rect_mor_x3=figurka.centerx-krok
        rect_mor_y3=figurka.centery
        rect_mor_3=pygame.Rect(rect_mor_x3-30,rect_mor_y3-30,60,60)
        self.ctverce_morovy_doktor_bily.append(rect_mor_3)

        rect_mor_x4=figurka.centerx-2*krok
        rect_mor_y4=figurka.centery
        rect_mor_4=pygame.Rect(rect_mor_x4-30,rect_mor_y4-30,60,60)
        self.ctverce_morovy_doktor_bily.append(rect_mor_4)

        rect_mor_x5=figurka.centerx
        rect_mor_y5=figurka.centery+krok
        rect_mor_5=pygame.Rect(rect_mor_x5-30,rect_mor_y5-30,60,60)
        self.ctverce_morovy_doktor_bily.append(rect_mor_5)

        rect_mor_x6=figurka.centerx
        rect_mor_y6=figurka.centery+krok*2
        rect_mor_6=pygame.Rect(rect_mor_x6-30,rect_mor_y6-30,60,60)
        self.ctverce_morovy_doktor_bily.append(rect_mor_6)

        rect_mor_x7=figurka.centerx
        rect_mor_y7=figurka.centery+krok*3
        rect_mor_7=pygame.Rect(rect_mor_x7-30,rect_mor_y7-30,60,60)
        self.ctverce_morovy_doktor_bily.append(rect_mor_7)

        rect_mor_x8=figurka.centerx
        rect_mor_y8=figurka.centery+krok*4
        rect_mor_8=pygame.Rect(rect_mor_x8-30,rect_mor_y8-30,60,60)
        self.ctverce_morovy_doktor_bily.append(rect_mor_8)

        rect_mor_x9=figurka.centerx
        rect_mor_y9=figurka.centery+krok*5
        rect_mor_9=pygame.Rect(rect_mor_x9-30,rect_mor_y9-30,60,60)
        self.ctverce_morovy_doktor_bily.append(rect_mor_9)

        rect_mor_x10=figurka.centerx
        rect_mor_y10=figurka.centery+krok*6
        rect_mor_10=pygame.Rect(rect_mor_x10-30,rect_mor_y10-30,60,60)
        self.ctverce_morovy_doktor_bily.append(rect_mor_10)

        rect_mor_x11=figurka.centerx
        rect_mor_y11=figurka.centery+krok*7
        rect_mor_11=pygame.Rect(rect_mor_x11-30,rect_mor_y11-30,60,60)
        self.ctverce_morovy_doktor_bily.append(rect_mor_11)

        rect_mor_x12=figurka.centerx
        rect_mor_y12=figurka.centery-krok
        rect_mor_12=pygame.Rect(rect_mor_x12-30,rect_mor_y12-30,60,60)
        self.ctverce_morovy_doktor_bily.append(rect_mor_12)

        rect_mor_x13=figurka.centerx
        rect_mor_y13=figurka.centery-krok*2
        rect_mor_13=pygame.Rect(rect_mor_x13-30,rect_mor_y13-30,60,60)
        self.ctverce_morovy_doktor_bily.append(rect_mor_13)

        rect_mor_x14=figurka.centerx
        rect_mor_y14=figurka.centery-krok*3
        rect_mor_14=pygame.Rect(rect_mor_x14-30,rect_mor_y14-30,60,60)
        self.ctverce_morovy_doktor_bily.append(rect_mor_14)

        rect_mor_x15=figurka.centerx
        rect_mor_y15=figurka.centery-krok*4
        rect_mor_15=pygame.Rect(rect_mor_x15-30,rect_mor_y15-30,60,60)
        self.ctverce_morovy_doktor_bily.append(rect_mor_15)

        rect_mor_x16=figurka.centerx
        rect_mor_y16=figurka.centery-krok*5
        rect_mor_16=pygame.Rect(rect_mor_x16-30,rect_mor_y16-30,60,60)
        self.ctverce_morovy_doktor_bily.append(rect_mor_16)

        rect_mor_x17=figurka.centerx
        rect_mor_y17=figurka.centery-krok*6
        rect_mor_17=pygame.Rect(rect_mor_x17-30,rect_mor_y17-30,60,60)
        self.ctverce_morovy_doktor_bily.append(rect_mor_17)

        rect_mor_x18=figurka.centerx
        rect_y18=figurka.centery-krok*7
        rect18=pygame.Rect(rect_mor_x18-30,rect_y18-30,60,60)
        self.ctverce_morovy_doktor_bily.append(rect18)






                 

    

    


                

           
