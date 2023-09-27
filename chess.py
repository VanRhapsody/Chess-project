import pygame
import mysql.connector
import random
from entities.morovy_doktor_bily import morovy_doktor_bily
from entities.arcibiskup_bily import arcibiskup_bily

#Classy

class Sachovnice(pygame.sprite.Sprite):
    def __init__(self):
        scale = 150
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0:
                    pygame.draw.rect(screen, (255,248,220), (x * scale, y * scale, scale, scale))
                else:
                    pygame.draw.rect(screen, (139,69,19), (x * scale, y * scale, scale, scale))


pygame.init()

"""#Nastavení připojení k databázi
db_connection = mysql.connector.connect(
    host="dbs.spskladno.cz",
    user="student3",
    password="spsnet",
    database="vyuka3"
)

cursor = db_connection.cursor()

cursor.execute("SELECT * FROM leaderboard")
result = cursor.fetchall()

cursor.close()
db_connection.close()
"""
screen_width=1920
screen_height=1080
screen=pygame.display.set_mode((screen_width,screen_height),pygame.FULLSCREEN)
pygame.display.set_caption("Šachy dle našeho")

#Nastavení fps
clock=pygame.time.Clock()
fps=60

#Načtení obrázků figurek
#arcibiskup_bily=pygame.image.load("img/Arcibiskup_bily.png") #todo=zvětšit jeho velikost
#arcibiskup_cerny=pygame.image.load("img/Arcibiskup_cerny.png")
#hades_bily=pygame.image.load("img/Hades_bily.png")
#hades_cerny=pygame.image.load("img/Hades_cerny.png")
#kardinal_bily=pygame.image.load("img/Kardinal_bily.png")
#kardinal_cerny=pygame.image.load("img/Kardinal_cerny.png")
#legionar_bily=pygame.image.load("img/Legionar_bily.png")
#legionar_cerny=pygame.image.load("img/Legionar_cerny.png")
# morovy_doktor_bily=pygame.image.load("img/Morovy_doktor_bily.png")
# morovy_doktor_cerny=pygame.image.load("img/Morovy_dotkor_cerny.png")
# persefona_bila=pygame.image.load("img/Persefona_bila.png")
# persefona_cerna=pygame.image.load("img/Persefona_cerna.png")
# valecnik_bily=pygame.image.load("img/Valecnik_bily.png")
# valecnik_cerny=pygame.image.load("img/Valecnik_cerny.png")
morovy_doktor_bily_figurka=morovy_doktor_bily("img/Morovy_doktor_bily.png")
arcibiskup_bily_figuka=arcibiskup_bily("img/Arcibiskup_bily.png")

#Nastavení pozic bílých figurek
# morovy_doktor_bily_rect=morovy_doktor_bily.get_rect()
# morovy_doktor_bily_rect.center=(540,120)
# arcibiskup_bily_rect=arcibiskup_bily.get_rect()
# arcibiskup_bily_rect.center=(660,120)
# kardinal_bily_rect=kardinal_bily.get_rect()
# kardinal_bily_rect.center=(780,120)
# hades_bily_rect=hades_bily.get_rect()
# hades_bily_rect.center=(900,120)
# persefona_bila_rect=persefona_bila.get_rect()
# persefona_bila_rect.center=(1020,120)
# kardinal_bily_rect1=kardinal_bily.get_rect()
# kardinal_bily_rect1.center=(1140,120)
# arcibiskup_bily_rect1=arcibiskup_bily.get_rect()
# arcibiskup_bily_rect1.center=(1260,120)
# morovy_doktor_bily_rect1=morovy_doktor_bily.get_rect()
# morovy_doktor_bily_rect1.center=(1380,120)
# valecnik_bily_rect=valecnik_bily.get_rect()
# valecnik_bily_rect.center=(540,240)
# legionar_bily_rect=legionar_bily.get_rect()
# legionar_bily_rect.center=(660,240)
# valecnik_bily_rect1=valecnik_bily.get_rect()
# valecnik_bily_rect1.center=(780,240)
# legionar_bily_rect1=legionar_bily.get_rect()
# legionar_bily_rect1.center=(900,240)
# valecnik_bily_rect2=valecnik_bily.get_rect()
# valecnik_bily_rect2.center=(1020,240)
# legionar_bily_rect2=legionar_bily.get_rect()
# legionar_bily_rect2.center=(1140,240)
# valecnik_bily_rect3=valecnik_bily.get_rect()
# valecnik_bily_rect3.center=(1260,240)
# legionar_bily_rect3=legionar_bily.get_rect()
# legionar_bily_rect3.center=(1380,240)

