import pygame
import mysql.connector
import random

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

#Nastavení připojení k databázi
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

screen_width=1920
screen_height=1080
screen= pygame.display.set_mode((screen_width,screen_height),pygame.FULLSCREEN)
pygame.display.set_caption("Šachy dle našeho")

#Nastavení fps
clock=pygame.time.Clock()
fps=60

#Načtení obrázků figurek
arcibiskup_bily=pygame.image.load("img/Arcibiskup_bily.png") #todo=zvětšit jeho velikost
arcibiskup_cerny=pygame.image.load("img/Arcibiskup_cerny.png")
hades_bily=pygame.image.load("img/Hades_bily.png")
hades_cerny=pygame.image.load("img/Hades_cerny.png")
kardinal_bily=pygame.image.load("img/Kardinal_bily.png")
kardinal_cerny=pygame.image.load("img/Kardinal_cerny.png")
legionar_bily=pygame.image.load("img/Legionar_bily.png")
legionar_cerny=pygame.image.load("img/Legionar_cerny.png")
morovy_doktor_bily=pygame.image.load("img/Morovy_doktor_bily.png")
morovy_doktor_cerny=pygame.image.load("img/Morovy_dotkor_cerny.png")
persefona_bila=pygame.image.load("img/Persefona_bila.png")
persefona_cerna=pygame.image.load("img/Persefona_cerna.png")
valecnik_bily=pygame.image.load("img/Valecnik_bily.png")
valecnik_cerny=pygame.image.load("img/Valecnik_cerny.png")

#Nastavení pozic bílých figurek
morovy_doktor_bily_rect=morovy_doktor_bily.get_rect()
morovy_doktor_bily_rect.center=(540,120)
arcibiskup_bily_rect=arcibiskup_bily.get_rect()
arcibiskup_bily_rect.center=(660,120)
kardinal_bily_rect=kardinal_bily.get_rect()
kardinal_bily_rect.center=(780,120)
hades_bily_rect=hades_bily.get_rect()
hades_bily_rect.center=(900,120)
persefona_bila_rect=persefona_bila.get_rect()
persefona_bila_rect.center=(1020,120)
kardinal_bily_rect1=kardinal_bily.get_rect()
kardinal_bily_rect1.center=(1140,120)
arcibiskup_bily_rect1=arcibiskup_bily.get_rect()
arcibiskup_bily_rect1.center=(1260,120)
morovy_doktor_bily_rect1=morovy_doktor_bily.get_rect()
morovy_doktor_bily_rect1.center=(1380,120)
valecnik_bily_rect=valecnik_bily.get_rect()
valecnik_bily_rect.center=(540,240)
legionar_bily_rect=legionar_bily.get_rect()
legionar_bily_rect.center=(660,240)
valecnik_bily_rect1=valecnik_bily.get_rect()
valecnik_bily_rect1.center=(780,240)
legionar_bily_rect1=legionar_bily.get_rect()
legionar_bily_rect1.center=(900,240)
valecnik_bily_rect2=valecnik_bily.get_rect()
valecnik_bily_rect2.center=(1020,240)
legionar_bily_rect2=legionar_bily.get_rect()
legionar_bily_rect2.center=(1140,240)
valecnik_bily_rect3=valecnik_bily.get_rect()
valecnik_bily_rect3.center=(1260,240)
legionar_bily_rect3=legionar_bily.get_rect()
legionar_bily_rect3.center=(1380,240)

#Nastavení pozic černých figurek
morovy_doktor_cerny_rect=morovy_doktor_cerny.get_rect()
morovy_doktor_cerny_rect.center=(540,960)
arcibiskup_cerny_rect=arcibiskup_cerny.get_rect()
arcibiskup_cerny_rect.center=(660,960)
kardinal_cerny_rect=kardinal_cerny.get_rect()
kardinal_cerny_rect.center=(780,960)
hades_cerny_rect=hades_cerny.get_rect()
hades_cerny_rect.center=(900,960)
persefona_cerna_rect=persefona_cerna.get_rect()
persefona_cerna_rect.center=(1020,960)
kardinal_cerny_rect1=kardinal_cerny.get_rect()
kardinal_cerny_rect1.center=(1140,960)
arcibiskup_cerny_rect1=arcibiskup_cerny.get_rect()
arcibiskup_cerny_rect1.center=(1260,960)
morovy_doktor_cerny_rect1=morovy_doktor_cerny.get_rect()
morovy_doktor_cerny_rect1.center=(1380,960)
legionar_cerny_rect=legionar_cerny.get_rect()
legionar_cerny_rect.center=(540,840)
valecnik_cerny_rect=valecnik_cerny.get_rect()
valecnik_cerny_rect.center=(660,840)
legionar_cerny_rect1=legionar_cerny.get_rect()
legionar_cerny_rect1.center=(780,840)
valecnik_cerny_rect1=valecnik_cerny.get_rect()
valecnik_cerny_rect1.center=(900,840)
legionar_cerny_rect2=legionar_cerny.get_rect()
legionar_cerny_rect2.center=(1020,840)
valecnik_cerny_rect2=valecnik_cerny.get_rect()
valecnik_cerny_rect2.center=(1140,840)
legionar_cerny_rect3=legionar_cerny.get_rect()
legionar_cerny_rect3.center=(1260,840)
valecnik_cerny_rect3=valecnik_cerny.get_rect()
valecnik_cerny_rect3.center=(1380,840)

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
leaderboard_font=pygame.font.SysFont("georgia",50,False)
leadeboard_text_font=pygame.font.SysFont("georgia",30,False)
leaderboard_text=leaderboard_font.render("Leaderboard",True, white)
leaderboard_text_rect=leaderboard_text.get_rect()
leaderboard_text_rect.center=(1660,60)
leaderboard_background=pygame.Rect(1400,30,500,1000)

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

#Morový doktor bílý
rect_x1=morovy_doktor_bily_rect.centerx+krok
rect_y1=morovy_doktor_bily_rect.centery
rect1=pygame.Rect(rect_x1-30,rect_y1-30,60,60)

rect_x2=morovy_doktor_bily_rect.centerx+krok*2
rect_y2=morovy_doktor_bily_rect.centery
rect2=pygame.Rect(rect_x2-30,rect_y2-30,60,60)

rect_x3=morovy_doktor_bily_rect.centerx-krok
rect_y3=morovy_doktor_bily_rect.centery
rect3=pygame.Rect(rect_x3-30,rect_y3-30,60,60)

rect_x4=morovy_doktor_bily_rect.centerx-2*krok
rect_y4=morovy_doktor_bily_rect.centery
rect4=pygame.Rect(rect_x4-30,rect_y4-30,60,60)

rect_x5=morovy_doktor_bily_rect.centerx
rect_y5=morovy_doktor_bily_rect.centery+krok
rect5=pygame.Rect(rect_x5-30,rect_y5-30,60,60)

rect_x6=morovy_doktor_bily_rect.centerx
rect_y6=morovy_doktor_bily_rect.centery+krok*2
rect6=pygame.Rect(rect_x6-30,rect_y6-30,60,60)

rect_x7=morovy_doktor_bily_rect.centerx
rect_y7=morovy_doktor_bily_rect.centery+krok*3
rect7=pygame.Rect(rect_x7-30,rect_y7-30,60,60)

rect_x8=morovy_doktor_bily_rect.centerx
rect_y8=morovy_doktor_bily_rect.centery+krok*4
rect8=pygame.Rect(rect_x8-30,rect_y8-30,60,60)

rect_x9=morovy_doktor_bily_rect.centerx
rect_y9=morovy_doktor_bily_rect.centery+krok*5
rect9=pygame.Rect(rect_x9-30,rect_y9-30,60,60)

rect_x10=morovy_doktor_bily_rect.centerx
rect_y10=morovy_doktor_bily_rect.centery+krok*6
rect10=pygame.Rect(rect_x10-30,rect_y10-30,60,60)

rect_x11=morovy_doktor_bily_rect.centerx
rect_y11=morovy_doktor_bily_rect.centery+krok*7
rect11=pygame.Rect(rect_x11-30,rect_y11-30,60,60)

rect_x12=morovy_doktor_bily_rect.centerx
rect_y12=morovy_doktor_bily_rect.centery-krok
rect12=pygame.Rect(rect_x12-30,rect_y12-30,60,60)

rect_x13=morovy_doktor_bily_rect.centerx
rect_y13=morovy_doktor_bily_rect.centery-krok*2
rect13=pygame.Rect(rect_x13-30,rect_y13-30,60,60)

rect_x14=morovy_doktor_bily_rect.centerx
rect_y14=morovy_doktor_bily_rect.centery-krok*3
rect14=pygame.Rect(rect_x14-30,rect_y14-30,60,60)

rect_x15=morovy_doktor_bily_rect.centerx
rect_y15=morovy_doktor_bily_rect.centery-krok*4
rect15=pygame.Rect(rect_x15-30,rect_y15-30,60,60)

rect_x16=morovy_doktor_bily_rect.centerx
rect_y16=morovy_doktor_bily_rect.centery-krok*5
rect16=pygame.Rect(rect_x16-30,rect_y16-30,60,60)

rect_x17=morovy_doktor_bily_rect.centerx
rect_y17=morovy_doktor_bily_rect.centery-krok*6
rect17=pygame.Rect(rect_x17-30,rect_y17-30,60,60)

rect_x18=morovy_doktor_bily_rect.centerx
rect_y18=morovy_doktor_bily_rect.centery-krok*7
rect18=pygame.Rect(rect_x18-30,rect_y18-30,60,60)

ctverce_morovy_doktor_bily=[rect1,rect2,rect3,rect4,rect5,rect6,rect7,rect8,rect9,rect10,rect11,rect12,rect13,rect14,rect15,rect16,rect17,rect18]

#Arcibiskup bílý
rect_x19=arcibiskup_bily_rect.centerx+krok*2
rect_y19=arcibiskup_bily_rect.centery
rect19=pygame.Rect(rect_x19-30,rect_y19-30,60,60)

rect_x20=arcibiskup_bily_rect.centerx+krok*2
rect_y20=arcibiskup_bily_rect.centery+krok
rect20=pygame.Rect(rect_x20-30,rect_y20-30,60,60)

rect_x21=arcibiskup_bily_rect.centerx+krok*2
rect_y21=arcibiskup_bily_rect.centery-krok
rect21=pygame.Rect(rect_x21-30,rect_y21-30,60,60)

rect_x22=arcibiskup_bily_rect.centerx-krok*2
rect_y22=arcibiskup_bily_rect.centery
rect22=pygame.Rect(rect_x22-30,rect_y22-30,60,60)

rect_x23=arcibiskup_bily_rect.centerx-krok*2
rect_y23=arcibiskup_bily_rect.centery+krok
rect23=pygame.Rect(rect_x23-30,rect_y23-30,60,60)

rect_x24=arcibiskup_bily_rect.centerx-krok*2
rect_y24=arcibiskup_bily_rect.centery-krok
rect24=pygame.Rect(rect_x24-30,rect_y24-30,60,60)

rect_x25=arcibiskup_bily_rect.centerx
rect_y25=arcibiskup_bily_rect.centery+krok*2
rect25=pygame.Rect(rect_x25-30,rect_y25-30,60,60)

rect_x26=arcibiskup_bily_rect.centerx+krok
rect_y26=arcibiskup_bily_rect.centery+krok*2
rect26=pygame.Rect(rect_x26-30,rect_y26-30,60,60)

rect_x27=arcibiskup_bily_rect.centerx-krok
rect_y27=arcibiskup_bily_rect.centery+krok*2
rect27=pygame.Rect(rect_x27-30,rect_y27-30,60,60)

rect_x28=arcibiskup_bily_rect.centerx
rect_y28=arcibiskup_bily_rect.centery-krok*2
rect28=pygame.Rect(rect_x28-30,rect_y28-30,60,60)

rect_x29=arcibiskup_bily_rect.centerx+krok
rect_y29=arcibiskup_bily_rect.centery-krok*2
rect29=pygame.Rect(rect_x29-30,rect_y29-30,60,60)

rect_x30=arcibiskup_bily_rect.centerx-krok
rect_y30=arcibiskup_bily_rect.centery-krok*2
rect30=pygame.Rect(rect_x30-30,rect_y30-30,60,60)

ctverce_arcibiskup_bily=[rect19,rect20,rect21,rect22,rect23,rect24,rect25,rect26,rect27,rect28,rect29,rect30]

#Kardinál bílý
rect_x31=kardinal_bily_rect.centerx+krok
rect_y31=kardinal_bily_rect.centery-krok
rect31=pygame.Rect(rect_x31-30,rect_y31-30,60,60)

rect_x32=kardinal_bily_rect.centerx-krok
rect_y32=kardinal_bily_rect.centery-krok
rect32=pygame.Rect(rect_x32-30,rect_y32-30,60,60)

rect_x33=kardinal_bily_rect.centerx+krok
rect_y33=kardinal_bily_rect.centery+krok
rect33=pygame.Rect(rect_x33-30,rect_y33-30,60,60)

rect_x34=kardinal_bily_rect.centerx-krok
rect_y34=kardinal_bily_rect.centery+krok
rect34=pygame.Rect(rect_x34-30,rect_y34-30,60,60)

ctverce_kardinal_bily=[rect31,rect32,rect33,rect34]

#Hádes bílý
rect_x35=hades_bily_rect.centerx
rect_y35=hades_bily_rect.centery-krok
rect35=pygame.Rect(rect_x35-30,rect_y35-30,60,60)

rect_x36=hades_bily_rect.centerx
rect_y36=hades_bily_rect.centery-krok*2
rect36=pygame.Rect(rect_x36-30,rect_y36-30,60,60)

rect_x37=hades_bily_rect.centerx
rect_y37=hades_bily_rect.centery-krok*3
rect37=pygame.Rect(rect_x37-30,rect_y37-30,60,60)

rect_x38=hades_bily_rect.centerx+krok
rect_y38=hades_bily_rect.centery-krok
rect38=pygame.Rect(rect_x38-30,rect_y38-30,60,60)

rect_x39=hades_bily_rect.centerx+krok*2
rect_y39=hades_bily_rect.centery-krok*2
rect39=pygame.Rect(rect_x39-30,rect_y39-30,60,60)

rect_x40=hades_bily_rect.centerx+krok*3
rect_y40=hades_bily_rect.centery-krok*3
rect40=pygame.Rect(rect_x40-30,rect_y40-30,60,60)

rect_x41=hades_bily_rect.centerx+krok
rect_y41=hades_bily_rect.centery
rect41=pygame.Rect(rect_x41-30,rect_y41-30,60,60)

rect_x42=hades_bily_rect.centerx+krok*2
rect_y42=hades_bily_rect.centery
rect42=pygame.Rect(rect_x42-30,rect_y42-30,60,60)

rect_x43=hades_bily_rect.centerx+krok*3
rect_y43=hades_bily_rect.centery
rect43=pygame.Rect(rect_x43-30,rect_y43-30,60,60)

rect_x44=hades_bily_rect.centerx+krok
rect_y44=hades_bily_rect.centery+krok
rect44=pygame.Rect(rect_x44-30,rect_y44-30,60,60)

rect_x45=hades_bily_rect.centerx+krok*2
rect_y45=hades_bily_rect.centery+krok*2
rect45=pygame.Rect(rect_x45-30,rect_y45-30,60,60)

