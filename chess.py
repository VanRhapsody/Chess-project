
import pygame
import mysql.connector
import random

pygame.init()


# Funkce
def collisionWhite(figurka, figurkaxInit, figurkayInit, counter):
    if figurka.colliderect(plagueDoctorWhiteRect):
        figurka.centerx = figurkaxInit
        figurka.centery = figurkayInit
        counter -= 1
    elif figurka.colliderect(archbishopWhiteRect):
        figurka.centerx = figurkaxInit
        figurka.centery = figurkayInit
        counter -= 1
    elif figurka.colliderect(cardinalWhiteRect):
        figurka.centerx = figurkaxInit
        figurka.centery = figurkayInit
        counter -= 1
    elif figurka.colliderect(persephoneWhiteRect):
        figurka.centerx = figurkaxInit
        figurka.centery = figurkayInit
        counter -= 1
    elif figurka.colliderect(plagueDoctorWhiteRect1):
        figurka.centerx = figurkaxInit
        figurka.centery = figurkayInit
        counter -= 1
    elif figurka.colliderect(cardinalWhiteRect1):
        figurka.centerx = figurkaxInit
        figurka.centery = figurkayInit
        counter -= 1
    elif figurka.colliderect(archbishopWhiteRect1):
        figurka.centerx = figurkaxInit
        figurka.centery = figurkayInit
        counter -= 1
    elif figurka.colliderect(warriorWhiteRect):
        figurka.centerx = figurkaxInit
        figurka.centery = figurkayInit
        counter -= 1
    elif figurka.colliderect(legionaryWhiteRect):
        figurka.centerx = figurkaxInit
        figurka.centery = figurkayInit
        counter -= 1
    elif figurka.colliderect(warriorWhiteRect1):
        figurka.centerx = figurkaxInit
        figurka.centery = figurkayInit
        counter -= 1
    elif figurka.colliderect(legionaryWhiteRect1):
        figurka.centerx = figurkaxInit
        figurka.centery = figurkayInit
        counter -= 1
    elif figurka.colliderect(warriorWhiteRect2):
        figurka.centerx = figurkaxInit
        figurka.centery = figurkayInit
        counter -= 1
    elif figurka.colliderect(legionaryWhiteRect2):
        figurka.centerx = figurkaxInit
        figurka.centery = figurkayInit
        counter -= 1
    elif figurka.colliderect(warriorWhiteRect3):
        figurka.centerx = figurkaxInit
        figurka.centery = figurkayInit
        counter -= 1
    elif figurka.colliderect(legionaryWhiteRect3):
        figurka.centerx = figurkaxInit
        figurka.centery = figurkayInit
        counter -= 1


# Nastavení připojení k databázi
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

screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Šachy dle našeho")

# Nastavení fps
clock = pygame.time.Clock()
fps = 60

# Načtení obrázků figurek
archbishopWhite = pygame.image.load("img/Arcibiskup_bily.png")  # todo=zvětšit jeho velikost
archbishopBlack = pygame.image.load("img/Arcibiskup_cerny.png")
hadesWhite = pygame.image.load("img/Hades_bily.png")
hadesBlack = pygame.image.load("img/Hades_cerny.png")
cardinalWhite = pygame.image.load("img/Kardinal_bily.png")
cardinalBlack = pygame.image.load("img/Kardinal_cerny.png")
legionaryWhite = pygame.image.load("img/Legionar_bily.png")
legionaryBlack = pygame.image.load("img/Legionar_cerny.png")
plagueDoctorWhite = pygame.image.load("img/Morovy_doktor_bily.png")
plagueDoctorBlack = pygame.image.load("img/Morovy_dotkor_cerny.png")
persephoneWhite = pygame.image.load("img/Persefona_bila.png")
persephoneBlack = pygame.image.load("img/Persefona_cerna.png")
warriorWhite = pygame.image.load("img/Valecnik_bily.png")
warriorBlack = pygame.image.load("img/Valecnik_cerny.png")

# Nastavení pozic bílých figurek
plagueDoctorWhiteRect = plagueDoctorWhite.get_rect()
plagueDoctorWhiteRect.center = (540, 120)
archbishopWhiteRect = archbishopWhite.get_rect()
archbishopWhiteRect.center = (660, 120)
cardinalWhiteRect = cardinalWhite.get_rect()
cardinalWhiteRect.center = (780, 120)
hadesWhiteRect = hadesWhite.get_rect()
hadesWhiteRect.center = (900, 120)
persephoneWhiteRect = persephoneWhite.get_rect()
persephoneWhiteRect.center = (1020, 120)
cardinalWhiteRect1 = cardinalWhite.get_rect()
cardinalWhiteRect1.center = (1140, 120)
archbishopWhiteRect1 = archbishopWhite.get_rect()
archbishopWhiteRect1.center = (1260, 120)
plagueDoctorWhiteRect1 = plagueDoctorWhite.get_rect()
plagueDoctorWhiteRect1.center = (1380, 120)
warriorWhiteRect = warriorWhite.get_rect()
warriorWhiteRect.center = (540, 240)
legionaryWhiteRect = legionaryWhite.get_rect()
legionaryWhiteRect.center = (660, 240)
warriorWhiteRect1 = warriorWhite.get_rect()
warriorWhiteRect1.center = (780, 240)
legionaryWhiteRect1 = legionaryWhite.get_rect()
legionaryWhiteRect1.center = (900, 240)
warriorWhiteRect2 = warriorWhite.get_rect()
warriorWhiteRect2.center = (1020, 240)
legionaryWhiteRect2 = legionaryWhite.get_rect()
legionaryWhiteRect2.center = (1140, 240)
warriorWhiteRect3 = warriorWhite.get_rect()
warriorWhiteRect3.center = (1260, 240)
legionaryWhiteRect3 = legionaryWhite.get_rect()
legionaryWhiteRect3.center = (1380, 240)

# Nastavení pozic černých figurek
plagueDoctorBlackRect = plagueDoctorBlack.get_rect()
plagueDoctorBlackRect.center = (540, 960)
archbishopBlackRect = archbishopBlack.get_rect()
archbishopBlackRect.center = (660, 960)
cardinalBlackRect = cardinalBlack.get_rect()
cardinalBlackRect.center = (780, 960)
hadesBlackRect = hadesBlack.get_rect()
hadesBlackRect.center = (900, 960)
persephoneBlackRect = persephoneBlack.get_rect()
persephoneBlackRect.center = (1020, 960)
cardinalBlackRect1 = cardinalBlack.get_rect()
cardinalBlackRect1.center = (1140, 960)
archbishopBlackRect1 = archbishopBlack.get_rect()
archbishopBlackRect1.center = (1260, 960)
plagueDoctorBlackRect1 = plagueDoctorBlack.get_rect()
plagueDoctorBlackRect1.center = (1380, 960)
legionaryBlackRect = legionaryBlack.get_rect()
legionaryBlackRect.center = (540, 840)
warriorBlackRect = warriorBlack.get_rect()
warriorBlackRect.center = (660, 840)
legionaryBlackRect1 = legionaryBlack.get_rect()
legionaryBlackRect1.center = (780, 840)
warriorBlackRect1 = warriorBlack.get_rect()
warriorBlackRect1.center = (900, 840)
legionaryBlackRect2 = legionaryBlack.get_rect()
legionaryBlackRect2.center = (1020, 840)
warriorBlackRect2 = warriorBlack.get_rect()
warriorBlackRect2.center = (1140, 840)
legionaryBlackRect3 = legionaryBlack.get_rect()
legionaryBlackRect3.center = (1260, 840)
warriorBlackRect3 = warriorBlack.get_rect()
warriorBlackRect3.center = (1380, 840)

# Deklarace barev
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
active_color = (255, 255, 255)
passive_collor = (180, 180, 180)
# Nastavení pozadí
background_image = pygame.image.load("loginpozadi.jpg")
background_image_rect = background_image.get_rect()
background_image_rect.center = (screen_width / 2, screen_height / 2)

# Hudba v pozadí
songs = ["Anguish.mp3", "Bleach OST 3-Clavar La Espada.mp3", "y2mate.com - Kyrie Ⅱ.mp3", "Nube Negra.mp3",
         "y2mate.com - American Prometheus.mp3"]
song = random.choice(songs)
pygame.mixer.music.load(song)
pygame.mixer.music.play(1, 0)

# Texty pro buttony a samotné buttony

button = pygame.Rect(810, 360, 300, 80)
button_font = pygame.font.SysFont("georgia", 40, False)
button_text_start_game = button_font.render("Začít hru", True, black)
button_text_start_game_rect = button_text_start_game.get_rect()
button_text_start_game_rect.center = (screen_width / 2, 400)

button1 = pygame.Rect(810, 460, 300, 80)

button_text_start_game1 = button_font.render("Nightmare mode", True, black)
button_text_start_game_rect1 = button_text_start_game1.get_rect()
button_text_start_game_rect1.center = (screen_width / 2, 500)

button2 = pygame.Rect(810, 560, 300, 80)

button_text_start_game2 = button_font.render("Ukončit hru", True, black)
button_text_start_game_rect2 = button_text_start_game2.get_rect()
button_text_start_game_rect2.center = (screen_width / 2, 600)

# Text pro leaderboard a pozadí pro ni
leaderboard_font = pygame.font.SysFont("georgia", 80, False)
leadeboard_text_font = pygame.font.SysFont("georgia", 50, False)
leaderboard_text = leaderboard_font.render("Leaderboard", True, white)
leaderboard_text_rect = leaderboard_text.get_rect()
leaderboard_text_rect.center = (1650, 60)
leaderboard_background = pygame.Rect(1400, 10, 500, 1050)

# Zvuk zahájení hry
start_game = pygame.mixer.Sound("Sound effect bell.mp3")

# Text pro input
header_font = pygame.font.SysFont("georgia", 50, False)
input_font = pygame.font.SysFont("georgia", 40, False)
mail_header = header_font.render("Zadejte E-Mail", True, white)
mail_header_rect = mail_header.get_rect()
mail_header_rect.midleft = (100, 300)
input_box1 = pygame.rect.Rect(100, 350, 2000, 70)
input_user_text1 = ''

pass_header = header_font.render("Zadejte heslo", True, white)
pass_header_rect = pass_header.get_rect()
pass_header_rect.midleft = (100, 460)
input_box2 = pygame.rect.Rect(100, 510, 2000, 70)
input_user_text2 = ''
inputUserText2Hidden = ''  # slouží pro zobrazení hvězdiček v poli pro heslo při psaní

send_header = header_font.render("Přihlásit se", True, black)
send_header_rect = send_header.get_rect()
send_header_rect.midleft = (100, 645)
send_box = pygame.rect.Rect(100, 607, 250, 75)

# Text pro oznámení přihlášení
logged_header = header_font.render("Úspěšně přihlášeno", True, white)
logged_header_rect = logged_header.get_rect()
logged_header_rect.midleft = (100, 715)

failed_header = header_font.render("Neplatné údaje", True, white)
failed_header_rect = failed_header.get_rect()
failed_header_rect.midleft = (100, 710)

fill_header = header_font.render("Vyplňte prosím všechna pole", True, white)
fill_header_rect = fill_header.get_rect()
fill_header_rect.midleft = (100, 710)

# Text pro název hry
title_font = pygame.font.SysFont("georgia", 80, False)
title_header = title_font.render("Our Chess", True, white)
title_header_rect = title_header.get_rect()
title_header_rect.center = (screen_width / 2, 300)

# Zjištění konce hudby v hlavním menu
music_end = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(music_end)

# region figurky

# Získání pozic čtverců (nápověd) pro pohyb figurek

step = 120

# Morový doktor bílý
rectsPlagueDoctorWhite = []

rectPlagueWhitex1 = plagueDoctorWhiteRect.centerx + step
rectPlagueWhitey1 = plagueDoctorWhiteRect.centery
rectPlagueWhite1 = pygame.Rect(rectPlagueWhitex1 - 30, rectPlagueWhitey1 - 30, 60, 60)
rectsPlagueDoctorWhite.append(rectPlagueWhite1)

rectPlagueWhitex2 = plagueDoctorWhiteRect.centerx + step * 2
rectPlagueWhitey2 = plagueDoctorWhiteRect.centery
rectPlagueWhite2 = pygame.Rect(rectPlagueWhitex2 - 30, rectPlagueWhitey2 - 30, 60, 60)
rectsPlagueDoctorWhite.append(rectPlagueWhite2)

rectPlagueWhitex3 = plagueDoctorWhiteRect.centerx - step
rectPlagueWhitey3 = plagueDoctorWhiteRect.centery
rectPlagueWhite3 = pygame.Rect(rectPlagueWhitex3 - 30, rectPlagueWhitey3 - 30, 60, 60)
rectsPlagueDoctorWhite.append(rectPlagueWhite3)

rectPlagueWhitex4 = plagueDoctorWhiteRect.centerx - 2 * step
rectPlagueWhitey4 = plagueDoctorWhiteRect.centery
rectPlagueWhite4 = pygame.Rect(rectPlagueWhitex4 - 30, rectPlagueWhitey4 - 30, 60, 60)
rectsPlagueDoctorWhite.append(rectPlagueWhite4)

rectPlagueWhitex5 = plagueDoctorWhiteRect.centerx
rectPlagueWhitey5 = plagueDoctorWhiteRect.centery + step
rectPlagueWhite5 = pygame.Rect(rectPlagueWhitex5 - 30, rectPlagueWhitey5 - 30, 60, 60)
rectsPlagueDoctorWhite.append(rectPlagueWhite5)

rectPlagueWhitex6 = plagueDoctorWhiteRect.centerx
rectPlagueWhitey6 = plagueDoctorWhiteRect.centery + step * 2
rectPlagueWhite6 = pygame.Rect(rectPlagueWhitex6 - 30, rectPlagueWhitey6 - 30, 60, 60)
rectsPlagueDoctorWhite.append(rectPlagueWhite6)

rectPlagueWhitex7 = plagueDoctorWhiteRect.centerx
rectPlagueWhitey7 = plagueDoctorWhiteRect.centery + step * 3
rectPlagueWhite7 = pygame.Rect(rectPlagueWhitex7 - 30, rectPlagueWhitey7 - 30, 60, 60)
rectsPlagueDoctorWhite.append(rectPlagueWhite7)

rectPlagueWhitex8 = plagueDoctorWhiteRect.centerx
rectPlagueWhitey8 = plagueDoctorWhiteRect.centery + step * 4
rectPlagueWhite8 = pygame.Rect(rectPlagueWhitex8 - 30, rectPlagueWhitey8 - 30, 60, 60)
rectsPlagueDoctorWhite.append(rectPlagueWhite8)

rectPlagueWhitex9 = plagueDoctorWhiteRect.centerx
rectPlagueWhitey9 = plagueDoctorWhiteRect.centery + step * 5
rectPlagueWhite9 = pygame.Rect(rectPlagueWhitex9 - 30, rectPlagueWhitey9 - 30, 60, 60)
rectsPlagueDoctorWhite.append(rectPlagueWhite9)

rectPlagueWhitex10 = plagueDoctorWhiteRect.centerx
rectPlagueWhitey10 = plagueDoctorWhiteRect.centery + step * 6
rectPlagueWhite10 = pygame.Rect(rectPlagueWhitex10 - 30, rectPlagueWhitey10 - 30, 60, 60)
rectsPlagueDoctorWhite.append(rectPlagueWhite10)

rectPlagueWhitex11 = plagueDoctorWhiteRect.centerx
rectPlagueWhitey11 = plagueDoctorWhiteRect.centery + step * 7
rectPlagueWhite11 = pygame.Rect(rectPlagueWhitex11 - 30, rectPlagueWhitey11 - 30, 60, 60)
rectsPlagueDoctorWhite.append(rectPlagueWhite11)

rectPlagueWhitex12 = plagueDoctorWhiteRect.centerx
rectPlagueWhitey12 = plagueDoctorWhiteRect.centery - step
rectPlagueWhite12 = pygame.Rect(rectPlagueWhitex12 - 30, rectPlagueWhitey12 - 30, 60, 60)
rectsPlagueDoctorWhite.append(rectPlagueWhite12)

rectPlagueWhitex13 = plagueDoctorWhiteRect.centerx
rectPlagueWhitey13 = plagueDoctorWhiteRect.centery - step * 2
rectPlagueWhite13 = pygame.Rect(rectPlagueWhitex13 - 30, rectPlagueWhitey13 - 30, 60, 60)
rectsPlagueDoctorWhite.append(rectPlagueWhite13)

rectPlagueWhitex14 = plagueDoctorWhiteRect.centerx
rectPlagueWhitey14 = plagueDoctorWhiteRect.centery - step * 3
rectPlagueWhite14 = pygame.Rect(rectPlagueWhitex14 - 30, rectPlagueWhitey14 - 30, 60, 60)
rectsPlagueDoctorWhite.append(rectPlagueWhite14)

rectPlagueWhitex15 = plagueDoctorWhiteRect.centerx
rectPlagueWhitey15 = plagueDoctorWhiteRect.centery - step * 4
rectPlagueWhite15 = pygame.Rect(rectPlagueWhitex15 - 30, rectPlagueWhitey15 - 30, 60, 60)
rectsPlagueDoctorWhite.append(rectPlagueWhite15)

rectPlagueWhitex16 = plagueDoctorWhiteRect.centerx
rectPlagueyWhite16 = plagueDoctorWhiteRect.centery - step * 5
rectPlagueWhite16 = pygame.Rect(rectPlagueWhitex16 - 30, rectPlagueyWhite16 - 30, 60, 60)
rectsPlagueDoctorWhite.append(rectPlagueWhite16)

rectPlagueWhitex17 = plagueDoctorWhiteRect.centerx
rectPlagueWhitey17 = plagueDoctorWhiteRect.centery - step * 6
rectPlagueWhite17 = pygame.Rect(rectPlagueWhitex17 - 30, rectPlagueWhitey17 - 30, 60, 60)
rectsPlagueDoctorWhite.append(rectPlagueWhite17)

rectPlagueWhitex18 = plagueDoctorWhiteRect.centerx
rectPlagueWhitey18 = plagueDoctorWhiteRect.centery - step * 7
rectPlagueWhite18 = pygame.Rect(rectPlagueWhitex18 - 30, rectPlagueWhitey18 - 30, 60, 60)
rectsPlagueDoctorWhite.append(rectPlagueWhite18)

# Arcibiskup bílý
rectsArchbishopWhite = []

rectArchbishopWhitex1 = archbishopWhiteRect.centerx + step * 2
rectArchbishopWhitey1 = archbishopWhiteRect.centery
rectArchbishopWhite1 = pygame.Rect(rectArchbishopWhitex1 - 30, rectArchbishopWhitey1 - 30, 60, 60)
rectsArchbishopWhite.append(rectArchbishopWhite1)

rectArchbishopWhitex2 = archbishopWhiteRect.centerx + step * 2
rectArchbishopWhitey2 = archbishopWhiteRect.centery + step
rectArchbishopWhite2 = pygame.Rect(rectArchbishopWhitex2 - 30, rectArchbishopWhitey2 - 30, 60, 60)
rectsArchbishopWhite.append(rectArchbishopWhite2)

rectArchbishopWhitex3 = archbishopWhiteRect.centerx + step * 2
rectArchbishopWhitey3 = archbishopWhiteRect.centery - step
rectArchbishopWhite3 = pygame.Rect(rectArchbishopWhitex3 - 30, rectArchbishopWhitey3 - 30, 60, 60)
rectsArchbishopWhite.append(rectArchbishopWhite3)

rectArchbishopWhitex4 = archbishopWhiteRect.centerx - step * 2
rectArchbishopWhitey4 = archbishopWhiteRect.centery
rectArchbishopWhite4 = pygame.Rect(rectArchbishopWhitex4 - 30, rectArchbishopWhitey4 - 30, 60, 60)
rectsArchbishopWhite.append(rectArchbishopWhite4)

rectArchbishopWhitex5 = archbishopWhiteRect.centerx - step * 2
rectArchbishopWhitey5 = archbishopWhiteRect.centery + step
rectArchbishopWhite5 = pygame.Rect(rectArchbishopWhitex5 - 30, rectArchbishopWhitey5 - 30, 60, 60)
rectsArchbishopWhite.append(rectArchbishopWhite5)

rectArchbishopWhitex6 = archbishopWhiteRect.centerx - step * 2
rectArchbishopWhitey6 = archbishopWhiteRect.centery - step
rectArchbishopWhite6 = pygame.Rect(rectArchbishopWhitex6 - 30, rectArchbishopWhitey6 - 30, 60, 60)
rectsArchbishopWhite.append(rectArchbishopWhite6)

rectArchbishopWhitex7 = archbishopWhiteRect.centerx
rectArchbishopWhitey7 = archbishopWhiteRect.centery + step * 2
rectArchbishopWhite7 = pygame.Rect(rectArchbishopWhitex7 - 30, rectArchbishopWhitey7 - 30, 60, 60)
rectsArchbishopWhite.append(rectArchbishopWhite7)

rectArchbishopWhitex8 = archbishopWhiteRect.centerx + step
rectArchbishopWhitey8 = archbishopWhiteRect.centery + step * 2
rectArchbishopWhite8 = pygame.Rect(rectArchbishopWhitex8 - 30, rectArchbishopWhitey8 - 30, 60, 60)
rectsArchbishopWhite.append(rectArchbishopWhite8)

rectArchbishopWhitex9 = archbishopWhiteRect.centerx - step
rectArchbishopWhitey9 = archbishopWhiteRect.centery + step * 2
rectArchbishopWhite9 = pygame.Rect(rectArchbishopWhitex9 - 30, rectArchbishopWhitey9 - 30, 60, 60)
rectsArchbishopWhite.append(rectArchbishopWhite9)

rectArchbishopWhitex10 = archbishopWhiteRect.centerx
rectArchbishopWhitey10 = archbishopWhiteRect.centery - step * 2
rectArchbishopWhite10 = pygame.Rect(rectArchbishopWhitex10 - 30, rectArchbishopWhitey10 - 30, 60, 60)
rectsArchbishopWhite.append(rectArchbishopWhite10)

rectArchbishopWhitex11 = archbishopWhiteRect.centerx + step
rectArchbishopWhitey11 = archbishopWhiteRect.centery - step * 2
rectArchbishopWhite11 = pygame.Rect(rectArchbishopWhitex11 - 30, rectArchbishopWhitey11 - 30, 60, 60)
rectsArchbishopWhite.append(rectArchbishopWhite11)

rectArchbishopWhitex12 = archbishopWhiteRect.centerx - step
rectArchbishopWhitey12 = archbishopWhiteRect.centery - step * 2
rectArchbishopWhite12 = pygame.Rect(rectArchbishopWhitex12 - 30, rectArchbishopWhitey12 - 30, 60, 60)
rectsArchbishopWhite.append(rectArchbishopWhite12)

# Kardinál bílý
rectsCardinalWhite = []

rectCardinalWhitex1 = cardinalWhiteRect.centerx + step
rectCardinalWhitey1 = cardinalWhiteRect.centery - step
rectCardinalWhite1 = pygame.Rect(rectCardinalWhitex1 - 30, rectCardinalWhitey1 - 30, 60, 60)
rectsCardinalWhite.append(rectCardinalWhite1)

rectCardinalWhitex2 = cardinalWhiteRect.centerx - step
rectCardinalWhitey2 = cardinalWhiteRect.centery - step
rectCardinalWhite2 = pygame.Rect(rectCardinalWhitex2 - 30, rectCardinalWhitey2 - 30, 60, 60)
rectsCardinalWhite.append(rectCardinalWhite2)

rectCardinalWhitex3 = cardinalWhiteRect.centerx + step
rectCardinalWhitey3 = cardinalWhiteRect.centery + step
rectCardinalWhite3 = pygame.Rect(rectCardinalWhitex3 - 30, rectCardinalWhitey3 - 30, 60, 60)
rectsCardinalWhite.append(rectCardinalWhite3)

rectCardinalWhitex4 = cardinalWhiteRect.centerx - step
rectCardinalWhitey4 = cardinalWhiteRect.centery + step
rectCardinalWhite4 = pygame.Rect(rectCardinalWhitex4 - 30, rectCardinalWhitey4 - 30, 60, 60)
rectsCardinalWhite.append(rectCardinalWhite4)

# Hádes bílý
rectsHadesWhite = []

rectHadesWhitex1 = hadesWhiteRect.centerx
rectHadesWhitey1 = hadesWhiteRect.centery - step
rectHadesWhite1 = pygame.Rect(rectHadesWhitex1 - 30, rectHadesWhitey1 - 30, 60, 60)
rectsHadesWhite.append(rectHadesWhite1)

rectHadesWhitex2 = hadesWhiteRect.centerx
rectHadesWhitey2 = hadesWhiteRect.centery - step * 2
rectHadesWhite2 = pygame.Rect(rectHadesWhitex2 - 30, rectHadesWhitey2 - 30, 60, 60)
rectsHadesWhite.append(rectHadesWhite2)

rectHadesWhitex3 = hadesWhiteRect.centerx
rectHadesWhitey3 = hadesWhiteRect.centery - step * 3
rectHadesWhite3 = pygame.Rect(rectHadesWhitex3 - 30, rectHadesWhitey3 - 30, 60, 60)
rectsHadesWhite.append(rectHadesWhite3)

rectHadesWhitex4 = hadesWhiteRect.centerx + step
rectHadesWhitey4 = hadesWhiteRect.centery - step
rectHadesWhite4 = pygame.Rect(rectHadesWhitex4 - 30, rectHadesWhitey4 - 30, 60, 60)
rectsHadesWhite.append(rectHadesWhite4)

rectHadesWhitex5 = hadesWhiteRect.centerx + step * 2
rectHadesWhitey5 = hadesWhiteRect.centery - step * 2
rectHadesWhite5 = pygame.Rect(rectHadesWhitex5 - 30, rectHadesWhitey5 - 30, 60, 60)
rectsHadesWhite.append(rectHadesWhite5)

rectHadesWhitex6 = hadesWhiteRect.centerx + step * 3
rectHadesWhitey6 = hadesWhiteRect.centery - step * 3
rectHadesWhite6 = pygame.Rect(rectHadesWhitex6 - 30, rectHadesWhitey6 - 30, 60, 60)
rectsHadesWhite.append(rectHadesWhite6)

rectHadesWhitex7 = hadesWhiteRect.centerx + step
rectHadesWhitey7 = hadesWhiteRect.centery
rectHadesWhite7 = pygame.Rect(rectHadesWhitex7 - 30, rectHadesWhitey7 - 30, 60, 60)
rectsHadesWhite.append(rectHadesWhite7)

rectHadesWhitex8 = hadesWhiteRect.centerx + step * 2
rectHadesWhitey8 = hadesWhiteRect.centery
rectHadesWhite8 = pygame.Rect(rectHadesWhitex8 - 30, rectHadesWhitey8 - 30, 60, 60)
rectsHadesWhite.append(rectHadesWhite8)

rectHadesWhitex9 = hadesWhiteRect.centerx + step * 3
rectHadesWhitey9 = hadesWhiteRect.centery
rectHadesWhite9 = pygame.Rect(rectHadesWhitex9 - 30, rectHadesWhitey9 - 30, 60, 60)
rectsHadesWhite.append(rectHadesWhite9)

rectHadesWhitex10 = hadesWhiteRect.centerx + step
rectHadesWhitey10 = hadesWhiteRect.centery + step
rectHadesWhite10 = pygame.Rect(rectHadesWhitex10 - 30, rectHadesWhitey10 - 30, 60, 60)
rectsHadesWhite.append(rectHadesWhite10)

rectHadesWhitex11 = hadesWhiteRect.centerx + step * 2
rectHadesWhitey11 = hadesWhiteRect.centery + step * 2
rectHadesWhite11 = pygame.Rect(rectHadesWhitex11 - 30, rectHadesWhitey11 - 30, 60, 60)
rectsHadesWhite.append(rectHadesWhite11)

rectHadesWhitex12 = hadesWhiteRect.centerx - step
rectHadesWhitey12 = hadesWhiteRect.centery - step
rectHadesWhite12 = pygame.Rect(rectHadesWhitex12 - 30, rectHadesWhitey12 - 30, 60, 60)
rectsHadesWhite.append(rectHadesWhite12)

rectHadesWhitex13 = hadesWhiteRect.centerx - step * 2
rectHadesWhitey13 = hadesWhiteRect.centery - step * 2
rectHadesWhite13 = pygame.Rect(rectHadesWhitex13 - 30, rectHadesWhitey13 - 30, 60, 60)
rectsHadesWhite.append(rectHadesWhite13)

rectHadesWhitex14 = hadesWhiteRect.centerx - step * 3
rectHadesWhitey14 = hadesWhiteRect.centery - step * 3
rectHadesWhite14 = pygame.Rect(rectHadesWhitex14 - 30, rectHadesWhitey14 - 30, 60, 60)
rectsHadesWhite.append(rectHadesWhite14)

rectHadesWhitex15 = hadesWhiteRect.centerx - step
rectHadesWhitey15 = hadesWhiteRect.centery
rectHadesWhite15 = pygame.Rect(rectHadesWhitex15 - 30, rectHadesWhitey15 - 30, 60, 60)
rectsHadesWhite.append(rectHadesWhite15)

rectHadesWhitex16 = hadesWhiteRect.centerx - step * 2
rectHadesWhitey16 = hadesWhiteRect.centery
rectHadesWhite16 = pygame.Rect(rectHadesWhitex16 - 30, rectHadesWhitey16 - 30, 60, 60)
rectsHadesWhite.append(rectHadesWhite16)

rectHadesWhitex17 = hadesWhiteRect.centerx - step * 3
rectHadesWhitey17 = hadesWhiteRect.centery
rectHadesWhite17 = pygame.Rect(rectHadesWhitex17 - 30, rectHadesWhitey17 - 30, 60, 60)
rectsHadesWhite.append(rectHadesWhite17)

rectHadesWhitex18 = hadesWhiteRect.centerx - step
rectHadesWhitey18 = hadesWhiteRect.centery + step
rectHadesWhite18 = pygame.Rect(rectHadesWhitex18 - 30, rectHadesWhitey18 - 30, 60, 60)
rectsHadesWhite.append(rectHadesWhite18)

rectHadesWhitex19 = hadesWhiteRect.centerx - step * 2
rectHadesWhitey19 = hadesWhiteRect.centery + step * 2
rectHadesWhite19 = pygame.Rect(rectHadesWhitex19 - 30, rectHadesWhitey19 - 30, 60, 60)
rectsHadesWhite.append(rectHadesWhite19)

# Persefona bílá
rectsPersephoneWhite = []

rectPersephoneWhitex1 = persephoneWhiteRect.centerx + step
rectPersephoneWhitey1 = persephoneWhiteRect.centery
rectPersephoneWhite1 = pygame.Rect(rectPersephoneWhitex1 - 30, rectPersephoneWhitey1 - 30, 60, 60)
rectsPersephoneWhite.append(rectPersephoneWhite1)

rectPersephoneWhitex2 = persephoneWhiteRect.centerx + step
rectPersephoneWhitey2 = persephoneWhiteRect.centery - step
rectPersephoneWhite2 = pygame.Rect(rectPersephoneWhitex2 - 30, rectPersephoneWhitey2 - 30, 60, 60)
rectsPersephoneWhite.append(rectPersephoneWhite2)

rectPersephoneWhitex3 = persephoneWhiteRect.centerx
rectPersephoneWhitey3 = persephoneWhiteRect.centery - step
rectPersephoneWhite3 = pygame.Rect(rectPersephoneWhitex3 - 30, rectPersephoneWhitey3 - 30, 60, 60)
rectsPersephoneWhite.append(rectPersephoneWhite3)

rectPersephoneWhitex4 = persephoneWhiteRect.centerx - step
rectPersephoneWhitey4 = persephoneWhiteRect.centery - step
rectPersephoneWhite4 = pygame.Rect(rectPersephoneWhitex4 - 30, rectPersephoneWhitey4 - 30, 60, 60)
rectsPersephoneWhite.append(rectPersephoneWhite4)

rectPersephoneWhitex5 = persephoneWhiteRect.centerx - step
rectPersephoneWhitey5 = persephoneWhiteRect.centery
rectPersephoneWhite5 = pygame.Rect(rectPersephoneWhitex5 - 30, rectPersephoneWhitey5 - 30, 60, 60)
rectsPersephoneWhite.append(rectPersephoneWhite5)

rectPersephoneWhitex6 = persephoneWhiteRect.centerx - step
rectPersephoneWhitey6 = persephoneWhiteRect.centery + step
rectPersephoneWhite6 = pygame.Rect(rectPersephoneWhitex6 - 30, rectPersephoneWhitey6 - 30, 60, 60)
rectsPersephoneWhite.append(rectPersephoneWhite6)

rectPersephoneWhitex7 = persephoneWhiteRect.centerx
rectPersephoneWhitey7 = persephoneWhiteRect.centery + step
rectPersephoneWhite7 = pygame.Rect(rectPersephoneWhitex7 - 30, rectPersephoneWhitey7 - 30, 60, 60)
rectsPersephoneWhite.append(rectPersephoneWhite7)

rectPersephoneWhitex8 = persephoneWhiteRect.centerx
rectPersephoneWhitey8 = persephoneWhiteRect.centery + step
rectPersephoneWhite8 = pygame.Rect(rectPersephoneWhitex8 - 30, rectPersephoneWhitey8 - 30, 60, 60)
rectsPersephoneWhite.append(rectPersephoneWhite8)

rectPersephoneWhitex9 = persephoneWhiteRect.centerx + step
rectPersephoneWhitey9 = persephoneWhiteRect.centery + step
rectPersephoneWhite9 = pygame.Rect(rectPersephoneWhitex9 - 30, rectPersephoneWhitey9 - 30, 60, 60)
rectsPersephoneWhite.append(rectPersephoneWhite9)

# Kardinál bílý 1
rectsCardinalWhite_1 = []

rectCardinalWhitex1_1 = cardinalWhiteRect1.centerx + step
rectCardinalWhitey1_1 = cardinalWhiteRect1.centery - step
rectCardinalWhite1_1 = pygame.Rect(rectCardinalWhitex1_1 - 30, rectCardinalWhitey1_1 - 30, 60, 60)
rectsCardinalWhite_1.append(rectCardinalWhite1_1)

rectCardinalWhitex2_1 = cardinalWhiteRect1.centerx + step
rectCardinalWhitey2_1 = cardinalWhiteRect1.centery + step
rectCardinalWhite2_1 = pygame.Rect(rectCardinalWhitex2_1 - 30, rectCardinalWhitey2_1 - 30, 60, 60)
rectsCardinalWhite_1.append(rectCardinalWhite2_1)

rectCardinalWhitex3_1 = cardinalWhiteRect1.centerx - step
rectCardinalWhitey3_1 = cardinalWhiteRect1.centery - step
rectCardinalWhite3_1 = pygame.Rect(rectCardinalWhitex3_1 - 30, rectCardinalWhitey3_1 - 30, 60, 60)
rectsCardinalWhite_1.append(rectCardinalWhite3_1)

rectCardinalWhitex4_1 = cardinalWhiteRect1.centerx - step
rectCardinalWhitey4_1 = cardinalWhiteRect1.centery + step
rectCardinalWhite4_1 = pygame.Rect(rectCardinalWhitex4_1 - 30, rectCardinalWhitey3_1 - 30, 60, 60)
rectsCardinalWhite_1.append(rectCardinalWhite4_1)

# Arcibiskup bílý 1
rectsArchbishopWhite_1 = []

rectArchbishopWhitex1_1 = archbishopWhiteRect1.centerx + step * 2
rectArchbishopWhitey1_1 = archbishopWhiteRect1.centery
rectArchbishopWhite1_1 = pygame.Rect(rectArchbishopWhitex1_1 - 30, rectArchbishopWhitey1_1 - 30, 60, 60)
rectsArchbishopWhite_1.append(rectArchbishopWhite1_1)

rectArchbishopWhitex2_1 = archbishopWhiteRect1.centerx + step * 2
rectArchbishopWhitey2_1 = archbishopWhiteRect1.centery - step
rectArchbishopWhite2_1 = pygame.Rect(rectArchbishopWhitex2_1 - 30, rectArchbishopWhitey2_1 - 30, 60, 60)
rectsArchbishopWhite_1.append(rectArchbishopWhite2_1)

rectArchbishopWhitex3_1 = archbishopWhiteRect1.centerx + step * 2
rectArchbishopWhitey3_1 = archbishopWhiteRect1.centery + step
rectArchbishopWhite3_1 = pygame.Rect(rectArchbishopWhitex3_1 - 30, rectArchbishopWhitey3_1 - 30, 60, 60)
rectsArchbishopWhite_1.append(rectArchbishopWhite3_1)

rectArchbishopWhitex4_1 = archbishopWhiteRect1.centerx
rectArchbishopWhitey4_1 = archbishopWhiteRect1.centery + step * 2
rectArchbishopWhite4_1 = pygame.Rect(rectArchbishopWhitex4_1 - 30, rectArchbishopWhitey4_1 - 30, 60, 60)
rectsArchbishopWhite_1.append(rectArchbishopWhite4_1)

rectArchbishopWhitex5_1 = archbishopWhiteRect1.centerx + step
rectArchbishopWhitey5_1 = archbishopWhiteRect1.centery + step * 2
rectArchbishopWhite5_1 = pygame.Rect(rectArchbishopWhitex5_1 - 30, rectArchbishopWhitey5_1 - 30, 60, 60)
rectsArchbishopWhite_1.append(rectArchbishopWhite5_1)

rectArchbishopWhitex6_1 = archbishopWhiteRect1.centerx - step
rectArchbishopWhitey6_1 = archbishopWhiteRect1.centery + step * 2
rectArchbishopWhite6_1 = pygame.Rect(rectArchbishopWhitex6_1 - 30, rectArchbishopWhitey6_1 - 30, 60, 60)
rectsArchbishopWhite_1.append(rectArchbishopWhite6_1)

rectArchbishopWhitex7_1 = archbishopWhiteRect1.centerx - step * 2
rectArchbishopWhitey7_1 = archbishopWhiteRect1.centery
rectArchbishopWhite7_1 = pygame.Rect(rectArchbishopWhitex7_1 - 30, rectArchbishopWhitey7_1 - 30, 60, 60)
rectsArchbishopWhite_1.append(rectArchbishopWhite7_1)

rectArchbishopWhitex8_1 = archbishopWhiteRect1.centerx - step * 2
rectArchbishopWhitey8_1 = archbishopWhiteRect1.centery - step
rectArchbishopWhite8_1 = pygame.Rect(rectArchbishopWhitex8_1 - 30, rectArchbishopWhitey8_1 - 30, 60, 60)
rectsArchbishopWhite_1.append(rectArchbishopWhite8_1)

rectArchbishopWhitex9_1 = archbishopWhiteRect1.centerx - step * 2
rectArchbishopWhitey9_1 = archbishopWhiteRect1.centery + step
rectArchbishopWhite9_1 = pygame.Rect(rectArchbishopWhitex9_1 - 30, rectArchbishopWhitey9_1 - 30, 60, 60)
rectsArchbishopWhite_1.append(rectArchbishopWhite9_1)

rectArchbishopWhitex10_1 = archbishopWhiteRect1.centerx
rectArchbishopWhitey10_1 = archbishopWhiteRect1.centery - step * 2
rectArchbishopWhite10_1 = pygame.Rect(rectArchbishopWhitex10_1 - 30, rectArchbishopWhitey10_1 - 30, 60, 60)
rectsArchbishopWhite_1.append(rectArchbishopWhite10_1)

rectArchbishopWhitex11_1 = archbishopWhiteRect1.centerx + step
rectArchbishopWhitey11_1 = archbishopWhiteRect1.centery - step * 2
rectArchbishopWhite11_1 = pygame.Rect(rectArchbishopWhitex11_1 - 30, rectArchbishopWhitey11_1 - 30, 60, 60)
rectsArchbishopWhite_1.append(rectArchbishopWhite11_1)

rectArchbishopWhitex12_1 = archbishopWhiteRect1.centerx - step
rectArchbishopWhitey12_1 = archbishopWhiteRect1.centery - step * 2
rectArchbishopWhite12_1 = pygame.Rect(rectArchbishopWhitex12_1 - 30, rectArchbishopWhitey12_1 - 30, 60, 60)
rectsArchbishopWhite_1.append(rectArchbishopWhite12_1)

# Morový doktor bílý 1
rectsPlagueDoctorWhite_1 = []

rectPlagueWhitex1_1 = plagueDoctorWhiteRect1.centerx
rectPlagueWhitey1_1 = plagueDoctorWhiteRect1.centery + step
rectPlagueWhite1_1 = pygame.Rect(rectPlagueWhitex1_1 - 30, rectPlagueWhitey1_1 - 30, 60, 60)
rectsPlagueDoctorWhite_1.append(rectPlagueWhite1_1)

rectPlagueWhitex2_1 = plagueDoctorWhiteRect1.centerx
rectPlagueWhitey2_1 = plagueDoctorWhiteRect1.centery + step * 2
rectPlagueWhite2_1 = pygame.Rect(rectPlagueWhitex2_1 - 30, rectPlagueWhitey2_1 - 30, 60, 60)
rectsPlagueDoctorWhite_1.append(rectPlagueWhite2_1)

rectPlagueWhitex3_1 = plagueDoctorWhiteRect1.centerx
rectPlagueWhitey3_1 = plagueDoctorWhiteRect1.centery + step * 3
rectPlagueWhite3_1 = pygame.Rect(rectPlagueWhitex3_1 - 30, rectPlagueWhitey3_1 - 30, 60, 60)
rectsPlagueDoctorWhite_1.append(rectPlagueWhite3_1)

rectPlagueWhitex4_1 = plagueDoctorWhiteRect1.centerx
rectPlagueWhitey4_1 = plagueDoctorWhiteRect1.centery + step * 4
rectPlagueWhite4_1 = pygame.Rect(rectPlagueWhitex4_1 - 30, rectPlagueWhitey4_1 - 30, 60, 60)
rectsPlagueDoctorWhite_1.append(rectPlagueWhite4_1)

rectPlagueWhitex5_1 = plagueDoctorWhiteRect1.centerx
rectPlagueWhitey5_1 = plagueDoctorWhiteRect1.centery + step * 5
rectPlagueWhite5_1 = pygame.Rect(rectPlagueWhitex5_1 - 30, rectPlagueWhitey5_1 - 30, 60, 60)
rectsPlagueDoctorWhite_1.append(rectPlagueWhite5_1)

rectPlagueWhitex6_1 = plagueDoctorWhiteRect1.centerx
rectPlagueWhitey6_1 = plagueDoctorWhiteRect1.centery + step * 6
rectPlagueWhite6_1 = pygame.Rect(rectPlagueWhitex6_1 - 30, rectPlagueWhitey6_1 - 30, 60, 60)
rectsPlagueDoctorWhite_1.append(rectPlagueWhite6_1)

rectPlagueWhitex7_1 = plagueDoctorWhiteRect1.centerx
rectPlagueWhitey7_1 = plagueDoctorWhiteRect1.centery + step * 7
rectPlagueWhite7_1 = pygame.Rect(rectPlagueWhitex7_1 - 30, rectPlagueWhitey7_1 - 30, 60, 60)
rectsPlagueDoctorWhite_1.append(rectPlagueWhite7_1)

rectPlagueWhitex8_1 = plagueDoctorWhiteRect1.centerx
rectPlagueWhitey8_1 = plagueDoctorWhiteRect1.centery - step
rectPlagueWhite8_1 = pygame.Rect(rectPlagueWhitex8_1 - 30, rectPlagueWhitey8_1 - 30, 60, 60)
rectsPlagueDoctorWhite_1.append(rectPlagueWhite8_1)

rectPlagueWhitex9_1 = plagueDoctorWhiteRect1.centerx
rectPlagueWhitey9_1 = plagueDoctorWhiteRect1.centery - step * 2
rectPlagueWhite9_1 = pygame.Rect(rectPlagueWhitex9_1 - 30, rectPlagueWhitey9_1 - 30, 60, 60)
rectsPlagueDoctorWhite_1.append(rectPlagueWhite9_1)

rectPlagueWhitex10_1 = plagueDoctorWhiteRect1.centerx
rectPlagueWhitey10_1 = plagueDoctorWhiteRect1.centery - step * 3
rectPlagueWhite10_1 = pygame.Rect(rectPlagueWhitex10_1 - 30, rectPlagueWhitey10_1 - 30, 60, 60)
rectsPlagueDoctorWhite_1.append(rectPlagueWhite10_1)

rectPlagueWhitex11_1 = plagueDoctorWhiteRect1.centerx
rectPlagueWhitey11_1 = plagueDoctorWhiteRect1.centery - step * 4
rectPlagueWhite11_1 = pygame.Rect(rectPlagueWhitex11_1 - 30, rectPlagueWhitey11_1 - 30, 60, 60)
rectsPlagueDoctorWhite_1.append(rectPlagueWhite11_1)

rectPlagueWhitex12_1 = plagueDoctorWhiteRect1.centerx
rectPlagueWhitey12_1 = plagueDoctorWhiteRect1.centery - step * 5
rectPlagueWhite12_1 = pygame.Rect(rectPlagueWhitex12_1 - 30, rectPlagueWhitey12_1 - 30, 60, 60)
rectsPlagueDoctorWhite_1.append(rectPlagueWhite12_1)

rectPlagueWhitex13_1 = plagueDoctorWhiteRect1.centerx
rectPlagueWhitey13_1 = plagueDoctorWhiteRect1.centery - step * 6
rectPlagueWhite13_1 = pygame.Rect(rectPlagueWhitex13_1 - 30, rectPlagueWhitey13_1 - 30, 60, 60)
rectsPlagueDoctorWhite_1.append(rectPlagueWhite13_1)

rectPlagueWhitex14_1 = plagueDoctorWhiteRect1.centerx
rectPlagueWhitey14_1 = plagueDoctorWhiteRect1.centery - step * 7
rectPlagueWhite14_1 = pygame.Rect(rectPlagueWhitex14_1 - 30, rectPlagueWhitey14_1 - 30, 60, 60)
rectsPlagueDoctorWhite_1.append(rectPlagueWhite14_1)

rectPlagueWhitex15_1 = plagueDoctorWhiteRect1.centerx + step
rectPlagueWhitey15_1 = plagueDoctorWhiteRect1.centery
rectPlagueWhite15_1 = pygame.Rect(rectPlagueWhitex15_1 - 30, rectPlagueWhitey15_1 - 30, 60, 60)
rectsPlagueDoctorWhite_1.append(rectPlagueWhite15_1)

rectPlagueWhitex16_1 = plagueDoctorWhiteRect1.centerx + step * 2
rectPlagueWhitey16_1 = plagueDoctorWhiteRect1.centery
rectPlagueWhite16_1 = pygame.Rect(rectPlagueWhitex16_1 - 30, rectPlagueWhitey16_1 - 30, 60, 60)
rectsPlagueDoctorWhite_1.append(rectPlagueWhite16_1)

rectPlagueWhitex17_1 = plagueDoctorWhiteRect1.centerx - step
rectPlagueWhitey17_1 = plagueDoctorWhiteRect1.centery
rectPlagueWhite17_1 = pygame.Rect(rectPlagueWhitex17_1 - 30, rectPlagueWhitey17_1 - 30, 60, 60)
rectsPlagueDoctorWhite_1.append(rectPlagueWhite17_1)

rectPlagueWhitex18_1 = plagueDoctorWhiteRect1.centerx - step * 2
rectPlagueWhitey18_1 = plagueDoctorWhiteRect1.centery
rectPlagueWhite18_1 = pygame.Rect(rectPlagueWhitex18_1 - 30, rectPlagueWhitey18_1 - 30, 60, 60)
rectsPlagueDoctorWhite_1.append(rectPlagueWhite18_1)

# Válečník bílý 1
rectsWarriorWhite = []

rectWarriorWhitex1 = warriorWhiteRect.centerx + step
rectWarriorWhitey1 = warriorWhiteRect.centery
rectWarriorWhite1 = pygame.Rect(rectWarriorWhitex1 - 30, rectWarriorWhitey1 - 30, 60, 60)
rectsWarriorWhite.append(rectWarriorWhite1)

rectWarriorWhitex2 = warriorWhiteRect.centerx - step
rectWarriorWhitey2 = warriorWhiteRect.centery
rectWarriorWhite2 = pygame.Rect(rectWarriorWhitex2 - 30, rectWarriorWhitey2 - 30, 60, 60)
rectsWarriorWhite.append(rectWarriorWhite2)

rectWarriorWhitex3 = warriorWhiteRect.centerx
rectWarriorWhitey3 = warriorWhiteRect.centery + step
rectWarriorWhite3 = pygame.Rect(rectWarriorWhitex3 - 30, rectWarriorWhitey3 - 30, 60, 60)
rectsWarriorWhite.append(rectWarriorWhite3)

rectWarriorWhitex4 = warriorWhiteRect.centerx
rectWarriorWhitey4 = warriorWhiteRect.centery - step
rectWarriorWhite4 = pygame.Rect(rectWarriorWhitex4 - 30, rectWarriorWhitey4 - 30, 60, 60)
rectsWarriorWhite.append(rectWarriorWhite4)

# Válečník bílý 1 abilita
rectsWarriorWhiteAbility = []

rectWarriorWhitex1Ability = warriorWhiteRect.centerx + step * 2
rectWarriorWhitey1Ability = warriorWhiteRect.centery
rectWarriorWhite1Ability = pygame.Rect(rectWarriorWhitex1Ability - 30, rectWarriorWhitey1Ability - 30, 60, 60)
rectsWarriorWhiteAbility.append(rectWarriorWhite1Ability)

rectWarriorWhitex2Ability = warriorWhiteRect.centerx - step * 2
rectWarriorWhitey2Ability = warriorWhiteRect.centery
rectWarriorWhite2Ability = pygame.Rect(rectWarriorWhitex2Ability - 30, rectWarriorWhitey2Ability - 30, 60, 60)
rectsWarriorWhiteAbility.append(rectWarriorWhite2Ability)

rectWarriorWhitex3Ability = warriorWhiteRect.centerx
rectWarriorWhitey3Ability = warriorWhiteRect.centery - step * 2
rectWarriorWhite3Ability = pygame.Rect(rectWarriorWhitex3Ability - 30, rectWarriorWhitey3Ability - 30, 60, 60)
rectsWarriorWhiteAbility.append(rectWarriorWhite3Ability)

rectWarriorWhitex4Ability = warriorWhiteRect.centerx
rectWarriorWhitey4Ability = warriorWhiteRect.centery + step * 2
rectWarriorWhite4Ability = pygame.Rect(rectWarriorWhitex4Ability - 30, rectWarriorWhitey4Ability - 30, 60, 60)
rectsWarriorWhiteAbility.append(rectWarriorWhite4Ability)

# Legionář bílý 1
rectsLegionaryWhite = []

rectLegionaryWhitex1 = legionaryWhiteRect.centerx + step
rectLegionaryWhitey1 = legionaryWhiteRect.centery + step
rectLegionaryWhite1 = pygame.Rect(rectLegionaryWhitex1 - 30, rectLegionaryWhitey1 - 30, 60, 60)
rectsLegionaryWhite.append(rectLegionaryWhite1)

rectLegionaryWhitex2 = legionaryWhiteRect.centerx
rectLegionaryWhitey2 = legionaryWhiteRect.centery + step
rectLegionaryWhite2 = pygame.Rect(rectLegionaryWhitex2 - 30, rectLegionaryWhitey2 - 30, 60, 60)
rectsLegionaryWhite.append(rectLegionaryWhite2)

rectLegionaryWhitex3 = legionaryWhiteRect.centerx - step
rectLegionaryWhitey3 = legionaryWhiteRect.centery + step
rectLegionaryWhite3 = pygame.Rect(rectLegionaryWhitex3 - 30, rectLegionaryWhitey3 - 30, 60, 60)
rectsLegionaryWhite.append(rectLegionaryWhite3)

# Válečník bílý 2
rectsWarriorWhite_1 = []

rectWarriorWhitex1_1 = warriorWhiteRect1.centerx + step
rectWarriorWhitey1_1 = warriorWhiteRect1.centery
rectWarriorWhite1_1 = pygame.Rect(rectWarriorWhitex1_1 - 30, rectWarriorWhitey1_1 - 30, 60, 60)
rectsWarriorWhite_1.append(rectWarriorWhite1_1)

rectWarriorWhitex2_1 = warriorWhiteRect1.centerx - step
rectWarriorWhitey2_1 = warriorWhiteRect1.centery
rectWarriorWhite2_1 = pygame.Rect(rectWarriorWhitex2_1 - 30, rectWarriorWhitey2_1 - 30, 60, 60)
rectsWarriorWhite_1.append(rectWarriorWhite2_1)

rectWarriorWhitex3_1 = warriorWhiteRect1.centerx
rectWarriorWhitey3_1 = warriorWhiteRect1.centery + step
rectWarriorWhite3_1 = pygame.Rect(rectWarriorWhitex3_1 - 30, rectWarriorWhitey3_1 - 30, 60, 60)
rectsWarriorWhite_1.append(rectWarriorWhite3_1)

rectWarriorWhitex4_1 = warriorWhiteRect1.centerx
rectWarriorWhitey4_1 = warriorWhiteRect1.centery - step
rectWarriorWhite4_1 = pygame.Rect(rectWarriorWhitex4_1 - 30, rectWarriorWhitey4_1 - 30, 60, 60)
rectsWarriorWhite_1.append(rectWarriorWhite4_1)

# Válečník bílý 2 abilita
rectsWarriorWhiteAbility_1 = []

rectWarriorWhitex1_1Ability = warriorWhiteRect1.centerx + step * 2
rectWarriorWhitey1_1Ability = warriorWhiteRect1.centery
rectWarriorWhite1_1Ability = pygame.Rect(rectWarriorWhitex1_1Ability - 30, rectWarriorWhitey1_1Ability - 30, 60, 60)
rectsWarriorWhiteAbility_1.append(rectWarriorWhite1_1Ability)

rectWarriorWhitex2_1Ability = warriorWhiteRect1.centerx - step * 2
rectWarriorWhitey2_1Ability = warriorWhiteRect1.centery
rectWarriorWhite2_1Ability = pygame.Rect(rectWarriorWhitex2_1Ability - 30, rectWarriorWhitey2_1Ability - 30, 60, 60)
rectsWarriorWhiteAbility_1.append(rectWarriorWhite2_1Ability)

rectWarriorWhitex3_1Ability = warriorWhiteRect1.centerx
rectWarriorWhitey3_1Ability = warriorWhiteRect1.centery - step * 2
rectWarriorWhite3_1Ability = pygame.Rect(rectWarriorWhitex3_1Ability - 30, rectWarriorWhitey3_1Ability - 30, 60, 60)
rectsWarriorWhiteAbility_1.append(rectWarriorWhite3_1Ability)

rectWarriorWhitex4_1Ability = warriorWhiteRect1.centerx
rectWarriorWhitey4_1Ability = warriorWhiteRect1.centery + step * 2
rectWarriorWhite4_1Ability = pygame.Rect(rectWarriorWhitex4_1Ability - 30, rectWarriorWhitey4_1Ability - 30, 60, 60)
rectsWarriorWhiteAbility_1.append(rectWarriorWhite4_1Ability)

# Legionář bílý 2
rectsLegionaryWhite_1 = []

rectLegionaryWhitex1_1 = legionaryWhiteRect1.centerx + step
rectLegionaryWhitey1_1 = legionaryWhiteRect1.centery + step
rectLegionaryWhite1_1 = pygame.Rect(rectLegionaryWhitex1_1 - 30, rectLegionaryWhitey1_1 - 30, 60, 60)
rectsLegionaryWhite_1.append(rectLegionaryWhite1_1)

rectLegionaryWhitex2_1 = legionaryWhiteRect1.centerx
rectLegionaryWhitey2_1 = legionaryWhiteRect1.centery + step
rectLegionaryWhite2_1 = pygame.Rect(rectLegionaryWhitex2_1 - 30, rectLegionaryWhitey2_1 - 30, 60, 60)
rectsLegionaryWhite_1.append(rectLegionaryWhite2_1)

rectLegionaryWhitex3_1 = legionaryWhiteRect1.centerx - step
rectLegionaryWhitey3_1 = legionaryWhiteRect1.centery + step
rectLegionaryWhite3_1 = pygame.Rect(rectLegionaryWhitex3_1 - 30, rectLegionaryWhitey3_1 - 30, 60, 60)
rectsLegionaryWhite_1.append(rectLegionaryWhite3_1)

#

rectsWarriorWhite_2 = []

rectWarriorWhitex1_2 = warriorWhiteRect2.centerx + step
rectWarriorWhitey1_2 = warriorWhiteRect2.centery
rectWarriorWhite1_2 = pygame.Rect(rectWarriorWhitex1_2 - 30, rectWarriorWhitey1_2 - 30, 60, 60)
rectsWarriorWhite_2.append(rectWarriorWhite1_2)

rectWarriorWhitex2_2 = warriorWhiteRect2.centerx - step
rectWarriorWhitey2_2 = warriorWhiteRect2.centery
rectWarriorWhite2_2 = pygame.Rect(rectWarriorWhitex2_2 - 30, rectWarriorWhitey2_2 - 30, 60, 60)
rectsWarriorWhite_2.append(rectWarriorWhite2_2)

rectWarriorWhitex3_2 = warriorWhiteRect2.centerx
rectWarriorWhitey3_2 = warriorWhiteRect2.centery + step
rectWarriorWhite3_2 = pygame.Rect(rectWarriorWhitex3_2 - 30, rectWarriorWhitey3_2 - 30, 60, 60)
rectsWarriorWhite_2.append(rectWarriorWhite3_2)

rectWarriorWhitex4_2 = warriorWhiteRect2.centerx
rectWarriorWhitey4_2 = warriorWhiteRect2.centery - step
rectWarriorWhite4_2 = pygame.Rect(rectWarriorWhitex4_2 - 30, rectWarriorWhitey4_2 - 30, 60, 60)
rectsWarriorWhite_2.append(rectWarriorWhite4_2)

# Válečník bílý 3 abilita
rectsWarriorWhiteAbility_2 = []

rectWarriorWhitex1_2Ability = warriorWhiteRect2.centerx + step * 2
rectWarriorWhitey1_2Ability = warriorWhiteRect2.centery
rectWarriorWhite1_2Ability = pygame.Rect(rectWarriorWhitex1_2Ability - 30, rectWarriorWhitey1_2Ability - 30, 60, 60)
rectsWarriorWhiteAbility_2.append(rectWarriorWhite1_2Ability)

rectWarriorWhitex2_2Ability = warriorWhiteRect2.centerx - step * 2
rectWarriorWhitey2_2Ability = warriorWhiteRect2.centery
rectWarriorWhite2_2Ability = pygame.Rect(rectWarriorWhitex2_2Ability - 30, rectWarriorWhitey2_2Ability - 30, 60, 60)
rectsWarriorWhiteAbility_2.append(rectWarriorWhite2_2Ability)

rectWarriorWhitex3_2Ability = warriorWhiteRect2.centerx
rectWarriorWhitey3_2Ability = warriorWhiteRect2.centery - step * 2
rectWarriorWhite3_2Ability = pygame.Rect(rectWarriorWhitex3_2Ability - 30, rectWarriorWhitey3_2Ability - 30, 60, 60)
rectsWarriorWhiteAbility_2.append(rectWarriorWhite3_2Ability)

rectWarriorWhitex4_2Ability = warriorWhiteRect2.centerx
rectWarriorWhitey4_2Ability = warriorWhiteRect2.centery + step * 2
rectWarriorWhite4_2Ability = pygame.Rect(rectWarriorWhitex4_2Ability - 30, rectWarriorWhitey4_2Ability - 30, 60, 60)
rectsWarriorWhiteAbility_2.append(rectWarriorWhite4_2Ability)

# Legionář bílý 3
rectsLegionaryWhite_2 = []

rectLegionaryWhitex1_2 = legionaryWhiteRect2.centerx + step
rectLegionaryWhitey1_2 = legionaryWhiteRect2.centery + step
rectLegionaryWhite1_2 = pygame.Rect(rectLegionaryWhitex1_2 - 30, rectLegionaryWhitey1_2 - 30, 60, 60)
rectsLegionaryWhite_2.append(rectLegionaryWhite1_2)

rectLegionaryWhitex2_2 = legionaryWhiteRect2.centerx
rectLegionaryWhitey2_2 = legionaryWhiteRect2.centery + step
rectLegionaryWhite2_2 = pygame.Rect(rectLegionaryWhitex2_2 - 30, rectLegionaryWhitey2_2 - 30, 60, 60)
rectsLegionaryWhite_2.append(rectLegionaryWhite2_2)

rectLegionaryWhitex3_2 = legionaryWhiteRect2.centerx - step
rectLegionaryWhitey3_2 = legionaryWhiteRect2.centery + step
rectLegionaryWhite3_2 = pygame.Rect(rectLegionaryWhitex3_2 - 30, rectLegionaryWhitey3_2 - 30, 60, 60)
rectsLegionaryWhite_2.append(rectLegionaryWhite3_2)

# Válečník bílý 4
rectsWarriorWhite_3 = []

rectWarriorWhitex1_3 = warriorWhiteRect3.centerx + step
rectWarriorWhitey1_3 = warriorWhiteRect3.centery
rectWarriorWhite1_3 = pygame.Rect(rectWarriorWhitex1_3 - 30, rectWarriorWhitey1_3 - 30, 60, 60)
rectsWarriorWhite_3.append(rectWarriorWhite1_3)

rectWarriorWhitex2_3 = warriorWhiteRect3.centerx - step
rectWarriorWhitey2_3 = warriorWhiteRect3.centery
rectWarriorWhite2_3 = pygame.Rect(rectWarriorWhitex2_3 - 30, rectWarriorWhitey2_3 - 30, 60, 60)
rectsWarriorWhite_3.append(rectWarriorWhite2_3)

rectWarriorWhitex3_3 = warriorWhiteRect3.centerx
rectWarriorWhitey3_3 = warriorWhiteRect3.centery + step
rectWarriorWhite3_3 = pygame.Rect(rectWarriorWhitex3_3 - 30, rectWarriorWhitey3_3 - 30, 60, 60)
rectsWarriorWhite_3.append(rectWarriorWhite3_3)

rectWarriorWhitex4_3 = warriorWhiteRect3.centerx
rectWarriorWhitey4_3 = warriorWhiteRect3.centery - step
rectWarriorWhite4_3 = pygame.Rect(rectWarriorWhitex4_3 - 30, rectWarriorWhitey4_3 - 30, 60, 60)
rectsWarriorWhite_3.append(rectWarriorWhite4_3)

# Válečník bílý 4 abilita
rectsWarriorWhiteAbility_3 = []

rectWarriorWhitex1_3Ability = warriorWhiteRect3.centerx + step * 2
rectWarriorWhitey1_3Ability = warriorWhiteRect3.centery
rectWarriorWhite1_3Ability = pygame.Rect(rectWarriorWhitex1_3Ability - 30, rectWarriorWhitey1_3Ability - 30, 60, 60)
rectsWarriorWhiteAbility_3.append(rectWarriorWhite1_3Ability)

rectWarriorWhitex2_3Ability = warriorWhiteRect3.centerx - step * 2
rectWarriorWhitey2_3Ability = warriorWhiteRect3.centery
rectWarriorWhite2_3Ability = pygame.Rect(rectWarriorWhitex2_3Ability - 30, rectWarriorWhitey2_3Ability - 30, 60, 60)
rectsWarriorWhiteAbility_3.append(rectWarriorWhite2_3Ability)

rectWarriorWhitex3_3Ability = warriorWhiteRect3.centerx
rectWarriorWhitey3_3Ability = warriorWhiteRect3.centery - step * 2
rectWarriorWhite3_3Ability = pygame.Rect(rectWarriorWhitex3_3Ability - 30, rectWarriorWhitey3_3Ability - 30, 60, 60)
rectsWarriorWhiteAbility_3.append(rectWarriorWhite3_3Ability)

rectWarriorWhitex4_3Ability = warriorWhiteRect3.centerx
rectWarriorWhitey4_3Ability = warriorWhiteRect3.centery + step * 2
rectWarriorWhite4_3Ability = pygame.Rect(rectWarriorWhitex4_3Ability - 30, rectWarriorWhitey4_3Ability - 30, 60, 60)
rectsWarriorWhiteAbility_3.append(rectWarriorWhite4_3Ability)

# Legionář bílý 4
rectsLegionaryWhite_3 = []

rectLegionaryWhitex1_3 = legionaryWhiteRect3.centerx + step
rectLegionaryWhitey1_3 = legionaryWhiteRect3.centery + step
rectLegionaryWhite1_3 = pygame.Rect(rectLegionaryWhitex1_3 - 30, rectLegionaryWhitey1_3 - 30, 60, 60)
rectsLegionaryWhite_3.append(rectLegionaryWhite1_3)

rectLegionaryWhitex2_3 = legionaryWhiteRect3.centerx
rectLegionaryWhitey2_3 = legionaryWhiteRect3.centery + step
rectLegionaryWhite2_3 = pygame.Rect(rectLegionaryWhitex2_3 - 30, rectLegionaryWhitey2_3 - 30, 60, 60)
rectsLegionaryWhite_3.append(rectLegionaryWhite2_3)

rectLegionaryWhitex3_3 = legionaryWhiteRect3.centerx - step
rectLegionaryWhitey3_3 = legionaryWhiteRect3.centery + step
rectLegionaryWhite3_3 = pygame.Rect(rectLegionaryWhitex3_3 - 30, rectLegionaryWhitey3_3 - 30, 60, 60)
rectsLegionaryWhite_3.append(rectLegionaryWhite3_3)

# Morový doktor černý 1
rectsPlagueDoctorBlack = []

rectPlagueBlackx1 = plagueDoctorBlackRect.centerx + step
rectPlagueBlacky1 = plagueDoctorBlackRect.centery
rectPlagueBlack1 = pygame.Rect(rectPlagueBlackx1 - 30, rectPlagueBlacky1 - 30, 60, 60)
rectsPlagueDoctorBlack.append(rectPlagueBlack1)

rectPlagueBlackx2 = plagueDoctorBlackRect.centerx + step * 2
rectPlagueBlacky2 = plagueDoctorBlackRect.centery
rectPlagueBlack2 = pygame.Rect(rectPlagueBlackx2 - 30, rectPlagueBlacky2 - 30, 60, 60)
rectsPlagueDoctorBlack.append(rectPlagueBlack2)

rectPlagueBlackx3 = plagueDoctorBlackRect.centerx - step
rectPlagueBlacky3 = plagueDoctorBlackRect.centery
rectPlagueBlack3 = pygame.Rect(rectPlagueBlackx3 - 30, rectPlagueBlacky3 - 30, 60, 60)
rectsPlagueDoctorBlack.append(rectPlagueBlack3)

rectPlagueBlackx4 = plagueDoctorBlackRect.centerx - step * 2
rectPlagueBlacky4 = plagueDoctorBlackRect.centery
rectPlagueBlack4 = pygame.Rect(rectPlagueBlackx4 - 30, rectPlagueBlacky4 - 30, 60, 60)
rectsPlagueDoctorBlack.append(rectPlagueBlack4)

rectPlagueBlackx5 = plagueDoctorBlackRect.centerx
rectPlagueBlacky5 = plagueDoctorBlackRect.centery + step
rectPlagueBlack5 = pygame.Rect(rectPlagueBlackx5 - 30, rectPlagueBlacky5 - 30, 60, 60)
rectsPlagueDoctorBlack.append(rectPlagueBlack5)

rectPlagueBlackx6 = plagueDoctorBlackRect.centerx
rectPlagueBlacky6 = plagueDoctorBlackRect.centery + step * 2
rectPlagueBlack6 = pygame.Rect(rectPlagueBlackx6 - 30, rectPlagueBlacky6 - 30, 60, 60)
rectsPlagueDoctorBlack.append(rectPlagueBlack6)

rectPlagueBlackx7 = plagueDoctorBlackRect.centerx
rectPlagueBlacky7 = plagueDoctorBlackRect.centery + step * 3
rectPlagueBlack7 = pygame.Rect(rectPlagueBlackx7 - 30, rectPlagueBlacky7 - 30, 60, 60)
rectsPlagueDoctorBlack.append(rectPlagueBlack7)

rectPlagueBlackx8 = plagueDoctorBlackRect.centerx
rectPlagueBlacky8 = plagueDoctorBlackRect.centery + step * 4
rectPlagueBlack8 = pygame.Rect(rectPlagueBlackx8 - 30, rectPlagueBlacky8 - 30, 60, 60)
rectsPlagueDoctorBlack.append(rectPlagueBlack8)

rectPlagueBlackx9 = plagueDoctorBlackRect.centerx
rectPlagueBlacky9 = plagueDoctorBlackRect.centery + step * 5
rectPlagueBlack9 = pygame.Rect(rectPlagueBlackx9 - 30, rectPlagueBlacky9 - 30, 60, 60)
rectsPlagueDoctorBlack.append(rectPlagueBlack9)

rectPlagueBlackx10 = plagueDoctorBlackRect.centerx
rectPlagueBlacky10 = plagueDoctorBlackRect.centery + step * 6
rectPlagueBlack10 = pygame.Rect(rectPlagueBlackx10 - 30, rectPlagueBlacky10 - 30, 60, 60)
rectsPlagueDoctorBlack.append(rectPlagueBlack10)

rectPlagueBlackx11 = plagueDoctorBlackRect.centerx
rectPlagueBlacky11 = plagueDoctorBlackRect.centery + step * 7
rectPlagueBlack11 = pygame.Rect(rectPlagueBlackx11 - 30, rectPlagueBlacky11 - 30, 60, 60)
rectsPlagueDoctorBlack.append(rectPlagueBlack11)

rectPlagueBlackx12 = plagueDoctorBlackRect.centerx
rectPlagueBlacky12 = plagueDoctorBlackRect.centery - step
rectPlagueBlack12 = pygame.Rect(rectPlagueBlackx12 - 30, rectPlagueBlacky12 - 30, 60, 60)
rectsPlagueDoctorBlack.append(rectPlagueBlack12)

rectPlagueBlackx13 = plagueDoctorBlackRect.centerx
rectPlagueBlacky13 = plagueDoctorBlackRect.centery - step * 2
rectPlagueBlack13 = pygame.Rect(rectPlagueBlackx13 - 30, rectPlagueBlacky13 - 30, 60, 60)
rectsPlagueDoctorBlack.append(rectPlagueBlack13)

rectPlagueBlackx14 = plagueDoctorBlackRect.centerx
rectPlagueBlacky14 = plagueDoctorBlackRect.centery - step * 3
rectPlagueBlack14 = pygame.Rect(rectPlagueBlackx14 - 30, rectPlagueBlacky14 - 30, 60, 60)
rectsPlagueDoctorBlack.append(rectPlagueBlack14)

rectPlagueBlackx15 = plagueDoctorBlackRect.centerx
rectPlagueBlacky15 = plagueDoctorBlackRect.centery - step * 4
rectPlagueBlack15 = pygame.Rect(rectPlagueBlackx15 - 30, rectPlagueBlacky15 - 30, 60, 60)
rectsPlagueDoctorBlack.append(rectPlagueBlack15)

rectPlagueBlackx16 = plagueDoctorBlackRect.centerx
rectPlagueBlacky16 = plagueDoctorBlackRect.centery - step * 5
rectPlagueBlack16 = pygame.Rect(rectPlagueBlackx16 - 30, rectPlagueBlacky16 - 30, 60, 60)
rectsPlagueDoctorBlack.append(rectPlagueBlack16)

rectPlagueBlackx17 = plagueDoctorBlackRect.centerx
rectPlagueBlacky17 = plagueDoctorBlackRect.centery - step * 6
rectPlagueBlack17 = pygame.Rect(rectPlagueBlackx17 - 30, rectPlagueBlacky17 - 30, 60, 60)
rectsPlagueDoctorBlack.append(rectPlagueBlack17)

rectPlagueBlackx18 = plagueDoctorBlackRect.centerx
rectPlagueBlacky18 = plagueDoctorBlackRect.centery - step * 7
rectPlagueBlack18 = pygame.Rect(rectPlagueBlackx18 - 30, rectPlagueBlacky18 - 30, 60, 60)
rectsPlagueDoctorBlack.append(rectPlagueBlack18)

# Arcibiskup černý 1
rectsArchbishopBlack = []

rectArchbishopBlackx1 = archbishopBlackRect.centerx + step * 2
rectArchbishopBlacky1 = archbishopBlackRect.centery
rectArchbishopBlack1 = pygame.Rect(rectArchbishopBlackx1 - 30, rectArchbishopBlacky1 - 30, 60, 60)
rectsArchbishopBlack.append(rectArchbishopBlack1)

rectArchbishopBlackx2 = archbishopBlackRect.centerx + step * 2
rectArchbishopBlacky2 = archbishopBlackRect.centery + step
rectArchbishopBlack2 = pygame.Rect(rectArchbishopBlackx2 - 30, rectArchbishopBlacky2 - 30, 60, 60)
rectsArchbishopBlack.append(rectArchbishopBlack2)

rectArchbishopBlackx3 = archbishopBlackRect.centerx + step * 2
rectArchbishopBlacky3 = archbishopBlackRect.centery - step
rectArchbishopBlack3 = pygame.Rect(rectArchbishopBlackx3 - 30, rectArchbishopBlacky3 - 30, 60, 60)
rectsArchbishopBlack.append(rectArchbishopBlack3)

rectArchbishopBlackx4 = archbishopBlackRect.centerx
rectArchbishopBlacky4 = archbishopBlackRect.centery + step * 2
rectArchbishopBlack4 = pygame.Rect(rectArchbishopBlackx4 - 30, rectArchbishopBlacky4 - 30, 60, 60)
rectsArchbishopBlack.append(rectArchbishopBlack4)

rectArchbishopBlackx5 = archbishopBlackRect.centerx + step
rectArchbishopBlacky5 = archbishopBlackRect.centery + step * 2
rectArchbishopBlack5 = pygame.Rect(rectArchbishopBlackx5 - 30, rectArchbishopBlacky5 - 30, 60, 60)
rectsArchbishopBlack.append(rectArchbishopBlack5)

rectArchbishopBlackx6 = archbishopBlackRect.centerx - step
rectArchbishopBlacky6 = archbishopBlackRect.centery + step * 2
rectArchbishopBlack6 = pygame.Rect(rectArchbishopBlackx6 - 30, rectArchbishopBlacky6 - 30, 60, 60)
rectsArchbishopBlack.append(rectArchbishopBlack6)

rectArchbishopBlackx7 = archbishopBlackRect.centerx - step * 2
rectArchbishopBlacky7 = archbishopBlackRect.centery
rectArchbishopBlack7 = pygame.Rect(rectArchbishopBlackx7 - 30, rectArchbishopBlacky7 - 30, 60, 60)
rectsArchbishopBlack.append(rectArchbishopBlack7)

rectArchbishopBlackx8 = archbishopBlackRect.centerx - step * 2
rectArchbishopBlacky8 = archbishopBlackRect.centery + step
rectArchbishopBlack8 = pygame.Rect(rectArchbishopBlackx8 - 30, rectArchbishopBlacky8 - 30, 60, 60)
rectsArchbishopBlack.append(rectArchbishopBlack8)

rectArchbishopBlackx9 = archbishopBlackRect.centerx - step * 2
rectArchbishopBlacky9 = archbishopBlackRect.centery - step
rectArchbishopBlack9 = pygame.Rect(rectArchbishopBlackx9 - 30, rectArchbishopBlacky9 - 30, 60, 60)
rectsArchbishopBlack.append(rectArchbishopBlack9)

rectArchbishopBlackx10 = archbishopBlackRect.centerx
rectArchbishopBlacky10 = archbishopBlackRect.centery - step * 2
rectArchbishopBlack10 = pygame.Rect(rectArchbishopBlackx10 - 30, rectArchbishopBlacky10 - 30, 60, 60)
rectsArchbishopBlack.append(rectArchbishopBlack10)

rectArchbishopBlackx11 = archbishopBlackRect.centerx + step
rectArchbishopBlacky11 = archbishopBlackRect.centery - step * 2
rectArchbishopBlack11 = pygame.Rect(rectArchbishopBlackx11 - 30, rectArchbishopBlacky11 - 30, 60, 60)
rectsArchbishopBlack.append(rectArchbishopBlack11)

rectArchbishopBlackx12 = archbishopBlackRect.centerx - step
rectArchbishopBlacky12 = archbishopBlackRect.centery - step * 2
rectArchbishopBlack12 = pygame.Rect(rectArchbishopBlackx12 - 30, rectArchbishopBlacky12 - 30, 60, 60)
rectsArchbishopBlack.append(rectArchbishopBlack12)

# Kardinál černý 1
rectsCardinalBlack = []

rectCardinalBlackx1 = cardinalBlackRect.centerx + step
rectCardinalBlacky1 = cardinalBlackRect.centery - step
rectCardinalBlack1 = pygame.Rect(rectCardinalBlackx1 - 30, rectCardinalBlacky1 - 30, 60, 60)
rectsCardinalBlack.append(rectCardinalBlack1)

rectCardinalBlackx2 = cardinalBlackRect.centerx - step
rectCardinalBlacky2 = cardinalBlackRect.centery - step
rectCardinalBlack2 = pygame.Rect(rectCardinalBlackx2 - 30, rectCardinalBlacky2 - 30, 60, 60)
rectsCardinalBlack.append(rectCardinalBlack2)

rectCardinalBlackx3 = cardinalBlackRect.centerx + step
rectCardinalBlacky3 = cardinalBlackRect.centery + step
rectCardinalBlack3 = pygame.Rect(rectCardinalBlackx3 - 30, rectCardinalBlacky3 - 30, 60, 60)
rectsCardinalBlack.append(rectCardinalBlack3)

rectCardinalBlackx4 = cardinalBlackRect.centerx - step
rectCardinalBlacky4 = cardinalBlackRect.centery + step
rectCardinalBlack4 = pygame.Rect(rectCardinalBlackx4 - 30, rectCardinalBlacky4 - 30, 60, 60)
rectsCardinalBlack.append(rectCardinalBlack4)

# Hádes černý
rectsHadesBlack = []

rectHadesBlackx1 = hadesBlackRect.centerx + step
rectHadesBlacky1 = hadesBlackRect.centery
rectHadesBlack1 = pygame.Rect(rectHadesBlackx1 - 30, rectHadesBlacky1 - 30, 60, 60)
rectsHadesBlack.append(rectHadesBlack1)

rectHadesBlackx2 = hadesBlackRect.centerx + step * 2
rectHadesBlacky2 = hadesBlackRect.centery
rectHadesBlack2 = pygame.Rect(rectHadesBlackx2 - 30, rectHadesBlacky2 - 30, 60, 60)
rectsHadesBlack.append(rectHadesBlack2)

rectHadesBlackx3 = hadesBlackRect.centerx + step * 3
rectHadesBlacky3 = hadesBlackRect.centery
rectHadesBlack3 = pygame.Rect(rectHadesBlackx3 - 30, rectHadesBlacky3 - 30, 60, 60)
rectsHadesBlack.append(rectHadesBlack3)

rectHadesBlackx4 = hadesBlackRect.centerx - step
rectHadesBlacky4 = hadesBlackRect.centery
rectHadesBlack4 = pygame.Rect(rectHadesBlackx4 - 30, rectHadesBlacky4 - 30, 60, 60)
rectsHadesBlack.append(rectHadesBlack4)

rectHadesBlackx5 = hadesBlackRect.centerx - step * 2
rectHadesBlacky5 = hadesBlackRect.centery
rectHadesBlack5 = pygame.Rect(rectHadesBlackx5 - 30, rectHadesBlacky5 - 30, 60, 60)
rectsHadesBlack.append(rectHadesBlack5)

rectHadesBlackx6 = hadesBlackRect.centerx - step * 3
rectHadesBlacky6 = hadesBlackRect.centery
rectHadesBlack6 = pygame.Rect(rectHadesBlackx6 - 30, rectHadesBlacky6 - 30, 60, 60)
rectsHadesBlack.append(rectHadesBlack6)

rectHadesBlackx7 = hadesBlackRect.centerx
rectHadesBlacky7 = hadesBlackRect.centery - step
rectHadesBlack7 = pygame.Rect(rectHadesBlackx7 - 30, rectHadesBlacky7 - 30, 60, 60)
rectsHadesBlack.append(rectHadesBlack7)

rectHadesBlackx8 = hadesBlackRect.centerx
rectHadesBlacky8 = hadesBlackRect.centery - step * 2
rectHadesBlack8 = pygame.Rect(rectHadesBlackx8 - 30, rectHadesBlacky8 - 30, 60, 60)
rectsHadesBlack.append(rectHadesBlack8)

rectHadesBlackx9 = hadesBlackRect.centerx
rectHadesBlacky9 = hadesBlackRect.centery - step * 3
rectHadesBlack9 = pygame.Rect(rectHadesBlackx9 - 30, rectHadesBlacky9 - 30, 60, 60)
rectsHadesBlack.append(rectHadesBlack9)

rectHadesBlackx10 = hadesBlackRect.centerx + step
rectHadesBlacky10 = hadesBlackRect.centery - step
rectHadesBlack10 = pygame.Rect(rectHadesBlackx10 - 30, rectHadesBlacky10 - 30, 60, 60)
rectsHadesBlack.append(rectHadesBlack10)

rectHadesBlackx11 = hadesBlackRect.centerx + step * 2
rectHadesBlacky11 = hadesBlackRect.centery - step * 2
rectHadesBlack11 = pygame.Rect(rectHadesBlackx11 - 30, rectHadesBlacky11 - 30, 60, 60)
rectsHadesBlack.append(rectHadesBlack11)

rectHadesBlackx12 = hadesBlackRect.centerx + step * 3
rectHadesBlacky12 = hadesBlackRect.centery - step * 3
rectHadesBlack12 = pygame.Rect(rectHadesBlackx12 - 30, rectHadesBlacky12 - 30, 60, 60)
rectsHadesBlack.append(rectHadesBlack12)

rectHadesBlackx13 = hadesBlackRect.centerx - step
rectHadesBlacky13 = hadesBlackRect.centery - step
rectHadesBlack13 = pygame.Rect(rectHadesBlackx13 - 30, rectHadesBlacky13 - 30, 60, 60)
rectsHadesBlack.append(rectHadesBlack13)

rectHadesBlackx14 = hadesBlackRect.centerx - step * 2
rectHadesBlacky14 = hadesBlackRect.centery - step * 2
rectHadesBlack14 = pygame.Rect(rectHadesBlackx14 - 30, rectHadesBlacky14 - 30, 60, 60)
rectsHadesBlack.append(rectHadesBlack14)

rectHadesBlackx15 = hadesBlackRect.centerx - step * 3
rectHadesBlacky15 = hadesBlackRect.centery - step * 3
rectHadesBlack15 = pygame.Rect(rectHadesBlackx15 - 30, rectHadesBlacky15 - 30, 60, 60)
rectsHadesBlack.append(rectHadesBlack15)

rectHadesBlackx16 = hadesBlackRect.centerx + step
rectHadesBlacky16 = hadesBlackRect.centery + step
rectHadesBlacky16 = pygame.Rect(rectHadesBlackx16 - 30, rectHadesBlacky16 - 30, 60, 60)
rectsHadesBlack.append(rectHadesBlacky16)

rectHadesBlackx17 = hadesBlackRect.centerx + step * 2
rectHadesBlacky17 = hadesBlackRect.centery + step * 2
rectHadesBlack17 = pygame.Rect(rectHadesBlackx17 - 30, rectHadesBlacky17 - 30, 60, 60)
rectsHadesBlack.append(rectHadesBlack17)

rectHadesBlackx18 = hadesBlackRect.centerx - step
rectHadesBlacky18 = hadesBlackRect.centery + step
rectHadesBlack18 = pygame.Rect(rectHadesBlackx18 - 30, rectHadesBlacky18 - 30, 60, 60)
rectsHadesBlack.append(rectHadesBlack18)

rectHadesBlackx19 = hadesBlackRect.centerx - step * 2
rectHadesBlacky19 = hadesBlackRect.centery + step * 2
rectHadesBlack19 = pygame.Rect(rectHadesBlackx19 - 30, rectHadesBlacky19 - 30, 60, 60)
rectsHadesBlack.append(rectHadesBlack19)

# Persefona černá
rectsPersephoneBlack = []

rectPersephoneBlackx1 = persephoneBlackRect.centerx + step
rectPersephoneBlacky1 = persephoneBlackRect.centery - step
rectPersephoneBlack1 = pygame.Rect(rectPersephoneBlackx1 - 30, rectPersephoneBlacky1 - 30, 60, 60)
rectsPersephoneBlack.append(rectPersephoneBlack1)

rectPersephoneBlackx2 = persephoneBlackRect.centerx + step
rectPersephoneBlacky2 = persephoneBlackRect.centery
rectPersephoneBlack2 = pygame.Rect(rectPersephoneBlackx2 - 30, rectPersephoneBlacky2 - 30, 60, 60)
rectsPersephoneBlack.append(rectPersephoneBlack2)

rectPersephoneBlackx3 = persephoneBlackRect.centerx + step
rectPersephoneBlacky3 = persephoneBlackRect.centery + step
rectPersephoneBlack3 = pygame.Rect(rectPersephoneBlackx3 - 30, rectPersephoneBlacky3 - 30, 60, 60)
rectsPersephoneBlack.append(rectPersephoneBlack3)

rectPersephoneBlackx4 = persephoneBlackRect.centerx
rectPersephoneBlacky4 = persephoneBlackRect.centery + step
rectPersephoneBlack4 = pygame.Rect(rectPersephoneBlackx4 - 30, rectPersephoneBlacky4 - 30, 60, 60)
rectsPersephoneBlack.append(rectPersephoneBlack4)

rectPersephoneBlackx5 = persephoneBlackRect.centerx
rectPersephoneBlacky5 = persephoneBlackRect.centery - step
rectPersephoneBlack5 = pygame.Rect(rectPersephoneBlackx5 - 30, rectPersephoneBlacky5 - 30, 60, 60)
rectsPersephoneBlack.append(rectPersephoneBlack5)

rectPersephoneBlackx6 = persephoneBlackRect.centerx - step
rectPersephoneBlacky6 = persephoneBlackRect.centery - step
rectPersephoneBlack6 = pygame.Rect(rectPersephoneBlackx6 - 30, rectPersephoneBlacky6 - 30, 60, 60)
rectsPersephoneBlack.append(rectPersephoneBlack6)

rectPersephoneBlackx7 = persephoneBlackRect.centerx - step
rectPersephoneBlacky7 = persephoneBlackRect.centery
rectPersephoneBlack7 = pygame.Rect(rectPersephoneBlackx7 - 30, rectPersephoneBlacky7 - 30, 60, 60)
rectsPersephoneBlack.append(rectPersephoneBlack7)

rectPersephoneBlackx8 = persephoneBlackRect.centerx - step
rectPersephoneBlacky8 = persephoneBlackRect.centery + step
rectPersephoneBlack8 = pygame.Rect(rectPersephoneBlackx8 - 30, rectPersephoneBlacky8 - 30, 60, 60)
rectsPersephoneBlack.append(rectPersephoneBlack8)

# Kardinál černý 1
rectsCardinalBlack_1 = []

rectCardinalBlackx1_1 = cardinalBlackRect1.centerx + step
rectCardinalBlacky1_1 = cardinalBlackRect1.centery - step
rectCardinalBlack1_1 = pygame.Rect(rectCardinalBlackx1_1 - 30, rectCardinalBlacky1_1 - 30, 60, 60)
rectsCardinalBlack_1.append(rectCardinalBlack1_1)

rectCardinalBlackx2_1 = cardinalBlackRect1.centerx + step
rectCardinalBlacky2_1 = cardinalBlackRect1.centery + step
rectCardinalBlack2_1 = pygame.Rect(rectCardinalBlackx2_1 - 30, rectCardinalBlacky2_1 - 30, 60, 60)
rectsCardinalBlack_1.append(rectCardinalBlack2_1)

rectCardinalBlackx3_1 = cardinalBlackRect1.centerx - step
rectCardinalBlacky3_1 = cardinalBlackRect1.centery - step
rectCardinalBlack3_1 = pygame.Rect(rectCardinalBlackx3_1 - 30, rectCardinalBlacky3_1 - 30, 60, 60)
rectsCardinalBlack_1.append(rectCardinalBlack3_1)

rectCardinalBlackx4_1 = cardinalBlackRect1.centerx - step
rectCardinalBlacky4_1 = cardinalBlackRect1.centery + step
rectCardinalBlack4_1 = pygame.Rect(rectCardinalBlackx4_1 - 30, rectCardinalBlacky4_1 - 30, 60, 60)
rectsCardinalBlack_1.append(rectCardinalBlack4_1)

# Arcibiskup černý 1
rectsArchbishopBlack_1 = []

rectArchbishopBlackx1_1 = archbishopBlackRect1.centerx + step * 2
rectArchbishopBlacky1_1 = archbishopBlackRect1.centery
rectArchbishopBlack1_1 = pygame.Rect(rectArchbishopBlackx1_1 - 30, rectArchbishopBlacky1_1 - 30, 60, 60)
rectsArchbishopBlack_1.append(rectArchbishopBlack1_1)

rectArchbishopBlackx2_1 = archbishopBlackRect1.centerx + step * 2
rectArchbishopBlacky2_1 = archbishopBlackRect1.centery - step
rectArchbishopBlack2_1 = pygame.Rect(rectArchbishopBlackx2_1 - 30, rectArchbishopBlacky2_1 - 30, 60, 60)
rectsArchbishopBlack_1.append(rectArchbishopBlack2_1)

rectArchbishopBlackx3_1 = archbishopBlackRect1.centerx + step * 2
rectArchbishopBlacky3_1 = archbishopBlackRect1.centery + step
rectArchbishopBlack3_1 = pygame.Rect(rectArchbishopBlackx3_1 - 30, rectArchbishopBlacky3_1 - 30, 60, 60)
rectsArchbishopBlack_1.append(rectArchbishopBlack3_1)

rectArchbishopBlackx4_1 = archbishopBlackRect1.centerx - step * 2
rectArchbishopBlacky4_1 = archbishopBlackRect1.centery
rectArchbishopBlack4_1 = pygame.Rect(rectArchbishopBlackx4_1 - 30, rectArchbishopBlacky4_1 - 30, 60, 60)
rectsArchbishopBlack_1.append(rectArchbishopBlack4_1)

rectArchbishopBlackx5_1 = archbishopBlackRect1.centerx - step * 2
rectArchbishopBlacky5_1 = archbishopBlackRect1.centery - step
rectArchbishopBlack5_1 = pygame.Rect(rectArchbishopBlackx5_1 - 30, rectArchbishopBlacky5_1 - 30, 60, 60)
rectsArchbishopBlack_1.append(rectArchbishopBlack5_1)

rectArchbishopBlackx6_1 = archbishopBlackRect1.centerx - step * 2
rectArchbishopBlacky6_1 = archbishopBlackRect1.centery + step
rectArchbishopBlack6_1 = pygame.Rect(rectArchbishopBlackx6_1 - 30, rectArchbishopBlacky6_1 - 30, 60, 60)
rectsArchbishopBlack_1.append(rectArchbishopBlack6_1)

rectArchbishopBlackx7_1 = archbishopBlackRect1.centerx
rectArchbishopBlacky7_1 = archbishopBlackRect1.centery + step * 2
rectArchbishopBlack7_1 = pygame.Rect(rectArchbishopBlackx7_1 - 30, rectArchbishopBlacky7_1 - 30, 60, 60)
rectsArchbishopBlack_1.append(rectArchbishopBlack7_1)

rectArchbishopBlackx8_1 = archbishopBlackRect1.centerx - step
rectArchbishopBlacky8_1 = archbishopBlackRect1.centery + step * 2
rectArchbishopBlack8_1 = pygame.Rect(rectArchbishopBlackx8_1 - 30, rectArchbishopBlacky8_1 - 30, 60, 60)
rectsArchbishopBlack_1.append(rectArchbishopBlack8_1)

rectArchbishopBlackx9_1 = archbishopBlackRect1.centerx + step
rectArchbishopBlacky9_1 = archbishopBlackRect1.centery + step * 2
rectArchbishopBlack9_1 = pygame.Rect(rectArchbishopBlackx9_1 - 30, rectArchbishopBlacky9_1 - 30, 60, 60)
rectsArchbishopBlack_1.append(rectArchbishopBlack9_1)

rectArchbishopBlackx10_1 = archbishopBlackRect1.centerx
rectArchbishopBlacky10_1 = archbishopBlackRect1.centery - step * 2
rectArchbishopBlack10_1 = pygame.Rect(rectArchbishopBlackx10_1 - 30, rectArchbishopBlacky10_1 - 30, 60, 60)
rectsArchbishopBlack_1.append(rectArchbishopBlack10_1)

rectArchbishopBlackx11_1 = archbishopBlackRect1.centerx - step
rectArchbishopBlacky11_1 = archbishopBlackRect1.centery - step * 2
rectArchbishopBlack11_1 = pygame.Rect(rectArchbishopBlackx11_1 - 30, rectArchbishopBlacky11_1 - 30, 60, 60)
rectsArchbishopBlack_1.append(rectArchbishopBlack11_1)

rectArchbishopBlackx12_1 = archbishopBlackRect1.centerx + step
rectArchbishopBlacky12_1 = archbishopBlackRect1.centery - step * 2
rectArchbishopBlack12_1 = pygame.Rect(rectArchbishopBlackx12_1 - 30, rectArchbishopBlacky12_1 - 30, 60, 60)
rectsArchbishopBlack_1.append(rectArchbishopBlack12_1)

# Morový doktor černý 1
rectsPlagueDoctorBlack_1 = []

rectPlagueBlackx1_1 = plagueDoctorBlackRect1.centerx + step
rectPlagueBlacky1_1 = plagueDoctorBlackRect1.centery
rectPlagueBlack1_1 = pygame.Rect(rectPlagueBlackx1_1 - 30, rectPlagueBlacky1_1 - 30, 60, 60)
rectsPlagueDoctorBlack_1.append(rectPlagueBlack1_1)

rectPlagueBlackx2_1 = plagueDoctorBlackRect1.centerx + step * 2
rectPlagueBlacky2_1 = plagueDoctorBlackRect1.centery
rectPlagueBlack2_1 = pygame.Rect(rectPlagueBlackx2_1 - 30, rectPlagueBlacky2_1 - 30, 60, 60)
rectsPlagueDoctorBlack_1.append(rectPlagueBlack2_1)

rectPlagueBlackx3_1 = plagueDoctorBlackRect1.centerx - step
rectPlagueBlacky3_1 = plagueDoctorBlackRect1.centery
rectPlagueBlack3_1 = pygame.Rect(rectPlagueBlackx3_1 - 30, rectPlagueBlacky3_1 - 30, 60, 60)
rectsPlagueDoctorBlack_1.append(rectPlagueBlack3_1)

rectPlagueBlackx4_1 = plagueDoctorBlackRect1.centerx - step * 2
rectPlagueBlacky4_1 = plagueDoctorBlackRect1.centery
rectPlagueBlack4_1 = pygame.Rect(rectPlagueBlackx4_1 - 30, rectPlagueBlacky4_1 - 30, 60, 60)
rectsPlagueDoctorBlack_1.append(rectPlagueBlack4_1)

rectPlagueBlackx5_1 = plagueDoctorBlackRect1.centerx
rectPlagueBlacky5_1 = plagueDoctorBlackRect1.centery + step
rectPlagueBlack5_1 = pygame.Rect(rectPlagueBlackx5_1 - 30, rectPlagueBlacky5_1 - 30, 60, 60)
rectsPlagueDoctorBlack_1.append(rectPlagueBlack5_1)

rectPlagueBlackx6_1 = plagueDoctorBlackRect1.centerx
rectPlagueBlacky6_1 = plagueDoctorBlackRect1.centery + step * 2
rectPlagueBlack6_1 = pygame.Rect(rectPlagueBlackx6_1 - 30, rectPlagueBlacky6_1 - 30, 60, 60)
rectsPlagueDoctorBlack_1.append(rectPlagueBlack6_1)

rectPlagueBlackx7_1 = plagueDoctorBlackRect1.centerx
rectPlagueBlacky7_1 = plagueDoctorBlackRect1.centery + step * 3
rectPlagueBlack7_1 = pygame.Rect(rectPlagueBlackx7_1 - 30, rectPlagueBlacky7_1 - 30, 60, 60)
rectsPlagueDoctorBlack_1.append(rectPlagueBlack7_1)

rectPlagueBlackx8_1 = plagueDoctorBlackRect1.centerx
rectPlagueBlacky8_1 = plagueDoctorBlackRect1.centery + step * 4
rectPlagueBlack8_1 = pygame.Rect(rectPlagueBlackx8_1 - 30, rectPlagueBlacky8_1 - 30, 60, 60)
rectsPlagueDoctorBlack_1.append(rectPlagueBlack8_1)

rectPlagueBlackx9_1 = plagueDoctorBlackRect1.centerx
rectPlagueBlacky9_1 = plagueDoctorBlackRect1.centery + step * 5
rectPlagueBlack9_1 = pygame.Rect(rectPlagueBlackx9_1 - 30, rectPlagueBlacky9_1 - 30, 60, 60)
rectsPlagueDoctorBlack_1.append(rectPlagueBlack9_1)

rectPlagueBlackx10_1 = plagueDoctorBlackRect1.centerx
rectPlagueBlacky10_1 = plagueDoctorBlackRect1.centery + step * 6
rectPlagueBlack10_1 = pygame.Rect(rectPlagueBlackx10_1 - 30, rectPlagueBlacky10_1 - 30, 60, 60)
rectsPlagueDoctorBlack_1.append(rectPlagueBlack10_1)

rectPlagueBlackx11_1 = plagueDoctorBlackRect1.centerx
rectPlagueBlacky11_1 = plagueDoctorBlackRect1.centery + step * 7
rectPlagueBlack11_1 = pygame.Rect(rectPlagueBlackx11_1 - 30, rectPlagueBlacky11_1 - 30, 60, 60)
rectsPlagueDoctorBlack_1.append(rectPlagueBlack11_1)

rectPlagueBlackx12_1 = plagueDoctorBlackRect1.centerx
rectPlagueBlacky12_1 = plagueDoctorBlackRect1.centery - step
rectPlagueBlack12_1 = pygame.Rect(rectPlagueBlackx12_1 - 30, rectPlagueBlacky12_1 - 30, 60, 60)
rectsPlagueDoctorBlack_1.append(rectPlagueBlack12_1)

rectPlagueBlackx13_1 = plagueDoctorBlackRect1.centerx
rectPlagueBlacky13_1 = plagueDoctorBlackRect1.centery - step * 2
rectPlagueBlack13_1 = pygame.Rect(rectPlagueBlackx13_1 - 30, rectPlagueBlacky13_1 - 30, 60, 60)
rectsPlagueDoctorBlack_1.append(rectPlagueBlack13_1)

rectPlagueBlackx14_1 = plagueDoctorBlackRect1.centerx
rectPlagueBlacky14_1 = plagueDoctorBlackRect1.centery - step * 3
rectPlagueBlack14_1 = pygame.Rect(rectPlagueBlackx14_1 - 30, rectPlagueBlacky14_1 - 30, 60, 60)
rectsPlagueDoctorBlack_1.append(rectPlagueBlack14_1)

rectPlagueBlackx15_1 = plagueDoctorBlackRect1.centerx
rectPlagueBlacky15_1 = plagueDoctorBlackRect1.centery - step * 4
rectPlagueBlack15_1 = pygame.Rect(rectPlagueBlackx15_1 - 30, rectPlagueBlacky15_1 - 30, 60, 60)
rectsPlagueDoctorBlack_1.append(rectPlagueBlack15_1)

rectPlagueBlackx16_1 = plagueDoctorBlackRect1.centerx
rectPlagueBlacky16_1 = plagueDoctorBlackRect1.centery - step * 5
rectPlagueBlack16_1 = pygame.Rect(rectPlagueBlackx16_1 - 30, rectPlagueBlackx16_1 - 30, 60, 60)
rectsPlagueDoctorBlack_1.append(rectPlagueBlack16_1)

rectPlagueBlackx17_1 = plagueDoctorBlackRect1.centerx
rectPlagueBlacky17_1 = plagueDoctorBlackRect1.centery - step * 6
rectPlagueBlack17_1 = pygame.Rect(rectPlagueBlackx17_1 - 30, rectPlagueBlacky17_1 - 30, 60, 60)
rectsPlagueDoctorBlack_1.append(rectPlagueBlack17_1)

rectPlagueBlackx18_1 = plagueDoctorBlackRect1.centerx
rectPlagueBlacky18_1 = plagueDoctorBlackRect1.centery - step * 7
rectPlagueBlack18_1 = pygame.Rect(rectPlagueBlackx18_1 - 30, rectPlagueBlacky18_1 - 30, 60, 60)
rectsPlagueDoctorBlack_1.append(rectPlagueBlack18_1)

# Legionář černý
rectsLegionaryBlack = []

rectLegionaryBlackx1 = legionaryBlackRect.centerx + step
rectLegionaryBlacky1 = legionaryBlackRect.centery - step
rectLegionaryBlack1 = pygame.Rect(rectLegionaryBlackx1 - 30, rectLegionaryBlacky1 - 30, 60, 60)
rectsLegionaryBlack.append(rectLegionaryBlack1)

rectLegionaryBlackx2 = legionaryBlackRect.centerx
rectLegionaryBlacky2 = legionaryBlackRect.centery - step
rectLegionaryBlack2 = pygame.Rect(rectLegionaryBlackx2 - 30, rectLegionaryBlacky2 - 30, 60, 60)
rectsLegionaryBlack.append(rectLegionaryBlack2)

rectLegionaryBlackx3 = legionaryBlackRect.centerx - step
rectLegionaryBlacky3 = legionaryBlackRect.centery - step
rectLegionaryBlack3 = pygame.Rect(rectLegionaryBlackx3 - 30, rectLegionaryBlacky3 - 30, 60, 60)
rectsLegionaryBlack.append(rectLegionaryBlack3)

# Válečník černý
rectsWarriorBlack = []

rectWarriorBlackx1 = warriorBlackRect.centerx + step
rectWarriorBlacky1 = warriorBlackRect.centery
rectWarriorBlack1 = pygame.Rect(rectWarriorBlackx1 - 30, rectWarriorBlacky1 - 30, 60, 60)
rectsWarriorBlack.append(rectWarriorBlack1)

rectWarriorBlackx2 = warriorBlackRect.centerx
rectWarriorBlacky2 = warriorBlackRect.centery + step
rectWarriorBlack2 = pygame.Rect(rectWarriorBlackx2 - 30, rectWarriorBlacky2 - 30, 60, 60)
rectsWarriorBlack.append(rectWarriorBlack2)

rectWarriorBlackx3 = warriorBlackRect.centerx - step
rectWarriorBlacky3 = warriorBlackRect.centery
rectWarriorBlack3 = pygame.Rect(rectWarriorBlackx3 - 30, rectWarriorBlacky3 - 30, 60, 60)
rectsWarriorBlack.append(rectWarriorBlack3)

rectWarriorBlackx4 = warriorBlackRect.centerx
rectWarriorBlacky4 = warriorBlackRect.centery - step
rectWarriorBlack4 = pygame.Rect(rectWarriorBlackx4 - 30, rectWarriorBlacky4 - 30, 60, 60)
rectsWarriorBlack.append(rectWarriorBlack4)

# Válečník černý abilita
rectsWarriorBlackAbility = []

rectWarriorBlackx1Ability = warriorBlackRect.centerx + step * 2
rectWarriorBlack1Ability = warriorBlackRect.centery
rectWarriorBlack1Ability = pygame.Rect(rectWarriorBlackx1Ability - 30, rectWarriorBlack1Ability - 30,
                                       60, 60)
rectsWarriorBlackAbility.append(rectWarriorBlack1Ability)

rectWarriorBlackx2Ability = warriorBlackRect.centerx - step * 2
rectWarriorBlacky2Ability = warriorBlackRect.centery
rectWarriorBlack2Ability = pygame.Rect(rectWarriorBlackx2Ability - 30, rectWarriorBlacky2Ability - 30,
                                       60, 60)
rectsWarriorBlackAbility.append(rectWarriorBlack2Ability)

rectWarriorBlackx3Ability = warriorBlackRect.centerx
rectWarriorBlacky3Ability = warriorBlackRect.centery - step * 2
rectWarriorBlack3Ability = pygame.Rect(rectWarriorBlackx3Ability - 30, rectWarriorBlacky3Ability - 30,
                                       60, 60)
rectsWarriorBlackAbility.append(rectWarriorWhite3Ability)

rectWarriorBlackx4Ability = warriorBlackRect.centerx
rectWarriorBlacky4Ability = warriorBlackRect.centery + step * 2
rectWarriorBlack4Ability = pygame.Rect(rectWarriorBlackx4Ability - 30, rectWarriorBlacky4Ability - 30,
                                       60, 60)
rectsWarriorBlackAbility.append(rectWarriorBlack4Ability)

# Legionář černý 1
rectsLegionaryBlack_1 = []

rectLegionaryBlackx1_1 = legionaryBlackRect1.centerx + step
rectLegionaryBlacky1_1 = legionaryBlackRect1.centery - step
rectLegionaryBlack1_1 = pygame.Rect(rectLegionaryBlackx1_1 - 30, rectLegionaryBlacky1_1 - 30, 60, 60)
rectsLegionaryBlack_1.append(rectLegionaryBlack1_1)

rectLegionaryBlackx2_1 = legionaryBlackRect1.centerx
rectLegionaryBlacky2_1 = legionaryBlackRect1.centery - step
rectLegionaryBlack2_1 = pygame.Rect(rectLegionaryBlackx2_1 - 30, rectLegionaryBlacky2_1 - 30, 60, 60)
rectsLegionaryBlack_1.append(rectLegionaryBlack2_1)

rectLegionaryBlackx3_1 = legionaryBlackRect1.centerx - step
rectLegionaryBlacky3_1 = legionaryBlackRect1.centery - step
rectLegionaryBlack3_1 = pygame.Rect(rectLegionaryBlackx3_1 - 30, rectLegionaryBlacky3_1 - 30, 60, 60)
rectsLegionaryBlack_1.append(rectLegionaryBlack3_1)

# Válečník černý 1
rectsWarriorBlack_1 = []

rectWarriorBlackx1_1 = warriorBlackRect1.centerx + step
rectWarriorBlacky1_1 = warriorBlackRect1.centery
rectWarriorBlack1_1 = pygame.Rect(rectWarriorBlackx1_1 - 30, rectWarriorBlacky1_1 - 30, 60, 60)
rectsWarriorBlack_1.append(rectWarriorBlack1_1)

rectWarriorBlackx2_1 = warriorBlackRect1.centerx
rectWarriorBlacky2_1 = warriorBlackRect1.centery + step
rectWarriorBlack2_1 = pygame.Rect(rectWarriorBlackx2_1 - 30, rectWarriorBlacky2_1 - 30, 60, 60)
rectsWarriorBlack_1.append(rectWarriorBlack2_1)

rectWarriorBlackx3_1 = warriorBlackRect1.centerx
rectWarriorBlacky3_1 = warriorBlackRect1.centery - step
rectWarriorBlack3_1 = pygame.Rect(rectWarriorBlackx3_1 - 30, rectWarriorBlacky3_1 - 30, 60, 60)
rectsWarriorBlack_1.append(rectWarriorBlack3_1)

rectWarriorBlackx4_1 = warriorBlackRect1.centerx - step
rectWarriorBlacky4_1 = warriorBlackRect1.centery
rectWarriorBlack4_1 = pygame.Rect(rectWarriorBlackx4_1 - 30, rectWarriorBlacky4_1 - 30, 60, 60)
rectsWarriorBlack_1.append(rectWarriorBlack4_1)

# Válečník černý 1 abilita
rectsWarriorBlackAbility_1 = []

rectWarriorBlackx1_1Ability = warriorBlackRect1.centerx + step * 2
rectWarriorBlacky1_1Ability = warriorBlackRect1.centery
rectWarriorBlack1_1Ability = pygame.Rect(rectWarriorBlackx1_1Ability - 30, rectWarriorBlacky1_1Ability - 30,
                                         60, 60)
rectsWarriorBlackAbility_1.append(rectWarriorBlack1_1Ability)

rectWarriorBlackx2_1Ability = warriorBlackRect1.centerx - step * 2
rectWarriorBlacky2_1Ability = warriorBlackRect1.centery
rectWarriorBlack2_1Ability = pygame.Rect(rectWarriorBlackx2_1Ability - 30, rectWarriorBlacky2_1Ability - 30,
                                         60, 60)
rectsWarriorBlackAbility_1.append(rectWarriorBlack2_1Ability)

rectWarriorBlackx3_1Ability = warriorBlackRect1.centerx
rectWarriorBlacky3_1Ability = warriorBlackRect1.centery - step * 2
rectWarriorBlack3_1Ability = pygame.Rect(rectWarriorBlackx3_1Ability - 30, rectWarriorBlacky3_1Ability - 30,
                                         60, 60)
rectsWarriorBlackAbility_1.append(rectWarriorBlack3_1Ability)

rectWarriorBlackx4_1Ability = warriorBlackRect1.centerx
rectWarriorBlacky4_1Ability = warriorBlackRect1.centery + step * 2
rectWarriorBlack4_1Ability = pygame.Rect(rectWarriorBlackx4_1Ability - 30, rectWarriorBlacky4_1Ability - 30,
                                         60, 60)
rectsWarriorBlackAbility_1.append(rectWarriorBlack4_1Ability)

# Legionář černý 2
rectsLegionaryBlack_2 = []

rectLegionaryBlackx1_2 = legionaryBlackRect2.centerx + step
rectLegionaryBlacky1_2 = legionaryBlackRect2.centery - step
rectLegionaryBlack1_2 = pygame.Rect(rectLegionaryBlackx1_2 - 30, rectLegionaryBlacky1_2 - 30, 60, 60)
rectsLegionaryBlack_2.append(rectLegionaryBlack1_2)

rectLegionaryBlackx2_2 = legionaryBlackRect2.centerx
rectLegionaryBlacky2_2 = legionaryBlackRect2.centery - step
rectLegionaryBlack2_2 = pygame.Rect(rectLegionaryBlackx2_2 - 30, rectLegionaryBlacky2_2 - 30, 60, 60)
rectsLegionaryBlack_2.append(rectLegionaryBlack2_2)

rectLegionaryBlackx3_2 = legionaryBlackRect2.centerx - step
rectLegionaryBlacky3_2 = legionaryBlackRect2.centery - step
rectLegionaryBlack3_2 = pygame.Rect(rectLegionaryBlackx3_2 - 30, rectLegionaryBlacky3_2 - 30, 60, 60)
rectsLegionaryBlack_2.append(rectLegionaryBlack3_2)

# Válečník černý 2
rectsWarriorBlack_2 = []

rectWarriorBlackx1_2 = warriorBlackRect2.centerx + step
rectWarriorBlacky1_2 = warriorBlackRect2.centery
rectWarriorBlack1_2 = pygame.Rect(rectWarriorBlackx1_2 - 30, rectWarriorBlacky1_2 - 30, 60, 60)
rectsWarriorBlack_2.append(rectWarriorBlack1_2)

rectWarriorBlackx2_2 = warriorBlackRect2.centerx
rectWarriorBlacky2_2 = warriorBlackRect2.centery + step
rectWarriorBlack2_2 = pygame.Rect(rectWarriorBlackx2_2 - 30, rectWarriorBlacky2_2 - 30, 60, 60)
rectsWarriorBlack_2.append(rectWarriorBlack2_2)

rectWarriorBlackx3_2 = warriorBlackRect2.centerx - step
rectWarriorBlacky3_2 = warriorBlackRect2.centery
rectWarriorBlack3_2 = pygame.Rect(rectWarriorBlackx3_2 - 30, rectWarriorBlacky3_2 - 30, 60, 60)
rectsWarriorBlack_2.append(rectWarriorBlack3_2)

rectWarriorBlackx4_2 = warriorBlackRect2.centerx
rectWarriorBlacky4_2 = warriorBlackRect2.centery - step
rectWarriorBlack4_2 = pygame.Rect(rectWarriorBlackx4_2 - 30, rectWarriorBlacky4_2 - 30, 60, 60)
rectsWarriorBlack_2.append(rectWarriorBlack4_2)

# Válečník černý 2 abilita
rectsWarriorBlackAbility_2 = []

rectWarriorBlackx1_2Ability = warriorBlackRect2.centerx + step * 2
rectWarriorBlacky1_2Ability = warriorBlackRect2.centery
rectWarriorBlack1_2Ability = pygame.Rect(rectWarriorBlackx1_2Ability - 30, rectWarriorBlacky1_2Ability - 30,
                                         60, 60)
rectsWarriorBlackAbility_2.append(rectWarriorBlack1_2Ability)

rectWarriorBlackx2_2Ability = warriorBlackRect2.centerx - step * 2
rectWarriorBlacky2_2Ability = warriorBlackRect2.centery
rectWarriorBlack2_2Ability = pygame.Rect(rectWarriorBlackx2_2Ability - 30, rectWarriorBlacky2_2Ability - 30,
                                         60, 60)
rectsWarriorBlackAbility_2.append(rectWarriorBlack2_2Ability)

rectWarriorBlackx3_2Ability = warriorBlackRect2.centerx
rectWarriorBlacky3_2Ability = warriorBlackRect2.centery - step * 2
rectWarriorBlack3_2Ability = pygame.Rect(rectWarriorBlackx3_2Ability - 30, rectWarriorBlacky3_2Ability - 30,
                                         60, 60)
rectsWarriorBlackAbility_2.append(rectWarriorBlack3_2Ability)

rectWarriorBlackx4_2Ability = warriorBlackRect2.centerx
rectWarriorBlacky4_2Ability = warriorBlackRect2.centery + step * 2
rectWarriorBlack4_2Ability = pygame.Rect(rectWarriorBlackx4_2Ability - 30, rectWarriorBlacky4_2Ability - 30,
                                         60, 60)
rectsWarriorBlackAbility_2.append(rectWarriorBlack4_2Ability)

# Legionář černý 3
rectsLegionaryBlack_3 = []

rectLegionaryBlackx1_3 = legionaryBlackRect3.centerx + step
rectLegionaryBlacky1_3 = legionaryBlackRect3.centery - step
rectLegionaryBlack1_3 = pygame.Rect(rectLegionaryBlackx1_3 - 30, rectLegionaryBlacky1_3 - 30, 60, 60)
rectsLegionaryBlack_3.append(rectLegionaryBlack1_3)

rectLegionaryBlackx2_3 = legionaryBlackRect3.centerx
rectLegionaryBlacky2_3 = legionaryBlackRect3.centery - step
rectLegionaryBlack2_3 = pygame.Rect(rectLegionaryBlackx2_3 - 30, rectLegionaryBlacky2_3 - 30, 60, 60)
rectsLegionaryBlack_3.append(rectLegionaryBlack2_3)

rectLegionaryBlackx3_3 = legionaryBlackRect3.centerx - step
rectLegionaryBlacky3_3 = legionaryBlackRect3.centery - step
rectLegionaryBlack3_3 = pygame.Rect(rectLegionaryBlackx3_3 - 30, rectLegionaryBlacky3_3 - 30, 60, 60)
rectsLegionaryBlack_3.append(rectLegionaryBlack3_3)

# Válečník černý 3
rectsWarriorBlack_3 = []

rectWarriorBlackx1_3 = warriorBlackRect3.centerx
rectWarriorBlacky1_3 = warriorBlackRect3.centery + step
rectWarriorBlack1_3 = pygame.Rect(rectWarriorBlackx1_3 - 30, rectWarriorBlacky1_3 - 30, 60, 60)
rectsWarriorBlack_3.append(rectWarriorBlack1_3)

rectWarriorBlackx2_3 = warriorBlackRect3.centerx - step
rectWarriorBlacky2_3 = warriorBlackRect3.centery
rectWarriorBlack2_3 = pygame.Rect(rectWarriorBlackx2_3 - 30, rectWarriorBlacky2_3 - 30, 60, 60)
rectsWarriorBlack_3.append(rectWarriorBlack2_3)

rectWarriorBlackx3_3 = warriorBlackRect3.centerx
rectWarriorBlacky3_3 = warriorBlackRect3.centery - step
rectWarriorBlack3_3 = pygame.Rect(rectWarriorBlackx3_3 - 30, rectWarriorBlacky3_3 - 30, 60, 60)
rectsWarriorBlack_3.append(rectWarriorBlack3_3)

rectWarriorBlackx4_3 = warriorBlackRect3.centerx + step
rectWarriorBlacky4_3 = warriorBlackRect3.centery
rectWarriorBlack4_3 = pygame.Rect(rectWarriorBlackx4_3 - 30, rectWarriorBlacky4_3 - 30, 60, 60)
rectsWarriorBlack_3.append(rectWarriorBlack4_3)

# Válečník černý 3 abilita
rectsWarriorBlackAbility_3 = []

rectWarriorBlackx1_3Ability = warriorBlackRect3.centerx + step * 2
rectWarriorBlacky1_3Ability = warriorBlackRect3.centery
rectWarriorBlack1_3Ability = pygame.Rect(rectWarriorBlackx1_3Ability - 30, rectWarriorBlacky1_3Ability - 30,
                                         60, 60)
rectsWarriorBlackAbility_3.append(rectWarriorBlack1_3Ability)

rectWarriorBlackx2_3Ability = warriorBlackRect3.centerx - step * 2
rectWarriorBlacky2_3Ability = warriorBlackRect3.centery
rectWarriorBlack2_3Ability = pygame.Rect(rectWarriorBlackx2_3Ability - 30, rectWarriorBlacky2_3Ability - 30,
                                         60, 60)
rectsWarriorBlackAbility_3.append(rectWarriorBlack2_3Ability)

rectWarriorBlackx3_3Ability = warriorBlackRect3.centerx
rectWarriorBlacky3_3Ability = warriorBlackRect3.centery - step * 2
rectWarriorBlack3_3Ability = pygame.Rect(rectWarriorBlackx3_3Ability - 30, rectWarriorBlacky3_3Ability - 30,
                                         60, 60)
rectsWarriorBlackAbility_3.append(rectWarriorBlack3_3Ability)

rectWarriorBlackx4_3Ability = warriorBlackRect3.centerx
rectWarriorBlacky4_3Ability = warriorBlackRect3.centery + step * 2
rectWarriorBlack4_3Ability = pygame.Rect(rectWarriorBlackx4_3Ability - 30, rectWarriorBlacky4_3Ability - 30,
                                         60, 60)
rectsWarriorBlackAbility_3.append(rectWarriorBlack4_3Ability)

# endregion

# Nastavení counteru, který určuje, jaká barva je na tahu
counter = 0

# Nastavení bool proměnných pro funkčnost programu v prvotní fázi
active = False
active1 = False
active2 = False
empty = False
user = False
pohyb = False
show_main_menu = True
play_game = False
run = True
pohybuje = False

#Nastavení bool proměnných pro možnost tažení pro danou figurku, aby nemohly v současnou chvíli táhnout i jiné figurky
plagueDoctorWhitePlaying=False
archbishopWhitePlaying=False
cardinalWhitePlaying=False
hadesWhitePlaying=False
persephoneWhitePlaying=False
cardinalWhitePlaying1=False
archbishopWhitePlaying1=False
plagueDoctorWhitePlaying1=False
legionaryWhitePlaying=False
warriorWhitePlaying=False
legionaryWhitePlaying1=False
warriorWhitePlaying1=False
legionaryWhitePlaying2=False
warriorWhitePlaying2=False
legionaryWhitePlaying3=False
warriorWhitePlaying3=False
figuresWhitePlaying=[plagueDoctorWhitePlaying,archbishopWhitePlaying,cardinalWhitePlaying,hadesWhitePlaying,persephoneWhitePlaying,cardinalWhitePlaying1,archbishopWhitePlaying1,plagueDoctorWhitePlaying1,legionaryWhitePlaying,warriorWhitePlaying,legionaryWhitePlaying1,warriorWhitePlaying1,legionaryWhitePlaying2,warriorWhitePlaying2,legionaryWhitePlaying3,warriorWhitePlaying3]

plagueDoctorBlackPlaying=False
archbishopBlackPlaying=False
cardinalBlackPlaying=False
hadesBlackPlaying=False
persephoneBlackPlaying=False
cardinalBlackPlaying1=False
archbishopBlackPlaying1=False
plagueDoctorBlackPlaying1=False
legionaryBlackPlaying=False
warriorBlackPlaying=False
legionaryBlackPlaying1=False
warriorBlackPlaying1=False
legionaryBlackPlaying2=False
warriorBlackPlaying2=False
legionaryBlackPlaying3=False
warriorBlackPlaying3=False
figuresBlackPlaying=[plagueDoctorBlackPlaying,archbishopBlackPlaying,cardinalBlackPlaying,hadesBlackPlaying,persephoneBlackPlaying,cardinalBlackPlaying1,archbishopBlackPlaying1,plagueDoctorBlackPlaying1,legionaryBlackPlaying,warriorBlackPlaying,legionaryBlackPlaying1,warriorBlackPlaying1,legionaryBlackPlaying2,warriorBlackPlaying2,legionaryBlackPlaying3,warriorBlackPlaying3]

figuresWhite = [plagueDoctorWhiteRect, archbishopWhiteRect, cardinalWhiteRect, hadesWhiteRect, persephoneWhiteRect,
                cardinalWhiteRect1, archbishopWhiteRect1, plagueDoctorWhiteRect1, legionaryWhiteRect,
                warriorWhiteRect, legionaryWhiteRect1, warriorWhiteRect1, legionaryWhiteRect2, warriorWhiteRect2,
                legionaryWhiteRect3, warriorWhiteRect3]
figuresBlack = [plagueDoctorBlackRect, archbishopBlackRect, cardinalBlackRect, hadesBlackRect,
                persephoneBlackRect, cardinalBlackRect1, archbishopBlackRect1, plagueDoctorBlackRect1,
                legionaryBlackRect, warriorBlackRect, legionaryBlackRect1, warriorBlackRect1,
                legionaryBlackRect2, warriorBlackRect2, legionaryBlackRect3, warriorBlackRect3]

while run:
    mx, my = pygame.mouse.get_pos()

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button2.collidepoint(event.pos) and show_main_menu:
                run = False
            if button.collidepoint(event.pos) and show_main_menu:
                show_main_menu = False
                play_game = True
                pygame.mixer.music.stop()
                start_game.play()
                screen.fill((0, 0, 0))
            if input_box1.collidepoint(event.pos) and show_main_menu:
                active = True
            else:
                active = False
            if input_box2.collidepoint(event.pos) and show_main_menu:
                active1 = True
            else:
                active1 = False
            if send_box.collidepoint(event.pos) and show_main_menu:
                active2 = True
                if input_user_text1 == '' or input_user_text2 == '':
                    screen.blit(fill_header, fill_header_rect)
                    empty = True
                else:
                    empty = False
                    conn = mysql.connector.connect(
                        host="dbs.spskladno.cz",
                        user="student3",
                        password="spsnet",
                        database="vyuka3"
                    )
                    cursor1 = conn.cursor()
                    print(input_user_text1, input_user_text2)
                    query = "SELECT * FROM registracechess WHERE email = %s AND password = %s"
                    cursor1.execute(query, (input_user_text1, input_user_text2))
                    user = cursor1.fetchone()
                    # cursor1.close() z nějakého důvodu to s tímto po přihlášení padá, AI nepomohlo
                    conn.close()

                    if user:
                        screen.blit(logged_header, logged_header_rect)
                        print("Úspěch")
                        user_email = input_user_text1
                        input_user_text1 = ''
                        input_user_text2 = ''

                    else:
                        screen.blit(failed_header, failed_header_rect)
                        print("Neúspěch")
            else:
                active2 = False

        if event.type == pygame.KEYDOWN and show_main_menu:
            if event.key == pygame.K_BACKSPACE:
                if active:
                    input_user_text1 = input_user_text1[:-1]
            else:
                if active:
                    input_user_text1 += event.unicode
            if event.key == pygame.K_BACKSPACE:
                if active1:
                    input_user_text2 = input_user_text2[:-1]
            else:
                if active1:
                    input_user_text2 += event.unicode
                    inputUserText2Hidden += '*'
        if event.type == music_end and show_main_menu:
            song = random.choice(songs)
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(1, 0)

    # Kontrola kolize s buttonem
    x, y = pygame.mouse.get_pos()

    if show_main_menu:
        # Vykreslení pozadí
        screen.blit(background_image, background_image_rect)
        # Hover pro buttony
        if button.x <= x <= button.x + 300 and button.y <= y <= button.y + 80:
            pygame.draw.rect(screen, (180, 180, 180), button)
        else:
            pygame.draw.rect(screen, (110, 110, 110), button)

        if button1.x <= x <= button1.x + 300 and button1.y <= y <= button1.y + 80:
            pygame.draw.rect(screen, (180, 180, 180), button1)
        else:
            pygame.draw.rect(screen, (110, 110, 110), button1)

        if button2.x <= x <= button2.x + 300 and button2.y <= y <= button2.y + 80:
            pygame.draw.rect(screen, (180, 180, 180), button2)
        else:
            pygame.draw.rect(screen, (110, 110, 110), button2)

        # Vykreslení textu pro buttony
        screen.blit(button_text_start_game, button_text_start_game_rect)
        screen.blit(button_text_start_game1, button_text_start_game_rect1)
        screen.blit(button_text_start_game2, button_text_start_game_rect2)

        # Vykreslení pozadí leaderboardu a textu leaderboardu
        pygame.draw.rect(screen, black, leaderboard_background)
        screen.blit(leaderboard_text, leaderboard_text_rect)

        # Vypsání dat pro leadeboard
        y = 100
        for row in result:
            text = " - ".join(str(item) for item in row)
            text_surface = leadeboard_text_font.render(text, True, white)
            print(text_surface)
            screen.blit(text_surface, (1500, y))
            y += 40

            # Vykreslení login formu
        if active:
            color = active_color
        else:
            color = passive_collor
        if active1:
            color1 = active_color
        else:
            color1 = passive_collor
        if active2:
            color2 = active_color
            if user:
                screen.blit(logged_header, logged_header_rect)
            elif empty:
                screen.blit(fill_header, fill_header_rect)
            else:
                screen.blit(failed_header, failed_header_rect)
        else:
            color2 = passive_collor

        # Vykreslení login formu
        pygame.draw.rect(screen, color, input_box1)
        pygame.draw.rect(screen, color1, input_box2)
        pygame.draw.rect(screen, color2, send_box)

        input_text = input_font.render(input_user_text1, True, (0, 0, 0))
        input_text1 = input_font.render(inputUserText2Hidden, True, (0, 0, 0))

        screen.blit(input_text, (input_box1.x + 5, input_box1.y + 5))
        screen.blit(input_text1, (input_box2.x + 5, input_box2.y + 5))

        input_box1.w = max(500, input_text.get_width() + 10)
        input_box2.w = max(500, input_text1.get_width() + 10)
        input_box2.w = 500

        screen.blit(mail_header, mail_header_rect)
        screen.blit(pass_header, pass_header_rect)
        screen.blit(send_header, send_header_rect)

        # Vykreslení názvu hry
        screen.blit(title_header, title_header_rect)

    if play_game:
        # Zastavení hudby v pozadí
        pygame.mixer.music.stop()

        scale = 120
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0:
                    pygame.draw.rect(screen, (255, 248, 220), (x * scale + 480, y * scale + 60, scale, scale))
                else:
                    pygame.draw.rect(screen, (139, 69, 19), (x * scale + 480, y * scale + 60, scale, scale))
        if plagueDoctorWhiteRect in figuresWhite:
            screen.blit(plagueDoctorWhite, plagueDoctorWhiteRect)
        if archbishopWhiteRect in figuresWhite:
            screen.blit(archbishopWhite, archbishopWhiteRect)
        if cardinalWhiteRect in figuresWhite:
            screen.blit(cardinalWhite, cardinalWhiteRect)
        if hadesWhiteRect in figuresWhite:
            screen.blit(hadesWhite, hadesWhiteRect)
        if persephoneWhiteRect in figuresWhite:
            screen.blit(persephoneWhite, persephoneWhiteRect)
        if cardinalWhiteRect1 in figuresWhite:
            screen.blit(cardinalWhite, cardinalWhiteRect1)
        if archbishopWhiteRect1 in figuresWhite:
            screen.blit(archbishopWhite, archbishopWhiteRect1)
        if plagueDoctorWhiteRect1 in figuresWhite:
            screen.blit(plagueDoctorWhite, plagueDoctorWhiteRect1)
        if legionaryWhiteRect in figuresWhite:
            screen.blit(legionaryWhite, legionaryWhiteRect)
        if warriorWhiteRect in figuresWhite:
            screen.blit(warriorWhite, warriorWhiteRect)
        if legionaryWhiteRect1 in figuresWhite:
            screen.blit(legionaryWhite, legionaryWhiteRect1)
        if warriorWhiteRect1 in figuresWhite:
            screen.blit(warriorWhite, warriorWhiteRect1)
        if legionaryWhiteRect2 in figuresWhite:
            screen.blit(legionaryWhite, legionaryWhiteRect2)
        if warriorWhiteRect2 in figuresWhite:
            screen.blit(warriorWhite, warriorWhiteRect2)
        if legionaryWhiteRect3 in figuresWhite:
            screen.blit(legionaryWhite, legionaryWhiteRect3)
        if warriorWhiteRect3 in figuresWhite:
            screen.blit(warriorWhite, warriorWhiteRect3)

        if plagueDoctorBlackRect in figuresBlack:
            screen.blit(plagueDoctorBlack, plagueDoctorBlackRect)
        if archbishopBlackRect in figuresBlack:
            screen.blit(archbishopBlack, archbishopBlackRect)
        if cardinalBlackRect in figuresBlack:
            screen.blit(cardinalBlack, cardinalBlackRect)
        if hadesBlackRect in figuresBlack:
            screen.blit(hadesBlack, hadesBlackRect)
        if persephoneBlackRect in figuresBlack:
            screen.blit(persephoneBlack, persephoneBlackRect)
        if cardinalBlackRect1 in figuresBlack:
            screen.blit(cardinalBlack, cardinalBlackRect1)
        if archbishopBlackRect1 in figuresBlack:
            screen.blit(archbishopBlack, archbishopBlackRect1)
        if plagueDoctorBlackRect1 in figuresBlack:
            screen.blit(plagueDoctorBlack, plagueDoctorBlackRect1)
        if legionaryBlackRect in figuresBlack:
            screen.blit(legionaryBlack, legionaryBlackRect)
        if warriorBlackRect in figuresBlack:
            screen.blit(warriorBlack, warriorBlackRect)
        if legionaryBlackRect1 in figuresBlack:
            screen.blit(legionaryBlack, legionaryBlackRect1)
        if warriorBlackRect1 in figuresBlack:
            screen.blit(warriorBlack, warriorBlackRect1)
        if legionaryBlackRect2 in figuresBlack:
            screen.blit(legionaryBlack, legionaryBlackRect2)
        if warriorBlackRect2 in figuresBlack:
            screen.blit(warriorBlack, warriorBlackRect2)
        if legionaryBlackRect3 in figuresBlack:
            screen.blit(legionaryBlack, legionaryBlackRect3)
        if warriorBlackRect3 in figuresBlack:
            screen.blit(warriorBlack, warriorBlackRect3)

        # Tažení figurek

        # Opětovné deklarování pozic čtverců pro pohyb figurek, aby zůstaly na místě a nepohybovaly se společně s figurkou při jejím pohybu
        if not pohyb:
            plagueWhitexInit = plagueDoctorWhiteRect.centerx
            plagueWhiteyInit = plagueDoctorWhiteRect.centery

            rectPlagueWhitex1 = plagueDoctorWhiteRect.centerx + step
            rectPlagueWhitey1 = plagueDoctorWhiteRect.centery
            rectPlagueWhite1 = pygame.Rect(rectPlagueWhitex1 - 30, rectPlagueWhitey1 - 30, 60, 60)

            rectPlagueWhitex2 = plagueDoctorWhiteRect.centerx + step * 2
            rectPlagueWhitey2 = plagueDoctorWhiteRect.centery
            rectPlagueWhite2 = pygame.Rect(rectPlagueWhitex2 - 30, rectPlagueWhitey2 - 30, 60, 60)

            rectPlagueWhitex3 = plagueDoctorWhiteRect.centerx - step
            rectPlagueWhitey3 = plagueDoctorWhiteRect.centery
            rectPlagueWhite3 = pygame.Rect(rectPlagueWhitex3 - 30, rectPlagueWhitey3 - 30, 60, 60)

            rectPlagueWhitex4 = plagueDoctorWhiteRect.centerx - 2 * step
            rectPlagueWhitey4 = plagueDoctorWhiteRect.centery
            rectPlagueWhite4 = pygame.Rect(rectPlagueWhitex4 - 30, rectPlagueWhitey4 - 30, 60, 60)

            rectPlagueWhitex5 = plagueDoctorWhiteRect.centerx
            rectPlagueWhitey5 = plagueDoctorWhiteRect.centery + step
            rectPlagueWhite5 = pygame.Rect(rectPlagueWhitex5 - 30, rectPlagueWhitey5 - 30, 60, 60)

            rectPlagueWhitex6 = plagueDoctorWhiteRect.centerx
            rectPlagueWhitey6 = plagueDoctorWhiteRect.centery + step * 2
            rectPlagueWhite6 = pygame.Rect(rectPlagueWhitex6 - 30, rectPlagueWhitey6 - 30, 60, 60)

            rectPlagueWhitex7 = plagueDoctorWhiteRect.centerx
            rectPlagueWhitey7 = plagueDoctorWhiteRect.centery + step * 3
            rectPlagueWhite7 = pygame.Rect(rectPlagueWhitex7 - 30, rectPlagueWhitey7 - 30, 60, 60)

            rectPlagueWhitex8 = plagueDoctorWhiteRect.centerx
            rectPlagueWhitey8 = plagueDoctorWhiteRect.centery + step * 4
            rectPlagueWhite8 = pygame.Rect(rectPlagueWhitex8 - 30, rectPlagueWhitey8 - 30, 60, 60)

            rectPlagueWhitex9 = plagueDoctorWhiteRect.centerx
            rectPlagueWhitey9 = plagueDoctorWhiteRect.centery + step * 5
            rectPlagueWhite9 = pygame.Rect(rectPlagueWhitex9 - 30, rectPlagueWhitey9 - 30, 60, 60)

            rectPlagueWhitex10 = plagueDoctorWhiteRect.centerx
            rectPlagueWhitey10 = plagueDoctorWhiteRect.centery + step * 6
            rectPlague10 = pygame.Rect(rectPlagueWhitex10 - 30, rectPlagueWhitey10 - 30, 60, 60)

            rectPlagueWhitex11 = plagueDoctorWhiteRect.centerx
            rectPlagueWhitey11 = plagueDoctorWhiteRect.centery + step * 7
            rectPlagueWhite11 = pygame.Rect(rectPlagueWhitex11 - 30, rectPlagueWhitey11 - 30, 60, 60)

            rectPlagueWhitex12 = plagueDoctorWhiteRect.centerx
            rectPlagueWhitey12 = plagueDoctorWhiteRect.centery - step
            rectPlagueWhite12 = pygame.Rect(rectPlagueWhitex12 - 30, rectPlagueWhitey12 - 30, 60, 60)

            rectPlagueWhitex13 = plagueDoctorWhiteRect.centerx
            rectPlagueWhitey13 = plagueDoctorWhiteRect.centery - step * 2
            rectPlagueWhite13 = pygame.Rect(rectPlagueWhitex13 - 30, rectPlagueWhitey13 - 30, 60, 60)

            rectPlagueWhitex14 = plagueDoctorWhiteRect.centerx
            rectPlagueWhitey14 = plagueDoctorWhiteRect.centery - step * 3
            rectPlagueWhite14 = pygame.Rect(rectPlagueWhitex14 - 30, rectPlagueWhitey14 - 30, 60, 60)

            rectPlagueWhitex15 = plagueDoctorWhiteRect.centerx
            rectPlagueWhitey15 = plagueDoctorWhiteRect.centery - step * 4
            rectPlagueWhite15 = pygame.Rect(rectPlagueWhitex15 - 30, rectPlagueWhitey15 - 30, 60, 60)

            rectPlagueWhitex16 = plagueDoctorWhiteRect.centerx
            rectPlagueyWhite16 = plagueDoctorWhiteRect.centery - step * 5
            rectPlagueWhite16 = pygame.Rect(rectPlagueWhitex16 - 30, rectPlagueyWhite16 - 30, 60, 60)

            rectPlagueWhitex17 = plagueDoctorWhiteRect.centerx
            rectPlagueWhitey17 = plagueDoctorWhiteRect.centery - step * 6
            rectPlagueWhite17 = pygame.Rect(rectPlagueWhitex17 - 30, rectPlagueWhitey17 - 30, 60, 60)

            rectPlagueWhitex18 = plagueDoctorWhiteRect.centerx
            rectPlagueWhitey18 = plagueDoctorWhiteRect.centery - step * 7
            rectPlagueWhite18 = pygame.Rect(rectPlagueWhitex18 - 30, rectPlagueWhitey18 - 30, 60, 60)

            # Arcibiskup bílý
            archbishopWhitexInit = archbishopWhiteRect.centerx
            archbishopWhiteyInit = archbishopWhiteRect.centery

            rectArchbishopWhitex1 = archbishopWhiteRect.centerx + step * 2
            rectArchbishopWhitey1 = archbishopWhiteRect.centery
            rectArchbishopWhite1 = pygame.Rect(rectArchbishopWhitex1 - 30, rectArchbishopWhitey1 - 30, 60, 60)

            rectArchbishopWhitex2 = archbishopWhiteRect.centerx + step * 2
            rectArchbishopWhitey2 = archbishopWhiteRect.centery + step
            rectArchbishopWhite2 = pygame.Rect(rectArchbishopWhitex2 - 30, rectArchbishopWhitey2 - 30, 60, 60)

            rectArchbishopWhitex3 = archbishopWhiteRect.centerx + step * 2
            rectArchbishopWhitey3 = archbishopWhiteRect.centery - step
            rectArchbishopWhite3 = pygame.Rect(rectArchbishopWhitex3 - 30, rectArchbishopWhitey3 - 30, 60, 60)

            rectArchbishopWhitex4 = archbishopWhiteRect.centerx - step * 2
            rectArchbishopWhitey4 = archbishopWhiteRect.centery
            rectArchbishopWhite4 = pygame.Rect(rectArchbishopWhitex4 - 30, rectArchbishopWhitey4 - 30, 60, 60)

            rectArchbishopWhitex5 = archbishopWhiteRect.centerx - step * 2
            rectArchbishopWhitey5 = archbishopWhiteRect.centery + step
            rectArchbishopWhite5 = pygame.Rect(rectArchbishopWhitex5 - 30, rectArchbishopWhitey5 - 30, 60, 60)

            rectArchbishopWhitex6 = archbishopWhiteRect.centerx - step * 2
            rectArchbishopWhitey6 = archbishopWhiteRect.centery - step
            rectArchbishopWhite6 = pygame.Rect(rectArchbishopWhitex6 - 30, rectArchbishopWhitey6 - 30, 60, 60)

            rectArchbishopWhitex7 = archbishopWhiteRect.centerx
            rectArchbishopWhitey7 = archbishopWhiteRect.centery + step * 2
            rectArchbishopWhite7 = pygame.Rect(rectArchbishopWhitex7 - 30, rectArchbishopWhitey7 - 30, 60, 60)

            rectArchbishopWhitex8 = archbishopWhiteRect.centerx + step
            rectArchbishopWhitey8 = archbishopWhiteRect.centery + step * 2
            rectArchbishopWhite8 = pygame.Rect(rectArchbishopWhitex8 - 30, rectArchbishopWhitey8 - 30, 60, 60)

            rectArchbishopWhitex9 = archbishopWhiteRect.centerx - step
            rectArchbishopWhitey9 = archbishopWhiteRect.centery + step * 2
            rectArchbishopWhite9 = pygame.Rect(rectArchbishopWhitex9 - 30, rectArchbishopWhitey9 - 30, 60, 60)

            rectArchbishopWhitex10 = archbishopWhiteRect.centerx
            rectArchbishopWhitey10 = archbishopWhiteRect.centery - step * 2
            rectArchbishopWhite10 = pygame.Rect(rectArchbishopWhitex10 - 30, rectArchbishopWhitey10 - 30, 60, 60)

            rectArchbishopWhitex11 = archbishopWhiteRect.centerx + step
            rectArchbishopWhitey11 = archbishopWhiteRect.centery - step * 2
            rectArchbishopWhite11 = pygame.Rect(rectArchbishopWhitex11 - 30, rectArchbishopWhitey11 - 30, 60, 60)

            rectArchbishopWhitex12 = archbishopWhiteRect.centerx - step
            rectArchbishopWhitey12 = archbishopWhiteRect.centery - step * 2
            rectArchbishopWhite12 = pygame.Rect(rectArchbishopWhitex12 - 30, rectArchbishopWhitey12 - 30, 60, 60)

            # Kardinál bílý
            cardinalWhitexInit = cardinalWhiteRect.centerx
            cardinalWhiteyInit = cardinalWhiteRect.centery

            rectsCardinalWhite = []

            rectCardinalWhitex1 = cardinalWhiteRect.centerx + step
            rectCardinalWhitey1 = cardinalWhiteRect.centery - step
            rectCardinalWhite1 = pygame.Rect(rectCardinalWhitex1 - 30, rectCardinalWhitey1 - 30, 60, 60)
            rectsCardinalWhite.append(rectCardinalWhite1)

            rectCardinalWhitex2 = cardinalWhiteRect.centerx - step
            rectCardinalWhitey2 = cardinalWhiteRect.centery - step
            rectCardinalWhite2 = pygame.Rect(rectCardinalWhitex2 - 30, rectCardinalWhitey2 - 30, 60, 60)
            rectsCardinalWhite.append(rectCardinalWhite2)

            rectCardinalWhitex3 = cardinalWhiteRect.centerx + step
            rectCardinalWhitey3 = cardinalWhiteRect.centery + step
            rectCardinalWhite3 = pygame.Rect(rectCardinalWhitex3 - 30, rectCardinalWhitey3 - 30, 60, 60)
            rectsCardinalWhite.append(rectCardinalWhite3)

            rectCardinalWhitex4 = cardinalWhiteRect.centerx - step
            rectCardinalWhitey4 = cardinalWhiteRect.centery + step
            rectCardinalWhite4 = pygame.Rect(rectCardinalWhitex4 - 30, rectCardinalWhitey4 - 30, 60, 60)
            rectsCardinalWhite.append(rectCardinalWhite4)

            # Hádes bílý
            hadesWhitexInit = hadesWhiteRect.centerx
            hadesWhiteyInit = hadesWhiteRect.centery

            rectsHadesWhite = []

            rectHadesWhitex1 = hadesWhiteRect.centerx
            rectHadesWhitey1 = hadesWhiteRect.centery - step
            rectHadesWhite1 = pygame.Rect(rectHadesWhitex1 - 30, rectHadesWhitey1 - 30, 60, 60)
            rectsHadesWhite.append(rectHadesWhite1)

            rectHadesWhitex2 = hadesWhiteRect.centerx
            rectHadesWhitey2 = hadesWhiteRect.centery - step * 2
            rectHadesWhite2 = pygame.Rect(rectHadesWhitex2 - 30, rectHadesWhitey2 - 30, 60, 60)
            rectsHadesWhite.append(rectHadesWhite2)

            rectHadesWhitex3 = hadesWhiteRect.centerx
            rectHadesWhitey3 = hadesWhiteRect.centery - step * 3
            rectHadesWhite3 = pygame.Rect(rectHadesWhitex3 - 30, rectHadesWhitey3 - 30, 60, 60)
            rectsHadesWhite.append(rectHadesWhite3)

            rectHadesWhitex4 = hadesWhiteRect.centerx + step
            rectHadesWhitey4 = hadesWhiteRect.centery - step
            rectHadesWhite4 = pygame.Rect(rectHadesWhitex4 - 30, rectHadesWhitey4 - 30, 60, 60)
            rectsHadesWhite.append(rectHadesWhite4)

            rectHadesWhitex5 = hadesWhiteRect.centerx + step * 2
            rectHadesWhitey5 = hadesWhiteRect.centery - step * 2
            rectHadesWhite5 = pygame.Rect(rectHadesWhitex5 - 30, rectHadesWhitey5 - 30, 60, 60)
            rectsHadesWhite.append(rectHadesWhite5)

            rectHadesWhitex6 = hadesWhiteRect.centerx + step * 3
            rectHadesWhitey6 = hadesWhiteRect.centery - step * 3
            rectHadesWhite6 = pygame.Rect(rectHadesWhitex6 - 30, rectHadesWhitey6 - 30, 60, 60)
            rectsHadesWhite.append(rectHadesWhite6)

            rectHadesWhitex7 = hadesWhiteRect.centerx + step
            rectHadesWhitey7 = hadesWhiteRect.centery
            rectHadesWhite7 = pygame.Rect(rectHadesWhitex7 - 30, rectHadesWhitey7 - 30, 60, 60)
            rectsHadesWhite.append(rectHadesWhite7)

            rectHadesWhitex8 = hadesWhiteRect.centerx + step * 2
            rectHadesWhitey8 = hadesWhiteRect.centery
            rectHadesWhite8 = pygame.Rect(rectHadesWhitex8 - 30, rectHadesWhitey8 - 30, 60, 60)
            rectsHadesWhite.append(rectHadesWhite8)

            rectHadesWhitex9 = hadesWhiteRect.centerx + step * 3
            rectHadesWhitey9 = hadesWhiteRect.centery
            rectHadesWhite9 = pygame.Rect(rectHadesWhitex9 - 30, rectHadesWhitey9 - 30, 60, 60)
            rectsHadesWhite.append(rectHadesWhite9)

            rectHadesWhitex10 = hadesWhiteRect.centerx + step
            rectHadesWhitey10 = hadesWhiteRect.centery + step
            rectHadesWhite10 = pygame.Rect(rectHadesWhitex10 - 30, rectHadesWhitey10 - 30, 60, 60)
            rectsHadesWhite.append(rectHadesWhite10)

            rectHadesWhitex11 = hadesWhiteRect.centerx + step * 2
            rectHadesWhitey11 = hadesWhiteRect.centery + step * 2
            rectHadesWhite11 = pygame.Rect(rectHadesWhitex11 - 30, rectHadesWhitey11 - 30, 60, 60)
            rectsHadesWhite.append(rectHadesWhite11)

            rectHadesWhitex12 = hadesWhiteRect.centerx - step
            rectHadesWhitey12 = hadesWhiteRect.centery - step
            rectHadesWhite12 = pygame.Rect(rectHadesWhitex12 - 30, rectHadesWhitey12 - 30, 60, 60)
            rectsHadesWhite.append(rectHadesWhite12)

            rectHadesWhitex13 = hadesWhiteRect.centerx - step * 2
            rectHadesWhitey13 = hadesWhiteRect.centery - step * 2
            rectHadesWhite13 = pygame.Rect(rectHadesWhitex13 - 30, rectHadesWhitey13 - 30, 60, 60)
            rectsHadesWhite.append(rectHadesWhite13)

            rectHadesWhitex14 = hadesWhiteRect.centerx - step * 3
            rectHadesWhitey14 = hadesWhiteRect.centery - step * 3
            rectHadesWhite14 = pygame.Rect(rectHadesWhitex14 - 30, rectHadesWhitey14 - 30, 60, 60)
            rectsHadesWhite.append(rectHadesWhite14)

            rectHadesWhitex15 = hadesWhiteRect.centerx - step
            rectHadesWhitey15 = hadesWhiteRect.centery
            rectHadesWhite15 = pygame.Rect(rectHadesWhitex15 - 30, rectHadesWhitey15 - 30, 60, 60)
            rectsHadesWhite.append(rectHadesWhite15)

            rectHadesWhitex16 = hadesWhiteRect.centerx - step * 2
            rectHadesWhitey16 = hadesWhiteRect.centery
            rectHadesWhite16 = pygame.Rect(rectHadesWhitex16 - 30, rectHadesWhitey16 - 30, 60, 60)
            rectsHadesWhite.append(rectHadesWhite16)

            rectHadesWhitex17 = hadesWhiteRect.centerx - step * 3
            rectHadesWhitey17 = hadesWhiteRect.centery
            rectHadesWhite17 = pygame.Rect(rectHadesWhitex17 - 30, rectHadesWhitey17 - 30, 60, 60)
            rectsHadesWhite.append(rectHadesWhite17)

            rectHadesWhitex18 = hadesWhiteRect.centerx - step
            rectHadesWhitey18 = hadesWhiteRect.centery + step
            rectHadesWhite18 = pygame.Rect(rectHadesWhitex18 - 30, rectHadesWhitey18 - 30, 60, 60)
            rectsHadesWhite.append(rectHadesWhite18)

            rectHadesWhitex19 = hadesWhiteRect.centerx - step * 2
            rectHadesWhitey19 = hadesWhiteRect.centery + step * 2
            rectHadesWhite19 = pygame.Rect(rectHadesWhitex19 - 30, rectHadesWhitey19 - 30, 60, 60)
            rectsHadesWhite.append(rectHadesWhite19)

            # Persefona bílá
            persephoneWhitexInit = persephoneWhiteRect.centerx
            persephoneWhiteyInit = persephoneWhiteRect.centery

            rectsPersephoneWhite = []

            rectPersephoneWhitex1 = persephoneWhiteRect.centerx + step
            rectPersephoneWhitey1 = persephoneWhiteRect.centery
            rectPersephoneWhite1 = pygame.Rect(rectPersephoneWhitex1 - 30, rectPersephoneWhitey1 - 30, 60, 60)
            rectsPersephoneWhite.append(rectPersephoneWhite1)

            rectPersephoneWhitex2 = persephoneWhiteRect.centerx + step
            rectPersephoneWhitey2 = persephoneWhiteRect.centery - step
            rectPersephoneWhite2 = pygame.Rect(rectPersephoneWhitex2 - 30, rectPersephoneWhitey2 - 30, 60, 60)
            rectsPersephoneWhite.append(rectPersephoneWhite2)

            rectPersephoneWhitex3 = persephoneWhiteRect.centerx
            rectPersephoneWhitey3 = persephoneWhiteRect.centery - step
            rectPersephoneWhite3 = pygame.Rect(rectPersephoneWhitex3 - 30, rectPersephoneWhitey3 - 30, 60, 60)
            rectsPersephoneWhite.append(rectPersephoneWhite3)

            rectPersephoneWhitex4 = persephoneWhiteRect.centerx - step
            rectPersephoneWhitey4 = persephoneWhiteRect.centery - step
            rectPersephoneWhite4 = pygame.Rect(rectPersephoneWhitex4 - 30, rectPersephoneWhitey4 - 30, 60, 60)
            rectsPersephoneWhite.append(rectPersephoneWhite4)

            rectPersephoneWhitex5 = persephoneWhiteRect.centerx - step
            rectPersephoneWhitey5 = persephoneWhiteRect.centery
            rectPersephoneWhite5 = pygame.Rect(rectPersephoneWhitex5 - 30, rectPersephoneWhitey5 - 30, 60, 60)
            rectsPersephoneWhite.append(rectPersephoneWhite5)

            rectPersephoneWhitex6 = persephoneWhiteRect.centerx - step
            rectPersephoneWhitey6 = persephoneWhiteRect.centery + step
            rectPersephoneWhite6 = pygame.Rect(rectPersephoneWhitex6 - 30, rectPersephoneWhitey6 - 30, 60, 60)
            rectsPersephoneWhite.append(rectPersephoneWhite6)

            rectPersephoneWhitex7 = persephoneWhiteRect.centerx
            rectPersephoneWhitey7 = persephoneWhiteRect.centery + step
            rectPersephoneWhite7 = pygame.Rect(rectPersephoneWhitex7 - 30, rectPersephoneWhitey7 - 30, 60, 60)
            rectsPersephoneWhite.append(rectPersephoneWhite7)

            rectPersephoneWhitex8 = persephoneWhiteRect.centerx
            rectPersephoneWhitey8 = persephoneWhiteRect.centery + step
            rectPersephoneWhite8 = pygame.Rect(rectPersephoneWhitex8 - 30, rectPersephoneWhitey8 - 30, 60, 60)
            rectsPersephoneWhite.append(rectPersephoneWhite8)

            rectPersephoneWhitex9 = persephoneWhiteRect.centerx + step
            rectPersephoneWhitey9 = persephoneWhiteRect.centery + step
            rectPersephoneWhite9 = pygame.Rect(rectPersephoneWhitex9 - 30, rectPersephoneWhitey9 - 30, 60, 60)
            rectsPersephoneWhite.append(rectPersephoneWhite9)

            # Kardinál bílý 1
            cardinalWhitexInit1 = cardinalWhiteRect1.centerx
            cardinalWhiteyInit1 = cardinalWhiteRect1.centery

            rectsCardinalWhite_1 = []

            rectCardinalWhitex1_1 = cardinalWhiteRect1.centerx + step
            rectCardinalWhitey1_1 = cardinalWhiteRect1.centery - step
            rectCardinalWhite1_1 = pygame.Rect(rectCardinalWhitex1_1 - 30, rectCardinalWhitey1_1 - 30, 60, 60)
            rectsCardinalWhite_1.append(rectCardinalWhite1_1)

            rectCardinalWhitex2_1 = cardinalWhiteRect1.centerx + step
            rectCardinalWhitey2_1 = cardinalWhiteRect1.centery + step
            rectCardinalWhite2_1 = pygame.Rect(rectCardinalWhitex2_1 - 30, rectCardinalWhitey2_1 - 30, 60, 60)
            rectsCardinalWhite_1.append(rectCardinalWhite2_1)

            rectCardinalWhitex3_1 = cardinalWhiteRect1.centerx - step
            rectCardinalWhitey3_1 = cardinalWhiteRect1.centery - step
            rectCardinalWhite3_1 = pygame.Rect(rectCardinalWhitex3_1 - 30, rectCardinalWhitey3_1 - 30, 60, 60)
            rectsCardinalWhite_1.append(rectCardinalWhite3_1)

            rectCardinalWhitex4_1 = cardinalWhiteRect1.centerx - step
            rectCardinalWhitey4_1 = cardinalWhiteRect1.centery + step
            rectCardinalWhite4_1 = pygame.Rect(rectCardinalWhitex4_1 - 30, rectCardinalWhitey3_1 - 30, 60, 60)
            rectsCardinalWhite_1.append(rectCardinalWhite4_1)

            # Arcibiskup bílý 1
            archbishopWhitexInit1 = archbishopWhiteRect1.centerx
            archbishopWhiteyInit1 = archbishopWhiteRect1.centery

            rectsArchbishopWhite_1 = []

            rectArchbishopWhitex1_1 = archbishopWhiteRect1.centerx + step * 2
            rectArchbishopWhitey1_1 = archbishopWhiteRect1.centery
            rectArchbishopWhite1_1 = pygame.Rect(rectArchbishopWhitex1_1 - 30, rectArchbishopWhitey1_1 - 30, 60, 60)
            rectsArchbishopWhite_1.append(rectArchbishopWhite1_1)

            rectArchbishopWhitex2_1 = archbishopWhiteRect1.centerx + step * 2
            rectArchbishopWhitey2_1 = archbishopWhiteRect1.centery - step
            rectArchbishopWhite2_1 = pygame.Rect(rectArchbishopWhitex2_1 - 30, rectArchbishopWhitey2_1 - 30, 60, 60)
            rectsArchbishopWhite_1.append(rectArchbishopWhite2_1)

            rectArchbishopWhitex3_1 = archbishopWhiteRect1.centerx + step * 2
            rectArchbishopWhitey3_1 = archbishopWhiteRect1.centery + step
            rectArchbishopWhite3_1 = pygame.Rect(rectArchbishopWhitex3_1 - 30, rectArchbishopWhitey3_1 - 30, 60, 60)
            rectsArchbishopWhite_1.append(rectArchbishopWhite3_1)

            rectArchbishopWhitex4_1 = archbishopWhiteRect1.centerx
            rectArchbishopWhitey4_1 = archbishopWhiteRect1.centery + step * 2
            rectArchbishopWhite4_1 = pygame.Rect(rectArchbishopWhitex4_1 - 30, rectArchbishopWhitey4_1 - 30, 60, 60)
            rectsArchbishopWhite_1.append(rectArchbishopWhite4_1)

            rectArchbishopWhitex5_1 = archbishopWhiteRect1.centerx + step
            rectArchbishopWhitey5_1 = archbishopWhiteRect1.centery + step * 2
            rectArchbishopWhite5_1 = pygame.Rect(rectArchbishopWhitex5_1 - 30, rectArchbishopWhitey5_1 - 30, 60, 60)
            rectsArchbishopWhite_1.append(rectArchbishopWhite5_1)

            rectArchbishopWhitex6_1 = archbishopWhiteRect1.centerx - step
            rectArchbishopWhitey6_1 = archbishopWhiteRect1.centery + step * 2
            rectArchbishopWhite6_1 = pygame.Rect(rectArchbishopWhitex6_1 - 30, rectArchbishopWhitey6_1 - 30, 60, 60)
            rectsArchbishopWhite_1.append(rectArchbishopWhite6_1)

            rectArchbishopWhitex7_1 = archbishopWhiteRect1.centerx - step * 2
            rectArchbishopWhitey7_1 = archbishopWhiteRect1.centery
            rectArchbishopWhite7_1 = pygame.Rect(rectArchbishopWhitex7_1 - 30, rectArchbishopWhitey7_1 - 30, 60, 60)
            rectsArchbishopWhite_1.append(rectArchbishopWhite7_1)

            rectArchbishopWhitex8_1 = archbishopWhiteRect1.centerx - step * 2
            rectArchbishopWhitey8_1 = archbishopWhiteRect1.centery - step
            rectArchbishopWhite8_1 = pygame.Rect(rectArchbishopWhitex8_1 - 30, rectArchbishopWhitey8_1 - 30, 60, 60)
            rectsArchbishopWhite_1.append(rectArchbishopWhite8_1)

            rectArchbishopWhitex9_1 = archbishopWhiteRect1.centerx - step * 2
            rectArchbishopWhitey9_1 = archbishopWhiteRect1.centery + step
            rectArchbishopWhite9_1 = pygame.Rect(rectArchbishopWhitex9_1 - 30, rectArchbishopWhitey9_1 - 30, 60, 60)
            rectsArchbishopWhite_1.append(rectArchbishopWhite9_1)

            rectArchbishopWhitex10_1 = archbishopWhiteRect1.centerx
            rectArchbishopWhitey10_1 = archbishopWhiteRect1.centery - step * 2
            rectArchbishopWhite10_1 = pygame.Rect(rectArchbishopWhitex10_1 - 30, rectArchbishopWhitey10_1 - 30, 60, 60)
            rectsArchbishopWhite_1.append(rectArchbishopWhite10_1)

            rectArchbishopWhitex11_1 = archbishopWhiteRect1.centerx + step
            rectArchbishopWhitey11_1 = archbishopWhiteRect1.centery - step * 2
            rectArchbishopWhite11_1 = pygame.Rect(rectArchbishopWhitex11_1 - 30, rectArchbishopWhitey11_1 - 30, 60, 60)
            rectsArchbishopWhite_1.append(rectArchbishopWhite11_1)

            rectArchbishopWhitex12_1 = archbishopWhiteRect1.centerx - step
            rectArchbishopWhitey12_1 = archbishopWhiteRect1.centery - step * 2
            rectArchbishopWhite12_1 = pygame.Rect(rectArchbishopWhitex12_1 - 30, rectArchbishopWhitey12_1 - 30, 60, 60)
            rectsArchbishopWhite_1.append(rectArchbishopWhite12_1)

            # Morový doktor bílý 1
            plagueWhitexInit1 = plagueDoctorWhiteRect1.centerx
            plagueWhiteyInit1 = plagueDoctorWhiteRect1.centery

            rectsPlagueDoctorWhite_1 = []

            rectPlagueWhitex1_1 = plagueDoctorWhiteRect1.centerx
            rectPlagueWhitey1_1 = plagueDoctorWhiteRect1.centery + step
            rectPlagueWhite1_1 = pygame.Rect(rectPlagueWhitex1_1 - 30, rectPlagueWhitey1_1 - 30, 60, 60)
            rectsPlagueDoctorWhite_1.append(rectPlagueWhite1_1)

            rectPlagueWhitex2_1 = plagueDoctorWhiteRect1.centerx
            rectPlagueWhitey2_1 = plagueDoctorWhiteRect1.centery + step * 2
            rectPlagueWhite2_1 = pygame.Rect(rectPlagueWhitex2_1 - 30, rectPlagueWhitey2_1 - 30, 60, 60)
            rectsPlagueDoctorWhite_1.append(rectPlagueWhite2_1)

            rectPlagueWhitex3_1 = plagueDoctorWhiteRect1.centerx
            rectPlagueWhitey3_1 = plagueDoctorWhiteRect1.centery + step * 3
            rectPlagueWhite3_1 = pygame.Rect(rectPlagueWhitex3_1 - 30, rectPlagueWhitey3_1 - 30, 60, 60)
            rectsPlagueDoctorWhite_1.append(rectPlagueWhite3_1)

            rectPlagueWhitex4_1 = plagueDoctorWhiteRect1.centerx
            rectPlagueWhitey4_1 = plagueDoctorWhiteRect1.centery + step * 4
            rectPlagueWhite4_1 = pygame.Rect(rectPlagueWhitex4_1 - 30, rectPlagueWhitey4_1 - 30, 60, 60)
            rectsPlagueDoctorWhite_1.append(rectPlagueWhite4_1)

            rectPlagueWhitex5_1 = plagueDoctorWhiteRect1.centerx
            rectPlagueWhitey5_1 = plagueDoctorWhiteRect1.centery + step * 5
            rectPlagueWhite5_1 = pygame.Rect(rectPlagueWhitex5_1 - 30, rectPlagueWhitey5_1 - 30, 60, 60)
            rectsPlagueDoctorWhite_1.append(rectPlagueWhite5_1)

            rectPlagueWhitex6_1 = plagueDoctorWhiteRect1.centerx
            rectPlagueWhitey6_1 = plagueDoctorWhiteRect1.centery + step * 6
            rectPlagueWhite6_1 = pygame.Rect(rectPlagueWhitex6_1 - 30, rectPlagueWhitey6_1 - 30, 60, 60)
            rectsPlagueDoctorWhite_1.append(rectPlagueWhite6_1)

            rectPlagueWhitex7_1 = plagueDoctorWhiteRect1.centerx
            rectPlagueWhitey7_1 = plagueDoctorWhiteRect1.centery + step * 7
            rectPlagueWhite7_1 = pygame.Rect(rectPlagueWhitex7_1 - 30, rectPlagueWhitey7_1 - 30, 60, 60)
            rectsPlagueDoctorWhite_1.append(rectPlagueWhite7_1)

            rectPlagueWhitex8_1 = plagueDoctorWhiteRect1.centerx
            rectPlagueWhitey8_1 = plagueDoctorWhiteRect1.centery - step
            rectPlagueWhite8_1 = pygame.Rect(rectPlagueWhitex8_1 - 30, rectPlagueWhitey8_1 - 30, 60, 60)
            rectsPlagueDoctorWhite_1.append(rectPlagueWhite8_1)

            rectPlagueWhitex9_1 = plagueDoctorWhiteRect1.centerx
            rectPlagueWhitey9_1 = plagueDoctorWhiteRect1.centery - step * 2
            rectPlagueWhite9_1 = pygame.Rect(rectPlagueWhitex9_1 - 30, rectPlagueWhitey9_1 - 30, 60, 60)
            rectsPlagueDoctorWhite_1.append(rectPlagueWhite9_1)

            rectPlagueWhitex10_1 = plagueDoctorWhiteRect1.centerx
            rectPlagueWhitey10_1 = plagueDoctorWhiteRect1.centery - step * 3
            rectPlagueWhite10_1 = pygame.Rect(rectPlagueWhitex10_1 - 30, rectPlagueWhitey10_1 - 30, 60, 60)
            rectsPlagueDoctorWhite_1.append(rectPlagueWhite10_1)

            rectPlagueWhitex11_1 = plagueDoctorWhiteRect1.centerx
            rectPlagueWhitey11_1 = plagueDoctorWhiteRect1.centery - step * 4
            rectPlagueWhite11_1 = pygame.Rect(rectPlagueWhitex11_1 - 30, rectPlagueWhitey11_1 - 30, 60, 60)
            rectsPlagueDoctorWhite_1.append(rectPlagueWhite11_1)

            rectPlagueWhitex12_1 = plagueDoctorWhiteRect1.centerx
            rectPlagueWhitey12_1 = plagueDoctorWhiteRect1.centery - step * 5
            rectPlagueWhite12_1 = pygame.Rect(rectPlagueWhitex12_1 - 30, rectPlagueWhitey12_1 - 30, 60, 60)
            rectsPlagueDoctorWhite_1.append(rectPlagueWhite12_1)

            rectPlagueWhitex13_1 = plagueDoctorWhiteRect1.centerx
            rectPlagueWhitey13_1 = plagueDoctorWhiteRect1.centery - step * 6
            rectPlagueWhite13_1 = pygame.Rect(rectPlagueWhitex13_1 - 30, rectPlagueWhitey13_1 - 30, 60, 60)
            rectsPlagueDoctorWhite_1.append(rectPlagueWhite13_1)

            rectPlagueWhitex14_1 = plagueDoctorWhiteRect1.centerx
            rectPlagueWhitey14_1 = plagueDoctorWhiteRect1.centery - step * 7
            rectPlagueWhite14_1 = pygame.Rect(rectPlagueWhitex14_1 - 30, rectPlagueWhitey14_1 - 30, 60, 60)
            rectsPlagueDoctorWhite_1.append(rectPlagueWhite14_1)

            rectPlagueWhitex15_1 = plagueDoctorWhiteRect1.centerx + step
            rectPlagueWhitey15_1 = plagueDoctorWhiteRect1.centery
            rectPlagueWhite15_1 = pygame.Rect(rectPlagueWhitex15_1 - 30, rectPlagueWhitey15_1 - 30, 60, 60)
            rectsPlagueDoctorWhite_1.append(rectPlagueWhite15_1)

            rectPlagueWhitex16_1 = plagueDoctorWhiteRect1.centerx + step * 2
            rectPlagueWhitey16_1 = plagueDoctorWhiteRect1.centery
            rectPlagueWhite16_1 = pygame.Rect(rectPlagueWhitex16_1 - 30, rectPlagueWhitey16_1 - 30, 60, 60)
            rectsPlagueDoctorWhite_1.append(rectPlagueWhite16_1)

            rectPlagueWhitex17_1 = plagueDoctorWhiteRect1.centerx - step
            rectPlagueWhitey17_1 = plagueDoctorWhiteRect1.centery
            rectPlagueWhite17_1 = pygame.Rect(rectPlagueWhitex17_1 - 30, rectPlagueWhitey17_1 - 30, 60, 60)
            rectsPlagueDoctorWhite_1.append(rectPlagueWhite17_1)

            rectPlagueWhitex18_1 = plagueDoctorWhiteRect1.centerx - step * 2
            rectPlagueWhitey18_1 = plagueDoctorWhiteRect1.centery
            rectPlagueWhite18_1 = pygame.Rect(rectPlagueWhitex18_1 - 30, rectPlagueWhitey18_1 - 30, 60, 60)
            rectsPlagueDoctorWhite_1.append(rectPlagueWhite18_1)

            # Válečník bílý 1
            warriorWhitexInit = warriorWhiteRect.centerx
            warriorWhiteyInit = warriorWhiteRect.centery

            rectsWarriorWhite = []

            rectWarriorWhitex1 = warriorWhiteRect.centerx + step
            rectWarriorWhitey1 = warriorWhiteRect.centery
            rectWarriorWhite1 = pygame.Rect(rectWarriorWhitex1 - 30, rectWarriorWhitey1 - 30, 60, 60)
            rectsWarriorWhite.append(rectWarriorWhite1)

            rectWarriorWhitex2 = warriorWhiteRect.centerx - step
            rectWarriorWhitey2 = warriorWhiteRect.centery
            rectWarriorWhite2 = pygame.Rect(rectWarriorWhitex2 - 30, rectWarriorWhitey2 - 30, 60, 60)
            rectsWarriorWhite.append(rectWarriorWhite2)

            rectWarriorWhitex3 = warriorWhiteRect.centerx
            rectWarriorWhitey3 = warriorWhiteRect.centery + step
            rectWarriorWhite3 = pygame.Rect(rectWarriorWhitex3 - 30, rectWarriorWhitey3 - 30, 60, 60)
            rectsWarriorWhite.append(rectWarriorWhite3)

            rectWarriorWhitex4 = warriorWhiteRect.centerx
            rectWarriorWhitey4 = warriorWhiteRect.centery - step
            rectWarriorWhite4 = pygame.Rect(rectWarriorWhitex4 - 30, rectWarriorWhitey4 - 30, 60, 60)
            rectsWarriorWhite.append(rectWarriorWhite4)

            # Válečník bílý 1 abilita
            rectsWarriorWhiteAbility = []

            rectWarriorWhitex1Ability = warriorWhiteRect.centerx + step * 2
            rectWarriorWhitey1Ability = warriorWhiteRect.centery
            rectWarriorWhite1Ability = pygame.Rect(rectWarriorWhitex1Ability - 30, rectWarriorWhitey1Ability - 30, 60,
                                                   60)
            rectsWarriorWhiteAbility.append(rectWarriorWhite1Ability)

            rectWarriorWhitex2Ability = warriorWhiteRect.centerx - step * 2
            rectWarriorWhitey2Ability = warriorWhiteRect.centery
            rectWarriorWhite2Ability = pygame.Rect(rectWarriorWhitex2Ability - 30, rectWarriorWhitey2Ability - 30, 60,
                                                   60)
            rectsWarriorWhiteAbility.append(rectWarriorWhite2Ability)

            rectWarriorWhitex3Ability = warriorWhiteRect.centerx
            rectWarriorWhitey3Ability = warriorWhiteRect.centery - step * 2
            rectWarriorWhite3Ability = pygame.Rect(rectWarriorWhitex3Ability - 30, rectWarriorWhitey3Ability - 30, 60,
                                                   60)
            rectsWarriorWhiteAbility.append(rectWarriorWhite3Ability)

            rectWarriorWhitex4Ability = warriorWhiteRect.centerx
            rectWarriorWhitey4Ability = warriorWhiteRect.centery + step * 2
            rectWarriorWhite4Ability = pygame.Rect(rectWarriorWhitex4Ability - 30, rectWarriorWhitey4Ability - 30, 60,
                                                   60)
            rectsWarriorWhiteAbility.append(rectWarriorWhite4Ability)

            # Legionář bílý 1
            legionaryWhitexInit = legionaryWhiteRect.centerx
            legionaryWhiteyInit = legionaryWhiteRect.centery

            rectsLegionaryWhite = []

            rectLegionaryWhitex1 = legionaryWhiteRect.centerx + step
            rectLegionaryWhitey1 = legionaryWhiteRect.centery + step
            rectLegionaryWhite1 = pygame.Rect(rectLegionaryWhitex1 - 30, rectLegionaryWhitey1 - 30, 60, 60)
            rectsLegionaryWhite.append(rectLegionaryWhite1)

            rectLegionaryWhitex2 = legionaryWhiteRect.centerx
            rectLegionaryWhitey2 = legionaryWhiteRect.centery + step
            rectLegionaryWhite2 = pygame.Rect(rectLegionaryWhitex2 - 30, rectLegionaryWhitey2 - 30, 60, 60)
            rectsLegionaryWhite.append(rectLegionaryWhite2)

            rectLegionaryWhitex3 = legionaryWhiteRect.centerx - step
            rectLegionaryWhitey3 = legionaryWhiteRect.centery + step
            rectLegionaryWhite3 = pygame.Rect(rectLegionaryWhitex3 - 30, rectLegionaryWhitey3 - 30, 60, 60)
            rectsLegionaryWhite.append(rectLegionaryWhite3)

            # Válečník bílý 2
            warriorWhitexInit1 = warriorWhiteRect1.centerx
            warriorWhiteyInit1 = warriorWhiteRect1.centery

            rectsWarriorWhite_1 = []

            rectWarriorWhitex1_1 = warriorWhiteRect1.centerx + step
            rectWarriorWhitey1_1 = warriorWhiteRect1.centery
            rectWarriorWhite1_1 = pygame.Rect(rectWarriorWhitex1_1 - 30, rectWarriorWhitey1_1 - 30, 60, 60)
            rectsWarriorWhite_1.append(rectWarriorWhite1_1)

            rectWarriorWhitex2_1 = warriorWhiteRect1.centerx - step
            rectWarriorWhitey2_1 = warriorWhiteRect1.centery
            rectWarriorWhite2_1 = pygame.Rect(rectWarriorWhitex2_1 - 30, rectWarriorWhitey2_1 - 30, 60, 60)
            rectsWarriorWhite_1.append(rectWarriorWhite2_1)

            rectWarriorWhitex3_1 = warriorWhiteRect1.centerx
            rectWarriorWhitey3_1 = warriorWhiteRect1.centery + step
            rectWarriorWhite3_1 = pygame.Rect(rectWarriorWhitex3_1 - 30, rectWarriorWhitey3_1 - 30, 60, 60)
            rectsWarriorWhite_1.append(rectWarriorWhite3_1)

            rectWarriorWhitex4_1 = warriorWhiteRect1.centerx
            rectWarriorWhitey4_1 = warriorWhiteRect1.centery - step
            rectWarriorWhite4_1 = pygame.Rect(rectWarriorWhitex4_1 - 30, rectWarriorWhitey4_1 - 30, 60, 60)
            rectsWarriorWhite_1.append(rectWarriorWhite4_1)

            # Válečník bílý 2 abilita
            rectsWarriorWhiteAbility_1 = []

            rectWarriorWhitex1_1Ability = warriorWhiteRect1.centerx + step * 2
            rectWarriorWhitey1_1Ability = warriorWhiteRect1.centery
            rectWarriorWhite1_1Ability = pygame.Rect(rectWarriorWhitex1_1Ability - 30, rectWarriorWhitey1_1Ability - 30,
                                                     60, 60)
            rectsWarriorWhiteAbility_1.append(rectWarriorWhite1_1Ability)

            rectWarriorWhitex2_1Ability = warriorWhiteRect1.centerx - step * 2
            rectWarriorWhitey2_1Ability = warriorWhiteRect1.centery
            rectWarriorWhite2_1Ability = pygame.Rect(rectWarriorWhitex2_1Ability - 30, rectWarriorWhitey2_1Ability - 30,
                                                     60, 60)
            rectsWarriorWhiteAbility_1.append(rectWarriorWhite2_1Ability)

            rectWarriorWhitex3_1Ability = warriorWhiteRect1.centerx
            rectWarriorWhitey3_1Ability = warriorWhiteRect1.centery - step * 2
            rectWarriorWhite3_1Ability = pygame.Rect(rectWarriorWhitex3_1Ability - 30, rectWarriorWhitey3_1Ability - 30,
                                                     60, 60)
            rectsWarriorWhiteAbility_1.append(rectWarriorWhite3_1Ability)

            rectWarriorWhitex4_1Ability = warriorWhiteRect1.centerx
            rectWarriorWhitey4_1Ability = warriorWhiteRect1.centery + step * 2
            rectWarriorWhite4_1Ability = pygame.Rect(rectWarriorWhitex4_1Ability - 30, rectWarriorWhitey4_1Ability - 30,
                                                     60, 60)
            rectsWarriorWhiteAbility_1.append(rectWarriorWhite4_1Ability)

            # Legionář bílý 2
            legionaryWhitexInit1 = legionaryWhiteRect1.centerx
            legionaryWhiteyInit1 = legionaryWhiteRect1.centery

            rectsLegionaryWhite_1 = []

            rectLegionaryWhitex1_1 = legionaryWhiteRect1.centerx + step
            rectLegionaryWhitey1_1 = legionaryWhiteRect1.centery + step
            rectLegionaryWhite1_1 = pygame.Rect(rectLegionaryWhitex1_1 - 30, rectLegionaryWhitey1_1 - 30, 60, 60)
            rectsLegionaryWhite_1.append(rectLegionaryWhite1_1)

            rectLegionaryWhitex2_1 = legionaryWhiteRect1.centerx
            rectLegionaryWhitey2_1 = legionaryWhiteRect1.centery + step
            rectLegionaryWhite2_1 = pygame.Rect(rectLegionaryWhitex2_1 - 30, rectLegionaryWhitey2_1 - 30, 60, 60)
            rectsLegionaryWhite_1.append(rectLegionaryWhite2_1)

            rectLegionaryWhitex3_1 = legionaryWhiteRect1.centerx - step
            rectLegionaryWhitey3_1 = legionaryWhiteRect1.centery + step
            rectLegionaryWhite3_1 = pygame.Rect(rectLegionaryWhitex3_1 - 30, rectLegionaryWhitey3_1 - 30, 60, 60)
            rectsLegionaryWhite_1.append(rectLegionaryWhite3_1)

            # Válečník bílý 3
            warriorWhitexInit2 = warriorWhiteRect2.centerx
            warriorWhiteyInit2 = warriorWhiteRect2.centery

            rectsWarriorWhite_2 = []

            rectWarriorWhitex1_2 = warriorWhiteRect2.centerx + step
            rectWarriorWhitey1_2 = warriorWhiteRect2.centery
            rectWarriorWhite1_2 = pygame.Rect(rectWarriorWhitex1_2 - 30, rectWarriorWhitey1_2 - 30, 60, 60)
            rectsWarriorWhite_2.append(rectWarriorWhite1_2)

            rectWarriorWhitex2_2 = warriorWhiteRect2.centerx - step
            rectWarriorWhitey2_2 = warriorWhiteRect2.centery
            rectWarriorWhite2_2 = pygame.Rect(rectWarriorWhitex2_2 - 30, rectWarriorWhitey2_2 - 30, 60, 60)
            rectsWarriorWhite_2.append(rectWarriorWhite2_2)

            rectWarriorWhitex3_2 = warriorWhiteRect2.centerx
            rectWarriorWhitey3_2 = warriorWhiteRect2.centery + step
            rectWarriorWhite3_2 = pygame.Rect(rectWarriorWhitex3_2 - 30, rectWarriorWhitey3_2 - 30, 60, 60)
            rectsWarriorWhite_2.append(rectWarriorWhite3_2)

            rectWarriorWhitex4_2 = warriorWhiteRect2.centerx
            rectWarriorWhitey4_2 = warriorWhiteRect2.centery - step
            rectWarriorWhite4_2 = pygame.Rect(rectWarriorWhitex4_2 - 30, rectWarriorWhitey4_2 - 30, 60, 60)
            rectsWarriorWhite_2.append(rectWarriorWhite4_2)

            # Válečník bílý 3 abilita
            rectsWarriorWhiteAbility_2 = []

            rectWarriorWhitex1_2Ability = warriorWhiteRect2.centerx + step * 2
            rectWarriorWhitey1_2Ability = warriorWhiteRect2.centery
            rectWarriorWhite1_2Ability = pygame.Rect(rectWarriorWhitex1_2Ability - 30, rectWarriorWhitey1_2Ability - 30,
                                                     60, 60)
            rectsWarriorWhiteAbility_2.append(rectWarriorWhite1_2Ability)

            rectWarriorWhitex2_2Ability = warriorWhiteRect2.centerx - step * 2
            rectWarriorWhitey2_2Ability = warriorWhiteRect2.centery
            rectWarriorWhite2_2Ability = pygame.Rect(rectWarriorWhitex2_2Ability - 30, rectWarriorWhitey2_2Ability - 30,
                                                     60, 60)
            rectsWarriorWhiteAbility_2.append(rectWarriorWhite2_2Ability)

            rectWarriorWhitex3_2Ability = warriorWhiteRect2.centerx
            rectWarriorWhitey3_2Ability = warriorWhiteRect2.centery - step * 2
            rectWarriorWhite3_2Ability = pygame.Rect(rectWarriorWhitex3_2Ability - 30, rectWarriorWhitey3_2Ability - 30,
                                                     60, 60)
            rectsWarriorWhiteAbility_2.append(rectWarriorWhite3_2Ability)

            rectWarriorWhitex4_2Ability = warriorWhiteRect2.centerx
            rectWarriorWhitey4_2Ability = warriorWhiteRect2.centery + step * 2
            rectWarriorWhite4_2Ability = pygame.Rect(rectWarriorWhitex4_2Ability - 30, rectWarriorWhitey4_2Ability - 30,
                                                     60, 60)
            rectsWarriorWhiteAbility_2.append(rectWarriorWhite4_2Ability)

            # Legionář bílý 3
            legionaryWhitexInit2 = legionaryWhiteRect2.centerx
            legionaryWhiteyInit2 = legionaryWhiteRect2.centery

            rectsLegionaryWhite_2 = []

            rectLegionaryWhitex1_2 = legionaryWhiteRect2.centerx + step
            rectLegionaryWhitey1_2 = legionaryWhiteRect2.centery + step
            rectLegionaryWhite1_2 = pygame.Rect(rectLegionaryWhitex1_2 - 30, rectLegionaryWhitey1_2 - 30, 60, 60)
            rectsLegionaryWhite_2.append(rectLegionaryWhite1_2)

            rectLegionaryWhitex2_2 = legionaryWhiteRect2.centerx
            rectLegionaryWhitey2_2 = legionaryWhiteRect2.centery + step
            rectLegionaryWhite2_2 = pygame.Rect(rectLegionaryWhitex2_2 - 30, rectLegionaryWhitey2_2 - 30, 60, 60)
            rectsLegionaryWhite_2.append(rectLegionaryWhite2_2)

            rectLegionaryWhitex3_2 = legionaryWhiteRect2.centerx - step
            rectLegionaryWhitey3_2 = legionaryWhiteRect2.centery + step
            rectLegionaryWhite3_2 = pygame.Rect(rectLegionaryWhitex3_2 - 30, rectLegionaryWhitey3_2 - 30, 60, 60)
            rectsLegionaryWhite_2.append(rectLegionaryWhite3_2)

            # Válečník bílý 4
            warriorWhitexInit3 = warriorWhiteRect3.centerx
            warriorWhiteyInit3 = warriorWhiteRect3.centery

            rectsWarriorWhite_3 = []

            rectWarriorWhitex1_3 = warriorWhiteRect3.centerx + step
            rectWarriorWhitey1_3 = warriorWhiteRect3.centery
            rectWarriorWhite1_3 = pygame.Rect(rectWarriorWhitex1_3 - 30, rectWarriorWhitey1_3 - 30, 60, 60)
            rectsWarriorWhite_3.append(rectWarriorWhite1_3)

            rectWarriorWhitex2_3 = warriorWhiteRect3.centerx - step
            rectWarriorWhitey2_3 = warriorWhiteRect3.centery
            rectWarriorWhite2_3 = pygame.Rect(rectWarriorWhitex2_3 - 30, rectWarriorWhitey2_3 - 30, 60, 60)
            rectsWarriorWhite_3.append(rectWarriorWhite2_3)

            rectWarriorWhitex3_3 = warriorWhiteRect3.centerx
            rectWarriorWhitey3_3 = warriorWhiteRect3.centery + step
            rectWarriorWhite3_3 = pygame.Rect(rectWarriorWhitex3_3 - 30, rectWarriorWhitey3_3 - 30, 60, 60)
            rectsWarriorWhite_3.append(rectWarriorWhite3_3)

            rectWarriorWhitex4_3 = warriorWhiteRect3.centerx
            rectWarriorWhitey4_3 = warriorWhiteRect3.centery - step
            rectWarriorWhite4_3 = pygame.Rect(rectWarriorWhitex4_3 - 30, rectWarriorWhitey4_3 - 30, 60, 60)
            rectsWarriorWhite_3.append(rectWarriorWhite4_3)

            # Válečník bílý 4 abilita
            rectsWarriorWhiteAbility_3 = []

            rectWarriorWhitex1_3Ability = warriorWhiteRect3.centerx + step * 2
            rectWarriorWhitey1_3Ability = warriorWhiteRect3.centery
            rectWarriorWhite1_3Ability = pygame.Rect(rectWarriorWhitex1_3Ability - 30, rectWarriorWhitey1_3Ability - 30,
                                                     60, 60)
            rectsWarriorWhiteAbility_3.append(rectWarriorWhite1_3Ability)

            rectWarriorWhitex2_3Ability = warriorWhiteRect3.centerx - step * 2
            rectWarriorWhitey2_3Ability = warriorWhiteRect3.centery
            rectWarriorWhite2_3Ability = pygame.Rect(rectWarriorWhitex2_3Ability - 30, rectWarriorWhitey2_3Ability - 30,
                                                     60, 60)
            rectsWarriorWhiteAbility_3.append(rectWarriorWhite2_3Ability)

            rectWarriorWhitex3_3Ability = warriorWhiteRect3.centerx
            rectWarriorWhitey3_3Ability = warriorWhiteRect3.centery - step * 2
            rectWarriorWhite3_3Ability = pygame.Rect(rectWarriorWhitex3_3Ability - 30, rectWarriorWhitey3_3Ability - 30,
                                                     60, 60)
            rectsWarriorWhiteAbility_3.append(rectWarriorWhite3_3Ability)

            rectWarriorWhitex4_3Ability = warriorWhiteRect3.centerx
            rectWarriorWhitey4_3Ability = warriorWhiteRect3.centery + step * 2
            rectWarriorWhite4_3Ability = pygame.Rect(rectWarriorWhitex4_3Ability - 30, rectWarriorWhitey4_3Ability - 30,
                                                     60, 60)
            rectsWarriorWhiteAbility_3.append(rectWarriorWhite4_3Ability)

            # Legionář bílý 4
            legionaryWhitexInit3 = legionaryWhiteRect3.centerx
            legionaryWhiteyInit3 = legionaryWhiteRect3.centery

            rectsLegionaryWhite_3 = []

            rectLegionaryWhitex1_3 = legionaryWhiteRect3.centerx + step
            rectLegionaryWhitey1_3 = legionaryWhiteRect3.centery + step
            rectLegionaryWhite1_3 = pygame.Rect(rectLegionaryWhitex1_3 - 30, rectLegionaryWhitey1_3 - 30, 60, 60)
            rectsLegionaryWhite_3.append(rectLegionaryWhite1_3)

            rectLegionaryWhitex2_3 = legionaryWhiteRect3.centerx
            rectLegionaryWhitey2_3 = legionaryWhiteRect3.centery + step
            rectLegionaryWhite2_3 = pygame.Rect(rectLegionaryWhitex2_3 - 30, rectLegionaryWhitey2_3 - 30, 60, 60)
            rectsLegionaryWhite_3.append(rectLegionaryWhite2_3)

            rectLegionaryWhitex3_3 = legionaryWhiteRect3.centerx - step
            rectLegionaryWhitey3_3 = legionaryWhiteRect3.centery + step
            rectLegionaryWhite3_3 = pygame.Rect(rectLegionaryWhitex3_3 - 30, rectLegionaryWhitey3_3 - 30, 60, 60)
            rectsLegionaryWhite_3.append(rectLegionaryWhite3_3)

            # Morový doktor černý 1
            plagueBlackxInit = plagueDoctorBlackRect.centerx
            plagueBlackyInit = plagueDoctorBlackRect.centery

            rectsPlagueDoctorBlack = []

            rectPlagueBlackx1 = plagueDoctorBlackRect.centerx + step
            rectPlagueBlacky1 = plagueDoctorBlackRect.centery
            rectPlagueBlack1 = pygame.Rect(rectPlagueBlackx1 - 30, rectPlagueBlacky1 - 30, 60, 60)
            rectsPlagueDoctorBlack.append(rectPlagueBlack1)

            rectPlagueBlackx2 = plagueDoctorBlackRect.centerx + step * 2
            rectPlagueBlacky2 = plagueDoctorBlackRect.centery
            rectPlagueBlack2 = pygame.Rect(rectPlagueBlackx2 - 30, rectPlagueBlacky2 - 30, 60, 60)
            rectsPlagueDoctorBlack.append(rectPlagueBlack2)

            rectPlagueBlackx3 = plagueDoctorBlackRect.centerx - step
            rectPlagueBlacky3 = plagueDoctorBlackRect.centery
            rectPlagueBlack3 = pygame.Rect(rectPlagueBlackx3 - 30, rectPlagueBlacky3 - 30, 60, 60)
            rectsPlagueDoctorBlack.append(rectPlagueBlack3)

            rectPlagueBlackx4 = plagueDoctorBlackRect.centerx - step * 2
            rectPlagueBlacky4 = plagueDoctorBlackRect.centery
            rectPlagueBlack4 = pygame.Rect(rectPlagueBlackx4 - 30, rectPlagueBlacky4 - 30, 60, 60)
            rectsPlagueDoctorBlack.append(rectPlagueBlack4)

            rectPlagueBlackx5 = plagueDoctorBlackRect.centerx
            rectPlagueBlacky5 = plagueDoctorBlackRect.centery + step
            rectPlagueBlack5 = pygame.Rect(rectPlagueBlackx5 - 30, rectPlagueBlacky5 - 30, 60, 60)
            rectsPlagueDoctorBlack.append(rectPlagueBlack5)

            rectPlagueBlackx6 = plagueDoctorBlackRect.centerx
            rectPlagueBlacky6 = plagueDoctorBlackRect.centery + step * 2
            rectPlagueBlack6 = pygame.Rect(rectPlagueBlackx6 - 30, rectPlagueBlacky6 - 30, 60, 60)
            rectsPlagueDoctorBlack.append(rectPlagueBlack6)

            rectPlagueBlackx7 = plagueDoctorBlackRect.centerx
            rectPlagueBlacky7 = plagueDoctorBlackRect.centery + step * 3
            rectPlagueBlack7 = pygame.Rect(rectPlagueBlackx7 - 30, rectPlagueBlacky7 - 30, 60, 60)
            rectsPlagueDoctorBlack.append(rectPlagueBlack7)

            rectPlagueBlackx8 = plagueDoctorBlackRect.centerx
            rectPlagueBlacky8 = plagueDoctorBlackRect.centery + step * 4
            rectPlagueBlack8 = pygame.Rect(rectPlagueBlackx8 - 30, rectPlagueBlacky8 - 30, 60, 60)
            rectsPlagueDoctorBlack.append(rectPlagueBlack8)

            rectPlagueBlackx9 = plagueDoctorBlackRect.centerx
            rectPlagueBlacky9 = plagueDoctorBlackRect.centery + step * 5
            rectPlagueBlack9 = pygame.Rect(rectPlagueBlackx9 - 30, rectPlagueBlacky9 - 30, 60, 60)
            rectsPlagueDoctorBlack.append(rectPlagueBlack9)

            rectPlagueBlackx10 = plagueDoctorBlackRect.centerx
            rectPlagueBlacky10 = plagueDoctorBlackRect.centery + step * 6
            rectPlagueBlack10 = pygame.Rect(rectPlagueBlackx10 - 30, rectPlagueBlacky10 - 30, 60, 60)
            rectsPlagueDoctorBlack.append(rectPlagueBlack10)

            rectPlagueBlackx11 = plagueDoctorBlackRect.centerx
            rectPlagueBlacky11 = plagueDoctorBlackRect.centery + step * 7
            rectPlagueBlack11 = pygame.Rect(rectPlagueBlackx11 - 30, rectPlagueBlacky11 - 30, 60, 60)
            rectsPlagueDoctorBlack.append(rectPlagueBlack11)

            rectPlagueBlackx12 = plagueDoctorBlackRect.centerx
            rectPlagueBlacky12 = plagueDoctorBlackRect.centery - step
            rectPlagueBlack12 = pygame.Rect(rectPlagueBlackx12 - 30, rectPlagueBlacky12 - 30, 60, 60)
            rectsPlagueDoctorBlack.append(rectPlagueBlack12)

            rectPlagueBlackx13 = plagueDoctorBlackRect.centerx
            rectPlagueBlacky13 = plagueDoctorBlackRect.centery - step * 2
            rectPlagueBlack13 = pygame.Rect(rectPlagueBlackx13 - 30, rectPlagueBlacky13 - 30, 60, 60)
            rectsPlagueDoctorBlack.append(rectPlagueBlack13)

            rectPlagueBlackx14 = plagueDoctorBlackRect.centerx
            rectPlagueBlacky14 = plagueDoctorBlackRect.centery - step * 3
            rectPlagueBlack14 = pygame.Rect(rectPlagueBlackx14 - 30, rectPlagueBlacky14 - 30, 60, 60)
            rectsPlagueDoctorBlack.append(rectPlagueBlack14)

            rectPlagueBlackx15 = plagueDoctorBlackRect.centerx
            rectPlagueBlacky15 = plagueDoctorBlackRect.centery - step * 4
            rectPlagueBlack15 = pygame.Rect(rectPlagueBlackx15 - 30, rectPlagueBlacky15 - 30, 60, 60)
            rectsPlagueDoctorBlack.append(rectPlagueBlack15)

            rectPlagueBlackx16 = plagueDoctorBlackRect.centerx
            rectPlagueBlacky16 = plagueDoctorBlackRect.centery - step * 5
            rectPlagueBlack16 = pygame.Rect(rectPlagueBlackx16 - 30, rectPlagueBlacky16 - 30, 60, 60)
            rectsPlagueDoctorBlack.append(rectPlagueBlack16)

            rectPlagueBlackx17 = plagueDoctorBlackRect.centerx
            rectPlagueBlacky17 = plagueDoctorBlackRect.centery - step * 6
            rectPlagueBlack17 = pygame.Rect(rectPlagueBlackx17 - 30, rectPlagueBlacky17 - 30, 60, 60)
            rectsPlagueDoctorBlack.append(rectPlagueBlack17)

            rectPlagueBlackx18 = plagueDoctorBlackRect.centerx
            rectPlagueBlacky18 = plagueDoctorBlackRect.centery - step * 7
            rectPlagueBlack18 = pygame.Rect(rectPlagueBlackx18 - 30, rectPlagueBlacky18 - 30, 60, 60)
            rectsPlagueDoctorBlack.append(rectPlagueBlack18)

            # Arcibiskup černý 1
            archbishopBlackxInit = archbishopBlackRect.centerx
            archbishopBlackyInit = archbishopBlackRect.centery

            rectsArchbishopBlack = []

            rectArchbishopBlackx1 = archbishopBlackRect.centerx + step * 2
            rectArchbishopBlacky1 = archbishopBlackRect.centery
            rectArchbishopBlack1 = pygame.Rect(rectArchbishopBlackx1 - 30, rectArchbishopBlacky1 - 30, 60, 60)
            rectsArchbishopBlack.append(rectArchbishopBlack1)

            rectArchbishopBlackx2 = archbishopBlackRect.centerx + step * 2
            rectArchbishopBlacky2 = archbishopBlackRect.centery + step
            rectArchbishopBlack2 = pygame.Rect(rectArchbishopBlackx2 - 30, rectArchbishopBlacky2 - 30, 60, 60)
            rectsArchbishopBlack.append(rectArchbishopBlack2)

            rectArchbishopBlackx3 = archbishopBlackRect.centerx + step * 2
            rectArchbishopBlacky3 = archbishopBlackRect.centery - step
            rectArchbishopBlack3 = pygame.Rect(rectArchbishopBlackx3 - 30, rectArchbishopBlacky3 - 30, 60, 60)
            rectsArchbishopBlack.append(rectArchbishopBlack3)

            rectArchbishopBlackx4 = archbishopBlackRect.centerx
            rectArchbishopBlacky4 = archbishopBlackRect.centery + step * 2
            rectArchbishopBlack4 = pygame.Rect(rectArchbishopBlackx4 - 30, rectArchbishopBlacky4 - 30, 60, 60)
            rectsArchbishopBlack.append(rectArchbishopBlack4)

            rectArchbishopBlackx5 = archbishopBlackRect.centerx + step
            rectArchbishopBlacky5 = archbishopBlackRect.centery + step * 2
            rectArchbishopBlack5 = pygame.Rect(rectArchbishopBlackx5 - 30, rectArchbishopBlacky5 - 30, 60, 60)
            rectsArchbishopBlack.append(rectArchbishopBlack5)

            rectArchbishopBlackx6 = archbishopBlackRect.centerx - step
            rectArchbishopBlacky6 = archbishopBlackRect.centery + step * 2
            rectArchbishopBlack6 = pygame.Rect(rectArchbishopBlackx6 - 30, rectArchbishopBlacky6 - 30, 60, 60)
            rectsArchbishopBlack.append(rectArchbishopBlack6)

            rectArchbishopBlackx7 = archbishopBlackRect.centerx - step * 2
            rectArchbishopBlacky7 = archbishopBlackRect.centery
            rectArchbishopBlack7 = pygame.Rect(rectArchbishopBlackx7 - 30, rectArchbishopBlacky7 - 30, 60, 60)
            rectsArchbishopBlack.append(rectArchbishopBlack7)

            rectArchbishopBlackx8 = archbishopBlackRect.centerx - step * 2
            rectArchbishopBlacky8 = archbishopBlackRect.centery + step
            rectArchbishopBlack8 = pygame.Rect(rectArchbishopBlackx8 - 30, rectArchbishopBlacky8 - 30, 60, 60)
            rectsArchbishopBlack.append(rectArchbishopBlack8)

            rectArchbishopBlackx9 = archbishopBlackRect.centerx - step * 2
            rectArchbishopBlacky9 = archbishopBlackRect.centery - step
            rectArchbishopBlack9 = pygame.Rect(rectArchbishopBlackx9 - 30, rectArchbishopBlacky9 - 30, 60, 60)
            rectsArchbishopBlack.append(rectArchbishopBlack9)

            rectArchbishopBlackx10 = archbishopBlackRect.centerx
            rectArchbishopBlacky10 = archbishopBlackRect.centery - step * 2
            rectArchbishopBlack10 = pygame.Rect(rectArchbishopBlackx10 - 30, rectArchbishopBlacky10 - 30, 60, 60)
            rectsArchbishopBlack.append(rectArchbishopBlack10)

            rectArchbishopBlackx11 = archbishopBlackRect.centerx + step
            rectArchbishopBlacky11 = archbishopBlackRect.centery - step * 2
            rectArchbishopBlack11 = pygame.Rect(rectArchbishopBlackx11 - 30, rectArchbishopBlacky11 - 30, 60, 60)
            rectsArchbishopBlack.append(rectArchbishopBlack11)

            rectArchbishopBlackx12 = archbishopBlackRect.centerx - step
            rectArchbishopBlacky12 = archbishopBlackRect.centery - step * 2
            rectArchbishopBlack12 = pygame.Rect(rectArchbishopBlackx12 - 30, rectArchbishopBlacky12 - 30, 60, 60)
            rectsArchbishopBlack.append(rectArchbishopBlack12)

            # Kardinál černý 1
            cardinalBlackxInit = cardinalBlackRect.centerx
            cardinalBlackyInit = cardinalBlackRect.centery

            rectsCardinalBlack = []

            rectCardinalBlackx1 = cardinalBlackRect.centerx + step
            rectCardinalBlacky1 = cardinalBlackRect.centery - step
            rectCardinalBlack1 = pygame.Rect(rectCardinalBlackx1 - 30, rectCardinalBlacky1 - 30, 60, 60)
            rectsCardinalBlack.append(rectCardinalBlack1)

            rectCardinalBlackx2 = cardinalBlackRect.centerx - step
            rectCardinalBlacky2 = cardinalBlackRect.centery - step
            rectCardinalBlack2 = pygame.Rect(rectCardinalBlackx2 - 30, rectCardinalBlacky2 - 30, 60, 60)
            rectsCardinalBlack.append(rectCardinalBlack2)

            rectCardinalBlackx3 = cardinalBlackRect.centerx + step
            rectCardinalBlacky3 = cardinalBlackRect.centery + step
            rectCardinalBlack3 = pygame.Rect(rectCardinalBlackx3 - 30, rectCardinalBlacky3 - 30, 60, 60)
            rectsCardinalBlack.append(rectCardinalBlack3)

            rectCardinalBlackx4 = cardinalBlackRect.centerx - step
            rectCardinalBlacky4 = cardinalBlackRect.centery + step
            rectCardinalBlack4 = pygame.Rect(rectCardinalBlackx4 - 30, rectCardinalBlacky4 - 30, 60, 60)
            rectsCardinalBlack.append(rectCardinalBlack4)

            # Hádes černý
            hadesBlackxInit = hadesBlackRect.centerx
            hadesBlackyInit = hadesBlackRect.centery

            rectsHadesBlack = []

            rectHadesBlackx1 = hadesBlackRect.centerx + step
            rectHadesBlacky1 = hadesBlackRect.centery
            rectHadesBlack1 = pygame.Rect(rectHadesBlackx1 - 30, rectHadesBlacky1 - 30, 60, 60)
            rectsHadesBlack.append(rectHadesBlack1)

            rectHadesBlackx2 = hadesBlackRect.centerx + step * 2
            rectHadesBlacky2 = hadesBlackRect.centery
            rectHadesBlack2 = pygame.Rect(rectHadesBlackx2 - 30, rectHadesBlacky2 - 30, 60, 60)
            rectsHadesBlack.append(rectHadesBlack2)

            rectHadesBlackx3 = hadesBlackRect.centerx + step * 3
            rectHadesBlacky3 = hadesBlackRect.centery
            rectHadesBlack3 = pygame.Rect(rectHadesBlackx3 - 30, rectHadesBlacky3 - 30, 60, 60)
            rectsHadesBlack.append(rectHadesBlack3)

            rectHadesBlackx4 = hadesBlackRect.centerx - step
            rectHadesBlacky4 = hadesBlackRect.centery
            rectHadesBlack4 = pygame.Rect(rectHadesBlackx4 - 30, rectHadesBlacky4 - 30, 60, 60)
            rectsHadesBlack.append(rectHadesBlack4)

            rectHadesBlackx5 = hadesBlackRect.centerx - step * 2
            rectHadesBlacky5 = hadesBlackRect.centery
            rectHadesBlack5 = pygame.Rect(rectHadesBlackx5 - 30, rectHadesBlacky5 - 30, 60, 60)
            rectsHadesBlack.append(rectHadesBlack5)

            rectHadesBlackx6 = hadesBlackRect.centerx - step * 3
            rectHadesBlacky6 = hadesBlackRect.centery
            rectHadesBlack6 = pygame.Rect(rectHadesBlackx6 - 30, rectHadesBlacky6 - 30, 60, 60)
            rectsHadesBlack.append(rectHadesBlack6)

            rectHadesBlackx7 = hadesBlackRect.centerx
            rectHadesBlacky7 = hadesBlackRect.centery - step
            rectHadesBlack7 = pygame.Rect(rectHadesBlackx7 - 30, rectHadesBlacky7 - 30, 60, 60)
            rectsHadesBlack.append(rectHadesBlack7)

            rectHadesBlackx8 = hadesBlackRect.centerx
            rectHadesBlacky8 = hadesBlackRect.centery - step * 2
            rectHadesBlack8 = pygame.Rect(rectHadesBlackx8 - 30, rectHadesBlacky8 - 30, 60, 60)
            rectsHadesBlack.append(rectHadesBlack8)

            rectHadesBlackx9 = hadesBlackRect.centerx
            rectHadesBlacky9 = hadesBlackRect.centery - step * 3
            rectHadesBlack9 = pygame.Rect(rectHadesBlackx9 - 30, rectHadesBlacky9 - 30, 60, 60)
            rectsHadesBlack.append(rectHadesBlack9)

            rectHadesBlackx10 = hadesBlackRect.centerx + step
            rectHadesBlacky10 = hadesBlackRect.centery - step
            rectHadesBlack10 = pygame.Rect(rectHadesBlackx10 - 30, rectHadesBlacky10 - 30, 60, 60)
            rectsHadesBlack.append(rectHadesBlack10)

            rectHadesBlackx11 = hadesBlackRect.centerx + step * 2
            rectHadesBlacky11 = hadesBlackRect.centery - step * 2
            rectHadesBlack11 = pygame.Rect(rectHadesBlackx11 - 30, rectHadesBlacky11 - 30, 60, 60)
            rectsHadesBlack.append(rectHadesBlack11)

            rectHadesBlackx12 = hadesBlackRect.centerx + step * 3
            rectHadesBlacky12 = hadesBlackRect.centery - step * 3
            rectHadesBlack12 = pygame.Rect(rectHadesBlackx12 - 30, rectHadesBlacky12 - 30, 60, 60)
            rectsHadesBlack.append(rectHadesBlack12)

            rectHadesBlackx13 = hadesBlackRect.centerx - step
            rectHadesBlacky13 = hadesBlackRect.centery - step
            rectHadesBlack13 = pygame.Rect(rectHadesBlackx13 - 30, rectHadesBlacky13 - 30, 60, 60)
            rectsHadesBlack.append(rectHadesBlack13)

            rectHadesBlackx14 = hadesBlackRect.centerx - step * 2
            rectHadesBlacky14 = hadesBlackRect.centery - step * 2
            rectHadesBlack14 = pygame.Rect(rectHadesBlackx14 - 30, rectHadesBlacky14 - 30, 60, 60)
            rectsHadesBlack.append(rectHadesBlack14)

            rectHadesBlackx15 = hadesBlackRect.centerx - step * 3
            rectHadesBlacky15 = hadesBlackRect.centery - step * 3
            rectHadesBlack15 = pygame.Rect(rectHadesBlackx15 - 30, rectHadesBlacky15 - 30, 60, 60)
            rectsHadesBlack.append(rectHadesBlack15)

            rectHadesBlackx16 = hadesBlackRect.centerx + step
            rectHadesBlacky16 = hadesBlackRect.centery + step
            rectHadesBlack16 = pygame.Rect(rectHadesBlackx16 - 30, rectHadesBlacky16 - 30, 60, 60)
            rectsHadesBlack.append(rectHadesBlack16)

            rectHadesBlackx17 = hadesBlackRect.centerx + step * 2
            rectHadesBlacky17 = hadesBlackRect.centery + step * 2
            rectHadesBlack17 = pygame.Rect(rectHadesBlackx17 - 30, rectHadesBlacky17 - 30, 60, 60)
            rectsHadesBlack.append(rectHadesBlack17)

            rectHadesBlackx18 = hadesBlackRect.centerx - step
            rectHadesBlacky18 = hadesBlackRect.centery + step
            rectHadesBlack18 = pygame.Rect(rectHadesBlackx18 - 30, rectHadesBlacky18 - 30, 60, 60)
            rectsHadesBlack.append(rectHadesBlack18)

            rectHadesBlackx19 = hadesBlackRect.centerx - step * 2
            rectHadesBlacky19 = hadesBlackRect.centery + step * 2
            rectHadesBlack19 = pygame.Rect(rectHadesBlackx19 - 30, rectHadesBlacky19 - 30, 60, 60)
            rectsHadesBlack.append(rectHadesBlack19)

            # Persefona černá
            persephoneBlackxInit = persephoneBlackRect.centerx
            persephoneBlackyInit = persephoneBlackRect.centery

            rectsPersephoneBlack = []

            rectPersephoneBlackx1 = persephoneBlackRect.centerx + step
            rectPersephoneBlacky1 = persephoneBlackRect.centery - step
            rectPersephoneBlack1 = pygame.Rect(rectPersephoneBlackx1 - 30, rectPersephoneBlacky1 - 30, 60, 60)
            rectsPersephoneBlack.append(rectPersephoneBlack1)

            rectPersephoneBlackx2 = persephoneBlackRect.centerx + step
            rectPersephoneBlacky2 = persephoneBlackRect.centery
            rectPersephoneBlack2 = pygame.Rect(rectPersephoneBlackx2 - 30, rectPersephoneBlacky2 - 30, 60, 60)
            rectsPersephoneBlack.append(rectPersephoneBlack2)

            rectPersephoneBlackx3 = persephoneBlackRect.centerx + step
            rectPersephoneBlacky3 = persephoneBlackRect.centery + step
            rectPersephoneBlack3 = pygame.Rect(rectPersephoneBlackx3 - 30, rectPersephoneBlacky3 - 30, 60, 60)
            rectsPersephoneBlack.append(rectPersephoneBlack3)

            rectPersephoneBlackx4 = persephoneBlackRect.centerx
            rectPersephoneBlacky4 = persephoneBlackRect.centery + step
            rectPersephoneBlack4 = pygame.Rect(rectPersephoneBlackx4 - 30, rectPersephoneBlacky4 - 30, 60, 60)
            rectsPersephoneBlack.append(rectPersephoneBlack4)

            rectPersephoneBlackx5 = persephoneBlackRect.centerx
            rectPersephoneBlacky5 = persephoneBlackRect.centery - step
            rectPersephoneBlack5 = pygame.Rect(rectPersephoneBlackx5 - 30, rectPersephoneBlacky5 - 30, 60, 60)
            rectsPersephoneBlack.append(rectPersephoneBlack5)

            rectPersephoneBlackx6 = persephoneBlackRect.centerx - step
            rectPersephoneBlacky6 = persephoneBlackRect.centery - step
            rectPersephoneBlack6 = pygame.Rect(rectPersephoneBlackx6 - 30, rectPersephoneBlacky6 - 30, 60, 60)
            rectsPersephoneBlack.append(rectPersephoneBlack6)

            rectPersephoneBlackx7 = persephoneBlackRect.centerx - step
            rectPersephoneBlacky7 = persephoneBlackRect.centery
            rectPersephoneBlack7 = pygame.Rect(rectPersephoneBlackx7 - 30, rectPersephoneBlacky7 - 30, 60, 60)
            rectsPersephoneBlack.append(rectPersephoneBlack7)

            rectPersephoneBlackx8 = persephoneBlackRect.centerx - step
            rectPersephoneBlacky8 = persephoneBlackRect.centery + step
            rectPersephoneBlack8 = pygame.Rect(rectPersephoneBlackx8 - 30, rectPersephoneBlacky8 - 30, 60, 60)
            rectsPersephoneBlack.append(rectPersephoneBlack8)

            # Kardinál černý 1
            cardinalBlackxInit1 = cardinalBlackRect1.centerx
            cardinalBlackyInit1 = cardinalBlackRect1.centery

            rectsCardinalBlack_1 = []

            rectCardinalBlackx1_1 = cardinalBlackRect1.centerx + step
            rectCardinalBlacky1_1 = cardinalBlackRect1.centery - step
            rectCardinalBlack1_1 = pygame.Rect(rectCardinalBlackx1_1 - 30, rectCardinalBlacky1_1 - 30, 60, 60)
            rectsCardinalBlack_1.append(rectCardinalBlack1_1)

            rectCardinalBlackx2_1 = cardinalBlackRect1.centerx + step
            rectCardinalBlacky2_1 = cardinalBlackRect1.centery + step
            rectCardinalBlack2_1 = pygame.Rect(rectCardinalBlackx2_1 - 30, rectCardinalBlacky2_1 - 30, 60, 60)
            rectsCardinalBlack_1.append(rectCardinalBlack2_1)

            rectCardinalBlackx3_1 = cardinalBlackRect1.centerx - step
            rectCardinalBlacky3_1 = cardinalBlackRect1.centery - step
            rectCardinalBlack3_1 = pygame.Rect(rectCardinalBlackx3_1 - 30, rectCardinalBlacky3_1 - 30, 60, 60)
            rectsCardinalBlack_1.append(rectCardinalBlack3_1)

            rectCardinalBlackx4_1 = cardinalBlackRect1.centerx - step
            rectCardinalBlacky4_1 = cardinalBlackRect1.centery + step
            rectCardinalBlack4_1 = pygame.Rect(rectCardinalBlackx4_1 - 30, rectCardinalBlacky4_1 - 30, 60, 60)
            rectsCardinalBlack_1.append(rectCardinalBlack4_1)

            # Arcibiskup černý 1
            archbishopBlackxInit1 = archbishopBlackRect1.centerx
            archbishopBlackyInit1 = archbishopBlackRect1.centery

            rectsArchbishopBlack_1 = []

            rectArchbishopBlackx1_1 = archbishopBlackRect1.centerx + step * 2
            rectArchbishopBlacky1_1 = archbishopBlackRect1.centery
            rectArchbishopBlack1_1 = pygame.Rect(rectArchbishopBlackx1_1 - 30, rectArchbishopBlacky1_1 - 30, 60, 60)
            rectsArchbishopBlack_1.append(rectArchbishopBlack1_1)

            rectArchbishopBlackx2_1 = archbishopBlackRect1.centerx + step * 2
            rectArchbishopBlacky2_1 = archbishopBlackRect1.centery - step
            rectArchbishopBlack2_1 = pygame.Rect(rectArchbishopBlackx2_1 - 30, rectArchbishopBlacky2_1 - 30, 60, 60)
            rectsArchbishopBlack_1.append(rectArchbishopBlack2_1)

            rectArchbishopBlackx3_1 = archbishopBlackRect1.centerx + step * 2
            rectArchbishopBlacky3_1 = archbishopBlackRect1.centery + step
            rectArchbishopBlack3_1 = pygame.Rect(rectArchbishopBlackx3_1 - 30, rectArchbishopBlacky3_1 - 30, 60, 60)
            rectsArchbishopBlack_1.append(rectArchbishopBlack3_1)

            rectArchbishopBlackx4_1 = archbishopBlackRect1.centerx - step * 2
            rectArchbishopBlacky4_1 = archbishopBlackRect1.centery
            rectArchbishopBlack4_1 = pygame.Rect(rectArchbishopBlackx4_1 - 30, rectArchbishopBlacky4_1 - 30, 60, 60)
            rectsArchbishopBlack_1.append(rectArchbishopBlack4_1)

            rectArchbishopBlackx5_1 = archbishopBlackRect1.centerx - step * 2
            rectArchbishopBlacky5_1 = archbishopBlackRect1.centery - step
            rectArchbishopBlack5_1 = pygame.Rect(rectArchbishopBlackx5_1 - 30, rectArchbishopBlacky5_1 - 30, 60, 60)
            rectsArchbishopBlack_1.append(rectArchbishopBlack5_1)

            rectArchbishopBlackx6_1 = archbishopBlackRect1.centerx - step * 2
            rectArchbishopBlacky6_1 = archbishopBlackRect1.centery + step
            rectArchbishopBlack6_1 = pygame.Rect(rectArchbishopBlackx6_1 - 30, rectArchbishopBlacky6_1 - 30, 60, 60)
            rectsArchbishopBlack_1.append(rectArchbishopBlack6_1)

            rectArchbishopBlackx7_1 = archbishopBlackRect1.centerx
            rectArchbishopBlacky7_1 = archbishopBlackRect1.centery + step * 2
            rectArchbishopBlack7_1 = pygame.Rect(rectArchbishopBlackx7_1 - 30, rectArchbishopBlacky7_1 - 30, 60, 60)
            rectsArchbishopBlack_1.append(rectArchbishopBlack7_1)

            rectArchbishopBlackx8_1 = archbishopBlackRect1.centerx - step
            rectArchbishopBlacky8_1 = archbishopBlackRect1.centery + step * 2
            rectArchbishopBlack8_1 = pygame.Rect(rectArchbishopBlackx8_1 - 30, rectArchbishopBlacky8_1 - 30, 60, 60)
            rectsArchbishopBlack_1.append(rectArchbishopBlack8_1)

            rectArchbishopBlackx9_1 = archbishopBlackRect1.centerx + step
            rectArchbishopBlacky9_1 = archbishopBlackRect1.centery + step * 2
            rectArchbishopBlack9_1 = pygame.Rect(rectArchbishopBlackx9_1 - 30, rectArchbishopBlacky9_1 - 30, 60, 60)
            rectsArchbishopBlack_1.append(rectArchbishopBlack9_1)

            rectArchbishopBlackx10_1 = archbishopBlackRect1.centerx
            rectArchbishopBlacky10_1 = archbishopBlackRect1.centery - step * 2
            rectArchbishopBlack10_1 = pygame.Rect(rectArchbishopBlackx10_1 - 30, rectArchbishopBlacky10_1 - 30, 60, 60)
            rectsArchbishopBlack_1.append(rectArchbishopBlack10_1)

            rectArchbishopBlackx11_1 = archbishopBlackRect1.centerx - step
            rectArchbishopBlacky11_1 = archbishopBlackRect1.centery - step * 2
            rectArchbishopBlack11_1 = pygame.Rect(rectArchbishopBlackx11_1 - 30, rectArchbishopBlacky11_1 - 30, 60, 60)
            rectsArchbishopBlack_1.append(rectArchbishopBlack11_1)

            rectArchbishopBlackx12_1 = archbishopBlackRect1.centerx + step
            rectArchbishopBlacky12_1 = archbishopBlackRect1.centery - step * 2
            rectArchbishopBlack12_1 = pygame.Rect(rectArchbishopBlackx12_1 - 30, rectArchbishopBlacky12_1 - 30, 60, 60)
            rectsArchbishopBlack_1.append(rectArchbishopBlack12_1)

            # Morový doktor černý 1
            plagueBlackxInit1 = plagueDoctorBlackRect1.centerx
            plagueBlackyInit1 = plagueDoctorBlackRect1.centery

            rectsPlagueDoctorBlack_1 = []

            rectPlagueBlackx1_1 = plagueDoctorBlackRect1.centerx + step
            rectPlagueBlacky1_1 = plagueDoctorBlackRect1.centery
            rectPlagueBlack1_1 = pygame.Rect(rectPlagueBlackx1_1 - 30, rectPlagueBlacky1_1 - 30, 60, 60)
            rectsPlagueDoctorBlack_1.append(rectPlagueBlack1_1)

            rectPlagueBlackx2_1 = plagueDoctorBlackRect1.centerx + step * 2
            rectPlagueBlacky2_1 = plagueDoctorBlackRect1.centery
            rectPlagueBlack2_1 = pygame.Rect(rectPlagueBlackx2_1 - 30, rectPlagueBlacky2_1 - 30, 60, 60)
            rectsPlagueDoctorBlack_1.append(rectPlagueBlack2_1)

            rectPlagueBlackx3_1 = plagueDoctorBlackRect1.centerx - step
            rectPlagueBlacky3_1 = plagueDoctorBlackRect1.centery
            rectPlagueBlack3_1 = pygame.Rect(rectPlagueBlackx3_1 - 30, rectPlagueBlacky3_1 - 30, 60, 60)
            rectsPlagueDoctorBlack_1.append(rectPlagueBlack3_1)

            rectPlagueBlackx4_1 = plagueDoctorBlackRect1.centerx - step * 2
            rectPlagueBlacky4_1 = plagueDoctorBlackRect1.centery
            rectPlagueBlack4_1 = pygame.Rect(rectPlagueBlackx4_1 - 30, rectPlagueBlacky4_1 - 30, 60, 60)
            rectsPlagueDoctorBlack_1.append(rectPlagueBlack4_1)

            rectPlagueBlackx5_1 = plagueDoctorBlackRect1.centerx
            rectPlagueBlacky5_1 = plagueDoctorBlackRect1.centery + step
            rectPlagueBlack5_1 = pygame.Rect(rectPlagueBlackx5_1 - 30, rectPlagueBlacky5_1 - 30, 60, 60)
            rectsPlagueDoctorBlack_1.append(rectPlagueBlack5_1)

            rectPlagueBlackx6_1 = plagueDoctorBlackRect1.centerx
            rectPlagueBlacky6_1 = plagueDoctorBlackRect1.centery + step * 2
            rectPlagueBlack6_1 = pygame.Rect(rectPlagueBlackx6_1 - 30, rectPlagueBlacky6_1 - 30, 60, 60)
            rectsPlagueDoctorBlack_1.append(rectPlagueBlack6_1)

            rectPlagueBlackx7_1 = plagueDoctorBlackRect1.centerx
            rectPlagueBlacky7_1 = plagueDoctorBlackRect1.centery + step * 3
            rectPlagueBlack7_1 = pygame.Rect(rectPlagueBlackx7_1 - 30, rectPlagueBlacky7_1 - 30, 60, 60)
            rectsPlagueDoctorBlack_1.append(rectPlagueBlack7_1)

            rectPlagueBlackx8_1 = plagueDoctorBlackRect1.centerx
            rectPlagueBlacky8_1 = plagueDoctorBlackRect1.centery + step * 4
            rectPlagueBlack8_1 = pygame.Rect(rectPlagueBlackx8_1 - 30, rectPlagueBlacky8_1 - 30, 60, 60)
            rectsPlagueDoctorBlack_1.append(rectPlagueBlack8_1)

            rectPlagueBlackx9_1 = plagueDoctorBlackRect1.centerx
            rectPlagueBlacky9_1 = plagueDoctorBlackRect1.centery + step * 5
            rectPlagueBlack9_1 = pygame.Rect(rectPlagueBlackx9_1 - 30, rectPlagueBlacky9_1 - 30, 60, 60)
            rectsPlagueDoctorBlack_1.append(rectPlagueBlack9_1)

            rectPlagueBlackx10_1 = plagueDoctorBlackRect1.centerx
            rectPlagueBlacky10_1 = plagueDoctorBlackRect1.centery + step * 6
            rectPlagueBlack10_1 = pygame.Rect(rectPlagueBlackx10_1 - 30, rectPlagueBlacky10_1 - 30, 60, 60)
            rectsPlagueDoctorBlack_1.append(rectPlagueBlack10_1)

            rectPlagueBlackx11_1 = plagueDoctorBlackRect1.centerx
            rectPlagueBlacky11_1 = plagueDoctorBlackRect1.centery + step * 7
            rectPlagueBlack11_1 = pygame.Rect(rectPlagueBlackx11_1 - 30, rectPlagueBlacky11_1 - 30, 60, 60)
            rectsPlagueDoctorBlack_1.append(rectPlagueBlack11_1)

            rectPlagueBlackx12_1 = plagueDoctorBlackRect1.centerx
            rectPlagueBlacky12_1 = plagueDoctorBlackRect1.centery - step
            rectPlagueBlack12_1 = pygame.Rect(rectPlagueBlackx12_1 - 30, rectPlagueBlacky12_1 - 30, 60, 60)
            rectsPlagueDoctorBlack_1.append(rectPlagueBlack12_1)

            rectPlagueBlackx13_1 = plagueDoctorBlackRect1.centerx
            rectPlagueBlacky13_1 = plagueDoctorBlackRect1.centery - step * 2
            rectPlagueBlack13_1 = pygame.Rect(rectPlagueBlackx13_1 - 30, rectPlagueBlacky13_1 - 30, 60, 60)
            rectsPlagueDoctorBlack_1.append(rectPlagueBlack13_1)

            rectPlagueBlackx14_1 = plagueDoctorBlackRect1.centerx
            rectPlagueBlacky14_1 = plagueDoctorBlackRect1.centery - step * 3
            rectPlagueBlack14_1 = pygame.Rect(rectPlagueBlackx14_1 - 30, rectPlagueBlacky14_1 - 30, 60, 60)
            rectsPlagueDoctorBlack_1.append(rectPlagueBlack14_1)

            rectPlagueBlackx15_1 = plagueDoctorBlackRect1.centerx
            rectPlagueBlacky15_1 = plagueDoctorBlackRect1.centery - step * 4
            rectPlagueBlack15_1 = pygame.Rect(rectPlagueBlackx15_1 - 30, rectPlagueBlacky15_1 - 30, 60, 60)
            rectsPlagueDoctorBlack_1.append(rectPlagueBlack15_1)

            rectPlagueBlackx16_1 = plagueDoctorBlackRect1.centerx
            rectPlagueBlacky16_1 = plagueDoctorBlackRect1.centery - step * 5
            rectPlagueBlack16_1 = pygame.Rect(rectPlagueBlackx16_1 - 30, rectPlagueBlackx16_1 - 30, 60, 60)
            rectsPlagueDoctorBlack_1.append(rectPlagueBlack16_1)

            rectPlagueBlackx17_1 = plagueDoctorBlackRect1.centerx
            rectPlagueBlacky17_1 = plagueDoctorBlackRect1.centery - step * 6
            rectPlagueBlack17_1 = pygame.Rect(rectPlagueBlackx17_1 - 30, rectPlagueBlacky17_1 - 30, 60, 60)
            rectsPlagueDoctorBlack_1.append(rectPlagueBlack17_1)

            rectPlagueBlackx18_1 = plagueDoctorBlackRect1.centerx
            rectPlagueBlacky18_1 = plagueDoctorBlackRect1.centery - step * 7
            rectPlagueBlack18_1 = pygame.Rect(rectPlagueBlackx18_1 - 30, rectPlagueBlacky18_1 - 30, 60, 60)
            rectsPlagueDoctorBlack_1.append(rectPlagueBlack18_1)

            # Legionář černý
            legionaryBlackxInit = legionaryBlackRect.centerx
            legionaryBlackyInit = legionaryBlackRect.centery

            rectsLegionaryBlack = []

            rectLegionaryBlackx1 = legionaryBlackRect.centerx + step
            rectLegionaryBlacky1 = legionaryBlackRect.centery - step
            rectLegionaryBlack1 = pygame.Rect(rectLegionaryBlackx1 - 30, rectLegionaryBlacky1 - 30, 60, 60)
            rectsLegionaryBlack.append(rectLegionaryBlack1)

            rectLegionaryBlackx2 = legionaryBlackRect.centerx
            rectLegionaryBlacky2 = legionaryBlackRect.centery - step
            rectLegionaryBlack2 = pygame.Rect(rectLegionaryBlackx2 - 30, rectLegionaryBlacky2 - 30, 60, 60)
            rectsLegionaryBlack.append(rectLegionaryBlack2)

            rectLegionaryBlackx3 = legionaryBlackRect.centerx - step
            rectLegionaryBlacky3 = legionaryBlackRect.centery - step
            rectLegionaryBlack3 = pygame.Rect(rectLegionaryBlackx3 - 30, rectLegionaryBlacky3 - 30, 60, 60)
            rectsLegionaryBlack.append(rectLegionaryBlack3)

            # Válečník černý
            warriorBlackxInit = warriorBlackRect.centerx
            warriorBlackyInit = warriorBlackRect.centery

            rectsWarriorBlack = []

            rectWarriorBlackx1 = warriorBlackRect.centerx + step
            rectWarriorBlacky1 = warriorBlackRect.centery
            rectWarriorBlack1 = pygame.Rect(rectWarriorBlackx1 - 30, rectWarriorBlacky1 - 30, 60, 60)
            rectsWarriorBlack.append(rectWarriorBlack1)

            rectWarriorBlackx2 = warriorBlackRect.centerx
            rectWarriorBlacky2 = warriorBlackRect.centery + step
            rectWarriorBlack2 = pygame.Rect(rectWarriorBlackx2 - 30, rectWarriorBlacky2 - 30, 60, 60)
            rectsWarriorBlack.append(rectWarriorBlack2)

            rectWarriorBlackx3 = warriorBlackRect.centerx - step
            rectWarriorBlacky3 = warriorBlackRect.centery
            rectWarriorBlack3 = pygame.Rect(rectWarriorBlackx3 - 30, rectWarriorBlacky3 - 30, 60, 60)
            rectsWarriorBlack.append(rectWarriorBlack3)

            rectWarriorBlackx4 = warriorBlackRect.centerx
            rectWarriorBlacky4 = warriorBlackRect.centery - step
            rectWarriorBlack4 = pygame.Rect(rectWarriorBlackx4 - 30, rectWarriorBlacky4 - 30, 60, 60)
            rectsWarriorBlack.append(rectWarriorBlack4)

            # Válečník černý abilita
            rectsWarriorBlackAbility = []

            rectWarriorBlackx1Ability = warriorBlackRect.centerx + step * 2
            rectWarriorBlack1Ability = warriorBlackRect.centery
            rectWarriorBlack1Ability = pygame.Rect(rectWarriorBlackx1Ability - 30, rectWarriorBlack1Ability - 30,
                                                   60, 60)
            rectsWarriorBlackAbility.append(rectWarriorBlack1Ability)

            rectWarriorBlackx2Ability = warriorBlackRect.centerx - step * 2
            rectWarriorBlacky2Ability = warriorBlackRect.centery
            rectWarriorBlack2Ability = pygame.Rect(rectWarriorBlackx2Ability - 30, rectWarriorBlacky2Ability - 30,
                                                   60, 60)
            rectsWarriorBlackAbility.append(rectWarriorBlack2Ability)

            rectWarriorBlackx3Ability = warriorBlackRect.centerx
            rectWarriorBlacky3Ability = warriorBlackRect.centery - step * 2
            rectWarriorBlack3Ability = pygame.Rect(rectWarriorBlackx3Ability - 30, rectWarriorBlacky3Ability - 30,
                                                   60, 60)
            rectsWarriorBlackAbility.append(rectWarriorBlack3Ability)

            rectWarriorBlackx4Ability = warriorBlackRect.centerx
            rectWarriorBlacky4Ability = warriorBlackRect.centery + step * 2
            rectWarriorBlack4Ability = pygame.Rect(rectWarriorBlackx4Ability - 30, rectWarriorBlacky4Ability - 30,
                                                   60, 60)
            rectsWarriorBlackAbility.append(rectWarriorBlack4Ability)

            # Legionář černý 1
            legionaryBlackxInit1 = legionaryBlackRect1.centerx
            legionaryBlackyInit1 = legionaryBlackRect1.centery

            rectsLegionaryBlack_1 = []

            rectLegionaryBlackx1_1 = legionaryBlackRect1.centerx + step
            rectLegionaryBlacky1_1 = legionaryBlackRect1.centery - step
            rectLegionaryBlack1_1 = pygame.Rect(rectLegionaryBlackx1_1 - 30, rectLegionaryBlacky1_1 - 30, 60, 60)
            rectsLegionaryBlack_1.append(rectLegionaryBlack1_1)

            rectLegionaryBlackx2_1 = legionaryBlackRect1.centerx
            rectLegionaryBlacky2_1 = legionaryBlackRect1.centery - step
            rectLegionaryBlack2_1 = pygame.Rect(rectLegionaryBlackx2_1 - 30, rectLegionaryBlacky2_1 - 30, 60, 60)
            rectsLegionaryBlack_1.append(rectLegionaryBlack2_1)

            rectLegionaryBlackx3_1 = legionaryBlackRect1.centerx - step
            rectLegionaryBlacky3_1 = legionaryBlackRect1.centery - step
            rectLegionaryBlack3_1 = pygame.Rect(rectLegionaryBlackx3_1 - 30, rectLegionaryBlacky3_1 - 30, 60, 60)
            rectsLegionaryBlack_1.append(rectLegionaryBlack3_1)

            # Válečník černý 1
            warriorBlackxInit1 = warriorBlackRect1.centerx
            warriorBlackyInit1 = warriorBlackRect1.centery

            rectsWarriorBlack_1 = []

            rectWarriorBlackx1_1 = warriorBlackRect1.centerx + step
            rectWarriorBlacky1_1 = warriorBlackRect1.centery
            rectWarriorBlack1_1 = pygame.Rect(rectWarriorBlackx1_1 - 30, rectWarriorBlacky1_1 - 30, 60, 60)
            rectsWarriorBlack_1.append(rectWarriorBlack1_1)

            rectWarriorBlackx2_1 = warriorBlackRect1.centerx
            rectWarriorBlacky2_1 = warriorBlackRect1.centery + step
            rectWarriorBlack2_1 = pygame.Rect(rectWarriorBlackx2_1 - 30, rectWarriorBlacky2_1 - 30, 60, 60)
            rectsWarriorBlack_1.append(rectWarriorBlack2_1)

            rectWarriorBlackx3_1 = warriorBlackRect1.centerx
            rectWarriorBlacky3_1 = warriorBlackRect1.centery - step
            rectWarriorBlack3_1 = pygame.Rect(rectWarriorBlackx3_1 - 30, rectWarriorBlacky3_1 - 30, 60, 60)
            rectsWarriorBlack_1.append(rectWarriorBlack3_1)

            rectWarriorBlackx4_1 = warriorBlackRect1.centerx - step
            rectWarriorBlacky4_1 = warriorBlackRect1.centery
            rectWarriorBlack4_1 = pygame.Rect(rectWarriorBlackx4_1 - 30, rectWarriorBlacky4_1 - 30, 60, 60)
            rectsWarriorBlack_1.append(rectWarriorBlack4_1)

            # Válečník černý 1 abilita
            rectsWarriorBlackAbility_1 = []

            rectWarriorBlackx1_1Ability = warriorBlackRect1.centerx + step * 2
            rectWarriorBlacky1_1Ability = warriorBlackRect1.centery
            rectWarriorBlack1_1Ability = pygame.Rect(rectWarriorBlackx1_1Ability - 30, rectWarriorBlacky1_1Ability - 30,
                                                     60, 60)
            rectsWarriorBlackAbility_1.append(rectWarriorBlack1_1Ability)

            rectWarriorBlackx2_1Ability = warriorBlackRect1.centerx - step * 2
            rectWarriorBlacky2_1Ability = warriorBlackRect1.centery
            rectWarriorBlack2_1Ability = pygame.Rect(rectWarriorBlackx2_1Ability - 30, rectWarriorBlacky2_1Ability - 30,
                                                     60, 60)
            rectsWarriorBlackAbility_1.append(rectWarriorBlack2_1Ability)

            rectWarriorBlackx3_1Ability = warriorBlackRect1.centerx
            rectWarriorBlacky3_1Ability = warriorBlackRect1.centery - step * 2
            rectWarriorBlack3_1Ability = pygame.Rect(rectWarriorBlackx3_1Ability - 30, rectWarriorBlacky3_1Ability - 30,
                                                     60, 60)
            rectsWarriorBlackAbility_1.append(rectWarriorBlack3_1Ability)

            rectWarriorBlackx4_1Ability = warriorBlackRect1.centerx
            rectWarriorBlacky4_1Ability = warriorBlackRect1.centery + step * 2
            rectWarriorBlack4_1Ability = pygame.Rect(rectWarriorBlackx4_1Ability - 30, rectWarriorBlacky4_1Ability - 30,
                                                     60, 60)
            rectsWarriorBlackAbility_1.append(rectWarriorBlack4_1Ability)

            # Legionář černý 2
            legionaryBlackxInit2 = legionaryBlackRect2.centerx
            legionaryBlackyInit2 = legionaryBlackRect2.centery

            rectsLegionaryBlack_2 = []

            rectLegionaryBlackx1_2 = legionaryBlackRect2.centerx + step
            rectLegionaryBlacky1_2 = legionaryBlackRect2.centery - step
            rectLegionaryBlack1_2 = pygame.Rect(rectLegionaryBlackx1_2 - 30, rectLegionaryBlacky1_2 - 30, 60, 60)
            rectsLegionaryBlack_2.append(rectLegionaryBlack1_2)

            rectLegionaryBlackx2_2 = legionaryBlackRect2.centerx
            rectLegionaryBlacky2_2 = legionaryBlackRect2.centery - step
            rectLegionaryBlack2_2 = pygame.Rect(rectLegionaryBlackx2_2 - 30, rectLegionaryBlacky2_2 - 30, 60, 60)
            rectsLegionaryBlack_2.append(rectLegionaryBlack2_2)

            rectLegionaryBlackx3_2 = legionaryBlackRect2.centerx - step
            rectLegionaryBlacky3_2 = legionaryBlackRect2.centery - step
            rectLegionaryBlack3_2 = pygame.Rect(rectLegionaryBlackx3_2 - 30, rectLegionaryBlacky3_2 - 30, 60, 60)
            rectsLegionaryBlack_2.append(rectLegionaryBlack3_2)

            # Válečník černý 2
            warriorBlackxInit2 = warriorBlackRect2.centerx
            warriorBlackyInit2 = warriorBlackRect2.centery

            rectsWarriorBlack_2 = []

            rectWarriorBlackx1_2 = warriorBlackRect2.centerx + step
            rectWarriorBlacky1_2 = warriorBlackRect2.centery
            rectWarriorBlack1_2 = pygame.Rect(rectWarriorBlackx1_2 - 30, rectWarriorBlacky1_2 - 30, 60, 60)
            rectsWarriorBlack_2.append(rectWarriorBlack1_2)

            rectWarriorBlackx2_2 = warriorBlackRect2.centerx
            rectWarriorBlacky2_2 = warriorBlackRect2.centery + step
            rectWarriorBlack2_2 = pygame.Rect(rectWarriorBlackx2_2 - 30, rectWarriorBlacky2_2 - 30, 60, 60)
            rectsWarriorBlack_2.append(rectWarriorBlack2_2)

            rectWarriorBlackx3_2 = warriorBlackRect2.centerx - step
            rectWarriorBlacky3_2 = warriorBlackRect2.centery
            rectWarriorBlack3_2 = pygame.Rect(rectWarriorBlackx3_2 - 30, rectWarriorBlacky3_2 - 30, 60, 60)
            rectsWarriorBlack_2.append(rectWarriorBlack3_2)

            rectWarriorBlackx4_2 = warriorBlackRect2.centerx
            rectWarriorBlacky4_2 = warriorBlackRect2.centery - step
            rectWarriorBlack4_2 = pygame.Rect(rectWarriorBlackx4_2 - 30, rectWarriorBlacky4_2 - 30, 60, 60)
            rectsWarriorBlack_2.append(rectWarriorBlack4_2)

            # Válečník černý 2 abilita
            rectsWarriorBlackAbility_2 = []

            rectWarriorBlackx1_2Ability = warriorBlackRect2.centerx + step * 2
            rectWarriorBlacky1_2Ability = warriorBlackRect2.centery
            rectWarriorBlack1_2Ability = pygame.Rect(rectWarriorBlackx1_2Ability - 30, rectWarriorBlacky1_2Ability - 30,
                                                     60, 60)
            rectsWarriorBlackAbility_2.append(rectWarriorBlack1_2Ability)

            rectWarriorBlackx2_2Ability = warriorBlackRect2.centerx - step * 2
            rectWarriorBlacky2_2Ability = warriorBlackRect2.centery
            rectWarriorBlack2_2Ability = pygame.Rect(rectWarriorBlackx2_2Ability - 30, rectWarriorBlacky2_2Ability - 30,
                                                     60, 60)
            rectsWarriorBlackAbility_2.append(rectWarriorBlack2_2Ability)

            rectWarriorBlackx3_2Ability = warriorBlackRect2.centerx
            rectWarriorBlacky3_2Ability = warriorBlackRect2.centery - step * 2
            rectWarriorBlack3_2Ability = pygame.Rect(rectWarriorBlackx3_2Ability - 30, rectWarriorBlacky3_2Ability - 30,
                                                     60, 60)
            rectsWarriorBlackAbility_2.append(rectWarriorBlack3_2Ability)

            rectWarriorBlackx4_2Ability = warriorBlackRect2.centerx
            rectWarriorBlacky4_2Ability = warriorBlackRect2.centery + step * 2
            rectWarriorBlack4_2Ability = pygame.Rect(rectWarriorBlackx4_2Ability - 30, rectWarriorBlacky4_2Ability - 30,
                                                     60, 60)
            rectsWarriorBlackAbility_2.append(rectWarriorBlack4_2Ability)

            # Legionář černý 3
            legionaryBlackxInit3 = legionaryBlackRect3.centerx
            legionaryBlackyInit3 = legionaryBlackRect3.centery

            rectsLegionaryBlack_3 = []

            rectLegionaryBlackx1_3 = legionaryBlackRect3.centerx + step
            rectLegionaryBlacky1_3 = legionaryBlackRect3.centery - step
            rectLegionaryBlack1_3 = pygame.Rect(rectLegionaryBlackx1_3 - 30, rectLegionaryBlacky1_3 - 30, 60, 60)
            rectsLegionaryBlack_3.append(rectLegionaryBlack1_3)

            rectLegionaryBlackx2_3 = legionaryBlackRect3.centerx
            rectLegionaryBlacky2_3 = legionaryBlackRect3.centery - step
            rectLegionaryBlack2_3 = pygame.Rect(rectLegionaryBlackx2_3 - 30, rectLegionaryBlacky2_3 - 30, 60, 60)
            rectsLegionaryBlack_3.append(rectLegionaryBlack2_3)

            rectLegionaryBlackx3_3 = legionaryBlackRect3.centerx - step
            rectLegionaryBlacky3_3 = legionaryBlackRect3.centery - step
            rectLegionaryBlack3_3 = pygame.Rect(rectLegionaryBlackx3_3 - 30, rectLegionaryBlacky3_3 - 30, 60, 60)
            rectsLegionaryBlack_3.append(rectLegionaryBlack3_3)

            # Válečník černý 3
            warriorBlackxInit3 = warriorBlackRect3.centerx
            warriorBlackyInit3 = warriorBlackRect3.centery

            rectsWarriorBlack_3 = []

            rectWarriorBlackx1_3 = warriorBlackRect3.centerx
            rectWarriorBlacky1_3 = warriorBlackRect3.centery + step
            rectWarriorBlack1_3 = pygame.Rect(rectWarriorBlackx1_3 - 30, rectWarriorBlacky1_3 - 30, 60, 60)
            rectsWarriorBlack_3.append(rectWarriorBlack1_3)

            rectWarriorBlackx2_3 = warriorBlackRect3.centerx - step
            rectWarriorBlacky2_3 = warriorBlackRect3.centery
            rectWarriorBlack2_3 = pygame.Rect(rectWarriorBlackx2_3 - 30, rectWarriorBlacky2_3 - 30, 60, 60)
            rectsWarriorBlack_3.append(rectWarriorBlack2_3)

            rectWarriorBlackx3_3 = warriorBlackRect3.centerx
            rectWarriorBlacky3_3 = warriorBlackRect3.centery - step
            rectWarriorBlack3_3 = pygame.Rect(rectWarriorBlackx3_3 - 30, rectWarriorBlacky3_3 - 30, 60, 60)
            rectsWarriorBlack_3.append(rectWarriorBlack3_3)

            rectWarriorBlackx4_3 = warriorBlackRect3.centerx + step
            rectWarriorBlacky4_3 = warriorBlackRect3.centery
            rectWarriorBlack4_3 = pygame.Rect(rectWarriorBlackx4_3 - 30, rectWarriorBlacky4_3 - 30, 60, 60)
            rectsWarriorBlack_3.append(rectWarriorBlack4_3)

            # Válečník černý 3 abilita
            rectsWarriorBlackAbility_3 = []

            rectWarriorBlackx1_3Ability = warriorBlackRect3.centerx + step * 2
            rectWarriorBlacky1_3Ability = warriorBlackRect3.centery
            rectWarriorBlack1_3Ability = pygame.Rect(rectWarriorBlackx1_3Ability - 30, rectWarriorBlacky1_3Ability - 30,
                                                     60, 60)
            rectsWarriorBlackAbility_3.append(rectWarriorBlack1_3Ability)

            rectWarriorBlackx2_3Ability = warriorBlackRect3.centerx - step * 2
            rectWarriorBlacky2_3Ability = warriorBlackRect3.centery
            rectWarriorBlack2_3Ability = pygame.Rect(rectWarriorBlackx2_3Ability - 30, rectWarriorBlacky2_3Ability - 30,
                                                     60, 60)
            rectsWarriorBlackAbility_3.append(rectWarriorBlack2_3Ability)

            rectWarriorBlackx3_3Ability = warriorBlackRect3.centerx
            rectWarriorBlacky3_3Ability = warriorBlackRect3.centery - step * 2
            rectWarriorBlack3_3Ability = pygame.Rect(rectWarriorBlackx3_3Ability - 30, rectWarriorBlacky3_3Ability - 30,
                                                     60, 60)
            rectsWarriorBlackAbility_3.append(rectWarriorBlack3_3Ability)

            rectWarriorBlackx4_3Ability = warriorBlackRect3.centerx
            rectWarriorBlacky4_3Ability = warriorBlackRect3.centery + step * 2
            rectWarriorBlack4_3Ability = pygame.Rect(rectWarriorBlackx4_3Ability - 30, rectWarriorBlacky4_3Ability - 30,
                                                     60, 60)
            rectsWarriorBlackAbility_3.append(rectWarriorBlack4_3Ability)

        if event.type == pygame.KEYDOWN:
            if counter % 2 == 0:
                keys = pygame.key.get_pressed()

                if legionaryWhiteRect.collidepoint(pygame.mouse.get_pos()):
                    if event.key == pygame.K_F9:
                        #legionaryWhiteRect.centerx = legionar_bily_x_abilita
                        #legionaryWhiteRect.centery = legionar_bily_y_abilita
                        counter += 1
                elif legionaryWhiteRect1.collidepoint(pygame.mouse.get_pos()):
                    if event.key == pygame.K_F9:
                        legionaryWhiteRect1.centerx = legionar_bily_x_abilita_1
                        legionaryWhiteRect1.centery = legionar_bily_y_abilita_1
                        counter += 1
                elif legionaryWhiteRect2.collidepoint(pygame.mouse.get_pos()):
                    if event.key == pygame.K_F9:
                        legionaryWhiteRect2.centerx = legionar_bily_x_abilita_2
                        legionaryWhiteRect2.centery = legionar_bily_y_abilita_2
                        counter += 1
                elif legionaryWhiteRect3.collidepoint(pygame.mouse.get_pos()):
                    if event.key == pygame.K_F9:
                        legionaryWhiteRect3.centerx = legionar_bily_x_abilita_3
                        legionaryWhiteRect3.centery = legionar_bily_y_abilita_3
                        counter += 1

            else:
                keys = pygame.key.get_pressed()

                if legionaryBlackRect.collidepoint(pygame.mouse.get_pos()):
                    if event.key == pygame.K_F9:
                        legionaryBlackRect.centerx = legionar_cerny_x_abilita
                        legionaryBlackRect.centery = legionar_cerny_y_abilita
                        counter += 1
                if legionaryBlackRect1.collidepoint(pygame.mouse.get_pos()):
                    if event.key == pygame.K_F9:
                        legionaryBlackRect1.centerx = legionar_cerny_x_abilita_1
                        legionaryBlackRect1.centery = legionar_cerny_y_abilita_1
                        counter += 1
                if legionaryBlackRect2.collidepoint(pygame.mouse.get_pos()):
                    if event.key == pygame.K_F9:
                        legionaryBlackRect2.centerx = legionar_cerny_x_abilita_2
                        legionaryBlackRect2.centery = legionar_cerny_y_abilita_2
                        counter += 1
                if legionaryBlackRect3.collidepoint(pygame.mouse.get_pos()):
                    if event.key == pygame.K_F9:
                        legionaryBlackRect3.centerx = legionar_cerny_x_abilita_3
                        legionaryBlackRect3.centery = legionar_cerny_y_abilita_3
                        counter += 1

        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:

            pohyb = True
            """for figurka_cerna in figuresBlack:
                if figurka_cerna.collidepoint(event.pos):
                    figurka_cerna.centerx=event.pos[0]
                    figurka_cerna.centery=event.pos[1]
            for figurka_bila in figuresWhite:
                if figurka_bila.collidepoint(event.pos):
                    figurka_bila.centerx=event.pos[0]
                    figurka_bila.centery=event.pos[1]"""
            if counter % 2 == 0:  # Algoritmus funguje následovně - pokud je counter sudé číslo, hraje bílý, pokud je liché, hraje černý hráč
                keys = pygame.key.get_pressed()
                
                if plagueDoctorWhiteRect.collidepoint(event.pos):
                    if not plagueDoctorWhitePlaying:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                plagueDoctorWhitePlaying=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                plagueDoctorWhitePlaying=True
                elif plagueDoctorWhitePlaying:
                    if rectPlagueWhite1.collidepoint(event.pos):
                        plagueDoctorWhiteRect.centerx = rectPlagueWhite1.centerx
                        plagueDoctorWhiteRect.centery = rectPlagueWhite1.centery
                        counter += 1
                        plagueDoctorWhitePlaying=False
                    elif rectPlagueWhite2.collidepoint(event.pos):
                        plagueDoctorWhiteRect.centerx = rectPlagueWhite2.centerx
                        plagueDoctorWhiteRect.centery = rectPlagueWhite2.centery
                        counter += 1
                        plagueDoctorWhitePlaying=False
                    elif rectPlagueWhite3.collidepoint(event.pos):
                        plagueDoctorWhiteRect.centerx = rectPlagueWhite3.centerx
                        plagueDoctorWhiteRect.centery = rectPlagueWhite3.centery
                        counter += 1
                        plagueDoctorWhitePlaying=False
                    elif rectPlagueWhite4.collidepoint(event.pos):
                        plagueDoctorWhiteRect.centerx = rectPlagueWhite4.centerx
                        plagueDoctorWhiteRect.centery = rectPlagueWhite4.centery
                        counter += 1
                        plagueDoctorWhitePlaying=False
                    elif rectPlagueWhite5.collidepoint(event.pos):
                        plagueDoctorWhiteRect.centerx = rectPlagueWhite5.centerx
                        plagueDoctorWhiteRect.centery = rectPlagueWhite5.centery
                        counter += 1
                        plagueDoctorWhitePlaying=False
                    elif rectPlagueWhite6.collidepoint(event.pos):
                        plagueDoctorWhiteRect.centerx = rectPlagueWhite6.centerx
                        plagueDoctorWhiteRect.centery = rectPlagueWhite6.centery
                        counter += 1
                        plagueDoctorWhitePlaying=False
                    elif rectPlagueWhite7.collidepoint(event.pos):
                        plagueDoctorWhiteRect.centerx = rectPlagueWhite7.centerx
                        plagueDoctorWhiteRect.centery = rectPlagueWhite7.centery
                        counter += 1
                        plagueDoctorWhitePlaying=False
                    elif rectPlagueWhite8.collidepoint(event.pos):
                        plagueDoctorWhiteRect.centerx = rectPlagueWhite8.centerx
                        plagueDoctorWhiteRect.centery = rectPlagueWhite8.centery
                        counter += 1
                        plagueDoctorWhitePlaying=False
                    elif rectPlagueWhite9.collidepoint(event.pos):
                        plagueDoctorWhiteRect.centerx = rectPlagueWhite9.centerx
                        plagueDoctorWhiteRect.centery = rectPlagueWhite9.centery
                        counter += 1
                        plagueDoctorWhitePlaying=False
                    elif rectPlagueWhite10.collidepoint(event.pos):
                        plagueDoctorWhiteRect.centerx = rectPlagueWhite10.centerx
                        plagueDoctorWhiteRect.centery = rectPlagueWhite10.centery
                        counter += 1
                        plagueDoctorWhitePlaying=False
                    elif rectPlagueWhite11.collidepoint(event.pos):
                        plagueDoctorWhiteRect.centerx = rectPlagueWhite11.centerx
                        plagueDoctorWhiteRect.centery = rectPlagueWhite11.centery
                        counter += 1
                        plagueDoctorWhitePlaying=False
                    elif rectPlagueWhite12.collidepoint(event.pos):
                        plagueDoctorWhiteRect.centerx = rectPlagueWhite12.centerx
                        plagueDoctorWhiteRect.centery = rectPlagueWhite12.centery
                        counter += 1
                        plagueDoctorWhitePlaying=False
                    elif rectPlagueWhite13.collidepoint(event.pos):
                        plagueDoctorWhiteRect.centerx = rectPlagueWhite13.centerx
                        plagueDoctorWhiteRect.centery = rectPlagueWhite13.centery
                        counter += 1
                        plagueDoctorWhitePlaying=False
                    elif rectPlagueWhite14.collidepoint(event.pos):
                        plagueDoctorWhiteRect.centerx = rectPlagueWhite14.centerx
                        plagueDoctorWhiteRect.centery = rectPlagueWhite14.centery
                        counter += 1
                        plagueDoctorWhitePlaying=False
                    elif rectPlagueWhite15.collidepoint(event.pos):
                        plagueDoctorWhiteRect.centerx = rectPlagueWhite15.centerx
                        plagueDoctorWhiteRect.centery = rectPlagueWhite15.centery
                        counter += 1
                        plagueDoctorWhitePlaying=False
                    elif rectPlagueWhite16.collidepoint(event.pos):
                        plagueDoctorWhiteRect.centerx = rectPlagueWhite16.centerx
                        plagueDoctorWhiteRect.centery = rectPlagueWhite16.centery
                        counter += 1
                        plagueDoctorWhitePlaying=False
                    elif rectPlagueWhite17.collidepoint(event.pos):
                        plagueDoctorWhiteRect.centerx = rectPlagueWhite17.centerx
                        plagueDoctorWhiteRect.centery = rectPlagueWhite17.centery
                        counter += 1
                        plagueDoctorWhitePlaying=False
                    elif rectPlagueWhite18.collidepoint(event.pos):
                        plagueDoctorWhiteRect.centerx = rectPlagueWhite18.centerx
                        plagueDoctorWhiteRect.centery = rectPlagueWhite18.centery
                        counter += 1
                        plagueDoctorWhitePlaying=False
                    else:
                        plagueDoctorWhiteRect.centerx = plagueWhitexInit
                        plagueDoctorWhiteRect.centery = plagueWhiteyInit
                        plagueDoctorWhitePlaying=False
                    if plagueDoctorWhiteRect.colliderect(archbishopWhiteRect):
                        plagueDoctorWhiteRect.centerx = plagueWhitexInit
                        plagueDoctorWhiteRect.centery = plagueWhiteyInit
                        counter -= 1
                        plagueDoctorWhitePlaying=False
                    elif plagueDoctorWhiteRect.colliderect(cardinalWhiteRect):
                        plagueDoctorWhiteRect.centerx = plagueWhitexInit
                        plagueDoctorWhiteRect.centery = plagueWhiteyInit
                        counter -= 1
                        plagueDoctorWhitePlaying=False
                    elif plagueDoctorWhiteRect.colliderect(hadesWhiteRect):
                        plagueDoctorWhiteRect.centerx = plagueWhitexInit
                        plagueDoctorWhiteRect.centery = plagueWhiteyInit
                        counter -= 1
                        plagueDoctorWhitePlaying=False
                    elif plagueDoctorWhiteRect.colliderect(persephoneWhiteRect):
                        plagueDoctorWhiteRect.centerx = plagueWhitexInit
                        plagueDoctorWhiteRect.centery = plagueWhiteyInit
                        counter -= 1
                        plagueDoctorWhitePlaying=False
                    elif plagueDoctorWhiteRect.colliderect(cardinalWhiteRect1):
                        plagueDoctorWhiteRect.centerx = plagueWhitexInit
                        plagueDoctorWhiteRect.centery = plagueWhiteyInit
                        counter -= 1
                        plagueDoctorWhitePlaying=False
                    elif plagueDoctorWhiteRect.colliderect(archbishopWhiteRect1):
                        plagueDoctorWhiteRect.centerx = plagueWhitexInit
                        plagueDoctorWhiteRect.centery = plagueWhiteyInit
                        counter -= 1
                        plagueDoctorWhitePlaying=False
                    elif plagueDoctorWhiteRect.colliderect(plagueDoctorWhiteRect1):
                        plagueDoctorWhiteRect.centerx = plagueWhitexInit
                        plagueDoctorWhiteRect.centery = plagueWhiteyInit
                        counter -= 1
                        plagueDoctorWhitePlaying=False
                    elif plagueDoctorWhiteRect.colliderect(warriorWhiteRect):
                        plagueDoctorWhiteRect.centerx = plagueWhitexInit
                        plagueDoctorWhiteRect.centery = plagueWhiteyInit
                        counter -= 1
                        plagueDoctorWhitePlaying=False
                    elif plagueDoctorWhiteRect.colliderect(legionaryWhiteRect):
                        plagueDoctorWhiteRect.centerx = plagueWhitexInit
                        plagueDoctorWhiteRect.centery = plagueWhiteyInit
                        counter -= 1
                        plagueDoctorWhitePlaying=False
                    elif plagueDoctorWhiteRect.colliderect(warriorWhiteRect1):
                        plagueDoctorWhiteRect.centerx = plagueWhitexInit
                        plagueDoctorWhiteRect.centery = plagueWhiteyInit
                        counter -= 1
                        plagueDoctorWhitePlaying=False
                    elif plagueDoctorWhiteRect.colliderect(legionaryWhiteRect1):
                        plagueDoctorWhiteRect.centerx = plagueWhitexInit
                        plagueDoctorWhiteRect.centery = plagueWhiteyInit
                        counter -= 1
                        plagueDoctorWhitePlaying=False
                    elif plagueDoctorWhiteRect.colliderect(warriorWhiteRect2):
                        plagueDoctorWhiteRect.centerx = plagueWhitexInit
                        plagueDoctorWhiteRect.centery = plagueWhiteyInit
                        counter -= 1
                        plagueDoctorWhitePlaying=False
                    elif plagueDoctorWhiteRect.colliderect(legionaryWhiteRect2):
                        plagueDoctorWhiteRect.centerx = plagueWhitexInit
                        plagueDoctorWhiteRect.centery = plagueWhiteyInit
                        counter -= 1
                        plagueDoctorWhitePlaying=False
                    elif plagueDoctorWhiteRect.colliderect(warriorWhiteRect3):
                        plagueDoctorWhiteRect.centerx = plagueWhitexInit
                        plagueDoctorWhiteRect.centery = plagueWhiteyInit
                        counter -= 1
                        plagueDoctorWhitePlaying=False
                    elif plagueDoctorWhiteRect.colliderect(legionaryWhiteRect3):
                        plagueDoctorWhiteRect.centerx = plagueWhitexInit
                        plagueDoctorWhiteRect.centery = plagueWhiteyInit
                        counter -= 1
                        plagueDoctorWhitePlaying=False        
                        

                        #plagueDoctorWhiteRect.centerx = event.pos[0]
                        #plagueDoctorWhiteRect.centery = event.pos[1]

                if archbishopWhiteRect.collidepoint(event.pos):
                    if not archbishopWhitePlaying:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                archbishopWhitePlaying=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                archbishopWhitePlaying=True
                elif archbishopWhitePlaying:
                    if rectArchbishopWhite1.collidepoint(event.pos):
                        archbishopWhiteRect.centerx = rectArchbishopWhite1.centerx
                        archbishopWhiteRect.centery = rectArchbishopWhite1.centery
                        counter += 1
                        archbishopWhitePlaying=False
                    elif rectArchbishopWhite2.collidepoint(event.pos):
                        archbishopWhiteRect.centerx = rectArchbishopWhite2.centerx
                        archbishopWhiteRect.centery = rectArchbishopWhite2.centery
                        counter += 1
                        archbishopWhitePlaying=False
                    elif rectArchbishopWhite3.collidepoint(event.pos):
                        archbishopWhiteRect.centerx = rectArchbishopWhite3.centerx
                        archbishopWhiteRect.centery = rectArchbishopWhite3.centery
                        counter += 1
                        archbishopWhitePlaying=False
                    elif rectArchbishopWhite4.collidepoint(event.pos):
                        archbishopWhiteRect.centerx = rectArchbishopWhite4.centerx
                        archbishopWhiteRect.centery = rectArchbishopWhite4.centery
                        counter += 1
                        archbishopWhitePlaying=False
                    elif rectArchbishopWhite5.collidepoint(event.pos):
                        archbishopWhiteRect.centerx = rectArchbishopWhite5.centerx
                        archbishopWhiteRect.centery = rectArchbishopWhite5.centery
                        counter += 1
                        archbishopWhitePlaying=False
                    elif rectArchbishopWhite6.collidepoint(event.pos):
                        archbishopWhiteRect.centerx = rectArchbishopWhite6.centerx
                        archbishopWhiteRect.centery = rectArchbishopWhite6.centery
                        counter += 1
                        archbishopWhitePlaying=False
                    elif rectArchbishopWhite7.collidepoint(event.pos):
                        archbishopWhiteRect.centerx = rectArchbishopWhite7.centerx
                        archbishopWhiteRect.centery = rectArchbishopWhite7.centery
                        counter += 1
                        archbishopWhitePlaying=False
                    elif rectArchbishopWhite8.collidepoint(event.pos):
                        archbishopWhiteRect.centerx = rectArchbishopWhite8.centerx
                        archbishopWhiteRect.centery = rectArchbishopWhite8.centery
                        counter += 1
                        archbishopWhitePlaying=False
                    elif rectArchbishopWhite9.collidepoint(event.pos):
                        archbishopWhiteRect.centerx = rectArchbishopWhite9.centerx
                        archbishopWhiteRect.centery = rectArchbishopWhite9.centery
                        counter += 1
                        archbishopWhitePlaying=False
                    elif rectArchbishopWhite10.collidepoint(event.pos):
                        archbishopWhiteRect.centerx = rectArchbishopWhite10.centerx
                        archbishopWhiteRect.centery = rectArchbishopWhite10.centery
                        counter += 1
                        archbishopWhitePlaying=False
                    elif rectArchbishopWhite11.collidepoint(event.pos):
                        archbishopWhiteRect.centerx = rectArchbishopWhite11.centerx
                        archbishopWhiteRect.centery = rectArchbishopWhite11.centery
                        counter += 1
                        archbishopWhitePlaying=False
                    elif rectArchbishopWhite12.collidepoint(event.pos):
                        archbishopWhiteRect.centerx = rectArchbishopWhite12.centerx
                        archbishopWhiteRect.centery = rectArchbishopWhite12.centery
                        counter += 1
                        archbishopWhitePlaying=False
                    else:
                        archbishopWhiteRect.centerx = archbishopWhitexInit
                        archbishopWhiteRect.centery = archbishopWhiteyInit
                        archbishopWhitePlaying=False
                    if archbishopWhiteRect.colliderect(plagueDoctorWhiteRect):
                        archbishopWhiteRect.centerx = archbishopWhitexInit
                        archbishopWhiteRect.centery = archbishopWhiteyInit
                        counter -= 1
                        archbishopWhitePlaying=False
                    elif archbishopWhiteRect.colliderect(cardinalWhiteRect):
                        archbishopWhiteRect.centerx = archbishopWhitexInit
                        archbishopWhiteRect.centery = archbishopWhiteyInit
                        counter -= 1
                        archbishopWhitePlaying=False
                    elif archbishopWhiteRect.colliderect(hadesWhiteRect):
                        archbishopWhiteRect.centerx = archbishopWhitexInit
                        archbishopWhiteRect.centery = archbishopWhiteyInit
                        counter -= 1
                        archbishopWhitePlaying=False
                    elif archbishopWhiteRect.colliderect(persephoneWhiteRect):
                        archbishopWhiteRect.centerx = archbishopWhitexInit
                        archbishopWhiteRect.centery = archbishopWhiteyInit
                        counter -= 1
                        archbishopWhitePlaying=False
                    elif archbishopWhiteRect.colliderect(cardinalWhiteRect1):
                        archbishopWhiteRect.centerx = archbishopWhitexInit
                        archbishopWhiteRect.centery = archbishopWhiteyInit
                        counter -= 1
                        archbishopWhitePlaying=False
                    elif archbishopWhiteRect.colliderect(archbishopWhiteRect1):
                        archbishopWhiteRect.centerx = archbishopWhitexInit
                        archbishopWhiteRect.centery = archbishopWhiteyInit
                        counter -= 1
                        archbishopWhitePlaying=False
                    elif archbishopWhiteRect.colliderect(plagueDoctorWhiteRect1):
                        archbishopWhiteRect.centerx = archbishopWhitexInit
                        archbishopWhiteRect.centery = archbishopWhiteyInit
                        counter -= 1
                        archbishopWhitePlaying=False
                    elif archbishopWhiteRect.colliderect(warriorWhiteRect):
                        archbishopWhiteRect.centerx = archbishopWhitexInit
                        archbishopWhiteRect.centery = archbishopWhiteyInit
                        counter -= 1
                        archbishopWhitePlaying=False
                    elif archbishopWhiteRect.colliderect(legionaryWhiteRect):
                        archbishopWhiteRect.centerx = archbishopWhitexInit
                        archbishopWhiteRect.centery = archbishopWhiteyInit
                        counter -= 1
                        archbishopWhitePlaying=False
                    elif archbishopWhiteRect.colliderect(warriorWhiteRect1):
                        archbishopWhiteRect.centerx = archbishopWhitexInit
                        archbishopWhiteRect.centery = archbishopWhiteyInit
                        counter -= 1
                        archbishopWhitePlaying=False
                    elif archbishopWhiteRect.colliderect(legionaryWhiteRect1):
                        archbishopWhiteRect.centerx = archbishopWhitexInit
                        archbishopWhiteRect.centery = archbishopWhiteyInit
                        counter -= 1
                        archbishopWhitePlaying=False
                    elif archbishopWhiteRect.colliderect(warriorWhiteRect2):
                        archbishopWhiteRect.centerx = archbishopWhitexInit
                        archbishopWhiteRect.centery = archbishopWhiteyInit
                        counter -= 1
                        archbishopWhitePlaying=False
                    elif archbishopWhiteRect.colliderect(legionaryWhiteRect2):
                        archbishopWhiteRect.centerx = archbishopWhitexInit
                        archbishopWhiteRect.centery = archbishopWhiteyInit
                        counter -= 1
                        archbishopWhitePlaying=False
                    elif archbishopWhiteRect.colliderect(warriorWhiteRect3):
                        archbishopWhiteRect.centerx = archbishopWhitexInit
                        archbishopWhiteRect.centery = archbishopWhiteyInit
                        counter -= 1
                        archbishopWhitePlaying=False
                    elif archbishopWhiteRect.colliderect(legionaryWhiteRect3):
                        archbishopWhiteRect.centerx = archbishopWhitexInit
                        archbishopWhiteRect.centery = archbishopWhiteyInit
                        counter -= 1
                        archbishopWhitePlaying=False

                      

                        #archbishopWhiteRect.centerx = event.pos[0]
                        #archbishopWhiteRect.centery = event.pos[1]

                if cardinalWhiteRect.collidepoint(event.pos):
                    if not cardinalWhitePlaying:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                cardinalWhitePlaying=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                cardinalWhitePlaying=True
                elif cardinalWhitePlaying:
                    if rectCardinalWhite1.collidepoint(event.pos):
                        cardinalWhiteRect.centerx = rectCardinalWhite1.centerx
                        cardinalWhiteRect.centery = rectCardinalWhite1.centery
                        counter += 1
                        cardinalWhitePlaying=False
                    elif rectCardinalWhite2.collidepoint(event.pos):
                        cardinalWhiteRect.centerx = rectCardinalWhite2.centerx
                        cardinalWhiteRect.centery = rectCardinalWhite2.centery
                        counter += 1
                        cardinalWhitePlaying=False
                    elif rectCardinalWhite3.collidepoint(event.pos):
                        cardinalWhiteRect.centerx = rectCardinalWhite3.centerx
                        cardinalWhiteRect.centery = rectCardinalWhite3.centery
                        counter += 1
                        cardinalWhitePlaying=False
                    elif rectCardinalWhite4.collidepoint(event.pos):
                        cardinalWhiteRect.centerx = rectCardinalWhite4.centerx
                        cardinalWhiteRect.centery = rectCardinalWhite4.centery
                        counter += 1
                        cardinalWhitePlaying=False
                    else:
                        cardinalWhiteRect.centerx = cardinalWhitexInit
                        cardinalWhiteRect.centery = cardinalWhiteyInit
                        cardinalWhitePlaying=False
                    if cardinalWhiteRect.colliderect(plagueDoctorWhiteRect):
                        cardinalWhiteRect.centerx = cardinalWhitexInit
                        cardinalWhiteRect.centery = cardinalWhiteyInit
                        counter -= 1
                        cardinalWhitePlaying=False
                    elif cardinalWhiteRect.colliderect(archbishopWhiteRect):
                        cardinalWhiteRect.centerx = cardinalWhitexInit
                        cardinalWhiteRect.centery = cardinalWhiteyInit
                        counter -= 1
                        cardinalWhitePlaying=False
                    elif cardinalWhiteRect.colliderect(hadesWhiteRect):
                        cardinalWhiteRect.centerx = cardinalWhitexInit
                        cardinalWhiteRect.centery = cardinalWhiteyInit
                        counter -= 1
                        cardinalWhitePlaying=False
                    elif cardinalWhiteRect.colliderect(persephoneWhiteRect):
                        cardinalWhiteRect.centerx = cardinalWhitexInit
                        cardinalWhiteRect.centery = cardinalWhiteyInit
                        counter -= 1
                        cardinalWhitePlaying=False
                    elif cardinalWhiteRect.colliderect(plagueDoctorWhiteRect1):
                        cardinalWhiteRect.centerx = cardinalWhitexInit
                        cardinalWhiteRect.centery = cardinalWhiteyInit
                        counter -= 1
                        cardinalWhitePlaying=False
                    elif cardinalWhiteRect.colliderect(cardinalWhiteRect1):
                        cardinalWhiteRect.centerx = cardinalWhitexInit
                        cardinalWhiteRect.centery = cardinalWhiteyInit
                        counter -= 1
                        cardinalWhitePlaying=False
                    elif cardinalWhiteRect.colliderect(archbishopWhiteRect1):
                        cardinalWhiteRect.centerx = cardinalWhitexInit
                        cardinalWhiteRect.centery = cardinalWhiteyInit
                        counter -= 1
                        cardinalWhitePlaying=False
                    elif cardinalWhiteRect.colliderect(warriorWhiteRect):
                        cardinalWhiteRect.centerx = cardinalWhitexInit
                        cardinalWhiteRect.centery = cardinalWhiteyInit
                        counter -= 1
                        cardinalWhitePlaying=False
                    elif cardinalWhiteRect.colliderect(legionaryWhiteRect):
                        cardinalWhiteRect.centerx = cardinalWhitexInit
                        cardinalWhiteRect.centery = cardinalWhiteyInit
                        counter -= 1
                        cardinalWhitePlaying=False
                    elif cardinalWhiteRect.colliderect(warriorWhiteRect1):
                        cardinalWhiteRect.centerx = cardinalWhitexInit
                        cardinalWhiteRect.centery = cardinalWhiteyInit
                        counter -= 1
                        cardinalWhitePlaying=False
                    elif cardinalWhiteRect.colliderect(legionaryWhiteRect1):
                        cardinalWhiteRect.centerx = cardinalWhitexInit
                        cardinalWhiteRect.centery = cardinalWhiteyInit
                        counter -= 1
                        cardinalWhitePlaying=False
                    elif cardinalWhiteRect.colliderect(warriorWhiteRect2):
                        cardinalWhiteRect.centerx = cardinalWhitexInit
                        cardinalWhiteRect.centery = cardinalWhiteyInit
                        counter -= 1
                        cardinalWhitePlaying=False
                    elif cardinalWhiteRect.colliderect(legionaryWhiteRect2):
                        cardinalWhiteRect.centerx = cardinalWhitexInit
                        cardinalWhiteRect.centery = cardinalWhiteyInit
                        counter -= 1
                        cardinalWhitePlaying=False
                    elif cardinalWhiteRect.colliderect(warriorWhiteRect3):
                        cardinalWhiteRect.centerx = cardinalWhitexInit
                        cardinalWhiteRect.centery = cardinalWhiteyInit
                        counter -= 1
                        cardinalWhitePlaying=False
                    elif cardinalWhiteRect.colliderect(legionaryWhiteRect3):
                        cardinalWhiteRect.centerx = cardinalWhitexInit
                        cardinalWhiteRect.centery = cardinalWhiteyInit
                        counter -= 1
                        cardinalWhitePlaying=False


                        #cardinalWhiteRect.centerx = event.pos[0]
                        #cardinalWhiteRect.centery = event.pos[1]

                if hadesWhiteRect.collidepoint(event.pos):
                    if not hadesWhitePlaying:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                hadesWhitePlaying=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                hadesWhitePlaying=True
                elif hadesWhitePlaying:
                    if rectHadesWhite1.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite1.centerx
                        hadesWhiteRect.centery = rectHadesWhite1.centery
                        counter += 1
                        hadesWhitePlaying=False
                    elif rectHadesWhite2.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite2.centerx
                        hadesWhiteRect.centery = rectHadesWhite2.centery
                        counter += 1
                        hadesWhitePlaying=False
                    elif rectHadesWhite3.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite3.centerx
                        hadesWhiteRect.centery = rectHadesWhite3.centery
                        counter += 1
                        hadesWhitePlaying=False
                    elif rectHadesWhite4.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite4.centerx
                        hadesWhiteRect.centery = rectHadesWhite4.centery
                        counter += 1
                        hadesWhitePlaying=False
                    elif rectHadesWhite5.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite5.centerx
                        hadesWhiteRect.centery = rectHadesWhite5.centery
                        counter += 1
                        hadesWhitePlaying=False
                    elif rectHadesWhite6.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite6.centerx
                        hadesWhiteRect.centery = rectHadesWhite6.centery
                        counter += 1
                        hadesWhitePlaying=False
                    elif rectHadesWhite7.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite7.centerx
                        hadesWhiteRect.centery = rectHadesWhite7.centery
                        counter += 1
                        hadesWhitePlaying=False
                    elif rectHadesWhite8.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite8.centerx
                        hadesWhiteRect.centery = rectHadesWhite8.centery
                        counter += 1
                        hadesWhitePlaying=False
                    elif rectHadesWhite9.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite9.centerx
                        hadesWhiteRect.centery = rectHadesWhite9.centery
                        counter += 1
                        hadesWhitePlaying=False
                    elif rectHadesWhite10.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite10.centerx
                        hadesWhiteRect.centery = rectHadesWhite10.centery
                        counter += 1
                        hadesWhitePlaying=False
                    elif rectHadesWhite11.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite11.centerx
                        hadesWhiteRect.centery = rectHadesWhite11.centery
                        counter += 1
                        hadesWhitePlaying=False
                    elif rectHadesWhite12.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite12.centerx
                        hadesWhiteRect.centery = rectHadesWhite12.centery
                        counter += 1
                        hadesWhitePlaying=False
                    elif rectHadesWhite13.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite13.centerx
                        hadesWhiteRect.centery = rectHadesWhite13.centery
                        counter += 1
                        hadesWhitePlaying=False
                    elif rectHadesWhite14.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite14.centerx
                        hadesWhiteRect.centery = rectHadesWhite14.centery
                        counter += 1
                        hadesWhitePlaying=False
                    elif rectHadesWhite15.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite15.centerx
                        hadesWhiteRect.centery = rectHadesWhite15.centery
                        counter += 1
                        hadesWhitePlaying=False
                    elif rectHadesWhite16.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite16.centerx
                        hadesWhiteRect.centery = rectHadesWhite16.centery
                        counter += 1
                        hadesWhitePlaying=False
                    elif rectHadesWhite17.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite17.centerx
                        hadesWhiteRect.centery = rectHadesWhite17.centery
                        counter += 1
                        hadesWhitePlaying=False
                    elif rectHadesWhite18.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite18.centerx
                        hadesWhiteRect.centery = rectHadesWhite18.centery
                        counter += 1
                        hadesWhitePlaying=False
                    elif rectHadesWhite19.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite19.centerx
                        hadesWhiteRect.centery = rectHadesWhite19.centery
                        counter += 1
                        hadesWhitePlaying=False
                    else:
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        hadesWhitePlaying=False
                    if hadesWhiteRect.colliderect(plagueDoctorWhiteRect):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        counter -= 1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(archbishopWhiteRect):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        counter -= 1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(cardinalWhiteRect):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        counter -= 1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(persephoneWhiteRect):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        counter -= 1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(plagueDoctorWhiteRect1):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        counter -= 1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(cardinalWhiteRect1):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        counter -= 1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(archbishopWhiteRect1):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        counter -= 1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(warriorWhiteRect):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        counter -= 1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(legionaryWhiteRect):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        counter -= 1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(warriorWhiteRect1):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        counter -= 1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(legionaryWhiteRect1):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        counter -= 1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(warriorWhiteRect2):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        counter -= 1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(legionaryWhiteRect2):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        counter -= 1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(warriorWhiteRect3):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        counter -= 1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(legionaryWhiteRect3):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        counter -= 1
                        hadesWhitePlaying=False
                       
                if persephoneWhiteRect.collidepoint(event.pos):
                    if not persephoneWhitePlaying:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                persephoneWhitePlaying=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                persephoneWhitePlaying=True
                elif persephoneWhitePlaying:
                    if rectPersephoneWhite1.collidepoint(event.pos):
                        persephoneWhiteRect.centerx = rectPersephoneWhite1.centerx
                        persephoneWhiteRect.centery = rectPersephoneWhite1.centery
                        counter += 1
                        persephoneWhitePlaying=False
                    elif rectPersephoneWhite2.collidepoint(event.pos):
                        persephoneWhiteRect.centerx = rectPersephoneWhite2.centerx
                        persephoneWhiteRect.centery = rectPersephoneWhite2.centery
                        counter += 1
                        persephoneWhitePlaying=False
                    elif rectPersephoneWhite3.collidepoint(event.pos):
                        persephoneWhiteRect.centerx = rectPersephoneWhite3.centerx
                        persephoneWhiteRect.centery = rectPersephoneWhite3.centery
                        counter += 1
                        persephoneWhitePlaying=False
                    elif rectPersephoneWhite4.collidepoint(event.pos):
                        persephoneWhiteRect.centerx = rectPersephoneWhite4.centerx
                        persephoneWhiteRect.centery = rectPersephoneWhite4.centery
                        counter += 1
                        persephoneWhitePlaying=False
                    elif rectPersephoneWhite5.collidepoint(event.pos):
                        persephoneWhiteRect.centerx = rectPersephoneWhite5.centerx
                        persephoneWhiteRect.centery = rectPersephoneWhite5.centery
                        counter += 1
                        persephoneWhitePlaying=False
                    elif rectPersephoneWhite6.collidepoint(event.pos):
                        persephoneWhiteRect.centerx = rectPersephoneWhite6.centerx
                        persephoneWhiteRect.centery = rectPersephoneWhite6.centery
                        counter += 1
                        persephoneWhitePlaying=False
                    elif rectPersephoneWhite7.collidepoint(event.pos):
                        persephoneWhiteRect.centerx = rectPersephoneWhite7.centerx
                        persephoneWhiteRect.centery = rectPersephoneWhite7.centery
                        counter += 1
                        persephoneWhitePlaying=False
                    elif rectPersephoneWhite8.collidepoint(event.pos):
                        persephoneWhiteRect.centerx = rectPersephoneWhite8.centerx
                        persephoneWhiteRect.centery = rectPersephoneWhite8.centery
                        counter += 1
                        persephoneWhitePlaying=False
                    elif rectPersephoneWhite9.collidepoint(event.pos):
                        persephoneWhiteRect.centerx = rectPersephoneWhite9.centerx
                        persephoneWhiteRect.centery = rectPersephoneWhite9.centery
                        counter += 1
                        persephoneWhitePlaying=False
                    else:
                        persephoneWhiteRect.centerx = persephoneWhitexInit
                        persephoneWhiteRect.centery = persephoneWhiteyInit
                        persephoneWhitePlaying=False
                    if persephoneWhiteRect.colliderect(plagueDoctorWhiteRect):
                        persephoneWhiteRect.centerx = persephoneWhitexInit
                        persephoneWhiteRect.centery = persephoneWhiteyInit
                        counter -= 1
                        persephoneWhitePlaying=False
                    elif persephoneWhiteRect.colliderect(archbishopWhiteRect):
                        persephoneWhiteRect.centerx = persephoneWhitexInit
                        persephoneWhiteRect.centery = persephoneWhiteyInit
                        counter -= 1
                        persephoneWhitePlaying=False
                    elif persephoneWhiteRect.colliderect(cardinalWhiteRect):
                        persephoneWhiteRect.centerx = persephoneWhitexInit
                        persephoneWhiteRect.centery = persephoneWhiteyInit
                        counter -= 1
                        persephoneWhitePlaying=False
                    elif persephoneWhiteRect.colliderect(hadesWhiteRect):
                        persephoneWhiteRect.centerx = persephoneWhitexInit
                        persephoneWhiteRect.centery = persephoneWhiteyInit
                        counter -= 1
                        persephoneWhitePlaying=False
                    elif persephoneWhiteRect.colliderect(plagueDoctorWhiteRect1):
                        persephoneWhiteRect.centerx = persephoneWhitexInit
                        persephoneWhiteRect.centery = persephoneWhiteyInit
                        counter -= 1
                        persephoneWhitePlaying=False
                    elif persephoneWhiteRect.colliderect(cardinalWhiteRect1):
                        persephoneWhiteRect.centerx = persephoneWhitexInit
                        persephoneWhiteRect.centery = persephoneWhiteyInit
                        counter -= 1
                        persephoneWhitePlaying=False
                    elif persephoneWhiteRect.colliderect(archbishopWhiteRect1):
                        persephoneWhiteRect.centerx = persephoneWhitexInit
                        persephoneWhiteRect.centery = persephoneWhiteyInit
                        counter -= 1
                        persephoneWhitePlaying=False
                    elif persephoneWhiteRect.colliderect(warriorWhiteRect):
                        persephoneWhiteRect.centerx = persephoneWhitexInit
                        persephoneWhiteRect.centery = persephoneWhiteyInit
                        counter -= 1
                        persephoneWhitePlaying=False
                    elif persephoneWhiteRect.colliderect(legionaryWhiteRect):
                        persephoneWhiteRect.centerx = persephoneWhitexInit
                        persephoneWhiteRect.centery = persephoneWhiteyInit
                        counter -= 1
                        persephoneWhitePlaying=False
                    elif persephoneWhiteRect.colliderect(warriorWhiteRect1):
                        persephoneWhiteRect.centerx = persephoneWhitexInit
                        persephoneWhiteRect.centery = persephoneWhiteyInit
                        counter -= 1
                        persephoneWhitePlaying=False
                    elif persephoneWhiteRect.colliderect(legionaryWhiteRect1):
                        persephoneWhiteRect.centerx = persephoneWhitexInit
                        persephoneWhiteRect.centery = persephoneWhiteyInit
                        counter -= 1
                        persephoneWhitePlaying=False
                    elif persephoneWhiteRect.colliderect(warriorWhiteRect2):
                        persephoneWhiteRect.centerx = persephoneWhitexInit
                        persephoneWhiteRect.centery = persephoneWhiteyInit
                        counter -= 1
                        persephoneWhitePlaying=False
                    elif persephoneWhiteRect.colliderect(legionaryWhiteRect2):
                        persephoneWhiteRect.centerx = persephoneWhitexInit
                        persephoneWhiteRect.centery = persephoneWhiteyInit
                        counter -= 1
                        persephoneWhitePlaying=False
                    elif persephoneWhiteRect.colliderect(warriorWhiteRect3):
                        persephoneWhiteRect.centerx = persephoneWhitexInit
                        persephoneWhiteRect.centery = persephoneWhiteyInit
                        counter -= 1
                        persephoneWhitePlaying=False
                    elif persephoneWhiteRect.colliderect(legionaryWhiteRect3):
                        persephoneWhiteRect.centerx = persephoneWhitexInit
                        persephoneWhiteRect.centery = persephoneWhiteyInit
                        counter -= 1
                        persephoneWhitePlaying=False
                     

                if cardinalWhiteRect1.collidepoint(event.pos):
                    if not cardinalWhitePlaying1:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                cardinalWhitePlaying1=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                cardinalWhitePlaying1=True
                elif cardinalWhitePlaying1:
                    if rectCardinalWhite1.collidepoint(event.pos):
                        cardinalWhiteRect1.centerx = rectCardinalWhite1.centerx
                        cardinalWhiteRect1.centery = rectCardinalWhite1.centery
                        counter += 1
                        cardinalWhitePlaying1=False
                    elif rectCardinalWhite2.collidepoint(event.pos):
                        cardinalWhiteRect1.centerx = rectCardinalWhite2.centerx
                        cardinalWhiteRect1.centery = rectCardinalWhite2.centery
                        counter += 1
                        cardinalWhitePlaying1=False
                    elif rectCardinalWhite3.collidepoint(event.pos):
                        cardinalWhiteRect1.centerx = rectCardinalWhite3.centerx
                        cardinalWhiteRect1.centery = rectCardinalWhite3.centery
                        counter += 1
                        cardinalWhitePlaying1=False
                    elif rectCardinalWhite4.collidepoint(event.pos):
                        cardinalWhiteRect1.centerx = rectCardinalWhite4.centerx
                        cardinalWhiteRect1.centery = rectCardinalWhite4.centery
                        counter += 1
                        cardinalWhitePlaying1=False
                    else:
                        cardinalWhiteRect1.centerx = cardinalWhitexInit1
                        cardinalWhiteRect1.centery = cardinalWhiteyInit1
                        cardinalWhitePlaying1=False
                    if cardinalWhiteRect1.colliderect(plagueDoctorWhiteRect):
                        cardinalWhiteRect1.centerx = cardinalWhitexInit1
                        cardinalWhiteRect1.centery = cardinalWhiteyInit1
                        counter -= 1
                        cardinalWhitePlaying1=False
                    elif cardinalWhiteRect1.colliderect(archbishopWhiteRect):
                        cardinalWhiteRect1.centerx = cardinalWhitexInit1
                        cardinalWhiteRect1.centery = cardinalWhiteyInit1
                        counter -= 1
                        cardinalWhitePlaying1=False
                    elif cardinalWhiteRect1.colliderect(cardinalWhiteRect):
                        cardinalWhiteRect1.centerx = cardinalWhitexInit1
                        cardinalWhiteRect1.centery = cardinalWhiteyInit1
                        counter -= 1
                        cardinalWhitePlaying1=False
                    elif cardinalWhiteRect1.colliderect(hadesWhiteRect):
                        cardinalWhiteRect1.centerx = cardinalWhitexInit1
                        cardinalWhiteRect1.centery = cardinalWhiteyInit1
                        counter -= 1
                        cardinalWhitePlaying1=False
                    elif cardinalWhiteRect1.colliderect(plagueDoctorWhiteRect1):
                        cardinalWhiteRect1.centerx = cardinalWhitexInit1
                        cardinalWhiteRect1.centery = cardinalWhiteyInit1
                        counter -= 1
                        cardinalWhitePlaying1=False
                    elif cardinalWhiteRect1.colliderect(persephoneWhiteRect):
                        cardinalWhiteRect1.centerx = cardinalWhitexInit1
                        cardinalWhiteRect1.centery = cardinalWhiteyInit1
                        counter -= 1
                        cardinalWhitePlaying1=False
                    elif cardinalWhiteRect1.colliderect(archbishopWhiteRect1):
                        cardinalWhiteRect1.centerx = cardinalWhitexInit1
                        cardinalWhiteRect1.centery = cardinalWhiteyInit1
                        counter -= 1
                        cardinalWhitePlaying1=False
                    elif cardinalWhiteRect1.colliderect(warriorWhiteRect):
                        cardinalWhiteRect1.centerx = cardinalWhitexInit1
                        cardinalWhiteRect1.centery = cardinalWhiteyInit1
                        counter -= 1
                        cardinalWhitePlaying1=False
                    elif cardinalWhiteRect1.colliderect(legionaryWhiteRect):
                        cardinalWhiteRect1.centerx = cardinalWhitexInit1
                        cardinalWhiteRect1.centery = cardinalWhiteyInit1
                        counter -= 1
                        cardinalWhitePlaying1=False
                    elif cardinalWhiteRect1.colliderect(warriorWhiteRect1):
                        cardinalWhiteRect1.centerx = cardinalWhitexInit1
                        cardinalWhiteRect1.centery = cardinalWhiteyInit1
                        counter -= 1
                        cardinalWhitePlaying1=False
                    elif cardinalWhiteRect1.colliderect(legionaryWhiteRect1):
                        cardinalWhiteRect1.centerx = cardinalWhitexInit1
                        cardinalWhiteRect1.centery = cardinalWhiteyInit1
                        counter -= 1
                        cardinalWhitePlaying1=False
                    elif cardinalWhiteRect1.colliderect(warriorWhiteRect2):
                        cardinalWhiteRect1.centerx = cardinalWhitexInit1
                        cardinalWhiteRect1.centery = cardinalWhiteyInit1
                        counter -= 1
                        cardinalWhitePlaying1=False
                    elif cardinalWhiteRect1.colliderect(legionaryWhiteRect2):
                        cardinalWhiteRect1.centerx = cardinalWhitexInit1
                        cardinalWhiteRect1.centery = cardinalWhiteyInit1
                        counter -= 1
                        cardinalWhitePlaying1=False
                    elif cardinalWhiteRect1.colliderect(warriorWhiteRect3):
                        cardinalWhiteRect1.centerx = cardinalWhitexInit1
                        cardinalWhiteRect1.centery = cardinalWhiteyInit1
                        counter -= 1
                        cardinalWhitePlaying1=False
                    elif cardinalWhiteRect1.colliderect(legionaryWhiteRect3):
                        cardinalWhiteRect1.centerx = cardinalWhitexInit1
                        cardinalWhiteRect1.centery = cardinalWhiteyInit1
                        counter -= 1
                        cardinalWhitePlaying1=False

                if archbishopWhiteRect1.collidepoint(event.pos):
                    if not archbishopWhitePlaying1:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                archbishopWhitePlaying1=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                archbishopWhitePlaying1=True
                elif archbishopWhitePlaying1:
                    if rectArchbishopWhite1.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite1.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite1.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite2.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite2.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite2.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite3.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite3.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite3.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite4.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite4.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite4.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite5.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite5.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite5.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite6.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite6.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite6.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite7.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite7.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite7.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite8.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite8.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite8.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite9.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite9.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite9.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite10.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite10.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite10.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite11.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite11.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite11.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite12.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite12.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite12.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    else:
                        archbishopWhiteRect1.centerx = archbishopWhitexInit1
                        archbishopWhiteRect1.centery = archbishopWhiteyInit1
                        archbishopWhitePlaying1=False
                    if archbishopWhiteRect1.colliderect(plagueDoctorWhiteRect):
                        archbishopWhiteRect1.centerx = archbishopWhitexInit1
                        archbishopWhiteRect1.centery = archbishopWhiteyInit1
                        counter -= 1
                        archbishopWhitePlaying1=False
                    elif archbishopWhiteRect1.colliderect(archbishopWhiteRect):
                        archbishopWhiteRect1.centerx = archbishopWhitexInit1
                        archbishopWhiteRect1.centery = archbishopWhiteyInit1
                        counter -= 1
                        archbishopWhitePlaying1=False
                    elif archbishopWhiteRect1.colliderect(cardinalWhiteRect):
                        archbishopWhiteRect1.centerx = archbishopWhitexInit1
                        archbishopWhiteRect1.centery = archbishopWhiteyInit1
                        counter -= 1
                        archbishopWhitePlaying1=False
                    elif archbishopWhiteRect1.colliderect(hadesWhiteRect):
                        archbishopWhiteRect1.centerx = archbishopWhitexInit1
                        archbishopWhiteRect1.centery = archbishopWhiteyInit1
                        counter -= 1
                        archbishopWhitePlaying1=False
                    elif archbishopWhiteRect1.colliderect(plagueDoctorWhiteRect1):
                        archbishopWhiteRect1.centerx = archbishopWhitexInit1
                        archbishopWhiteRect1.centery = archbishopWhiteyInit1
                        counter -= 1
                        archbishopWhitePlaying1=False
                    elif archbishopWhiteRect1.colliderect(persephoneWhiteRect):
                        archbishopWhiteRect1.centerx = archbishopWhitexInit1
                        archbishopWhiteRect1.centery = archbishopWhiteyInit1
                        counter -= 1
                        archbishopWhitePlaying1=False
                    elif archbishopWhiteRect1.colliderect(cardinalWhiteRect1):
                        archbishopWhiteRect1.centerx = archbishopWhitexInit1
                        archbishopWhiteRect1.centery = archbishopWhiteyInit1
                        counter -= 1
                        archbishopWhitePlaying1=False
                    elif archbishopWhiteRect1.colliderect(warriorWhiteRect):
                        archbishopWhiteRect1.centerx = archbishopWhitexInit1
                        archbishopWhiteRect1.centery = archbishopWhiteyInit1
                        counter -= 1
                        archbishopWhitePlaying1=False
                    elif archbishopWhiteRect1.colliderect(legionaryWhiteRect):
                        archbishopWhiteRect1.centerx = archbishopWhitexInit1
                        archbishopWhiteRect1.centery = archbishopWhiteyInit1
                        counter -= 1
                        archbishopWhitePlaying1=False
                    elif archbishopWhiteRect1.colliderect(warriorWhiteRect1):
                        archbishopWhiteRect1.centerx = archbishopWhitexInit1
                        archbishopWhiteRect1.centery = archbishopWhiteyInit1
                        counter -= 1
                        archbishopWhitePlaying1=False
                    elif archbishopWhiteRect1.colliderect(legionaryWhiteRect1):
                        archbishopWhiteRect1.centerx = archbishopWhitexInit1
                        archbishopWhiteRect1.centery = archbishopWhiteyInit1
                        counter -= 1
                        archbishopWhitePlaying1=False
                    elif archbishopWhiteRect1.colliderect(warriorWhiteRect2):
                        archbishopWhiteRect1.centerx = archbishopWhitexInit1
                        archbishopWhiteRect1.centery = archbishopWhiteyInit1
                        counter -= 1
                        archbishopWhitePlaying1=False
                    elif archbishopWhiteRect1.colliderect(legionaryWhiteRect2):
                        archbishopWhiteRect1.centerx = archbishopWhitexInit1
                        archbishopWhiteRect1.centery = archbishopWhiteyInit1
                        counter -= 1
                        archbishopWhitePlaying1=False
                    elif archbishopWhiteRect1.colliderect(warriorWhiteRect3):
                        archbishopWhiteRect1.centerx = archbishopWhitexInit1
                        archbishopWhiteRect1.centery = archbishopWhiteyInit1
                        counter -= 1
                        archbishopWhitePlaying1=False
                    elif archbishopWhiteRect1.colliderect(legionaryWhiteRect3):
                        archbishopWhiteRect1.centerx = archbishopWhitexInit1
                        archbishopWhiteRect1.centery = archbishopWhiteyInit1
                        counter -= 1
                        archbishopWhitePlaying1=False


                if plagueDoctorWhiteRect1.collidepoint(event.pos):
                    if not plagueDoctorWhitePlaying1:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                plagueDoctorWhitePlaying1=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                plagueDoctorWhitePlaying1=True
                elif plagueDoctorWhitePlaying1:
                    if rectPlagueWhite1_1.collidepoint(event.pos):
                        plagueDoctorWhiteRect1.centerx = rectPlagueWhite1_1.centerx
                        plagueDoctorWhiteRect1.centery = rectPlagueWhite1_1.centery
                        counter += 1
                        plagueDoctorWhitePlaying1=False
                    elif rectPlagueWhite2_1.collidepoint(event.pos):
                        plagueDoctorWhiteRect1.centerx = rectPlagueWhite2_1.centerx
                        plagueDoctorWhiteRect1.centery = rectPlagueWhite2_1.centery
                        counter += 1
                        plagueDoctorWhitePlaying1=False
                    elif rectPlagueWhite3_1.collidepoint(event.pos):
                        plagueDoctorWhiteRect1.centerx = rectPlagueWhite3_1.centerx
                        plagueDoctorWhiteRect1.centery = rectPlagueWhite3_1.centery
                        counter += 1
                        plagueDoctorWhitePlaying1=False
                    elif rectPlagueWhite4_1.collidepoint(event.pos):
                        plagueDoctorWhiteRect1.centerx = rectPlagueWhite4_1.centerx
                        plagueDoctorWhiteRect1.centery = rectPlagueWhite4_1.centery
                        counter += 1
                        plagueDoctorWhitePlaying1=False
                    elif rectPlagueWhite5_1.collidepoint(event.pos):
                        plagueDoctorWhiteRect1.centerx = rectPlagueWhite5_1.centerx
                        plagueDoctorWhiteRect1.centery = rectPlagueWhite5_1.centery
                        counter += 1
                        plagueDoctorWhitePlaying1=False
                    elif rectPlagueWhite6_1.collidepoint(event.pos):
                        plagueDoctorWhiteRect1.centerx = rectPlagueWhite6_1.centerx
                        plagueDoctorWhiteRect1.centery = rectPlagueWhite6_1.centery
                        counter += 1
                        plagueDoctorWhitePlaying1=False
                    elif rectPlagueWhite7_1.collidepoint(event.pos):
                        plagueDoctorWhiteRect1.centerx = rectPlagueWhite7_1.centerx
                        plagueDoctorWhiteRect1.centery = rectPlagueWhite7_1.centery
                        counter += 1
                        plagueDoctorWhitePlaying1=False
                    elif rectPlagueWhite8_1.collidepoint(event.pos):
                        plagueDoctorWhiteRect1.centerx = rectPlagueWhite8_1.centerx
                        plagueDoctorWhiteRect1.centery = rectPlagueWhite8_1.centery
                        counter += 1
                        plagueDoctorWhitePlaying1=False
                    elif rectPlagueWhite9_1.collidepoint(event.pos):
                        plagueDoctorWhiteRect1.centerx = rectPlagueWhite9_1.centerx
                        plagueDoctorWhiteRect1.centery = rectPlagueWhite9_1.centery
                        counter += 1
                        plagueDoctorWhitePlaying1=False
                    elif rectPlagueWhite10_1.collidepoint(event.pos):
                        plagueDoctorWhiteRect1.centerx = rectPlagueWhite10_1.centerx
                        plagueDoctorWhiteRect1.centery = rectPlagueWhite10_1.centery
                        counter += 1
                        plagueDoctorWhitePlaying1=False
                    elif rectPlagueWhite11_1.collidepoint(event.pos):
                        plagueDoctorWhiteRect1.centerx = rectPlagueWhite11_1.centerx
                        plagueDoctorWhiteRect1.centery = rectPlagueWhite11_1.centery
                        counter += 1
                        plagueDoctorWhitePlaying1=False
                    elif rectPlagueWhite12_1.collidepoint(event.pos):
                        plagueDoctorWhiteRect1.centerx = rectPlagueWhite12_1.centerx
                        plagueDoctorWhiteRect1.centery = rectPlagueWhite12_1.centery
                        counter += 1
                        plagueDoctorWhitePlaying1=False
                    elif rectPlagueWhite13_1.collidepoint(event.pos):
                        plagueDoctorWhiteRect1.centerx = rectPlagueWhite13_1.centerx
                        plagueDoctorWhiteRect1.centery = rectPlagueWhite13_1.centery
                        counter += 1
                        plagueDoctorWhitePlaying1=False
                    elif rectPlagueWhite14_1.collidepoint(event.pos):
                        plagueDoctorWhiteRect1.centerx = rectPlagueWhite14_1.centerx
                        plagueDoctorWhiteRect1.centery = rectPlagueWhite14_1.centery
                        counter += 1
                        plagueDoctorWhitePlaying1=False
                    elif rectPlagueWhite15_1.collidepoint(event.pos):
                        plagueDoctorWhiteRect1.centerx = rectPlagueWhite15_1.centerx
                        plagueDoctorWhiteRect1.centery = rectPlagueWhite15_1.centery
                        counter += 1
                        plagueDoctorWhitePlaying1=False
                    elif rectPlagueWhite16_1.collidepoint(event.pos):
                        plagueDoctorWhiteRect1.centerx = rectPlagueWhite16_1.centerx
                        plagueDoctorWhiteRect1.centery = rectPlagueWhite16_1.centery
                        counter += 1
                        plagueDoctorWhitePlaying1=False
                    elif rectPlagueWhite17_1.collidepoint(event.pos):
                        plagueDoctorWhiteRect1.centerx = rectPlagueWhite17_1.centerx
                        plagueDoctorWhiteRect1.centery = rectPlagueWhite17_1.centery
                        counter += 1
                        plagueDoctorWhitePlaying1=False
                    elif rectPlagueWhite18_1.collidepoint(event.pos):
                        plagueDoctorWhiteRect1.centerx = rectPlagueWhite18_1.centerx
                        plagueDoctorWhiteRect1.centery = rectPlagueWhite18_1.centery
                        counter += 1
                        plagueDoctorWhitePlaying1=False
                    else:
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                    if plagueDoctorWhiteRect1.colliderect(plagueDoctorWhiteRect):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                    elif plagueDoctorWhiteRect1.colliderect(archbishopWhiteRect):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                    elif plagueDoctorWhiteRect1.colliderect(cardinalWhiteRect):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                    elif plagueDoctorWhiteRect1.colliderect(hadesWhiteRect):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                    elif plagueDoctorWhiteRect1.colliderect(cardinalWhiteRect1):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                    elif plagueDoctorWhiteRect1.colliderect(persephoneWhiteRect):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                    elif plagueDoctorWhiteRect1.colliderect(archbishopWhiteRect1):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                    elif plagueDoctorWhiteRect1.colliderect(warriorWhiteRect):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                    elif plagueDoctorWhiteRect1.colliderect(legionaryWhiteRect):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                    elif plagueDoctorWhiteRect1.colliderect(warriorWhiteRect1):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                    elif plagueDoctorWhiteRect1.colliderect(legionaryWhiteRect1):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                    elif plagueDoctorWhiteRect1.colliderect(warriorWhiteRect2):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                    elif plagueDoctorWhiteRect1.colliderect(legionaryWhiteRect2):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                    elif plagueDoctorWhiteRect1.colliderect(warriorWhiteRect3):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                    elif plagueDoctorWhiteRect1.colliderect(legionaryWhiteRect3):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1




                if warriorWhiteRect.collidepoint(event.pos):
                    if not warriorWhitePlaying:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                warriorWhitePlaying=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                warriorWhitePlaying=True
                elif warriorWhitePlaying:
                    if rectWarriorWhite1Ability.collidepoint(event.pos) and counter % 4 == 0:
                        warriorWhiteRect.centerx = rectWarriorWhite1Ability.centerx
                        warriorWhiteRect.centery = rectWarriorWhite1Ability.centery
                        counter += 1
                        warriorWhitePlaying=False
                    elif rectWarriorWhite2Ability.collidepoint(event.pos) and counter % 4 == 0:
                        warriorWhiteRect.centerx = rectWarriorWhite2Ability.centerx
                        warriorWhiteRect.centery = rectWarriorWhite2Ability.centery
                        counter += 1
                        warriorWhitePlaying=False
                    elif rectWarriorWhite3Ability.collidepoint(event.pos) and counter % 4 == 0:
                        warriorWhiteRect.centerx = rectWarriorWhite3Ability.centerx
                        warriorWhiteRect.centery = rectWarriorWhite3Ability.centery
                        counter += 1
                        warriorWhitePlaying=False
                    elif rectWarriorWhite4Ability.collidepoint(event.pos) and counter % 4 == 0:
                        warriorWhiteRect.centerx = rectWarriorWhite4Ability.centerx
                        warriorWhiteRect.centery = rectWarriorWhite4Ability.centery
                        counter += 1
                        warriorWhitePlaying=False
                    elif rectWarriorWhite1.collidepoint(event.pos):
                        warriorWhiteRect.centerx = rectWarriorWhite1.centerx
                        warriorWhiteRect.centery = rectWarriorWhite1.centery
                        counter += 1
                        warriorWhitePlaying=False
                    elif rectWarriorWhite2.collidepoint(event.pos):
                        warriorWhiteRect.centerx = rectWarriorWhite2.centerx
                        warriorWhiteRect.centery = rectWarriorWhite2.centery
                        counter += 1
                        warriorWhitePlaying=False
                    elif rectWarriorWhite3.collidepoint(event.pos):
                        warriorWhiteRect.centerx = rectWarriorWhite3.centerx
                        warriorWhiteRect.centery = rectWarriorWhite3.centery
                        counter += 1
                        warriorWhitePlaying=False
                    elif rectWarriorWhite4.collidepoint(event.pos):
                        warriorWhiteRect.centerx = rectWarriorWhite4.centerx
                        warriorWhiteRect.centery = rectWarriorWhite4.centery
                        counter += 1
                        warriorWhitePlaying=False
                    else:
                        warriorWhiteRect.centerx = warriorWhitexInit
                        warriorWhiteRect.centery = warriorWhiteyInit
                        warriorWhitePlaying=False
                    if warriorWhiteRect.colliderect(plagueDoctorWhiteRect):
                        warriorWhiteRect.centerx = warriorWhitexInit
                        warriorWhiteRect.centery = warriorWhiteyInit
                        counter -= 1
                        warriorWhitePlaying=False
                    elif warriorWhiteRect.colliderect(archbishopWhiteRect):
                        warriorWhiteRect.centerx = warriorWhitexInit
                        warriorWhiteRect.centery = warriorWhiteyInit
                        counter -= 1
                        warriorWhitePlaying=False
                    elif warriorWhiteRect.colliderect(cardinalWhiteRect):
                        warriorWhiteRect.centerx = warriorWhitexInit
                        warriorWhiteRect.centery = warriorWhiteyInit
                        counter -= 1
                        warriorWhitePlaying=False
                    elif warriorWhiteRect.colliderect(hadesWhiteRect):
                        warriorWhiteRect.centerx = warriorWhitexInit
                        warriorWhiteRect.centery = warriorWhiteyInit
                        counter -= 1
                        warriorWhitePlaying=False
                    elif warriorWhiteRect.colliderect(cardinalWhiteRect1):
                        warriorWhiteRect.centerx = warriorWhitexInit
                        warriorWhiteRect.centery = warriorWhiteyInit
                        counter -= 1
                        warriorWhitePlaying=False
                    elif warriorWhiteRect.colliderect(persephoneWhiteRect):
                        warriorWhiteRect.centerx = warriorWhitexInit
                        warriorWhiteRect.centery = warriorWhiteyInit
                        counter -= 1
                        warriorWhitePlaying=False
                    elif warriorWhiteRect.colliderect(archbishopWhiteRect1):
                        warriorWhiteRect.centerx = warriorWhitexInit
                        warriorWhiteRect.centery = warriorWhiteyInit
                        counter -= 1
                        warriorWhitePlaying=False
                    elif warriorWhiteRect.colliderect(plagueDoctorWhiteRect1):
                        warriorWhiteRect.centerx = warriorWhitexInit
                        warriorWhiteRect.centery = warriorWhiteyInit
                        counter -= 1
                        warriorWhitePlaying=False
                    elif warriorWhiteRect.colliderect(legionaryWhiteRect):
                        warriorWhiteRect.centerx = warriorWhitexInit
                        warriorWhiteRect.centery = warriorWhiteyInit
                        counter -= 1
                        warriorWhitePlaying=False
                    elif warriorWhiteRect.colliderect(warriorWhiteRect1):
                        warriorWhiteRect.centerx = warriorWhitexInit
                        warriorWhiteRect.centery = warriorWhiteyInit
                        counter -= 1
                        warriorWhitePlaying=False
                    elif warriorWhiteRect.colliderect(legionaryWhiteRect1):
                        warriorWhiteRect.centerx = warriorWhitexInit
                        warriorWhiteRect.centery = warriorWhiteyInit
                        counter -= 1
                        warriorWhitePlaying=False
                    elif warriorWhiteRect.colliderect(warriorWhiteRect2):
                        warriorWhiteRect.centerx = warriorWhitexInit
                        warriorWhiteRect.centery = warriorWhiteyInit
                        counter -= 1
                        warriorWhitePlaying=False
                    elif warriorWhiteRect.colliderect(legionaryWhiteRect2):
                        warriorWhiteRect.centerx = warriorWhitexInit
                        warriorWhiteRect.centery = warriorWhiteyInit
                        counter -= 1
                        warriorWhitePlaying=False
                    elif warriorWhiteRect.colliderect(warriorWhiteRect3):
                        warriorWhiteRect.centerx = warriorWhitexInit
                        warriorWhiteRect.centery = warriorWhiteyInit
                        counter -= 1
                        warriorWhitePlaying=False
                    elif warriorWhiteRect.colliderect(legionaryWhiteRect3):
                        warriorWhiteRect.centerx = warriorWhitexInit
                        warriorWhiteRect.centery = warriorWhiteyInit
                        counter -= 1
                        warriorWhitePlaying=False
                            



                if legionaryWhiteRect.collidepoint(event.pos):
                    if not legionaryWhitePlaying:
                            for x,playing in enumerate(figuresWhitePlaying):
                                if playing==True:
                                    playing=False
                                    legionaryWhitePlaying=True
                                    break
                                elif x==len(figuresWhitePlaying)-1:
                                    legionaryWhitePlaying=True
                elif legionaryWhitePlaying:
                    if rectLegionaryWhite1.collidepoint(event.pos):
                        rectLegionaryWhitex1_1 = legionaryWhitexInit1
                        rectLegionaryWhitey1_1 = legionaryWhiteyInit1
                        legionaryWhiteRect1.centerx = rectLegionaryWhite1.centerx
                        legionaryWhiteRect1.centery = rectLegionaryWhite1.centery
                        counter += 1
                        legionaryWhitePlaying=False
                    elif rectLegionaryWhite2.collidepoint(event.pos):
                        rectLegionaryWhitex1_1 = legionaryWhitexInit1
                        rectLegionaryWhitey1_1 = legionaryWhitexInit1
                        legionaryWhiteRect1.centerx = rectLegionaryWhite2.centerx
                        legionaryWhiteRect1.centery = rectLegionaryWhite2.centery
                        counter += 1
                        legionaryWhitePlaying=False
                    elif rectLegionaryWhite3.collidepoint(event.pos):
                        legionar_bily_x_abilita_1 = legionaryWhitexInit1
                        legionar_bily_y_abilita_1 = legionaryWhiteyInit1
                        legionaryWhiteRect1.centerx = rectLegionaryWhite3.centerx
                        legionaryWhiteRect1.centery = rectLegionaryWhite3.centery
                        counter += 1
                        legionaryWhitePlaying=False
                    else:
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        legionaryWhitePlaying=False
                    if legionaryWhiteRect1.colliderect(plagueDoctorWhiteRect):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect1.colliderect(archbishopWhiteRect):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect1.colliderect(cardinalWhiteRect):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect1.colliderect(hadesWhiteRect):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect1.colliderect(cardinalWhiteRect1):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect1.colliderect(persephoneWhiteRect):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect1.colliderect(archbishopWhiteRect1):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect1.colliderect(plagueDoctorWhiteRect1):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect1.colliderect(warriorWhiteRect):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect1.colliderect(legionaryWhiteRect):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect1.colliderect(warriorWhiteRect1):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect1.colliderect(warriorWhiteRect2):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect1.colliderect(legionaryWhiteRect2):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect1.colliderect(warriorWhiteRect3):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect1.colliderect(legionaryWhiteRect3):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying=False
                       


                if warriorWhiteRect1.collidepoint(event.pos):
                    if not warriorWhitePlaying1:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                warriorWhitePlaying1=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                warriorWhitePlaying1=True
                elif warriorWhitePlaying1:
                    if rectWarriorWhite1_1Ability.collidepoint(event.pos) and counter % 4 == 0:
                        warriorWhiteRect1.centerx = rectWarriorWhite1_1Ability.centerx
                        warriorWhiteRect1.centery = rectWarriorWhite1_1Ability.centery
                        counter += 1
                        warriorWhitePlaying1=False
                    elif rectWarriorWhite2_1Ability.collidepoint(event.pos) and counter % 4 == 0:
                        warriorWhiteRect1.centerx = rectWarriorWhite2_1Ability.centerx
                        warriorWhiteRect1.centery = rectWarriorWhite2_1Ability.centery
                        counter += 1
                        warriorWhitePlaying1=False
                    elif rectWarriorWhite3_1Ability.collidepoint(event.pos) and counter % 4 == 0:
                        warriorWhiteRect1.centerx = rectWarriorWhite3_1Ability.centerx
                        warriorWhiteRect1.centery = rectWarriorWhite3_1Ability.centery
                        counter += 1
                        warriorWhitePlaying1=False
                    elif rectWarriorWhite4_1Ability.collidepoint(event.pos) and counter % 4 == 0:
                        warriorWhiteRect1.centerx = rectWarriorWhite4_1Ability.centerx
                        warriorWhiteRect1.centery = rectWarriorWhite4_1Ability.centery
                        counter += 1
                        warriorWhitePlaying1=False
                    elif rectWarriorWhite1_1.collidepoint(event.pos):
                        warriorWhiteRect1.centerx = rectWarriorWhite1_1.centerx
                        warriorWhiteRect1.centery = rectWarriorWhite1_1.centery
                        counter += 1
                        warriorWhitePlaying1=False
                    elif rectWarriorWhite2_1.collidepoint(event.pos):
                        warriorWhiteRect1.centerx = rectWarriorWhite2_1.centerx
                        warriorWhiteRect1.centery = rectWarriorWhite2_1.centery
                        counter += 1
                        warriorWhitePlaying1=False
                    elif rectWarriorWhite3_1.collidepoint(event.pos):
                        warriorWhiteRect1.centerx = rectWarriorWhite3_1.centerx
                        warriorWhiteRect1.centery = rectWarriorWhite3_1.centery
                        counter += 1
                        warriorWhitePlaying1=False
                    elif rectWarriorWhite4_1.collidepoint(event.pos):
                        warriorWhiteRect1.centerx = rectWarriorWhite4_1.centerx
                        warriorWhiteRect1.centery = rectWarriorWhite4_1.centery
                        counter += 1
                        warriorWhitePlaying1=False
                    else:
                        warriorWhiteRect1.centerx = warriorWhitexInit1
                        warriorWhiteRect1.centery = warriorWhiteyInit1
                        warriorWhitePlaying1=False
                    if warriorWhiteRect1.colliderect(plagueDoctorWhiteRect):
                        warriorWhiteRect1.centerx = warriorWhitexInit1
                        warriorWhiteRect1.centery = warriorWhiteyInit1
                        counter -= 1
                        warriorWhitePlaying1=False
                    elif warriorWhiteRect1.colliderect(archbishopWhiteRect):
                        warriorWhiteRect1.centerx = warriorWhitexInit1
                        warriorWhiteRect1.centery = warriorWhiteyInit1
                        counter -= 1
                        warriorWhitePlaying1=False
                    elif warriorWhiteRect1.colliderect(cardinalWhiteRect):
                        warriorWhiteRect1.centerx = warriorWhitexInit1
                        warriorWhiteRect1.centery = warriorWhiteyInit1
                        counter -= 1
                        warriorWhitePlaying1=False
                    elif warriorWhiteRect1.colliderect(hadesWhiteRect):
                        warriorWhiteRect1.centerx = warriorWhitexInit1
                        warriorWhiteRect1.centery = warriorWhiteyInit1
                        counter -= 1
                        warriorWhitePlaying1=False
                    elif warriorWhiteRect1.colliderect(cardinalWhiteRect1):
                        warriorWhiteRect1.centerx = warriorWhitexInit1
                        warriorWhiteRect1.centery = warriorWhiteyInit1
                        counter -= 1
                        warriorWhitePlaying1=False
                    elif warriorWhiteRect1.colliderect(persephoneWhiteRect):
                        warriorWhiteRect1.centerx = warriorWhitexInit1
                        warriorWhiteRect1.centery = warriorWhiteyInit1
                        counter -= 1
                        warriorWhitePlaying1=False
                    elif warriorWhiteRect1.colliderect(archbishopWhiteRect1):
                        warriorWhiteRect1.centerx = warriorWhitexInit1
                        warriorWhiteRect1.centery = warriorWhiteyInit1
                        counter -= 1
                        warriorWhitePlaying1=False
                    elif warriorWhiteRect1.colliderect(plagueDoctorWhiteRect1):
                        warriorWhiteRect1.centerx = warriorWhitexInit1
                        warriorWhiteRect1.centery = warriorWhiteyInit1
                        counter -= 1
                        warriorWhitePlaying1=False
                    elif warriorWhiteRect1.colliderect(warriorWhiteRect):
                        warriorWhiteRect1.centerx = warriorWhitexInit1
                        warriorWhiteRect1.centery = warriorWhiteyInit1
                        counter -= 1
                        warriorWhitePlaying1=False
                    elif warriorWhiteRect1.colliderect(legionaryWhiteRect):
                        warriorWhiteRect1.centerx = warriorWhitexInit1
                        warriorWhiteRect1.centery = warriorWhiteyInit1
                        counter -= 1
                        warriorWhitePlaying1=False
                    elif warriorWhiteRect1.colliderect(legionaryWhiteRect1):
                        warriorWhiteRect1.centerx = warriorWhitexInit1
                        warriorWhiteRect1.centery = warriorWhiteyInit1
                        counter -= 1
                        warriorWhitePlaying1=False
                    elif warriorWhiteRect1.colliderect(warriorWhiteRect2):
                        warriorWhiteRect1.centerx = warriorWhitexInit1
                        warriorWhiteRect1.centery = warriorWhiteyInit1
                        counter -= 1
                        warriorWhitePlaying1=False
                    elif warriorWhiteRect1.colliderect(legionaryWhiteRect2):
                        warriorWhiteRect1.centerx = warriorWhitexInit1
                        warriorWhiteRect1.centery = warriorWhiteyInit1
                        counter -= 1
                        warriorWhitePlaying1=False
                    elif warriorWhiteRect1.colliderect(warriorWhiteRect3):
                        warriorWhiteRect1.centerx = warriorWhitexInit1
                        warriorWhiteRect1.centery = warriorWhiteyInit1
                        counter -= 1
                        warriorWhitePlaying1=False
                    elif warriorWhiteRect1.colliderect(legionaryWhiteRect3):
                        warriorWhiteRect1.centerx = warriorWhitexInit1
                        warriorWhiteRect1.centery = warriorWhiteyInit1
                        counter -= 1
                        warriorWhitePlaying1=False

                if legionaryWhiteRect1.collidepoint(event.pos):
                    if not legionaryWhitePlaying1:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                legionaryWhitePlaying1=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                legionaryWhitePlaying1=True
                elif legionaryWhitePlaying1:
                    if rectLegionaryWhite1_1.collidepoint(event.pos):
                        rectLegionaryWhitex1_1 = legionaryWhitexInit1
                        rectLegionaryWhitey1_1 = legionaryWhiteyInit1
                        legionaryWhiteRect1.centerx = rectLegionaryWhite1_1.centerx
                        legionaryWhiteRect1.centery = rectLegionaryWhite1_1.centery
                        counter += 1
                        legionaryWhitePlaying1=False
                    elif rectLegionaryWhite2_1.collidepoint(event.pos):
                        rectLegionaryWhitex1_1 = legionaryWhitexInit1
                        rectLegionaryWhitey1_1 = legionaryWhitexInit1
                        legionaryWhiteRect1.centerx = rectLegionaryWhite2_1.centerx
                        legionaryWhiteRect1.centery = rectLegionaryWhite2_1.centery
                        counter += 1
                        legionaryWhitePlaying1=False
                    elif rectLegionaryWhite3_1.collidepoint(event.pos):
                        legionar_bily_x_abilita_1 = legionaryWhitexInit1
                        legionar_bily_y_abilita_1 = legionaryWhiteyInit1
                        legionaryWhiteRect1.centerx = rectLegionaryWhite3_1.centerx
                        legionaryWhiteRect1.centery = rectLegionaryWhite3_1.centery
                        counter += 1
                        legionaryWhitePlaying1=False
                    else:
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        legionaryWhitePlaying1=False
                    if legionaryWhiteRect1.colliderect(plagueDoctorWhiteRect):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying1=False
                    elif legionaryWhiteRect1.colliderect(archbishopWhiteRect):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying1=False
                    elif legionaryWhiteRect1.colliderect(cardinalWhiteRect):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying1=False
                    elif legionaryWhiteRect1.colliderect(hadesWhiteRect):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying1=False
                    elif legionaryWhiteRect1.colliderect(cardinalWhiteRect1):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying1=False
                    elif legionaryWhiteRect1.colliderect(persephoneWhiteRect):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying1=False
                    elif legionaryWhiteRect1.colliderect(archbishopWhiteRect1):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying1=False
                    elif legionaryWhiteRect1.colliderect(plagueDoctorWhiteRect1):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying1=False
                    elif legionaryWhiteRect1.colliderect(warriorWhiteRect):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying1=False
                    elif legionaryWhiteRect1.colliderect(legionaryWhiteRect):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying1=False
                    elif legionaryWhiteRect1.colliderect(warriorWhiteRect1):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying1=False
                    elif legionaryWhiteRect1.colliderect(warriorWhiteRect2):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying1=False
                    elif legionaryWhiteRect1.colliderect(legionaryWhiteRect2):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying1=False
                    elif legionaryWhiteRect1.colliderect(warriorWhiteRect3):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying1=False
                    elif legionaryWhiteRect1.colliderect(legionaryWhiteRect3):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        counter -= 1
                        legionaryWhitePlaying1=False
                    

                if warriorWhiteRect2.collidepoint(event.pos):
                    if not warriorWhitePlaying2:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                warriorWhitePlaying2=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                warriorWhitePlaying2=True
                elif warriorWhitePlaying2:
                    if rectWarriorWhite1_2Ability.collidepoint(event.pos) and counter % 4 == 0:
                        warriorWhiteRect2.centerx = rectWarriorWhite1_2Ability.centerx
                        warriorWhiteRect2.centery = rectWarriorWhite1_2Ability.centery
                        counter += 1
                        warriorWhitePlaying2=False
                    elif rectWarriorWhite2_2Ability.collidepoint(event.pos) and counter % 4 == 0:
                        warriorWhiteRect2.centerx = rectWarriorWhite2_2Ability.centerx
                        warriorWhiteRect2.centery = rectWarriorWhite2_2Ability.centery
                        counter += 1
                        warriorWhitePlaying2=False
                    elif rectWarriorWhite3_2Ability.collidepoint(event.pos) and counter % 4 == 0:
                        warriorWhiteRect2.centerx = rectWarriorWhite3_2Ability.centerx
                        warriorWhiteRect2.centery = rectWarriorWhite3_2Ability.centery
                        counter += 1
                        warriorWhitePlaying2=False
                    elif rectWarriorWhite4_2Ability.collidepoint(event.pos) and counter % 4 == 0:
                        warriorWhiteRect2.centerx = rectWarriorWhite4_2Ability.centerx
                        warriorWhiteRect2.centery = rectWarriorWhite4_2Ability.centery
                        counter += 1
                        warriorWhitePlaying2=False
                    elif rectWarriorWhite1_2.collidepoint(event.pos):
                        warriorWhiteRect2.centerx = rectWarriorWhite1_2.centerx
                        warriorWhiteRect2.centery = rectWarriorWhite1_2.centery
                        counter += 1
                        warriorWhitePlaying2=False
                    elif rectWarriorWhite2_2.collidepoint(event.pos):
                        warriorWhiteRect2.centerx = rectWarriorWhite2_2.centerx
                        warriorWhiteRect2.centery = rectWarriorWhite2_2.centery
                        counter += 1
                        warriorWhitePlaying2=False
                    elif rectWarriorWhite3_2.collidepoint(event.pos):
                        warriorWhiteRect2.centerx = rectWarriorWhite3_2.centerx
                        warriorWhiteRect2.centery = rectWarriorWhite3_2.centery
                        counter += 1
                        warriorWhitePlaying2=False
                    elif rectWarriorWhite4_2.collidepoint(event.pos):
                        warriorWhiteRect2.centerx = rectWarriorWhite4_2.centerx
                        warriorWhiteRect2.centery = rectWarriorWhite4_2.centery
                        counter += 1
                        warriorWhitePlaying2=False
                    else:
                        warriorWhiteRect2.centerx = warriorWhitexInit2
                        warriorWhiteRect2.centery = warriorWhiteyInit2
                        warriorWhitePlaying2=False
                    if warriorWhiteRect2.colliderect(plagueDoctorWhiteRect):
                        warriorWhiteRect2.centerx = warriorWhitexInit2
                        warriorWhiteRect2.centery = warriorWhiteyInit2
                        counter -= 1
                        warriorWhitePlaying2=False
                    elif warriorWhiteRect2.colliderect(archbishopWhiteRect):
                        warriorWhiteRect2.centerx = warriorWhitexInit2
                        warriorWhiteRect2.centery = warriorWhiteyInit2
                        counter -= 1
                        warriorWhitePlaying2=False
                    elif warriorWhiteRect2.colliderect(cardinalWhiteRect):
                        warriorWhiteRect2.centerx = warriorWhitexInit2
                        warriorWhiteRect2.centery = warriorWhiteyInit2
                        counter -= 1
                        warriorWhitePlaying2=False
                    elif warriorWhiteRect2.colliderect(hadesWhiteRect):
                        warriorWhiteRect2.centerx = warriorWhitexInit2
                        warriorWhiteRect2.centery = warriorWhiteyInit2
                        counter -= 1
                        warriorWhitePlaying2=False
                    elif warriorWhiteRect2.colliderect(cardinalWhiteRect1):
                        warriorWhiteRect2.centerx = warriorWhitexInit2
                        warriorWhiteRect2.centery = warriorWhiteyInit2
                        counter -= 1
                        warriorWhitePlaying2=False
                    elif warriorWhiteRect2.colliderect(persephoneWhiteRect):
                        warriorWhiteRect2.centerx = warriorWhitexInit2
                        warriorWhiteRect2.centery = warriorWhiteyInit2
                        counter -= 1
                        warriorWhitePlaying2=False
                    elif warriorWhiteRect2.colliderect(archbishopWhiteRect1):
                        warriorWhiteRect2.centerx = warriorWhitexInit2
                        warriorWhiteRect2.centery = warriorWhiteyInit2
                        counter -= 1
                        warriorWhitePlaying2=False
                    elif warriorWhiteRect2.colliderect(plagueDoctorWhiteRect1):
                        warriorWhiteRect2.centerx = warriorWhitexInit2
                        warriorWhiteRect2.centery = warriorWhiteyInit2
                        counter -= 1
                        warriorWhitePlaying2=False
                    elif warriorWhiteRect2.colliderect(warriorWhiteRect):
                        warriorWhiteRect2.centerx = warriorWhitexInit2
                        warriorWhiteRect2.centery = warriorWhiteyInit2
                        counter -= 1
                        warriorWhitePlaying2=False
                    elif warriorWhiteRect2.colliderect(legionaryWhiteRect):
                        warriorWhiteRect2.centerx = warriorWhitexInit2
                        warriorWhiteRect2.centery = warriorWhiteyInit2
                        counter -= 1
                        warriorWhitePlaying2=False
                    elif warriorWhiteRect2.colliderect(warriorWhiteRect1):
                        warriorWhiteRect2.centerx = warriorWhitexInit2
                        warriorWhiteRect2.centery = warriorWhiteyInit2
                        counter -= 1
                        warriorWhitePlaying2=False
                    elif warriorWhiteRect2.colliderect(legionaryWhiteRect1):
                        warriorWhiteRect2.centerx = warriorWhitexInit2
                        warriorWhiteRect2.centery = warriorWhiteyInit2
                        counter -= 1
                        warriorWhitePlaying2=False
                    elif warriorWhiteRect2.colliderect(legionaryWhiteRect2):
                        warriorWhiteRect2.centerx = warriorWhitexInit2
                        warriorWhiteRect2.centery = warriorWhiteyInit2
                        counter -= 1
                        warriorWhitePlaying2=False
                    elif warriorWhiteRect2.colliderect(legionaryWhiteRect2):
                        warriorWhiteRect2.centerx = warriorWhitexInit2
                        warriorWhiteRect2.centery = warriorWhiteyInit2
                        counter -= 1
                        warriorWhitePlaying2=False
                    elif warriorWhiteRect2.colliderect(warriorWhiteRect3):
                        warriorWhiteRect2.centerx = warriorWhitexInit2
                        warriorWhiteRect2.centery = warriorWhiteyInit2
                        counter -= 1
                        warriorWhitePlaying2=False
                    elif warriorWhiteRect2.colliderect(legionaryWhiteRect3):
                        warriorWhiteRect2.centerx = warriorWhitexInit2
                        warriorWhiteRect2.centery = warriorWhiteyInit2
                        counter -= 1
                        warriorWhitePlaying2=False


                if legionaryWhiteRect2.collidepoint(event.pos):
                    if not legionaryWhitePlaying2:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                legionaryWhitePlaying2=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                legionaryWhitePlaying2=True
                elif legionaryWhitePlaying2:
                    if rectLegionaryWhite1_2.collidepoint(event.pos):
                        legionar_bily_x_abilita_2 = legionaryWhitexInit2
                        legionar_bily_y_abilita_2 = legionaryWhiteyInit2
                        legionaryWhiteRect2.centerx = rectLegionaryWhite1_2.centerx
                        legionaryWhiteRect2.centery = rectLegionaryWhite1_2.centery
                        counter += 1
                        legionaryWhitePlaying2=False
                    elif rectLegionaryWhite2_2.collidepoint(event.pos):
                        legionar_bily_x_abilita_2 = legionaryWhitexInit2
                        legionar_bily_y_abilita_2 = legionaryWhiteyInit2
                        legionaryWhiteRect2.centerx = rectLegionaryWhite2_2.centerx
                        legionaryWhiteRect2.centery = rectLegionaryWhite2_2.centery
                        counter += 1
                        legionaryWhitePlaying2=False
                    elif rectLegionaryWhite3_2.collidepoint(event.pos):
                        legionar_bily_x_abilita_2 = legionaryWhitexInit2
                        legionar_bily_y_abilita_2 = legionaryWhiteyInit2
                        legionaryWhiteRect2.centerx = rectLegionaryWhite3_2.centerx
                        legionaryWhiteRect2.centery = rectLegionaryWhite3_2.centery
                        counter += 1
                        legionaryWhitePlaying2=False
                    else:
                        legionaryWhiteRect2.centerx = legionaryWhitexInit2
                        legionaryWhiteRect2.centery = legionaryWhiteyInit2
                        legionaryWhitePlaying2=False
                    if legionaryWhiteRect2.colliderect(plagueDoctorWhiteRect):
                        legionaryWhiteRect2.centerx = legionaryWhitexInit2
                        legionaryWhiteRect2.centery = legionaryWhiteyInit2
                        counter -= 1
                        legionaryWhitePlaying2=False
                    elif legionaryWhiteRect2.colliderect(archbishopWhiteRect):
                        legionaryWhiteRect2.centerx = legionaryWhitexInit2
                        legionaryWhiteRect2.centery = legionaryWhiteyInit2
                        counter -= 1
                        legionaryWhitePlaying2=False
                    elif legionaryWhiteRect2.colliderect(cardinalWhiteRect):
                        legionaryWhiteRect2.centerx = legionaryWhitexInit2
                        legionaryWhiteRect2.centery = legionaryWhiteyInit2
                        counter -= 1
                        legionaryWhitePlaying2=False
                    elif legionaryWhiteRect2.colliderect(hadesWhiteRect):
                        legionaryWhiteRect2.centerx = legionaryWhitexInit2
                        legionaryWhiteRect2.centery = legionaryWhiteyInit2
                        counter -= 1
                        legionaryWhitePlaying2=False
                    elif legionaryWhiteRect2.colliderect(cardinalWhiteRect1):
                        legionaryWhiteRect2.centerx = legionaryWhitexInit2
                        legionaryWhiteRect2.centery = legionaryWhiteyInit2
                        counter -= 1
                        legionaryWhitePlaying2=False
                    elif legionaryWhiteRect2.colliderect(persephoneWhiteRect):
                        legionaryWhiteRect2.centerx = legionaryWhitexInit2
                        legionaryWhiteRect2.centery = legionaryWhiteyInit2
                        counter -= 1
                        legionaryWhitePlaying2=False
                    elif legionaryWhiteRect2.colliderect(archbishopWhiteRect1):
                        legionaryWhiteRect2.centerx = legionaryWhitexInit2
                        legionaryWhiteRect2.centery = legionaryWhiteyInit2
                        counter -= 1
                        legionaryWhitePlaying2=False
                    elif legionaryWhiteRect2.colliderect(plagueDoctorWhiteRect1):
                        legionaryWhiteRect2.centerx = legionaryWhitexInit2
                        legionaryWhiteRect2.centery = legionaryWhiteyInit2
                        counter -= 1
                        legionaryWhitePlaying2=False
                    elif legionaryWhiteRect2.colliderect(warriorWhiteRect):
                        legionaryWhiteRect2.centerx = legionaryWhitexInit2
                        legionaryWhiteRect2.centery = legionaryWhiteyInit2
                        counter -= 1
                        legionaryWhitePlaying2=False
                    elif legionaryWhiteRect2.colliderect(legionaryWhiteRect):
                        legionaryWhiteRect2.centerx = legionaryWhitexInit2
                        legionaryWhiteRect2.centery = legionaryWhiteyInit2
                        counter -= 1
                        legionaryWhitePlaying2=False
                    elif legionaryWhiteRect2.colliderect(warriorWhiteRect1):
                        legionaryWhiteRect2.centerx = legionaryWhitexInit2
                        legionaryWhiteRect2.centery = legionaryWhiteyInit2
                        counter -= 1
                        legionaryWhitePlaying2=False
                    elif legionaryWhiteRect2.colliderect(warriorWhiteRect2):
                        legionaryWhiteRect2.centerx = legionaryWhitexInit2
                        legionaryWhiteRect2.centery = legionaryWhiteyInit2
                        counter -= 1
                        legionaryWhitePlaying2=False
                    elif legionaryWhiteRect2.colliderect(legionaryWhiteRect1):
                        legionaryWhiteRect2.centerx = legionaryWhitexInit2
                        legionaryWhiteRect2.centery = legionaryWhiteyInit2
                        counter -= 1
                        legionaryWhitePlaying2=False
                    elif legionaryWhiteRect2.colliderect(warriorWhiteRect3):
                        legionaryWhiteRect2.centerx = legionaryWhitexInit2
                        legionaryWhiteRect2.centery = legionaryWhiteyInit2
                        counter -= 1
                        legionaryWhitePlaying2=False
                    elif legionaryWhiteRect2.colliderect(legionaryWhiteRect3):
                        legionaryWhiteRect2.centerx = legionaryWhitexInit2
                        legionaryWhiteRect2.centery = legionaryWhiteyInit2
                        counter -= 1
                        legionaryWhitePlaying2=False

                if warriorWhiteRect3.collidepoint(event.pos):
                    if not warriorWhitePlaying3:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                warriorWhitePlaying3=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                warriorWhitePlaying3=True
                elif warriorWhitePlaying3:
                    if rectWarriorWhite1_3Ability.collidepoint(event.pos) and counter % 4 == 0:
                        warriorWhiteRect3.centerx = rectWarriorWhite1_3Ability.centerx
                        warriorWhiteRect3.centery = rectWarriorWhite1_3Ability.centery
                        counter += 1
                        warriorWhitePlaying3=False
                    elif rectWarriorWhite2_3Ability.collidepoint(event.pos) and counter % 4 == 0:
                        warriorWhiteRect3.centerx = rectWarriorWhite2_3Ability.centerx
                        warriorWhiteRect3.centery = rectWarriorWhite2_3Ability.centery
                        counter += 1
                        warriorWhitePlaying3=False
                    elif rectWarriorWhite3_3Ability.collidepoint(event.pos) and counter % 4 == 0:
                        warriorWhiteRect3.centerx = rectWarriorWhite3_3Ability.centerx
                        warriorWhiteRect3.centery = rectWarriorWhite3_3Ability.centery
                        counter += 1
                        warriorWhitePlaying3=False
                    elif rectWarriorWhite4_3Ability.collidepoint(event.pos) and counter % 4 == 0:
                        warriorWhiteRect3.centerx = rectWarriorWhite4_3Ability.centerx
                        warriorWhiteRect3.centery = rectWarriorWhite4_3Ability.centery
                        counter += 1
                        warriorWhitePlaying3=False
                    elif rectWarriorWhite1_3.collidepoint(event.pos):
                        warriorWhiteRect3.centerx = rectWarriorWhite1_3.centerx
                        warriorWhiteRect3.centery = rectWarriorWhite1_3.centery
                        counter += 1
                        warriorWhitePlaying3=False
                    elif rectWarriorWhite2_3.collidepoint(event.pos):
                        warriorWhiteRect3.centerx = rectWarriorWhite2_3.centerx
                        warriorWhiteRect3.centery = rectWarriorWhite2_3.centery
                        counter += 1
                        warriorWhitePlaying3=False
                    elif rectWarriorWhite3_3.collidepoint(event.pos):
                        warriorWhiteRect3.centerx = rectWarriorWhite3_3.centerx
                        warriorWhiteRect3.centery = rectWarriorWhite3_3.centery
                        counter += 1
                        warriorWhitePlaying3=False
                    elif rectWarriorWhite4_3.collidepoint(event.pos):
                        warriorWhiteRect3.centerx = rectWarriorWhite4_3.centerx
                        warriorWhiteRect3.centery = rectWarriorWhite4_3.centery
                        counter += 1
                        warriorWhitePlaying3=False
                    else:
                        warriorWhiteRect3.centerx = warriorWhitexInit3
                        warriorWhiteRect3.centery = warriorWhiteyInit3
                        warriorWhitePlaying3=False
                    if warriorWhiteRect3.colliderect(plagueDoctorWhiteRect):
                        warriorWhiteRect3.centerx = warriorWhitexInit3
                        warriorWhiteRect3.centery = warriorWhiteyInit3
                        counter -= 1
                        warriorWhitePlaying3=False
                    elif warriorWhiteRect3.colliderect(archbishopWhiteRect):
                        warriorWhiteRect3.centerx = warriorWhitexInit3
                        warriorWhiteRect3.centery = warriorWhiteyInit3
                        counter -= 1
                        warriorWhitePlaying3=False
                    elif warriorWhiteRect3.colliderect(cardinalWhiteRect):
                        warriorWhiteRect3.centerx = warriorWhitexInit3
                        warriorWhiteRect3.centery = warriorWhiteyInit3
                        counter -= 1
                        warriorWhitePlaying3=False
                    elif warriorWhiteRect3.colliderect(hadesWhiteRect):
                        warriorWhiteRect3.centerx = warriorWhitexInit3
                        warriorWhiteRect3.centery = warriorWhiteyInit3
                        counter -= 1
                        warriorWhitePlaying3=False
                    elif warriorWhiteRect3.colliderect(cardinalWhiteRect1):
                        warriorWhiteRect3.centerx = warriorWhitexInit3
                        warriorWhiteRect3.centery = warriorWhiteyInit3
                        counter -= 1
                        warriorWhitePlaying3=False
                    elif warriorWhiteRect3.colliderect(persephoneWhiteRect):
                        warriorWhiteRect3.centerx = warriorWhitexInit3
                        warriorWhiteRect3.centery = warriorWhiteyInit3
                        counter -= 1
                        warriorWhitePlaying3=False
                    elif warriorWhiteRect3.colliderect(archbishopWhiteRect1):
                        warriorWhiteRect3.centerx = warriorWhitexInit3
                        warriorWhiteRect3.centery = warriorWhiteyInit3
                        counter -= 1
                        warriorWhitePlaying3=False
                    elif warriorWhiteRect3.colliderect(plagueDoctorWhiteRect1):
                        warriorWhiteRect3.centerx = warriorWhitexInit3
                        warriorWhiteRect3.centery = warriorWhiteyInit3
                        counter -= 1
                        warriorWhitePlaying3=False
                    elif warriorWhiteRect3.colliderect(warriorWhiteRect):
                        warriorWhiteRect3.centerx = warriorWhitexInit3
                        warriorWhiteRect3.centery = warriorWhiteyInit3
                        counter -= 1
                        warriorWhitePlaying3=False
                    elif warriorWhiteRect3.colliderect(legionaryWhiteRect):
                        warriorWhiteRect3.centerx = warriorWhitexInit3
                        warriorWhiteRect3.centery = warriorWhiteyInit3
                        counter -= 1
                        warriorWhitePlaying3=False
                    elif warriorWhiteRect3.colliderect(warriorWhiteRect1):
                        warriorWhiteRect3.centerx = warriorWhitexInit3
                        warriorWhiteRect3.centery = warriorWhiteyInit3
                        counter -= 1
                        warriorWhitePlaying3=False
                    elif warriorWhiteRect3.colliderect(warriorWhiteRect2):
                        warriorWhiteRect3.centerx = warriorWhitexInit3
                        warriorWhiteRect3.centery = warriorWhiteyInit3
                        counter -= 1
                        warriorWhitePlaying3=False
                    elif warriorWhiteRect3.colliderect(legionaryWhiteRect1):
                        warriorWhiteRect3.centerx = warriorWhitexInit3
                        warriorWhiteRect3.centery = warriorWhiteyInit3
                        counter -= 1
                        warriorWhitePlaying3=False
                    elif warriorWhiteRect3.colliderect(legionaryWhiteRect2):
                        warriorWhiteRect3.centerx = warriorWhitexInit3
                        warriorWhiteRect3.centery = warriorWhiteyInit3
                        counter -= 1
                        warriorWhitePlaying3=False
                    elif warriorWhiteRect3.colliderect(legionaryWhiteRect3):
                        warriorWhiteRect3.centerx = warriorWhitexInit3
                        warriorWhiteRect3.centery = warriorWhiteyInit3
                        counter -= 1
                        warriorWhitePlaying3=False


                if legionaryWhiteRect3.collidepoint(event.pos):
                    if not legionaryWhitePlaying3:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                legionaryWhitePlaying3=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                legionaryWhitePlaying3=True
                elif legionaryWhitePlaying3:
                    if rectLegionaryWhite1_3.collidepoint(event.pos):
                        legionar_bily_x_abilita_3 = legionaryWhitexInit3
                        legionar_bily_y_abilita_3 = legionaryWhiteyInit3
                        legionaryWhiteRect3.centerx = rectLegionaryWhite1_3.centerx
                        legionaryWhiteRect3.centery = rectLegionaryWhite1_3.centery
                        counter += 1
                        legionaryWhitePlaying3=False
                    elif rectLegionaryWhite2_3.collidepoint(event.pos):
                        legionar_bily_x_abilita_3 = legionaryWhitexInit3
                        legionar_bily_y_abilita_3 = legionaryWhiteyInit3
                        legionaryWhiteRect3.centerx = rectLegionaryWhite2_3.centerx
                        legionaryWhiteRect3.centery = rectLegionaryWhite2_3.centery
                        counter += 1
                        legionaryWhitePlaying3=False
                    elif rectLegionaryWhite3_3.collidepoint(event.pos):
                        legionar_bily_x_abilita_3 = legionaryWhitexInit3
                        legionar_bily_y_abilita_3 = legionaryWhiteyInit3
                        legionaryWhiteRect3.centerx = rectLegionaryWhite3_3.centerx
                        legionaryWhiteRect3.centery = rectLegionaryWhite3_3.centery
                        counter += 1
                        legionaryWhitePlaying3=False
                    else:
                        legionaryWhiteRect3.centerx = legionaryWhitexInit3
                        legionaryWhiteRect3.centery = legionaryWhiteyInit3
                        legionaryWhitePlaying3=False
                    if legionaryWhiteRect3.colliderect(plagueDoctorWhiteRect):
                        legionaryWhiteRect3.centerx = legionaryWhitexInit3
                        legionaryWhiteRect3.centery = legionaryWhiteyInit3
                        counter -= 1
                        legionaryWhitePlaying3=False
                    elif legionaryWhiteRect3.colliderect(archbishopWhiteRect):
                        legionaryWhiteRect3.centerx = legionaryWhitexInit3
                        legionaryWhiteRect3.centery = legionaryWhiteyInit3
                        counter -= 1
                        legionaryWhitePlaying3=False
                    elif legionaryWhiteRect3.colliderect(cardinalWhiteRect):
                        legionaryWhiteRect3.centerx = legionaryWhitexInit3
                        legionaryWhiteRect3.centery = legionaryWhiteyInit3
                        counter -= 1
                        legionaryWhitePlaying3=False
                    elif legionaryWhiteRect3.colliderect(hadesWhiteRect):
                        legionaryWhiteRect3.centerx = legionaryWhitexInit3
                        legionaryWhiteRect3.centery = legionaryWhiteyInit3
                        counter -= 1
                        legionaryWhitePlaying3=False
                    elif legionaryWhiteRect3.colliderect(cardinalWhiteRect1):
                        legionaryWhiteRect3.centerx = legionaryWhitexInit3
                        legionaryWhiteRect3.centery = legionaryWhiteyInit3
                        counter -= 1
                        legionaryWhitePlaying3=False
                    elif legionaryWhiteRect3.colliderect(persephoneWhiteRect):
                        legionaryWhiteRect3.centerx = legionaryWhitexInit3
                        legionaryWhiteRect3.centery = legionaryWhiteyInit3
                        counter -= 1
                        legionaryWhitePlaying3=False
                    elif legionaryWhiteRect3.colliderect(archbishopWhiteRect1):
                        legionaryWhiteRect3.centerx = legionaryWhitexInit3
                        legionaryWhiteRect3.centery = legionaryWhiteyInit3
                        counter -= 1
                        legionaryWhitePlaying3=False
                    elif legionaryWhiteRect3.colliderect(plagueDoctorWhiteRect1):
                        legionaryWhiteRect3.centerx = legionaryWhitexInit3
                        legionaryWhiteRect3.centery = legionaryWhiteyInit3
                        counter -= 1
                        legionaryWhitePlaying3=False
                    elif legionaryWhiteRect3.colliderect(warriorWhiteRect):
                        legionaryWhiteRect3.centerx = legionaryWhitexInit3
                        legionaryWhiteRect3.centery = legionaryWhiteyInit3
                        counter -= 1
                        legionaryWhitePlaying3=False
                    elif legionaryWhiteRect3.colliderect(legionaryWhiteRect):
                        legionaryWhiteRect3.centerx = legionaryWhitexInit3
                        legionaryWhiteRect3.centery = legionaryWhiteyInit3
                        counter -= 1
                        legionaryWhitePlaying3=False
                    elif legionaryWhiteRect3.colliderect(warriorWhiteRect1):
                        legionaryWhiteRect3.centerx = legionaryWhitexInit3
                        legionaryWhiteRect3.centery = legionaryWhiteyInit3
                        counter -= 1
                        legionaryWhitePlaying3=False
                    elif legionaryWhiteRect3.colliderect(warriorWhiteRect2):
                        legionaryWhiteRect3.centerx = legionaryWhitexInit3
                        legionaryWhiteRect3.centery = legionaryWhiteyInit3
                        counter -= 1
                        legionaryWhitePlaying3=False
                    elif legionaryWhiteRect3.colliderect(legionaryWhiteRect1):
                        legionaryWhiteRect3.centerx = legionaryWhitexInit3
                        legionaryWhiteRect3.centery = legionaryWhiteyInit3
                        counter -= 1
                        legionaryWhitePlaying3=False
                    elif legionaryWhiteRect3.colliderect(legionaryWhiteRect2):
                        legionaryWhiteRect3.centerx = legionaryWhitexInit3
                        legionaryWhiteRect3.centery = legionaryWhiteyInit3
                        counter -= 1
                        legionaryWhitePlaying3=False
                    elif legionaryWhiteRect3.colliderect(warriorWhiteRect3):
                        legionaryWhiteRect3.centerx = legionaryWhitexInit3
                        legionaryWhiteRect3.centery = legionaryWhiteyInit3
                        counter -= 1
                        legionaryWhitePlaying3=False

            else:
                if plagueDoctorBlackRect.collidepoint(event.pos):
                    if not plagueDoctorBlackPlaying:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                plagueDoctorBlackPlaying=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                plagueDoctorBlackPlaying=True
                elif plagueDoctorBlackPlaying:
                    if rectPlagueBlack1.collidepoint(event.pos):
                        plagueDoctorBlackRect.centerx = rectPlagueBlack1.centerx
                        plagueDoctorBlackRect.centery = rectPlagueBlack1.centery
                        counter += 1
                        plagueDoctorBlackPlaying=False
                    elif rectPlagueBlack2.collidepoint(event.pos):
                        plagueDoctorBlackRect.centerx = rectPlagueBlack2.centerx
                        plagueDoctorBlackRect.centery = rectPlagueBlack2.centery
                        counter += 1
                        plagueDoctorBlackPlaying=False
                    elif rectPlagueBlack3.collidepoint(event.pos):
                        plagueDoctorBlackRect.centerx = rectPlagueBlack3.centerx
                        plagueDoctorBlackRect.centery = rectPlagueBlack3.centery
                        counter += 1
                        plagueDoctorBlackPlaying=False
                    elif rectPlagueBlack4.collidepoint(event.pos):
                        plagueDoctorBlackRect.centerx = rectPlagueBlack4.centerx
                        plagueDoctorBlackRect.centery = rectPlagueBlack4.centery
                        counter += 1
                        plagueDoctorBlackPlaying=False
                    elif rectPlagueBlack5.collidepoint(event.pos):
                        plagueDoctorBlackRect.centerx = rectPlagueBlack5.centerx
                        plagueDoctorBlackRect.centery = rectPlagueBlack5.centery
                        counter += 1
                        plagueDoctorBlackPlaying=False
                    elif rectPlagueBlack6.collidepoint(event.pos):
                        plagueDoctorBlackRect.centerx = rectPlagueBlack6.centerx
                        plagueDoctorBlackRect.centery = rectPlagueBlack6.centery
                        counter += 1
                        plagueDoctorBlackPlaying=False
                    elif rectPlagueBlack7.collidepoint(event.pos):
                        plagueDoctorBlackRect.centerx = rectPlagueBlack7.centerx
                        plagueDoctorBlackRect.centery = rectPlagueBlack7.centery
                        counter += 1
                        plagueDoctorBlackPlaying=False
                    elif rectPlagueBlack8.collidepoint(event.pos):
                        plagueDoctorBlackRect.centerx = rectPlagueBlack8.centerx
                        plagueDoctorBlackRect.centery = rectPlagueBlack8.centery
                        counter += 1
                        plagueDoctorBlackPlaying=False
                    elif rectPlagueBlack9.collidepoint(event.pos):
                        plagueDoctorBlackRect.centerx = rectPlagueBlack9.centerx
                        plagueDoctorBlackRect.centery = rectPlagueBlack9.centery
                        counter += 1
                        plagueDoctorBlackPlaying=False
                    elif rectPlagueBlack10.collidepoint(event.pos):
                        plagueDoctorBlackRect.centerx = rectPlagueBlack10.centerx
                        plagueDoctorBlackRect.centery = rectPlagueBlack10.centery
                        counter += 1
                        plagueDoctorBlackPlaying=False
                    elif rectPlagueBlack11.collidepoint(event.pos):
                        plagueDoctorBlackRect.centerx = rectPlagueBlack11.centerx
                        plagueDoctorBlackRect.centery = rectPlagueBlack11.centery
                        counter += 1
                        plagueDoctorBlackPlaying=False
                    elif rectPlagueBlack12.collidepoint(event.pos):
                        plagueDoctorBlackRect.centerx = rectPlagueBlack12.centerx
                        plagueDoctorBlackRect.centery = rectPlagueBlack12.centery
                        counter += 1
                        plagueDoctorBlackPlaying=False
                    elif rectPlagueBlack13.collidepoint(event.pos):
                        plagueDoctorBlackRect.centerx = rectPlagueBlack13.centerx
                        plagueDoctorBlackRect.centery = rectPlagueBlack13.centery
                        counter += 1
                        plagueDoctorBlackPlaying=False
                    elif rectPlagueBlack14.collidepoint(event.pos):
                        plagueDoctorBlackRect.centerx = rectPlagueBlack14.centerx
                        plagueDoctorBlackRect.centery = rectPlagueBlack14.centery
                        counter += 1
                        plagueDoctorBlackPlaying=False
                    elif rectPlagueBlack15.collidepoint(event.pos):
                        plagueDoctorBlackRect.centerx = rectPlagueBlack15.centerx
                        plagueDoctorBlackRect.centery = rectPlagueBlack15.centery
                        counter += 1
                        plagueDoctorBlackPlaying=False
                    elif rectPlagueBlack16.collidepoint(event.pos):
                        plagueDoctorBlackRect.centerx = rectPlagueBlack16.centerx
                        plagueDoctorBlackRect.centery = rectPlagueBlack16.centery
                        counter += 1
                        plagueDoctorBlackPlaying=False
                    elif rectPlagueBlack17.collidepoint(event.pos):
                        plagueDoctorBlackRect.centerx = rectPlagueBlack17.centerx
                        plagueDoctorBlackRect.centery = rectPlagueBlack17.centery
                        counter += 1
                        plagueDoctorBlackPlaying=False
                    elif rectPlagueBlack18.collidepoint(event.pos):
                        plagueDoctorBlackRect.centerx = rectPlagueBlack18.centerx
                        plagueDoctorBlackRect.centery = rectPlagueBlack18.centery
                        counter += 1
                        plagueDoctorBlackPlaying=False
                    else:
                        plagueDoctorBlackRect.centerx = plagueBlackxInit
                        plagueDoctorBlackRect.centery = plagueBlackyInit
                        plagueDoctorBlackPlaying=False
                    if plagueDoctorBlackRect.colliderect(archbishopBlackRect):
                        plagueDoctorBlackRect.centerx = plagueBlackxInit
                        plagueDoctorBlackRect.centery = plagueBlackyInit
                        counter -= 1
                        plagueDoctorBlackPlaying=False
                    elif plagueDoctorBlackRect.colliderect(cardinalBlackRect):
                        plagueDoctorBlackRect.centerx = plagueBlackxInit
                        plagueDoctorBlackRect.centery = plagueBlackyInit
                        counter -= 1
                        plagueDoctorBlackPlaying=False
                    elif plagueDoctorBlackRect.colliderect(hadesBlackRect):
                        plagueDoctorBlackRect.centerx = plagueBlackxInit
                        plagueDoctorBlackRect.centery = plagueBlackyInit
                        counter -= 1
                        plagueDoctorBlackPlaying=False
                    elif plagueDoctorBlackRect.colliderect(persephoneBlackRect):
                        plagueDoctorBlackRect.centerx = plagueBlackxInit
                        plagueDoctorBlackRect.centery = plagueBlackyInit
                        counter -= 1
                        plagueDoctorBlackPlaying=False
                    elif plagueDoctorBlackRect.colliderect(cardinalBlackRect1):
                        plagueDoctorBlackRect.centerx = plagueBlackxInit
                        plagueDoctorBlackRect.centery = plagueBlackyInit
                        counter -= 1
                        plagueDoctorBlackPlaying=False
                    elif plagueDoctorBlackRect.colliderect(archbishopBlackRect1):
                        plagueDoctorBlackRect.centerx = plagueBlackxInit
                        plagueDoctorBlackRect.centery = plagueBlackyInit
                        counter -= 1
                        plagueDoctorBlackPlaying=False
                    elif plagueDoctorBlackRect.colliderect(plagueDoctorBlackRect1):
                        plagueDoctorBlackRect.centerx = plagueBlackxInit
                        plagueDoctorBlackRect.centery = plagueBlackyInit
                        counter -= 1
                        plagueDoctorBlackPlaying=False
                    elif plagueDoctorBlackRect.colliderect(legionaryBlackRect):
                        plagueDoctorBlackRect.centerx = plagueBlackxInit
                        plagueDoctorBlackRect.centery = plagueBlackyInit
                        counter -= 1
                        plagueDoctorBlackPlaying=False
                    elif plagueDoctorBlackRect.colliderect(warriorBlackRect):
                        plagueDoctorBlackRect.centerx = plagueBlackxInit
                        plagueDoctorBlackRect.centery = plagueBlackyInit
                        counter -= 1
                        plagueDoctorBlackPlaying=False
                    elif plagueDoctorBlackRect.colliderect(legionaryBlackRect1):
                        plagueDoctorBlackRect.centerx = plagueBlackxInit
                        plagueDoctorBlackRect.centery = plagueBlackyInit
                        counter -= 1
                        plagueDoctorBlackPlaying=False
                    elif plagueDoctorBlackRect.colliderect(warriorBlackRect1):
                        plagueDoctorBlackRect.centerx = plagueBlackxInit
                        plagueDoctorBlackRect.centery = plagueBlackyInit
                        counter -= 1
                        plagueDoctorBlackPlaying=False
                    elif plagueDoctorBlackRect.colliderect(legionaryBlackRect2):
                        plagueDoctorBlackRect.centerx = plagueBlackxInit
                        plagueDoctorBlackRect.centery = plagueBlackyInit
                        counter -= 1
                        plagueDoctorBlackPlaying=False
                    elif plagueDoctorBlackRect.colliderect(warriorBlackRect2):
                        plagueDoctorBlackRect.centerx = plagueBlackxInit
                        plagueDoctorBlackRect.centery = plagueBlackyInit
                        counter -= 1
                        plagueDoctorBlackPlaying=False
                    elif plagueDoctorBlackRect.colliderect(legionaryBlackRect3):
                        plagueDoctorBlackRect.centerx = plagueBlackxInit
                        plagueDoctorBlackRect.centery = plagueBlackyInit
                        counter -= 1
                        plagueDoctorBlackPlaying=False
                    elif plagueDoctorBlackRect.colliderect(warriorBlackRect3):
                        plagueDoctorBlackRect.centerx = plagueBlackxInit
                        plagueDoctorBlackRect.centery = plagueBlackyInit
                        counter -= 1
                        plagueDoctorBlackPlaying=False

                if archbishopBlackRect.collidepoint(event.pos):
                    if not archbishopBlackPlaying:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                archbishopBlackPlaying=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                archbishopBlackPlaying=True
                elif archbishopBlackPlaying:
                    if rectArchbishopBlack1.collidepoint(event.pos):
                        archbishopBlackRect.centerx = rectArchbishopBlack1.centerx
                        archbishopBlackRect.centery = rectArchbishopBlack1.centery
                        counter += 1
                        archbishopBlackPlaying=False
                    elif rectArchbishopBlack2.collidepoint(event.pos):
                        archbishopBlackRect.centerx = rectArchbishopBlack2.centerx
                        archbishopBlackRect.centery = rectArchbishopBlack2.centery
                        counter += 1
                        archbishopBlackPlaying=False
                    elif rectArchbishopBlack3.collidepoint(event.pos):
                        archbishopBlackRect.centerx = rectArchbishopBlack3.centerx
                        archbishopBlackRect.centery = rectArchbishopBlack3.centery
                        counter += 1
                        archbishopBlackPlaying=False
                    elif rectArchbishopBlack4.collidepoint(event.pos):
                        archbishopBlackRect.centerx = rectArchbishopBlack4.centerx
                        archbishopBlackRect.centery = rectArchbishopBlack4.centery
                        counter += 1
                        archbishopBlackPlaying=False
                    elif rectArchbishopBlack5.collidepoint(event.pos):
                        archbishopBlackRect.centerx = rectArchbishopBlack5.centerx
                        archbishopBlackRect.centery = rectArchbishopBlack5.centery
                        counter += 1
                        archbishopBlackPlaying=False
                    elif rectArchbishopBlack6.collidepoint(event.pos):
                        archbishopBlackRect.centerx = rectArchbishopBlack6.centerx
                        archbishopBlackRect.centery = rectArchbishopBlack6.centery
                        counter += 1
                        archbishopBlackPlaying=False
                    elif rectArchbishopBlack7.collidepoint(event.pos):
                        archbishopBlackRect.centerx = rectArchbishopBlack7.centerx
                        archbishopBlackRect.centery = rectArchbishopBlack7.centery
                        counter += 1
                        archbishopBlackPlaying=False
                    elif rectArchbishopBlack8.collidepoint(event.pos):
                        archbishopBlackRect.centerx = rectArchbishopBlack8.centerx
                        archbishopBlackRect.centery = rectArchbishopBlack8.centery
                        counter += 1
                        archbishopBlackPlaying=False
                    elif rectArchbishopBlack9.collidepoint(event.pos):
                        archbishopBlackRect.centerx = rectArchbishopBlack9.centerx
                        archbishopBlackRect.centery = rectArchbishopBlack9.centery
                        counter += 1
                        archbishopBlackPlaying=False
                    elif rectArchbishopBlack10.collidepoint(event.pos):
                        archbishopBlackRect.centerx = rectArchbishopBlack10.centerx
                        archbishopBlackRect.centery = rectArchbishopBlack10.centery
                        counter += 1
                        archbishopBlackPlaying=False
                    elif rectArchbishopBlack11.collidepoint(event.pos):
                        archbishopBlackRect.centerx = rectArchbishopBlack11.centerx
                        archbishopBlackRect.centery = rectArchbishopBlack11.centery
                        counter += 1
                        archbishopBlackPlaying=False
                    elif rectArchbishopBlack12.collidepoint(event.pos):
                        archbishopBlackRect.centerx = rectArchbishopBlack12.centerx
                        archbishopBlackRect.centery = rectArchbishopBlack12.centery
                        counter += 1
                        archbishopBlackPlaying=False
                    else:
                        archbishopBlackRect.centerx = archbishopBlackxInit
                        archbishopBlackRect.centery = archbishopBlackyInit
                        archbishopBlackPlaying=False
                    if archbishopBlackRect.colliderect(plagueDoctorBlackRect):
                        archbishopBlackRect.centerx = archbishopBlackxInit
                        archbishopBlackRect.centery = archbishopBlackyInit
                        counter -= 1
                        archbishopBlackPlaying=False
                    elif archbishopBlackRect.colliderect(cardinalBlackRect):
                        archbishopBlackRect.centerx = archbishopBlackxInit
                        archbishopBlackRect.centery = archbishopBlackyInit
                        counter -= 1
                        archbishopBlackPlaying=False
                    elif archbishopBlackRect.colliderect(hadesBlackRect):
                        archbishopBlackRect.centerx = archbishopBlackxInit
                        archbishopBlackRect.centery = archbishopBlackyInit
                        counter -= 1
                        archbishopBlackPlaying=False
                    elif archbishopBlackRect.colliderect(persephoneBlackRect):
                        archbishopBlackRect.centerx = archbishopBlackxInit
                        archbishopBlackRect.centery = archbishopBlackyInit
                        counter -= 1
                        archbishopBlackPlaying=False
                    elif archbishopBlackRect.colliderect(cardinalBlackRect1):
                        archbishopBlackRect.centerx = archbishopBlackxInit
                        archbishopBlackRect.centery = archbishopBlackyInit
                        counter -= 1
                        archbishopBlackPlaying=False
                    elif archbishopBlackRect.colliderect(archbishopBlackRect1):
                        archbishopBlackRect.centerx = archbishopBlackxInit
                        archbishopBlackRect.centery = archbishopBlackyInit
                        counter -= 1
                        archbishopBlackPlaying=False
                    elif archbishopBlackRect.colliderect(plagueDoctorBlackRect1):
                        archbishopBlackRect.centerx = archbishopBlackxInit
                        archbishopBlackRect.centery = archbishopBlackyInit
                        counter -= 1
                        archbishopBlackPlaying=False
                    elif archbishopBlackRect.colliderect(legionaryBlackRect):
                        archbishopBlackRect.centerx = archbishopBlackxInit
                        archbishopBlackRect.centery = archbishopBlackyInit
                        counter -= 1
                        archbishopBlackPlaying=False
                    elif archbishopBlackRect.colliderect(warriorBlackRect):
                        archbishopBlackRect.centerx = archbishopBlackxInit
                        archbishopBlackRect.centery = archbishopBlackyInit
                        counter -= 1
                        archbishopBlackPlaying=False
                    elif archbishopBlackRect.colliderect(legionaryBlackRect1):
                        archbishopBlackRect.centerx = archbishopBlackxInit
                        archbishopBlackRect.centery = archbishopBlackyInit
                        counter -= 1
                        archbishopBlackPlaying=False
                    elif archbishopBlackRect.colliderect(warriorBlackRect1):
                        archbishopBlackRect.centerx = archbishopBlackxInit
                        archbishopBlackRect.centery = archbishopBlackyInit
                        counter -= 1
                        archbishopBlackPlaying=False
                    elif archbishopBlackRect.colliderect(legionaryBlackRect2):
                        archbishopBlackRect.centerx = archbishopBlackxInit
                        archbishopBlackRect.centery = archbishopBlackyInit
                        counter -= 1
                        archbishopBlackPlaying=False
                    elif archbishopBlackRect.colliderect(warriorBlackRect2):
                        archbishopBlackRect.centerx = archbishopBlackxInit
                        archbishopBlackRect.centery = archbishopBlackyInit
                        counter -= 1
                        archbishopBlackPlaying=False
                    elif archbishopBlackRect.colliderect(legionaryBlackRect3):
                        archbishopBlackRect.centerx = archbishopBlackxInit
                        archbishopBlackRect.centery = archbishopBlackyInit
                        counter -= 1
                        archbishopBlackPlaying=False
                    elif archbishopBlackRect.colliderect(warriorBlackRect3):
                        archbishopBlackRect.centerx = archbishopBlackxInit
                        archbishopBlackRect.centery = archbishopBlackyInit
                        counter -= 1
                        archbishopBlackPlaying=False

                

                if cardinalBlackRect.collidepoint(event.pos):
                    if not cardinalBlackPlaying:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                cardinalBlackPlaying=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                cardinalBlackPlaying=True
                elif cardinalBlackPlaying:
                    if rectCardinalBlack1.collidepoint(event.pos):
                        cardinalBlackRect.centerx = rectCardinalBlack1.centerx
                        cardinalBlackRect.centery = rectCardinalBlack1.centery
                        counter += 1
                        cardinalBlackPlaying=False
                    elif rectCardinalBlack2.collidepoint(event.pos):
                        cardinalBlackRect.centerx = rectCardinalBlack2.centerx
                        cardinalBlackRect.centery = rectCardinalBlack2.centery
                        counter += 1
                        cardinalBlackPlaying=False
                    elif rectCardinalBlack3.collidepoint(event.pos):
                        cardinalBlackRect.centerx = rectCardinalBlack3.centerx
                        cardinalBlackRect.centery = rectCardinalBlack3.centery
                        counter += 1
                        cardinalBlackPlaying=False
                    elif rectCardinalBlack4.collidepoint(event.pos):
                        cardinalBlackRect.centerx = rectCardinalBlack4.centerx
                        cardinalBlackRect.centery = rectCardinalBlack4.centery
                        counter += 1
                        cardinalBlackPlaying=False
                    else:
                        cardinalBlackRect.centerx = cardinalBlackxInit
                        cardinalBlackRect.centery = cardinalBlackyInit
                        cardinalBlackPlaying=False
                    if cardinalBlackRect.colliderect(plagueDoctorBlackRect):
                        cardinalBlackRect.centerx = cardinalBlackxInit
                        cardinalBlackRect.centery = cardinalBlackyInit
                        counter -= 1
                        cardinalBlackPlaying=False
                    elif cardinalBlackRect.colliderect(archbishopBlackRect):
                        cardinalBlackRect.centerx = cardinalBlackxInit
                        cardinalBlackRect.centery = cardinalBlackyInit
                        counter -= 1
                        cardinalBlackPlaying=False
                    elif cardinalBlackRect.colliderect(hadesBlackRect):
                        cardinalBlackRect.centerx = cardinalBlackxInit
                        cardinalBlackRect.centery = cardinalBlackyInit
                        counter -= 1
                        cardinalBlackPlaying=False
                    elif cardinalBlackRect.colliderect(persephoneBlackRect):
                        cardinalBlackRect.centerx = cardinalBlackxInit
                        cardinalBlackRect.centery = cardinalBlackyInit
                        counter -= 1
                        cardinalBlackPlaying=False
                    elif cardinalBlackRect.colliderect(cardinalBlackRect1):
                        cardinalBlackRect.centerx = cardinalBlackxInit
                        cardinalBlackRect.centery = cardinalBlackyInit
                        counter -= 1
                        cardinalBlackPlaying=False
                    elif cardinalBlackRect.colliderect(archbishopBlackRect1):
                        cardinalBlackRect.centerx = cardinalBlackxInit
                        cardinalBlackRect.centery = cardinalBlackyInit
                        counter -= 1
                        cardinalBlackPlaying=False
                    elif cardinalBlackRect.colliderect(plagueDoctorBlackRect1):
                        cardinalBlackRect.centerx = cardinalBlackxInit
                        cardinalBlackRect.centery = cardinalBlackyInit
                        counter -= 1
                        cardinalBlackPlaying=False
                    elif cardinalBlackRect.colliderect(legionaryBlackRect):
                        cardinalBlackRect.centerx = cardinalBlackxInit
                        cardinalBlackRect.centery = cardinalBlackyInit
                        counter -= 1
                        cardinalBlackPlaying=False
                    elif cardinalBlackRect.colliderect(warriorBlackRect):
                        cardinalBlackRect.centerx = cardinalBlackxInit
                        cardinalBlackRect.centery = cardinalBlackyInit
                        counter -= 1
                        cardinalBlackPlaying=False
                    elif cardinalBlackRect.colliderect(legionaryBlackRect1):
                        cardinalBlackRect.centerx = cardinalBlackxInit
                        cardinalBlackRect.centery = cardinalBlackyInit
                        counter -= 1
                        cardinalBlackPlaying=False
                    elif cardinalBlackRect.colliderect(warriorBlackRect1):
                        cardinalBlackRect.centerx = cardinalBlackxInit
                        cardinalBlackRect.centery = cardinalBlackyInit
                        counter -= 1
                        cardinalBlackPlaying=False
                    elif cardinalBlackRect.colliderect(legionaryBlackRect2):
                        cardinalBlackRect.centerx = cardinalBlackxInit
                        cardinalBlackRect.centery = cardinalBlackyInit
                        counter -= 1
                        cardinalBlackPlaying=False
                    elif cardinalBlackRect.colliderect(warriorBlackRect2):
                        cardinalBlackRect.centerx = cardinalBlackxInit
                        cardinalBlackRect.centery = cardinalBlackyInit
                        counter -= 1
                        cardinalBlackPlaying=False
                    elif cardinalBlackRect.colliderect(legionaryBlackRect3):
                        cardinalBlackRect.centerx = cardinalBlackxInit
                        cardinalBlackRect.centery = cardinalBlackyInit
                        counter -= 1
                        cardinalBlackPlaying=False
                    elif cardinalBlackRect.colliderect(warriorBlackRect3):
                        cardinalBlackRect.centerx = cardinalBlackxInit
                        cardinalBlackRect.centery = cardinalBlackyInit
                        counter -= 1
                        cardinalBlackPlaying=False


                if hadesBlackRect.collidepoint(event.pos):
                    if not hadesBlackPlaying:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                hadesBlackPlaying=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                hadesBlackPlaying=True
                elif hadesBlackPlaying:
                    if rectHadesBlack1.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack1.centerx
                        hadesBlackRect.centery = rectHadesBlack1.centery
                        counter += 1
                        hadesBlackPlaying=False
                    elif rectHadesBlack2.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack2.centerx
                        hadesBlackRect.centery = rectHadesBlack2.centery
                        counter += 1
                        hadesBlackPlaying=False
                    elif rectHadesBlack3.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack3.centerx
                        hadesBlackRect.centery = rectHadesBlack3.centery
                        counter += 1
                        hadesBlackPlaying=False
                    elif rectHadesBlack4.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack4.centerx
                        hadesBlackRect.centery = rectHadesBlack4.centery
                        counter += 1
                        hadesBlackPlaying=False
                    elif rectHadesBlack5.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack5.centerx
                        hadesBlackRect.centery = rectHadesBlack5.centery
                        counter += 1
                        hadesBlackPlaying=False
                    elif rectHadesBlack6.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack6.centerx
                        hadesBlackRect.centery = rectHadesBlack6.centery
                        counter += 1
                        hadesBlackPlaying=False
                    elif rectHadesBlack7.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack7.centerx
                        hadesBlackRect.centery = rectHadesBlack7.centery
                        counter += 1
                        hadesBlackPlaying=False
                    elif rectHadesBlack8.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack8.centerx
                        hadesBlackRect.centery = rectHadesBlack8.centery
                        counter += 1
                        hadesBlackPlaying=False
                    elif rectHadesBlack9.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack9.centerx
                        hadesBlackRect.centery = rectHadesBlack9.centery
                        counter += 1
                        hadesBlackPlaying=False
                    elif rectHadesBlack10.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack10.centerx
                        hadesBlackRect.centery = rectHadesBlack10.centery
                        counter += 1
                        hadesBlackPlaying=False
                    elif rectHadesBlack11.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack11.centerx
                        hadesBlackRect.centery = rectHadesBlack11.centery
                        counter += 1
                        hadesBlackPlaying=False
                    elif rectHadesBlack12.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack12.centerx
                        hadesBlackRect.centery = rectHadesBlack12.centery
                        counter += 1
                        hadesBlackPlaying=False
                    elif rectHadesBlack13.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack13.centerx
                        hadesBlackRect.centery = rectHadesBlack13.centery
                        counter += 1
                        hadesBlackPlaying=False
                    elif rectHadesBlack14.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack14.centerx
                        hadesBlackRect.centery = rectHadesBlack14.centery
                        counter += 1
                        hadesBlackPlaying=False
                    elif rectHadesBlack15.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack15.centerx
                        hadesBlackRect.centery = rectHadesBlack15.centery
                        counter += 1
                        hadesBlackPlaying=False
                    elif rectHadesBlack16.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack16.centerx
                        hadesBlackRect.centery = rectHadesBlack16.centery
                        counter += 1
                        hadesBlackPlaying=False
                    elif rectHadesBlack17.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack17.centerx
                        hadesBlackRect.centery = rectHadesBlack17.centery
                        counter += 1
                        hadesBlackPlaying=False
                    elif rectHadesBlack18.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack18.centerx
                        hadesBlackRect.centery = rectHadesBlack18.centery
                        counter += 1
                        hadesBlackPlaying=False
                    elif rectHadesBlack19.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack19.centerx
                        hadesBlackRect.centery = rectHadesBlack19.centery
                        counter += 1
                        hadesBlackPlaying=False
                    else:
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        hadesBlackPlaying=False
                    if hadesBlackRect.colliderect(plagueDoctorBlackRect):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        counter -= 1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(archbishopBlackRect):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        counter -= 1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(cardinalBlackRect):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        counter -= 1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(persephoneBlackRect):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        counter -= 1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(cardinalBlackRect1):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        counter -= 1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(archbishopBlackRect1):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        counter -= 1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(plagueDoctorBlackRect1):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        counter -= 1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(legionaryBlackRect):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        counter -= 1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(warriorBlackRect):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        counter -= 1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(legionaryBlackRect1):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        counter -= 1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(warriorBlackRect1):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        counter -= 1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(legionaryBlackRect2):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        counter -= 1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(warriorBlackRect2):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        counter -= 1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(legionaryBlackRect3):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        counter -= 1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(warriorBlackRect3):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        counter -= 1
                        hadesBlackPlaying=False

                if persephoneBlackRect.collidepoint(event.pos):
                    if not persephoneBlackPlaying:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                persephoneBlackPlaying=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                persephoneBlackPlaying=True
                elif persephoneBlackPlaying:
                    if rectPersephoneBlack1.collidepoint(event.pos):
                        persephoneBlackRect.centerx = rectPersephoneBlack1.centerx
                        persephoneBlackRect.centery = rectPersephoneBlack1.centery
                        counter += 1
                        persephoneBlackPlaying=False
                    elif rectPersephoneBlack2.collidepoint(event.pos):
                        persephoneBlackRect.centerx = rectPersephoneBlack2.centerx
                        persephoneBlackRect.centery = rectPersephoneBlack2.centery
                        counter += 1
                        persephoneBlackPlaying=False
                    elif rectPersephoneBlack3.collidepoint(event.pos):
                        persephoneBlackRect.centerx = rectPersephoneBlack3.centerx
                        persephoneBlackRect.centery = rectPersephoneBlack3.centery
                        counter += 1
                        persephoneBlackPlaying=False
                    elif rectPersephoneBlack4.collidepoint(event.pos):
                        persephoneBlackRect.centerx = rectPersephoneBlack4.centerx
                        persephoneBlackRect.centery = rectPersephoneBlack4.centery
                        counter += 1
                        persephoneBlackPlaying=False
                    elif rectPersephoneBlack5.collidepoint(event.pos):
                        persephoneBlackRect.centerx = rectPersephoneBlack5.centerx
                        persephoneBlackRect.centery = rectPersephoneBlack5.centery
                        counter += 1
                        persephoneBlackPlaying=False
                    elif rectPersephoneBlack6.collidepoint(event.pos):
                        persephoneBlackRect.centerx = rectPersephoneBlack6.centerx
                        persephoneBlackRect.centery = rectPersephoneBlack6.centery
                        counter += 1
                        persephoneBlackPlaying=False
                    elif rectPersephoneBlack7.collidepoint(event.pos):
                        persephoneBlackRect.centerx = rectPersephoneBlack7.centerx
                        persephoneBlackRect.centery = rectPersephoneBlack7.centery
                        counter += 1
                        persephoneBlackPlaying=False
                    elif rectPersephoneBlack8.collidepoint(event.pos):
                        persephoneBlackRect.centerx = rectPersephoneBlack8.centerx
                        persephoneBlackRect.centery = rectPersephoneBlack8.centery
                        counter += 1
                        persephoneBlackPlaying=False
                    else:
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        persephoneBlackPlaying=False
                    if persephoneBlackRect.colliderect(plagueDoctorBlackRect):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                    elif persephoneBlackRect.colliderect(archbishopBlackRect):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                    elif persephoneBlackRect.colliderect(cardinalBlackRect):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                    elif persephoneBlackRect.colliderect(hadesBlackRect):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                    elif persephoneBlackRect.colliderect(cardinalBlackRect1):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                    elif persephoneBlackRect.colliderect(archbishopBlackRect1):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                    elif persephoneBlackRect.colliderect(plagueDoctorBlackRect1):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                    elif persephoneBlackRect.colliderect(legionaryBlackRect):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                    elif persephoneBlackRect.colliderect(warriorBlackRect):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                    elif persephoneBlackRect.colliderect(legionaryBlackRect1):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                    elif persephoneBlackRect.colliderect(warriorBlackRect1):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                    elif persephoneBlackRect.colliderect(legionaryBlackRect2):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                    elif persephoneBlackRect.colliderect(warriorBlackRect2):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                    elif persephoneBlackRect.colliderect(legionaryBlackRect3):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                    elif persephoneBlackRect.colliderect(warriorBlackRect3):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False

                if cardinalBlackRect1.collidepoint(event.pos):
                    if not cardinalBlackPlaying1:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                cardinalBlackPlaying1=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                cardinalBlackPlaying1=True
                elif cardinalBlackPlaying1:
                    if rectCardinalBlack1_1.collidepoint(event.pos):
                        cardinalBlackRect1.centerx = rectCardinalBlack1_1.centerx
                        cardinalBlackRect1.centery = rectCardinalBlack1_1.centery
                        counter += 1
                        cardinalBlackPlaying1=False
                    elif rectCardinalBlack2_1.collidepoint(event.pos):
                        cardinalBlackRect1.centerx = rectCardinalBlack2_1.centerx
                        cardinalBlackRect1.centery = rectCardinalBlack2_1.centery
                        counter += 1
                        cardinalBlackPlaying1=False
                    elif rectCardinalBlack3_1.collidepoint(event.pos):
                        cardinalBlackRect1.centerx = rectCardinalBlack3_1.centerx
                        cardinalBlackRect1.centery = rectCardinalBlack3_1.centery
                        counter += 1
                        cardinalBlackPlaying1=False
                    elif rectCardinalBlack4_1.collidepoint(event.pos):
                        cardinalBlackRect1.centerx = rectCardinalBlack4_1.centerx
                        cardinalBlackRect1.centery = rectCardinalBlack4_1.centery
                        counter += 1
                        cardinalBlackPlaying1=False
                    else:
                        cardinalBlackRect1.centerx = cardinalBlackxInit1
                        cardinalBlackRect1.centery = cardinalBlackyInit1
                        cardinalBlackPlaying1=False
                    if cardinalBlackRect1.colliderect(plagueDoctorBlackRect):
                        cardinalBlackRect1.centerx = cardinalBlackxInit1
                        cardinalBlackRect1.centery = cardinalBlackyInit1
                        counter -= 1
                        cardinalBlackPlaying1=False
                    elif cardinalBlackRect1.colliderect(archbishopBlackRect):
                        cardinalBlackRect1.centerx = cardinalBlackxInit1
                        cardinalBlackRect1.centery = cardinalBlackyInit1
                        counter -= 1
                        cardinalBlackPlaying1=False
                    elif cardinalBlackRect1.colliderect(cardinalBlackRect):
                        cardinalBlackRect1.centerx = cardinalBlackxInit1
                        cardinalBlackRect1.centery = cardinalBlackyInit1
                        counter -= 1
                        cardinalBlackPlaying1=False
                    elif cardinalBlackRect1.colliderect(hadesBlackRect):
                        cardinalBlackRect1.centerx = cardinalBlackxInit1
                        cardinalBlackRect1.centery = cardinalBlackyInit1
                        counter -= 1
                        cardinalBlackPlaying1=False
                    elif cardinalBlackRect1.colliderect(persephoneBlackRect):
                        cardinalBlackRect1.centerx = cardinalBlackxInit1
                        cardinalBlackRect1.centery = cardinalBlackyInit1
                        counter -= 1
                        cardinalBlackPlaying1=False
                    elif cardinalBlackRect1.colliderect(archbishopBlackRect1):
                        cardinalBlackRect1.centerx = cardinalBlackxInit1
                        cardinalBlackRect1.centery = cardinalBlackyInit1
                        counter -= 1
                        cardinalBlackPlaying1=False
                    elif cardinalBlackRect1.colliderect(plagueDoctorBlackRect1):
                        cardinalBlackRect1.centerx = cardinalBlackxInit1
                        cardinalBlackRect1.centery = cardinalBlackyInit1
                        counter -= 1
                        cardinalBlackPlaying1=False
                    elif cardinalBlackRect1.colliderect(legionaryBlackRect):
                        cardinalBlackRect1.centerx = cardinalBlackxInit1
                        cardinalBlackRect1.centery = cardinalBlackyInit1
                        counter -= 1
                        cardinalBlackPlaying1=False
                    elif cardinalBlackRect1.colliderect(warriorBlackRect):
                        cardinalBlackRect1.centerx = cardinalBlackxInit1
                        cardinalBlackRect1.centery = cardinalBlackyInit1
                        counter -= 1
                        cardinalBlackPlaying1=False
                    elif cardinalBlackRect1.colliderect(legionaryBlackRect1):
                        cardinalBlackRect1.centerx = cardinalBlackxInit1
                        cardinalBlackRect1.centery = cardinalBlackyInit1
                        counter -= 1
                        cardinalBlackPlaying1=False
                    elif cardinalBlackRect1.colliderect(warriorBlackRect1):
                        cardinalBlackRect1.centerx = cardinalBlackxInit1
                        cardinalBlackRect1.centery = cardinalBlackyInit1
                        counter -= 1
                        cardinalBlackPlaying1=False
                    elif cardinalBlackRect1.colliderect(legionaryBlackRect2):
                        cardinalBlackRect1.centerx = cardinalBlackxInit1
                        cardinalBlackRect1.centery = cardinalBlackyInit1
                        counter -= 1
                        cardinalBlackPlaying1=False
                    elif cardinalBlackRect1.colliderect(warriorBlackRect2):
                        cardinalBlackRect1.centerx = cardinalBlackxInit1
                        cardinalBlackRect1.centery = cardinalBlackyInit1
                        counter -= 1
                        cardinalBlackPlaying1=False
                    elif cardinalBlackRect1.colliderect(legionaryBlackRect3):
                        cardinalBlackRect1.centerx = cardinalBlackxInit1
                        cardinalBlackRect1.centery = cardinalBlackyInit1
                        counter -= 1
                        cardinalBlackPlaying1=False
                    elif cardinalBlackRect1.colliderect(warriorBlackRect3):
                        cardinalBlackRect1.centerx = cardinalBlackxInit1
                        cardinalBlackRect1.centery = cardinalBlackyInit1
                        counter -= 1
                        cardinalBlackPlaying1=False


                if archbishopBlackRect1.collidepoint(event.pos):
                    if not archbishopBlackPlaying1:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                archbishopBlackPlaying1=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                archbishopBlackPlaying1=True
                elif archbishopBlackPlaying1:
                    if rectArchbishopBlack1_1.collidepoint(event.pos):
                        archbishopBlackRect1.centerx = rectArchbishopBlack1_1.centerx
                        archbishopBlackRect1.centery = rectArchbishopBlack1_1.centery
                        counter += 1
                        archbishopBlackPlaying1=False
                    elif rectArchbishopBlack2_1.collidepoint(event.pos):
                        archbishopBlackRect1.centerx = rectArchbishopBlack2_1.centerx
                        archbishopBlackRect1.centery = rectArchbishopBlack2_1.centery
                        counter += 1
                        archbishopBlackPlaying1=False
                    elif rectArchbishopBlack3_1.collidepoint(event.pos):
                        archbishopBlackRect1.centerx = rectArchbishopBlack3_1.centerx
                        archbishopBlackRect1.centery = rectArchbishopBlack3_1.centery
                        counter += 1
                        archbishopBlackPlaying1=False
                    elif rectArchbishopBlack4_1.collidepoint(event.pos):
                        archbishopBlackRect1.centerx = rectArchbishopBlack4_1.centerx
                        archbishopBlackRect1.centery = rectArchbishopBlack4_1.centery
                        counter += 1
                        archbishopBlackPlaying1=False
                    elif rectArchbishopBlack5_1.collidepoint(event.pos):
                        archbishopBlackRect1.centerx = rectArchbishopBlack5_1.centerx
                        archbishopBlackRect1.centery = rectArchbishopBlack5_1.centery
                        counter += 1
                        archbishopBlackPlaying1=False
                    elif rectArchbishopBlack6_1.collidepoint(event.pos):
                        archbishopBlackRect1.centerx = rectArchbishopBlack6_1.centerx
                        archbishopBlackRect1.centery = rectArchbishopBlack6_1.centery
                        counter += 1
                        archbishopBlackPlaying1=False
                    elif rectArchbishopBlack7_1.collidepoint(event.pos):
                        archbishopBlackRect1.centerx = rectArchbishopBlack7_1.centerx
                        archbishopBlackRect1.centery = rectArchbishopBlack7_1.centery
                        counter += 1
                        archbishopBlackPlaying1=False
                    elif rectArchbishopBlack8_1.collidepoint(event.pos):
                        archbishopBlackRect1.centerx = rectArchbishopBlack8_1.centerx
                        archbishopBlackRect1.centery = rectArchbishopBlack8_1.centery
                        counter += 1
                        archbishopBlackPlaying1=False
                    elif rectArchbishopBlack9_1.collidepoint(event.pos):
                        archbishopBlackRect1.centerx = rectArchbishopBlack9_1.centerx
                        archbishopBlackRect1.centery = rectArchbishopBlack9_1.centery
                        counter += 1
                        archbishopBlackPlaying1=False
                    elif rectArchbishopBlack10_1.collidepoint(event.pos):
                        archbishopBlackRect1.centerx = rectArchbishopBlack10_1.centerx
                        archbishopBlackRect1.centery = rectArchbishopBlack10_1.centery
                        counter += 1
                        archbishopBlackPlaying1=False
                    elif rectArchbishopBlack11_1.collidepoint(event.pos):
                        archbishopBlackRect1.centerx = rectArchbishopBlack11_1.centerx
                        archbishopBlackRect1.centery = rectArchbishopBlack11_1.centery
                        counter += 1
                        archbishopBlackPlaying1=False
                    elif rectArchbishopBlack12_1.collidepoint(event.pos):
                        archbishopBlackRect1.centerx = rectArchbishopBlack12_1.centerx
                        archbishopBlackRect1.centery = rectArchbishopBlack12_1.centery
                        counter += 1
                        archbishopBlackPlaying1=False
                    else:
                        archbishopBlackRect1.centerx = archbishopBlackxInit1
                        archbishopBlackRect1.centery = archbishopBlackyInit1
                        archbishopBlackPlaying1=False
                    if archbishopBlackRect1.colliderect(plagueDoctorBlackRect):
                        archbishopBlackRect1.centerx = archbishopBlackxInit1
                        archbishopBlackRect1.centery = archbishopBlackyInit1
                        counter -= 1
                        archbishopBlackPlaying1=False
                    elif archbishopBlackRect1.colliderect(archbishopBlackRect):
                        archbishopBlackRect1.centerx = archbishopBlackxInit1
                        archbishopBlackRect1.centery = archbishopBlackyInit1
                        counter -= 1
                        archbishopBlackPlaying1=False
                    elif archbishopBlackRect1.colliderect(cardinalBlackRect):
                        archbishopBlackRect1.centerx = archbishopBlackxInit1
                        archbishopBlackRect1.centery = archbishopBlackyInit1
                        counter -= 1
                        archbishopBlackPlaying1=False
                    elif archbishopBlackRect1.colliderect(hadesBlackRect):
                        archbishopBlackRect1.centerx = archbishopBlackxInit1
                        archbishopBlackRect1.centery = archbishopBlackyInit1
                        counter -= 1
                        archbishopBlackPlaying1=False
                    elif archbishopBlackRect1.colliderect(persephoneBlackRect):
                        archbishopBlackRect1.centerx = archbishopBlackxInit1
                        archbishopBlackRect1.centery = archbishopBlackyInit1
                        counter -= 1
                        archbishopBlackPlaying1=False
                    elif archbishopBlackRect1.colliderect(cardinalBlackRect1):
                        archbishopBlackRect1.centerx = archbishopBlackxInit1
                        archbishopBlackRect1.centery = archbishopBlackyInit1
                        counter -= 1
                        archbishopBlackPlaying1=False
                    elif archbishopBlackRect1.colliderect(plagueDoctorBlackRect1):
                        archbishopBlackRect1.centerx = archbishopBlackxInit1
                        archbishopBlackRect1.centery = archbishopBlackyInit1
                        counter -= 1
                        archbishopBlackPlaying1=False
                    elif archbishopBlackRect1.colliderect(legionaryBlackRect):
                        archbishopBlackRect1.centerx = archbishopBlackxInit1
                        archbishopBlackRect1.centery = archbishopBlackyInit1
                        counter -= 1
                        archbishopBlackPlaying1=False
                    elif archbishopBlackRect1.colliderect(warriorBlackRect):
                        archbishopBlackRect1.centerx = archbishopBlackxInit1
                        archbishopBlackRect1.centery = archbishopBlackyInit1
                        counter -= 1
                        archbishopBlackPlaying1=False
                    elif archbishopBlackRect1.colliderect(legionaryBlackRect1):
                        archbishopBlackRect1.centerx = archbishopBlackxInit1
                        archbishopBlackRect1.centery = archbishopBlackyInit1
                        counter -= 1
                        archbishopBlackPlaying1=False
                    elif archbishopBlackRect1.colliderect(warriorBlackRect1):
                        archbishopBlackRect1.centerx = archbishopBlackxInit1
                        archbishopBlackRect1.centery = archbishopBlackyInit1
                        counter -= 1
                        archbishopBlackPlaying1=False
                    elif archbishopBlackRect1.colliderect(legionaryBlackRect2):
                        archbishopBlackRect1.centerx = archbishopBlackxInit1
                        archbishopBlackRect1.centery = archbishopBlackyInit1
                        counter -= 1
                        archbishopBlackPlaying1=False
                    elif archbishopBlackRect1.colliderect(warriorBlackRect2):
                        archbishopBlackRect1.centerx = archbishopBlackxInit1
                        archbishopBlackRect1.centery = archbishopBlackyInit1
                        counter -= 1
                        archbishopBlackPlaying1=False
                    elif archbishopBlackRect1.colliderect(legionaryBlackRect3):
                        archbishopBlackRect1.centerx = archbishopBlackxInit1
                        archbishopBlackRect1.centery = archbishopBlackyInit1
                        counter -= 1
                        archbishopBlackPlaying1=False
                    elif archbishopBlackRect1.colliderect(warriorBlackRect3):
                        archbishopBlackRect1.centerx = archbishopBlackxInit1
                        archbishopBlackRect1.centery = archbishopBlackyInit1
                        counter -= 1
                        archbishopBlackPlaying1=False

                if plagueDoctorBlackRect1.collidepoint(event.pos):
                    if not plagueDoctorBlackPlaying1:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                plagueDoctorBlackPlaying1=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                plagueDoctorBlackPlaying1=True
                elif plagueDoctorBlackPlaying1:
                    if rectPlagueBlack1_1.collidepoint(event.pos):
                        plagueDoctorBlackRect1.centerx = rectPlagueBlack1_1.centerx
                        plagueDoctorBlackRect1.centery = rectPlagueBlack1_1.centery
                        counter += 1
                        plagueDoctorBlackPlaying1=False
                    elif rectPlagueBlack2_1.collidepoint(event.pos):
                        plagueDoctorBlackRect1.centerx = rectPlagueBlack2_1.centerx
                        plagueDoctorBlackRect1.centery = rectPlagueBlack2_1.centery
                        counter += 1
                        plagueDoctorBlackPlaying1=False
                    elif rectPlagueBlack3_1.collidepoint(event.pos):
                        plagueDoctorBlackRect1.centerx = rectPlagueBlack3_1.centerx
                        plagueDoctorBlackRect1.centery = rectPlagueBlack3_1.centery
                        counter += 1
                        plagueDoctorBlackPlaying1=False
                    elif rectPlagueBlack4_1.collidepoint(event.pos):
                        plagueDoctorBlackRect1.centerx = rectPlagueBlack4_1.centerx
                        plagueDoctorBlackRect1.centery = rectPlagueBlack4_1.centery
                        counter += 1
                        plagueDoctorBlackPlaying1=False
                    elif rectPlagueBlack5_1.collidepoint(event.pos):
                        plagueDoctorBlackRect1.centerx = rectPlagueBlack5_1.centerx
                        plagueDoctorBlackRect1.centery = rectPlagueBlack5_1.centery
                        counter += 1
                        plagueDoctorBlackPlaying1=False
                    elif rectPlagueBlack6_1.collidepoint(event.pos):
                        plagueDoctorBlackRect1.centerx = rectPlagueBlack6_1.centerx
                        plagueDoctorBlackRect1.centery = rectPlagueBlack6_1.centery
                        counter += 1
                        plagueDoctorBlackPlaying1=False
                    elif rectPlagueBlack7_1.collidepoint(event.pos):
                        plagueDoctorBlackRect1.centerx = rectPlagueBlack7_1.centerx
                        plagueDoctorBlackRect1.centery = rectPlagueBlack7_1.centery
                        counter += 1
                        plagueDoctorBlackPlaying1=False
                    elif rectPlagueBlack8_1.collidepoint(event.pos):
                        plagueDoctorBlackRect1.centerx = rectPlagueBlack8_1.centerx
                        plagueDoctorBlackRect1.centery = rectPlagueBlack8_1.centery
                        counter += 1
                        plagueDoctorBlackPlaying1=False
                    elif rectPlagueBlack9_1.collidepoint(event.pos):
                        plagueDoctorBlackRect1.centerx = rectPlagueBlack9_1.centerx
                        plagueDoctorBlackRect1.centery = rectPlagueBlack9_1.centery
                        counter += 1
                        plagueDoctorBlackPlaying1=False
                    elif rectPlagueBlack10_1.collidepoint(event.pos):
                        plagueDoctorBlackRect1.centerx = rectPlagueBlack10_1.centerx
                        plagueDoctorBlackRect1.centery = rectPlagueBlack10_1.centery
                        counter += 1
                        plagueDoctorBlackPlaying1=False
                    elif rectPlagueBlack11_1.collidepoint(event.pos):
                        plagueDoctorBlackRect1.centerx = rectPlagueBlack11_1.centerx
                        plagueDoctorBlackRect1.centery = rectPlagueBlack11_1.centery
                        counter += 1
                        plagueDoctorBlackPlaying1=False
                    elif rectPlagueBlack12_1.collidepoint(event.pos):
                        plagueDoctorBlackRect1.centerx = rectPlagueBlack12_1.centerx
                        plagueDoctorBlackRect1.centery = rectPlagueBlack12_1.centery
                        counter += 1
                        plagueDoctorBlackPlaying1=False
                    elif rectPlagueBlack13_1.collidepoint(event.pos):
                        plagueDoctorBlackRect1.centerx = rectPlagueBlack13_1.centerx
                        plagueDoctorBlackRect1.centery = rectPlagueBlack13_1.centery
                        counter += 1
                        plagueDoctorBlackPlaying1=False
                    elif rectPlagueBlack14_1.collidepoint(event.pos):
                        plagueDoctorBlackRect1.centerx = rectPlagueBlack14_1.centerx
                        plagueDoctorBlackRect1.centery = rectPlagueBlack14_1.centery
                        counter += 1
                        plagueDoctorBlackPlaying1=False
                    elif rectPlagueBlack15_1.collidepoint(event.pos):
                        plagueDoctorBlackRect1.centerx = rectPlagueBlack15_1.centerx
                        plagueDoctorBlackRect1.centery = rectPlagueBlack15_1.centery
                        counter += 1
                        plagueDoctorBlackPlaying1=False
                    elif rectPlagueBlack16_1.collidepoint(event.pos):
                        plagueDoctorBlackRect1.centerx = rectPlagueBlack16_1.centerx
                        plagueDoctorBlackRect1.centery = rectPlagueBlack16_1.centery
                        counter += 1
                        plagueDoctorBlackPlaying1=False
                    elif rectPlagueBlack17_1.collidepoint(event.pos):
                        plagueDoctorBlackRect1.centerx = rectPlagueBlack17_1.centerx
                        plagueDoctorBlackRect1.centery = rectPlagueBlack17_1.centery
                        counter += 1
                        plagueDoctorBlackPlaying1=False
                    elif rectPlagueBlack18_1.collidepoint(event.pos):
                        plagueDoctorBlackRect1.centerx = rectPlagueBlack18_1.centerx
                        plagueDoctorBlackRect1.centery = rectPlagueBlack18_1.centery
                        counter += 1
                        plagueDoctorBlackPlaying1=False
                    else:
                        plagueDoctorBlackRect1.centerx = plagueBlackxInit1
                        plagueDoctorBlackRect1.centery = plagueBlackyInit1
                        plagueDoctorBlackPlaying1=False
                    if plagueDoctorBlackRect1.colliderect(plagueDoctorBlackRect):
                        plagueDoctorBlackRect1.centerx = plagueBlackxInit1
                        plagueDoctorBlackRect1.centery = plagueBlackyInit1
                        counter -= 1
                        plagueDoctorBlackPlaying1=False
                    elif plagueDoctorBlackRect1.colliderect(archbishopBlackRect):
                        plagueDoctorBlackRect1.centerx = plagueBlackxInit1
                        plagueDoctorBlackRect1.centery = plagueBlackyInit1
                        counter -= 1
                        plagueDoctorBlackPlaying1=False
                    elif plagueDoctorBlackRect1.colliderect(cardinalBlackRect):
                        plagueDoctorBlackRect1.centerx = plagueBlackxInit1
                        plagueDoctorBlackRect1.centery = plagueBlackyInit1
                        counter -= 1
                        plagueDoctorBlackPlaying1=False
                    elif plagueDoctorBlackRect1.colliderect(hadesBlackRect):
                        plagueDoctorBlackRect1.centerx = plagueBlackxInit1
                        plagueDoctorBlackRect1.centery = plagueBlackyInit1
                        counter -= 1
                        plagueDoctorBlackPlaying1=False
                    elif plagueDoctorBlackRect1.colliderect(persephoneBlackRect):
                        plagueDoctorBlackRect1.centerx = plagueBlackxInit1
                        plagueDoctorBlackRect1.centery = plagueBlackyInit1
                        counter -= 1
                        plagueDoctorBlackPlaying1=False
                    elif plagueDoctorBlackRect1.colliderect(cardinalBlackRect1):
                        plagueDoctorBlackRect1.centerx = plagueBlackxInit1
                        plagueDoctorBlackRect1.centery = plagueBlackyInit1
                        counter -= 1
                        plagueDoctorBlackPlaying1=False
                    elif plagueDoctorBlackRect1.colliderect(archbishopBlackRect1):
                        plagueDoctorBlackRect1.centerx = plagueBlackxInit1
                        plagueDoctorBlackRect1.centery = plagueBlackyInit1
                        counter -= 1
                        plagueDoctorBlackPlaying1=False
                    elif plagueDoctorBlackRect1.colliderect(legionaryBlackRect):
                        plagueDoctorBlackRect1.centerx = plagueBlackxInit1
                        plagueDoctorBlackRect1.centery = plagueBlackyInit1
                        counter -= 1
                        plagueDoctorBlackPlaying1=False
                    elif plagueDoctorBlackRect1.colliderect(warriorBlackRect):
                        plagueDoctorBlackRect1.centerx = plagueBlackxInit1
                        plagueDoctorBlackRect1.centery = plagueBlackyInit1
                        counter -= 1
                        plagueDoctorBlackPlaying1=False
                    elif plagueDoctorBlackRect1.colliderect(legionaryBlackRect1):
                        plagueDoctorBlackRect1.centerx = plagueBlackxInit1
                        plagueDoctorBlackRect1.centery = plagueBlackyInit1
                        counter -= 1
                        plagueDoctorBlackPlaying1=False
                    elif plagueDoctorBlackRect1.colliderect(warriorBlackRect1):
                        plagueDoctorBlackRect1.centerx = plagueBlackxInit1
                        plagueDoctorBlackRect1.centery = plagueBlackyInit1
                        counter -= 1
                        plagueDoctorBlackPlaying1=False
                    elif plagueDoctorBlackRect1.colliderect(legionaryBlackRect2):
                        plagueDoctorBlackRect1.centerx = plagueBlackxInit1
                        plagueDoctorBlackRect1.centery = plagueBlackyInit1
                        counter -= 1
                        plagueDoctorBlackPlaying1=False
                    elif plagueDoctorBlackRect1.colliderect(warriorBlackRect2):
                        plagueDoctorBlackRect1.centerx = plagueBlackxInit1
                        plagueDoctorBlackRect1.centery = plagueBlackyInit1
                        counter -= 1
                        plagueDoctorBlackPlaying1=False
                    elif plagueDoctorBlackRect1.colliderect(legionaryBlackRect3):
                        plagueDoctorBlackRect1.centerx = plagueBlackxInit1
                        plagueDoctorBlackRect1.centery = plagueBlackyInit1
                        counter -= 1
                        plagueDoctorBlackPlaying1=False
                    elif plagueDoctorBlackRect1.colliderect(warriorBlackRect3):
                        plagueDoctorBlackRect1.centerx = plagueBlackxInit1
                        plagueDoctorBlackRect1.centery = plagueBlackyInit1
                        counter -= 1
                        plagueDoctorBlackPlaying1=False

                if legionaryBlackRect.collidepoint(event.pos):
                    if not legionaryBlackPlaying:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                legionaryBlackPlaying=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                legionaryBlackPlaying=True
                elif legionaryBlackPlaying:
                    if rectLegionaryBlack1.collidepoint(event.pos):
                        legionar_cerny_x_abilita = legionaryBlackxInit
                        legionar_cerny_y_abilita = legionaryBlackyInit
                        legionaryBlackRect.centerx = rectLegionaryBlack1.centerx
                        legionaryBlackRect.centery = rectLegionaryBlack1.centery
                        counter += 1
                        legionaryBlackPlaying=False
                    elif rectLegionaryBlack2.collidepoint(event.pos):
                        legionar_cerny_x_abilita = legionaryBlackxInit
                        legionar_cerny_y_abilita = legionaryBlackyInit
                        legionaryBlackRect.centerx = rectLegionaryBlack2.centerx
                        legionaryBlackRect.centery = rectLegionaryBlack2.centery
                        counter += 1
                        legionaryBlackPlaying=False
                    elif rectLegionaryBlack3.collidepoint(event.pos):
                        legionar_cerny_x_abilita = legionaryBlackxInit
                        legionar_cerny_y_abilita = legionaryBlackyInit
                        legionaryBlackRect.centerx = rectLegionaryBlack3.centerx
                        legionaryBlackRect.centery = rectLegionaryBlack3.centery
                        counter += 1
                        legionaryBlackPlaying=False
                    else:
                        legionaryBlackRect.centerx = legionaryBlackxInit
                        legionaryBlackRect.centery = legionaryBlackyInit
                        legionaryBlackPlaying=False
                    if legionaryBlackRect.colliderect(plagueDoctorBlackRect):
                        legionaryBlackRect.centerx = legionaryBlackxInit
                        legionaryBlackRect.centery = legionaryBlackyInit
                        counter -= 1
                        legionaryBlackPlaying=False
                    elif legionaryBlackRect.colliderect(archbishopBlackRect):
                        legionaryBlackRect.centerx = legionaryBlackxInit
                        legionaryBlackRect.centery = legionaryBlackyInit
                        counter -= 1
                        legionaryBlackPlaying=False
                    elif legionaryBlackRect.colliderect(cardinalBlackRect):
                        legionaryBlackRect.centerx = legionaryBlackxInit
                        legionaryBlackRect.centery = legionaryBlackyInit
                        counter -= 1
                        legionaryBlackPlaying=False
                    elif legionaryBlackRect.colliderect(hadesBlackRect):
                        legionaryBlackRect.centerx = legionaryBlackxInit
                        legionaryBlackRect.centery = legionaryBlackyInit
                        counter -= 1
                        legionaryBlackPlaying=False
                    elif legionaryBlackRect.colliderect(persephoneBlackRect):
                        legionaryBlackRect.centerx = legionaryBlackxInit
                        legionaryBlackRect.centery = legionaryBlackyInit
                        counter -= 1
                        legionaryBlackPlaying=False
                    elif legionaryBlackRect.colliderect(cardinalBlackRect1):
                        legionaryBlackRect.centerx = legionaryBlackxInit
                        legionaryBlackRect.centery = legionaryBlackyInit
                        counter -= 1
                        legionaryBlackPlaying=False
                    elif legionaryBlackRect.colliderect(archbishopBlackRect1):
                        legionaryBlackRect.centerx = legionaryBlackxInit
                        legionaryBlackRect.centery = legionaryBlackyInit
                        counter -= 1
                        legionaryBlackPlaying=False
                    elif legionaryBlackRect.colliderect(plagueDoctorBlackRect1):
                        legionaryBlackRect.centerx = legionaryBlackxInit
                        legionaryBlackRect.centery = legionaryBlackyInit
                        counter -= 1
                        legionaryBlackPlaying=False
                    elif legionaryBlackRect.colliderect(warriorBlackRect):
                        legionaryBlackRect.centerx = legionaryBlackxInit
                        legionaryBlackRect.centery = legionaryBlackyInit
                        counter -= 1
                        legionaryBlackPlaying=False
                    elif legionaryBlackRect.colliderect(legionaryBlackRect1):
                        legionaryBlackRect.centerx = legionaryBlackxInit
                        legionaryBlackRect.centery = legionaryBlackyInit
                        counter -= 1
                        legionaryBlackPlaying=False
                    elif legionaryBlackRect.colliderect(warriorBlackRect1):
                        legionaryBlackRect.centerx = legionaryBlackxInit
                        legionaryBlackRect.centery = legionaryBlackyInit
                        counter -= 1
                        legionaryBlackPlaying=False
                    elif legionaryBlackRect.colliderect(legionaryBlackRect2):
                        legionaryBlackRect.centerx = legionaryBlackxInit
                        legionaryBlackRect.centery = legionaryBlackyInit
                        counter -= 1
                        legionaryBlackPlaying=False
                    elif legionaryBlackRect.colliderect(warriorBlackRect2):
                        legionaryBlackRect.centerx = legionaryBlackxInit
                        legionaryBlackRect.centery = legionaryBlackyInit
                        counter -= 1
                        legionaryBlackPlaying=False
                    elif legionaryBlackRect.colliderect(legionaryBlackRect3):
                        legionaryBlackRect.centerx = legionaryBlackxInit
                        legionaryBlackRect.centery = legionaryBlackyInit
                        counter -= 1
                        legionaryBlackPlaying=False
                    elif legionaryBlackRect.colliderect(warriorBlackRect3):
                        legionaryBlackRect.centerx = legionaryBlackxInit
                        legionaryBlackRect.centery = legionaryBlackyInit
                        counter -= 1
                        legionaryBlackPlaying=False

                if warriorBlackRect.collidepoint(event.pos):
                    if not warriorBlackPlaying:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                warriorBlackPlaying=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                warriorBlackPlaying=True
                elif warriorBlackPlaying:
                    if rectWarriorBlack1Ability.collidepoint(event.pos) and (counter - 1) % 4 == 0:
                        warriorBlackRect.centerx = rectWarriorBlack1Ability.centerx
                        warriorBlackRect.centery = rectWarriorBlack1Ability.centery
                        counter += 1
                        warriorBlackPlaying=False
                    elif rectWarriorBlack2Ability.collidepoint(event.pos) and (counter - 1) % 4 == 0:
                        warriorBlackRect.centerx = rectWarriorBlack2Ability.centerx
                        warriorBlackRect.centery = rectWarriorBlack2Ability.centery
                        counter += 1
                        warriorBlackPlaying=False
                    elif rectWarriorBlack3Ability.collidepoint(event.pos) and (counter - 1) % 4 == 0:
                        warriorBlackRect.centerx = rectWarriorBlack3Ability.centerx
                        warriorBlackRect.centery = rectWarriorBlack3Ability.centery
                        counter += 1
                        warriorBlackPlaying=False
                    elif rectWarriorBlack4Ability.collidepoint(event.pos) and (counter - 1) % 4 == 0:
                        warriorBlackRect.centerx = rectWarriorBlack4Ability.centerx
                        warriorBlackRect.centery = rectWarriorBlack4Ability.centery
                        counter += 1
                        warriorBlackPlaying=False
                    elif rectWarriorBlack1.collidepoint(event.pos):
                        warriorBlackRect.centerx = rectWarriorBlack1.centerx
                        warriorBlackRect.centery = rectWarriorBlack1.centery
                        counter += 1
                        warriorBlackPlaying=False
                    elif rectWarriorBlack2.collidepoint(event.pos):
                        warriorBlackRect.centerx = rectWarriorBlack2.centerx
                        warriorBlackRect.centery = rectWarriorBlack2.centery
                        counter += 1
                        warriorBlackPlaying=False
                    elif rectWarriorBlack3.collidepoint(event.pos):
                        warriorBlackRect.centerx = rectWarriorBlack3.centerx
                        warriorBlackRect.centery = rectWarriorBlack3.centery
                        counter += 1
                        warriorBlackPlaying=False
                    elif rectWarriorBlack4.collidepoint(event.pos):
                        warriorBlackRect.centerx = rectWarriorBlack4.centerx
                        warriorBlackRect.centery = rectWarriorBlack4.centery
                        counter += 1
                        warriorBlackPlaying=False
                    else:
                        warriorBlackRect.centerx = warriorBlackxInit
                        warriorBlackRect.centery = warriorBlackyInit
                        warriorBlackPlaying=False
                    if warriorBlackRect.colliderect(plagueDoctorBlackRect):
                        warriorBlackRect.centerx = warriorBlackxInit
                        warriorBlackRect.centery = warriorBlackyInit
                        counter -= 1
                        warriorBlackPlaying=False
                    elif warriorBlackRect.colliderect(archbishopBlackRect):
                        warriorBlackRect.centerx = warriorBlackxInit
                        warriorBlackRect.centery = warriorBlackyInit
                        counter -= 1
                        warriorBlackPlaying=False
                    elif warriorBlackRect.colliderect(cardinalBlackRect):
                        warriorBlackRect.centerx = warriorBlackxInit
                        warriorBlackRect.centery = warriorBlackyInit
                        counter -= 1
                        warriorBlackPlaying=False
                    elif warriorBlackRect.colliderect(hadesBlackRect):
                        warriorBlackRect.centerx = warriorBlackxInit
                        warriorBlackRect.centery = warriorBlackyInit
                        counter -= 1
                        warriorBlackPlaying=False
                    elif warriorBlackRect.colliderect(persephoneBlackRect):
                        warriorBlackRect.centerx = warriorBlackxInit
                        warriorBlackRect.centery = warriorBlackyInit
                        counter -= 1
                        warriorBlackPlaying=False
                    elif warriorBlackRect.colliderect(cardinalBlackRect1):
                        warriorBlackRect.centerx = warriorBlackxInit
                        warriorBlackRect.centery = warriorBlackyInit
                        counter -= 1
                        warriorBlackPlaying=False
                    elif warriorBlackRect.colliderect(archbishopBlackRect1):
                        warriorBlackRect.centerx = warriorBlackxInit
                        warriorBlackRect.centery = warriorBlackyInit
                        counter -= 1
                        warriorBlackPlaying=False
                    elif warriorBlackRect.colliderect(plagueDoctorBlackRect1):
                        warriorBlackRect.centerx = warriorBlackxInit
                        warriorBlackRect.centery = warriorBlackyInit
                        counter -= 1
                        warriorBlackPlaying=False
                    elif warriorBlackRect.colliderect(legionaryBlackRect):
                        warriorBlackRect.centerx = warriorBlackxInit
                        warriorBlackRect.centery = warriorBlackyInit
                        counter -= 1
                        warriorBlackPlaying=False
                    elif warriorBlackRect.colliderect(legionaryBlackRect1):
                        warriorBlackRect.centerx = warriorBlackxInit
                        warriorBlackRect.centery = warriorBlackyInit
                        counter -= 1
                        warriorBlackPlaying=False
                    elif warriorBlackRect.colliderect(warriorBlackRect1):
                        warriorBlackRect.centerx = warriorBlackxInit
                        warriorBlackRect.centery = warriorBlackyInit
                        counter -= 1
                        warriorBlackPlaying=False
                    elif warriorBlackRect.colliderect(legionaryBlackRect2):
                        warriorBlackRect.centerx = warriorBlackxInit
                        warriorBlackRect.centery = warriorBlackyInit
                        counter -= 1
                        warriorBlackPlaying=False
                    elif warriorBlackRect.colliderect(warriorBlackRect2):
                        warriorBlackRect.centerx = warriorBlackxInit
                        warriorBlackRect.centery = warriorBlackyInit
                        counter -= 1
                        warriorBlackPlaying=False
                    elif warriorBlackRect.colliderect(legionaryBlackRect3):
                        warriorBlackRect.centerx = warriorBlackxInit
                        warriorBlackRect.centery = warriorBlackyInit
                        counter -= 1
                        warriorBlackPlaying=False
                    elif warriorBlackRect.colliderect(warriorBlackRect3):
                        warriorBlackRect.centerx = warriorBlackxInit
                        warriorBlackRect.centery = warriorBlackyInit
                        counter -= 1
                        warriorBlackPlaying=False
                        
                if warriorBlackRect1.collidepoint(event.pos):
                    if not warriorBlackPlaying1:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                warriorBlackPlaying1=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                warriorBlackPlaying1=True
                elif warriorBlackPlaying1:
                    if rectWarriorBlack1_1Ability.collidepoint(event.pos) and (counter - 1) % 4 == 0:
                        warriorBlackRect1.centerx = rectWarriorBlack1_1Ability.centerx
                        warriorBlackRect1.centery = rectWarriorBlack1_1Ability.centery
                        counter += 1
                        warriorBlackPlaying1=False
                    elif rectWarriorBlack2_1Ability.collidepoint(event.pos) and (counter - 1) % 4 == 0:
                        warriorBlackRect1.centerx = rectWarriorBlack2_1Ability.centerx
                        warriorBlackRect1.centery = rectWarriorBlack2_1Ability.centery
                        counter += 1
                        warriorBlackPlaying1=False
                    elif rectWarriorBlack3_1Ability.collidepoint(event.pos) and (counter - 1) % 4 == 0:
                        warriorBlackRect1.centerx = rectWarriorBlack3_1Ability.centerx
                        warriorBlackRect1.centery = rectWarriorBlack3_1Ability.centery
                        counter += 1
                        warriorBlackPlaying1=False
                    elif rectWarriorBlack4_1Ability.collidepoint(event.pos) and (counter - 1) % 4 == 0:
                        warriorBlackRect1.centerx = rectWarriorBlack4_1Ability.centerx
                        warriorBlackRect1.centery = rectWarriorBlack4_1Ability.centery
                        counter += 1
                        warriorBlackPlaying1=False
                    elif rectWarriorBlack1_1.collidepoint(event.pos):
                        warriorBlackRect1.centerx = rectWarriorBlack1_1.centerx
                        warriorBlackRect1.centery = rectWarriorBlack1_1.centery
                        counter += 1
                        warriorBlackPlaying1=False
                    elif rectWarriorBlack2_1.collidepoint:
                        warriorBlackRect1.centerx = rectWarriorBlack2_1.centerx
                        warriorBlackRect1.centery = rectWarriorBlack2_1.centery
                        counter += 1
                        warriorBlackPlaying1=False
                    elif rectWarriorBlack3_1.colliderect(rectWarriorBlack3_1):
                        warriorBlackRect1.centerx = rectWarriorBlack3_1.centerx
                        warriorBlackRect1.centery = rectWarriorBlack3_1.centery
                        counter += 1
                        warriorBlackPlaying1=False
                    elif rectWarriorBlack4_1.colliderect(rectWarriorBlack4_1):
                        warriorBlackRect1.centerx = rectWarriorBlack4_1.centerx
                        warriorBlackRect1.centery = rectWarriorBlack4_1.centery
                        counter += 1
                        warriorBlackPlaying1=False
                    else:
                        warriorBlackRect1.centerx = warriorBlackxInit1
                        warriorBlackRect1.centery = warriorBlackyInit1
                        warriorBlackPlaying1=False
                    if warriorBlackRect1.colliderect(plagueDoctorBlackRect):
                        warriorBlackRect1.centerx = warriorBlackxInit1
                        warriorBlackRect1.centery = warriorBlackyInit1
                        counter -= 1
                        warriorBlackPlaying1=False
                    elif warriorBlackRect1.colliderect(archbishopBlackRect):
                        warriorBlackRect1.centerx = warriorBlackxInit1
                        warriorBlackRect1.centery = warriorBlackyInit1
                        counter -= 1
                        warriorBlackPlaying1=False
                    elif warriorBlackRect1.colliderect(cardinalBlackRect):
                        warriorBlackRect1.centerx = warriorBlackxInit1
                        warriorBlackRect1.centery = warriorBlackyInit1
                        counter -= 1
                        warriorBlackPlaying1=False
                    elif warriorBlackRect1.colliderect(hadesBlackRect):
                        warriorBlackRect1.centerx = warriorBlackxInit1
                        warriorBlackRect1.centery = warriorBlackyInit1
                        counter -= 1
                        warriorBlackPlaying1=False
                    elif warriorBlackRect1.colliderect(persephoneBlackRect):
                        warriorBlackRect1.centerx = warriorBlackxInit1
                        warriorBlackRect1.centery = warriorBlackyInit1
                        counter -= 1
                        warriorBlackPlaying1=False
                    elif warriorBlackRect1.colliderect(cardinalBlackRect1):
                        warriorBlackRect1.centerx = warriorBlackxInit1
                        warriorBlackRect1.centery = warriorBlackyInit1
                        counter -= 1
                        warriorBlackPlaying1=False
                    elif warriorBlackRect1.colliderect(archbishopBlackRect1):
                        warriorBlackRect1.centerx = warriorBlackxInit1
                        warriorBlackRect1.centery = warriorBlackyInit1
                        counter -= 1
                        warriorBlackPlaying1=False
                    elif warriorBlackRect1.colliderect(plagueDoctorBlackRect1):
                        warriorBlackRect1.centerx = warriorBlackxInit1
                        warriorBlackRect1.centery = warriorBlackyInit1
                        counter -= 1
                        warriorBlackPlaying1=False
                    elif warriorBlackRect1.colliderect(legionaryBlackRect):
                        warriorBlackRect1.centerx = warriorBlackxInit1
                        warriorBlackRect1.centery = warriorBlackyInit1
                        counter -= 1
                        warriorBlackPlaying1=False
                    elif warriorBlackRect1.colliderect(warriorBlackRect):
                        warriorBlackRect1.centerx = warriorBlackxInit1
                        warriorBlackRect1.centery = warriorBlackyInit1
                        counter -= 1
                    elif warriorBlackRect1.colliderect(legionaryBlackRect1):
                        warriorBlackRect1.centerx = warriorBlackxInit1
                        warriorBlackRect1.centery = warriorBlackyInit1
                        counter -= 1
                        warriorBlackPlaying1=False
                    elif warriorBlackRect1.colliderect(legionaryBlackRect2):
                        warriorBlackRect1.centerx = warriorBlackxInit1
                        warriorBlackRect1.centery = warriorBlackyInit1
                        counter -= 1
                        warriorBlackPlaying1=False
                    elif warriorBlackRect1.colliderect(warriorBlackRect2):
                        warriorBlackRect1.centerx = warriorBlackxInit1
                        warriorBlackRect1.centery = warriorBlackyInit1
                        counter -= 1
                        warriorBlackPlaying1=False
                    elif warriorBlackRect1.colliderect(legionaryBlackRect3):
                        warriorBlackRect1.centerx = warriorBlackxInit1
                        warriorBlackRect1.centery = warriorBlackyInit1
                        counter -= 1
                        warriorBlackPlaying1=False
                    elif warriorBlackRect1.colliderect(warriorBlackRect3):
                        warriorBlackRect1.centerx = warriorBlackxInit1
                        warriorBlackRect1.centery = warriorBlackyInit1
                        counter -= 1
                        warriorBlackPlaying1=False


                if legionaryBlackRect1.collidepoint(event.pos):
                    if not legionaryBlackPlaying1:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                legionaryBlackPlaying1=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                legionaryBlackPlaying1=True
                elif legionaryBlackPlaying1:
                    if rectLegionaryBlack1_1.collidepoint(event.pos):
                        legionar_cerny_x_abilita_1 = legionaryBlackxInit1
                        legionar_cerny_y_abilita_1 = legionaryBlackyInit1
                        legionaryBlackRect1.centerx = rectLegionaryBlack1_1.centerx
                        legionaryBlackRect1.centery = rectLegionaryBlack1_1.centery
                        counter += 1
                        legionaryBlackPlaying1=False
                    elif rectLegionaryBlack2_1.collidepoint(event.pos):
                        legionar_cerny_x_abilita_1 = legionaryBlackxInit1
                        legionar_cerny_y_abilita_1 = legionaryBlackyInit1
                        legionaryBlackRect1.centerx = rectLegionaryBlack2_1.centerx
                        legionaryBlackRect1.centery = rectLegionaryBlack2_1.centery
                        counter += 1
                        legionaryBlackPlaying1=False
                    elif rectLegionaryBlack3_1.collidepoint(event.pos):
                        legionar_cerny_x_abilita_1 = legionaryBlackxInit1
                        legionar_cerny_y_abilita_1 = legionaryBlackyInit1
                        legionaryBlackRect1.centerx = rectLegionaryBlack3_1.centerx
                        legionaryBlackRect1.centery = rectLegionaryBlack3_1.centery
                        counter += 1
                        legionaryBlackPlaying1=False
                    else:
                        legionaryBlackRect1.centerx = legionaryBlackxInit1
                        legionaryBlackRect1.centery = legionaryBlackyInit1
                        legionaryBlackPlaying1=False
                    if legionaryBlackRect1.colliderect(plagueDoctorBlackRect):
                        legionaryBlackRect1.centerx = legionaryBlackxInit1
                        legionaryBlackRect1.centery = legionaryBlackyInit1
                        counter -= 1
                        legionaryBlackPlaying1=False
                    elif legionaryBlackRect1.colliderect(archbishopBlackRect):
                        legionaryBlackRect1.centerx = legionaryBlackxInit1
                        legionaryBlackRect1.centery = legionaryBlackyInit1
                        counter -= 1
                        legionaryBlackPlaying1=False
                    elif legionaryBlackRect1.colliderect(cardinalBlackRect):
                        legionaryBlackRect1.centerx = legionaryBlackxInit1
                        legionaryBlackRect1.centery = legionaryBlackyInit1
                        counter -= 1
                        legionaryBlackPlaying1=False
                    elif legionaryBlackRect1.colliderect(hadesBlackRect):
                        legionaryBlackRect1.centerx = legionaryBlackxInit1
                        legionaryBlackRect1.centery = legionaryBlackyInit1
                        counter -= 1
                        legionaryBlackPlaying1=False
                    elif legionaryBlackRect1.colliderect(persephoneBlackRect):
                        legionaryBlackRect1.centerx = legionaryBlackxInit1
                        legionaryBlackRect1.centery = legionaryBlackyInit1
                        counter -= 1
                        legionaryBlackPlaying1=False
                    elif legionaryBlackRect1.colliderect(cardinalBlackRect1):
                        legionaryBlackRect1.centerx = legionaryBlackxInit1
                        legionaryBlackRect1.centery = legionaryBlackyInit1
                        counter -= 1
                        legionaryBlackPlaying1=False
                    elif legionaryBlackRect1.colliderect(archbishopBlackRect1):
                        legionaryBlackRect1.centerx = legionaryBlackxInit1
                        legionaryBlackRect1.centery = legionaryBlackyInit1
                        counter -= 1
                        legionaryBlackPlaying1=False
                    elif legionaryBlackRect1.colliderect(plagueDoctorBlackRect1):
                        legionaryBlackRect1.centerx = legionaryBlackxInit1
                        legionaryBlackRect1.centery = legionaryBlackyInit1
                        counter -= 1
                        legionaryBlackPlaying1=False
                    elif legionaryBlackRect1.colliderect(legionaryBlackRect):
                        legionaryBlackRect1.centerx = legionaryBlackxInit1
                        legionaryBlackRect1.centery = legionaryBlackyInit1
                        counter -= 1
                        legionaryBlackPlaying1=False
                    elif legionaryBlackRect1.colliderect(warriorBlackRect):
                        legionaryBlackRect1.centerx = legionaryBlackxInit1
                        legionaryBlackRect1.centery = legionaryBlackyInit1
                        counter -= 1
                        legionaryBlackPlaying1=False
                    elif legionaryBlackRect1.colliderect(warriorBlackRect1):
                        legionaryBlackRect1.centerx = legionaryBlackxInit1
                        legionaryBlackRect1.centery = legionaryBlackyInit1
                        counter -= 1
                        legionaryBlackPlaying1=False
                    elif legionaryBlackRect1.colliderect(legionaryBlackRect2):
                        legionaryBlackRect1.centerx = legionaryBlackxInit1
                        legionaryBlackRect1.centery = legionaryBlackyInit1
                        counter -= 1
                        legionaryBlackPlaying1=False
                    elif legionaryBlackRect1.colliderect(warriorBlackRect2):
                        legionaryBlackRect1.centerx = legionaryBlackxInit1
                        legionaryBlackRect1.centery = legionaryBlackyInit1
                        counter -= 1
                        legionaryBlackPlaying1=False
                    elif legionaryBlackRect1.colliderect(legionaryBlackRect3):
                        legionaryBlackRect1.centerx = legionaryBlackxInit1
                        legionaryBlackRect1.centery = legionaryBlackyInit1
                        counter -= 1
                        legionaryBlackPlaying1=False
                    elif legionaryBlackRect1.colliderect(warriorBlackRect3):
                        legionaryBlackRect1.centerx = legionaryBlackxInit1
                        legionaryBlackRect1.centery = legionaryBlackyInit1
                        counter -= 1
                        legionaryBlackPlaying1=False

                if warriorBlackRect2.collidepoint(event.pos):
                    if not warriorBlackPlaying2:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                warriorBlackPlaying2=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                warriorBlackPlaying2=True
                elif warriorBlackPlaying2:
                    if rectWarriorBlack1_2Ability.collidepoint(event.pos) and (counter - 1) % 4 == 0:
                        warriorBlackRect2.centerx = rectWarriorBlack1_2Ability.centerx
                        warriorBlackRect2.centery = rectWarriorBlack1_2Ability.centery
                        counter += 1
                        warriorBlackPlaying2=False
                    elif rectWarriorBlack2_2Ability.collidepoint(event.pos) and (counter - 1) % 4 == 0:
                        warriorBlackRect2.centerx = rectWarriorBlack2_2Ability.centerx
                        warriorBlackRect2.centery = rectWarriorBlack2_2Ability.centery
                        counter += 1
                        warriorBlackPlaying2=False
                    elif rectWarriorBlack3_2Ability.collidepoint(event.pos) and (counter - 1) % 4 == 0:
                        warriorBlackRect2.centerx = rectWarriorBlack3_2Ability.centerx
                        warriorBlackRect2.centery = rectWarriorBlack3_2Ability.centery
                        counter += 1
                        warriorBlackPlaying2=False
                    elif rectWarriorBlack4_2Ability.collidepoint(event.pos) and (counter - 1) % 4 == 0:
                        warriorBlackRect2.centerx = rectWarriorBlack4_2Ability.centerx
                        warriorBlackRect2.centery = rectWarriorBlack4_2Ability.centery
                        counter += 1
                        warriorBlackPlaying2=False
                    elif rectWarriorBlack1_2.collidepoint(event.pos):
                        warriorBlackRect2.centerx = rectWarriorBlack1_2.centerx
                        warriorBlackRect2.centery = rectWarriorBlack1_2.centery
                        counter += 1
                        warriorBlackPlaying2=False
                    elif rectWarriorBlack2_2.collidepoint(event.pos):
                        warriorBlackRect2.centerx = rectWarriorBlack2_2.centerx
                        warriorBlackRect2.centery = rectWarriorBlack2_2.centery
                        counter += 1
                        warriorBlackPlaying2=False
                    elif rectWarriorBlack3_2.collidepoint(event.pos):
                        warriorBlackRect2.centerx = rectWarriorBlack3_2.centerx
                        warriorBlackRect2.centery = rectWarriorBlack3_2.centery
                        counter += 1
                        warriorBlackPlaying2=False
                    elif rectWarriorBlack4_2.collidepoint(event.pos):
                        warriorBlackRect2.centerx = rectWarriorBlack4_2.centerx
                        warriorBlackRect2.centery = rectWarriorBlack4_2.centery
                        counter += 1
                        warriorBlackPlaying2=False
                    else:
                        warriorBlackRect2.centerx = warriorBlackxInit2
                        warriorBlackRect2.centery = warriorBlackyInit2
                        warriorBlackPlaying2=False
                    if warriorBlackRect2.colliderect(plagueDoctorBlackRect):
                        warriorBlackRect2.centerx = warriorBlackxInit2
                        warriorBlackRect2.centery = warriorBlackyInit2
                        counter -= 1
                        warriorBlackPlaying2=False
                    elif warriorBlackRect2.colliderect(archbishopBlackRect):
                        warriorBlackRect2.centerx = warriorBlackxInit2
                        warriorBlackRect2.centery = warriorBlackyInit2
                        counter -= 1
                        warriorBlackPlaying2=False
                    elif warriorBlackRect2.colliderect(cardinalBlackRect):
                        warriorBlackRect2.centerx = warriorBlackxInit2
                        warriorBlackRect2.centery = warriorBlackyInit2
                        counter -= 1
                        warriorBlackPlaying2=False
                    elif warriorBlackRect2.colliderect(hadesBlackRect):
                        warriorBlackRect2.centerx = warriorBlackxInit2
                        warriorBlackRect2.centery = warriorBlackyInit2
                        counter -= 1
                        warriorBlackPlaying2=False
                    elif warriorBlackRect2.colliderect(persephoneBlackRect):
                        warriorBlackRect2.centerx = warriorBlackxInit2
                        warriorBlackRect2.centery = warriorBlackyInit2
                        counter -= 1
                        warriorBlackPlaying2=False
                    elif warriorBlackRect2.colliderect(cardinalBlackRect1):
                        warriorBlackRect2.centerx = warriorBlackxInit2
                        warriorBlackRect2.centery = warriorBlackyInit2
                        counter -= 1
                        warriorBlackPlaying2=False
                    elif warriorBlackRect2.colliderect(archbishopBlackRect1):
                        warriorBlackRect2.centerx = warriorBlackxInit2
                        warriorBlackRect2.centery = warriorBlackyInit2
                        counter -= 1
                        warriorBlackPlaying2=False
                    elif warriorBlackRect2.colliderect(plagueDoctorBlackRect1):
                        warriorBlackRect2.centerx = warriorBlackxInit2
                        warriorBlackRect2.centery = warriorBlackyInit2
                        counter -= 1
                        warriorBlackPlaying2=False
                    elif warriorBlackRect2.colliderect(legionaryBlackRect):
                        warriorBlackRect2.centerx = warriorBlackxInit2
                        warriorBlackRect2.centery = warriorBlackyInit2
                        counter -= 1
                        warriorBlackPlaying2=False
                    elif warriorBlackRect2.colliderect(warriorBlackRect):
                        warriorBlackRect2.centerx = warriorBlackxInit2
                        warriorBlackRect2.centery = warriorBlackyInit2
                        counter -= 1
                        warriorBlackPlaying2=False
                    elif warriorBlackRect2.colliderect(legionaryBlackRect1):
                        warriorBlackRect2.centerx = warriorBlackxInit2
                        warriorBlackRect2.centery = warriorBlackyInit2
                        counter -= 1
                        warriorBlackPlaying2=False
                    elif warriorBlackRect2.colliderect(warriorBlackRect1):
                        warriorBlackRect2.centerx = warriorBlackxInit2
                        warriorBlackRect2.centery = warriorBlackyInit2
                        counter -= 1
                        warriorBlackPlaying2=False
                    elif warriorBlackRect2.colliderect(legionaryBlackRect2):
                        warriorBlackRect2.centerx = warriorBlackxInit2
                        warriorBlackRect2.centery = warriorBlackyInit2
                        counter -= 1
                        warriorBlackPlaying2=False
                    elif warriorBlackRect2.colliderect(legionaryBlackRect3):
                        warriorBlackRect2.centerx = warriorBlackxInit2
                        warriorBlackRect2.centery = warriorBlackyInit2
                        counter -= 1
                        warriorBlackPlaying2=False
                    elif warriorBlackRect2.colliderect(warriorBlackRect3):
                        warriorBlackRect2.centerx = warriorBlackxInit2
                        warriorBlackRect2.centery = warriorBlackyInit2
                        counter -= 1
                        warriorBlackPlaying2=False


                if legionaryBlackRect2.collidepoint(event.pos):
                    if not legionaryBlackPlaying2:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                legionaryBlackPlaying2=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                legionaryBlackPlaying2=True
                elif legionaryBlackPlaying2:
                    if rectLegionaryBlack1_2.collidepoint(event.pos):
                        legionar_cerny_x_abilita_2 = legionaryBlackxInit2
                        legionar_cerny_y_abilita_2 = legionaryBlackyInit2
                        legionaryBlackRect2.centerx = rectLegionaryBlack1_2.centerx
                        legionaryBlackRect2.centery = rectLegionaryBlack1_2.centery
                        counter += 1
                        legionaryBlackPlaying2=False
                    elif rectLegionaryBlack2_2.collidepoint(event.pos):
                        legionar_cerny_x_abilita_2 = legionaryBlackxInit2
                        legionar_cerny_y_abilita_2 = legionaryBlackyInit2
                        legionaryBlackRect2.centerx = rectLegionaryBlack2_2.centerx
                        legionaryBlackRect2.centery = rectLegionaryBlack2_2.centery
                        counter += 1
                        legionaryBlackPlaying2=False
                    elif rectLegionaryBlack3_2.collidepoint(event.pos):
                        legionar_cerny_x_abilita_2 = legionaryBlackxInit2
                        legionar_cerny_y_abilita_2 = legionaryBlackyInit2
                        legionaryBlackRect2.centerx = rectLegionaryBlack3_2.centerx
                        legionaryBlackRect2.centery = rectLegionaryBlack3_2.centery
                        counter += 1
                        legionaryBlackPlaying2=False
                    else:
                        legionaryBlackRect2.centerx = legionaryBlackxInit2
                        legionaryBlackRect2.centery = legionaryBlackyInit2
                        legionaryBlackPlaying2=False
                    if legionaryBlackRect2.colliderect(plagueDoctorBlackRect):
                        legionaryBlackRect2.centerx = legionaryBlackxInit2
                        legionaryBlackRect2.centery = legionaryBlackyInit2
                        counter -= 1
                        legionaryBlackPlaying2=False
                    elif legionaryBlackRect2.colliderect(archbishopBlackRect):
                        legionaryBlackRect2.centerx = legionaryBlackxInit2
                        legionaryBlackRect2.centery = legionaryBlackyInit2
                        counter -= 1
                        legionaryBlackPlaying2=False
                    elif legionaryBlackRect2.colliderect(cardinalBlackRect):
                        legionaryBlackRect2.centerx = legionaryBlackxInit2
                        legionaryBlackRect2.centery = legionaryBlackyInit2
                        counter -= 1
                        legionaryBlackPlaying2=False
                    elif legionaryBlackRect2.colliderect(hadesBlackRect):
                        legionaryBlackRect2.centerx = legionaryBlackxInit2
                        legionaryBlackRect2.centery = legionaryBlackyInit2
                        counter -= 1
                        legionaryBlackPlaying2=False
                    elif legionaryBlackRect2.colliderect(persephoneBlackRect):
                        legionaryBlackRect2.centerx = legionaryBlackxInit2
                        legionaryBlackRect2.centery = legionaryBlackyInit2
                        counter -= 1
                        legionaryBlackPlaying2=False
                    elif legionaryBlackRect2.colliderect(cardinalBlackRect1):
                        legionaryBlackRect2.centerx = legionaryBlackxInit2
                        legionaryBlackRect2.centery = legionaryBlackyInit2
                        counter -= 1
                        legionaryBlackPlaying2=False
                    elif legionaryBlackRect2.colliderect(archbishopBlackRect1):
                        legionaryBlackRect2.centerx = legionaryBlackxInit2
                        legionaryBlackRect2.centery = legionaryBlackyInit2
                        counter -= 1
                        legionaryBlackPlaying2=False
                    elif legionaryBlackRect2.colliderect(plagueDoctorBlackRect1):
                        legionaryBlackRect2.centerx = legionaryBlackxInit2
                        legionaryBlackRect2.centery = legionaryBlackyInit2
                        counter -= 1
                        legionaryBlackPlaying2=False
                    elif legionaryBlackRect2.colliderect(legionaryBlackRect):
                        legionaryBlackRect2.centerx = legionaryBlackxInit2
                        legionaryBlackRect2.centery = legionaryBlackyInit2
                        counter -= 1
                        legionaryBlackPlaying2=False
                    elif legionaryBlackRect2.colliderect(warriorBlackRect):
                        legionaryBlackRect2.centerx = legionaryBlackxInit2
                        legionaryBlackRect2.centery = legionaryBlackyInit2
                        counter -= 1
                        legionaryBlackPlaying2=False
                    elif legionaryBlackRect2.colliderect(legionaryBlackRect1):
                        legionaryBlackRect2.centerx = legionaryBlackxInit2
                        legionaryBlackRect2.centery = legionaryBlackyInit2
                        counter -= 1
                        legionaryBlackPlaying2=False
                    elif legionaryBlackRect2.colliderect(warriorBlackRect1):
                        legionaryBlackRect2.centerx = legionaryBlackxInit2
                        legionaryBlackRect2.centery = legionaryBlackyInit2
                        counter -= 1
                        legionaryBlackPlaying2=False
                    elif legionaryBlackRect2.colliderect(warriorBlackRect2):
                        legionaryBlackRect2.centerx = legionaryBlackxInit2
                        legionaryBlackRect2.centery = legionaryBlackyInit2
                        counter -= 1
                        legionaryBlackPlaying2=False
                    elif legionaryBlackRect2.colliderect(legionaryBlackRect3):
                        legionaryBlackRect2.centerx = legionaryBlackxInit2
                        legionaryBlackRect2.centery = legionaryBlackyInit2
                        counter -= 1
                        legionaryBlackPlaying2=False
                    elif legionaryBlackRect2.colliderect(warriorBlackRect3):
                        legionaryBlackRect2.centerx = legionaryBlackxInit2
                        legionaryBlackRect2.centery = legionaryBlackyInit2
                        counter -= 1
                        legionaryBlackPlaying2=False

                if legionaryBlackRect3.collidepoint(event.pos):
                    if not legionaryBlackPlaying3:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                legionaryBlackPlaying3=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                legionaryBlackPlaying3=True
                elif legionaryBlackPlaying3:
                    if rectLegionaryBlack1_3.collidepoint(event.pos):
                        legionar_cerny_x_abilita_3 = legionaryBlackxInit3
                        legionar_cerny_y_abilita_3 = legionaryBlackyInit3
                        legionaryBlackRect3.centerx = rectLegionaryBlack1_3.centerx
                        legionaryBlackRect3.centery = rectLegionaryBlack1_3.centery
                        counter += 1
                        legionaryBlackPlaying3=False
                    elif rectLegionaryBlack2_3.collidepoint(event.pos):
                        legionar_cerny_x_abilita_3 = legionaryBlackxInit3
                        legionar_cerny_y_abilita_3 = legionaryBlackyInit3
                        legionaryBlackRect3.centerx = rectLegionaryBlack2_3.centerx
                        legionaryBlackRect3.centery = rectLegionaryBlack2_3.centery
                        counter += 1
                        legionaryBlackPlaying3=False
                    elif rectLegionaryBlack3_3.collidepoint(event.pos):
                        legionar_cerny_x_abilita_3 = legionaryBlackxInit3
                        legionar_cerny_y_abilita_3 = legionaryBlackyInit3
                        legionaryBlackRect3.centerx = rectLegionaryBlack3_3.centerx
                        legionaryBlackRect3.centery = rectLegionaryBlack3_3.centery
                        counter += 1
                        legionaryBlackPlaying3=False
                    else:
                        legionaryBlackRect3.centerx = legionaryBlackxInit3
                        legionaryBlackRect3.centery = legionaryBlackyInit3
                        legionaryBlackPlaying3=False
                    if legionaryBlackRect3.colliderect(plagueDoctorBlackRect):
                        legionaryBlackRect3.centerx = legionaryBlackxInit3
                        legionaryBlackRect3.centery = legionaryBlackyInit3
                        counter -= 1
                        legionaryBlackPlaying3=False
                    elif legionaryBlackRect3.colliderect(archbishopBlackRect):
                        legionaryBlackRect3.centerx = legionaryBlackxInit3
                        legionaryBlackRect3.centery = legionaryBlackyInit3
                        counter -= 1
                        legionaryBlackPlaying3=False
                    elif legionaryBlackRect3.colliderect(cardinalBlackRect):
                        legionaryBlackRect3.centerx = legionaryBlackxInit3
                        legionaryBlackRect3.centery = legionaryBlackyInit3
                        counter -= 1
                        legionaryBlackPlaying3=False
                    elif legionaryBlackRect3.colliderect(hadesBlackRect):
                        legionaryBlackRect3.centerx = legionaryBlackxInit3
                        legionaryBlackRect3.centery = legionaryBlackyInit3
                        counter -= 1
                        legionaryBlackPlaying3=False
                    elif legionaryBlackRect3.colliderect(persephoneBlackRect):
                        legionaryBlackRect3.centerx = legionaryBlackxInit3
                        legionaryBlackRect3.centery = legionaryBlackyInit3
                        counter -= 1
                        legionaryBlackPlaying3=False
                    elif legionaryBlackRect3.colliderect(cardinalBlackRect1):
                        legionaryBlackRect3.centerx = legionaryBlackxInit3
                        legionaryBlackRect3.centery = legionaryBlackyInit3
                        counter -= 1
                        legionaryBlackPlaying3=False
                    elif legionaryBlackRect3.colliderect(archbishopBlackRect1):
                        legionaryBlackRect3.centerx = legionaryBlackxInit3
                        legionaryBlackRect3.centery = legionaryBlackyInit3
                        counter -= 1
                        legionaryBlackPlaying3=False
                    elif legionaryBlackRect3.colliderect(plagueDoctorBlackRect1):
                        legionaryBlackRect3.centerx = legionaryBlackxInit3
                        legionaryBlackRect3.centery = legionaryBlackyInit3
                        counter -= 1
                        legionaryBlackPlaying3=False
                    elif legionaryBlackRect3.colliderect(legionaryBlackRect):
                        legionaryBlackRect3.centerx = legionaryBlackxInit3
                        legionaryBlackRect3.centery = legionaryBlackyInit3
                        counter -= 1
                        legionaryBlackPlaying3=False
                    elif legionaryBlackRect3.colliderect(warriorBlackRect):
                        legionaryBlackRect3.centerx = legionaryBlackxInit3
                        legionaryBlackRect3.centery = legionaryBlackyInit3
                        counter -= 1
                        legionaryBlackPlaying3=False
                    elif legionaryBlackRect3.colliderect(legionaryBlackRect1):
                        legionaryBlackRect3.centerx = legionaryBlackxInit3
                        legionaryBlackRect3.centery = legionaryBlackyInit3
                        counter -= 1
                        legionaryBlackPlaying3=False
                    elif legionaryBlackRect3.colliderect(warriorBlackRect1):
                        legionaryBlackRect3.centerx = legionaryBlackxInit3
                        legionaryBlackRect3.centery = legionaryBlackyInit3
                        counter -= 1
                        legionaryBlackPlaying3=False
                    elif legionaryBlackRect3.colliderect(legionaryBlackRect2):
                        legionaryBlackRect3.centerx = legionaryBlackxInit3
                        legionaryBlackRect3.centery = legionaryBlackyInit3
                        counter -= 1
                        legionaryBlackPlaying3=False
                    elif legionaryBlackRect3.colliderect(legionaryBlackRect1):
                        legionaryBlackRect3.centerx = legionaryBlackxInit3
                        legionaryBlackRect3.centery = legionaryBlackyInit3
                        counter -= 1
                        legionaryBlackPlaying3=False
                    elif legionaryBlackRect3.colliderect(warriorBlackRect3):
                        legionaryBlackRect3.centerx = legionaryBlackxInit3
                        legionaryBlackRect3.centery = legionaryBlackyInit3
                        counter -= 1
                        legionaryBlackPlaying3=False

                if warriorBlackRect3.collidepoint(event.pos):
                    if not warriorBlackPlaying3:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                warriorBlackPlaying3=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                warriorBlackPlaying3=True
                elif warriorBlackPlaying3:
                    if rectWarriorBlack1_3Ability.collidepoint(event.pos) and (counter - 1) % 4 == 0:
                        warriorBlackRect3.centerx = rectWarriorBlack1_3Ability.centerx
                        warriorBlackRect3.centery = rectWarriorBlack1_3Ability.centery
                        counter += 1
                        warriorBlackPlaying3=False
                    elif rectWarriorBlack2_3Ability.collidepoint(event.pos) and (counter - 1) % 4 == 0:
                        warriorBlackRect3.centerx = rectWarriorBlack2_3Ability.centerx
                        warriorBlackRect3.centery = rectWarriorBlack2_3Ability.centery
                        counter += 1
                        warriorBlackPlaying3=False
                    elif rectWarriorBlack3_3Ability.collidepoint(event.pos) and (counter - 1) % 4 == 0:
                        warriorBlackRect3.centerx = rectWarriorBlack3_3Ability.centerx
                        warriorBlackRect3.centery = rectWarriorBlack3_3Ability.centery
                        counter += 1
                        warriorBlackPlaying3=False
                    elif rectWarriorBlack4_3Ability.collidepoint(event.pos) and (counter - 1) % 4 == 0:
                        warriorBlackRect3.centerx = rectWarriorBlack4_3Ability.centerx
                        warriorBlackRect3.centery = rectWarriorBlack4_3Ability.centery
                        counter += 1
                        warriorBlackPlaying3=False
                    elif warriorBlackRect3.colliderect(rectWarriorBlack1_3):
                        warriorBlackRect3.centerx = rectWarriorBlack1_3.centerx
                        warriorBlackRect3.centery = rectWarriorBlack1_3.centery
                        counter += 1
                        warriorBlackPlaying3=False
                    elif warriorBlackRect3.colliderect(rectWarriorBlack2_3):
                        warriorBlackRect3.centerx = rectWarriorBlack2_3.centerx
                        warriorBlackRect3.centery = rectWarriorBlack2_3.centery
                        counter += 1
                        warriorBlackPlaying3=False
                    elif warriorBlackRect3.colliderect(rectWarriorBlack3_3):
                        warriorBlackRect3.centerx = rectWarriorBlack3_3.centerx
                        warriorBlackRect3.centery = rectWarriorBlack3_3.centery
                        counter += 1
                        warriorBlackPlaying3=False
                    elif warriorBlackRect3.colliderect(rectWarriorBlack4_3):
                        warriorBlackRect3.centerx = rectWarriorBlack4_3.centerx
                        warriorBlackRect3.centery = rectWarriorBlack4_3.centery
                        counter += 1
                        warriorBlackPlaying3=False
                    else:
                        warriorBlackRect3.centerx = warriorBlackxInit3
                        warriorBlackRect3.centery = warriorBlackyInit3
                        warriorBlackPlaying3=False
                    if warriorBlackRect3.colliderect(plagueDoctorBlackRect):
                        warriorBlackRect3.centerx = warriorBlackxInit3
                        warriorBlackRect3.centery = warriorBlackyInit3
                        counter -= 1
                        warriorBlackPlaying3=False
                    elif warriorBlackRect3.colliderect(archbishopBlackRect):
                        warriorBlackRect3.centerx = warriorBlackxInit3
                        warriorBlackRect3.centery = warriorBlackyInit3
                        counter -= 1
                        warriorBlackPlaying3=False
                    elif warriorBlackRect3.colliderect(cardinalBlackRect):
                        warriorBlackRect3.centerx = warriorBlackxInit3
                        warriorBlackRect3.centery = warriorBlackyInit3
                        counter -= 1
                        warriorBlackPlaying3=False
                    elif warriorBlackRect3.colliderect(hadesBlackRect):
                        warriorBlackRect3.centerx = warriorBlackxInit3
                        warriorBlackRect3.centery = warriorBlackyInit3
                        counter -= 1
                        warriorBlackPlaying3=False
                    elif warriorBlackRect3.colliderect(persephoneBlackRect):
                        warriorBlackRect3.centerx = warriorBlackxInit3
                        warriorBlackRect3.centery = warriorBlackyInit3
                        counter -= 1
                        warriorBlackPlaying3=False
                    elif warriorBlackRect3.colliderect(cardinalBlackRect1):
                        warriorBlackRect3.centerx = warriorBlackxInit3
                        warriorBlackRect3.centery = warriorBlackyInit3
                        counter -= 1
                        warriorBlackPlaying3=False
                    elif warriorBlackRect3.colliderect(archbishopBlackRect1):
                        warriorBlackRect3.centerx = warriorBlackxInit3
                        warriorBlackRect3.centery = warriorBlackyInit3
                        counter -= 1
                        warriorBlackPlaying3=False
                    elif warriorBlackRect3.colliderect(plagueDoctorBlackRect1):
                        warriorBlackRect3.centerx = warriorBlackxInit3
                        warriorBlackRect3.centery = warriorBlackyInit3
                        counter -= 1
                        warriorBlackPlaying3=False
                    elif warriorBlackRect3.colliderect(legionaryBlackRect):
                        warriorBlackRect3.centerx = warriorBlackxInit3
                        warriorBlackRect3.centery = warriorBlackyInit3
                        counter -= 1
                        warriorBlackPlaying3=False
                    elif warriorBlackRect3.colliderect(warriorBlackRect):
                        warriorBlackRect3.centerx = warriorBlackxInit3
                        warriorBlackRect3.centery = warriorBlackyInit3
                        counter -= 1
                        warriorBlackPlaying3=False
                    elif warriorBlackRect3.colliderect(legionaryBlackRect1):
                        warriorBlackRect3.centerx = warriorBlackxInit3
                        warriorBlackRect3.centery = warriorBlackyInit3
                        counter -= 1
                        warriorBlackPlaying3=False
                    elif warriorBlackRect3.colliderect(warriorBlackRect1):
                        warriorBlackRect3.centerx = warriorBlackxInit3
                        warriorBlackRect3.centery = warriorBlackyInit3
                        counter -= 1
                        warriorBlackPlaying3=False
                    elif warriorBlackRect3.colliderect(legionaryBlackRect2):
                        warriorBlackRect3.centerx = warriorBlackxInit3
                        warriorBlackRect3.centery = warriorBlackyInit3
                        counter -= 1
                        warriorBlackPlaying3=False
                    elif warriorBlackRect3.colliderect(legionaryBlackRect3):
                        warriorBlackRect3.centerx = warriorBlackxInit3
                        warriorBlackRect3.centery = warriorBlackyInit3
                        counter -= 1
                        warriorBlackPlaying3=False
                    elif warriorBlackRect3.colliderect(warriorBlackRect2):
                        warriorBlackRect3.centerx = warriorBlackxInit3
                        warriorBlackRect3.centery = warriorBlackyInit3
                        counter -= 1
                        warriorBlackPlaying3=False


        if plagueDoctorWhitePlaying:
            for ctverec in rectsPlagueDoctorWhite:
                if (ctverec.right < 1440 or ctverec.left > 475) or (
                        ctverec.bottom < 850 or ctverec.top > 60):
                    pygame.draw.rect(screen, black, ctverec, 5)
        if archbishopWhitePlaying:
            for ctverec in rectsArchbishopWhite:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                            ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen, black, ctverec, 5)
        if cardinalWhitePlaying:
            for ctverec in rectsCardinalWhite:
                if (ctverec.right < 1440 or ctverec.left > 475) or (
                        ctverec.bottom < 850 or ctverec.top > 60):
                    pygame.draw.rect(screen, black, ctverec, 5)
        if hadesWhitePlaying:
            for ctverec in rectsHadesWhite:
                if (ctverec.right < 1440 or ctverec.left > 475) or (
                        ctverec.bottom < 850 or ctverec.top > 60):
                    pygame.draw.rect(screen, black, ctverec, 5)
        if persephoneWhitePlaying:
            for ctverec in rectsPersephoneWhite:
                                if (ctverec.right < 1440 or ctverec.left > 475) or (
                                        ctverec.bottom < 850 or ctverec.top > 60):
                                    pygame.draw.rect(screen, black, ctverec, 5)
        if cardinalWhitePlaying1:
            for ctverec in rectsCardinalWhite_1:
                if (ctverec.right < 1440 or ctverec.left > 475) or (
                        ctverec.bottom < 850 or ctverec.top > 60):
                    pygame.draw.rect(screen, black, ctverec, 5)
        if archbishopWhitePlaying1:
            for ctverec in rectsArchbishopWhite_1:
                if (ctverec.right < 1440 or ctverec.left > 475) or (
                        ctverec.bottom < 850 or ctverec.top > 60):
                    pygame.draw.rect(screen, black, ctverec, 5)
        if plagueDoctorWhitePlaying1:
            for ctverec in rectsPlagueDoctorWhite_1:
                if (ctverec.right < 1440 or ctverec.left > 475) or (
                        ctverec.bottom < 850 or ctverec.top > 60):
                    pygame.draw.rect(screen, black, ctverec, 5)
        if warriorWhitePlaying:
            for ctverec in rectsWarriorWhite:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                                    ctverec.bottom < 850 or ctverec.top > 60):
                                pygame.draw.rect(screen, black, ctverec, 5)
                    if counter % 4 == 0:
                            for ctverec in rectsWarriorWhiteAbility:
                                if (ctverec.right < 1440 or ctverec.left > 475) or (
                                        ctverec.bottom < 850 or ctverec.top > 60):
                                    pygame.draw.rect(screen, black, ctverec, 5)
        if legionaryWhitePlaying:
            for ctverec in rectsLegionaryWhite:
                if (ctverec.right < 1440 or ctverec.left > 475) or (
                        ctverec.bottom < 850 or ctverec.top > 60):
                    pygame.draw.rect(screen, black, ctverec, 5)    
        if warriorWhitePlaying1:
            for ctverec in rectsWarriorWhite_1:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                            ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen, black, ctverec, 5)
            if counter % 4 == 0:
                for ctverec in rectsWarriorWhiteAbility_1:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                            ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen, black, ctverec, 5)   
        if legionaryWhitePlaying1:
            for ctverec in rectsLegionaryWhite_1:
                        if (ctverec.right < 1440 or ctverec.left > 475) or (
                                ctverec.bottom < 850 or ctverec.top > 60):
                            pygame.draw.rect(screen, black, ctverec, 5)
        if warriorWhitePlaying2:
            for ctverec in rectsWarriorWhite_2:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                            ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen, black, ctverec, 5)
            if counter % 4 == 0:
                for ctverec in rectsWarriorWhiteAbility_2:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                            ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen, black, ctverec, 5)   
        if legionaryWhitePlaying2:
            for ctverec in rectsLegionaryWhite_2:
                if (ctverec.right < 1440 or ctverec.left > 475) or (
                        ctverec.bottom < 850 or ctverec.top > 60):
                    pygame.draw.rect(screen, black, ctverec, 5)
        if warriorWhitePlaying3:
            for ctverec in rectsWarriorWhite_3:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                            ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen, black, ctverec, 5)
            if counter % 4 == 0:
                for ctverec in rectsWarriorWhiteAbility_3:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                            ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen, black, ctverec, 5)
        if plagueDoctorBlackPlaying:
            for ctverec in rectsPlagueDoctorBlack:
                if (ctverec.right < 1440 or ctverec.left > 475) or (
                        ctverec.bottom < 850 or ctverec.top > 60):
                    pygame.draw.rect(screen, black, ctverec, 5)
        if archbishopBlackPlaying:
            for ctverec in rectsArchbishopBlack:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                            ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen, black, ctverec, 5)
        if cardinalBlackPlaying:
            for ctverec in rectsCardinalBlack:
                if (ctverec.right < 1440 or ctverec.left > 475) or (
                        ctverec.bottom < 850 or ctverec.top > 60):
                    pygame.draw.rect(screen, black, ctverec, 5)
        if hadesBlackPlaying:
            for ctverec in rectsHadesBlack:
                if (ctverec.right < 1440 or ctverec.left > 475) or (
                        ctverec.bottom < 850 or ctverec.top > 60):
                    pygame.draw.rect(screen, black, ctverec, 5)
        if persephoneBlackPlaying:
            for ctverec in rectsPersephoneBlack:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                            ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen, black, ctverec, 5)
        if cardinalBlackPlaying1:
            for ctverec in rectsCardinalBlack_1:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                            ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen, black, ctverec, 5)
        if archbishopBlackPlaying1:
            for ctverec in rectsArchbishopBlack_1:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                            ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen, black, ctverec, 5)
        if plagueDoctorBlackPlaying1:
            for ctverec in rectsPlagueDoctorBlack_1:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                            ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen, black, ctverec, 5)
        if legionaryBlackPlaying:
            for ctverec in rectsLegionaryBlack:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                            ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen, black, ctverec, 5)
        if warriorBlackPlaying:
            for ctverec in rectsWarriorBlack:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                            ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen, black, ctverec, 5)
            if (counter-1) % 4 == 0:
                for ctverec in rectsWarriorBlackAbility:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                            ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen, black, ctverec, 5)
        if legionaryBlackPlaying1:
            for ctverec in rectsLegionaryBlack_1:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                            ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen, black, ctverec, 5)
        if warriorBlackPlaying1:
            for ctverec in rectsWarriorBlack_1:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                            ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen, black, ctverec, 5)
            if (counter-1) % 4 == 0:
                for ctverec in rectsWarriorBlackAbility_1:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                            ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen, black, ctverec, 5)
        if legionaryBlackPlaying2:
            for ctverec in rectsLegionaryBlack_2:
                if (ctverec.right < 1440 or ctverec.left > 475) or (
                        ctverec.bottom < 850 or ctverec.top > 60):
                    pygame.draw.rect(screen, black, ctverec, 5)
        if warriorBlackPlaying2:
            for ctverec in rectsWarriorBlack_2:
                if (ctverec.right < 1440 or ctverec.left > 475) or (ctverec.bottom < 850 or ctverec.top > 60):
                    pygame.draw.rect(screen, black, ctverec, 5)
            if (counter - 1) % 4 == 0:
                for ctverec in rectsWarriorBlackAbility_2:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                            ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen, black, ctverec, 5)
        if legionaryBlackPlaying3:
            for ctverec in rectsLegionaryBlack_3:
                if (ctverec.right < 1440 or ctverec.left > 475) or (
                        ctverec.bottom < 850 or ctverec.top > 60):
                    pygame.draw.rect(screen, black, ctverec, 5)
        if warriorBlackPlaying3:
            for ctverec in rectsWarriorBlack_3:
                if (ctverec.right < 1440 or ctverec.left > 475) or (ctverec.bottom < 850 or ctverec.top > 60):
                    pygame.draw.rect(screen, black, ctverec, 5)
                if (counter - 1) % 4 == 0:
                    for ctverec in rectsWarriorBlackAbility_3:
                        if (ctverec.right < 1440 or ctverec.left > 475) or (
                                ctverec.bottom < 850 or ctverec.top > 60):
                            pygame.draw.rect(screen, black, ctverec, 5)
                    

        


        if event.type == pygame.MOUSEBUTTONUP:
            mx,my=pygame.mouse.get_pos()
            # Todo: zjistit, jak tento proces zjednodušit pomocí for cyklu

            """for i in range(0,len(ctverce_morovy_doktor_bily)): 
                if plagueDoctorWhiteRect.colliderect(ctverce_morovy_doktor_bily[i]):
                    plagueDoctorWhiteRect.centerx=ctverce_morovy_doktor_bily[i].centerx
                    plagueDoctorWhiteRect.centery=ctverce_morovy_doktor_bily[i].centery

                elif i==len(ctverce_morovy_doktor_bily)-1:
                    plagueDoctorWhiteRect.centerx=plagueWhitexInit
                    plagueDoctorWhiteRect.centery=plagueWhiteyInit"""


            

            

            

           

            

            

            

            
            

            

            

            

            pohyb = False

            """for figurka1 in figuresBlack:
               
                if plagueDoctorBlackRect.colliderect(figurka1):
                    if figurka1==plagueDoctorBlackRect:
                         continue
                    else:
                        plagueDoctorBlackRect.centerx=plagueBlackxInit
                        plagueDoctorBlackRect.centery=plagueBlackyInit
                        counter-=1
                        break
                    

                elif archbishopBlackRect.colliderect(figurka1):
                    if figurka1==archbishopBlackRect:
                         continue
                    else:
                        archbishopBlackRect.centerx=archbishopBlackxInit
                        archbishopBlackRect.centery=archbishopBlackyInit
                        counter-=1
                        break
                    
                elif cardinalBlackRect.colliderect(figurka1):
                    if figurka1==cardinalBlackRect:
                         continue
                    else:
                        cardinalBlackRect.centerx=cardinalBlackxInit
                        cardinalBlackRect.centery=cardinalBlackyInit
                        counter-=1
                        break
                    
                elif hadesBlackRect.colliderect(figurka1):
                    if figurka1==hadesBlackRect:
                         continue
                    else:
                        hadesBlackRect.centerx=hadesBlackxInit
                        hadesBlackRect.centery=hadesBlackyInit
                        counter-=1
                        break
                    
                elif persephoneBlackRect.colliderect(figurka1):
                    if figurka1==persephoneBlackRect:
                         continue
                    else:
                        persephoneBlackRect.centerx=persephoneBlackxInit
                        persephoneBlackRect.centery=persephoneBlackyInit
                        counter-=1
                        break
                    
                elif cardinalBlackRect1.colliderect(figurka1):
                    if figurka1==cardinalBlackRect1:
                         continue
                    else:
                        cardinalBlackRect1.centerx=cardinalBlackxInit1
                        cardinalBlackRect1.centery=cardinalBlackyInit1
                        counter-=1
                        break
                        
                elif archbishopBlackRect1.colliderect(figurka1):
                    if figurka1==archbishopBlackRect1:
                         continue
                    else:
                        archbishopBlackRect1.centerx=archbishopBlackxInit1
                        archbishopBlackRect1.centery=archbishopBlackyInit1
                        counter-=1
                        break
                    
                elif plagueDoctorBlackRect1.colliderect(figurka1):
                    if figurka1==plagueDoctorBlackRect1:
                         continue
                    else:
                        plagueDoctorBlackRect1.centerx=plagueBlackxInit1
                        plagueDoctorBlackRect1.centery=plagueBlackyInit1
                        counter-=1
                        break
                elif warriorBlackRect.colliderect(figurka1):
                    if figurka1==warriorBlackRect:
                         continue
                    else:
                        warriorBlackRect.centerx=warriorBlackxInit
                        warriorBlackRect.centery=warriorBlackyInit
                        counter-=1
                        break
                elif legionaryBlackRect.colliderect(figurka1):
                    if figurka1==legionaryBlackRect:
                         continue
                    else:
                        legionaryBlackRect.centerx=legionaryBlackxInit
                        legionaryBlackRect.centery=legionaryBlackyInit
                        counter-=1
                        break
                elif warriorBlackRect1.colliderect(figurka1):
                    if figurka1==warriorBlackRect1:
                         continue
                    else:
                        warriorBlackRect1.centerx=warriorBlackxInit1
                        warriorBlackRect1.centery=warriorBlackyInit1
                        counter-=1
                        break
                elif legionaryBlackRect1.colliderect(figurka1):
                    if figurka1==legionaryBlackRect1:
                         continue
                    else:
                        legionaryBlackRect1.centerx=legionaryBlackxInit1
                        legionaryBlackRect1.centery=legionaryBlackyInit1
                        counter-=1
                        break
                elif warriorBlackRect2.colliderect(figurka1):
                    if figurka1==warriorBlackRect2:
                         continue
                    else:
                        warriorBlackRect2.centerx=warriorBlackxInit2
                        warriorBlackRect2.centery=warriorBlackyInit2
                        counter-=1
                        break
                elif legionaryBlackRect2.colliderect(figurka1):
                    if figurka1==legionaryBlackRect2:
                         continue
                    else:
                        legionaryBlackRect2.centerx=legionaryBlackxInit2
                        legionaryBlackRect2.centery=legionaryBlackyInit2
                        counter-=1
                        break
                elif warriorBlackRect3.colliderect(figurka1):
                    if figurka1==warriorBlackRect3:
                         continue
                    else:
                        warriorBlackRect3.centerx=warriorBlackxInit3
                        warriorBlackRect3.centery=warriorBlackyInit3
                        counter-=1
                        break
                elif legionaryBlackRect3.colliderect(figurka1):
                    if figurka1==legionaryBlackRect3:
                         continue
                    else:
                        legionaryBlackRect3.centerx=legionaryBlackxInit3
                        legionaryBlackRect3.centery=legionaryBlackyInit3
                        counter-=1
                        break"""

            """for figurka in figuresWhite:
                print(figurka)
                if plagueDoctorWhiteRect.colliderect(figurka):
                    if figurka==plagueDoctorWhiteRect:
                        continue
                    else:
                        plagueDoctorWhiteRect.centerx=plagueWhitexInit
                        plagueDoctorWhiteRect.centery=plagueWhiteyInit
                        counter-=1
                        print("ok")
                        break
                    

                elif archbishopWhiteRect.colliderect(figurka):
                    if figurka==archbishopWhiteRect:
                        continue
                    else:
                        archbishopWhiteRect.centerx=archbishopWhitexInit
                        archbishopWhiteRect.centery=archbishopWhiteyInit
                        counter-=1
                        break
                    
                elif cardinalWhiteRect.colliderect(figurka):
                    if figurka==cardinalWhiteRect:
                        continue
                    else:
                        cardinalWhiteRect.centerx=cardinalWhitexInit
                        cardinalWhiteRect.centery=cardinalWhiteyInit
                        counter-=1
                        break
                    
                elif hadesWhiteRect.colliderect(figurka):
                    if figurka==hadesWhiteRect:
                         continue
                    else:    
                        hadesWhiteRect.centerx=hadesWhitexInit
                        hadesWhiteRect.centery=hadesWhiteyInit
                        counter-=1
                        break
                    
                elif persephoneWhiteRect.colliderect(figurka):
                    if figurka==persephoneWhiteRect:
                         continue
                    else:
                        persephoneWhiteRect.centerx=persephoneWhitexInit
                        persephoneWhiteRect.centery=persephoneWhiteyInit
                        counter-=1
                        break
                    
                elif cardinalWhiteRect1.colliderect(figurka):
                    if figurka==cardinalWhiteRect1:
                         continue
                    else:
                        cardinalWhiteRect1.centerx=cardinalWhitexInit1
                        cardinalWhiteRect1.centery=cardinalWhiteyInit1
                        counter-=1
                        break
                    
                elif archbishopWhiteRect1.colliderect(figurka):
                    if figurka==archbishopWhiteRect1:
                         continue
                    else:
                        archbishopWhiteRect1.centerx=archbishopWhitexInit1
                        archbishopWhiteRect1.centery=archbishopWhiteyInit1
                        counter-=1
                        break
                    
                elif plagueDoctorWhiteRect1.colliderect(figurka):
                    if figurka==plagueDoctorWhiteRect1:
                         continue
                    else:
                        plagueDoctorWhiteRect1.centerx=plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery=plagueWhiteyInit1
                        counter-=1
                        break
                elif warriorWhiteRect.colliderect(figurka):
                    if figurka==warriorWhiteRect:
                         continue
                    else:
                        warriorWhiteRect.centerx=warriorWhitexInit
                        warriorWhiteRect.centery=valecnik_bily_y_pred
                        counter-=1
                        break
                elif legionaryWhiteRect.colliderect(figurka):
                    if figurka==legionaryWhiteRect:
                         continue
                    else:
                        legionaryWhiteRect.centerx=legionaryWhitexInit
                        legionaryWhiteRect.centery=legionaryWhiteyInit
                        counter-=1
                        break
                elif warriorWhiteRect1.colliderect(figurka):
                    if figurka==warriorWhiteRect1:
                         continue
                    else:
                        warriorWhiteRect1.centerx=warriorWhitexInit1
                        warriorWhiteRect1.centery=warriorWhiteyInit
                        counter-=1
                        break
                elif legionaryWhiteRect1.colliderect(figurka):
                    if figurka==legionaryWhiteRect1:
                         continue
                    else:
                        legionaryWhiteRect1.centerx=legionaryWhitexInit1
                        legionaryWhiteRect1.centery=legionaryWhiteyInit1
                        counter-=1
                        break
                elif warriorWhiteRect2.colliderect(figurka):
                    if figurka==warriorWhiteRect2:
                         continue
                    else:
                        warriorWhiteRect2.centerx=warriorWhitexInit2
                        warriorWhiteRect2.centery=valecnik_bily_y_pred_2
                        counter-=1
                        break
                elif legionaryWhiteRect2.colliderect(figurka):
                    if figurka==legionaryWhiteRect2:
                         continue
                    else:
                        legionaryWhiteRect2.centerx=legionaryWhitexInit2
                        legionaryWhiteRect2.centery=legionaryWhiteyInit2
                        counter-=1
                        break
                elif warriorWhiteRect3.colliderect(figurka):
                    if figurka==warriorWhiteRect3:
                         continue
                    else:
                        warriorWhiteRect3.centerx=warriorWhitexInit3
                        warriorWhiteRect3.centery=warriorWhiteyInit3
                        counter-=1
                        break
                elif legionaryWhiteRect3.colliderect(figurka):
                    if figurka==legionaryWhiteRect3:
                         continue
                    else:
                        legionaryWhiteRect3.centerx=legionaryWhitexInit3
                        legionaryWhiteRect3.centery=legionaryWhiteyInit3
                        counter-=1
                        break"""

            print(counter)

            # todo: Kontrola kolize
            # Bude to fungovat tak, že jakmile dojde ke kolizi mezi dvěma figurkami, zkontroluje se hodnota counteru a v závislosti na jeho modulu bude odebrána figurka příslušné barvy
            # counter=0 odehrál bílý, tedy musí brát černou figurku
            if counter % 2 != 0:
                if plagueDoctorWhiteRect.colliderect(plagueDoctorBlackRect):
                    figuresBlack[0] = ""
                    plagueDoctorBlackRect.centerx = -60
                    plagueDoctorBlackRect.centery = -60
                if plagueDoctorWhiteRect.colliderect(archbishopBlackRect):
                    figuresBlack[1] = ""
                    archbishopBlackRect.centerx = -60
                    archbishopBlackRect.centery = -60
                if plagueDoctorWhiteRect.colliderect(cardinalBlackRect):
                    figuresBlack[2] = ""
                    cardinalBlackRect.centerx = -60
                    cardinalBlackRect.centery = -60
                if plagueDoctorWhiteRect.colliderect(hadesBlackRect):
                    figuresBlack[3] = ""
                    hadesBlackRect.centerx = -60
                    hadesBlackRect.centery = -60
                if plagueDoctorWhiteRect.colliderect(persephoneBlackRect):
                    figuresBlack[4] = ""
                    persephoneBlackRect.centerx = -60
                    persephoneBlackRect.centery = -60
                if plagueDoctorWhiteRect.colliderect(cardinalBlackRect1):
                    figuresBlack[5] = ""
                    cardinalBlackRect1.centerx = -60
                    cardinalBlackRect1.centery = -60
                if plagueDoctorWhiteRect.colliderect(archbishopBlackRect1):
                    figuresBlack[6] = ""
                    archbishopBlackRect1.centerx = -60
                    archbishopBlackRect1.centery = -60
                if plagueDoctorWhiteRect.colliderect(plagueDoctorBlackRect1):
                    figuresBlack[7] = ""
                    plagueDoctorBlackRect1.centerx = -60
                    plagueDoctorBlackRect1.centery = -60
                if plagueDoctorWhiteRect.colliderect(legionaryBlackRect):
                    figuresBlack[8] = ""
                    legionaryBlackRect.centerx = -60
                    legionaryBlackRect.centery = -60
                if plagueDoctorWhiteRect.colliderect(warriorBlackRect):
                    figuresBlack[9] = ""
                    warriorBlackRect.centerx = -60
                    warriorBlackRect.centery = -60
                if plagueDoctorWhiteRect.colliderect(legionaryBlackRect1):
                    figuresBlack[10] = ""
                    legionaryBlackRect1.centerx = -60
                    legionaryBlackRect1.centery = -60
                if plagueDoctorWhiteRect.colliderect(warriorBlackRect1):
                    figuresBlack[11] = ""
                    warriorBlackRect1.centerx = -60
                    warriorBlackRect1.centery = -60
                if plagueDoctorWhiteRect.colliderect(legionaryBlackRect2):
                    figuresBlack[12] = ""
                    legionaryBlackRect2.centerx = -60
                    legionaryBlackRect2.centery = -60
                if plagueDoctorWhiteRect.colliderect(warriorBlackRect2):
                    figuresBlack[13] = ""
                    warriorBlackRect2.centerx = -60
                    warriorBlackRect2.centery = -60
                if plagueDoctorWhiteRect.colliderect(legionaryBlackRect3):
                    figuresBlack[14] = ""
                    legionaryBlackRect3.centerx = -60
                    legionaryBlackRect3.centery = -60
                if plagueDoctorWhiteRect.colliderect(warriorBlackRect3):
                    figuresBlack[15] = ""
                    warriorBlackRect3.centerx = -60
                    warriorBlackRect3.centery = -60

                if archbishopWhiteRect.colliderect(plagueDoctorBlackRect):
                    figuresBlack[0] = ""
                    plagueDoctorBlackRect.centerx = -60
                    plagueDoctorBlackRect.centery = -60
                if archbishopWhiteRect.colliderect(archbishopBlackRect):
                    figuresBlack[1] = ""
                    archbishopBlackRect.centerx = -60
                    archbishopBlackRect.centery = -60
                if archbishopWhiteRect.colliderect(cardinalBlackRect):
                    figuresBlack[2] = ""
                    cardinalBlackRect.centerx = -60
                    cardinalBlackRect.centery = -60
                if archbishopWhiteRect.colliderect(hadesBlackRect):
                    figuresBlack[3] = ""
                    hadesBlackRect.centerx = -60
                    hadesBlackRect.centery = -60
                if archbishopWhiteRect.colliderect(persephoneBlackRect):
                    figuresBlack[4] = ""
                    persephoneBlackRect.centerx = -60
                    persephoneBlackRect.centery = -60
                if archbishopWhiteRect.colliderect(cardinalBlackRect1):
                    figuresBlack[5] = ""
                    cardinalBlackRect1.centerx = -60
                    cardinalBlackRect1.centery = -60
                if archbishopWhiteRect.colliderect(archbishopBlackRect1):
                    figuresBlack[6] = ""
                    archbishopBlackRect1.centerx = -60
                    archbishopBlackRect1.centery = -60
                if archbishopWhiteRect.colliderect(plagueDoctorBlackRect1):
                    figuresBlack[7] = ""
                    plagueDoctorBlackRect1.centerx = -60
                    plagueDoctorBlackRect1.centery = -60
                if archbishopWhiteRect.colliderect(legionaryBlackRect):
                    figuresBlack[8] = ""
                    legionaryBlackRect.centerx = -60
                    legionaryBlackRect.centery = -60
                if archbishopWhiteRect.colliderect(warriorBlackRect):
                    figuresBlack[9] = ""
                    warriorBlackRect.centerx = -60
                    warriorBlackRect.centery = -60
                if archbishopWhiteRect.colliderect(legionaryBlackRect1):
                    figuresBlack[10] = ""
                    legionaryBlackRect1.centerx = -60
                    legionaryBlackRect1.centery = -60
                if archbishopWhiteRect.colliderect(warriorBlackRect1):
                    figuresBlack[11] = ""
                    warriorBlackRect1.centerx = -60
                    warriorBlackRect1.centery = -60
                if archbishopWhiteRect.colliderect(legionaryBlackRect2):
                    figuresBlack[12] = ""
                    legionaryBlackRect2.centerx = -60
                    legionaryBlackRect2.centery = -60
                if archbishopWhiteRect.colliderect(warriorBlackRect2):
                    figuresBlack[13] = ""
                    warriorBlackRect2.centerx = -60
                    warriorBlackRect2.centery = -60
                if archbishopWhiteRect.colliderect(legionaryBlackRect3):
                    figuresBlack[14] = ""
                    legionaryBlackRect3.centerx = -60
                    legionaryBlackRect3.centery = -60
                if archbishopWhiteRect.colliderect(warriorBlackRect3):
                    figuresBlack[15] = ""
                    warriorBlackRect3.centerx = -60
                    warriorBlackRect3.centery = -60

                if cardinalWhiteRect.colliderect(plagueDoctorBlackRect):
                    figuresBlack[0] = ""
                    plagueDoctorBlackRect.centerx = -60
                    plagueDoctorBlackRect.centery = -60
                if cardinalWhiteRect.colliderect(archbishopBlackRect):
                    figuresBlack[1] = ""
                    archbishopBlackRect.centerx = -60
                    archbishopBlackRect.centery = -60
                if cardinalWhiteRect.colliderect(cardinalBlackRect):
                    figuresBlack[2] = ""
                    cardinalBlackRect.centerx = -60
                    cardinalBlackRect.centery = -60
                if cardinalWhiteRect.colliderect(hadesBlackRect):
                    figuresBlack[3] = ""
                    hadesBlackRect.centerx = -60
                    hadesBlackRect.centery = -60
                if cardinalWhiteRect.colliderect(persephoneBlackRect):
                    figuresBlack[4] = ""
                    persephoneBlackRect.centerx = -60
                    persephoneBlackRect.centery = -60
                if cardinalWhiteRect.colliderect(cardinalBlackRect1):
                    figuresBlack[5] = ""
                    cardinalBlackRect1.centerx = -60
                    cardinalBlackRect1.centery = -60
                if cardinalWhiteRect.colliderect(archbishopBlackRect1):
                    figuresBlack[6] = ""
                    archbishopBlackRect1.centerx = -60
                    archbishopBlackRect1.centery = -60
                if cardinalWhiteRect.colliderect(plagueDoctorBlackRect1):
                    figuresBlack[7] = ""
                    plagueDoctorBlackRect1.centerx = -60
                    plagueDoctorBlackRect1.centery = -60
                if cardinalWhiteRect.colliderect(legionaryBlackRect):
                    figuresBlack[8] = ""
                    legionaryBlackRect.centerx = -60
                    legionaryBlackRect.centery = -60
                if cardinalWhiteRect.colliderect(warriorBlackRect):
                    figuresBlack[9] = ""
                    warriorBlackRect.centerx = -60
                    warriorBlackRect.centery = -60
                if cardinalWhiteRect.colliderect(legionaryBlackRect1):
                    figuresBlack[10] = ""
                    legionaryBlackRect1.centerx = -60
                    legionaryBlackRect1.centery = -60
                if cardinalWhiteRect.colliderect(warriorBlackRect1):
                    figuresBlack[11] = ""
                    warriorBlackRect1.centerx = -60
                    warriorBlackRect1.centery = -60
                if cardinalWhiteRect.colliderect(legionaryBlackRect2):
                    figuresBlack[12] = ""
                    legionaryBlackRect2.centerx = -60
                    legionaryBlackRect2.centery = -60
                if cardinalWhiteRect.colliderect(warriorBlackRect2):
                    figuresBlack[13] = ""
                    warriorBlackRect2.centerx = -60
                    warriorBlackRect2.centery = -60
                if cardinalWhiteRect.colliderect(legionaryBlackRect3):
                    figuresBlack[14] = ""
                    legionaryBlackRect3.centerx = -60
                    legionaryBlackRect3.centery = -60
                if cardinalWhiteRect.colliderect(warriorBlackRect3):
                    figuresBlack[15] = ""
                    warriorBlackRect3.centerx = -60
                    warriorBlackRect3.centery = -60

                if hadesWhiteRect.colliderect(plagueDoctorBlackRect):
                    figuresBlack[0] = ""
                    plagueDoctorBlackRect.centerx = -60
                    plagueDoctorBlackRect.centery = -60
                if hadesWhiteRect.colliderect(archbishopBlackRect):
                    figuresBlack[1] = ""
                    archbishopBlackRect.centerx = -60
                    archbishopBlackRect.centery = -60
                if hadesWhiteRect.colliderect(cardinalBlackRect):
                    figuresBlack[2] = ""
                    cardinalBlackRect.centerx = -60
                    cardinalBlackRect.centery = -60
                if hadesWhiteRect.colliderect(hadesBlackRect):
                    figuresBlack[3] = ""
                    hadesBlackRect.centerx = -60
                    hadesBlackRect.centery = -60
                if hadesWhiteRect.colliderect(persephoneBlackRect):
                    figuresBlack[4] = ""
                    persephoneBlackRect.centerx = -60
                    persephoneBlackRect.centery = -60
                if hadesWhiteRect.colliderect(cardinalBlackRect1):
                    figuresBlack[5] = ""
                    cardinalBlackRect1.centerx = -60
                    cardinalBlackRect1.centery = -60
                if hadesWhiteRect.colliderect(archbishopBlackRect1):
                    figuresBlack[6] = ""
                    archbishopBlackRect1.centerx = -60
                    archbishopBlackRect1.centery = -60
                if hadesWhiteRect.colliderect(plagueDoctorBlackRect1):
                    figuresBlack[7] = ""
                    plagueDoctorBlackRect1.centerx = -60
                    plagueDoctorBlackRect1.centery = -60
                if hadesWhiteRect.colliderect(legionaryBlackRect):
                    figuresBlack[8] = ""
                    legionaryBlackRect.centerx = -60
                    legionaryBlackRect.centery = -60
                if hadesWhiteRect.colliderect(warriorBlackRect):
                    figuresBlack[9] = ""
                    warriorBlackRect.centerx = -60
                    warriorBlackRect.centery = -60
                if hadesWhiteRect.colliderect(legionaryBlackRect1):
                    figuresBlack[10] = ""
                    legionaryBlackRect1.centerx = -60
                    legionaryBlackRect1.centery = -60
                if hadesWhiteRect.colliderect(warriorBlackRect1):
                    figuresBlack[11] = ""
                    warriorBlackRect1.centerx = -60
                    warriorBlackRect1.centery = -60
                if hadesWhiteRect.colliderect(legionaryBlackRect2):
                    figuresBlack[12] = ""
                    legionaryBlackRect2.centerx = -60
                    legionaryBlackRect2.centery = -60
                if hadesWhiteRect.colliderect(warriorBlackRect2):
                    figuresBlack[13] = ""
                    warriorBlackRect2.centerx = -60
                    warriorBlackRect2.centery = -60
                if hadesWhiteRect.colliderect(legionaryBlackRect3):
                    figuresBlack[14] = ""
                    legionaryBlackRect3.centerx = -60
                    legionaryBlackRect3.centery = -60
                if hadesWhiteRect.colliderect(warriorBlackRect3):
                    figuresBlack[15] = ""
                    warriorBlackRect3.centerx = -60
                    warriorBlackRect3.centery = -60

                if persephoneWhiteRect.colliderect(plagueDoctorBlackRect):
                    figuresBlack[0] = ""
                    plagueDoctorBlackRect.centerx = -60
                    plagueDoctorBlackRect.centery = -60
                if persephoneWhiteRect.colliderect(archbishopBlackRect):
                    figuresBlack[1] = ""
                    archbishopBlackRect.centerx = -60
                    archbishopBlackRect.centery = -60
                if persephoneWhiteRect.colliderect(cardinalBlackRect):
                    figuresBlack[2] = ""
                    cardinalBlackRect.centerx = -60
                    cardinalBlackRect.centery = -60
                if persephoneWhiteRect.colliderect(hadesBlackRect):
                    figuresBlack[3] = ""
                    hadesBlackRect.centerx = -60
                    hadesBlackRect.centery = -60
                if persephoneWhiteRect.colliderect(persephoneBlackRect):
                    figuresBlack[4] = ""
                    persephoneBlackRect.centerx = -60
                    persephoneBlackRect.centery = -60
                if persephoneWhiteRect.colliderect(cardinalBlackRect1):
                    figuresBlack[5] = ""
                    cardinalBlackRect1.centerx = -60
                    cardinalBlackRect1.centery = -60
                if persephoneWhiteRect.colliderect(archbishopBlackRect1):
                    figuresBlack[6] = ""
                    archbishopBlackRect1.centerx = -60
                    archbishopBlackRect1.centery = -60
                if persephoneWhiteRect.colliderect(plagueDoctorBlackRect1):
                    figuresBlack[7] = ""
                    plagueDoctorBlackRect1.centerx = -60
                    plagueDoctorBlackRect1.centery = -60
                if persephoneWhiteRect.colliderect(legionaryBlackRect):
                    figuresBlack[8] = ""
                    legionaryBlackRect.centerx = -60
                    legionaryBlackRect.centery = -60
                if persephoneWhiteRect.colliderect(warriorBlackRect):
                    figuresBlack[9] = ""
                    warriorBlackRect.centerx = -60
                    warriorBlackRect.centery = -60
                if persephoneWhiteRect.colliderect(legionaryBlackRect1):
                    figuresBlack[10] = ""
                    legionaryBlackRect1.centerx = -60
                    legionaryBlackRect1.centery = -60
                if persephoneWhiteRect.colliderect(warriorBlackRect1):
                    figuresBlack[11] = ""
                    warriorBlackRect1.centerx = -60
                    warriorBlackRect1.centery = -60
                if persephoneWhiteRect.colliderect(legionaryBlackRect2):
                    figuresBlack[12] = ""
                    legionaryBlackRect2.centerx = -60
                    legionaryBlackRect2.centery = -60
                if persephoneWhiteRect.colliderect(warriorBlackRect2):
                    figuresBlack[13] = ""
                    warriorBlackRect2.centerx = -60
                    warriorBlackRect2.centery = -60
                if persephoneWhiteRect.colliderect(legionaryBlackRect3):
                    figuresBlack[14] = ""
                    legionaryBlackRect3.centerx = -60
                    legionaryBlackRect3.centery = -60
                if persephoneWhiteRect.colliderect(warriorBlackRect3):
                    figuresBlack[15] = ""
                    warriorBlackRect3.centerx = -60
                    warriorBlackRect3.centery = -60

                if cardinalWhiteRect1.colliderect(plagueDoctorBlackRect):
                    figuresBlack[0] = ""
                    plagueDoctorBlackRect.centerx = -60
                    plagueDoctorBlackRect.centery = -60
                if cardinalWhiteRect1.colliderect(archbishopBlackRect):
                    figuresBlack[1] = ""
                    archbishopBlackRect.centerx = -60
                    archbishopBlackRect.centery = -60
                if cardinalWhiteRect1.colliderect(cardinalBlackRect):
                    figuresBlack[2] = ""
                    cardinalBlackRect.centerx = -60
                    cardinalBlackRect.centery = -60
                if cardinalWhiteRect1.colliderect(hadesBlackRect):
                    figuresBlack[3] = ""
                    hadesBlackRect.centerx = -60
                    hadesBlackRect.centery = -60
                if cardinalWhiteRect1.colliderect(persephoneBlackRect):
                    figuresBlack[4] = ""
                    persephoneBlackRect.centerx = -60
                    persephoneBlackRect.centery = -60
                if cardinalWhiteRect1.colliderect(cardinalBlackRect1):
                    figuresBlack[5] = ""
                    cardinalBlackRect1.centerx = -60
                    cardinalBlackRect1.centery = -60
                if cardinalWhiteRect1.colliderect(archbishopBlackRect1):
                    figuresBlack[6] = ""
                    archbishopBlackRect1.centerx = -60
                    archbishopBlackRect1.centery = -60
                if cardinalWhiteRect1.colliderect(plagueDoctorBlackRect1):
                    figuresBlack[7] = ""
                    plagueDoctorBlackRect1.centerx = -60
                    plagueDoctorBlackRect1.centery = -60
                if cardinalWhiteRect1.colliderect(legionaryBlackRect):
                    figuresBlack[8] = ""
                    legionaryBlackRect.centerx = -60
                    legionaryBlackRect.centery = -60
                if cardinalWhiteRect1.colliderect(warriorBlackRect):
                    figuresBlack[9] = ""
                    warriorBlackRect.centerx = -60
                    warriorBlackRect.centery = -60
                if cardinalWhiteRect1.colliderect(legionaryBlackRect1):
                    figuresBlack[10] = ""
                    legionaryBlackRect1.centerx = -60
                    legionaryBlackRect1.centery = -60
                if cardinalWhiteRect1.colliderect(warriorBlackRect1):
                    figuresBlack[11] = ""
                    warriorBlackRect1.centerx = -60
                    warriorBlackRect1.centery = -60
                if cardinalWhiteRect1.colliderect(legionaryBlackRect2):
                    figuresBlack[12] = ""
                    legionaryBlackRect2.centerx = -60
                    legionaryBlackRect2.centery = -60
                if cardinalWhiteRect1.colliderect(warriorBlackRect2):
                    figuresBlack[13] = ""
                    warriorBlackRect2.centerx = -60
                    warriorBlackRect2.centery = -60
                if cardinalWhiteRect1.colliderect(legionaryBlackRect3):
                    figuresBlack[14] = ""
                    legionaryBlackRect3.centerx = -60
                    legionaryBlackRect3.centery = -60
                if cardinalWhiteRect1.colliderect(warriorBlackRect3):
                    figuresBlack[15] = ""
                    warriorBlackRect3.centerx = -60
                    warriorBlackRect3.centery = -60

                if archbishopWhiteRect1.colliderect(plagueDoctorBlackRect):
                    figuresBlack[0] = ""
                    plagueDoctorBlackRect.centerx = -60
                    plagueDoctorBlackRect.centery = -60
                if archbishopWhiteRect1.colliderect(archbishopBlackRect):
                    figuresBlack[1] = ""
                    archbishopBlackRect.centerx = -60
                    archbishopBlackRect.centery = -60
                if archbishopWhiteRect1.colliderect(cardinalBlackRect):
                    figuresBlack[2] = ""
                    cardinalBlackRect.centerx = -60
                    cardinalBlackRect.centery = -60
                if archbishopWhiteRect1.colliderect(hadesBlackRect):
                    figuresBlack[3] = ""
                    hadesBlackRect.centerx = -60
                    hadesBlackRect.centery = -60
                if archbishopWhiteRect1.colliderect(persephoneBlackRect):
                    figuresBlack[4] = ""
                    persephoneBlackRect.centerx = -60
                    persephoneBlackRect.centery = -60
                if archbishopWhiteRect1.colliderect(cardinalBlackRect1):
                    figuresBlack[5] = ""
                    cardinalBlackRect1.centerx = -60
                    cardinalBlackRect1.centery = -60
                if archbishopWhiteRect1.colliderect(archbishopBlackRect1):
                    figuresBlack[6] = ""
                    archbishopBlackRect1.centerx = -60
                    archbishopBlackRect1.centery = -60
                if archbishopWhiteRect1.colliderect(plagueDoctorBlackRect1):
                    figuresBlack[7] = ""
                    plagueDoctorBlackRect1.centerx = -60
                    plagueDoctorBlackRect1.centery = -60
                if archbishopWhiteRect1.colliderect(legionaryBlackRect):
                    figuresBlack[8] = ""
                    legionaryBlackRect.centerx = -60
                    legionaryBlackRect.centery = -60
                if archbishopWhiteRect1.colliderect(warriorBlackRect):
                    figuresBlack[9] = ""
                    warriorBlackRect.centerx = -60
                    warriorBlackRect.centery = -60
                if archbishopWhiteRect1.colliderect(legionaryBlackRect1):
                    figuresBlack[10] = ""
                    legionaryBlackRect1.centerx = -60
                    legionaryBlackRect1.centery = -60
                if archbishopWhiteRect1.colliderect(warriorBlackRect1):
                    figuresBlack[11] = ""
                    warriorBlackRect1.centerx = -60
                    warriorBlackRect1.centery = -60
                if archbishopWhiteRect1.colliderect(legionaryBlackRect2):
                    figuresBlack[12] = ""
                    legionaryBlackRect2.centerx = -60
                    legionaryBlackRect2.centery = -60
                if archbishopWhiteRect1.colliderect(warriorBlackRect2):
                    figuresBlack[13] = ""
                    warriorBlackRect2.centerx = -60
                    warriorBlackRect2.centery = -60
                if archbishopWhiteRect1.colliderect(legionaryBlackRect3):
                    figuresBlack[14] = ""
                    legionaryBlackRect3.centerx = -60
                    legionaryBlackRect3.centery = -60
                if archbishopWhiteRect1.colliderect(warriorBlackRect3):
                    figuresBlack[15] = ""
                    warriorBlackRect3.centerx = -60
                    warriorBlackRect3.centery = -60

                if plagueDoctorWhiteRect1.colliderect(plagueDoctorBlackRect):
                    figuresBlack[0] = ""
                    plagueDoctorBlackRect.centerx = -60
                    plagueDoctorBlackRect.centery = -60
                if plagueDoctorWhiteRect1.colliderect(archbishopBlackRect):
                    figuresBlack[1] = ""
                    archbishopBlackRect.centerx = -60
                    archbishopBlackRect.centery = -60
                if plagueDoctorWhiteRect1.colliderect(cardinalBlackRect):
                    figuresBlack[2] = ""
                    cardinalBlackRect.centerx = -60
                    cardinalBlackRect.centery = -60
                if plagueDoctorWhiteRect1.colliderect(hadesBlackRect):
                    figuresBlack[3] = ""
                    hadesBlackRect.centerx = -60
                    hadesBlackRect.centery = -60
                if plagueDoctorWhiteRect1.colliderect(persephoneBlackRect):
                    figuresBlack[4] = ""
                    persephoneBlackRect.centerx = -60
                    persephoneBlackRect.centery = -60
                if plagueDoctorWhiteRect1.colliderect(cardinalBlackRect1):
                    figuresBlack[5] = ""
                    cardinalBlackRect1.centerx = -60
                    cardinalBlackRect1.centery = -60
                if plagueDoctorWhiteRect1.colliderect(archbishopBlackRect1):
                    figuresBlack[6] = ""
                    archbishopBlackRect1.centerx = -60
                    archbishopBlackRect1.centery = -60
                if plagueDoctorWhiteRect1.colliderect(plagueDoctorBlackRect1):
                    figuresBlack[7] = ""
                    plagueDoctorBlackRect1.centerx = -60
                    plagueDoctorBlackRect1.centery = -60
                if plagueDoctorWhiteRect1.colliderect(legionaryBlackRect):
                    figuresBlack[8] = ""
                    legionaryBlackRect.centerx = -60
                    legionaryBlackRect.centery = -60
                if plagueDoctorWhiteRect1.colliderect(warriorBlackRect):
                    figuresBlack[9] = ""
                    warriorBlackRect.centerx = -60
                    warriorBlackRect.centery = -60
                if plagueDoctorWhiteRect1.colliderect(legionaryBlackRect1):
                    figuresBlack[10] = ""
                    legionaryBlackRect1.centerx = -60
                    legionaryBlackRect1.centery = -60
                if plagueDoctorWhiteRect1.colliderect(warriorBlackRect1):
                    figuresBlack[11] = ""
                    warriorBlackRect1.centerx = -60
                    warriorBlackRect1.centery = -60
                if plagueDoctorWhiteRect1.colliderect(legionaryBlackRect2):
                    figuresBlack[12] = ""
                    legionaryBlackRect2.centerx = -60
                    legionaryBlackRect2.centery = -60
                if plagueDoctorWhiteRect1.colliderect(warriorBlackRect2):
                    figuresBlack[13] = ""
                    warriorBlackRect2.centerx = -60
                    warriorBlackRect2.centery = -60
                if plagueDoctorWhiteRect1.colliderect(legionaryBlackRect3):
                    figuresBlack[14] = ""
                    legionaryBlackRect3.centerx = -60
                    legionaryBlackRect3.centery = -60
                if plagueDoctorWhiteRect1.colliderect(warriorBlackRect3):
                    figuresBlack[15] = ""
                    warriorBlackRect3.centerx = -60
                    warriorBlackRect3.centery = -60

                if legionaryWhiteRect.colliderect(plagueDoctorBlackRect):
                    figuresBlack[0] = ""
                    plagueDoctorBlackRect.centerx = -60
                    plagueDoctorBlackRect.centery = -60
                if legionaryWhiteRect.colliderect(archbishopBlackRect):
                    figuresBlack[1] = ""
                    archbishopBlackRect.centerx = -60
                    archbishopBlackRect.centery = -60
                if legionaryWhiteRect.colliderect(cardinalBlackRect):
                    figuresBlack[2] = ""
                    cardinalBlackRect.centerx = -60
                    cardinalBlackRect.centery = -60
                if legionaryWhiteRect.colliderect(hadesBlackRect):
                    figuresBlack[3] = ""
                    hadesBlackRect.centerx = -60
                    hadesBlackRect.centery = -60
                if legionaryWhiteRect.colliderect(persephoneBlackRect):
                    figuresBlack[4] = ""
                    persephoneBlackRect.centerx = -60
                    persephoneBlackRect.centery = -60
                if legionaryWhiteRect.colliderect(cardinalBlackRect1):
                    figuresBlack[5] = ""
                    cardinalBlackRect1.centerx = -60
                    cardinalBlackRect1.centery = -60
                if legionaryWhiteRect.colliderect(archbishopBlackRect1):
                    figuresBlack[6] = ""
                    archbishopBlackRect1.centerx = -60
                    archbishopBlackRect1.centery = -60
                if legionaryWhiteRect.colliderect(plagueDoctorBlackRect1):
                    figuresBlack[7] = ""
                    plagueDoctorBlackRect1.centerx = -60
                    plagueDoctorBlackRect1.centery = -60
                if legionaryWhiteRect.colliderect(legionaryBlackRect):
                    figuresBlack[8] = ""
                    legionaryBlackRect.centerx = -60
                    legionaryBlackRect.centery = -60
                if legionaryWhiteRect.colliderect(warriorBlackRect):
                    figuresBlack[9] = ""
                    warriorBlackRect.centerx = -60
                    warriorBlackRect.centery = -60
                if legionaryWhiteRect.colliderect(legionaryBlackRect1):
                    figuresBlack[10] = ""
                    legionaryBlackRect1.centerx = -60
                    legionaryBlackRect1.centery = -60
                if legionaryWhiteRect.colliderect(warriorBlackRect1):
                    figuresBlack[11] = ""
                    warriorBlackRect1.centerx = -60
                    warriorBlackRect1.centery = -60
                if legionaryWhiteRect.colliderect(legionaryBlackRect2):
                    figuresBlack[12] = ""
                    legionaryBlackRect2.centerx = -60
                    legionaryBlackRect2.centery = -60
                if legionaryWhiteRect.colliderect(warriorBlackRect2):
                    figuresBlack[13] = ""
                    warriorBlackRect2.centerx = -60
                    warriorBlackRect2.centery = -60
                if legionaryWhiteRect.colliderect(legionaryBlackRect3):
                    figuresBlack[14] = ""
                    legionaryBlackRect3.centerx = -60
                    legionaryBlackRect3.centery = -60
                if legionaryWhiteRect.colliderect(warriorBlackRect3):
                    figuresBlack[15] = ""
                    warriorBlackRect3.centerx = -60
                    warriorBlackRect3.centery = -60

                if warriorWhiteRect.colliderect(plagueDoctorBlackRect):
                    figuresBlack[0] = ""
                    plagueDoctorBlackRect.centerx = -60
                    plagueDoctorBlackRect.centery = -60
                if warriorWhiteRect.colliderect(archbishopBlackRect):
                    figuresBlack[1] = ""
                    archbishopBlackRect.centerx = -60
                    archbishopBlackRect.centery = -60
                if warriorWhiteRect.colliderect(cardinalBlackRect):
                    figuresBlack[2] = ""
                    cardinalBlackRect.centerx = -60
                    cardinalBlackRect.centery = -60
                if warriorWhiteRect.colliderect(hadesBlackRect):
                    figuresBlack[3] = ""
                    hadesBlackRect.centerx = -60
                    hadesBlackRect.centery = -60
                if warriorWhiteRect.colliderect(persephoneBlackRect):
                    figuresBlack[4] = ""
                    persephoneBlackRect.centerx = -60
                    persephoneBlackRect.centery = -60
                if warriorWhiteRect.colliderect(cardinalBlackRect1):
                    figuresBlack[5] = ""
                    cardinalBlackRect1.centerx = -60
                    cardinalBlackRect1.centery = -60
                if warriorWhiteRect.colliderect(archbishopBlackRect1):
                    figuresBlack[6] = ""
                    archbishopBlackRect1.centerx = -60
                    archbishopBlackRect1.centery = -60
                if warriorWhiteRect.colliderect(plagueDoctorBlackRect1):
                    figuresBlack[7] = ""
                    plagueDoctorBlackRect1.centerx = -60
                    plagueDoctorBlackRect1.centery = -60
                if warriorWhiteRect.colliderect(legionaryBlackRect):
                    figuresBlack[8] = ""
                    legionaryBlackRect.centerx = -60
                    legionaryBlackRect.centery = -60
                if warriorWhiteRect.colliderect(warriorBlackRect):
                    figuresBlack[9] = ""
                    warriorBlackRect.centerx = -60
                    warriorBlackRect.centery = -60
                if warriorWhiteRect.colliderect(legionaryBlackRect1):
                    figuresBlack[10] = ""
                    legionaryBlackRect1.centerx = -60
                    legionaryBlackRect1.centery = -60
                if warriorWhiteRect.colliderect(warriorBlackRect1):
                    figuresBlack[11] = ""
                    warriorBlackRect1.centerx = -60
                    warriorBlackRect1.centery = -60
                if warriorWhiteRect.colliderect(legionaryBlackRect2):
                    figuresBlack[12] = ""
                    legionaryBlackRect2.centerx = -60
                    legionaryBlackRect2.centery = -60
                if warriorWhiteRect.colliderect(warriorBlackRect2):
                    figuresBlack[13] = ""
                    warriorBlackRect2.centerx = -60
                    warriorBlackRect2.centery = -60
                if warriorWhiteRect.colliderect(legionaryBlackRect3):
                    figuresBlack[14] = ""
                    legionaryBlackRect3.centerx = -60
                    legionaryBlackRect3.centery = -60
                if warriorWhiteRect.colliderect(warriorBlackRect3):
                    figuresBlack[15] = ""
                    warriorBlackRect3.centerx = -60
                    warriorBlackRect3.centery = -60

                if legionaryWhiteRect1.colliderect(plagueDoctorBlackRect):
                    figuresBlack[0] = ""
                    plagueDoctorBlackRect.centerx = -60
                    plagueDoctorBlackRect.centery = -60
                if legionaryWhiteRect1.colliderect(archbishopBlackRect):
                    figuresBlack[1] = ""
                    archbishopBlackRect.centerx = -60
                    archbishopBlackRect.centery = -60
                if legionaryWhiteRect1.colliderect(cardinalBlackRect):
                    figuresBlack[2] = ""
                    cardinalBlackRect.centerx = -60
                    cardinalBlackRect.centery = -60
                if legionaryWhiteRect1.colliderect(hadesBlackRect):
                    figuresBlack[3] = ""
                    hadesBlackRect.centerx = -60
                    hadesBlackRect.centery = -60
                if legionaryWhiteRect1.colliderect(persephoneBlackRect):
                    figuresBlack[4] = ""
                    persephoneBlackRect.centerx = -60
                    persephoneBlackRect.centery = -60
                if legionaryWhiteRect1.colliderect(cardinalBlackRect1):
                    figuresBlack[5] = ""
                    cardinalBlackRect1.centerx = -60
                    cardinalBlackRect1.centery = -60
                if legionaryWhiteRect1.colliderect(archbishopBlackRect1):
                    figuresBlack[6] = ""
                    archbishopBlackRect1.centerx = -60
                    archbishopBlackRect1.centery = -60
                if legionaryWhiteRect1.colliderect(plagueDoctorBlackRect1):
                    figuresBlack[7] = ""
                    plagueDoctorBlackRect1.centerx = -60
                    plagueDoctorBlackRect1.centery = -60
                if legionaryWhiteRect1.colliderect(legionaryBlackRect):
                    figuresBlack[8] = ""
                    legionaryBlackRect.centerx = -60
                    legionaryBlackRect.centery = -60
                if legionaryWhiteRect1.colliderect(warriorBlackRect):
                    figuresBlack[9] = ""
                    warriorBlackRect.centerx = -60
                    warriorBlackRect.centery = -60
                if legionaryWhiteRect1.colliderect(legionaryBlackRect1):
                    figuresBlack[10] = ""
                    legionaryBlackRect1.centerx = -60
                    legionaryBlackRect1.centery = -60
                if legionaryWhiteRect1.colliderect(warriorBlackRect1):
                    figuresBlack[11] = ""
                    warriorBlackRect1.centerx = -60
                    warriorBlackRect1.centery = -60
                if legionaryWhiteRect1.colliderect(legionaryBlackRect2):
                    figuresBlack[12] = ""
                    legionaryBlackRect2.centerx = -60
                    legionaryBlackRect2.centery = -60
                if legionaryWhiteRect1.colliderect(warriorBlackRect2):
                    figuresBlack[13] = ""
                    warriorBlackRect2.centerx = -60
                    warriorBlackRect2.centery = -60
                if legionaryWhiteRect1.colliderect(legionaryBlackRect3):
                    figuresBlack[14] = ""
                    legionaryBlackRect3.centerx = -60
                    legionaryBlackRect3.centery = -60
                if legionaryWhiteRect1.colliderect(warriorBlackRect3):
                    figuresBlack[15] = ""
                    warriorBlackRect3.centerx = -60
                    warriorBlackRect3.centery = -60

                if warriorWhiteRect1.colliderect(plagueDoctorBlackRect):
                    figuresBlack[0] = ""
                    plagueDoctorBlackRect.centerx = -60
                    plagueDoctorBlackRect.centery = -60
                if warriorWhiteRect1.colliderect(archbishopBlackRect):
                    figuresBlack[1] = ""
                    archbishopBlackRect.centerx = -60
                    archbishopBlackRect.centery = -60
                if warriorWhiteRect1.colliderect(cardinalBlackRect):
                    figuresBlack[2] = ""
                    cardinalBlackRect.centerx = -60
                    cardinalBlackRect.centery = -60
                if warriorWhiteRect1.colliderect(hadesBlackRect):
                    figuresBlack[3] = ""
                    hadesBlackRect.centerx = -60
                    hadesBlackRect.centery = -60
                if warriorWhiteRect1.colliderect(persephoneBlackRect):
                    figuresBlack[4] = ""
                    persephoneBlackRect.centerx = -60
                    persephoneBlackRect.centery = -60
                if warriorWhiteRect1.colliderect(cardinalBlackRect1):
                    figuresBlack[5] = ""
                    cardinalBlackRect1.centerx = -60
                    cardinalBlackRect1.centery = -60
                if warriorWhiteRect1.colliderect(archbishopBlackRect1):
                    figuresBlack[6] = ""
                    archbishopBlackRect1.centerx = -60
                    archbishopBlackRect1.centery = -60
                if warriorWhiteRect1.colliderect(plagueDoctorBlackRect1):
                    figuresBlack[7] = ""
                    plagueDoctorBlackRect1.centerx = -60
                    plagueDoctorBlackRect1.centery = -60
                if warriorWhiteRect1.colliderect(legionaryBlackRect):
                    figuresBlack[8] = ""
                    legionaryBlackRect.centerx = -60
                    legionaryBlackRect.centery = -60
                if warriorWhiteRect1.colliderect(warriorBlackRect):
                    figuresBlack[9] = ""
                    warriorBlackRect.centerx = -60
                    warriorBlackRect.centery = -60
                if warriorWhiteRect1.colliderect(legionaryBlackRect1):
                    figuresBlack[10] = ""
                    legionaryBlackRect1.centerx = -60
                    legionaryBlackRect1.centery = -60
                if warriorWhiteRect1.colliderect(warriorBlackRect1):
                    figuresBlack[11] = ""
                    warriorBlackRect1.centerx = -60
                    warriorBlackRect1.centery = -60
                if warriorWhiteRect1.colliderect(legionaryBlackRect2):
                    figuresBlack[12] = ""
                    legionaryBlackRect2.centerx = -60
                    legionaryBlackRect2.centery = -60
                if warriorWhiteRect1.colliderect(warriorBlackRect2):
                    figuresBlack[13] = ""
                    warriorBlackRect2.centerx = -60
                    warriorBlackRect2.centery = -60
                if warriorWhiteRect1.colliderect(legionaryBlackRect3):
                    figuresBlack[14] = ""
                    legionaryBlackRect3.centerx = -60
                    legionaryBlackRect3.centery = -60
                if warriorWhiteRect1.colliderect(warriorBlackRect3):
                    figuresBlack[15] = ""
                    warriorBlackRect3.centerx = -60
                    warriorBlackRect3.centery = -60

                if legionaryWhiteRect2.colliderect(plagueDoctorBlackRect):
                    figuresBlack[0] = ""
                    plagueDoctorBlackRect.centerx = -60
                    plagueDoctorBlackRect.centery = -60
                if legionaryWhiteRect2.colliderect(archbishopBlackRect):
                    figuresBlack[1] = ""
                    archbishopBlackRect.centerx = -60
                    archbishopBlackRect.centery = -60
                if legionaryWhiteRect2.colliderect(cardinalBlackRect):
                    figuresBlack[2] = ""
                    cardinalBlackRect.centerx = -60
                    cardinalBlackRect.centery = -60
                if legionaryWhiteRect2.colliderect(hadesBlackRect):
                    figuresBlack[3] = ""
                    hadesBlackRect.centerx = -60
                    hadesBlackRect.centery = -60
                if legionaryWhiteRect2.colliderect(persephoneBlackRect):
                    figuresBlack[4] = ""
                    persephoneBlackRect.centerx = -60
                    persephoneBlackRect.centery = -60
                if legionaryWhiteRect2.colliderect(cardinalBlackRect1):
                    figuresBlack[5] = ""
                    cardinalBlackRect1.centerx = -60
                    cardinalBlackRect1.centery = -60
                if legionaryWhiteRect2.colliderect(archbishopBlackRect1):
                    figuresBlack[6] = ""
                    archbishopBlackRect1.centerx = -60
                    archbishopBlackRect1.centery = -60
                if legionaryWhiteRect2.colliderect(plagueDoctorBlackRect1):
                    figuresBlack[7] = ""
                    plagueDoctorBlackRect1.centerx = -60
                    plagueDoctorBlackRect1.centery = -60
                if legionaryWhiteRect2.colliderect(legionaryBlackRect):
                    figuresBlack[8] = ""
                    legionaryBlackRect.centerx = -60
                    legionaryBlackRect.centery = -60
                if legionaryWhiteRect2.colliderect(warriorBlackRect):
                    figuresBlack[9] = ""
                    warriorBlackRect.centerx = -60
                    warriorBlackRect.centery = -60
                if legionaryWhiteRect2.colliderect(legionaryBlackRect1):
                    figuresBlack[10] = ""
                    legionaryBlackRect1.centerx = -60
                    legionaryBlackRect1.centery = -60
                if legionaryWhiteRect2.colliderect(warriorBlackRect1):
                    figuresBlack[11] = ""
                    warriorBlackRect1.centerx = -60
                    warriorBlackRect1.centery = -60
                if legionaryWhiteRect2.colliderect(legionaryBlackRect2):
                    figuresBlack[12] = ""
                    legionaryBlackRect2.centerx = -60
                    legionaryBlackRect2.centery = -60
                if legionaryWhiteRect2.colliderect(warriorBlackRect2):
                    figuresBlack[13] = ""
                    warriorBlackRect2.centerx = -60
                    warriorBlackRect2.centery = -60
                if legionaryWhiteRect2.colliderect(legionaryBlackRect3):
                    figuresBlack[14] = ""
                    legionaryBlackRect3.centerx = -60
                    legionaryBlackRect3.centery = -60
                if legionaryWhiteRect2.colliderect(warriorBlackRect3):
                    figuresBlack[15] = ""
                    warriorBlackRect3.centerx = -60
                    warriorBlackRect3.centery = -60

                if warriorWhiteRect2.colliderect(plagueDoctorBlackRect):
                    figuresBlack[0] = ""
                    plagueDoctorBlackRect.centerx = -60
                    plagueDoctorBlackRect.centery = -60
                if warriorWhiteRect2.colliderect(archbishopBlackRect):
                    figuresBlack[1] = ""
                    archbishopBlackRect.centerx = -60
                    archbishopBlackRect.centery = -60
                if warriorWhiteRect2.colliderect(cardinalBlackRect):
                    figuresBlack[2] = ""
                    cardinalBlackRect.centerx = -60
                    cardinalBlackRect.centery = -60
                if warriorWhiteRect2.colliderect(hadesBlackRect):
                    figuresBlack[3] = ""
                    hadesBlackRect.centerx = -60
                    hadesBlackRect.centery = -60
                if warriorWhiteRect2.colliderect(persephoneBlackRect):
                    figuresBlack[4] = ""
                    persephoneBlackRect.centerx = -60
                    persephoneBlackRect.centery = -60
                if warriorWhiteRect2.colliderect(cardinalBlackRect1):
                    figuresBlack[5] = ""
                    cardinalBlackRect1.centerx = -60
                    cardinalBlackRect1.centery = -60
                if warriorWhiteRect2.colliderect(archbishopBlackRect1):
                    figuresBlack[6] = ""
                    archbishopBlackRect1.centerx = -60
                    archbishopBlackRect1.centery = -60
                if warriorWhiteRect2.colliderect(plagueDoctorBlackRect1):
                    figuresBlack[7] = ""
                    plagueDoctorBlackRect1.centerx = -60
                    plagueDoctorBlackRect1.centery = -60
                if warriorWhiteRect2.colliderect(legionaryBlackRect):
                    figuresBlack[8] = ""
                    legionaryBlackRect.centerx = -60
                    legionaryBlackRect.centery = -60
                if warriorWhiteRect2.colliderect(warriorBlackRect):
                    figuresBlack[9] = ""
                    warriorBlackRect.centerx = -60
                    warriorBlackRect.centery = -60
                if warriorWhiteRect2.colliderect(legionaryBlackRect1):
                    figuresBlack[10] = ""
                    legionaryBlackRect1.centerx = -60
                    legionaryBlackRect1.centery = -60
                if warriorWhiteRect2.colliderect(warriorBlackRect1):
                    figuresBlack[11] = ""
                    warriorBlackRect1.centerx = -60
                    warriorBlackRect1.centery = -60
                if warriorWhiteRect2.colliderect(legionaryBlackRect2):
                    figuresBlack[12] = ""
                    legionaryBlackRect2.centerx = -60
                    legionaryBlackRect2.centery = -60
                if warriorWhiteRect2.colliderect(warriorBlackRect2):
                    figuresBlack[13] = ""
                    warriorBlackRect2.centerx = -60
                    warriorBlackRect2.centery = -60
                if warriorWhiteRect2.colliderect(legionaryBlackRect3):
                    figuresBlack[14] = ""
                    legionaryBlackRect3.centerx = -60
                    legionaryBlackRect3.centery = -60
                if warriorWhiteRect2.colliderect(warriorBlackRect3):
                    figuresBlack[15] = ""
                    warriorBlackRect3.centerx = -60
                    warriorBlackRect3.centery = -60

                if legionaryWhiteRect3.colliderect(plagueDoctorBlackRect):
                    figuresBlack[0] = ""
                    plagueDoctorBlackRect.centerx = -60
                    plagueDoctorBlackRect.centery = -60
                if legionaryWhiteRect3.colliderect(archbishopBlackRect):
                    figuresBlack[1] = ""
                    archbishopBlackRect.centerx = -60
                    archbishopBlackRect.centery = -60
                if legionaryWhiteRect3.colliderect(cardinalBlackRect):
                    figuresBlack[2] = ""
                    cardinalBlackRect.centerx = -60
                    cardinalBlackRect.centery = -60
                if legionaryWhiteRect3.colliderect(hadesBlackRect):
                    figuresBlack[3] = ""
                    hadesBlackRect.centerx = -60
                    hadesBlackRect.centery = -60
                if legionaryWhiteRect3.colliderect(persephoneBlackRect):
                    figuresBlack[4] = ""
                    persephoneBlackRect.centerx = -60
                    persephoneBlackRect.centery = -60
                if legionaryWhiteRect3.colliderect(cardinalBlackRect1):
                    figuresBlack[5] = ""
                    cardinalBlackRect1.centerx = -60
                    cardinalBlackRect1.centery = -60
                if legionaryWhiteRect3.colliderect(archbishopBlackRect1):
                    figuresBlack[6] = ""
                    archbishopBlackRect1.centerx = -60
                    archbishopBlackRect1.centery = -60
                if legionaryWhiteRect3.colliderect(plagueDoctorBlackRect1):
                    figuresBlack[7] = ""
                    plagueDoctorBlackRect1.centerx = -60
                    plagueDoctorBlackRect1.centery = -60
                if legionaryWhiteRect3.colliderect(legionaryBlackRect):
                    figuresBlack[8] = ""
                    legionaryBlackRect.centerx = -60
                    legionaryBlackRect.centery = -60
                if legionaryWhiteRect3.colliderect(warriorBlackRect):
                    figuresBlack[9] = ""
                    warriorBlackRect.centerx = -60
                    warriorBlackRect.centery = -60
                if legionaryWhiteRect3.colliderect(legionaryBlackRect1):
                    figuresBlack[10] = ""
                    legionaryBlackRect1.centerx = -60
                    legionaryBlackRect1.centery = -60
                if legionaryWhiteRect3.colliderect(warriorBlackRect1):
                    figuresBlack[11] = ""
                    warriorBlackRect1.centerx = -60
                    warriorBlackRect1.centery = -60
                if legionaryWhiteRect3.colliderect(legionaryBlackRect2):
                    figuresBlack[12] = ""
                    legionaryBlackRect2.centerx = -60
                    legionaryBlackRect2.centery = -60
                if legionaryWhiteRect3.colliderect(warriorBlackRect2):
                    figuresBlack[13] = ""
                    warriorBlackRect2.centerx = -60
                    warriorBlackRect2.centery = -60
                if legionaryWhiteRect3.colliderect(legionaryBlackRect3):
                    figuresBlack[14] = ""
                    legionaryBlackRect3.centerx = -60
                    legionaryBlackRect3.centery = -60
                if legionaryWhiteRect3.colliderect(warriorBlackRect3):
                    figuresBlack[15] = ""
                    warriorBlackRect3.centerx = -60
                    warriorBlackRect3.centery = -60

                if warriorWhiteRect3.colliderect(plagueDoctorBlackRect):
                    figuresBlack[0] = ""
                    plagueDoctorBlackRect.centerx = -60
                    plagueDoctorBlackRect.centery = -60
                if warriorWhiteRect3.colliderect(archbishopBlackRect):
                    figuresBlack[1] = ""
                    archbishopBlackRect.centerx = -60
                    archbishopBlackRect.centery = -60
                if warriorWhiteRect3.colliderect(cardinalBlackRect):
                    figuresBlack[2] = ""
                    cardinalBlackRect.centerx = -60
                    cardinalBlackRect.centery = -60
                if warriorWhiteRect3.colliderect(hadesBlackRect):
                    figuresBlack[3] = ""
                    hadesBlackRect.centerx = -60
                    hadesBlackRect.centery = -60
                if warriorWhiteRect3.colliderect(persephoneBlackRect):
                    figuresBlack[4] = ""
                    persephoneBlackRect.centerx = -60
                    persephoneBlackRect.centery = -60
                if warriorWhiteRect3.colliderect(cardinalBlackRect1):
                    figuresBlack[5] = ""
                    cardinalBlackRect1.centerx = -60
                    cardinalBlackRect1.centery = -60
                if warriorWhiteRect3.colliderect(archbishopBlackRect1):
                    figuresBlack[6] = ""
                    archbishopBlackRect1.centerx = -60
                    archbishopBlackRect1.centery = -60
                if warriorWhiteRect3.colliderect(plagueDoctorBlackRect1):
                    figuresBlack[7] = ""
                    plagueDoctorBlackRect1.centerx = -60
                    plagueDoctorBlackRect1.centery = -60
                if warriorWhiteRect3.colliderect(legionaryBlackRect):
                    figuresBlack[8] = ""
                    legionaryBlackRect.centerx = -60
                    legionaryBlackRect.centery = -60
                if warriorWhiteRect3.colliderect(warriorBlackRect):
                    figuresBlack[9] = ""
                    warriorBlackRect.centerx = -60
                    warriorBlackRect.centery = -60
                if warriorWhiteRect3.colliderect(legionaryBlackRect1):
                    figuresBlack[10] = ""
                    legionaryBlackRect1.centerx = -60
                    legionaryBlackRect1.centery = -60
                if warriorWhiteRect3.colliderect(warriorBlackRect1):
                    figuresBlack[11] = ""
                    warriorBlackRect1.centerx = -60
                    warriorBlackRect1.centery = -60
                if warriorWhiteRect3.colliderect(legionaryBlackRect2):
                    figuresBlack[12] = ""
                    legionaryBlackRect2.centerx = -60
                    legionaryBlackRect2.centery = -60
                if warriorWhiteRect3.colliderect(warriorBlackRect2):
                    figuresBlack[13] = ""
                    warriorBlackRect2.centerx = -60
                    warriorBlackRect2.centery = -60
                if warriorWhiteRect3.colliderect(legionaryBlackRect3):
                    figuresBlack[14] = ""
                    legionaryBlackRect3.centerx = -60
                    legionaryBlackRect3.centery = -60
                if warriorWhiteRect3.colliderect(warriorBlackRect3):
                    figuresBlack[15] = ""
                    warriorBlackRect3.centerx = -60
                    warriorBlackRect3.centery = -60

            else:
                if plagueDoctorBlackRect.colliderect(plagueDoctorWhiteRect):
                    figuresWhite[0] = ""
                    plagueDoctorWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if plagueDoctorBlackRect.colliderect(archbishopWhiteRect):
                    figuresWhite[1] = ""
                    archbishopWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if plagueDoctorBlackRect.colliderect(cardinalWhiteRect):
                    figuresWhite[2] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if plagueDoctorBlackRect.colliderect(hadesWhiteRect):
                    figuresWhite[3] = ""
                    hadesWhiteRect.centerx = -120
                    hadesWhiteRect.centery = -120
                if plagueDoctorBlackRect.colliderect(persephoneWhiteRect):
                    figuresWhite[4] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if plagueDoctorBlackRect.colliderect(cardinalWhiteRect1):
                    figuresWhite[5] = ""
                    cardinalWhiteRect1.centerx = -120
                    cardinalWhiteRect1.centery = -120
                if plagueDoctorBlackRect.colliderect(archbishopWhiteRect1):
                    figuresWhite[6] = ""
                    archbishopWhiteRect1.centerx = -120
                    archbishopWhiteRect1.centery = -120
                if plagueDoctorBlackRect.colliderect(plagueDoctorWhiteRect1):
                    figuresWhite[7] = ""
                    plagueDoctorWhiteRect1.centerx = -120
                    plagueDoctorWhiteRect1.centery = -120
                if plagueDoctorBlackRect.colliderect(legionaryWhiteRect):
                    figuresWhite[8] = ""
                    legionaryWhiteRect.centerx = -120
                    legionaryWhiteRect.centery = -120
                if plagueDoctorBlackRect.colliderect(warriorWhiteRect):
                    figuresWhite[9] = ""
                    warriorWhiteRect.centerx = -120
                    warriorWhiteRect.centery = -120
                if plagueDoctorBlackRect.colliderect(legionaryWhiteRect1):
                    figuresWhite[10] = ""
                    legionaryWhiteRect1.centerx = -120
                    legionaryWhiteRect1.centery = -120
                if plagueDoctorBlackRect.colliderect(warriorWhiteRect1):
                    figuresWhite[11] = ""
                    warriorWhiteRect1.centerx = -120
                    warriorWhiteRect1.centery = -120
                if plagueDoctorBlackRect.colliderect(legionaryWhiteRect2):
                    figuresWhite[12] = ""
                    legionaryWhiteRect2.centerx = -120
                    legionaryWhiteRect2.centery = -120
                if plagueDoctorBlackRect.colliderect(warriorWhiteRect2):
                    figuresWhite[13] = ""
                    warriorWhiteRect2.centerx = -120
                    warriorWhiteRect2.centery = -120
                if plagueDoctorBlackRect.colliderect(legionaryWhiteRect3):
                    figuresWhite[14] = ""
                    legionaryWhiteRect3.centerx = -120
                    legionaryWhiteRect3.centery = -120
                if plagueDoctorBlackRect.colliderect(warriorWhiteRect3):
                    figuresWhite[15] = ""
                    warriorWhiteRect3.centerx = -120
                    warriorWhiteRect3.centery = -120

                if archbishopBlackRect.colliderect(plagueDoctorWhiteRect):
                    figuresWhite[0] = ""
                    plagueDoctorWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if archbishopBlackRect.colliderect(archbishopWhiteRect):
                    figuresWhite[1] = ""
                    archbishopWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if archbishopBlackRect.colliderect(cardinalWhiteRect):
                    figuresWhite[2] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if archbishopBlackRect.colliderect(hadesWhiteRect):
                    figuresWhite[3] = ""
                    hadesWhiteRect.centerx = -120
                    hadesWhiteRect.centery = -120
                if archbishopBlackRect.colliderect(persephoneWhiteRect):
                    figuresWhite[4] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if archbishopBlackRect.colliderect(cardinalWhiteRect1):
                    figuresWhite[5] = ""
                    cardinalWhiteRect1.centerx = -120
                    cardinalWhiteRect1.centery = -120
                if archbishopBlackRect.colliderect(archbishopWhiteRect1):
                    figuresWhite[6] = ""
                    archbishopWhiteRect1.centerx = -120
                    archbishopWhiteRect1.centery = -120
                if archbishopBlackRect.colliderect(plagueDoctorWhiteRect1):
                    figuresWhite[7] = ""
                    plagueDoctorWhiteRect1.centerx = -120
                    plagueDoctorWhiteRect1.centery = -120
                if archbishopBlackRect.colliderect(legionaryWhiteRect):
                    figuresWhite[8] = ""
                    legionaryWhiteRect.centerx = -120
                    legionaryWhiteRect.centery = -120
                if archbishopBlackRect.colliderect(warriorWhiteRect):
                    figuresWhite[9] = ""
                    warriorWhiteRect.centerx = -120
                    warriorWhiteRect.centery = -120
                if archbishopBlackRect.colliderect(legionaryWhiteRect1):
                    figuresWhite[10] = ""
                    legionaryWhiteRect1.centerx = -120
                    legionaryWhiteRect1.centery = -120
                if archbishopBlackRect.colliderect(warriorWhiteRect1):
                    figuresWhite[11] = ""
                    warriorWhiteRect1.centerx = -120
                    warriorWhiteRect1.centery = -120
                if archbishopBlackRect.colliderect(legionaryWhiteRect2):
                    figuresWhite[12] = ""
                    legionaryWhiteRect2.centerx = -120
                    legionaryWhiteRect2.centery = -120
                if archbishopBlackRect.colliderect(warriorWhiteRect2):
                    figuresWhite[13] = ""
                    warriorWhiteRect2.centerx = -120
                    warriorWhiteRect2.centery = -120
                if archbishopBlackRect.colliderect(legionaryWhiteRect3):
                    figuresWhite[14] = ""
                    legionaryWhiteRect3.centerx = -120
                    legionaryWhiteRect3.centery = -120
                if archbishopBlackRect.colliderect(warriorWhiteRect3):
                    figuresWhite[15] = ""
                    warriorWhiteRect3.centerx = -120
                    warriorWhiteRect3.centery = -120

                if cardinalBlackRect.colliderect(plagueDoctorWhiteRect):
                    figuresWhite[0] = ""
                    plagueDoctorWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if cardinalBlackRect.colliderect(archbishopWhiteRect):
                    figuresWhite[1] = ""
                    archbishopWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if cardinalBlackRect.colliderect(cardinalWhiteRect):
                    figuresWhite[2] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if cardinalBlackRect.colliderect(hadesWhiteRect):
                    figuresWhite[3] = ""
                    hadesWhiteRect.centerx = -120
                    hadesWhiteRect.centery = -120
                if cardinalBlackRect.colliderect(persephoneWhiteRect):
                    figuresWhite[4] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if cardinalBlackRect.colliderect(cardinalWhiteRect1):
                    figuresWhite[5] = ""
                    cardinalWhiteRect1.centerx = -120
                    cardinalWhiteRect1.centery = -120
                if cardinalBlackRect.colliderect(archbishopWhiteRect1):
                    figuresWhite[6] = ""
                    archbishopWhiteRect1.centerx = -120
                    archbishopWhiteRect1.centery = -120
                if cardinalBlackRect.colliderect(plagueDoctorWhiteRect1):
                    figuresWhite[7] = ""
                    plagueDoctorWhiteRect1.centerx = -120
                    plagueDoctorWhiteRect1.centery = -120
                if cardinalBlackRect.colliderect(legionaryWhiteRect):
                    figuresWhite[8] = ""
                    legionaryWhiteRect.centerx = -120
                    legionaryWhiteRect.centery = -120
                if cardinalBlackRect.colliderect(warriorWhiteRect):
                    figuresWhite[9] = ""
                    warriorWhiteRect.centerx = -120
                    warriorWhiteRect.centery = -120
                if cardinalBlackRect.colliderect(legionaryWhiteRect1):
                    figuresWhite[10] = ""
                    legionaryWhiteRect1.centerx = -120
                    legionaryWhiteRect1.centery = -120
                if cardinalBlackRect.colliderect(warriorWhiteRect1):
                    figuresWhite[11] = ""
                    warriorWhiteRect1.centerx = -120
                    warriorWhiteRect1.centery = -120
                if cardinalBlackRect.colliderect(legionaryWhiteRect2):
                    figuresWhite[12] = ""
                    legionaryWhiteRect2.centerx = -120
                    legionaryWhiteRect2.centery = -120
                if cardinalBlackRect.colliderect(warriorWhiteRect2):
                    figuresWhite[13] = ""
                    warriorWhiteRect2.centerx = -120
                    warriorWhiteRect2.centery = -120
                if cardinalBlackRect.colliderect(legionaryWhiteRect3):
                    figuresWhite[14] = ""
                    legionaryWhiteRect3.centerx = -120
                    legionaryWhiteRect3.centery = -120
                if cardinalBlackRect.colliderect(warriorWhiteRect3):
                    figuresWhite[15] = ""
                    warriorWhiteRect3.centerx = -120
                    warriorWhiteRect3.centery = -120

                if hadesBlackRect.colliderect(plagueDoctorWhiteRect):
                    figuresWhite[0] = ""
                    plagueDoctorWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if hadesBlackRect.colliderect(archbishopWhiteRect):
                    figuresWhite[1] = ""
                    archbishopWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if hadesBlackRect.colliderect(cardinalWhiteRect):
                    figuresWhite[2] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if hadesBlackRect.colliderect(hadesWhiteRect):
                    figuresWhite[3] = ""
                    hadesWhiteRect.centerx = -120
                    hadesWhiteRect.centery = -120
                if hadesBlackRect.colliderect(persephoneWhiteRect):
                    figuresWhite[4] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if hadesBlackRect.colliderect(cardinalWhiteRect1):
                    figuresWhite[5] = ""
                    cardinalWhiteRect1.centerx = -120
                    cardinalWhiteRect1.centery = -120
                if hadesBlackRect.colliderect(archbishopWhiteRect1):
                    figuresWhite[6] = ""
                    archbishopWhiteRect1.centerx = -120
                    archbishopWhiteRect1.centery = -120
                if hadesBlackRect.colliderect(plagueDoctorWhiteRect1):
                    figuresWhite[7] = ""
                    plagueDoctorWhiteRect1.centerx = -120
                    plagueDoctorWhiteRect1.centery = -120
                if hadesBlackRect.colliderect(legionaryWhiteRect):
                    figuresWhite[8] = ""
                    legionaryWhiteRect.centerx = -120
                    legionaryWhiteRect.centery = -120
                if hadesBlackRect.colliderect(warriorWhiteRect):
                    figuresWhite[9] = ""
                    warriorWhiteRect.centerx = -120
                    warriorWhiteRect.centery = -120
                if hadesBlackRect.colliderect(legionaryWhiteRect1):
                    figuresWhite[10] = ""
                    legionaryWhiteRect1.centerx = -120
                    legionaryWhiteRect1.centery = -120
                if hadesBlackRect.colliderect(warriorWhiteRect1):
                    figuresWhite[11] = ""
                    warriorWhiteRect1.centerx = -120
                    warriorWhiteRect1.centery = -120
                if hadesBlackRect.colliderect(legionaryWhiteRect2):
                    figuresWhite[12] = ""
                    legionaryWhiteRect2.centerx = -120
                    legionaryWhiteRect2.centery = -120
                if hadesBlackRect.colliderect(warriorWhiteRect2):
                    figuresWhite[13] = ""
                    warriorWhiteRect2.centerx = -120
                    warriorWhiteRect2.centery = -120
                if hadesBlackRect.colliderect(legionaryWhiteRect3):
                    figuresWhite[14] = ""
                    legionaryWhiteRect3.centerx = -120
                    legionaryWhiteRect3.centery = -120
                if hadesBlackRect.colliderect(warriorWhiteRect3):
                    figuresWhite[15] = ""
                    warriorWhiteRect3.centerx = -120
                    warriorWhiteRect3.centery = -120

                if persephoneBlackRect.colliderect(plagueDoctorWhiteRect):
                    figuresWhite[0] = ""
                    plagueDoctorWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if persephoneBlackRect.colliderect(archbishopWhiteRect):
                    figuresWhite[1] = ""
                    archbishopWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if persephoneBlackRect.colliderect(cardinalWhiteRect):
                    figuresWhite[2] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if persephoneBlackRect.colliderect(hadesWhiteRect):
                    figuresWhite[3] = ""
                    hadesWhiteRect.centerx = -120
                    hadesWhiteRect.centery = -120
                if persephoneBlackRect.colliderect(persephoneWhiteRect):
                    figuresWhite[4] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if persephoneBlackRect.colliderect(cardinalWhiteRect1):
                    figuresWhite[5] = ""
                    cardinalWhiteRect1.centerx = -120
                    cardinalWhiteRect1.centery = -120
                if persephoneBlackRect.colliderect(archbishopWhiteRect1):
                    figuresWhite[6] = ""
                    archbishopWhiteRect1.centerx = -120
                    archbishopWhiteRect1.centery = -120
                if persephoneBlackRect.colliderect(plagueDoctorWhiteRect1):
                    figuresWhite[7] = ""
                    plagueDoctorWhiteRect1.centerx = -120
                    plagueDoctorWhiteRect1.centery = -120
                if persephoneBlackRect.colliderect(legionaryWhiteRect):
                    figuresWhite[8] = ""
                    legionaryWhiteRect.centerx = -120
                    legionaryWhiteRect.centery = -120
                if persephoneBlackRect.colliderect(warriorWhiteRect):
                    figuresWhite[9] = ""
                    warriorWhiteRect.centerx = -120
                    warriorWhiteRect.centery = -120
                if persephoneBlackRect.colliderect(legionaryWhiteRect1):
                    figuresWhite[10] = ""
                    legionaryWhiteRect1.centerx = -120
                    legionaryWhiteRect1.centery = -120
                if persephoneBlackRect.colliderect(warriorWhiteRect1):
                    figuresWhite[11] = ""
                    warriorWhiteRect1.centerx = -120
                    warriorWhiteRect1.centery = -120
                if persephoneBlackRect.colliderect(legionaryWhiteRect2):
                    figuresWhite[12] = ""
                    legionaryWhiteRect2.centerx = -120
                    legionaryWhiteRect2.centery = -120
                if persephoneBlackRect.colliderect(warriorWhiteRect2):
                    figuresWhite[13] = ""
                    warriorWhiteRect2.centerx = -120
                    warriorWhiteRect2.centery = -120
                if persephoneBlackRect.colliderect(legionaryWhiteRect3):
                    figuresWhite[14] = ""
                    legionaryWhiteRect3.centerx = -120
                    legionaryWhiteRect3.centery = -120
                if persephoneBlackRect.colliderect(warriorWhiteRect3):
                    figuresWhite[15] = ""
                    warriorWhiteRect3.centerx = -120
                    warriorWhiteRect3.centery = -120

                if cardinalBlackRect1.colliderect(plagueDoctorWhiteRect):
                    figuresWhite[0] = ""
                    plagueDoctorWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if cardinalBlackRect1.colliderect(archbishopWhiteRect):
                    figuresWhite[1] = ""
                    archbishopWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if cardinalBlackRect1.colliderect(cardinalWhiteRect):
                    figuresWhite[2] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if cardinalBlackRect1.colliderect(hadesWhiteRect):
                    figuresWhite[3] = ""
                    hadesWhiteRect.centerx = -120
                    hadesWhiteRect.centery = -120
                if cardinalBlackRect1.colliderect(persephoneWhiteRect):
                    figuresWhite[4] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if cardinalBlackRect1.colliderect(cardinalWhiteRect1):
                    figuresWhite[5] = ""
                    cardinalWhiteRect1.centerx = -120
                    cardinalWhiteRect1.centery = -120
                if cardinalBlackRect1.colliderect(archbishopWhiteRect1):
                    figuresWhite[6] = ""
                    archbishopWhiteRect1.centerx = -120
                    archbishopWhiteRect1.centery = -120
                if cardinalBlackRect1.colliderect(plagueDoctorWhiteRect1):
                    figuresWhite[7] = ""
                    plagueDoctorWhiteRect1.centerx = -120
                    plagueDoctorWhiteRect1.centery = -120
                if cardinalBlackRect1.colliderect(legionaryWhiteRect):
                    figuresWhite[8] = ""
                    legionaryWhiteRect.centerx = -120
                    legionaryWhiteRect.centery = -120
                if cardinalBlackRect1.colliderect(warriorWhiteRect):
                    figuresWhite[9] = ""
                    warriorWhiteRect.centerx = -120
                    warriorWhiteRect.centery = -120
                if cardinalBlackRect1.colliderect(legionaryWhiteRect1):
                    figuresWhite[10] = ""
                    legionaryWhiteRect1.centerx = -120
                    legionaryWhiteRect1.centery = -120
                if cardinalBlackRect1.colliderect(warriorWhiteRect1):
                    figuresWhite[11] = ""
                    warriorWhiteRect1.centerx = -120
                    warriorWhiteRect1.centery = -120
                if cardinalBlackRect1.colliderect(legionaryWhiteRect2):
                    figuresWhite[12] = ""
                    legionaryWhiteRect2.centerx = -120
                    legionaryWhiteRect2.centery = -120
                if cardinalBlackRect1.colliderect(warriorWhiteRect2):
                    figuresWhite[13] = ""
                    warriorWhiteRect2.centerx = -120
                    warriorWhiteRect2.centery = -120
                if cardinalBlackRect1.colliderect(legionaryWhiteRect3):
                    figuresWhite[14] = ""
                    legionaryWhiteRect3.centerx = -120
                    legionaryWhiteRect3.centery = -120
                if cardinalBlackRect1.colliderect(warriorWhiteRect3):
                    figuresWhite[15] = ""
                    warriorWhiteRect3.centerx = -120
                    warriorWhiteRect3.centery = -120

                if archbishopBlackRect1.colliderect(plagueDoctorWhiteRect):
                    figuresWhite[0] = ""
                    plagueDoctorWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if archbishopBlackRect1.colliderect(archbishopWhiteRect):
                    figuresWhite[1] = ""
                    archbishopWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if archbishopBlackRect1.colliderect(cardinalWhiteRect):
                    figuresWhite[2] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if archbishopBlackRect1.colliderect(hadesWhiteRect):
                    figuresWhite[3] = ""
                    hadesWhiteRect.centerx = -120
                    hadesWhiteRect.centery = -120
                if archbishopBlackRect1.colliderect(persephoneWhiteRect):
                    figuresWhite[4] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if archbishopBlackRect1.colliderect(cardinalWhiteRect1):
                    figuresWhite[5] = ""
                    cardinalWhiteRect1.centerx = -120
                    cardinalWhiteRect1.centery = -120
                if archbishopBlackRect1.colliderect(archbishopWhiteRect1):
                    figuresWhite[6] = ""
                    archbishopWhiteRect1.centerx = -120
                    archbishopWhiteRect1.centery = -120
                if archbishopBlackRect1.colliderect(plagueDoctorWhiteRect1):
                    figuresWhite[7] = ""
                    plagueDoctorWhiteRect1.centerx = -120
                    plagueDoctorWhiteRect1.centery = -120
                if archbishopBlackRect1.colliderect(legionaryWhiteRect):
                    figuresWhite[8] = ""
                    legionaryWhiteRect.centerx = -120
                    legionaryWhiteRect.centery = -120
                if archbishopBlackRect1.colliderect(warriorWhiteRect):
                    figuresWhite[9] = ""
                    warriorWhiteRect.centerx = -120
                    warriorWhiteRect.centery = -120
                if archbishopBlackRect1.colliderect(legionaryWhiteRect1):
                    figuresWhite[10] = ""
                    legionaryWhiteRect1.centerx = -120
                    legionaryWhiteRect1.centery = -120
                if archbishopBlackRect1.colliderect(warriorWhiteRect1):
                    figuresWhite[11] = ""
                    warriorWhiteRect1.centerx = -120
                    warriorWhiteRect1.centery = -120
                if archbishopBlackRect1.colliderect(legionaryWhiteRect2):
                    figuresWhite[12] = ""
                    legionaryWhiteRect2.centerx = -120
                    legionaryWhiteRect2.centery = -120
                if archbishopBlackRect1.colliderect(warriorWhiteRect2):
                    figuresWhite[13] = ""
                    warriorWhiteRect2.centerx = -120
                    warriorWhiteRect2.centery = -120
                if archbishopBlackRect1.colliderect(legionaryWhiteRect3):
                    figuresWhite[14] = ""
                    legionaryWhiteRect3.centerx = -120
                    legionaryWhiteRect3.centery = -120
                if archbishopBlackRect1.colliderect(warriorWhiteRect3):
                    figuresWhite[15] = ""
                    warriorWhiteRect3.centerx = -120
                    warriorWhiteRect3.centery = -120

                if plagueDoctorBlackRect1.colliderect(plagueDoctorWhiteRect):
                    figuresWhite[0] = ""
                    plagueDoctorWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if plagueDoctorBlackRect1.colliderect(archbishopWhiteRect):
                    figuresWhite[1] = ""
                    archbishopWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if plagueDoctorBlackRect1.colliderect(cardinalWhiteRect):
                    figuresWhite[2] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if plagueDoctorBlackRect1.colliderect(hadesWhiteRect):
                    figuresWhite[3] = ""
                    hadesWhiteRect.centerx = -120
                    hadesWhiteRect.centery = -120
                if plagueDoctorBlackRect1.colliderect(persephoneWhiteRect):
                    figuresWhite[4] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if plagueDoctorBlackRect1.colliderect(cardinalWhiteRect1):
                    figuresWhite[5] = ""
                    cardinalWhiteRect1.centerx = -120
                    cardinalWhiteRect1.centery = -120
                if plagueDoctorBlackRect1.colliderect(archbishopWhiteRect1):
                    figuresWhite[6] = ""
                    archbishopWhiteRect1.centerx = -120
                    archbishopWhiteRect1.centery = -120
                if plagueDoctorBlackRect1.colliderect(plagueDoctorWhiteRect1):
                    figuresWhite[7] = ""
                    plagueDoctorWhiteRect1.centerx = -120
                    plagueDoctorWhiteRect1.centery = -120
                if plagueDoctorBlackRect1.colliderect(legionaryWhiteRect):
                    figuresWhite[8] = ""
                    legionaryWhiteRect.centerx = -120
                    legionaryWhiteRect.centery = -120
                if plagueDoctorBlackRect1.colliderect(warriorWhiteRect):
                    figuresWhite[9] = ""
                    warriorWhiteRect.centerx = -120
                    warriorWhiteRect.centery = -120
                if plagueDoctorBlackRect1.colliderect(legionaryWhiteRect1):
                    figuresWhite[10] = ""
                    legionaryWhiteRect1.centerx = -120
                    legionaryWhiteRect1.centery = -120
                if plagueDoctorBlackRect1.colliderect(warriorWhiteRect1):
                    figuresWhite[11] = ""
                    warriorWhiteRect1.centerx = -120
                    warriorWhiteRect1.centery = -120
                if plagueDoctorBlackRect1.colliderect(legionaryWhiteRect2):
                    figuresWhite[12] = ""
                    legionaryWhiteRect2.centerx = -120
                    legionaryWhiteRect2.centery = -120
                if plagueDoctorBlackRect1.colliderect(warriorWhiteRect2):
                    figuresWhite[13] = ""
                    warriorWhiteRect2.centerx = -120
                    warriorWhiteRect2.centery = -120
                if plagueDoctorBlackRect1.colliderect(legionaryWhiteRect3):
                    figuresWhite[14] = ""
                    legionaryWhiteRect3.centerx = -120
                    legionaryWhiteRect3.centery = -120
                if plagueDoctorBlackRect1.colliderect(warriorWhiteRect3):
                    figuresWhite[15] = ""
                    warriorWhiteRect3.centerx = -120
                    warriorWhiteRect3.centery = -120

                if legionaryBlackRect.colliderect(plagueDoctorWhiteRect):
                    figuresWhite[0] = ""
                    plagueDoctorWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if legionaryBlackRect.colliderect(archbishopWhiteRect):
                    figuresWhite[1] = ""
                    archbishopWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if legionaryBlackRect.colliderect(cardinalWhiteRect):
                    figuresWhite[2] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if legionaryBlackRect.colliderect(hadesWhiteRect):
                    figuresWhite[3] = ""
                    hadesWhiteRect.centerx = -120
                    hadesWhiteRect.centery = -120
                if legionaryBlackRect.colliderect(persephoneWhiteRect):
                    figuresWhite[4] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if legionaryBlackRect.colliderect(cardinalWhiteRect1):
                    figuresWhite[5] = ""
                    cardinalWhiteRect1.centerx = -120
                    cardinalWhiteRect1.centery = -120
                if legionaryBlackRect.colliderect(archbishopWhiteRect1):
                    figuresWhite[6] = ""
                    archbishopWhiteRect1.centerx = -120
                    archbishopWhiteRect1.centery = -120
                if legionaryBlackRect.colliderect(plagueDoctorWhiteRect1):
                    figuresWhite[7] = ""
                    plagueDoctorWhiteRect1.centerx = -120
                    plagueDoctorWhiteRect1.centery = -120
                if legionaryBlackRect.colliderect(legionaryWhiteRect):
                    figuresWhite[8] = ""
                    legionaryWhiteRect.centerx = -120
                    legionaryWhiteRect.centery = -120
                if legionaryBlackRect.colliderect(warriorWhiteRect):
                    figuresWhite[9] = ""
                    warriorWhiteRect.centerx = -120
                    warriorWhiteRect.centery = -120
                if legionaryBlackRect.colliderect(legionaryWhiteRect1):
                    figuresWhite[10] = ""
                    legionaryWhiteRect1.centerx = -120
                    legionaryWhiteRect1.centery = -120
                if legionaryBlackRect.colliderect(warriorWhiteRect1):
                    figuresWhite[11] = ""
                    warriorWhiteRect1.centerx = -120
                    warriorWhiteRect1.centery = -120
                if legionaryBlackRect.colliderect(legionaryWhiteRect2):
                    figuresWhite[12] = ""
                    legionaryWhiteRect2.centerx = -120
                    legionaryWhiteRect2.centery = -120
                if legionaryBlackRect.colliderect(warriorWhiteRect2):
                    figuresWhite[13] = ""
                    warriorWhiteRect2.centerx = -120
                    warriorWhiteRect2.centery = -120
                if legionaryBlackRect.colliderect(legionaryWhiteRect3):
                    figuresWhite[14] = ""
                    legionaryWhiteRect3.centerx = -120
                    legionaryWhiteRect3.centery = -120
                if legionaryBlackRect.colliderect(warriorWhiteRect3):
                    figuresWhite[15] = ""
                    warriorWhiteRect3.centerx = -120
                    warriorWhiteRect3.centery = -120

                if warriorBlackRect.colliderect(plagueDoctorWhiteRect):
                    figuresWhite[0] = ""
                    plagueDoctorWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if warriorBlackRect.colliderect(archbishopWhiteRect):
                    figuresWhite[1] = ""
                    archbishopWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if warriorBlackRect.colliderect(cardinalWhiteRect):
                    figuresWhite[2] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if warriorBlackRect.colliderect(hadesWhiteRect):
                    figuresWhite[3] = ""
                    hadesWhiteRect.centerx = -120
                    hadesWhiteRect.centery = -120
                if warriorBlackRect.colliderect(persephoneWhiteRect):
                    figuresWhite[4] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if warriorBlackRect.colliderect(cardinalWhiteRect1):
                    figuresWhite[5] = ""
                    cardinalWhiteRect1.centerx = -120
                    cardinalWhiteRect1.centery = -120
                if warriorBlackRect.colliderect(archbishopWhiteRect1):
                    figuresWhite[6] = ""
                    archbishopWhiteRect1.centerx = -120
                    archbishopWhiteRect1.centery = -120
                if warriorBlackRect.colliderect(plagueDoctorWhiteRect1):
                    figuresWhite[7] = ""
                    plagueDoctorWhiteRect1.centerx = -120
                    plagueDoctorWhiteRect1.centery = -120
                if warriorBlackRect.colliderect(legionaryWhiteRect):
                    figuresWhite[8] = ""
                    legionaryWhiteRect.centerx = -120
                    legionaryWhiteRect.centery = -120
                if warriorBlackRect.colliderect(warriorWhiteRect):
                    figuresWhite[9] = ""
                    warriorWhiteRect.centerx = -120
                    warriorWhiteRect.centery = -120
                if warriorBlackRect.colliderect(legionaryWhiteRect1):
                    figuresWhite[10] = ""
                    legionaryWhiteRect1.centerx = -120
                    legionaryWhiteRect1.centery = -120
                if warriorBlackRect.colliderect(warriorWhiteRect1):
                    figuresWhite[11] = ""
                    warriorWhiteRect1.centerx = -120
                    warriorWhiteRect1.centery = -120
                if warriorBlackRect.colliderect(legionaryWhiteRect2):
                    figuresWhite[12] = ""
                    legionaryWhiteRect2.centerx = -120
                    legionaryWhiteRect2.centery = -120
                if warriorBlackRect.colliderect(warriorWhiteRect2):
                    figuresWhite[13] = ""
                    warriorWhiteRect2.centerx = -120
                    warriorWhiteRect2.centery = -120
                if warriorBlackRect.colliderect(legionaryWhiteRect3):
                    figuresWhite[14] = ""
                    legionaryWhiteRect3.centerx = -120
                    legionaryWhiteRect3.centery = -120
                if warriorBlackRect.colliderect(warriorWhiteRect3):
                    figuresWhite[15] = ""
                    warriorWhiteRect3.centerx = -120
                    warriorWhiteRect3.centery = -120

                if legionaryBlackRect1.colliderect(plagueDoctorWhiteRect):
                    figuresWhite[0] = ""
                    plagueDoctorWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if legionaryBlackRect1.colliderect(archbishopWhiteRect):
                    figuresWhite[1] = ""
                    archbishopWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if legionaryBlackRect1.colliderect(cardinalWhiteRect):
                    figuresWhite[2] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if legionaryBlackRect1.colliderect(hadesWhiteRect):
                    figuresWhite[3] = ""
                    hadesWhiteRect.centerx = -120
                    hadesWhiteRect.centery = -120
                if legionaryBlackRect1.colliderect(persephoneWhiteRect):
                    figuresWhite[4] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if legionaryBlackRect1.colliderect(cardinalWhiteRect1):
                    figuresWhite[5] = ""
                    cardinalWhiteRect1.centerx = -120
                    cardinalWhiteRect1.centery = -120
                if legionaryBlackRect1.colliderect(archbishopWhiteRect1):
                    figuresWhite[6] = ""
                    archbishopWhiteRect1.centerx = -120
                    archbishopWhiteRect1.centery = -120
                if legionaryBlackRect1.colliderect(plagueDoctorWhiteRect1):
                    figuresWhite[7] = ""
                    plagueDoctorWhiteRect1.centerx = -120
                    plagueDoctorWhiteRect1.centery = -120
                if legionaryBlackRect1.colliderect(legionaryWhiteRect):
                    figuresWhite[8] = ""
                    legionaryWhiteRect.centerx = -120
                    legionaryWhiteRect.centery = -120
                if legionaryBlackRect1.colliderect(warriorWhiteRect):
                    figuresWhite[9] = ""
                    warriorWhiteRect.centerx = -120
                    warriorWhiteRect.centery = -120
                if legionaryBlackRect1.colliderect(legionaryWhiteRect1):
                    figuresWhite[10] = ""
                    legionaryWhiteRect1.centerx = -120
                    legionaryWhiteRect1.centery = -120
                if legionaryBlackRect1.colliderect(warriorWhiteRect1):
                    figuresWhite[11] = ""
                    warriorWhiteRect1.centerx = -120
                    warriorWhiteRect1.centery = -120
                if legionaryBlackRect1.colliderect(legionaryWhiteRect2):
                    figuresWhite[12] = ""
                    legionaryWhiteRect2.centerx = -120
                    legionaryWhiteRect2.centery = -120
                if legionaryBlackRect1.colliderect(warriorWhiteRect2):
                    figuresWhite[13] = ""
                    warriorWhiteRect2.centerx = -120
                    warriorWhiteRect2.centery = -120
                if legionaryBlackRect1.colliderect(legionaryWhiteRect3):
                    figuresWhite[14] = ""
                    legionaryWhiteRect3.centerx = -120
                    legionaryWhiteRect3.centery = -120
                if legionaryBlackRect1.colliderect(warriorWhiteRect3):
                    figuresWhite[15] = ""
                    warriorWhiteRect3.centerx = -120
                    warriorWhiteRect3.centery = -120

                if warriorBlackRect1.colliderect(plagueDoctorWhiteRect):
                    figuresWhite[0] = ""
                    plagueDoctorWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if warriorBlackRect1.colliderect(archbishopWhiteRect):
                    figuresWhite[1] = ""
                    archbishopWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if warriorBlackRect1.colliderect(cardinalWhiteRect):
                    figuresWhite[2] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if warriorBlackRect1.colliderect(hadesWhiteRect):
                    figuresWhite[3] = ""
                    hadesWhiteRect.centerx = -120
                    hadesWhiteRect.centery = -120
                if warriorBlackRect1.colliderect(persephoneWhiteRect):
                    figuresWhite[4] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if warriorBlackRect1.colliderect(cardinalWhiteRect1):
                    figuresWhite[5] = ""
                    cardinalWhiteRect1.centerx = -120
                    cardinalWhiteRect1.centery = -120
                if warriorBlackRect1.colliderect(archbishopWhiteRect1):
                    figuresWhite[6] = ""
                    archbishopWhiteRect1.centerx = -120
                    archbishopWhiteRect1.centery = -120
                if warriorBlackRect1.colliderect(plagueDoctorWhiteRect1):
                    figuresWhite[7] = ""
                    plagueDoctorWhiteRect1.centerx = -120
                    plagueDoctorWhiteRect1.centery = -120
                if warriorBlackRect1.colliderect(legionaryWhiteRect):
                    figuresWhite[8] = ""
                    legionaryWhiteRect.centerx = -120
                    legionaryWhiteRect.centery = -120
                if warriorBlackRect1.colliderect(warriorWhiteRect):
                    figuresWhite[9] = ""
                    warriorWhiteRect.centerx = -120
                    warriorWhiteRect.centery = -120
                if warriorBlackRect1.colliderect(legionaryWhiteRect1):
                    figuresWhite[10] = ""
                    legionaryWhiteRect1.centerx = -120
                    legionaryWhiteRect1.centery = -120
                if warriorBlackRect1.colliderect(warriorWhiteRect1):
                    figuresWhite[11] = ""
                    warriorWhiteRect1.centerx = -120
                    warriorWhiteRect1.centery = -120
                if warriorBlackRect1.colliderect(legionaryWhiteRect2):
                    figuresWhite[12] = ""
                    legionaryWhiteRect2.centerx = -120
                    legionaryWhiteRect2.centery = -120
                if warriorBlackRect1.colliderect(warriorWhiteRect2):
                    figuresWhite[13] = ""
                    warriorWhiteRect2.centerx = -120
                    warriorWhiteRect2.centery = -120
                if warriorBlackRect1.colliderect(legionaryWhiteRect3):
                    figuresWhite[14] = ""
                    legionaryWhiteRect3.centerx = -120
                    legionaryWhiteRect3.centery = -120
                if warriorBlackRect1.colliderect(warriorWhiteRect3):
                    figuresWhite[15] = ""
                    warriorWhiteRect3.centerx = -120
                    warriorWhiteRect3.centery = -120

                if legionaryBlackRect2.colliderect(plagueDoctorWhiteRect):
                    figuresWhite[0] = ""
                    plagueDoctorWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if legionaryBlackRect2.colliderect(archbishopWhiteRect):
                    figuresWhite[1] = ""
                    archbishopWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if legionaryBlackRect2.colliderect(cardinalWhiteRect):
                    figuresWhite[2] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if legionaryBlackRect2.colliderect(hadesWhiteRect):
                    figuresWhite[3] = ""
                    hadesWhiteRect.centerx = -120
                    hadesWhiteRect.centery = -120
                if legionaryBlackRect2.colliderect(persephoneWhiteRect):
                    figuresWhite[4] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if legionaryBlackRect2.colliderect(cardinalWhiteRect1):
                    figuresWhite[5] = ""
                    cardinalWhiteRect1.centerx = -120
                    cardinalWhiteRect1.centery = -120
                if legionaryBlackRect2.colliderect(archbishopWhiteRect1):
                    figuresWhite[6] = ""
                    archbishopWhiteRect1.centerx = -120
                    archbishopWhiteRect1.centery = -120
                if legionaryBlackRect2.colliderect(plagueDoctorWhiteRect1):
                    figuresWhite[7] = ""
                    plagueDoctorWhiteRect1.centerx = -120
                    plagueDoctorWhiteRect1.centery = -120
                if legionaryBlackRect2.colliderect(legionaryWhiteRect):
                    figuresWhite[8] = ""
                    legionaryWhiteRect.centerx = -120
                    legionaryWhiteRect.centery = -120
                if legionaryBlackRect2.colliderect(warriorWhiteRect):
                    figuresWhite[9] = ""
                    warriorWhiteRect.centerx = -120
                    warriorWhiteRect.centery = -120
                if legionaryBlackRect2.colliderect(legionaryWhiteRect1):
                    figuresWhite[10] = ""
                    legionaryWhiteRect1.centerx = -120
                    legionaryWhiteRect1.centery = -120
                if legionaryBlackRect2.colliderect(warriorWhiteRect1):
                    figuresWhite[11] = ""
                    warriorWhiteRect1.centerx = -120
                    warriorWhiteRect1.centery = -120
                if legionaryBlackRect2.colliderect(legionaryWhiteRect2):
                    figuresWhite[12] = ""
                    legionaryWhiteRect2.centerx = -120
                    legionaryWhiteRect2.centery = -120
                if legionaryBlackRect2.colliderect(warriorWhiteRect2):
                    figuresWhite[13] = ""
                    warriorWhiteRect2.centerx = -120
                    warriorWhiteRect2.centery = -120
                if legionaryBlackRect2.colliderect(legionaryWhiteRect3):
                    figuresWhite[14] = ""
                    legionaryWhiteRect3.centerx = -120
                    legionaryWhiteRect3.centery = -120
                if legionaryBlackRect2.colliderect(warriorWhiteRect3):
                    figuresWhite[15] = ""
                    warriorWhiteRect3.centerx = -120
                    warriorWhiteRect3.centery = -120

                if warriorBlackRect2.colliderect(plagueDoctorWhiteRect):
                    figuresWhite[0] = ""
                    plagueDoctorWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if warriorBlackRect2.colliderect(archbishopWhiteRect):
                    figuresWhite[1] = ""
                    archbishopWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if warriorBlackRect2.colliderect(cardinalWhiteRect):
                    figuresWhite[2] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if warriorBlackRect2.colliderect(hadesWhiteRect):
                    figuresWhite[3] = ""
                    hadesWhiteRect.centerx = -120
                    hadesWhiteRect.centery = -120
                if warriorBlackRect2.colliderect(persephoneWhiteRect):
                    figuresWhite[4] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if warriorBlackRect2.colliderect(cardinalWhiteRect1):
                    figuresWhite[5] = ""
                    cardinalWhiteRect1.centerx = -120
                    cardinalWhiteRect1.centery = -120
                if warriorBlackRect2.colliderect(archbishopWhiteRect1):
                    figuresWhite[6] = ""
                    archbishopWhiteRect1.centerx = -120
                    archbishopWhiteRect1.centery = -120
                if warriorBlackRect2.colliderect(plagueDoctorWhiteRect1):
                    figuresWhite[7] = ""
                    plagueDoctorWhiteRect1.centerx = -120
                    plagueDoctorWhiteRect1.centery = -120
                if warriorBlackRect2.colliderect(legionaryWhiteRect):
                    figuresWhite[8] = ""
                    legionaryWhiteRect.centerx = -120
                    legionaryWhiteRect.centery = -120
                if warriorBlackRect2.colliderect(warriorWhiteRect):
                    figuresWhite[9] = ""
                    warriorWhiteRect.centerx = -120
                    warriorWhiteRect.centery = -120
                if warriorBlackRect2.colliderect(legionaryWhiteRect1):
                    figuresWhite[10] = ""
                    legionaryWhiteRect1.centerx = -120
                    legionaryWhiteRect1.centery = -120
                if warriorBlackRect2.colliderect(warriorWhiteRect1):
                    figuresWhite[11] = ""
                    warriorWhiteRect1.centerx = -120
                    warriorWhiteRect1.centery = -120
                if warriorBlackRect2.colliderect(legionaryWhiteRect2):
                    figuresWhite[12] = ""
                    legionaryWhiteRect2.centerx = -120
                    legionaryWhiteRect2.centery = -120
                if warriorBlackRect2.colliderect(warriorWhiteRect2):
                    figuresWhite[13] = ""
                    warriorWhiteRect2.centerx = -120
                    warriorWhiteRect2.centery = -120
                if warriorBlackRect2.colliderect(legionaryWhiteRect3):
                    figuresWhite[14] = ""
                    legionaryWhiteRect3.centerx = -120
                    legionaryWhiteRect3.centery = -120
                if warriorBlackRect2.colliderect(warriorWhiteRect3):
                    figuresWhite[15] = ""
                    warriorWhiteRect3.centerx = -120
                    warriorWhiteRect3.centery = -120

                if legionaryBlackRect3.colliderect(plagueDoctorWhiteRect):
                    figuresWhite[0] = ""
                    plagueDoctorWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if legionaryBlackRect3.colliderect(archbishopWhiteRect):
                    figuresWhite[1] = ""
                    archbishopWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if legionaryBlackRect3.colliderect(cardinalWhiteRect):
                    figuresWhite[2] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if legionaryBlackRect3.colliderect(hadesWhiteRect):
                    figuresWhite[3] = ""
                    hadesWhiteRect.centerx = -120
                    hadesWhiteRect.centery = -120
                if legionaryBlackRect3.colliderect(persephoneWhiteRect):
                    figuresWhite[4] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if legionaryBlackRect3.colliderect(cardinalWhiteRect1):
                    figuresWhite[5] = ""
                    cardinalWhiteRect1.centerx = -120
                    cardinalWhiteRect1.centery = -120
                if legionaryBlackRect3.colliderect(archbishopWhiteRect1):
                    figuresWhite[6] = ""
                    archbishopWhiteRect1.centerx = -120
                    archbishopWhiteRect1.centery = -120
                if legionaryBlackRect3.colliderect(plagueDoctorWhiteRect1):
                    figuresWhite[7] = ""
                    plagueDoctorWhiteRect1.centerx = -120
                    plagueDoctorWhiteRect1.centery = -120
                if legionaryBlackRect3.colliderect(legionaryWhiteRect):
                    figuresWhite[8] = ""
                    legionaryWhiteRect.centerx = -120
                    legionaryWhiteRect.centery = -120
                if legionaryBlackRect3.colliderect(warriorWhiteRect):
                    figuresWhite[9] = ""
                    warriorWhiteRect.centerx = -120
                    warriorWhiteRect.centery = -120
                if legionaryBlackRect3.colliderect(legionaryWhiteRect1):
                    figuresWhite[10] = ""
                    legionaryWhiteRect1.centerx = -120
                    legionaryWhiteRect1.centery = -120
                if legionaryBlackRect3.colliderect(warriorWhiteRect1):
                    figuresWhite[11] = ""
                    warriorWhiteRect1.centerx = -120
                    warriorWhiteRect1.centery = -120
                if legionaryBlackRect3.colliderect(legionaryWhiteRect2):
                    figuresWhite[12] = ""
                    legionaryWhiteRect2.centerx = -120
                    legionaryWhiteRect2.centery = -120
                if legionaryBlackRect3.colliderect(warriorWhiteRect2):
                    figuresWhite[13] = ""
                    warriorWhiteRect2.centerx = -120
                    warriorWhiteRect2.centery = -120
                if legionaryBlackRect3.colliderect(legionaryWhiteRect3):
                    figuresWhite[14] = ""
                    legionaryWhiteRect3.centerx = -120
                    legionaryWhiteRect3.centery = -120
                if legionaryBlackRect3.colliderect(warriorWhiteRect3):
                    figuresWhite[15] = ""
                    warriorWhiteRect3.centerx = -120
                    warriorWhiteRect3.centery = -120

                if warriorBlackRect3.colliderect(plagueDoctorWhiteRect):
                    figuresWhite[0] = ""
                    plagueDoctorWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if warriorBlackRect3.colliderect(archbishopWhiteRect):
                    figuresWhite[1] = ""
                    archbishopWhiteRect.centerx = -120
                    plagueDoctorWhiteRect.centery = -120
                if warriorBlackRect3.colliderect(cardinalWhiteRect):
                    figuresWhite[2] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if warriorBlackRect3.colliderect(hadesWhiteRect):
                    figuresWhite[3] = ""
                    hadesWhiteRect.centerx = -120
                    hadesWhiteRect.centery = -120
                if warriorBlackRect3.colliderect(persephoneWhiteRect):
                    figuresWhite[4] = ""
                    cardinalBlackRect.centerx = -120
                    cardinalBlackRect.centery = -120
                if warriorBlackRect3.colliderect(cardinalWhiteRect1):
                    figuresWhite[5] = ""
                    cardinalWhiteRect1.centerx = -120
                    cardinalWhiteRect1.centery = -120
                if warriorBlackRect3.colliderect(archbishopWhiteRect1):
                    figuresWhite[6] = ""
                    archbishopWhiteRect1.centerx = -120
                    archbishopWhiteRect1.centery = -120
                if warriorBlackRect3.colliderect(plagueDoctorWhiteRect1):
                    figuresWhite[7] = ""
                    plagueDoctorWhiteRect1.centerx = -120
                    plagueDoctorWhiteRect1.centery = -120
                if warriorBlackRect3.colliderect(legionaryWhiteRect):
                    figuresWhite[8] = ""
                    legionaryWhiteRect.centerx = -120
                    legionaryWhiteRect.centery = -120
                if warriorBlackRect3.colliderect(warriorWhiteRect):
                    figuresWhite[9] = ""
                    warriorWhiteRect.centerx = -120
                    warriorWhiteRect.centery = -120
                if warriorBlackRect3.colliderect(legionaryWhiteRect1):
                    figuresWhite[10] = ""
                    legionaryWhiteRect1.centerx = -120
                    legionaryWhiteRect1.centery = -120
                if warriorBlackRect3.colliderect(warriorWhiteRect1):
                    figuresWhite[11] = ""
                    warriorWhiteRect1.centerx = -120
                    warriorWhiteRect1.centery = -120
                if warriorBlackRect3.colliderect(legionaryWhiteRect2):
                    figuresWhite[12] = ""
                    legionaryWhiteRect2.centerx = -120
                    legionaryWhiteRect2.centery = -120
                if warriorBlackRect3.colliderect(warriorWhiteRect2):
                    figuresWhite[13] = ""
                    warriorWhiteRect2.centerx = -120
                    warriorWhiteRect2.centery = -120
                if warriorBlackRect3.colliderect(legionaryWhiteRect3):
                    figuresWhite[14] = ""
                    legionaryWhiteRect3.centerx = -120
                    legionaryWhiteRect3.centery = -120
                if warriorBlackRect3.colliderect(warriorWhiteRect3):
                    figuresWhite[15] = ""
                    warriorWhiteRect3.centerx = -120
                    warriorWhiteRect3.centery = -120

    pygame.display.update()

    clock.tick(60)

pygame.quit()