#Nastavení pozic černých figurek
# morovy_doktor_cerny_rect=morovy_doktor_cerny.get_rect()
# morovy_doktor_cerny_rect.center=(540,960)
# arcibiskup_cerny_rect=arcibiskup_cerny.get_rect()
# arcibiskup_cerny_rect.center=(660,960)
# kardinal_cerny_rect=kardinal_cerny.get_rect()
# kardinal_cerny_rect.center=(780,960)
# hades_cerny_rect=hades_cerny.get_rect()
# hades_cerny_rect.center=(900,960)
# persefona_cerna_rect=persefona_cerna.get_rect()
# persefona_cerna_rect.center=(1020,960)
# kardinal_cerny_rect1=kardinal_cerny.get_rect()
# kardinal_cerny_rect1.center=(1140,960)
# arcibiskup_cerny_rect1=arcibiskup_cerny.get_rect()
# arcibiskup_cerny_rect1.center=(1260,960)
# morovy_doktor_cerny_rect1=morovy_doktor_cerny.get_rect()
# morovy_doktor_cerny_rect1.center=(1380,960)
# legionar_cerny_rect=legionar_cerny.get_rect()
# legionar_cerny_rect.center=(540,840)
# valecnik_cerny_rect=valecnik_cerny.get_rect()
# valecnik_cerny_rect.center=(660,840)
# legionar_cerny_rect1=legionar_cerny.get_rect()
# legionar_cerny_rect1.center=(780,840)
# valecnik_cerny_rect1=valecnik_cerny.get_rect()
# valecnik_cerny_rect1.center=(900,840)
# legionar_cerny_rect2=legionar_cerny.get_rect()
# legionar_cerny_rect2.center=(1020,840)
# valecnik_cerny_rect2=valecnik_cerny.get_rect()
# valecnik_cerny_rect2.center=(1140,840)
# legionar_cerny_rect3=legionar_cerny.get_rect()
# legionar_cerny_rect3.center=(1260,840)
# valecnik_cerny_rect3=valecnik_cerny.get_rect()
# valecnik_cerny_rect3.center=(1380,840)

#Deklarace barev
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
active_color=(255,255,255)
passive_collor=(180,180,180)
#Nastavení pozadí
background_image=pygame.image.load("loginpozadi.jpg")
background_image_rect=background_image.get_rect()
background_image_rect.center=(screen_width/2,screen_height/2)

#Hudba v pozadí
songs=["Anguish.mp3","Bleach OST 3-Clavar La Espada.mp3","y2mate.com - Kyrie Ⅱ.mp3","Nube Negra.mp3","y2mate.com - American Prometheus.mp3"]
song=random.choice(songs)
pygame.mixer.music.load(song)
pygame.mixer.music.play(1,0)

#Texty pro buttony a samotné buttony

button=pygame.Rect(810,360,300,80)
button_font=pygame.font.SysFont("georgia",40,False)
button_text_start_game=button_font.render("Začít hru", True, black)
button_text_start_game_rect=button_text_start_game.get_rect()
button_text_start_game_rect.center=(screen_width/2,400)

button1=pygame.Rect(810,460,300,80)

button_text_start_game1=button_font.render("Nightmare mode", True, black)
button_text_start_game_rect1=button_text_start_game1.get_rect()
button_text_start_game_rect1.center=(screen_width/2,500)

button2=pygame.Rect(810,560,300,80)