rect_x46=hades_bily_rect.centerx-krok
rect_y46=hades_bily_rect.centery-krok
rect46=pygame.Rect(rect_x46-30,rect_y46-30,60,60)

rect_x47=hades_bily_rect.centerx-krok*2
rect_y47=hades_bily_rect.centery-krok*2
rect47=pygame.Rect(rect_x47-30,rect_y47-30,60,60)

rect_x48=hades_bily_rect.centerx-krok*3
rect_y48=hades_bily_rect.centery-krok*3
rect48=pygame.Rect(rect_x48-30,rect_y48-30,60,60)

rect_x49=hades_bily_rect.centerx-krok
rect_y49=hades_bily_rect.centery
rect49=pygame.Rect(rect_x49-30,rect_y49-30,60,60)

rect_x50=hades_bily_rect.centerx-krok*2
rect_y50=hades_bily_rect.centery
rect50=pygame.Rect(rect_x50-30,rect_y50-30,60,60)

rect_x51=hades_bily_rect.centerx-krok*3
rect_y51=hades_bily_rect.centery
rect51=pygame.Rect(rect_x51-30,rect_y51-30,60,60)

rect_x52=hades_bily_rect.centerx-krok
rect_y52=hades_bily_rect.centery+krok
rect52=pygame.Rect(rect_x52-30,rect_y52-30,60,60)

rect_x53=hades_bily_rect.centerx-krok*2
rect_y53=hades_bily_rect.centery+krok*2
rect53=pygame.Rect(rect_x53-30,rect_y53-30,60,60)

ctverce_hades_bily=[rect35,rect36,rect37,rect38,rect39,rect40,rect41,rect42,rect43,rect44,rect45,rect46,rect47,rect48,rect49,rect50,rect51,rect52,rect53]

#Persefona bílá
ctverce_persefona_bila=[]

rect_per_x1=persefona_bila_rect.centerx+krok
rect_per_y1=persefona_bila_rect.centery
rect_per_1=pygame.Rect(rect_per_x1-30,rect_per_y1-30,60,60)
ctverce_persefona_bila.append(rect_per_1)

rect_per_x2=persefona_bila_rect.centerx+krok
rect_per_y2=persefona_bila_rect.centery-krok
rect_per_2=pygame.Rect(rect_per_x2-30,rect_per_y2-30,60,60)
ctverce_persefona_bila.append(rect_per_2)

rect_per_x3=persefona_bila_rect.centerx
rect_per_y3=persefona_bila_rect.centery-krok
rect_per_3=pygame.Rect(rect_per_x3-30,rect_per_y3-30,60,60)
ctverce_persefona_bila.append(rect_per_3)

rect_per_x4=persefona_bila_rect.centerx-krok
rect_per_y4=persefona_bila_rect.centery-krok
rect_per_4=pygame.Rect(rect_per_x4-30,rect_per_y4-30,60,60)
ctverce_persefona_bila.append(rect_per_4)

rect_per_x5=persefona_bila_rect.centerx-krok
rect_per_y5=persefona_bila_rect.centery
rect_per_5=pygame.Rect(rect_per_x5-30,rect_per_y5-30,60,60)
ctverce_persefona_bila.append(rect_per_5)

rect_per_x6=persefona_bila_rect.centerx-krok
rect_per_y6=persefona_bila_rect.centery+krok
rect_per_6=pygame.Rect(rect_per_x6-30,rect_per_y6-30,60,60)
ctverce_persefona_bila.append(rect_per_6)

rect_per_x7=persefona_bila_rect.centerx
rect_per_y7=persefona_bila_rect.centery+krok
rect_per_7=pygame.Rect(rect_per_x7-30,rect_per_y7-30,60,60)
ctverce_persefona_bila.append(rect_per_7)

rect_per_x8=persefona_bila_rect.centerx
rect_per_y8=persefona_bila_rect.centery+krok
rect_per_8=pygame.Rect(rect_per_x8-30,rect_per_y8-30,60,60)
ctverce_persefona_bila.append(rect_per_8)

rect_per_x9=persefona_bila_rect.centerx+krok
rect_per_y9=persefona_bila_rect.centery+krok
rect_per_9=pygame.Rect(rect_per_x9-30,rect_per_y9-30,60,60)
ctverce_persefona_bila.append(rect_per_9)

#Kardinál bílý 1
ctverce_kardinal_bily_1=[]

rect_kar_x1=kardinal_bily_rect1.centerx+krok
rect_kar_y1=kardinal_bily_rect1.centery-krok
rect_kar_1=pygame.Rect(rect_kar_x1-30,rect_kar_y1-30,60,60)
ctverce_kardinal_bily_1.append(rect_kar_1)

rect_kar_x2=kardinal_bily_rect1.centerx+krok
rect_kar_y2=kardinal_bily_rect1.centery+krok
rect_kar_2=pygame.Rect(rect_kar_x2-30,rect_kar_y2-30,60,60)
ctverce_kardinal_bily_1.append(rect_kar_2)

rect_kar_x3=kardinal_bily_rect1.centerx-krok
rect_kar_y3=kardinal_bily_rect1.centery-krok
rect_kar_3=pygame.Rect(rect_kar_x3-30,rect_kar_y3-30,60,60)
ctverce_kardinal_bily_1.append(rect_kar_3)

rect_kar_x4=kardinal_bily_rect1.centerx-krok
rect_kar_y4=kardinal_bily_rect1.centery+krok
rect_kar_4=pygame.Rect(rect_kar_x4-30,rect_kar_y4-30,60,60)
ctverce_kardinal_bily_1.append(rect_kar_4)

#Arcibiskup bílý 1
ctverce_arcibiskup_bily_1=[]

rect_arc_x1=arcibiskup_bily_rect1.centerx+krok*2
rect_arc_y1=arcibiskup_bily_rect1.centery
rect_arc_1=pygame.Rect(rect_arc_x1-30,rect_arc_y1-30,60,60)
ctverce_arcibiskup_bily_1.append(rect_arc_1)

rect_arc_x2=arcibiskup_bily_rect1.centerx+krok*2
rect_arc_y2=arcibiskup_bily_rect1.centery-krok
rect_arc_2=pygame.Rect(rect_arc_x2-30,rect_arc_y2-30,60,60)
ctverce_arcibiskup_bily_1.append(rect_arc_2)

rect_arc_x3=arcibiskup_bily_rect1.centerx+krok*2
rect_arc_y3=arcibiskup_bily_rect1.centery+krok
rect_arc_3=pygame.Rect(rect_arc_x3-30,rect_arc_y3-30,60,60)
ctverce_arcibiskup_bily_1.append(rect_arc_3)

rect_arc_x4=arcibiskup_bily_rect1.centerx
rect_arc_y4=arcibiskup_bily_rect1.centery+krok*2
rect_arc_4=pygame.Rect(rect_arc_x4-30,rect_arc_y4-30,60,60)
ctverce_arcibiskup_bily_1.append(rect_arc_4)

rect_arc_x5=arcibiskup_bily_rect1.centerx+krok
rect_arc_y5=arcibiskup_bily_rect1.centery+krok*2
rect_arc_5=pygame.Rect(rect_arc_x5-30,rect_arc_y5-30,60,60)
ctverce_arcibiskup_bily_1.append(rect_arc_5)

rect_arc_x6=arcibiskup_bily_rect1.centerx-krok
rect_arc_y6=arcibiskup_bily_rect1.centery+krok*2
rect_arc_6=pygame.Rect(rect_arc_x6-30,rect_arc_y6-30,60,60)
ctverce_arcibiskup_bily_1.append(rect_arc_6)

rect_arc_x7=arcibiskup_bily_rect1.centerx-krok*2
rect_arc_y7=arcibiskup_bily_rect1.centery
rect_arc_7=pygame.Rect(rect_arc_x7-30,rect_arc_y7-30,60,60)
ctverce_arcibiskup_bily_1.append(rect_arc_7)

rect_arc_x8=arcibiskup_bily_rect1.centerx-krok*2
rect_arc_y8=arcibiskup_bily_rect1.centery-krok
rect_arc_8=pygame.Rect(rect_arc_x8-30,rect_arc_y8-30,60,60)
ctverce_arcibiskup_bily_1.append(rect_arc_8)

rect_arc_x9=arcibiskup_bily_rect1.centerx-krok*2
rect_arc_y9=arcibiskup_bily_rect1.centery+krok
rect_arc_9=pygame.Rect(rect_arc_x9-30,rect_arc_y9-30,60,60)
ctverce_arcibiskup_bily_1.append(rect_arc_9)

rect_arc_x10=arcibiskup_bily_rect1.centerx
rect_arc_y10=arcibiskup_bily_rect1.centery-krok*2
rect_arc_10=pygame.Rect(rect_arc_x10-30,rect_arc_y10-30,60,60)
ctverce_arcibiskup_bily_1.append(rect_arc_10)

rect_arc_x11=arcibiskup_bily_rect1.centerx+krok
rect_arc_y11=arcibiskup_bily_rect1.centery-krok*2
rect_arc_11=pygame.Rect(rect_arc_x11-30,rect_arc_y11-30,60,60)
ctverce_arcibiskup_bily_1.append(rect_arc_11)

rect_arc_x12=arcibiskup_bily_rect1.centerx-krok
rect_arc_y12=arcibiskup_bily_rect1.centery-krok*2
rect_arc_12=pygame.Rect(rect_arc_x12-30,rect_arc_y12-30,60,60)
ctverce_arcibiskup_bily_1.append(rect_arc_12)

#Morový doktor bílý 1
ctverce_morovy_doktor_bily_1=[]

rect_mor_x1=morovy_doktor_bily_rect1.centerx
rect_mor_y1=morovy_doktor_bily_rect1.centery+krok
rect_mor_1=pygame.Rect(rect_mor_x1-30,rect_mor_y1-30,60,60)
ctverce_morovy_doktor_bily_1.append(rect_mor_1)

rect_mor_x2=morovy_doktor_bily_rect1.centerx
rect_mor_y2=morovy_doktor_bily_rect1.centery+krok*2
rect_mor_2=pygame.Rect(rect_mor_x2-30,rect_mor_y2-30,60,60)
ctverce_morovy_doktor_bily_1.append(rect_mor_2)

rect_mor_x3=morovy_doktor_bily_rect1.centerx
rect_mor_y3=morovy_doktor_bily_rect1.centery+krok*3
rect_mor_3=pygame.Rect(rect_mor_x3-30,rect_mor_y3-30,60,60)
ctverce_morovy_doktor_bily_1.append(rect_mor_3)

rect_mor_x4=morovy_doktor_bily_rect1.centerx
rect_mor_y4=morovy_doktor_bily_rect1.centery+krok*4
rect_mor_4=pygame.Rect(rect_mor_x4-30,rect_mor_y4-30,60,60)
ctverce_morovy_doktor_bily_1.append(rect_mor_4)

rect_mor_x5=morovy_doktor_bily_rect1.centerx
rect_mor_y5=morovy_doktor_bily_rect1.centery+krok*5
rect_mor_5=pygame.Rect(rect_mor_x5-30,rect_mor_y5-30,60,60)
ctverce_morovy_doktor_bily_1.append(rect_mor_5)

rect_mor_x6=morovy_doktor_bily_rect1.centerx
rect_mor_y6=morovy_doktor_bily_rect1.centery+krok*6
rect_mor_6=pygame.Rect(rect_mor_x6-30,rect_mor_y6-30,60,60)
ctverce_morovy_doktor_bily_1.append(rect_mor_6)

rect_mor_x7=morovy_doktor_bily_rect1.centerx
rect_mor_y7=morovy_doktor_bily_rect1.centery+krok*7
rect_mor_7=pygame.Rect(rect_mor_x7-30,rect_mor_y7-30,60,60)
ctverce_morovy_doktor_bily_1.append(rect_mor_7)

rect_mor_x8=morovy_doktor_bily_rect1.centerx
rect_mor_y8=morovy_doktor_bily_rect1.centery-krok
rect_mor_8=pygame.Rect(rect_mor_x8-30,rect_mor_y8-30,60,60)
ctverce_morovy_doktor_bily_1.append(rect_mor_8)

rect_mor_x9=morovy_doktor_bily_rect1.centerx
rect_mor_y9=morovy_doktor_bily_rect1.centery-krok*2
rect_mor_9=pygame.Rect(rect_mor_x9-30,rect_mor_y9-30,60,60)
ctverce_morovy_doktor_bily_1.append(rect_mor_9)

rect_mor_x10=morovy_doktor_bily_rect1.centerx
rect_mor_y10=morovy_doktor_bily_rect1.centery-krok*3
rect_mor_10=pygame.Rect(rect_mor_x10-30,rect_mor_y10-30,60,60)
ctverce_morovy_doktor_bily_1.append(rect_mor_10)

rect_mor_x11=morovy_doktor_bily_rect1.centerx
rect_mor_y11=morovy_doktor_bily_rect1.centery-krok*4
rect_mor_11=pygame.Rect(rect_mor_x11-30,rect_mor_y11-30,60,60)
ctverce_morovy_doktor_bily_1.append(rect_mor_11)

rect_mor_x12=morovy_doktor_bily_rect1.centerx
rect_mor_y12=morovy_doktor_bily_rect1.centery-krok*5
rect_mor_12=pygame.Rect(rect_mor_x12-30,rect_mor_y12-30,60,60)
ctverce_morovy_doktor_bily_1.append(rect_mor_12)

rect_mor_x13=morovy_doktor_bily_rect1.centerx
rect_mor_y13=morovy_doktor_bily_rect1.centery-krok*6
rect_mor_13=pygame.Rect(rect_mor_x13-30,rect_mor_y13-30,60,60)
ctverce_morovy_doktor_bily_1.append(rect_mor_13)

rect_mor_x14=morovy_doktor_bily_rect1.centerx
rect_mor_y14=morovy_doktor_bily_rect1.centery-krok*7
rect_mor_14=pygame.Rect(rect_mor_x14-30,rect_mor_y14-30,60,60)
ctverce_morovy_doktor_bily_1.append(rect_mor_14)

rect_mor_x15=morovy_doktor_bily_rect1.centerx+krok
rect_mor_y15=morovy_doktor_bily_rect1.centery
rect_mor_15=pygame.Rect(rect_mor_x15-30,rect_mor_y15-30,60,60)
ctverce_morovy_doktor_bily_1.append(rect_mor_15)

rect_mor_x16=morovy_doktor_bily_rect1.centerx+krok*2
rect_mor_y16=morovy_doktor_bily_rect1.centery
rect_mor_16=pygame.Rect(rect_mor_x16-30,rect_mor_y16-30,60,60)
ctverce_morovy_doktor_bily_1.append(rect_mor_16)

rect_mor_x17=morovy_doktor_bily_rect1.centerx-krok
rect_mor_y17=morovy_doktor_bily_rect1.centery
rect_mor_17=pygame.Rect(rect_mor_x17-30,rect_mor_y17-30,60,60)
ctverce_morovy_doktor_bily_1.append(rect_mor_17)

rect_mor_x18=morovy_doktor_bily_rect1.centerx-krok*2
rect_mor_y18=morovy_doktor_bily_rect1.centery
rect_mor_18=pygame.Rect(rect_mor_x18-30,rect_mor_y18-30,60,60)
ctverce_morovy_doktor_bily_1.append(rect_mor_18)

#Válečník bílý 1
ctverce_valecnik_bily=[]

rect_val_x1=valecnik_bily_rect.centerx+krok
rect_val_y1=valecnik_bily_rect.centery
rect_val_1=pygame.Rect(rect_val_x1-30,rect_val_y1-30,60,60)
ctverce_valecnik_bily.append(rect_val_1)

rect_val_x2=valecnik_bily_rect.centerx-krok
rect_val_y2=valecnik_bily_rect.centery
rect_val_2=pygame.Rect(rect_val_x2-30,rect_val_y2-30,60,60)
ctverce_valecnik_bily.append(rect_val_2)

rect_val_x3=valecnik_bily_rect.centerx
rect_val_y3=valecnik_bily_rect.centery+krok
rect_val_3=pygame.Rect(rect_val_x3-30,rect_val_y3-30,60,60)
ctverce_valecnik_bily.append(rect_val_3)

rect_val_x4=valecnik_bily_rect.centerx
rect_val_y4=valecnik_bily_rect.centery-krok
rect_val_4=pygame.Rect(rect_val_x4-30,rect_val_y4-30,60,60)
ctverce_valecnik_bily.append(rect_val_4)

#Legionář bílý 1
ctverce_legionar_bily=[]

rect_leg_x1=legionar_bily_rect.centerx+krok
rect_leg_y1=legionar_bily_rect.centery+krok
rect_leg_1=pygame.Rect(rect_leg_x1-30,rect_leg_y1-30,60,60)
ctverce_legionar_bily.append(rect_leg_1)

rect_leg_x2=legionar_bily_rect.centerx
rect_leg_y2=legionar_bily_rect.centery+krok
rect_leg_2=pygame.Rect(rect_leg_x2-30,rect_leg_y2-30,60,60)
ctverce_legionar_bily.append(rect_leg_2)

rect_leg_x3=legionar_bily_rect.centerx-krok
rect_leg_y3=legionar_bily_rect.centery+krok
rect_leg_3=pygame.Rect(rect_leg_x3-30,rect_leg_y3-30,60,60)
ctverce_legionar_bily.append(rect_leg_3)

#Válečník bílý 2
ctverce_valecnik_bily_1=[]

rect_val_1_x1=valecnik_bily_rect1.centerx+krok
rect_val_1_y1=valecnik_bily_rect1.centery
rect_val_1_1=pygame.Rect(rect_val_1_x1-30,rect_val_1_y1-30,60,60)
ctverce_valecnik_bily_1.append(rect_val_1_1)

rect_val_1_x2=valecnik_bily_rect1.centerx-krok
rect_val_1_y2=valecnik_bily_rect1.centery
rect_val_1_2=pygame.Rect(rect_val_1_x2-30,rect_val_1_y2-30,60,60)
ctverce_valecnik_bily_1.append(rect_val_1_2)

rect_val_1_x3=valecnik_bily_rect1.centerx
rect_val_1_y3=valecnik_bily_rect1.centery+krok
rect_val_1_3=pygame.Rect(rect_val_1_x3-30,rect_val_1_y3-30,60,60)
ctverce_valecnik_bily_1.append(rect_val_1_3)

rect_val_1_x4=valecnik_bily_rect1.centerx
rect_val_1_y4=valecnik_bily_rect1.centery-krok
rect_val_1_4=pygame.Rect(rect_val_1_x4-30,rect_val_1_y4-30,60,60)
ctverce_valecnik_bily_1.append(rect_val_1_4)

#Legionář bílý 2
ctverce_legionar_bily_1=[]

rect_leg_1_x1=legionar_bily_rect1.centerx+krok
rect_leg_1_y1=legionar_bily_rect1.centery+krok
rect_leg_1_1=pygame.Rect(rect_leg_1_x1-30,rect_leg_1_y1-30,60,60)
ctverce_legionar_bily_1.append(rect_leg_1_1)

rect_leg_1_x2=legionar_bily_rect1.centerx
rect_leg_1_y2=legionar_bily_rect1.centery+krok
rect_leg_1_2=pygame.Rect(rect_leg_1_x2-30,rect_leg_1_y2-30,60,60)
ctverce_legionar_bily_1.append(rect_leg_1_2)

rect_leg_1_x3=legionar_bily_rect1.centerx-krok
rect_leg_1_y3=legionar_bily_rect1.centery+krok
rect_leg_1_3=pygame.Rect(rect_leg_1_x3-30,rect_leg_1_y3-30,60,60)
ctverce_legionar_bily_1.append(rect_leg_1_3)

#Válečník bílý 3
ctverce_valecnik_bily_2=[]

rect_val_2_x1=valecnik_bily_rect2.centerx+krok
rect_val_2_y1=valecnik_bily_rect2.centery
rect_val_2_1=pygame.Rect(rect_val_2_x1-30,rect_val_2_y1-30,60,60)
ctverce_valecnik_bily_2.append(rect_val_2_1)

rect_val_2_x2=valecnik_bily_rect2.centerx-krok
rect_val_2_y2=valecnik_bily_rect2.centery
rect_val_2_2=pygame.Rect(rect_val_2_x2-30,rect_val_2_y2-30,60,60)
ctverce_valecnik_bily_2.append(rect_val_2_2)

rect_val_2_x3=valecnik_bily_rect2.centerx
rect_val_2_y3=valecnik_bily_rect2.centery+krok
rect_val_2_3=pygame.Rect(rect_val_2_x3-30,rect_val_2_y3-30,60,60)
ctverce_valecnik_bily_2.append(rect_val_2_3)

rect_val_2_x4=valecnik_bily_rect2.centerx
rect_val_2_y4=valecnik_bily_rect2.centery-krok
rect_val_2_4=pygame.Rect(rect_val_2_x4-30,rect_val_2_y4-30,60,60)
ctverce_valecnik_bily_2.append(rect_val_2_4)

#Legionář bílý 3
ctverce_legionar_bily_2=[]

rect_leg_2_x1=legionar_bily_rect2.centerx+krok
rect_leg_2_y1=legionar_bily_rect2.centery+krok
rect_leg_2_1=pygame.Rect(rect_leg_2_x1-30,rect_leg_2_y1-30,60,60)
ctverce_legionar_bily_2.append(rect_leg_2_1)

rect_leg_2_x2=legionar_bily_rect2.centerx
rect_leg_2_y2=legionar_bily_rect2.centery+krok
rect_leg_2_2=pygame.Rect(rect_leg_2_x2-30,rect_leg_2_y2-30,60,60)
ctverce_legionar_bily_2.append(rect_leg_2_2)

rect_leg_2_x3=legionar_bily_rect2.centerx-krok
rect_leg_2_y3=legionar_bily_rect2.centery+krok
rect_leg_2_3=pygame.Rect(rect_leg_2_x3-30,rect_leg_2_y3-30,60,60)
ctverce_legionar_bily_2.append(rect_leg_2_3)

#Válečník bílý 4
ctverce_valecnik_bily_3=[]

rect_val_3_x1=valecnik_bily_rect3.centerx+krok
rect_val_3_y1=valecnik_bily_rect3.centery
rect_val_3_1=(rect_val_3_x1-30,rect_val_3_y1-30,60,60)
ctverce_valecnik_bily_3.append(rect_val_3_1)

rect_val_3_x2=valecnik_bily_rect3.centerx-krok
rect_val_3_y2=valecnik_bily_rect3.centery
rect_val_3_2=(rect_val_3_x2-30,rect_val_3_y2-30,60,60)
ctverce_valecnik_bily_3.append(rect_val_3_2)

rect_val_3_x3=valecnik_bily_rect3.centerx
rect_val_3_y3=valecnik_bily_rect3.centery+krok
rect_val_3_3=(rect_val_3_x3-30,rect_val_3_y3-30,60,60)
ctverce_valecnik_bily_3.append(rect_val_3_3)

rect_val_3_x4=valecnik_bily_rect3.centerx
rect_val_3_y4=valecnik_bily_rect3.centery-krok
rect_val_3_4=(rect_val_3_x4-30,rect_val_3_y4-30,60,60)
ctverce_valecnik_bily_3.append(rect_val_3_4)

#Legionář bílý 4
ctverce_legionar_bily_3=[]

rect_leg_3_x1=legionar_bily_rect3.centerx+krok
rect_leg_3_y1=legionar_bily_rect3.centery+krok
rect_leg_3_1=pygame.Rect(rect_leg_3_x1-30,rect_leg_3_y1-30,60,60)
ctverce_legionar_bily_3.append(rect_leg_3_1)

rect_leg_3_x2=legionar_bily_rect3.centerx
rect_leg_3_y2=legionar_bily_rect3.centery+krok
rect_leg_3_2=pygame.Rect(rect_leg_3_x2-30,rect_leg_3_y2-30,60,60)
ctverce_legionar_bily_3.append(rect_leg_3_1)

rect_leg_3_x3=legionar_bily_rect3.centerx-krok
rect_leg_3_y3=legionar_bily_rect3.centery+krok
rect_leg_3_3=pygame.Rect(rect_leg_3_x3-30,rect_leg_3_y3-30,60,60)
ctverce_legionar_bily_3.append(rect_leg_3_3)