button_text_start_game2=button_font.render("Ukončit hru", True, black)
button_text_start_game_rect2=button_text_start_game2.get_rect()
button_text_start_game_rect2.center=(screen_width/2,600)

#Text pro leaderboard a pozadí pro ni
"""leaderboard_font=pygame.font.SysFont("georgia",50,False)
leadeboard_text_font=pygame.font.SysFont("georgia",30,False)
leaderboard_text=leaderboard_font.render("Leaderboard",True, white)
leaderboard_text_rect=leaderboard_text.get_rect()
leaderboard_text_rect.center=(1660,60)
leaderboard_background=pygame.Rect(1400,30,500,1000)"""

#Zvuk zahájení hry
start_game=pygame.mixer.Sound("Sound effect bell.mp3")

#Text pro input
header_font=pygame.font.SysFont("georgia",50,False)
input_font=pygame.font.SysFont("georgia",40,False)
mail_header=header_font.render("Zadejte E-Mail",True, white)
mail_header_rect=mail_header.get_rect()
mail_header_rect.midleft=(100,300)
input_box1=pygame.rect.Rect(100,350,2000,100)
input_user_text1=''

pass_header=header_font.render("Zadejte heslo",True, white)
pass_header_rect=pass_header.get_rect()
pass_header_rect.midleft=(100,520)
input_box2=pygame.rect.Rect(100,570,2000,100)
input_user_text2=''

send_header=header_font.render("Přihlásit se",True, black)
send_header_rect=send_header.get_rect()
send_header_rect.midleft=(100,740)
send_box=pygame.rect.Rect(100,700,350,90)

#Text pro oznámení přihlášení
logged_header=header_font.render("Úspěšně přihlášeno",True,white)
logged_header_rect=logged_header.get_rect()
logged_header_rect.midleft=(100,950)

failed_header=header_font.render("Neplatné údaje",True,white)
failed_header_rect=failed_header.get_rect()
failed_header_rect.midleft=(100,950)

fill_header=header_font.render("Vyplňte prosím všechna pole",True,white)
fill_header_rect=fill_header.get_rect()
fill_header_rect.midleft=(100,950)

#Text pro název hry
title_font=pygame.font.SysFont("georgia",80,False)
title_header=title_font.render("Our Chess",True, white)
title_header_rect=title_header.get_rect()
title_header_rect.center=(screen_width/2,300)

#Zjištění konce hudby v hlavním menu
music_end = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(music_end)

#Získání pozic čtverců (nápověd) pro pohyb figurek

krok=120



morovy_doktor_bily_figurka.update(morovy_doktor_bily_figurka.morovy_doktor_bily_rect)
arcibiskup_bily_figuka.update(arcibiskup_bily_figuka.arcibiskup_bily_rect)







#Nastavení bool proměnných pro funkčnost programu v prvotní fázi
active=False
active1=False
active2=False
empty=False
user=False
pohyb=False
show_main_menu=True
play_game=False
run=True
while run:
    mx,my=pygame.mouse.get_pos()
    print(mx,my)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if button2.collidepoint(event.pos) and show_main_menu:
                run=False
            if button.collidepoint(event.pos) and show_main_menu:
                show_main_menu=False
                play_game=True
                pygame.mixer.music.stop()
                start_game.play()
                screen.fill((0,0,0))
            if input_box1.collidepoint(event.pos) and show_main_menu:
                active = True
            else:
                active = False
            if input_box2.collidepoint(event.pos) and show_main_menu:
                active1=True
            else:
                active1=False
            if send_box.collidepoint(event.pos) and show_main_menu:
                active2=True
                if input_user_text1=='' or input_user_text2=='':
                    screen.blit(fill_header,fill_header_rect)
                    empty=True
                else:
                    empty=False
                    """"conn = mysql.connector.connect(
                    host="dbs.spskladno.cz",
                    user="student3",
                    password="spsnet",
                    database="vyuka3"
                    )
                    cursor1=conn.cursor()
                    print(input_user_text1,input_user_text2)
                    query = "SELECT * FROM registracechess WHERE email = %s AND password = %s"
                    cursor1.execute(query, (input_user_text1, input_user_text2))
                    user = cursor1.fetchone()
                    #cursor1.close() z nějakého důvodu to s tímto po přihlášení padá, AI nepomohlo
                    conn.close()"""
            
                    if user:
                        screen.blit(logged_header,logged_header_rect)
                        print("Úspěch")
                        user_email=input_user_text1
                        input_user_text1=''
                        input_user_text2=''
                        
                    else:
                        screen.blit(failed_header,failed_header_rect)
                        print("Neúspěch")
            else:
                active2=False

  
        if event.type==pygame.KEYDOWN and show_main_menu:
            if event.key==pygame.K_BACKSPACE:
                if active:
                    input_user_text1=input_user_text1[:-1]
            else: 
                if active:

                    input_user_text1+=event.unicode
            if event.key==pygame.K_BACKSPACE:
                if active1:
                    input_user_text2=input_user_text2[:-1]
            else: 
                if active1:

                    input_user_text2+=event.unicode
        if event.type==music_end and show_main_menu:
            song=random.choice(songs)
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(1,0)

    #Kontrola kolize s buttonem
    x,y=pygame.mouse.get_pos()

    if show_main_menu:
        #Vykreslení pozadí
        screen.blit(background_image,background_image_rect)
        #Hover pro buttony
        if button.x <= x <= button.x+300 and button.y <= y <= button.y + 80:
            pygame.draw.rect(screen,(180,180,180), button)
        else:
            pygame.draw.rect(screen,(110,110,110), button)

        if button1.x <= x <= button1.x+300 and button1.y <= y <= button1.y + 80:
            pygame.draw.rect(screen,(180,180,180), button1)
        else:
            pygame.draw.rect(screen,(110,110,110), button1)

        if button2.x <= x <= button2.x+300 and button2.y <= y <= button2.y + 80:
            pygame.draw.rect(screen,(180,180,180), button2)
        else:
            pygame.draw.rect(screen,(110,110,110), button2)

        #Vykreslení textu pro buttony
        screen.blit(button_text_start_game,button_text_start_game_rect)
        screen.blit(button_text_start_game1,button_text_start_game_rect1)
        screen.blit(button_text_start_game2,button_text_start_game_rect2)

        #Vykreslení pozadí leaderboardu a textu leaderboardu
        """pygame.draw.rect(screen,black,leaderboard_background)
        screen.blit(leaderboard_text,leaderboard_text_rect)"""

        #Vypsání dat pro leadeboard
        """y=100
        for row in result:
            text=", ".join(str(item) for item in row)
            text_surface=leadeboard_text_font.render(text,True, white)
            print(text_surface)
            screen.blit(text_surface, (1580,y))
            y+=40  """

        #Vykreslení login formu
        if active:
            color = active_color
        else:
            color = passive_collor
        if active1:
            color1 = active_color
        else:
            color1 = passive_collor
        if active2:
            color2=active_color
            if user:
                    screen.blit(logged_header,logged_header_rect)
            elif empty:
                    screen.blit(fill_header,fill_header_rect)
            else:
                    screen.blit(failed_header,failed_header_rect)
        else:
            color2=passive_collor
        
        #Vykreslení login formu
        pygame.draw.rect(screen, color, input_box1)
        pygame.draw.rect(screen, color1, input_box2)
        pygame.draw.rect(screen, color2 ,send_box)

        input_text = input_font.render(input_user_text1, True, (0,0,0))
        input_text1 = input_font.render(input_user_text2, True, (0,0,0))

        screen.blit(input_text, (input_box1.x+5, input_box1.y+5))
        screen.blit(input_text1, (input_box2.x+5, input_box2.y+5))

        input_box1.w = max(500, input_text.get_width()+10)
        input_box2.w = max(500, input_text1.get_width()+10)

        screen.blit(mail_header,mail_header_rect)
        screen.blit(pass_header,pass_header_rect)
        screen.blit(send_header,send_header_rect)

        #Vykreslení názvu hry
        screen.blit(title_header,title_header_rect)



        
    if play_game:
        #Zastavení hudby v pozadí
        pygame.mixer.music.stop()

        scale = 120
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0:
                    pygame.draw.rect(screen, (255,248,220), (x * scale+480, y * scale+60, scale, scale))
                else:
                    pygame.draw.rect(screen, (139,69,19), (x * scale+480, y * scale+60, scale, scale))
        
        morovy_doktor_bily_figurka.update(morovy_doktor_bily_figurka.morovy_doktor_bily_rect)
        arcibiskup_bily_figuka.update(arcibiskup_bily_figuka.arcibiskup_bily_rect)

        morovy_doktor_bily_figurka.draw(screen,morovy_doktor_bily_figurka.morovy_doktor_bily,morovy_doktor_bily_figurka.morovy_doktor_bily_rect)
        arcibiskup_bily_figuka.draw(screen,arcibiskup_bily_figuka.arcibiskup_bily,arcibiskup_bily_figuka.arcibiskup_bily_rect)


        pygame.display.update()
       
       


  

        

        #figurky_bile=[morovy_doktor_bily_rect,arcibiskup_bily_rect,kardinal_bily_rect,hades_bily_rect,persefona_bila_rect,kardinal_bily_rect1,arcibiskup_bily_rect1,morovy_doktor_bily_rect1,legionar_bily_rect,valecnik_bily_rect,legionar_bily_rect1,valecnik_bily_rect1,legionar_bily_rect2,valecnik_bily_rect2,legionar_bily_rect3,valecnik_bily_rect3]
        #figurky_cerne=[morovy_doktor_cerny_rect,arcibiskup_cerny_rect,kardinal_cerny_rect,hades_cerny_rect,persefona_cerna_rect,kardinal_bily_rect1,arcibiskup_cerny_rect1,morovy_doktor_cerny_rect1,legionar_cerny_rect,valecnik_cerny_rect,legionar_cerny_rect1,valecnik_cerny_rect1,legionar_cerny_rect2,valecnik_cerny_rect2,legionar_cerny_rect3,valecnik_cerny_rect3]
        #Tažení figurek, todo: omezit jejich pohyb na schéma tažení
        
        
    

          

        
        if event.type==pygame.MOUSEMOTION and event.buttons[0]==1:
            pohyb=True
            """for figurka_cerna in figurky_cerne:
                if figurka_cerna.collidepoint(event.pos):
                    figurka_cerna.centerx=event.pos[0]
                    figurka_cerna.centery=event.pos[1]
            for figurka_bila in figurky_bile:
                if figurka_bila.collidepoint(event.pos):
                    figurka_bila.centerx=event.pos[0]
                    figurka_bila.centery=event.pos[1]"""
            morovy_doktor_bily_figurka.move(screen,morovy_doktor_bily_figurka.morovy_doktor_bily_rect,morovy_doktor_bily_figurka.ctverce_morovy_doktor_bily)
            arcibiskup_bily_figuka.move(screen,arcibiskup_bily_figuka.arcibiskup_bily_rect,arcibiskup_bily_figuka.ctverce_arcibiskup_bily)
           
                 

                
                      

             
                    
        if event.type==pygame.MOUSEBUTTONUP:
            pohyb=False #Todo: zjistit, jak tento proces zjednodušit pomocí for cyklu
            """for i in range(0,len(ctverce_morovy_doktor_bily)): 
                if morovy_doktor_bily_rect.colliderect(ctverce_morovy_doktor_bily[i]):
                    morovy_doktor_bily_rect.centerx=ctverce_morovy_doktor_bily[i].centerx
                    morovy_doktor_bily_rect.centery=ctverce_morovy_doktor_bily[i].centery

                elif i==len(ctverce_morovy_doktor_bily)-1:
                    morovy_doktor_bily_rect.centerx=morovy_doktor_bily_x_pred
                    morovy_doktor_bily_rect.centery=morovy_doktor_bily_y_pred"""
      
            
            

            
        
        #Kontrola kolize


    pygame.display.update()

    clock.tick(60)

pygame.quit()