#Morový doktor černý 1


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
                    conn = mysql.connector.connect(
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
                    conn.close()
            
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
        pygame.draw.rect(screen,black,leaderboard_background)
        screen.blit(leaderboard_text,leaderboard_text_rect)

        #Vypsání dat pro leadeboard
        y=100
        for row in result:
            text=", ".join(str(item) for item in row)
            text_surface=leadeboard_text_font.render(text,True, white)
            print(text_surface)
            screen.blit(text_surface, (1580,y))
            y+=40  

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

        screen.blit(morovy_doktor_bily,morovy_doktor_bily_rect)
        screen.blit(arcibiskup_bily,arcibiskup_bily_rect)
        screen.blit(kardinal_bily,kardinal_bily_rect)
        screen.blit(hades_bily,hades_bily_rect)
        screen.blit(persefona_bila,persefona_bila_rect)
        screen.blit(kardinal_bily,kardinal_bily_rect1)
        screen.blit(arcibiskup_bily,arcibiskup_bily_rect1)
        screen.blit(morovy_doktor_bily,morovy_doktor_bily_rect1)
        screen.blit(legionar_bily,legionar_bily_rect)
        screen.blit(valecnik_bily,valecnik_bily_rect)
        screen.blit(legionar_bily,legionar_bily_rect1)
        screen.blit(valecnik_bily,valecnik_bily_rect1)
        screen.blit(legionar_bily,legionar_bily_rect2)
        screen.blit(valecnik_bily,valecnik_bily_rect2)
        screen.blit(legionar_bily,legionar_bily_rect3)
        screen.blit(valecnik_bily,valecnik_bily_rect3)

        screen.blit(morovy_doktor_cerny,morovy_doktor_cerny_rect)
        screen.blit(arcibiskup_cerny,arcibiskup_cerny_rect)
        screen.blit(kardinal_cerny,kardinal_cerny_rect)
        screen.blit(hades_cerny,hades_cerny_rect)
        screen.blit(persefona_cerna,persefona_cerna_rect)
        screen.blit(kardinal_cerny,kardinal_cerny_rect1)
        screen.blit(arcibiskup_cerny,arcibiskup_cerny_rect1)
        screen.blit(morovy_doktor_cerny,morovy_doktor_cerny_rect1)
        screen.blit(legionar_cerny,legionar_cerny_rect)
        screen.blit(valecnik_cerny,valecnik_cerny_rect)
        screen.blit(legionar_cerny,legionar_cerny_rect1)
        screen.blit(valecnik_cerny,valecnik_cerny_rect1)
        screen.blit(legionar_cerny,legionar_cerny_rect2)
        screen.blit(valecnik_cerny,valecnik_cerny_rect2)
        screen.blit(legionar_cerny,legionar_cerny_rect3)
        screen.blit(valecnik_cerny,valecnik_cerny_rect3)

        

        #figurky_bile=[morovy_doktor_bily_rect,arcibiskup_bily_rect,kardinal_bily_rect,hades_bily_rect,persefona_bila_rect,kardinal_bily_rect1,arcibiskup_bily_rect1,morovy_doktor_bily_rect1,legionar_bily_rect,valecnik_bily_rect,legionar_bily_rect1,valecnik_bily_rect1,legionar_bily_rect2,valecnik_bily_rect2,legionar_bily_rect3,valecnik_bily_rect3]
        #figurky_cerne=[morovy_doktor_cerny_rect,arcibiskup_cerny_rect,kardinal_cerny_rect,hades_cerny_rect,persefona_cerna_rect,kardinal_bily_rect1,arcibiskup_cerny_rect1,morovy_doktor_cerny_rect1,legionar_cerny_rect,valecnik_cerny_rect,legionar_cerny_rect1,valecnik_cerny_rect1,legionar_cerny_rect2,valecnik_cerny_rect2,legionar_cerny_rect3,valecnik_cerny_rect3]
        #Tažení figurek, todo: omezit jejich pohyb na schéma tažení
        
        
        if not pohyb:
            morovy_doktor_bily_x_pred=morovy_doktor_bily_rect.centerx
            morovy_doktor_bily_y_pred=morovy_doktor_bily_rect.centery
            
            rect_x1=morovy_doktor_bily_rect.centerx+krok
            rect_y1=morovy_doktor_bily_rect.centery
            rect1=pygame.Rect(rect_x1-30,rect_y1-30,60,60)

            rect_x2=morovy_doktor_bily_rect.centerx+krok*2
            rect_y2=morovy_doktor_bily_rect.centery
            rect2=pygame.Rect(rect_x2-30,rect_y2-30,60,60)

            rect_x3=morovy_doktor_bily_rect.centerx-krok
            rect_y3=morovy_doktor_bily_rect.centery
            rect3=pygame.Rect(rect_x3-30,rect_y3-30,60,60)

            rect_x4=morovy_doktor_bily_rect.centerx-2*krok
            rect_y4=morovy_doktor_bily_rect.centery
            rect4=pygame.Rect(rect_x4-30,rect_y4-30,60,60)

            rect_x5=morovy_doktor_bily_rect.centerx
            rect_y5=morovy_doktor_bily_rect.centery+krok
            rect5=pygame.Rect(rect_x5-30,rect_y5-30,60,60)

            rect_x6=morovy_doktor_bily_rect.centerx
            rect_y6=morovy_doktor_bily_rect.centery+krok*2
            rect6=pygame.Rect(rect_x6-30,rect_y6-30,60,60)

            rect_x7=morovy_doktor_bily_rect.centerx
            rect_y7=morovy_doktor_bily_rect.centery+krok*3
            rect7=pygame.Rect(rect_x7-30,rect_y7-30,60,60)

            rect_x8=morovy_doktor_bily_rect.centerx
            rect_y8=morovy_doktor_bily_rect.centery+krok*4
            rect8=pygame.Rect(rect_x8-30,rect_y8-30,60,60)

            rect_x9=morovy_doktor_bily_rect.centerx
            rect_y9=morovy_doktor_bily_rect.centery+krok*5
            rect9=pygame.Rect(rect_x9-30,rect_y9-30,60,60)

            rect_x10=morovy_doktor_bily_rect.centerx
            rect_y10=morovy_doktor_bily_rect.centery+krok*6
            rect10=pygame.Rect(rect_x10-30,rect_y10-30,60,60)

            rect_x11=morovy_doktor_bily_rect.centerx
            rect_y11=morovy_doktor_bily_rect.centery+krok*7
            rect11=pygame.Rect(rect_x11-30,rect_y11-30,60,60)

            rect_x12=morovy_doktor_bily_rect.centerx
            rect_y12=morovy_doktor_bily_rect.centery-krok
            rect12=pygame.Rect(rect_x12-30,rect_y12-30,60,60)

            rect_x13=morovy_doktor_bily_rect.centerx
            rect_y13=morovy_doktor_bily_rect.centery-krok*2
            rect13=pygame.Rect(rect_x13-30,rect_y13-30,60,60)

            rect_x14=morovy_doktor_bily_rect.centerx
            rect_y14=morovy_doktor_bily_rect.centery-krok*3
            rect14=pygame.Rect(rect_x14-30,rect_y14-30,60,60)

            rect_x15=morovy_doktor_bily_rect.centerx
            rect_y15=morovy_doktor_bily_rect.centery-krok*4
            rect15=pygame.Rect(rect_x15-30,rect_y15-30,60,60)

            rect_x16=morovy_doktor_bily_rect.centerx
            rect_y16=morovy_doktor_bily_rect.centery-krok*5
            rect16=pygame.Rect(rect_x16-30,rect_y16-30,60,60)

            rect_x17=morovy_doktor_bily_rect.centerx
            rect_y17=morovy_doktor_bily_rect.centery-krok*6
            rect17=pygame.Rect(rect_x17-30,rect_y17-30,60,60)

            rect_x18=morovy_doktor_bily_rect.centerx
            rect_y18=morovy_doktor_bily_rect.centery-krok*7
            rect18=pygame.Rect(rect_x18-30,rect_y18-30,60,60)

            ctverce_morovy_doktor_bily=[rect1,rect2,rect3,rect4,rect5,rect6,rect7,rect8,rect9,rect10,rect11,rect12,rect13,rect14,rect15,rect16,rect17,rect18]

            #Arcibiskup bílý
            arcibiskup_bily_x_pred=arcibiskup_bily_rect.centerx
            arcibiskup_bily_y_pred=arcibiskup_bily_rect.centery

            rect_x19=arcibiskup_bily_rect.centerx+krok*2
            rect_y19=arcibiskup_bily_rect.centery
            rect19=pygame.Rect(rect_x19-30,rect_y19-30,60,60)

            rect_x20=arcibiskup_bily_rect.centerx+krok*2
            rect_y20=arcibiskup_bily_rect.centery+krok
            rect20=pygame.Rect(rect_x20-30,rect_y20-30,60,60)

            rect_x21=arcibiskup_bily_rect.centerx+krok*2
            rect_y21=arcibiskup_bily_rect.centery-krok
            rect21=pygame.Rect(rect_x21-30,rect_y21-30,60,60)

            rect_x22=arcibiskup_bily_rect.centerx-krok*2
            rect_y22=arcibiskup_bily_rect.centery
            rect22=pygame.Rect(rect_x22-30,rect_y22-30,60,60)

            rect_x23=arcibiskup_bily_rect.centerx-krok*2
            rect_y23=arcibiskup_bily_rect.centery+krok
            rect23=pygame.Rect(rect_x23-30,rect_y23-30,60,60)

            rect_x24=arcibiskup_bily_rect.centerx-krok*2
            rect_y24=arcibiskup_bily_rect.centery-krok
            rect24=pygame.Rect(rect_x24-30,rect_y24-30,60,60)

            rect_x25=arcibiskup_bily_rect.centerx
            rect_y25=arcibiskup_bily_rect.centery+krok*2
            rect25=pygame.Rect(rect_x25-30,rect_y25-30,60,60)

            rect_x26=arcibiskup_bily_rect.centerx+krok
            rect_y26=arcibiskup_bily_rect.centery+krok*2
            rect26=pygame.Rect(rect_x26-30,rect_y26-30,60,60)

            rect_x27=arcibiskup_bily_rect.centerx-krok
            rect_y27=arcibiskup_bily_rect.centery+krok*2
            rect27=pygame.Rect(rect_x27-30,rect_y27-30,60,60)

            rect_x28=arcibiskup_bily_rect.centerx
            rect_y28=arcibiskup_bily_rect.centery-krok*2
            rect28=pygame.Rect(rect_x28-30,rect_y28-30,60,60)

            rect_x29=arcibiskup_bily_rect.centerx+krok
            rect_y29=arcibiskup_bily_rect.centery-krok*2
            rect29=pygame.Rect(rect_x29-30,rect_y29-30,60,60)

            rect_x30=arcibiskup_bily_rect.centerx-krok
            rect_y30=arcibiskup_bily_rect.centery-krok*2
            rect30=pygame.Rect(rect_x30-30,rect_y30-30,60,60)

            ctverce_arcibiskup_bily=[rect19,rect20,rect21,rect22,rect23,rect24,rect25,rect26,rect27,rect28,rect29,rect30]

            #Kardinál bílý
            kardinal_bily_x_pred=kardinal_bily_rect.centerx
            kardinal_bily_y_pred=kardinal_bily_rect.centery

            rect_x31=kardinal_bily_rect.centerx+krok
            rect_y31=kardinal_bily_rect.centery-krok
            rect31=pygame.Rect(rect_x31-30,rect_y31-30,60,60)

            rect_x32=kardinal_bily_rect.centerx-krok
            rect_y32=kardinal_bily_rect.centery-krok
            rect32=pygame.Rect(rect_x32-30,rect_y32-30,60,60)

            rect_x33=kardinal_bily_rect.centerx+krok
            rect_y33=kardinal_bily_rect.centery+krok
            rect33=pygame.Rect(rect_x33-30,rect_y33-30,60,60)

            rect_x34=kardinal_bily_rect.centerx-krok
            rect_y34=kardinal_bily_rect.centery+krok
            rect34=pygame.Rect(rect_x34-30,rect_y34-30,60,60)

            ctverce_kardinal_bily=[rect31,rect32,rect33,rect34]

            #Hádes bílý
            hades_bily_x_pred=hades_bily_rect.centerx
            hades_bily_y_pred=hades_bily_rect.centery

            rect_x35=hades_bily_rect.centerx
            rect_y35=hades_bily_rect.centery-krok
            rect35=pygame.Rect(rect_x35-30,rect_y35-30,60,60)

            rect_x36=hades_bily_rect.centerx
            rect_y36=hades_bily_rect.centery-krok*2
            rect36=pygame.Rect(rect_x36-30,rect_y36-30,60,60)

            rect_x37=hades_bily_rect.centerx
            rect_y37=hades_bily_rect.centery-krok*3
            rect37=pygame.Rect(rect_x37-30,rect_y37-30,60,60)

            rect_x38=hades_bily_rect.centerx+krok
            rect_y38=hades_bily_rect.centery-krok
            rect38=pygame.Rect(rect_x38-30,rect_y38-30,60,60)

            rect_x39=hades_bily_rect.centerx+krok*2
            rect_y39=hades_bily_rect.centery-krok*2
            rect39=pygame.Rect(rect_x39-30,rect_y39-30,60,60)

            rect_x40=hades_bily_rect.centerx+krok*3
            rect_y40=hades_bily_rect.centery-krok*3
            rect40=pygame.Rect(rect_x40-30,rect_y40-30,60,60)

            rect_x41=hades_bily_rect.centerx+krok
            rect_y41=hades_bily_rect.centery
            rect41=pygame.Rect(rect_x41-30,rect_y41-30,60,60)

            rect_x42=hades_bily_rect.centerx+krok*2
            rect_y42=hades_bily_rect.centery
            rect42=pygame.Rect(rect_x42-30,rect_y42-30,60,60)

            rect_x43=hades_bily_rect.centerx+krok*3
            rect_y43=hades_bily_rect.centery
            rect43=pygame.Rect(rect_x43-30,rect_y43-30,60,60)

            rect_x44=hades_bily_rect.centerx+krok
            rect_y44=hades_bily_rect.centery+krok
            rect44=pygame.Rect(rect_x44-30,rect_y44-30,60,60)

            rect_x45=hades_bily_rect.centerx+krok*2
            rect_y45=hades_bily_rect.centery+krok*2
            rect45=pygame.Rect(rect_x45-30,rect_y45-30,60,60)

            rect_x46=hades_bily_rect.centerx-krok
            rect_y46=hades_bily_rect.centery-krok
            rect46=pygame.Rect(rect_x46-30,rect_y46-30,60,60)

            rect_x47=hades_bily_rect.centerx-krok*2
            rect_y47=hades_bily_rect.centery-krok*2
            rect47=pygame.Rect(rect_x47-30,rect_y47-30,60,60)

            rect_x48=hades_bily_rect.centerx-krok*3
            rect_y48=hades_bily_rect.centery-krok*3
            rect48=pygame.Rect(rect_x48-30,rect_y48-30,60,60)

            rect_x49=hades_bily_rect.centerx-krok
            rect_y49=hades_bily_rect.centery
            rect49=pygame.Rect(rect_x49-30,rect_y49-30,60,60)

            rect_x50=hades_bily_rect.centerx-krok*2
            rect_y50=hades_bily_rect.centery
            rect50=pygame.Rect(rect_x50-30,rect_y50-30,60,60)

            rect_x51=hades_bily_rect.centerx-krok*3
            rect_y51=hades_bily_rect.centery
            rect51=pygame.Rect(rect_x51-30,rect_y51-30,60,60)

            rect_x52=hades_bily_rect.centerx-krok
            rect_y52=hades_bily_rect.centery+krok
            rect52=pygame.Rect(rect_x52-30,rect_y52-30,60,60)

            rect_x53=hades_bily_rect.centerx-krok*2
            rect_y53=hades_bily_rect.centery+krok*2
            rect53=pygame.Rect(rect_x53-30,rect_y53-30,60,60)

            ctverce_hades_bily=[rect35,rect36,rect37,rect38,rect39,rect40,rect41,rect42,rect43,rect44,rect45,rect46,rect47,rect48,rect49,rect50,rect51,rect52,rect53]

            #Persefona bílá
            persefona_bila_x_pred=persefona_bila_rect.centerx
            persefona_bila_y_pred=persefona_bila_rect.centery

            ctverce_persefona_bila=[]

            rect_per_x1=persefona_bila_rect.centerx+krok
            rect_per_y1=persefona_bila_rect.centery
            rect_per_1=pygame.Rect(rect_per_x1-30,rect_per_y1-30,60,60)
            ctverce_persefona_bila.append(rect_per_1)

            rect_per_x2=persefona_bila_rect.centerx+krok
            rect_per_y2=persefona_bila_rect.centery-krok
            rect_per_2=pygame.Rect(rect_per_x2-30,rect_per_y2-30,60,60)
            ctverce_persefona_bila.append(rect_per_2)

            rect_per_x3=persefona_bila_rect.centerx
            rect_per_y3=persefona_bila_rect.centery-krok
            rect_per_3=pygame.Rect(rect_per_x3-30,rect_per_y3-30,60,60)
            ctverce_persefona_bila.append(rect_per_3)

            rect_per_x4=persefona_bila_rect.centerx-krok
            rect_per_y4=persefona_bila_rect.centery-krok
            rect_per_4=pygame.Rect(rect_per_x4-30,rect_per_y4-30,60,60)
            ctverce_persefona_bila.append(rect_per_4)

            rect_per_x5=persefona_bila_rect.centerx-krok
            rect_per_y5=persefona_bila_rect.centery
            rect_per_5=pygame.Rect(rect_per_x5-30,rect_per_y5-30,60,60)
            ctverce_persefona_bila.append(rect_per_5)

            rect_per_x6=persefona_bila_rect.centerx-krok
            rect_per_y6=persefona_bila_rect.centery+krok
            rect_per_6=pygame.Rect(rect_per_x6-30,rect_per_y6-30,60,60)
            ctverce_persefona_bila.append(rect_per_6)

            rect_per_x7=persefona_bila_rect.centerx
            rect_per_y7=persefona_bila_rect.centery+krok
            rect_per_7=pygame.Rect(rect_per_x7-30,rect_per_y7-30,60,60)
            ctverce_persefona_bila.append(rect_per_7)

            rect_per_x8=persefona_bila_rect.centerx
            rect_per_y8=persefona_bila_rect.centery+krok
            rect_per_8=pygame.Rect(rect_per_x8-30,rect_per_y8-30,60,60)
            ctverce_persefona_bila.append(rect_per_8)

            rect_per_x9=persefona_bila_rect.centerx+krok
            rect_per_y9=persefona_bila_rect.centery+krok
            rect_per_9=pygame.Rect(rect_per_x9-30,rect_per_y9-30,60,60)
            ctverce_persefona_bila.append(rect_per_9)

            #Kardinál bílý 1
            kardinal_bily_x_pred_1=kardinal_bily_rect1.centerx
            kardinal_bily_y_pred_1=kardinal_bily_rect1.centery

            ctverce_kardinal_bily_1=[]

            rect_kar_x1=kardinal_bily_rect1.centerx+krok
            rect_kar_y1=kardinal_bily_rect1.centery-krok
            rect_kar_1=pygame.Rect(rect_kar_x1-30,rect_kar_y1-30,60,60)
            ctverce_kardinal_bily_1.append(rect_kar_1)

            rect_kar_x2=kardinal_bily_rect1.centerx+krok
            rect_kar_y2=kardinal_bily_rect1.centery+krok
            rect_kar_2=pygame.Rect(rect_kar_x2-30,rect_kar_y2-30,60,60)
            ctverce_kardinal_bily_1.append(rect_kar_2)

            rect_kar_x3=kardinal_bily_rect1.centerx-krok
            rect_kar_y3=kardinal_bily_rect1.centery-krok
            rect_kar_3=pygame.Rect(rect_kar_x3-30,rect_kar_y3-30,60,60)
            ctverce_kardinal_bily_1.append(rect_kar_3)

            rect_kar_x4=kardinal_bily_rect1.centerx-krok
            rect_kar_y4=kardinal_bily_rect1.centery+krok
            rect_kar_4=pygame.Rect(rect_kar_x4-30,rect_kar_y4-30,60,60)
            ctverce_kardinal_bily_1.append(rect_kar_4)

            #Arcibiskup bílý 1
            arcibiskup_bily_x_pred_1=arcibiskup_bily_rect1.centerx
            arcibiskup_bily_y_pred_1=arcibiskup_bily_rect1.centery

            ctverce_arcibiskup_bily_1=[]

            rect_arc_x1=arcibiskup_bily_rect1.centerx+krok*2
            rect_arc_y1=arcibiskup_bily_rect1.centery
            rect_arc_1=pygame.Rect(rect_arc_x1-30,rect_arc_y1-30,60,60)
            ctverce_arcibiskup_bily_1.append(rect_arc_1)

            rect_arc_x2=arcibiskup_bily_rect1.centerx+krok*2
            rect_arc_y2=arcibiskup_bily_rect1.centery-krok
            rect_arc_2=pygame.Rect(rect_arc_x2-30,rect_arc_y2-30,60,60)
            ctverce_arcibiskup_bily_1.append(rect_arc_2)

            rect_arc_x3=arcibiskup_bily_rect1.centerx+krok*2
            rect_arc_y3=arcibiskup_bily_rect1.centery+krok
            rect_arc_3=pygame.Rect(rect_arc_x3-30,rect_arc_y3-30,60,60)
            ctverce_arcibiskup_bily_1.append(rect_arc_3)

            rect_arc_x4=arcibiskup_bily_rect1.centerx
            rect_arc_y4=arcibiskup_bily_rect1.centery+krok*2
            rect_arc_4=pygame.Rect(rect_arc_x4-30,rect_arc_y4-30,60,60)
            ctverce_arcibiskup_bily_1.append(rect_arc_4)

            rect_arc_x5=arcibiskup_bily_rect1.centerx+krok
            rect_arc_y5=arcibiskup_bily_rect1.centery+krok*2
            rect_arc_5=pygame.Rect(rect_arc_x5-30,rect_arc_y5-30,60,60)
            ctverce_arcibiskup_bily_1.append(rect_arc_5)

            rect_arc_x6=arcibiskup_bily_rect1.centerx-krok
            rect_arc_y6=arcibiskup_bily_rect1.centery+krok*2
            rect_arc_6=pygame.Rect(rect_arc_x6-30,rect_arc_y6-30,60,60)
            ctverce_arcibiskup_bily_1.append(rect_arc_6)

            rect_arc_x7=arcibiskup_bily_rect1.centerx-krok*2
            rect_arc_y7=arcibiskup_bily_rect1.centery
            rect_arc_7=pygame.Rect(rect_arc_x7-30,rect_arc_y7-30,60,60)
            ctverce_arcibiskup_bily_1.append(rect_arc_7)

            rect_arc_x8=arcibiskup_bily_rect1.centerx-krok*2
            rect_arc_y8=arcibiskup_bily_rect1.centery-krok
            rect_arc_8=pygame.Rect(rect_arc_x8-30,rect_arc_y8-30,60,60)
            ctverce_arcibiskup_bily_1.append(rect_arc_8)

            rect_arc_x9=arcibiskup_bily_rect1.centerx-krok*2
            rect_arc_y9=arcibiskup_bily_rect1.centery+krok
            rect_arc_9=pygame.Rect(rect_arc_x9-30,rect_arc_y9-30,60,60)
            ctverce_arcibiskup_bily_1.append(rect_arc_9)

            rect_arc_x10=arcibiskup_bily_rect1.centerx
            rect_arc_y10=arcibiskup_bily_rect1.centery-krok*2
            rect_arc_10=pygame.Rect(rect_arc_x10-30,rect_arc_y10-30,60,60)
            ctverce_arcibiskup_bily_1.append(rect_arc_10)

            rect_arc_x11=arcibiskup_bily_rect1.centerx+krok
            rect_arc_y11=arcibiskup_bily_rect1.centery-krok*2
            rect_arc_11=pygame.Rect(rect_arc_x11-30,rect_arc_y11-30,60,60)
            ctverce_arcibiskup_bily_1.append(rect_arc_11)

            rect_arc_x12=arcibiskup_bily_rect1.centerx-krok
            rect_arc_y12=arcibiskup_bily_rect1.centery-krok*2
            rect_arc_12=pygame.Rect(rect_arc_x12-30,rect_arc_y12-30,60,60)
            ctverce_arcibiskup_bily_1.append(rect_arc_12)

            #Morový doktor bílý 1 
            morovy_doktor_bily_x_pred_1=morovy_doktor_bily_rect1.centerx
            morovy_doktor_bily_y_pred_1=morovy_doktor_bily_rect1.centery

            ctverce_morovy_doktor_bily_1=[]

            rect_mor_x1=morovy_doktor_bily_rect1.centerx
            rect_mor_y1=morovy_doktor_bily_rect1.centery+krok
            rect_mor_1=pygame.Rect(rect_mor_x1-30,rect_mor_y1-30,60,60)
            ctverce_morovy_doktor_bily_1.append(rect_mor_1)

            rect_mor_x2=morovy_doktor_bily_rect1.centerx
            rect_mor_y2=morovy_doktor_bily_rect1.centery+krok*2
            rect_mor_2=pygame.Rect(rect_mor_x2-30,rect_mor_y2-30,60,60)
            ctverce_morovy_doktor_bily_1.append(rect_mor_2)

            rect_mor_x3=morovy_doktor_bily_rect1.centerx
            rect_mor_y3=morovy_doktor_bily_rect1.centery+krok*3
            rect_mor_3=pygame.Rect(rect_mor_x3-30,rect_mor_y3-30,60,60)
            ctverce_morovy_doktor_bily_1.append(rect_mor_3)

            rect_mor_x4=morovy_doktor_bily_rect1.centerx
            rect_mor_y4=morovy_doktor_bily_rect1.centery+krok*4
            rect_mor_4=pygame.Rect(rect_mor_x4-30,rect_mor_y4-30,60,60)
            ctverce_morovy_doktor_bily_1.append(rect_mor_4)

            rect_mor_x5=morovy_doktor_bily_rect1.centerx
            rect_mor_y5=morovy_doktor_bily_rect1.centery+krok*5
            rect_mor_5=pygame.Rect(rect_mor_x5-30,rect_mor_y5-30,60,60)
            ctverce_morovy_doktor_bily_1.append(rect_mor_5)

            rect_mor_x6=morovy_doktor_bily_rect1.centerx
            rect_mor_y6=morovy_doktor_bily_rect1.centery+krok*6
            rect_mor_6=pygame.Rect(rect_mor_x6-30,rect_mor_y6-30,60,60)
            ctverce_morovy_doktor_bily_1.append(rect_mor_6)

            rect_mor_x7=morovy_doktor_bily_rect1.centerx
            rect_mor_y7=morovy_doktor_bily_rect1.centery+krok*7
            rect_mor_7=pygame.Rect(rect_mor_x7-30,rect_mor_y7-30,60,60)
            ctverce_morovy_doktor_bily_1.append(rect_mor_7)

            rect_mor_x8=morovy_doktor_bily_rect1.centerx
            rect_mor_y8=morovy_doktor_bily_rect1.centery-krok
            rect_mor_8=pygame.Rect(rect_mor_x8-30,rect_mor_y8-30,60,60)
            ctverce_morovy_doktor_bily_1.append(rect_mor_8)

            rect_mor_x9=morovy_doktor_bily_rect1.centerx
            rect_mor_y9=morovy_doktor_bily_rect1.centery-krok*2
            rect_mor_9=pygame.Rect(rect_mor_x9-30,rect_mor_y9-30,60,60)
            ctverce_morovy_doktor_bily_1.append(rect_mor_9)

            rect_mor_x10=morovy_doktor_bily_rect1.centerx
            rect_mor_y10=morovy_doktor_bily_rect1.centery-krok*3
            rect_mor_10=pygame.Rect(rect_mor_x10-30,rect_mor_y10-30,60,60)
            ctverce_morovy_doktor_bily_1.append(rect_mor_10)

            rect_mor_x11=morovy_doktor_bily_rect1.centerx
            rect_mor_y11=morovy_doktor_bily_rect1.centery-krok*4
            rect_mor_11=pygame.Rect(rect_mor_x11-30,rect_mor_y11-30,60,60)
            ctverce_morovy_doktor_bily_1.append(rect_mor_11)

            rect_mor_x12=morovy_doktor_bily_rect1.centerx
            rect_mor_y12=morovy_doktor_bily_rect1.centery-krok*5
            rect_mor_12=pygame.Rect(rect_mor_x12-30,rect_mor_y12-30,60,60)
            ctverce_morovy_doktor_bily_1.append(rect_mor_12)

            rect_mor_x13=morovy_doktor_bily_rect1.centerx
            rect_mor_y13=morovy_doktor_bily_rect1.centery-krok*6
            rect_mor_13=pygame.Rect(rect_mor_x13-30,rect_mor_y13-30,60,60)
            ctverce_morovy_doktor_bily_1.append(rect_mor_13)

            rect_mor_x14=morovy_doktor_bily_rect1.centerx
            rect_mor_y14=morovy_doktor_bily_rect1.centery-krok*7
            rect_mor_14=pygame.Rect(rect_mor_x14-30,rect_mor_y14-30,60,60)
            ctverce_morovy_doktor_bily_1.append(rect_mor_14)

            rect_mor_x15=morovy_doktor_bily_rect1.centerx+krok
            rect_mor_y15=morovy_doktor_bily_rect1.centery
            rect_mor_15=pygame.Rect(rect_mor_x15-30,rect_mor_y15-30,60,60)
            ctverce_morovy_doktor_bily_1.append(rect_mor_15)

            rect_mor_x16=morovy_doktor_bily_rect1.centerx+krok*2
            rect_mor_y16=morovy_doktor_bily_rect1.centery
            rect_mor_16=pygame.Rect(rect_mor_x16-30,rect_mor_y16-30,60,60)
            ctverce_morovy_doktor_bily_1.append(rect_mor_16)

            rect_mor_x17=morovy_doktor_bily_rect1.centerx-krok
            rect_mor_y17=morovy_doktor_bily_rect1.centery
            rect_mor_17=pygame.Rect(rect_mor_x17-30,rect_mor_y17-30,60,60)
            ctverce_morovy_doktor_bily_1.append(rect_mor_17)

            rect_mor_x18=morovy_doktor_bily_rect1.centerx-krok*2
            rect_mor_y18=morovy_doktor_bily_rect1.centery
            rect_mor_18=pygame.Rect(rect_mor_x18-30,rect_mor_y18-30,60,60)
            ctverce_morovy_doktor_bily_1.append(rect_mor_18)

            #Válečník bílý 1
            valecnik_bily_x_pred=valecnik_bily_rect.centerx
            valecnik_bily_y_pred=valecnik_bily_rect.centery

            ctverce_valecnik_bily=[]

            rect_val_x1=valecnik_bily_rect.centerx+krok
            rect_val_y1=valecnik_bily_rect.centery
            rect_val_1=pygame.Rect(rect_val_x1-30,rect_val_y1-30,60,60)
            ctverce_valecnik_bily.append(rect_val_1)

            rect_val_x2=valecnik_bily_rect.centerx-krok
            rect_val_y2=valecnik_bily_rect.centery
            rect_val_2=pygame.Rect(rect_val_x2-30,rect_val_y2-30,60,60)
            ctverce_valecnik_bily.append(rect_val_2)

            rect_val_x3=valecnik_bily_rect.centerx
            rect_val_y3=valecnik_bily_rect.centery+krok
            rect_val_3=pygame.Rect(rect_val_x3-30,rect_val_y3-30,60,60)
            ctverce_valecnik_bily.append(rect_val_3)

            rect_val_x4=valecnik_bily_rect.centerx
            rect_val_y4=valecnik_bily_rect.centery-krok
            rect_val_4=pygame.Rect(rect_val_x4-30,rect_val_y4-30,60,60)
            ctverce_valecnik_bily.append(rect_val_4)

            #Legionář bílý 1
            legionar_bily_x_pred=legionar_bily_rect.centerx
            legionar_bily_y_pred=legionar_bily_rect.centery


            ctverce_legionar_bily=[]

            rect_leg_x1=legionar_bily_rect.centerx+krok
            rect_leg_y1=legionar_bily_rect.centery+krok
            rect_leg_1=pygame.Rect(rect_leg_x1-30,rect_leg_y1-30,60,60)
            ctverce_legionar_bily.append(rect_leg_1)

            rect_leg_x2=legionar_bily_rect.centerx
            rect_leg_y2=legionar_bily_rect.centery+krok
            rect_leg_2=pygame.Rect(rect_leg_x2-30,rect_leg_y2-30,60,60)
            ctverce_legionar_bily.append(rect_leg_2)

            rect_leg_x3=legionar_bily_rect.centerx-krok
            rect_leg_y3=legionar_bily_rect.centery+krok
            rect_leg_3=pygame.Rect(rect_leg_x3-30,rect_leg_y3-30,60,60)
            ctverce_legionar_bily.append(rect_leg_3)

            #Válečník bílý 2
            valecnik_bily_x_pred_1=valecnik_bily_rect1.centerx
            valecnik_bily_y_pred_1=valecnik_bily_rect1.centery

            ctverce_valecnik_bily_1=[]

            rect_val_1_x1=valecnik_bily_rect1.centerx+krok
            rect_val_1_y1=valecnik_bily_rect1.centery
            rect_val_1_1=pygame.Rect(rect_val_1_x1-30,rect_val_1_y1-30,60,60)
            ctverce_valecnik_bily_1.append(rect_val_1_1)

            rect_val_1_x2=valecnik_bily_rect1.centerx-krok
            rect_val_1_y2=valecnik_bily_rect1.centery
            rect_val_1_2=pygame.Rect(rect_val_1_x2-30,rect_val_1_y2-30,60,60)
            ctverce_valecnik_bily_1.append(rect_val_1_2)

            rect_val_1_x3=valecnik_bily_rect1.centerx
            rect_val_1_y3=valecnik_bily_rect1.centery+krok
            rect_val_1_3=pygame.Rect(rect_val_1_x3-30,rect_val_1_y3-30,60,60)
            ctverce_valecnik_bily_1.append(rect_val_1_3)

            rect_val_1_x4=valecnik_bily_rect1.centerx
            rect_val_1_y4=valecnik_bily_rect1.centery-krok
            rect_val_1_4=pygame.Rect(rect_val_1_x4-30,rect_val_1_y4-30,60,60)
            ctverce_valecnik_bily_1.append(rect_val_1_4)

            #Legionář bílý 2
            legionar_bily_x_pred_1=legionar_bily_rect1.centerx
            legionar_bily_y_pred_1=legionar_bily_rect1.centery

            ctverce_legionar_bily_1=[]

            rect_leg_1_x1=legionar_bily_rect1.centerx+krok
            rect_leg_1_y1=legionar_bily_rect1.centery+krok
            rect_leg_1_1=pygame.Rect(rect_leg_1_x1-30,rect_leg_1_y1-30,60,60)
            ctverce_legionar_bily_1.append(rect_leg_1_1)

            rect_leg_1_x2=legionar_bily_rect1.centerx
            rect_leg_1_y2=legionar_bily_rect1.centery+krok
            rect_leg_1_2=pygame.Rect(rect_leg_1_x2-30,rect_leg_1_y2-30,60,60)
            ctverce_legionar_bily_1.append(rect_leg_1_2)

            rect_leg_1_x3=legionar_bily_rect1.centerx-krok
            rect_leg_1_3=legionar_bily_rect1.centery+krok
            rect_leg_1_3=pygame.Rect(rect_leg_1_x3-30,rect_leg_1_y3-30,60,60)
            ctverce_legionar_bily_1.append(rect_leg_1_3)

            #Válečník bílý 3
            valecnik_bily_x_pred_2=valecnik_bily_rect2.centerx
            valecnik_bily_y_pred_2=valecnik_bily_rect2.centery

            ctverce_valecnik_bily_2=[]

            rect_val_2_x1=valecnik_bily_rect2.centerx+krok
            rect_val_2_y1=valecnik_bily_rect2.centery
            rect_val_2_1=pygame.Rect(rect_val_2_x1-30,rect_val_2_y1-30,60,60)
            ctverce_valecnik_bily_2.append(rect_val_2_1)

            rect_val_2_x2=valecnik_bily_rect2.centerx-krok
            rect_val_2_y2=valecnik_bily_rect2.centery
            rect_val_2_2=pygame.Rect(rect_val_2_x2-30,rect_val_2_y2-30,60,60)
            ctverce_valecnik_bily_2.append(rect_val_2_2)

            rect_val_2_x3=valecnik_bily_rect2.centerx
            rect_val_2_y3=valecnik_bily_rect2.centery+krok
            rect_val_2_3=pygame.Rect(rect_val_2_x3-30,rect_val_2_y3-30,60,60)
            ctverce_valecnik_bily_2.append(rect_val_2_3)

            rect_val_2_x4=valecnik_bily_rect2.centerx
            rect_val_2_y4=valecnik_bily_rect2.centery-krok
            rect_val_2_4=pygame.Rect(rect_val_2_x4-30,rect_val_2_y4-30,60,60)
            ctverce_valecnik_bily_2.append(rect_val_2_4)

            #Legionář bílý 3
            legionar_bily_x_pred_2=legionar_bily_rect2.centerx
            legionar_bily_y_pred_2=legionar_bily_rect2.centery

            ctverce_legionar_bily_2=[]

            rect_leg_2_x1=legionar_bily_rect2.centerx+krok
            rect_leg_2_y1=legionar_bily_rect2.centery+krok
            rect_leg_2_1=pygame.Rect(rect_leg_2_x1-30,rect_leg_2_y1-30,60,60)
            ctverce_legionar_bily_2.append(rect_leg_2_1)

            rect_leg_2_x2=legionar_bily_rect2.centerx
            rect_leg_2_y2=legionar_bily_rect2.centery+krok
            rect_leg_2_2=pygame.Rect(rect_leg_2_x2-30,rect_leg_2_y2-30,60,60)
            ctverce_legionar_bily_2.append(rect_leg_2_2)

            rect_leg_2_x3=legionar_bily_rect2.centerx-krok
            rect_leg_2_y3=legionar_bily_rect2.centery+krok
            rect_leg_2_3=pygame.Rect(rect_leg_2_x3-30,rect_leg_2_y3-30,60,60)
            ctverce_legionar_bily_2.append(rect_leg_2_3)

            #Válečník bílý 4
            valecnik_bily_x_pred_3=valecnik_bily_rect3.centerx
            valecnik_bily_y_pred_3=valecnik_bily_rect3.centery
    
            ctverce_valecnik_bily_3=[]

            rect_val_3_x1=valecnik_bily_rect3.centerx+krok
            rect_val_3_y1=valecnik_bily_rect3.centery
            rect_val_3_1=(rect_val_3_x1-30,rect_val_3_y1-30,60,60)
            ctverce_valecnik_bily_3.append(rect_val_3_1)

            rect_val_3_x2=valecnik_bily_rect3.centerx-krok
            rect_val_3_y2=valecnik_bily_rect3.centery
            rect_val_3_2=(rect_val_3_x2-30,rect_val_3_y2-30,60,60)
            ctverce_valecnik_bily_3.append(rect_val_3_2)

            rect_val_3_x3=valecnik_bily_rect3.centerx
            rect_val_3_y3=valecnik_bily_rect3.centery+krok
            rect_val_3_3=(rect_val_3_x3-30,rect_val_3_y3-30,60,60)
            ctverce_valecnik_bily_3.append(rect_val_3_3)

            rect_val_3_x4=valecnik_bily_rect3.centerx
            rect_val_3_y4=valecnik_bily_rect3.centery-krok
            rect_val_3_4=(rect_val_3_x4-30,rect_val_3_y4-30,60,60)
            ctverce_valecnik_bily_3.append(rect_val_3_4)

            #Legionář bílý 4
            legionar_bily_x_pred_3=legionar_bily_rect3.centerx
            legionar_bily_y_pred_3=legionar_bily_rect3.centery

            ctverce_legionar_bily_3=[]

            rect_leg_3_x1=legionar_bily_rect3.centerx+krok
            rect_leg_3_y1=legionar_bily_rect3.centery+krok
            rect_leg_3_1=pygame.Rect(rect_leg_3_x1-30,rect_leg_3_y1-30,60,60)
            ctverce_legionar_bily_3.append(rect_leg_3_1)

            rect_leg_3_x2=legionar_bily_rect3.centerx
            rect_leg_3_y2=legionar_bily_rect3.centery+krok
            rect_leg_3_2=pygame.Rect(rect_leg_3_x2-30,rect_leg_3_y2-30,60,60)
            ctverce_legionar_bily_3.append(rect_leg_3_1)

            rect_leg_3_x3=legionar_bily_rect3.centerx-krok
            rect_leg_3_y3=legionar_bily_rect3.centery+krok
            rect_leg_3_3=pygame.Rect(rect_leg_3_x3-30,rect_leg_3_y3-30,60,60)
            ctverce_legionar_bily_3.append(rect_leg_3_3)




        
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
            if morovy_doktor_bily_rect.collidepoint(event.pos):
                for ctverec in ctverce_morovy_doktor_bily:
                    
                    if (ctverec.right < 1440 or ctverec.left > 475) or (ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen,black,ctverec,5)
               
                
                morovy_doktor_bily_rect.centerx=event.pos[0]
                morovy_doktor_bily_rect.centery=event.pos[1]

            elif arcibiskup_bily_rect.collidepoint(event.pos):
                for ctverec in ctverce_arcibiskup_bily:
                    
                    if (ctverec.right < 1440 or ctverec.left > 475) or (ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen,black,ctverec,5)
               
                
                arcibiskup_bily_rect.centerx=event.pos[0]
                arcibiskup_bily_rect.centery=event.pos[1]

            elif kardinal_bily_rect.collidepoint(event.pos):
                for ctverec in ctverce_kardinal_bily:
                        if (ctverec.right < 1440 or ctverec.left > 475) or (ctverec.bottom < 850 or ctverec.top > 60):
                            pygame.draw.rect(screen,black,ctverec,5)
                
                kardinal_bily_rect.centerx=event.pos[0]
                kardinal_bily_rect.centery=event.pos[1]
            
            elif hades_bily_rect.collidepoint(event.pos):
                for ctverec in ctverce_hades_bily:
                        if (ctverec.right < 1440 or ctverec.left > 475) or (ctverec.bottom < 850 or ctverec.top > 60):
                            pygame.draw.rect(screen,black,ctverec,5)
                
                hades_bily_rect.centerx=event.pos[0]
                hades_bily_rect.centery=event.pos[1]

            elif persefona_bila_rect.collidepoint(event.pos):
                for ctverec in ctverce_persefona_bila:
                        if (ctverec.right < 1440 or ctverec.left > 475) or (ctverec.bottom < 850 or ctverec.top > 60):
                            pygame.draw.rect(screen,black,ctverec,5)
                
                persefona_bila_rect.centerx=event.pos[0]
                persefona_bila_rect.centery=event.pos[1]
            
            elif kardinal_bily_rect1.collidepoint(event.pos):
                for ctverec in ctverce_kardinal_bily_1:
                        if (ctverec.right < 1440 or ctverec.left > 475) or (ctverec.bottom < 850 or ctverec.top > 60):
                            pygame.draw.rect(screen,black,ctverec,5)
                
                kardinal_bily_rect1.centerx=event.pos[0]
                kardinal_bily_rect1.centery=event.pos[1]
            
            elif arcibiskup_bily_rect1.collidepoint(event.pos):
                for ctverec in ctverce_arcibiskup_bily_1:
                        if (ctverec.right < 1440 or ctverec.left > 475) or (ctverec.bottom < 850 or ctverec.top > 60):
                            pygame.draw.rect(screen,black,ctverec,5)
                
                arcibiskup_bily_rect1.centerx=event.pos[0]
                arcibiskup_bily_rect1.centery=event.pos[1]
                 
            elif morovy_doktor_bily_rect1.collidepoint(event.pos):
                for ctverec in ctverce_morovy_doktor_bily_1:
                        if (ctverec.right < 1440 or ctverec.left > 475) or (ctverec.bottom < 850 or ctverec.top > 60):
                            pygame.draw.rect(screen,black,ctverec,5)
                
                morovy_doktor_bily_rect1.centerx=event.pos[0]
                morovy_doktor_bily_rect1.centery=event.pos[1]

            elif valecnik_bily_rect.collidepoint(event.pos):
                for ctverec in ctverce_valecnik_bily:
                        if (ctverec.right < 1440 or ctverec.left > 475) or (ctverec.bottom < 850 or ctverec.top > 60):
                            pygame.draw.rect(screen,black,ctverec,5)
                
                valecnik_bily_rect.centerx=event.pos[0]
                valecnik_bily_rect.centery=event.pos[1]

            elif legionar_bily_rect.collidepoint(event.pos):
                for ctverec in ctverce_legionar_bily:
                        if (ctverec.right < 1440 or ctverec.left > 475) or (ctverec.bottom < 850 or ctverec.top > 60):
                            pygame.draw.rect(screen,black,ctverec,5)
                
                legionar_bily_rect.centerx=event.pos[0]
                legionar_bily_rect.centery=event.pos[1]
            
            elif valecnik_bily_rect1.collidepoint(event.pos):
                for ctverec in ctverce_valecnik_bily_1:
                        if (ctverec.right < 1440 or ctverec.left > 475) or (ctverec.bottom < 850 or ctverec.top > 60):
                            pygame.draw.rect(screen,black,ctverec,5)
                
                valecnik_bily_rect1.centerx=event.pos[0]
                valecnik_bily_rect1.centery=event.pos[1]
            
            elif legionar_bily_rect1.collidepoint(event.pos):
                for ctverec in ctverce_legionar_bily_1:
                        if (ctverec.right < 1440 or ctverec.left > 475) or (ctverec.bottom < 850 or ctverec.top > 60):
                            pygame.draw.rect(screen,black,ctverec,5)
                
                legionar_bily_rect1.centerx=event.pos[0]
                legionar_bily_rect1.centery=event.pos[1]
                
            elif valecnik_bily_rect2.collidepoint(event.pos):
                for ctverec in ctverce_valecnik_bily_2:
                        if (ctverec.right < 1440 or ctverec.left > 475) or (ctverec.bottom < 850 or ctverec.top > 60):
                            pygame.draw.rect(screen,black,ctverec,5)
                
                valecnik_bily_rect2.centerx=event.pos[0]
                valecnik_bily_rect2.centery=event.pos[1]
                 
            elif legionar_bily_rect2.collidepoint(event.pos):
                for ctverec in ctverce_legionar_bily_2:
                        if (ctverec.right < 1440 or ctverec.left > 475) or (ctverec.bottom < 850 or ctverec.top > 60):
                            pygame.draw.rect(screen,black,ctverec,5)
                
                legionar_bily_rect2.centerx=event.pos[0]
                legionar_bily_rect2.centery=event.pos[1]   

            elif valecnik_bily_rect3.collidepoint(event.pos):
                for ctverec in ctverce_valecnik_bily_3:
                        if (ctverec.right < 1440 or ctverec.left > 475) or (ctverec.bottom < 850 or ctverec.top > 60):
                            pygame.draw.rect(screen,black,ctverec,5)
                
                valecnik_bily_rect3.centerx=event.pos[0]
                valecnik_bily_rect3.centery=event.pos[1]     
            
            elif legionar_bily_rect3.collidepoint(event.pos):
                for ctverec in ctverce_legionar_bily_3:
                        if (ctverec.right < 1440 or ctverec.left > 475) or (ctverec.bottom < 850 or ctverec.top > 60):
                            pygame.draw.rect(screen,black,ctverec,5)
                
                legionar_bily_rect3.centerx=event.pos[0]
                legionar_bily_rect3.centery=event.pos[1]   

                
                      

             
                    
        if event.type==pygame.MOUSEBUTTONUP:
            pohyb=False #Todo: zjistit, jak tento proces zjednodušit pomocí for cyklu
            """for i in range(0,len(ctverce_morovy_doktor_bily)): 
                if morovy_doktor_bily_rect.colliderect(ctverce_morovy_doktor_bily[i]):
                    morovy_doktor_bily_rect.centerx=ctverce_morovy_doktor_bily[i].centerx
                    morovy_doktor_bily_rect.centery=ctverce_morovy_doktor_bily[i].centery

                elif i==len(ctverce_morovy_doktor_bily)-1:
                    morovy_doktor_bily_rect.centerx=morovy_doktor_bily_x_pred
                    morovy_doktor_bily_rect.centery=morovy_doktor_bily_y_pred"""
            if morovy_doktor_bily_rect.colliderect(rect1):
                    morovy_doktor_bily_rect.centerx=rect1.centerx
                    morovy_doktor_bily_rect.centery=rect1.centery
            elif morovy_doktor_bily_rect.colliderect(rect2):
                    morovy_doktor_bily_rect.centerx=rect2.centerx
                    morovy_doktor_bily_rect.centery=rect2.centery
            elif morovy_doktor_bily_rect.colliderect(rect3):
                    morovy_doktor_bily_rect.centerx=rect3.centerx
                    morovy_doktor_bily_rect.centery=rect3.centery
            elif morovy_doktor_bily_rect.colliderect(rect4):
                    morovy_doktor_bily_rect.centerx=rect4.centerx
                    morovy_doktor_bily_rect.centery=rect4.centery
            elif morovy_doktor_bily_rect.colliderect(rect5):
                    morovy_doktor_bily_rect.centerx=rect5.centerx
                    morovy_doktor_bily_rect.centery=rect5.centery
            elif morovy_doktor_bily_rect.colliderect(rect6):
                    morovy_doktor_bily_rect.centerx=rect6.centerx
                    morovy_doktor_bily_rect.centery=rect6.centery
            elif morovy_doktor_bily_rect.colliderect(rect7):
                    morovy_doktor_bily_rect.centerx=rect7.centerx
                    morovy_doktor_bily_rect.centery=rect7.centery
            elif morovy_doktor_bily_rect.colliderect(rect8):
                    morovy_doktor_bily_rect.centerx=rect8.centerx
                    morovy_doktor_bily_rect.centery=rect8.centery
            elif morovy_doktor_bily_rect.colliderect(rect9):
                    morovy_doktor_bily_rect.centerx=rect9.centerx
                    morovy_doktor_bily_rect.centery=rect9.centery
            elif morovy_doktor_bily_rect.colliderect(rect10):
                    morovy_doktor_bily_rect.centerx=rect10.centerx
                    morovy_doktor_bily_rect.centery=rect10.centery
            elif morovy_doktor_bily_rect.colliderect(rect11):
                    morovy_doktor_bily_rect.centerx=rect11.centerx
                    morovy_doktor_bily_rect.centery=rect11.centery
            elif morovy_doktor_bily_rect.colliderect(rect12):
                    morovy_doktor_bily_rect.centerx=rect12.centerx
                    morovy_doktor_bily_rect.centery=rect12.centery
            elif morovy_doktor_bily_rect.colliderect(rect13):
                    morovy_doktor_bily_rect.centerx=rect13.centerx
                    morovy_doktor_bily_rect.centery=rect13.centery
            elif morovy_doktor_bily_rect.colliderect(rect14):
                    morovy_doktor_bily_rect.centerx=rect14.centerx
                    morovy_doktor_bily_rect.centery=rect14.centery
            elif morovy_doktor_bily_rect.colliderect(rect15):
                    morovy_doktor_bily_rect.centerx=rect15.centerx
                    morovy_doktor_bily_rect.centery=rect15.centery
            elif morovy_doktor_bily_rect.colliderect(rect16):
                    morovy_doktor_bily_rect.centerx=rect16.centerx
                    morovy_doktor_bily_rect.centery=rect16.centery
            elif morovy_doktor_bily_rect.colliderect(rect17):
                    morovy_doktor_bily_rect.centerx=rect17.centerx
                    morovy_doktor_bily_rect.centery=rect17.centery
            elif morovy_doktor_bily_rect.colliderect(rect18):
                    morovy_doktor_bily_rect.centerx=rect18.centerx
                    morovy_doktor_bily_rect.centery=rect18.centery
            else:
                    morovy_doktor_bily_rect.centerx=morovy_doktor_bily_x_pred
                    morovy_doktor_bily_rect.centery=morovy_doktor_bily_y_pred
            if (morovy_doktor_bily_rect.right > 1440 or morovy_doktor_bily_rect.left < 475) or (morovy_doktor_bily_rect.bottom > 1020 or morovy_doktor_bily_rect.top < 60):
                    morovy_doktor_bily_rect.centerx=morovy_doktor_bily_x_pred
                    morovy_doktor_bily_rect.centery=morovy_doktor_bily_y_pred
            
            if arcibiskup_bily_rect.colliderect(rect19):
                arcibiskup_bily_rect.centerx=rect19.centerx
                arcibiskup_bily_rect.centery=rect19.centery
            elif arcibiskup_bily_rect.colliderect(rect20):
                arcibiskup_bily_rect.centerx=rect20.centerx
                arcibiskup_bily_rect.centery=rect20.centery
            elif arcibiskup_bily_rect.colliderect(rect21):
                arcibiskup_bily_rect.centerx=rect21.centerx
                arcibiskup_bily_rect.centery=rect21.centery
            elif arcibiskup_bily_rect.colliderect(rect22):
                arcibiskup_bily_rect.centerx=rect22.centerx
                arcibiskup_bily_rect.centery=rect22.centery
            elif arcibiskup_bily_rect.colliderect(rect23):
                arcibiskup_bily_rect.centerx=rect23.centerx
                arcibiskup_bily_rect.centery=rect23.centery
            elif arcibiskup_bily_rect.colliderect(rect24):
                arcibiskup_bily_rect.centerx=rect24.centerx
                arcibiskup_bily_rect.centery=rect24.centery
            elif arcibiskup_bily_rect.colliderect(rect25):
                arcibiskup_bily_rect.centerx=rect25.centerx
                arcibiskup_bily_rect.centery=rect25.centery
            elif arcibiskup_bily_rect.colliderect(rect26):
                arcibiskup_bily_rect.centerx=rect26.centerx
                arcibiskup_bily_rect.centery=rect26.centery
            elif arcibiskup_bily_rect.colliderect(rect27):
                arcibiskup_bily_rect.centerx=rect27.centerx
                arcibiskup_bily_rect.centery=rect27.centery
            elif arcibiskup_bily_rect.colliderect(rect28):
                arcibiskup_bily_rect.centerx=rect28.centerx
                arcibiskup_bily_rect.centery=rect28.centery
            elif arcibiskup_bily_rect.colliderect(rect29):
                arcibiskup_bily_rect.centerx=rect29.centerx
                arcibiskup_bily_rect.centery=rect29.centery
            elif arcibiskup_bily_rect.colliderect(rect30):
                arcibiskup_bily_rect.centerx=rect30.centerx
                arcibiskup_bily_rect.centery=rect30.centery
            else:
                arcibiskup_bily_rect.centerx=arcibiskup_bily_x_pred
                arcibiskup_bily_rect.centery=arcibiskup_bily_y_pred
            if (arcibiskup_bily_rect.right > 1440 or arcibiskup_bily_rect.left < 475) or (arcibiskup_bily_rect.bottom > 1020 or arcibiskup_bily_rect.top < 60):
                    arcibiskup_bily_rect.centerx=arcibiskup_bily_x_pred
                    arcibiskup_bily_rect.centery=arcibiskup_bily_y_pred
            
            if kardinal_bily_rect.colliderect(rect31):
                kardinal_bily_rect.centerx=rect31.centerx
                kardinal_bily_rect.centery=rect31.centery              
            elif kardinal_bily_rect.colliderect(rect32):
                kardinal_bily_rect.centerx=rect32.centerx
                kardinal_bily_rect.centery=rect32.centery              
            elif kardinal_bily_rect.colliderect(rect33):
                kardinal_bily_rect.centerx=rect33.centerx
                kardinal_bily_rect.centery=rect34.centery              
            elif kardinal_bily_rect.colliderect(rect34):
                kardinal_bily_rect.centerx=rect34.centerx
                kardinal_bily_rect.centery=rect34.centery      
            else:
                kardinal_bily_rect.centerx=kardinal_bily_x_pred
                kardinal_bily_rect.centery=kardinal_bily_y_pred
            if (kardinal_bily_rect.right > 1440 or kardinal_bily_rect.left < 475) or (kardinal_bily_rect.bottom > 1020 or kardinal_bily_rect.top < 60):
                kardinal_bily_rect.centerx=kardinal_bily_x_pred
                kardinal_bily_rect.centery=kardinal_bily_y_pred

            if hades_bily_rect.colliderect(rect35):
                hades_bily_rect.centerx=rect35.centerx
                hades_bily_rect.centery=rect35.centery
                print("35")
            elif hades_bily_rect.colliderect(rect36):
                hades_bily_rect.centerx=rect36.centerx
                hades_bily_rect.centery=rect36.centery
                print("36")
                
            elif hades_bily_rect.colliderect(rect37):
                hades_bily_rect.centerx=rect37.centerx
                hades_bily_rect.centery=rect37.centery
                print("37")
            elif hades_bily_rect.colliderect(rect38):
                hades_bily_rect.centerx=rect38.centerx
                hades_bily_rect.centery=rect38.centery
                print("38")
            elif hades_bily_rect.colliderect(rect39):
                hades_bily_rect.centerx=rect39.centerx
                hades_bily_rect.centery=rect39.centery
                print("39")
                
                
            elif hades_bily_rect.colliderect(rect40):
                hades_bily_rect.centerx=rect40.centerx
                hades_bily_rect.centery=rect40.centery
                print("40")
            elif hades_bily_rect.colliderect(rect41):
                hades_bily_rect.centerx=rect41.centerx
                hades_bily_rect.centery=rect41.centery
                print("41")
            elif hades_bily_rect.colliderect(rect42):
                hades_bily_rect.centerx=rect42.centerx
                hades_bily_rect.centery=rect42.centery
                print("42")
            elif hades_bily_rect.colliderect(rect43):
                hades_bily_rect.centerx=rect43.centerx
                hades_bily_rect.centery=rect43.centery
                print("43")
            elif hades_bily_rect.colliderect(rect44):
                hades_bily_rect.centerx=rect44.centerx
                hades_bily_rect.centery=rect44.centery
                print("44")
            elif hades_bily_rect.colliderect(rect45):
                hades_bily_rect.centerx=rect45.centerx
                hades_bily_rect.centery=rect45.centery
                print("45")
            elif hades_bily_rect.colliderect(rect46):
                hades_bily_rect.centerx=rect46.centerx
                hades_bily_rect.centery=rect46.centery
                print("46")
            elif hades_bily_rect.colliderect(rect47):
                hades_bily_rect.centerx=rect47.centerx
                hades_bily_rect.centery=rect47.centery
                print("47")
            elif hades_bily_rect.colliderect(rect48):
                hades_bily_rect.centerx=rect48.centerx
                hades_bily_rect.centery=rect48.centery
                print("48")
            elif hades_bily_rect.colliderect(rect49):
                hades_bily_rect.centerx=rect49.centerx
                hades_bily_rect.centery=rect49.centery
                print("49")
            elif hades_bily_rect.colliderect(rect50):
                hades_bily_rect.centerx=rect50.centerx
                hades_bily_rect.centery=rect50.centery
                print("50")
            elif hades_bily_rect.colliderect(rect51):
                hades_bily_rect.centerx=rect51.centerx
                hades_bily_rect.centery=rect51.centery
                print("51")
            elif hades_bily_rect.colliderect(rect52):
                hades_bily_rect.centerx=rect52.centerx
                hades_bily_rect.centery=rect52.centery
                print("52")
            elif hades_bily_rect.colliderect(rect53):
                hades_bily_rect.centerx=rect53.centerx
                hades_bily_rect.centery=rect53.centery
                print("53")
            else:
                hades_bily_rect.centerx=hades_bily_x_pred
                hades_bily_rect.centery=hades_bily_y_pred
            if (hades_bily_rect.right > 1440 or hades_bily_rect.left < 475) or (hades_bily_rect.bottom > 1020 or hades_bily_rect.top < 60):
                hades_bily_rect.centerx=hades_bily_x_pred
                hades_bily_rect.centery=hades_bily_y_pred
            
            if persefona_bila_rect.colliderect(rect_per_1):
                persefona_bila_rect.centerx=rect_per_1.centerx
                persefona_bila_rect.centery=rect_per_1.centery
            elif persefona_bila_rect.colliderect(rect_per_2):
                persefona_bila_rect.centerx=rect_per_2.centerx
                persefona_bila_rect.centery=rect_per_2.centery
            elif persefona_bila_rect.colliderect(rect_per_3):
                persefona_bila_rect.centerx=rect_per_3.centerx
                persefona_bila_rect.centery=rect_per_3.centery
            elif persefona_bila_rect.colliderect(rect_per_4):
                persefona_bila_rect.centerx=rect_per_4.centerx
                persefona_bila_rect.centery=rect_per_4.centery
            elif persefona_bila_rect.colliderect(rect_per_5):
                persefona_bila_rect.centerx=rect_per_5.centerx
                persefona_bila_rect.centery=rect_per_5.centery
            elif persefona_bila_rect.colliderect(rect_per_6):
                persefona_bila_rect.centerx=rect_per_6.centerx
                persefona_bila_rect.centery=rect_per_6.centery
            elif persefona_bila_rect.colliderect(rect_per_7):
                persefona_bila_rect.centerx=rect_per_7.centerx
                persefona_bila_rect.centery=rect_per_7.centery
            elif persefona_bila_rect.colliderect(rect_per_8):
                persefona_bila_rect.centerx=rect_per_8.centerx
                persefona_bila_rect.centery=rect_per_8.centery
            elif persefona_bila_rect.colliderect(rect_per_9):
                persefona_bila_rect.centerx=rect_per_9.centerx
                persefona_bila_rect.centery=rect_per_9.centery
            else:
                persefona_bila_rect.centerx=persefona_bila_x_pred
                persefona_bila_rect.centery=persefona_bila_y_pred
            if (persefona_bila_rect.right > 1440 or persefona_bila_rect.left < 475) or (persefona_bila_rect.bottom > 1020 or persefona_bila_rect.top < 60):
                persefona_bila_rect.centerx=persefona_bila_x_pred
                persefona_bila_rect.centery=persefona_bila_y_pred

            if kardinal_bily_rect1.colliderect(rect_kar_1):
                kardinal_bily_rect1.centerx=rect_kar_1.centerx
                kardinal_bily_rect1.centery=rect_kar_1.centery
            elif kardinal_bily_rect1.colliderect(rect_kar_2):
                kardinal_bily_rect1.centerx=rect_kar_2.centerx
                kardinal_bily_rect1.centery=rect_kar_2.centery
            elif kardinal_bily_rect1.colliderect(rect_kar_3):
                kardinal_bily_rect1.centerx=rect_kar_3.centerx
                kardinal_bily_rect1.centery=rect_kar_3.centery
            elif kardinal_bily_rect1.colliderect(rect_kar_4):
                kardinal_bily_rect1.centerx=rect_kar_4.centerx
                kardinal_bily_rect1.centery=rect_kar_4.centery
            else:
                kardinal_bily_rect1.centerx=kardinal_bily_x_pred_1
                kardinal_bily_rect1.centery=kardinal_bily_y_pred_1
            if (kardinal_bily_rect1.right > 1440 or kardinal_bily_rect1.left < 475) or (kardinal_bily_rect1.bottom > 1020 or kardinal_bily_rect1.top < 60):
                kardinal_bily_rect1.centerx=kardinal_bily_x_pred_1
                kardinal_bily_rect1.centery=kardinal_bily_y_pred_1

            if arcibiskup_bily_rect1.colliderect(rect_arc_1):
                arcibiskup_bily_rect1.centerx=rect_arc_1.centerx
                arcibiskup_bily_rect1.centery=rect_arc_1.centery
            elif arcibiskup_bily_rect1.colliderect(rect_arc_2):
                arcibiskup_bily_rect1.centerx=rect_arc_2.centerx
                arcibiskup_bily_rect1.centery=rect_arc_2.centery
            elif arcibiskup_bily_rect1.colliderect(rect_arc_3):
                arcibiskup_bily_rect1.centerx=rect_arc_3.centerx
                arcibiskup_bily_rect1.centery=rect_arc_3.centery
            elif arcibiskup_bily_rect1.colliderect(rect_arc_4):
                arcibiskup_bily_rect1.centerx=rect_arc_4.centerx
                arcibiskup_bily_rect1.centery=rect_arc_4.centery
            elif arcibiskup_bily_rect1.colliderect(rect_arc_5):
                arcibiskup_bily_rect1.centerx=rect_arc_5.centerx
                arcibiskup_bily_rect1.centery=rect_arc_5.centery
            elif arcibiskup_bily_rect1.colliderect(rect_arc_6):
                arcibiskup_bily_rect1.centerx=rect_arc_6.centerx
                arcibiskup_bily_rect1.centery=rect_arc_6.centery
            elif arcibiskup_bily_rect1.colliderect(rect_arc_7):
                arcibiskup_bily_rect1.centerx=rect_arc_7.centerx
                arcibiskup_bily_rect1.centery=rect_arc_7.centery
            elif arcibiskup_bily_rect1.colliderect(rect_arc_8):
                arcibiskup_bily_rect1.centerx=rect_arc_8.centerx
                arcibiskup_bily_rect1.centery=rect_arc_8.centery
            elif arcibiskup_bily_rect1.colliderect(rect_arc_9):
                arcibiskup_bily_rect1.centerx=rect_arc_9.centerx
                arcibiskup_bily_rect1.centery=rect_arc_9.centery
            elif arcibiskup_bily_rect1.colliderect(rect_arc_10):
                arcibiskup_bily_rect1.centerx=rect_arc_10.centerx
                arcibiskup_bily_rect1.centery=rect_arc_10.centery
            elif arcibiskup_bily_rect1.colliderect(rect_arc_11):
                arcibiskup_bily_rect1.centerx=rect_arc_11.centerx
                arcibiskup_bily_rect1.centery=rect_arc_11.centery
            elif arcibiskup_bily_rect1.colliderect(rect_arc_12):
                arcibiskup_bily_rect1.centerx=rect_arc_12.centerx
                arcibiskup_bily_rect1.centery=rect_arc_12.centery
            else:
                arcibiskup_bily_rect1.centerx=arcibiskup_bily_x_pred_1
                arcibiskup_bily_rect1.centery=arcibiskup_bily_y_pred_1
            if (arcibiskup_bily_rect1.right > 1440 or arcibiskup_bily_rect1.left < 475) or (arcibiskup_bily_rect1.bottom > 1020 or arcibiskup_bily_rect1.top < 60):
                arcibiskup_bily_rect1.centerx=arcibiskup_bily_x_pred_1
                arcibiskup_bily_rect1.centery=arcibiskup_bily_y_pred_1
            
            if morovy_doktor_bily_rect1.colliderect(rect_mor_1):
                morovy_doktor_bily_rect1.centerx=rect_mor_1.centerx
                morovy_doktor_bily_rect1.centery=rect_mor_1.centery
            elif morovy_doktor_bily_rect1.colliderect(rect_mor_2):
                morovy_doktor_bily_rect1.centerx=rect_mor_2.centerx
                morovy_doktor_bily_rect1.centery=rect_mor_2.centery
            elif morovy_doktor_bily_rect1.colliderect(rect_mor_3):
                morovy_doktor_bily_rect1.centerx=rect_mor_3.centerx
                morovy_doktor_bily_rect1.centery=rect_mor_3.centery
            elif morovy_doktor_bily_rect1.colliderect(rect_mor_4):
                morovy_doktor_bily_rect1.centerx=rect_mor_4.centerx
                morovy_doktor_bily_rect1.centery=rect_mor_4.centery
            elif morovy_doktor_bily_rect1.colliderect(rect_mor_5):
                morovy_doktor_bily_rect1.centerx=rect_mor_5.centerx
                morovy_doktor_bily_rect1.centery=rect_mor_5.centery
            elif morovy_doktor_bily_rect1.colliderect(rect_mor_6):
                morovy_doktor_bily_rect1.centerx=rect_mor_6.centerx
                morovy_doktor_bily_rect1.centery=rect_mor_6.centery
            elif morovy_doktor_bily_rect1.colliderect(rect_mor_7):
                morovy_doktor_bily_rect1.centerx=rect_mor_7.centerx
                morovy_doktor_bily_rect1.centery=rect_mor_7.centery
            elif morovy_doktor_bily_rect1.colliderect(rect_mor_8):
                morovy_doktor_bily_rect1.centerx=rect_mor_8.centerx
                morovy_doktor_bily_rect1.centery=rect_mor_8.centery
            elif morovy_doktor_bily_rect1.colliderect(rect_mor_9):
                morovy_doktor_bily_rect1.centerx=rect_mor_9.centerx
                morovy_doktor_bily_rect1.centery=rect_mor_9.centery
            elif morovy_doktor_bily_rect1.colliderect(rect_mor_10):
                morovy_doktor_bily_rect1.centerx=rect_mor_10.centerx
                morovy_doktor_bily_rect1.centery=rect_mor_10.centery
            elif morovy_doktor_bily_rect1.colliderect(rect_mor_11):
                morovy_doktor_bily_rect1.centerx=rect_mor_11.centerx
                morovy_doktor_bily_rect1.centery=rect_mor_11.centery
            elif morovy_doktor_bily_rect1.colliderect(rect_mor_12):
                morovy_doktor_bily_rect1.centerx=rect_mor_12.centerx
                morovy_doktor_bily_rect1.centery=rect_mor_12.centery
            elif morovy_doktor_bily_rect1.colliderect(rect_mor_13):
                morovy_doktor_bily_rect1.centerx=rect_mor_13.centerx
                morovy_doktor_bily_rect1.centery=rect_mor_13.centery
            elif morovy_doktor_bily_rect1.colliderect(rect_mor_14):
                morovy_doktor_bily_rect1.centerx=rect_mor_14.centerx
                morovy_doktor_bily_rect1.centery=rect_mor_14.centery
            elif morovy_doktor_bily_rect1.colliderect(rect_mor_15):
                morovy_doktor_bily_rect1.centerx=rect_mor_15.centerx
                morovy_doktor_bily_rect1.centery=rect_mor_15.centery
            elif morovy_doktor_bily_rect1.colliderect(rect_mor_16):
                morovy_doktor_bily_rect1.centerx=rect_mor_16.centerx
                morovy_doktor_bily_rect1.centery=rect_mor_16.centery
            elif morovy_doktor_bily_rect1.colliderect(rect_mor_17):
                morovy_doktor_bily_rect1.centerx=rect_mor_17.centerx
                morovy_doktor_bily_rect1.centery=rect_mor_17.centery
            elif morovy_doktor_bily_rect1.colliderect(rect_mor_18):
                morovy_doktor_bily_rect1.centerx=rect_mor_18.centerx
                morovy_doktor_bily_rect1.centery=rect_mor_18.centery
            else:
                morovy_doktor_bily_rect1.centerx=morovy_doktor_bily_x_pred_1
                morovy_doktor_bily_rect1.centery=morovy_doktor_bily_y_pred_1
            if (morovy_doktor_bily_rect1.right > 1440 or morovy_doktor_bily_rect1.left < 475) or (morovy_doktor_bily_rect1.bottom > 1020 or morovy_doktor_bily_rect1.top < 60):
                morovy_doktor_bily_rect1.centerx=morovy_doktor_bily_x_pred_1
                morovy_doktor_bily_rect1.centery=morovy_doktor_bily_y_pred_1

            if valecnik_bily_rect.colliderect(rect_val_1):
                valecnik_bily_rect.centerx=rect_val_1.centerx
                valecnik_bily_rect.centery=rect_val_1.centery
            elif valecnik_bily_rect.colliderect(rect_val_2):
                valecnik_bily_rect.centerx=rect_val_2.centerx
                valecnik_bily_rect.centery=rect_val_2.centery
            elif valecnik_bily_rect.colliderect(rect_val_3):
                valecnik_bily_rect.centerx=rect_val_3.centerx
                valecnik_bily_rect.centery=rect_val_3.centery
            elif valecnik_bily_rect.colliderect(rect_val_4):
                valecnik_bily_rect.centerx=rect_val_4.centerx
                valecnik_bily_rect.centery=rect_val_4.centery
            else:
                valecnik_bily_rect.centerx=valecnik_bily_x_pred
                valecnik_bily_rect.centery=valecnik_bily_y_pred
            if (valecnik_bily_rect.right > 1440 or valecnik_bily_rect.left < 475) or (valecnik_bily_rect.bottom > 1020 or valecnik_bily_rect.top < 60):
                valecnik_bily_rect.centerx=valecnik_bily_x_pred
                valecnik_bily_rect.centery=valecnik_bily_y_pred

            if legionar_bily_rect.colliderect(rect_leg_1):
                legionar_bily_rect.centerx=rect_leg_1.centerx
                legionar_bily_rect.centery=rect_leg_1.centery
            elif legionar_bily_rect.colliderect(rect_leg_2):
                legionar_bily_rect.centerx=rect_leg_2.centerx
                legionar_bily_rect.centery=rect_leg_2.centery
            elif legionar_bily_rect.colliderect(rect_leg_3):
                legionar_bily_rect.centerx=rect_leg_3.centerx
                legionar_bily_rect.centery=rect_leg_3.centery
            else:
                legionar_bily_rect.centerx=legionar_bily_x_pred
                legionar_bily_rect.centery=legionar_bily_y_pred
            if (legionar_bily_rect.right > 1440 or legionar_bily_rect.left < 475) or (legionar_bily_rect.bottom > 1020 or legionar_bily_rect.top < 60):
                legionar_bily_rect.centerx=legionar_bily_x_pred
                legionar_bily_rect.centery=legionar_bily_y_pred

            if valecnik_bily_rect1.colliderect(rect_val_1_1):
                valecnik_bily_rect1.centerx=rect_val_1_1.centerx
                valecnik_bily_rect1.centery=rect_val_1_1.centery
            elif valecnik_bily_rect1.colliderect(rect_val_1_2):
                valecnik_bily_rect1.centerx=rect_val_1_2.centerx
                valecnik_bily_rect1.centery=rect_val_1_2.centery
            elif valecnik_bily_rect1.colliderect(rect_val_1_3):
                valecnik_bily_rect1.centerx=rect_val_1_3.centerx
                valecnik_bily_rect1.centery=rect_val_1_3.centery
            elif valecnik_bily_rect1.colliderect(rect_val_1_4):
                valecnik_bily_rect1.centerx=rect_val_1_4.centerx
                valecnik_bily_rect1.centery=rect_val_1_4.centery
            else:
                valecnik_bily_rect1.centerx=valecnik_bily_x_pred_1
                valecnik_bily_rect1.centery=valecnik_bily_y_pred_1
            if (valecnik_bily_rect1.right > 1440 or valecnik_bily_rect1.left < 475) or (valecnik_bily_rect1.bottom > 1020 or valecnik_bily_rect1.top < 60):
                valecnik_bily_rect1.centerx=valecnik_bily_x_pred_1
                valecnik_bily_rect1.centery=valecnik_bily_y_pred_1
            
            if legionar_bily_rect1.colliderect(rect_leg_1_1):
                legionar_bily_rect1.centerx=rect_leg_1_1.centerx
                legionar_bily_rect1.centery=rect_leg_1_1.centery
            elif legionar_bily_rect1.colliderect(rect_leg_1_2):
                legionar_bily_rect1.centerx=rect_leg_1_2.centerx
                legionar_bily_rect1.centery=rect_leg_1_2.centery
            elif legionar_bily_rect1.colliderect(rect_leg_1_3):
                legionar_bily_rect1.centerx=rect_leg_1_3.centerx
                legionar_bily_rect1.centery=rect_leg_1_3.centery
            else:
                legionar_bily_rect1.centerx=legionar_bily_x_pred_1
                legionar_bily_rect1.centery=legionar_bily_y_pred_1
            if (legionar_bily_rect1.right > 1440 or legionar_bily_rect1.left < 475) or (legionar_bily_rect1.bottom > 1020 or legionar_bily_rect1.top < 60):
                legionar_bily_rect1.centerx=legionar_bily_x_pred_1
                legionar_bily_rect1.centery=legionar_bily_y_pred_1

            if valecnik_bily_rect2.colliderect(rect_val_2_1):
                valecnik_bily_rect2.centerx=rect_val_2_1.centerx
                valecnik_bily_rect2.centery=rect_val_2_1.centery
            elif valecnik_bily_rect2.colliderect(rect_val_2_2):
                valecnik_bily_rect2.centerx=rect_val_2_2.centerx
                valecnik_bily_rect2.centery=rect_val_2_2.centery
            elif valecnik_bily_rect2.colliderect(rect_val_2_3):
                valecnik_bily_rect2.centerx=rect_val_2_3.centerx
                valecnik_bily_rect2.centery=rect_val_2_3.centery
            elif valecnik_bily_rect2.colliderect(rect_val_2_4):
                valecnik_bily_rect2.centerx=rect_val_2_4.centerx
                valecnik_bily_rect2.centery=rect_val_2_4.centery
            else:
                valecnik_bily_rect2.centerx=valecnik_bily_x_pred_2
                valecnik_bily_rect2.centery=valecnik_bily_y_pred_2
            if (valecnik_bily_rect2.right > 1440 or valecnik_bily_rect2.left < 475) or (valecnik_bily_rect2.bottom > 1020 or valecnik_bily_rect2.top < 60):
                valecnik_bily_rect2.centerx=valecnik_bily_x_pred_2
                valecnik_bily_rect2.centery=valecnik_bily_y_pred_2

            if legionar_bily_rect2.colliderect(rect_leg_2_1):
                legionar_bily_rect2.centerx=rect_leg_2_1.centerx
                legionar_bily_rect2.centery=rect_leg_2_1.centery
            elif legionar_bily_rect2.colliderect(rect_leg_2_2):
                legionar_bily_rect2.centerx=rect_leg_2_2.centerx
                legionar_bily_rect2.centery=rect_leg_2_2.centery
            elif legionar_bily_rect2.colliderect(rect_leg_2_3):
                legionar_bily_rect2.centerx=rect_leg_2_3.centerx
                legionar_bily_rect2.centery=rect_leg_2_3.centery
            else:
                legionar_bily_rect2.centerx=legionar_bily_x_pred_2
                legionar_bily_rect2.centery=legionar_bily_y_pred_2
            if (legionar_bily_rect2.right > 1440 or legionar_bily_rect2.left < 475) or (legionar_bily_rect2.bottom > 1020 or legionar_bily_rect2.top < 60):
                legionar_bily_rect2.centerx=legionar_bily_x_pred_2
                legionar_bily_rect2.centery=legionar_bily_y_pred_2
            
            if valecnik_bily_rect3.colliderct(rect_val_3_1):
                valecnik_bily_rect3.centerx=rect_val_3_1.centerx
                valecnik_bily_rect3.centery=rect_val_3_1.centery
            elif valecnik_bily_rect3.colliderct(rect_val_3_2):
                valecnik_bily_rect3.centerx=rect_val_3_2.centerx
                valecnik_bily_rect3.centery=rect_val_3_2.centery
            elif valecnik_bily_rect3.colliderct(rect_val_3_3):
                valecnik_bily_rect3.centerx=rect_val_3_3.centerx
                valecnik_bily_rect3.centery=rect_val_3_3.centery
            elif valecnik_bily_rect3.colliderct(rect_val_3_4):
                valecnik_bily_rect3.centerx=rect_val_3_4.centerx
                valecnik_bily_rect3.centery=rect_val_3_4.centery
            else:
                valecnik_bily_rect3.centerx=valecnik_bily_x_pred_3
                valecnik_bily_rect3.centery=valecnik_bily_y_pred_3
            if (valecnik_bily_rect3.right > 1440 or valecnik_bily_rect3.left < 475) or (valecnik_bily_rect3.bottom > 1020 or valecnik_bily_rect3.top < 60):
                valecnik_bily_rect3.centerx=valecnik_bily_x_pred_3
                valecnik_bily_rect3.centery=valecnik_bily_y_pred_3
            
            if legionar_bily_rect3.colliderect(rect_leg_3_1):
                legionar_bily_rect3.centerx=rect_leg_3_1.centerx
                legionar_bily_rect3.centery=rect_leg_3_1.centery
            elif legionar_bily_rect3.colliderect(rect_leg_3_2):
                legionar_bily_rect3.centerx=rect_leg_3_2.centerx
                legionar_bily_rect3.centery=rect_leg_3_2.centery
            elif legionar_bily_rect3.colliderect(rect_leg_3_3):
                legionar_bily_rect3.centerx=rect_leg_3_3.centerx
                legionar_bily_rect3.centery=rect_leg_3_3.centery
            else:
                legionar_bily_rect3.centerx=legionar_bily_x_pred_3
                legionar_bily_rect3.centery=legionar_bily_y_pred_3
            if (legionar_bily_rect3.right > 1440 or legionar_bily_rect3.left < 475) or (legionar_bily_rect3.bottom > 1020 or legionar_bily_rect3.top < 60):
                legionar_bily_rect3.centerx=legionar_bily_x_pred_3
                legionar_bily_rect3.centery=legionar_bily_y_pred_3
            

            

            
        
        #Kontrola kolize


    pygame.display.update()

    clock.tick(60)

pygame.quit()