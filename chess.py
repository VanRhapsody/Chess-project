import pygame
import mysql.connector
import random

pygame.init()

# Nastavení připojení k databázi
db_connection = mysql.connector.connect(
    host="dbs.spskladno.cz",
    user="student3",
    password="spsnet",
    database="vyuka3"
)

cursor = db_connection.cursor()

cursor.execute("SELECT DISTINCT(email),win_count FROM registracechess ORDER BY win_count DESC LIMIT 15")
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
plagueWhitexInit=plagueDoctorWhiteRect.centerx
plagueWhiteyInit=plagueDoctorWhiteRect.centery
archbishopWhiteRect = archbishopWhite.get_rect()
archbishopWhiteRect.center = (660, 120)
archbishopWhitexInit=archbishopWhiteRect.centerx
archbishopWhiteyInit=archbishopWhiteRect.centery
cardinalWhiteRect = cardinalWhite.get_rect()
cardinalWhiteRect.center = (780, 120)
cardinalWhitexInit=cardinalWhiteRect.centerx
cardinalWhiteyInit=cardinalWhiteRect.centery
hadesWhiteRect = hadesWhite.get_rect()
hadesWhiteRect.center = (900, 120)
hadesWhitexInit=hadesWhiteRect.centerx
hadesWhiteyInit=hadesWhiteRect.centery
persephoneWhiteRect = persephoneWhite.get_rect()
persephoneWhiteRect.center = (1020, 120)
persephoneWhitexInit=persephoneWhiteRect.centerx
persephoneWhiteyInit=persephoneWhiteRect.centery
cardinalWhiteRect1 = cardinalWhite.get_rect()
cardinalWhiteRect1.center = (1140, 120)
cardinalWhitexInit1=cardinalWhiteRect1.centerx
cardinalWhiteyInit1=cardinalWhiteRect1.centery
archbishopWhiteRect1 = archbishopWhite.get_rect()
archbishopWhiteRect1.center = (1260, 120)
archbishopWhitexInit1=archbishopWhiteRect1.centerx
archbishopWhiteyInit1=archbishopWhiteRect1.centery
plagueDoctorWhiteRect1 = plagueDoctorWhite.get_rect()
plagueDoctorWhiteRect1.center = (1380, 120)
plagueWhitexInit1=plagueDoctorWhiteRect1.centerx
plagueWhiteyInit1=plagueDoctorWhiteRect1.centery
warriorWhiteRect = warriorWhite.get_rect()
warriorWhiteRect.center = (540, 240)
warriorWhitexInit=warriorWhiteRect.centerx
warriorWhiteyInit=warriorWhiteRect.centery
legionaryWhiteRect = legionaryWhite.get_rect()
legionaryWhiteRect.center = (660, 240)
legionaryWhitexInit=legionaryWhiteRect.centerx
legionaryWhiteyInit=legionaryWhiteRect.centery
warriorWhiteRect1 = warriorWhite.get_rect()
warriorWhiteRect1.center = (780, 240)
warriorWhitexInit1=warriorWhiteRect1.centerx
warriorWhiteyInit1=warriorWhiteRect1.centery
legionaryWhiteRect1 = legionaryWhite.get_rect()
legionaryWhiteRect1.center = (900, 240)
legionaryWhitexInit1=legionaryWhiteRect1.centerx
legionaryWhiteyInit1=legionaryWhiteRect1.centery
warriorWhiteRect2 = warriorWhite.get_rect()
warriorWhiteRect2.center = (1020, 240)
warriorWhitexInit2=warriorWhiteRect2.centerx
warriorWhiteyInit2=warriorWhiteRect2.centery
legionaryWhiteRect2 = legionaryWhite.get_rect()
legionaryWhiteRect2.center = (1140, 240)
legionaryWhitexInit2=legionaryWhiteRect2.centerx
legionaryWhiteyInit2=legionaryWhiteRect2.centery
warriorWhiteRect3 = warriorWhite.get_rect()
warriorWhiteRect3.center = (1260, 240)
warriorWhitexInit3=warriorWhiteRect3.centerx
warriorWhiteyInit3=warriorWhiteRect3.centery
legionaryWhiteRect3 = legionaryWhite.get_rect()
legionaryWhiteRect3.center = (1380, 240)
legionaryWhitexInit3=legionaryWhiteRect3.centerx
legionaryWhiteyInit3=legionaryWhiteRect3.centery

# Nastavení pozic černých figurek
plagueDoctorBlackRect = plagueDoctorBlack.get_rect()
plagueDoctorBlackRect.center = (540, 960)
plagueBlackxInit=plagueDoctorBlackRect.centerx
plagueBlackyInit=plagueDoctorBlackRect.centery
archbishopBlackRect = archbishopBlack.get_rect()
archbishopBlackRect.center = (660, 960)
archbishopBlackxInit=archbishopBlackRect.centerx
archbishopBlackyInit=archbishopBlackRect.centery
cardinalBlackRect = cardinalBlack.get_rect()
cardinalBlackRect.center = (780, 960)
cardinalBlackxInit=cardinalBlackRect.centerx
cardinalBlackyInit=cardinalBlackRect.centery
hadesBlackRect = hadesBlack.get_rect()
hadesBlackRect.center = (900, 960)
hadesBlackxInit=hadesBlackRect.centerx
hadesBlackyInit=hadesBlackRect.centery
persephoneBlackRect = persephoneBlack.get_rect()
persephoneBlackRect.center = (1020, 960)
persephoneBlackxInit=persephoneBlackRect.centerx
persephoneBlackyInit=persephoneBlackRect.centery
cardinalBlackRect1 = cardinalBlack.get_rect()
cardinalBlackRect1.center = (1140, 960)
cardinalBlackxInit=cardinalBlackRect1.centerx
cardinalBlackyInit1=cardinalBlackRect1.centery
archbishopBlackRect1 = archbishopBlack.get_rect()
archbishopBlackRect1.center = (1260, 960)
archbishopBlackxInit1=archbishopBlackRect1.centerx
archbishopBlackyInit1=archbishopBlackRect1.centery
plagueDoctorBlackRect1 = plagueDoctorBlack.get_rect()
plagueDoctorBlackRect1.center = (1380, 960)
plagueBlackxInit1=plagueDoctorBlackRect1.centerx
plagueBlackyInit1=plagueDoctorBlackRect1.centery
legionaryBlackRect = legionaryBlack.get_rect()
legionaryBlackRect.center = (540, 840)
legionaryBlackxInit=legionaryBlackRect.centerx
legionaryBlackyInit=legionaryBlackRect.centery
warriorBlackRect = warriorBlack.get_rect()
warriorBlackRect.center = (660, 840)
warriorBlackxInit=warriorBlackRect.centerx
warriorBlackyInit=warriorBlackRect.centery
legionaryBlackRect1 = legionaryBlack.get_rect()
legionaryBlackRect1.center = (780, 840)
legionaryBlackxInit1=legionaryBlackRect1.centerx
legionaryBlackyInit1=legionaryBlackRect1.centery
warriorBlackRect1 = warriorBlack.get_rect()
warriorBlackRect1.center = (900, 840)
warriorBlackxInit1=warriorBlackRect1.centerx
warriorBlackyInit1=warriorBlackRect1.centery
legionaryBlackRect2 = legionaryBlack.get_rect()
legionaryBlackRect2.center = (1020, 840)
legionaryBlackxInit2=legionaryBlackRect2.centerx
legionaryBlackyInit2=legionaryBlackRect2.centery
warriorBlackRect2 = warriorBlack.get_rect()
warriorBlackRect2.center = (1140, 840)
warriorBlackxInit2=warriorBlackRect2.centerx
warriorBlackyInit2=warriorBlackRect2.centery
legionaryBlackRect3 = legionaryBlack.get_rect()
legionaryBlackRect3.center = (1260, 840)
legionaryBlackxInit3=legionaryBlackRect3.centerx
legionaryBlackyInit3=legionaryBlackRect3.centery
warriorBlackRect3 = warriorBlack.get_rect()
warriorBlackRect3.center = (1380, 840)
warriorBlackxInit3=warriorBlackRect3.centerx
warriorBlackyInit3=warriorBlackRect3.centery

# Deklarace barev
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
active_color = (255, 255, 255)
passive_collor = (180, 180, 180)
# Nastavení pozadí
background_image = pygame.image.load("images/loginpozadi.jpg")
background_image_rect = background_image.get_rect()
background_image_rect.center = (screen_width / 2, screen_height / 2)

# Hudba v pozadí
songs = ["music/Anguish.mp3", "music/Bleach OST 3-Clavar La Espada.mp3", "music/y2mate.com - Kyrie Ⅱ.mp3", "music/Nube Negra.mp3",
         "music/y2mate.com - American Prometheus.mp3","music/y2mate.com - オールフォーワンの力.mp3"]
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
leadeboard_text_font = pygame.font.SysFont("georgia", 30, False)
leaderboard_text = leaderboard_font.render("Leaderboard", True, white)
leaderboard_text_rect = leaderboard_text.get_rect()
leaderboard_text_rect.center = (1650, 60)
leaderboard_background = pygame.Rect(1400, 10, 500, 1050)

#Text pro nápovědu pro abilitu
ability_font=pygame.font.SysFont("georgia",40,False)
ability_text=ability_font.render("F9 - aktivovat abilitu",True, white)
ability_text_rect=ability_text.get_rect()
ability_text_rect.topright=(1380,10)

#Text pro označení uživatelů
user_1_text=leadeboard_text_font.render("Hráč 1", True, white)
user_1_text_rect=user_1_text.get_rect()
user_1_text_rect.topleft=(480,10)

user_2_text=leadeboard_text_font.render("Hráč 2", True, white)
user_2_text_rect=user_2_text.get_rect()
user_2_text_rect.bottomleft=(480,1070)

# Zvuk zahájení hry
start_game = pygame.mixer.Sound("sounds/Sound effect bell.mp3")

#Zvuk ability kardinála
cardinalAbilitySound=pygame.mixer.Sound("sounds/bankai1.mp3")

#Zvuk late game
lateGameMusic=pygame.mixer.Sound("music/y2mate.com - Bleach OST  Invasion.mp3")

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

# Získání pozic pro abilitu legionáře pro její funčknost v prvotní fázi hry
step=120

rectLegionaryWhitexAbility=legionaryWhiteRect.centerx
rectLegionaryWhiteyAbility=legionaryWhiteRect.centery

rectLegionaryWhitexAbility_1=legionaryWhiteRect1.centerx
rectLegionaryWhiteyAbility_1=legionaryWhiteRect1.centery

rectLegionaryWhitexAbility_2=legionaryWhiteRect2.centerx
rectLegionaryWhiteyAbility_2=legionaryWhiteRect2.centery

rectLegionaryWhitexAbility_3=legionaryWhiteRect3.centerx
rectLegionaryWhiteyAbility_3=legionaryWhiteRect3.centery

rectLegionaryBlackxAbility=legionaryBlackRect.centerx
rectLegionaryBlackyAbility=legionaryBlackRect.centery

rectLegionaryBlackxAbility_1=legionaryBlackRect1.centerx
rectLegionaryBlackyAbility_1=legionaryBlackRect1.centery

rectLegionaryBlackxAbility_2=legionaryBlackRect2.centerx
rectLegionaryBlackxAbility_2=legionaryBlackRect2.centery

rectLegionaryBlackxAbility_3=legionaryBlackRect3.centerx
rectLegionaryBlackyAbility_3=legionaryBlackRect3.centery

# Nastavení counteru, který určuje, jaká barva je na tahu
counter = 0

#Nastavení counteru a bool proměnných pro abilitu morového doktora
rectPlagueDoctorWhiteAbilityCounter=1
rectPlagueDoctorWhiteAbilityActivated=False
rectPlagueDoctorWhiteAbilityCounter_1=1
rectPlagueDoctorWhiteAbilityActivated_1=False
rectPlagueDoctorBlackAbilityCounter=1
rectPlagueDoctorBlackAbilityActivated=False
rectPlagueDoctorBlackAbilityCounter_1=1
rectPlagueDoctorBlackAbilityActivated_1=False

#Nastavení counteru pro arcibiskupa pro možnost zaznamenání získaných figurek
archbishopWhiteFiguresCount=0
archbishopWhiteAbilityCounter=1
archbishopWhiteAbilityActivated=False
archbishopWhiteFiguresCount_1=0
archbishopWhiteAbilityCounter_1=1
archbishopWhiteAbilityActivated_1=False
archbishopBlackFiguresCount=0
archbishopBlackAbilityCounter=1
archbishopBlackAbilityActivated=False
archbishopBlackFiguresCount_1=0
archbishopBlackAbilityCounter_1=1
archbishopBlackAbilityActivated_1=False

#Nastavení counetru a bool proměnných pro abilitu kardinála
cardinalWhiteAbilityCounter=1
cardinalWhiteAbilityActivated=False
cardinalWhiteAbilityCounter_1=1
cardinalWhiteAbilityActivated_1=False
cardinalBlackAbilityCounter=1
cardinalBlackAbilityActivated=False
cardinalBlackAbilityCounter_1=1
cardinalBlackAbilityActivated_1=False

#Nastavení counteru a bool proměnných pro abilitu Hádese
hadesWhiteAbilityActivated=False
hadesWhiteAbilityCounter=2

hadesBlackAbilityActivated=False
hadesBlackAbilityCounter=2

#Nastavení nových figurek pro kardinála při použití jeho ability
cardinalWhiteRectCopy=cardinalWhite.get_rect()
cardinalWhiteRectCopy.centerx=-500
cardinalWhiteRectCopy.centery=-500

cardinalWhiteRectCopy_1=cardinalWhite.get_rect()
cardinalWhiteRectCopy_1.centerx=-1000
cardinalWhiteRectCopy_1.centery=-1000

cardinalBlackRectCopy=cardinalBlack.get_rect()
cardinalBlackRectCopy.centerx=3000
cardinalBlackRectCopy.centery=3000

cardinalBlackRectCopy_1=cardinalBlack.get_rect()
cardinalBlackRectCopy_1.centerx=3500
cardinalBlackRectCopy_1.centery=3500

#Nastavení bool proměnných a counterů pro abilitu Persefony
persephoneWhiteAbilityActivated=False
persephoneWhiteAbilityCounter=2

persephoneBlackAbilityActivated=False
persephoneBlackAbilityCounter=2


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
late_game=False
user1_logged_in=False
user2_logged_in=False
user1_win=False
user2_win=False

#Nastavení emailů uživatelů pro funkčnost programu v prvotní fázi
user_email_1=""
user_email_2=""

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
cardinalWhitePlayingCopy=False
cardinalWhitePlayingCopy1=False
figuresWhitePlaying=[plagueDoctorWhitePlaying,archbishopWhitePlaying,cardinalWhitePlaying,hadesWhitePlaying,persephoneWhitePlaying,cardinalWhitePlaying1,archbishopWhitePlaying1,plagueDoctorWhitePlaying1,legionaryWhitePlaying,warriorWhitePlaying,legionaryWhitePlaying1,warriorWhitePlaying1,legionaryWhitePlaying2,warriorWhitePlaying2,legionaryWhitePlaying3,warriorWhitePlaying3,cardinalWhitePlayingCopy,cardinalWhitePlayingCopy1]

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
cardinalBlackPlayingCopy=False
cardinalBlackPlayingCopy1=False
figuresBlackPlaying=[plagueDoctorBlackPlaying,archbishopBlackPlaying,cardinalBlackPlaying,hadesBlackPlaying,persephoneBlackPlaying,cardinalBlackPlaying1,archbishopBlackPlaying1,plagueDoctorBlackPlaying1,legionaryBlackPlaying,warriorBlackPlaying,legionaryBlackPlaying1,warriorBlackPlaying1,legionaryBlackPlaying2,warriorBlackPlaying2,legionaryBlackPlaying3,warriorBlackPlaying3,cardinalBlackPlayingCopy,cardinalBlackPlayingCopy1]

figuresWhite = [plagueDoctorWhiteRect, archbishopWhiteRect, cardinalWhiteRect, hadesWhiteRect, persephoneWhiteRect,
                cardinalWhiteRect1, archbishopWhiteRect1, plagueDoctorWhiteRect1, legionaryWhiteRect,
                warriorWhiteRect, legionaryWhiteRect1, warriorWhiteRect1, legionaryWhiteRect2, warriorWhiteRect2,
                legionaryWhiteRect3, warriorWhiteRect3,cardinalWhiteRectCopy,cardinalWhiteRectCopy_1]
figuresBlack = [plagueDoctorBlackRect, archbishopBlackRect, cardinalBlackRect, hadesBlackRect,
                persephoneBlackRect, cardinalBlackRect1, archbishopBlackRect1, plagueDoctorBlackRect1,
                legionaryBlackRect, warriorBlackRect, legionaryBlackRect1, warriorBlackRect1,
                legionaryBlackRect2, warriorBlackRect2, legionaryBlackRect3, warriorBlackRect3,cardinalWhiteRectCopy,cardinalWhiteRectCopy_1]

while run:
    mx, my = pygame.mouse.get_pos()

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if user1_logged_in:
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

                            user_email_2 = input_user_text1
                            input_user_text1 = ''
                            input_user_text2 = ''
                            user2_logged_in=True
                            inputUserText2Hidden = ''
                            #Text pro označení uživatelů s přidaným emailem
                            user_2_text=leadeboard_text_font.render(f"Hráč 2 {user_email_2}", True, white)
                            user_2_text_rect=user_2_text.get_rect()
                            user_2_text_rect.bottomleft=(480,1070)

                        else:
                            screen.blit(failed_header, failed_header_rect)
                            inputUserText2Hidden = ''
                            input_user_text1 = ''
                else:
                    active2 = False
                screen.blit(login_header, login_header_rect)
            else:
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

                            user_email_1 = input_user_text1
                            input_user_text1 = ''
                            input_user_text2 = ''
                            inputUserText2Hidden = ''
                            user1_logged_in=True
                            #Text pro označení uživatelů s přidaným emailem
                            user_1_text=leadeboard_text_font.render(f"Hráč 1 {user_email_1}", True, white)
                            user_1_text_rect=user_1_text.get_rect()
                            user_1_text_rect.topleft=(480,10)
                        else:
                            screen.blit(failed_header, failed_header_rect)
                            inputUserText2Hidden = ''
                            input_user_text1 = ''
                else:
                    active2 = False
                screen.blit(login_header, login_header_rect)
            print(user_email_1,user_email_2)




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
            screen.blit(text_surface, (1400, y))
            y += 70

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
        if user1_logged_in:
            login_header = header_font.render("Přihlášení druhého uživatele", True, white)
            login_header_rect = pass_header.get_rect()
            login_header_rect.midleft = (100, 160)
        if user1_logged_in and user2_logged_in:
            login_header = header_font.render("", True, white)
            login_header_rect = pass_header.get_rect()
            login_header_rect.midleft = (100, 160)
        if not user1_logged_in:
            login_header = header_font.render("Přihlášení prvního uživatele", True, white)
            login_header_rect = pass_header.get_rect()
            login_header_rect.midleft = (100, 160)
        screen.blit(login_header,login_header_rect)

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
        screen.blit(user_1_text,user_1_text_rect)
        screen.blit(user_2_text,user_2_text_rect)
        # Zastavení hudby v pozadí a nastavení header textu na prázdný, protože během hry problikával
        login_header = header_font.render("", True, white)
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
        #if warriorWhiteRect in figuresWhite:
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
        screen.blit(cardinalWhite,cardinalWhiteRectCopy)
        screen.blit(cardinalWhite,cardinalWhiteRectCopy_1)

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
        screen.blit(cardinalBlack,cardinalBlackRectCopy)
        screen.blit(cardinalBlack,cardinalBlackRectCopy_1)

        if counter % 2 != 0:
            if plagueDoctorWhiteRect.colliderect(plagueDoctorBlackRect):
                plagueDoctorBlackRect.centerx = screen_width-step
                plagueDoctorBlackRect.centery = step
            if plagueDoctorWhiteRect.colliderect(archbishopBlackRect):
                archbishopBlackRect.centerx = screen_width-step*2
                archbishopBlackRect.centery = step
            if plagueDoctorWhiteRect.colliderect(cardinalBlackRect):
                cardinalBlackRect.centerx = screen_width-step*3
                cardinalBlackRect.centery = step
            if plagueDoctorWhiteRect.colliderect(hadesBlackRect):
                hadesBlackRect.centerx = screen_width-step
                hadesBlackRect.centery = step*2
                lateGameMusic.play()
                late_game=True
            if plagueDoctorWhiteRect.colliderect(persephoneBlackRect):
                persephoneBlackRect.centerx = screen_width-step*2
                persephoneBlackRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user1_win=True
            if plagueDoctorWhiteRect.colliderect(cardinalBlackRect1):
                cardinalBlackRect1.centerx = screen_width-step*3
                cardinalBlackRect1.centery = step*2
            if plagueDoctorWhiteRect.colliderect(archbishopBlackRect1):
                archbishopBlackRect1.centerx = screen_width-step
                archbishopBlackRect1.centery = step*3
            if plagueDoctorWhiteRect.colliderect(plagueDoctorBlackRect1):
                plagueDoctorBlackRect1.centerx = screen_width-step*2
                plagueDoctorBlackRect1.centery = step*3
            if plagueDoctorWhiteRect.colliderect(legionaryBlackRect):
                legionaryBlackRect.centerx = screen_width-step*3
                legionaryBlackRect.centery = step*3
            if plagueDoctorWhiteRect.colliderect(warriorBlackRect):
                warriorBlackRect.centerx = screen_width-step
                warriorBlackRect.centery = step*4
            if plagueDoctorWhiteRect.colliderect(legionaryBlackRect1):
                legionaryBlackRect1.centerx = screen_width-step*2
                legionaryBlackRect1.centery = step*4
            if plagueDoctorWhiteRect.colliderect(warriorBlackRect1):
                warriorBlackRect1.centerx = screen_width-step*3
                warriorBlackRect1.centery = step*4
            if plagueDoctorWhiteRect.colliderect(legionaryBlackRect2):
                legionaryBlackRect2.centerx = screen_width-step
                legionaryBlackRect2.centery = step*5
            if plagueDoctorWhiteRect.colliderect(warriorBlackRect2):
                warriorBlackRect2.centerx = screen_width-step*2
                warriorBlackRect2.centery = step*5
            if plagueDoctorWhiteRect.colliderect(legionaryBlackRect3):
                legionaryBlackRect3.centerx = screen_width-step*3
                legionaryBlackRect3.centery = step*5
            if plagueDoctorWhiteRect.colliderect(warriorBlackRect3):
                warriorBlackRect3.centerx = screen_width-step
                warriorBlackRect3.centery = step*6
            if plagueDoctorWhiteRect.colliderect(cardinalBlackRectCopy):
                cardinalBlackRectCopy.centerx=screen_width-step*2
                cardinalBlackRectCopy.centery=step*6
            if plagueDoctorWhiteRect.colliderect(cardinalBlackRectCopy_1):
                cardinalBlackRectCopy_1.centerx=screen_width-step*3
                cardinalBlackRectCopy_1.centery=step*6

            if archbishopWhiteRect.colliderect(plagueDoctorBlackRect):
                plagueDoctorBlackRect.centerx = screen_width-step
                plagueDoctorBlackRect.centery = step
                archbishopWhiteFiguresCount+=1
            if archbishopWhiteRect.colliderect(archbishopBlackRect):
                archbishopBlackRect.centerx = screen_width-step*2
                archbishopBlackRect.centery = step
                archbishopWhiteFiguresCount+=1
            if archbishopWhiteRect.colliderect(cardinalBlackRect):
                cardinalBlackRect.centerx = screen_width-step*3
                cardinalBlackRect.centery = step
                archbishopWhiteFiguresCount+=1
            if archbishopWhiteRect.colliderect(hadesBlackRect):
                hadesBlackRect.centerx = screen_width-step
                hadesBlackRect.centery = step*2
                archbishopWhiteFiguresCount+=1
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if archbishopWhiteRect.colliderect(persephoneBlackRect):
                persephoneBlackRect.centerx = screen_width-step*2
                persephoneBlackRect.centery = step*2
                archbishopWhiteFiguresCount+=1
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user1_win=True
            if archbishopWhiteRect.colliderect(cardinalBlackRect1):
                cardinalBlackRect1.centerx = screen_width-step*3
                cardinalBlackRect1.centery = step*2
                archbishopWhiteFiguresCount+=1
            if archbishopWhiteRect.colliderect(archbishopBlackRect1):
                archbishopBlackRect1.centerx = screen_width-step
                archbishopBlackRect1.centery = step*3
                archbishopWhiteFiguresCount+=1
            if archbishopWhiteRect.colliderect(plagueDoctorBlackRect1):
                plagueDoctorBlackRect1.centerx = screen_width-step*2
                plagueDoctorBlackRect1.centery = step*3
                archbishopWhiteFiguresCount+=1
            if archbishopWhiteRect.colliderect(legionaryBlackRect):
                legionaryBlackRect.centerx = screen_width-step*3
                legionaryBlackRect.centery = step*3
                archbishopWhiteFiguresCount+=1
            if archbishopWhiteRect.colliderect(warriorBlackRect):
                warriorBlackRect.centerx = screen_width-step
                warriorBlackRect.centery = step*4
                archbishopWhiteFiguresCount+=1
            if archbishopWhiteRect.colliderect(legionaryBlackRect1):
                legionaryBlackRect1.centerx = screen_width-step*2
                legionaryBlackRect1.centery = step*4
                archbishopWhiteFiguresCount+=1
            if archbishopWhiteRect.colliderect(warriorBlackRect1):
                warriorBlackRect1.centerx = screen_width-step*3
                warriorBlackRect1.centery = step*4
                archbishopWhiteFiguresCount+=1
            if archbishopWhiteRect.colliderect(legionaryBlackRect2):
                legionaryBlackRect2.centerx = screen_width-step
                legionaryBlackRect2.centery = step*5
                archbishopWhiteFiguresCount+=1
            if archbishopWhiteRect.colliderect(warriorBlackRect2):
                warriorBlackRect2.centerx = screen_width-step*2
                warriorBlackRect2.centery = step*5
                archbishopWhiteFiguresCount+=1
            if archbishopWhiteRect.colliderect(legionaryBlackRect3):
                legionaryBlackRect3.centerx = screen_width-step*3
                legionaryBlackRect3.centery = step*5
                archbishopWhiteFiguresCount+=1
            if archbishopWhiteRect.colliderect(warriorBlackRect3):
                warriorBlackRect3.centerx = screen_width-step
                warriorBlackRect3.centery = step*6
                archbishopWhiteFiguresCount+=1
            if archbishopWhiteRect.colliderect(cardinalBlackRectCopy):
                cardinalBlackRectCopy.centerx=screen_width-step*2
                cardinalBlackRectCopy.centery=step*6
                archbishopWhiteFiguresCount+=1
            if archbishopWhiteRect.colliderect(cardinalBlackRectCopy_1):
                cardinalBlackRectCopy_1.centerx=screen_width-step*3
                cardinalBlackRectCopy_1.centery=step*6
                archbishopWhiteFiguresCount+=1

            if cardinalWhiteRect.colliderect(plagueDoctorBlackRect):
                plagueDoctorBlackRect.centerx = screen_width-step
                plagueDoctorBlackRect.centery = step
            if cardinalWhiteRect.colliderect(archbishopBlackRect):
                archbishopBlackRect.centerx = screen_width-step*2
                archbishopBlackRect.centery = step
            if cardinalWhiteRect.colliderect(cardinalBlackRect):
                cardinalBlackRect.centerx = screen_width-step*3
                cardinalBlackRect.centery = step
            if cardinalWhiteRect.colliderect(hadesBlackRect):
                hadesBlackRect.centerx = screen_width-step
                hadesBlackRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if cardinalWhiteRect.colliderect(persephoneBlackRect):
                persephoneBlackRect.centerx = screen_width-step*2
                persephoneBlackRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user1_win=True
            if cardinalWhiteRect.colliderect(cardinalBlackRect1):
                cardinalBlackRect1.centerx = screen_width-step*3
                cardinalBlackRect1.centery = step*2
            if cardinalWhiteRect.colliderect(archbishopBlackRect1):
                archbishopBlackRect1.centerx = screen_width-step
                archbishopBlackRect1.centery = step*3
            if cardinalWhiteRect.colliderect(plagueDoctorBlackRect1):
                plagueDoctorBlackRect1.centerx = screen_width-step*2
                plagueDoctorBlackRect1.centery = step*3
            if cardinalWhiteRect.colliderect(legionaryBlackRect):
                legionaryBlackRect.centerx = screen_width-step*3
                legionaryBlackRect.centery = step*3
            if cardinalWhiteRect.colliderect(warriorBlackRect):
                warriorBlackRect.centerx = screen_width-step
                warriorBlackRect.centery = step*4
            if cardinalWhiteRect.colliderect(legionaryBlackRect1):
                legionaryBlackRect1.centerx = screen_width-step*2
                legionaryBlackRect1.centery = step*4
            if cardinalWhiteRect.colliderect(warriorBlackRect1):
                warriorBlackRect1.centerx = screen_width-step*3
                warriorBlackRect1.centery = step*4
            if cardinalWhiteRect.colliderect(legionaryBlackRect2):
                legionaryBlackRect2.centerx = screen_width-step
                legionaryBlackRect2.centery = step*5
            if cardinalWhiteRect.colliderect(warriorBlackRect2):
                warriorBlackRect2.centerx = screen_width-step*2
                warriorBlackRect2.centery = step*5
            if cardinalWhiteRect.colliderect(legionaryBlackRect3):
                legionaryBlackRect3.centerx = screen_width-step*3
                legionaryBlackRect3.centery = step*5
            if cardinalWhiteRect.colliderect(warriorBlackRect3):
                warriorBlackRect3.centerx = screen_width-step
                warriorBlackRect3.centery = step*6
            if cardinalWhiteRect.colliderect(cardinalBlackRectCopy):
                cardinalBlackRectCopy.centerx=screen_width-step*2
                cardinalBlackRectCopy.centery=step*6
            if cardinalWhiteRect.colliderect(cardinalBlackRectCopy_1):
                cardinalBlackRectCopy_1.centerx=screen_width-step*3
                cardinalBlackRectCopy_1.centery=step*6


            if hadesWhiteRect.colliderect(plagueDoctorBlackRect):
                plagueDoctorBlackRect.centerx = screen_width-step
                plagueDoctorBlackRect.centery = step
            if hadesWhiteRect.colliderect(archbishopBlackRect):
                archbishopBlackRect.centerx = screen_width-step*2
                archbishopBlackRect.centery = step
            if hadesWhiteRect.colliderect(cardinalBlackRect):
                cardinalBlackRect.centerx = screen_width-step*3
                cardinalBlackRect.centery = step
            if hadesWhiteRect.colliderect(hadesBlackRect):
                hadesBlackRect.centerx = screen_width-step
                hadesBlackRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if hadesWhiteRect.colliderect(persephoneBlackRect):
                persephoneBlackRect.centerx = screen_width-step*2
                persephoneBlackRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user1_win=True
            if hadesWhiteRect.colliderect(cardinalBlackRect1):
                cardinalBlackRect1.centerx = screen_width-step*3
                cardinalBlackRect1.centery = step*2
            if hadesWhiteRect.colliderect(archbishopBlackRect1):
                archbishopBlackRect1.centerx = screen_width-step
                archbishopBlackRect1.centery = step*3
            if hadesWhiteRect.colliderect(plagueDoctorBlackRect1):
                plagueDoctorBlackRect1.centerx = screen_width-step*2
                plagueDoctorBlackRect1.centery = step*3
            if hadesWhiteRect.colliderect(legionaryBlackRect):
                legionaryBlackRect.centerx = screen_width-step*3
                legionaryBlackRect.centery = step*3
            if hadesWhiteRect.colliderect(warriorBlackRect):
                warriorBlackRect.centerx = screen_width-step
                warriorBlackRect.centery = step*4
            if hadesWhiteRect.colliderect(legionaryBlackRect1):
                legionaryBlackRect1.centerx = screen_width-step*2
                legionaryBlackRect1.centery = step*4
            if hadesWhiteRect.colliderect(warriorBlackRect1):
                warriorBlackRect1.centerx = screen_width-step*3
                warriorBlackRect1.centery = step*4
            if hadesWhiteRect.colliderect(legionaryBlackRect2):
                legionaryBlackRect2.centerx = screen_width-step
                legionaryBlackRect2.centery = step*5
            if hadesWhiteRect.colliderect(warriorBlackRect2):
                warriorBlackRect2.centerx = screen_width-step*2
                warriorBlackRect2.centery = step*5
            if hadesWhiteRect.colliderect(legionaryBlackRect3):
                legionaryBlackRect3.centerx = screen_width-step*3
                legionaryBlackRect3.centery = step*5
            if hadesWhiteRect.colliderect(warriorBlackRect3):
                warriorBlackRect3.centerx = screen_width-step
                warriorBlackRect3.centery = step*6
            if hadesWhiteRect.colliderect(cardinalBlackRectCopy):
                cardinalBlackRectCopy.centerx=screen_width-step*2
                cardinalBlackRectCopy.centery=step*6
            if hadesWhiteRect.colliderect(cardinalBlackRectCopy_1):
                cardinalBlackRectCopy_1.centerx=screen_width-step*3
                cardinalBlackRectCopy_1.centery=step*6


            if persephoneWhiteRect.colliderect(plagueDoctorBlackRect):
                plagueDoctorBlackRect.centerx = screen_width-step
                plagueDoctorBlackRect.centery = step
            if persephoneWhiteRect.colliderect(archbishopBlackRect):
                archbishopBlackRect.centerx = screen_width-step*2
                archbishopBlackRect.centery = step
            if persephoneWhiteRect.colliderect(cardinalBlackRect):
                cardinalBlackRect.centerx = screen_width-step*3
                cardinalBlackRect.centery = step
            if persephoneWhiteRect.colliderect(hadesBlackRect):
                hadesBlackRect.centerx = screen_width-step
                hadesBlackRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if persephoneWhiteRect.colliderect(persephoneBlackRect):
                persephoneBlackRect.centerx = screen_width-step*2
                persephoneBlackRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user1_win=True
            if persephoneWhiteRect.colliderect(cardinalBlackRect1):
                cardinalBlackRect1.centerx = screen_width-step*3
                cardinalBlackRect1.centery = step*2
            if persephoneWhiteRect.colliderect(archbishopBlackRect1):
                archbishopBlackRect1.centerx = screen_width-step
                archbishopBlackRect1.centery = step*3
            if persephoneWhiteRect.colliderect(plagueDoctorBlackRect1):
                plagueDoctorBlackRect1.centerx = screen_width-step*2
                plagueDoctorBlackRect1.centery = step*3
            if persephoneWhiteRect.colliderect(legionaryBlackRect):
                legionaryBlackRect.centerx = screen_width-step*3
                legionaryBlackRect.centery = step*3
            if persephoneWhiteRect.colliderect(warriorBlackRect):
                warriorBlackRect.centerx = screen_width-step
                warriorBlackRect.centery = step*4
            if persephoneWhiteRect.colliderect(legionaryBlackRect1):
                legionaryBlackRect1.centerx = screen_width-step*2
                legionaryBlackRect1.centery = step*4
            if persephoneWhiteRect.colliderect(warriorBlackRect1):
                warriorBlackRect1.centerx = screen_width-step*3
                warriorBlackRect1.centery = step*4
            if persephoneWhiteRect.colliderect(legionaryBlackRect2):
                legionaryBlackRect2.centerx = screen_width-step
                legionaryBlackRect2.centery = step*5
            if persephoneWhiteRect.colliderect(warriorBlackRect2):
                warriorBlackRect2.centerx = screen_width-step*2
                warriorBlackRect2.centery = step*5
            if persephoneWhiteRect.colliderect(legionaryBlackRect3):
                legionaryBlackRect3.centerx = screen_width-step*3
                legionaryBlackRect3.centery = step*5
            if persephoneWhiteRect.colliderect(warriorBlackRect3):
                warriorBlackRect3.centerx = screen_width-step
                warriorBlackRect3.centery = step*6
            if persephoneWhiteRect.colliderect(cardinalBlackRectCopy):
                cardinalBlackRectCopy.centerx=screen_width-step*2
                cardinalBlackRectCopy.centery=step*6
            if persephoneWhiteRect.colliderect(cardinalBlackRectCopy_1):
                cardinalBlackRectCopy_1.centerx=screen_width-step*3
                cardinalBlackRectCopy_1.centery=step*6

            if cardinalWhiteRect1.colliderect(plagueDoctorBlackRect):
                plagueDoctorBlackRect.centerx = screen_width-step
                plagueDoctorBlackRect.centery = step
            if cardinalWhiteRect1.colliderect(archbishopBlackRect):
                archbishopBlackRect.centerx = screen_width-step*2
                archbishopBlackRect.centery = step
            if cardinalWhiteRect1.colliderect(cardinalBlackRect):
                cardinalBlackRect.centerx = screen_width-step*3
                cardinalBlackRect.centery = step
            if cardinalWhiteRect1.colliderect(hadesBlackRect):
                hadesBlackRect.centerx = screen_width-step
                hadesBlackRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if cardinalWhiteRect1.colliderect(persephoneBlackRect):
                persephoneBlackRect.centerx = screen_width-step*2
                persephoneBlackRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user1_win=True
            if cardinalWhiteRect1.colliderect(cardinalBlackRect1):
                cardinalBlackRect1.centerx = screen_width-step*3
                cardinalBlackRect1.centery = step*2
            if cardinalWhiteRect1.colliderect(archbishopBlackRect1):
                archbishopBlackRect1.centerx = screen_width-step
                archbishopBlackRect1.centery = step*3
            if cardinalWhiteRect1.colliderect(plagueDoctorBlackRect1):
                plagueDoctorBlackRect1.centerx = screen_width-step*2
                plagueDoctorBlackRect1.centery = step*3
            if cardinalWhiteRect1.colliderect(legionaryBlackRect):
                legionaryBlackRect.centerx = screen_width-step*3
                legionaryBlackRect.centery = step*3
            if cardinalWhiteRect1.colliderect(warriorBlackRect):
                warriorBlackRect.centerx = screen_width-step
                warriorBlackRect.centery = step*4
            if cardinalWhiteRect1.colliderect(legionaryBlackRect1):
                legionaryBlackRect1.centerx = screen_width-step*2
                legionaryBlackRect1.centery = step*4
            if cardinalWhiteRect1.colliderect(warriorBlackRect1):
                warriorBlackRect1.centerx = screen_width-step*3
                warriorBlackRect1.centery = step*4
            if cardinalWhiteRect1.colliderect(legionaryBlackRect2):
                legionaryBlackRect2.centerx = screen_width-step
                legionaryBlackRect2.centery = step*5
            if cardinalWhiteRect1.colliderect(warriorBlackRect2):
                warriorBlackRect2.centerx = screen_width-step*2
                warriorBlackRect2.centery = step*5
            if cardinalWhiteRect1.colliderect(legionaryBlackRect3):
                legionaryBlackRect3.centerx = screen_width-step*3
                legionaryBlackRect3.centery = step*5
            if cardinalWhiteRect1.colliderect(warriorBlackRect3):
                warriorBlackRect3.centerx = screen_width-step
                warriorBlackRect3.centery = step*6
            if cardinalWhiteRect1.colliderect(cardinalBlackRectCopy):
                cardinalBlackRectCopy.centerx=screen_width-step*2
                cardinalBlackRectCopy.centery=step*6
            if cardinalWhiteRect1.colliderect(cardinalBlackRectCopy_1):
                cardinalBlackRectCopy_1.centerx=screen_width-step*3
                cardinalBlackRectCopy_1.centery=step*6

            if archbishopWhiteRect1.colliderect(plagueDoctorBlackRect):
                plagueDoctorBlackRect.centerx = screen_width-step
                plagueDoctorBlackRect.centery = step
                archbishopWhiteFiguresCount_1+=1
            if archbishopWhiteRect1.colliderect(archbishopBlackRect):
                archbishopBlackRect.centerx = screen_width-step*2
                archbishopBlackRect.centery = step
                archbishopWhiteFiguresCount_1+=1
            if archbishopWhiteRect1.colliderect(cardinalBlackRect):
                cardinalBlackRect.centerx = screen_width-step*3
                cardinalBlackRect.centery = step
                archbishopWhiteFiguresCount_1+=1
            if archbishopWhiteRect1.colliderect(hadesBlackRect):
                hadesBlackRect.centerx = screen_width-step
                hadesBlackRect.centery = step*2
                archbishopWhiteFiguresCount_1+=1
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if archbishopWhiteRect1.colliderect(persephoneBlackRect):
                persephoneBlackRect.centerx = screen_width-step*2
                persephoneBlackRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user1_win=True
                archbishopWhiteFiguresCount_1+=1
            if archbishopWhiteRect1.colliderect(cardinalBlackRect1):
                cardinalBlackRect1.centerx = screen_width-step*3
                cardinalBlackRect1.centery = step*2
                archbishopWhiteFiguresCount_1+=1
            if archbishopWhiteRect1.colliderect(archbishopBlackRect1):
                archbishopBlackRect1.centerx = screen_width-step
                archbishopBlackRect1.centery = step*3
                archbishopWhiteFiguresCount_1+=1
            if archbishopWhiteRect1.colliderect(plagueDoctorBlackRect1):
                plagueDoctorBlackRect1.centerx = screen_width-step*2
                plagueDoctorBlackRect1.centery = step*3
                archbishopWhiteFiguresCount_1+=1
            if archbishopWhiteRect1.colliderect(legionaryBlackRect):
                legionaryBlackRect.centerx = screen_width-step*3
                legionaryBlackRect.centery = step*3
                archbishopWhiteFiguresCount_1+=1
            if archbishopWhiteRect1.colliderect(warriorBlackRect):
                warriorBlackRect.centerx = screen_width-step
                warriorBlackRect.centery = step*4
                archbishopWhiteFiguresCount_1+=1
            if archbishopWhiteRect1.colliderect(legionaryBlackRect1):
                legionaryBlackRect1.centerx = screen_width-step*2
                legionaryBlackRect1.centery = step*4
                archbishopWhiteFiguresCount_1+=1
            if archbishopWhiteRect1.colliderect(warriorBlackRect1):
                warriorBlackRect1.centerx = screen_width-step*3
                warriorBlackRect1.centery = step*4
                archbishopWhiteFiguresCount_1+=1
            if archbishopWhiteRect1.colliderect(legionaryBlackRect2):
                legionaryBlackRect2.centerx = screen_width-step
                legionaryBlackRect2.centery = step*5
                archbishopWhiteFiguresCount_1+=1
            if archbishopWhiteRect1.colliderect(warriorBlackRect2):
                warriorBlackRect2.centerx = screen_width-step*2
                warriorBlackRect2.centery = step*5
                archbishopWhiteFiguresCount_1+=1
            if archbishopWhiteRect1.colliderect(legionaryBlackRect3):
                legionaryBlackRect3.centerx = screen_width-step*3
                legionaryBlackRect3.centery = step*5
                archbishopWhiteFiguresCount_1+=1
            if archbishopWhiteRect1.colliderect(warriorBlackRect3):
                warriorBlackRect3.centerx = screen_width-step
                warriorBlackRect3.centery = step*6
                archbishopWhiteFiguresCount_1+=1
            if archbishopWhiteRect1.colliderect(cardinalBlackRectCopy):
                cardinalBlackRectCopy.centerx=screen_width-step*2
                cardinalBlackRectCopy.centery=step*6
                archbishopWhiteFiguresCount_1+=1
            if archbishopWhiteRect1.colliderect(cardinalBlackRectCopy_1):
                cardinalBlackRectCopy_1.centerx=screen_width-step*3
                cardinalBlackRectCopy_1.centery=step*6
                archbishopWhiteFiguresCount_1+=1

            if plagueDoctorWhiteRect1.colliderect(plagueDoctorBlackRect):
                plagueDoctorBlackRect.centerx = screen_width-step
                plagueDoctorBlackRect.centery = step
            if plagueDoctorWhiteRect1.colliderect(archbishopBlackRect):
                archbishopBlackRect.centerx = screen_width-step*2
                archbishopBlackRect.centery = step
            if plagueDoctorWhiteRect1.colliderect(cardinalBlackRect):
                cardinalBlackRect.centerx = screen_width-step*3
                cardinalBlackRect.centery = step
            if plagueDoctorWhiteRect1.colliderect(hadesBlackRect):
                hadesBlackRect.centerx = screen_width-step
                hadesBlackRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if plagueDoctorWhiteRect1.colliderect(persephoneBlackRect):
                persephoneBlackRect.centerx = screen_width-step*2
                persephoneBlackRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user1_win=True
            if plagueDoctorWhiteRect1.colliderect(cardinalBlackRect1):
                cardinalBlackRect1.centerx = screen_width-step*3
                cardinalBlackRect1.centery = step*2
            if plagueDoctorWhiteRect1.colliderect(archbishopBlackRect1):
                archbishopBlackRect1.centerx = screen_width-step
                archbishopBlackRect1.centery = step*3
            if plagueDoctorWhiteRect1.colliderect(plagueDoctorBlackRect1):
                plagueDoctorBlackRect1.centerx = screen_width-step*2
                plagueDoctorBlackRect1.centery = step*3
            if plagueDoctorWhiteRect1.colliderect(legionaryBlackRect):
                legionaryBlackRect.centerx = screen_width-step*3
                legionaryBlackRect.centery = step*3
            if plagueDoctorWhiteRect1.colliderect(warriorBlackRect):
                warriorBlackRect.centerx = screen_width-step
                warriorBlackRect.centery = step*4
            if plagueDoctorWhiteRect1.colliderect(legionaryBlackRect1):
                legionaryBlackRect1.centerx = screen_width-step*2
                legionaryBlackRect1.centery = step*4
            if plagueDoctorWhiteRect1.colliderect(warriorBlackRect1):
                warriorBlackRect1.centerx = screen_width-step*3
                warriorBlackRect1.centery = step*4
            if plagueDoctorWhiteRect1.colliderect(legionaryBlackRect2):
                legionaryBlackRect2.centerx = screen_width-step
                legionaryBlackRect2.centery = step*5
            if plagueDoctorWhiteRect1.colliderect(warriorBlackRect2):
                warriorBlackRect2.centerx = screen_width-step*2
                warriorBlackRect2.centery = step*5
            if plagueDoctorWhiteRect1.colliderect(legionaryBlackRect3):
                legionaryBlackRect3.centerx = screen_width-step*3
                legionaryBlackRect3.centery = step*5
            if plagueDoctorWhiteRect1.colliderect(warriorBlackRect3):
                warriorBlackRect3.centerx = screen_width-step
                warriorBlackRect3.centery = step*6
            if plagueDoctorWhiteRect1.colliderect(cardinalBlackRectCopy):
                cardinalBlackRectCopy.centerx=screen_width-step*2
                cardinalBlackRectCopy.centery=step*6
            if plagueDoctorWhiteRect1.colliderect(cardinalBlackRectCopy_1):
                cardinalBlackRectCopy_1.centerx=screen_width-step*3
                cardinalBlackRectCopy_1.centery=step*6

            if legionaryWhiteRect.colliderect(plagueDoctorBlackRect):
                plagueDoctorBlackRect.centerx = screen_width-step
                plagueDoctorBlackRect.centery = step
            if legionaryWhiteRect.colliderect(archbishopBlackRect):
                archbishopBlackRect.centerx = screen_width-step*2
                archbishopBlackRect.centery = step
            if legionaryWhiteRect.colliderect(cardinalBlackRect):
                cardinalBlackRect.centerx = screen_width-step*3
                cardinalBlackRect.centery = step
            if legionaryWhiteRect.colliderect(hadesBlackRect):
                hadesBlackRect.centerx = screen_width-step
                hadesBlackRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if legionaryWhiteRect.colliderect(persephoneBlackRect):
                persephoneBlackRect.centerx = screen_width-step*2
                persephoneBlackRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user1_win=True
            if legionaryWhiteRect.colliderect(cardinalBlackRect1):
                cardinalBlackRect1.centerx = screen_width-step*3
                cardinalBlackRect1.centery = step*2
            if legionaryWhiteRect.colliderect(archbishopBlackRect1):
                archbishopBlackRect1.centerx = screen_width-step
                archbishopBlackRect1.centery = step*3
            if legionaryWhiteRect.colliderect(plagueDoctorBlackRect1):
                plagueDoctorBlackRect1.centerx = screen_width-step*2
                plagueDoctorBlackRect1.centery = step*3
            if legionaryWhiteRect.colliderect(legionaryBlackRect):
                legionaryBlackRect.centerx = screen_width-step*3
                legionaryBlackRect.centery = step*3
            if legionaryWhiteRect.colliderect(warriorBlackRect):
                warriorBlackRect.centerx = screen_width-step
                warriorBlackRect.centery = step*4
            if legionaryWhiteRect.colliderect(legionaryBlackRect1):
                legionaryBlackRect1.centerx = screen_width-step*2
                legionaryBlackRect1.centery = step*4
            if legionaryWhiteRect.colliderect(warriorBlackRect1):
                warriorBlackRect1.centerx = screen_width-step*3
                warriorBlackRect1.centery = step*4
            if legionaryWhiteRect.colliderect(legionaryBlackRect2):
                legionaryBlackRect2.centerx = screen_width-step
                legionaryBlackRect2.centery = step*5
            if legionaryWhiteRect.colliderect(warriorBlackRect2):
                warriorBlackRect2.centerx = screen_width-step*2
                warriorBlackRect2.centery = step*5
            if legionaryWhiteRect.colliderect(legionaryBlackRect3):
                legionaryBlackRect3.centerx = screen_width-step*3
                legionaryBlackRect3.centery = step*5
            if legionaryWhiteRect.colliderect(warriorBlackRect3):
                warriorBlackRect3.centerx = screen_width-step
                warriorBlackRect3.centery = step*6
            if legionaryWhiteRect.colliderect(cardinalBlackRectCopy):
                cardinalBlackRectCopy.centerx=screen_width-step*2
                cardinalBlackRectCopy.centery=step*6
            if legionaryWhiteRect.colliderect(cardinalBlackRectCopy_1):
                cardinalBlackRectCopy_1.centerx=screen_width-step*3
                cardinalBlackRectCopy_1.centery=step*6

            if warriorWhiteRect.colliderect(plagueDoctorBlackRect):
                plagueDoctorBlackRect.centerx = screen_width-step
                plagueDoctorBlackRect.centery = step
            if warriorWhiteRect.colliderect(archbishopBlackRect):
                archbishopBlackRect.centerx = screen_width-step*2
                archbishopBlackRect.centery = step
            if warriorWhiteRect.colliderect(cardinalBlackRect):
                cardinalBlackRect.centerx = screen_width-step*3
                cardinalBlackRect.centery = step
            if warriorWhiteRect.colliderect(hadesBlackRect):
                hadesBlackRect.centerx = screen_width-step
                hadesBlackRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if warriorWhiteRect.colliderect(persephoneBlackRect):
                persephoneBlackRect.centerx = screen_width-step*2
                persephoneBlackRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user1_win=True
            if warriorWhiteRect.colliderect(cardinalBlackRect1):
                cardinalBlackRect1.centerx = screen_width-step*3
                cardinalBlackRect1.centery = step*2
            if warriorWhiteRect.colliderect(archbishopBlackRect1):
                archbishopBlackRect1.centerx = screen_width-step
                archbishopBlackRect1.centery = step*3
            if warriorWhiteRect.colliderect(plagueDoctorBlackRect1):
                plagueDoctorBlackRect1.centerx = screen_width-step*2
                plagueDoctorBlackRect1.centery = step*3
            if warriorWhiteRect.colliderect(legionaryBlackRect):
                legionaryBlackRect.centerx = screen_width-step*3
                legionaryBlackRect.centery = step*3
            if warriorWhiteRect.colliderect(warriorBlackRect):
                warriorBlackRect.centerx = screen_width-step
                warriorBlackRect.centery = step*4
            if warriorWhiteRect.colliderect(legionaryBlackRect1):
                legionaryBlackRect1.centerx = screen_width-step*2
                legionaryBlackRect1.centery = step*4
            if warriorWhiteRect.colliderect(warriorBlackRect1):
                warriorBlackRect1.centerx = screen_width-step*3
                warriorBlackRect1.centery = step*4
            if warriorWhiteRect.colliderect(legionaryBlackRect2):
                legionaryBlackRect2.centerx = screen_width-step
                legionaryBlackRect2.centery = step*5
            if warriorWhiteRect.colliderect(warriorBlackRect2):
                warriorBlackRect2.centerx = screen_width-step*2
                warriorBlackRect2.centery = step*5
            if warriorWhiteRect.colliderect(legionaryBlackRect3):
                legionaryBlackRect3.centerx = screen_width-step*3
                legionaryBlackRect3.centery = step*5
            if warriorWhiteRect.colliderect(warriorBlackRect3):
                warriorBlackRect3.centerx = screen_width-step
                warriorBlackRect3.centery = step*6
            if warriorWhiteRect.colliderect(cardinalBlackRectCopy):
                cardinalBlackRectCopy.centerx=screen_width-step*2
                cardinalBlackRectCopy.centery=step*6
            if warriorWhiteRect.colliderect(cardinalBlackRectCopy_1):
                cardinalBlackRectCopy_1.centerx=screen_width-step*3
                cardinalBlackRectCopy_1.centery=step*6

            if legionaryWhiteRect1.colliderect(plagueDoctorBlackRect):
                plagueDoctorBlackRect.centerx = screen_width-step
                plagueDoctorBlackRect.centery = step
            if legionaryWhiteRect1.colliderect(archbishopBlackRect):
                archbishopBlackRect.centerx = screen_width-step*2
                archbishopBlackRect.centery = step
            if legionaryWhiteRect1.colliderect(cardinalBlackRect):
                cardinalBlackRect.centerx = screen_width-step*3
                cardinalBlackRect.centery = step
            if legionaryWhiteRect1.colliderect(hadesBlackRect):
                hadesBlackRect.centerx = screen_width-step
                hadesBlackRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if legionaryWhiteRect1.colliderect(persephoneBlackRect):
                persephoneBlackRect.centerx = screen_width-step*2
                persephoneBlackRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user1_win=True
            if legionaryWhiteRect1.colliderect(cardinalBlackRect1):
                cardinalBlackRect1.centerx = screen_width-step*3
                cardinalBlackRect1.centery = step*2
            if legionaryWhiteRect1.colliderect(archbishopBlackRect1):
                archbishopBlackRect1.centerx = screen_width-step
                archbishopBlackRect1.centery = step*3
            if legionaryWhiteRect1.colliderect(plagueDoctorBlackRect1):
                plagueDoctorBlackRect1.centerx = screen_width-step*2
                plagueDoctorBlackRect1.centery = step*3
            if legionaryWhiteRect1.colliderect(legionaryBlackRect):
                legionaryBlackRect.centerx = screen_width-step*3
                legionaryBlackRect.centery = step*3
            if legionaryWhiteRect1.colliderect(warriorBlackRect):
                warriorBlackRect.centerx = screen_width-step
                warriorBlackRect.centery = step*4
            if legionaryWhiteRect1.colliderect(legionaryBlackRect1):
                legionaryBlackRect1.centerx = screen_width-step*2
                legionaryBlackRect1.centery = step*4
            if legionaryWhiteRect1.colliderect(warriorBlackRect1):
                warriorBlackRect1.centerx = screen_width-step*3
                warriorBlackRect1.centery = step*4
            if legionaryWhiteRect1.colliderect(legionaryBlackRect2):
                legionaryBlackRect2.centerx = screen_width-step
                legionaryBlackRect2.centery = step*5
            if legionaryWhiteRect1.colliderect(warriorBlackRect2):
                warriorBlackRect2.centerx = screen_width-step*2
                warriorBlackRect2.centery = step*5
            if legionaryWhiteRect1.colliderect(legionaryBlackRect3):
                legionaryBlackRect3.centerx = screen_width-step*3
                legionaryBlackRect3.centery = step*5
            if legionaryWhiteRect1.colliderect(warriorBlackRect3):
                warriorBlackRect3.centerx = screen_width-step
                warriorBlackRect3.centery = step*6
            if legionaryWhiteRect1.colliderect(cardinalBlackRectCopy):
                cardinalBlackRectCopy.centerx=screen_width-step*2
                cardinalBlackRectCopy.centery=step*6
            if legionaryWhiteRect1.colliderect(cardinalBlackRectCopy_1):
                cardinalBlackRectCopy_1.centerx=screen_width-step*3
                cardinalBlackRectCopy_1.centery=step*6

            if warriorWhiteRect1.colliderect(plagueDoctorBlackRect):
                plagueDoctorBlackRect.centerx = screen_width-step
                plagueDoctorBlackRect.centery = step
            if warriorWhiteRect1.colliderect(archbishopBlackRect):
                archbishopBlackRect.centerx = screen_width-step*2
                archbishopBlackRect.centery = step
            if warriorWhiteRect1.colliderect(cardinalBlackRect):
                cardinalBlackRect.centerx = screen_width-step*3
                cardinalBlackRect.centery = step
            if warriorWhiteRect1.colliderect(hadesBlackRect):
                hadesBlackRect.centerx = screen_width-step
                hadesBlackRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if warriorWhiteRect1.colliderect(persephoneBlackRect):
                persephoneBlackRect.centerx = screen_width-step*2
                persephoneBlackRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user1_win=True
            if warriorWhiteRect1.colliderect(cardinalBlackRect1):
                cardinalBlackRect1.centerx = screen_width-step*3
                cardinalBlackRect1.centery = step*2
            if warriorWhiteRect1.colliderect(archbishopBlackRect1):
                archbishopBlackRect1.centerx = screen_width-step
                archbishopBlackRect1.centery = step*3
            if warriorWhiteRect1.colliderect(plagueDoctorBlackRect1):
                plagueDoctorBlackRect1.centerx = screen_width-step*2
                plagueDoctorBlackRect1.centery = step*3
            if warriorWhiteRect1.colliderect(legionaryBlackRect):
                legionaryBlackRect.centerx = screen_width-step*3
                legionaryBlackRect.centery = step*3
            if warriorWhiteRect1.colliderect(warriorBlackRect):
                warriorBlackRect.centerx = screen_width-step
                warriorBlackRect.centery = step*4
            if warriorWhiteRect1.colliderect(legionaryBlackRect1):
                legionaryBlackRect1.centerx = screen_width-step*2
                legionaryBlackRect1.centery = step*4
            if warriorWhiteRect1.colliderect(warriorBlackRect1):
                warriorBlackRect1.centerx = screen_width-step*3
                warriorBlackRect1.centery = step*4
            if warriorWhiteRect1.colliderect(legionaryBlackRect2):
                legionaryBlackRect2.centerx = screen_width-step
                legionaryBlackRect2.centery = step*5
            if warriorWhiteRect1.colliderect(warriorBlackRect2):
                warriorBlackRect2.centerx = screen_width-step*2
                warriorBlackRect2.centery = step*5
            if warriorWhiteRect1.colliderect(legionaryBlackRect3):
                legionaryBlackRect3.centerx = screen_width-step*3
                legionaryBlackRect3.centery = step*5
            if warriorWhiteRect1.colliderect(warriorBlackRect3):
                warriorBlackRect3.centerx = screen_width-step
                warriorBlackRect3.centery = step*6
            if warriorWhiteRect1.colliderect(cardinalBlackRectCopy):
                cardinalBlackRectCopy.centerx=screen_width-step*2
                cardinalBlackRectCopy.centery=step*6
            if warriorWhiteRect1.colliderect(cardinalBlackRectCopy_1):
                cardinalBlackRectCopy_1.centerx=screen_width-step*3
                cardinalBlackRectCopy_1.centery=step*6

            if legionaryWhiteRect2.colliderect(plagueDoctorBlackRect):
                plagueDoctorBlackRect.centerx = screen_width-step
                plagueDoctorBlackRect.centery = step
            if legionaryWhiteRect2.colliderect(archbishopBlackRect):
                archbishopBlackRect.centerx = screen_width-step*2
                archbishopBlackRect.centery = step
            if legionaryWhiteRect2.colliderect(cardinalBlackRect):
                cardinalBlackRect.centerx = screen_width-step*3
                cardinalBlackRect.centery = step
            if legionaryWhiteRect2.colliderect(hadesBlackRect):
                hadesBlackRect.centerx = screen_width-step
                hadesBlackRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if legionaryWhiteRect2.colliderect(persephoneBlackRect):
                persephoneBlackRect.centerx = screen_width-step*2
                persephoneBlackRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user1_win=True
            if legionaryWhiteRect2.colliderect(cardinalBlackRect1):
                cardinalBlackRect1.centerx = screen_width-step*3
                cardinalBlackRect1.centery = step*2
            if legionaryWhiteRect2.colliderect(archbishopBlackRect1):
                archbishopBlackRect1.centerx = screen_width-step
                archbishopBlackRect1.centery = step*3
            if legionaryWhiteRect2.colliderect(plagueDoctorBlackRect1):
                plagueDoctorBlackRect1.centerx = screen_width-step*2
                plagueDoctorBlackRect1.centery = step*3
            if legionaryWhiteRect2.colliderect(legionaryBlackRect):
                legionaryBlackRect.centerx = screen_width-step*3
                legionaryBlackRect.centery = step*3
            if legionaryWhiteRect2.colliderect(warriorBlackRect):
                warriorBlackRect.centerx = screen_width-step
                warriorBlackRect.centery = step*4
            if legionaryWhiteRect2.colliderect(legionaryBlackRect1):
                legionaryBlackRect1.centerx = screen_width-step*2
                legionaryBlackRect1.centery = step*4
            if legionaryWhiteRect2.colliderect(warriorBlackRect1):
                warriorBlackRect1.centerx = screen_width-step*3
                warriorBlackRect1.centery = step*4
            if legionaryWhiteRect2.colliderect(legionaryBlackRect2):
                legionaryBlackRect2.centerx = screen_width-step
                legionaryBlackRect2.centery = step*5
            if legionaryWhiteRect2.colliderect(warriorBlackRect2):
                warriorBlackRect2.centerx = screen_width-step*2
                warriorBlackRect2.centery = step*5
            if legionaryWhiteRect2.colliderect(legionaryBlackRect3):
                legionaryBlackRect3.centerx = screen_width-step*3
                legionaryBlackRect3.centery = step*5
            if legionaryWhiteRect2.colliderect(warriorBlackRect3):
                warriorBlackRect3.centerx = screen_width-step
                warriorBlackRect3.centery = step*6
            if legionaryWhiteRect2.colliderect(cardinalBlackRectCopy):
                cardinalBlackRectCopy.centerx=screen_width-step*2
                cardinalBlackRectCopy.centery=step*6
            if legionaryWhiteRect2.colliderect(cardinalBlackRectCopy_1):
                cardinalBlackRectCopy_1.centerx=screen_width-step*3
                cardinalBlackRectCopy_1.centery=step*6

            if warriorWhiteRect2.colliderect(plagueDoctorBlackRect):
                plagueDoctorBlackRect.centerx = screen_width-step
                plagueDoctorBlackRect.centery = step
            if warriorWhiteRect2.colliderect(archbishopBlackRect):
                archbishopBlackRect.centerx = screen_width-step*2
                archbishopBlackRect.centery = step
            if warriorWhiteRect2.colliderect(cardinalBlackRect):
                cardinalBlackRect.centerx = screen_width-step*3
                cardinalBlackRect.centery = step
            if warriorWhiteRect2.colliderect(hadesBlackRect):
                hadesBlackRect.centerx = screen_width-step
                hadesBlackRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if warriorWhiteRect2.colliderect(persephoneBlackRect):
                persephoneBlackRect.centerx = screen_width-step*2
                persephoneBlackRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user1_win=True
            if warriorWhiteRect2.colliderect(cardinalBlackRect1):
                cardinalBlackRect1.centerx = screen_width-step*3
                cardinalBlackRect1.centery = step*2
            if warriorWhiteRect2.colliderect(archbishopBlackRect1):
                archbishopBlackRect1.centerx = screen_width-step
                archbishopBlackRect1.centery = step*3
            if warriorWhiteRect2.colliderect(plagueDoctorBlackRect1):
                plagueDoctorBlackRect1.centerx = screen_width-step*2
                plagueDoctorBlackRect1.centery = step*3
            if warriorWhiteRect2.colliderect(legionaryBlackRect):
                legionaryBlackRect.centerx = screen_width-step*3
                legionaryBlackRect.centery = step*3
            if warriorWhiteRect2.colliderect(warriorBlackRect):
                warriorBlackRect.centerx = screen_width-step
                warriorBlackRect.centery = step*4
            if warriorWhiteRect2.colliderect(legionaryBlackRect1):
                legionaryBlackRect1.centerx = screen_width-step*2
                legionaryBlackRect1.centery = step*4
            if warriorWhiteRect2.colliderect(warriorBlackRect1):
                warriorBlackRect1.centerx = screen_width-step*3
                warriorBlackRect1.centery = step*4
            if warriorWhiteRect2.colliderect(legionaryBlackRect2):
                legionaryBlackRect2.centerx = screen_width-step
                legionaryBlackRect2.centery = step*5
            if warriorWhiteRect2.colliderect(warriorBlackRect2):
                warriorBlackRect2.centerx = screen_width-step*2
                warriorBlackRect2.centery = step*5
            if warriorWhiteRect2.colliderect(legionaryBlackRect3):
                legionaryBlackRect3.centerx = screen_width-step*3
                legionaryBlackRect3.centery = step*5
            if warriorWhiteRect2.colliderect(warriorBlackRect3):
                warriorBlackRect3.centerx = screen_width-step
                warriorBlackRect3.centery = step*6
            if warriorWhiteRect2.colliderect(cardinalBlackRectCopy):
                cardinalBlackRectCopy.centerx=screen_width-step*2
                cardinalBlackRectCopy.centery=step*6
            if warriorWhiteRect2.colliderect(cardinalBlackRectCopy_1):
                cardinalBlackRectCopy_1.centerx=screen_width-step*3
                cardinalBlackRectCopy_1.centery=step*6

            if legionaryWhiteRect3.colliderect(plagueDoctorBlackRect):
                plagueDoctorBlackRect.centerx = screen_width-step
                plagueDoctorBlackRect.centery = step
            if legionaryWhiteRect3.colliderect(archbishopBlackRect):
                archbishopBlackRect.centerx = screen_width-step*2
                archbishopBlackRect.centery = step
            if legionaryWhiteRect3.colliderect(cardinalBlackRect):
                cardinalBlackRect.centerx = screen_width-step*3
                cardinalBlackRect.centery = step
            if legionaryWhiteRect3.colliderect(hadesBlackRect):
                hadesBlackRect.centerx = screen_width-step
                hadesBlackRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if legionaryWhiteRect3.colliderect(persephoneBlackRect):
                persephoneBlackRect.centerx = screen_width-step*2
                persephoneBlackRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user1_win=True
            if legionaryWhiteRect3.colliderect(cardinalBlackRect1):
                cardinalBlackRect1.centerx = screen_width-step*3
                cardinalBlackRect1.centery = step*2
            if legionaryWhiteRect3.colliderect(archbishopBlackRect1):
                archbishopBlackRect1.centerx = screen_width-step
                archbishopBlackRect1.centery = step*3
            if legionaryWhiteRect3.colliderect(plagueDoctorBlackRect1):
                plagueDoctorBlackRect1.centerx = screen_width-step*2
                plagueDoctorBlackRect1.centery = step*3
            if legionaryWhiteRect3.colliderect(legionaryBlackRect):
                legionaryBlackRect.centerx = screen_width-step*3
                legionaryBlackRect.centery = step*3
            if legionaryWhiteRect3.colliderect(warriorBlackRect):
                warriorBlackRect.centerx = screen_width-step
                warriorBlackRect.centery = step*4
            if legionaryWhiteRect3.colliderect(legionaryBlackRect1):
                legionaryBlackRect1.centerx = screen_width-step*2
                legionaryBlackRect1.centery = step*4
            if legionaryWhiteRect3.colliderect(warriorBlackRect1):
                warriorBlackRect1.centerx = screen_width-step*3
                warriorBlackRect1.centery = step*4
            if legionaryWhiteRect3.colliderect(legionaryBlackRect2):
                legionaryBlackRect2.centerx = screen_width-step
                legionaryBlackRect2.centery = step*5
            if legionaryWhiteRect3.colliderect(warriorBlackRect2):
                warriorBlackRect2.centerx = screen_width-step*2
                warriorBlackRect2.centery = step*5
            if legionaryWhiteRect3.colliderect(legionaryBlackRect3):
                legionaryBlackRect3.centerx = screen_width-step*3
                legionaryBlackRect3.centery = step*5
            if legionaryWhiteRect3.colliderect(warriorBlackRect3):
                warriorBlackRect3.centerx = screen_width-step
                warriorBlackRect3.centery = step*6
            if legionaryWhiteRect3.colliderect(cardinalBlackRectCopy):
                cardinalBlackRectCopy.centerx=screen_width-step*2
                cardinalBlackRectCopy.centery=step*6
            if legionaryWhiteRect3.colliderect(cardinalBlackRectCopy_1):
                cardinalBlackRectCopy_1.centerx=screen_width-step*3
                cardinalBlackRectCopy_1.centery=step*6

            if warriorWhiteRect3.colliderect(plagueDoctorBlackRect):
                plagueDoctorBlackRect.centerx = screen_width-step
                plagueDoctorBlackRect.centery = step
            if warriorWhiteRect3.colliderect(archbishopBlackRect):
                archbishopBlackRect.centerx = screen_width-step*2
                archbishopBlackRect.centery = step
            if warriorWhiteRect3.colliderect(cardinalBlackRect):
                cardinalBlackRect.centerx = screen_width-step*3
                cardinalBlackRect.centery = step
            if warriorWhiteRect3.colliderect(hadesBlackRect):
                hadesBlackRect.centerx = screen_width-step
                hadesBlackRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if warriorWhiteRect3.colliderect(persephoneBlackRect):
                persephoneBlackRect.centerx = screen_width-step*2
                persephoneBlackRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user1_win=True
            if warriorWhiteRect3.colliderect(cardinalBlackRect1):
                cardinalBlackRect1.centerx = screen_width-step*3
                cardinalBlackRect1.centery = step*2
            if warriorWhiteRect3.colliderect(archbishopBlackRect1):
                archbishopBlackRect1.centerx = screen_width-step
                archbishopBlackRect1.centery = step*3
            if warriorWhiteRect3.colliderect(plagueDoctorBlackRect1):
                plagueDoctorBlackRect1.centerx = screen_width-step*2
                plagueDoctorBlackRect1.centery = step*3
            if warriorWhiteRect3.colliderect(legionaryBlackRect):
                legionaryBlackRect.centerx = screen_width-step*3
                legionaryBlackRect.centery = step*3
            if warriorWhiteRect3.colliderect(warriorBlackRect):
                warriorBlackRect.centerx = screen_width-step
                warriorBlackRect.centery = step*4
            if warriorWhiteRect3.colliderect(legionaryBlackRect1):
                legionaryBlackRect1.centerx = screen_width-step*2
                legionaryBlackRect1.centery = step*4
            if warriorWhiteRect3.colliderect(warriorBlackRect1):
                warriorBlackRect1.centerx = screen_width-step*3
                warriorBlackRect1.centery = step*4
            if warriorWhiteRect3.colliderect(legionaryBlackRect2):
                legionaryBlackRect2.centerx = screen_width-step
                legionaryBlackRect2.centery = step*5
            if warriorWhiteRect3.colliderect(warriorBlackRect2):
                warriorBlackRect2.centerx = screen_width-step*2
                warriorBlackRect2.centery = step*5
            if warriorWhiteRect3.colliderect(legionaryBlackRect3):
                legionaryBlackRect3.centerx = screen_width-step*3
                legionaryBlackRect3.centery = step*5
            if warriorWhiteRect3.colliderect(warriorBlackRect3):
                warriorBlackRect3.centerx = screen_width-step
                warriorBlackRect3.centery = step*6
            if warriorWhiteRect3.colliderect(cardinalBlackRectCopy):
                cardinalBlackRectCopy.centerx=screen_width-step*2
                cardinalBlackRectCopy.centery=step*6
            if warriorWhiteRect3.colliderect(cardinalBlackRectCopy_1):
                cardinalBlackRectCopy_1.centerx=screen_width-step*3
                cardinalBlackRectCopy_1.centery=step*6
            
            if cardinalWhiteRectCopy.colliderect(plagueDoctorBlackRect):
                plagueDoctorBlackRect.centerx = screen_width-step
                plagueDoctorBlackRect.centery = step
            if cardinalWhiteRectCopy.colliderect(archbishopBlackRect):
                archbishopBlackRect.centerx = screen_width-step*2
                archbishopBlackRect.centery = step
            if cardinalWhiteRectCopy.colliderect(cardinalBlackRect):
                cardinalBlackRect.centerx = screen_width-step*3
                cardinalBlackRect.centery = step
            if cardinalWhiteRectCopy.colliderect(hadesBlackRect):
                hadesBlackRect.centerx = screen_width-step
                hadesBlackRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if cardinalWhiteRectCopy.colliderect(persephoneBlackRect):
                persephoneBlackRect.centerx = screen_width-step*2
                persephoneBlackRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user1_win=True
            if cardinalWhiteRectCopy.colliderect(cardinalBlackRect1):
                cardinalBlackRect1.centerx = screen_width-step*3
                cardinalBlackRect1.centery = step*2
            if cardinalWhiteRectCopy.colliderect(archbishopBlackRect1):
                archbishopBlackRect1.centerx = screen_width-step
                archbishopBlackRect1.centery = step*3
            if cardinalWhiteRectCopy.colliderect(plagueDoctorBlackRect1):
                plagueDoctorBlackRect1.centerx = screen_width-step*2
                plagueDoctorBlackRect1.centery = step*3
            if cardinalWhiteRectCopy.colliderect(legionaryBlackRect):
                legionaryBlackRect.centerx = screen_width-step*3
                legionaryBlackRect.centery = step*3
            if cardinalWhiteRectCopy.colliderect(warriorBlackRect):
                warriorBlackRect.centerx = screen_width-step
                warriorBlackRect.centery = step*4
            if cardinalWhiteRectCopy.colliderect(legionaryBlackRect1):
                legionaryBlackRect1.centerx = screen_width-step*2
                legionaryBlackRect1.centery = step*4
            if cardinalWhiteRectCopy.colliderect(warriorBlackRect1):
                warriorBlackRect1.centerx = screen_width-step*3
                warriorBlackRect1.centery = step*4
            if cardinalWhiteRectCopy.colliderect(legionaryBlackRect2):
                legionaryBlackRect2.centerx = screen_width-step
                legionaryBlackRect2.centery = step*5
            if cardinalWhiteRectCopy.colliderect(warriorBlackRect2):
                warriorBlackRect2.centerx = screen_width-step*2
                warriorBlackRect2.centery = step*5
            if cardinalWhiteRectCopy.colliderect(legionaryBlackRect3):
                legionaryBlackRect3.centerx = screen_width-step*3
                legionaryBlackRect3.centery = step*5
            if cardinalWhiteRectCopy.colliderect(warriorBlackRect3):
                warriorBlackRect3.centerx = screen_width-step
                warriorBlackRect3.centery = step*6
            if cardinalWhiteRectCopy.colliderect(cardinalBlackRectCopy):
                cardinalBlackRectCopy.centerx=screen_width-step*2
                cardinalBlackRectCopy.centery=step*6
            if cardinalWhiteRectCopy.colliderect(cardinalBlackRectCopy_1):
                cardinalBlackRectCopy_1.centerx=screen_width-step*3
                cardinalBlackRectCopy_1.centery=step*6
            
            if cardinalWhiteRectCopy_1.colliderect(plagueDoctorBlackRect):
                plagueDoctorBlackRect.centerx = screen_width-step
                plagueDoctorBlackRect.centery = step
            if cardinalWhiteRectCopy_1.colliderect(archbishopBlackRect):
                archbishopBlackRect.centerx = screen_width-step*2
                archbishopBlackRect.centery = step
            if cardinalWhiteRectCopy_1.colliderect(cardinalBlackRect):
                cardinalBlackRect.centerx = screen_width-step*3
                cardinalBlackRect.centery = step
            if cardinalWhiteRectCopy_1.colliderect(hadesBlackRect):
                hadesBlackRect.centerx = screen_width-step
                hadesBlackRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if cardinalWhiteRectCopy_1.colliderect(persephoneBlackRect):
                persephoneBlackRect.centerx = screen_width-step*2
                persephoneBlackRect.centery = step*2
                play_game=False
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user1_win=True
            if cardinalWhiteRectCopy_1.colliderect(cardinalBlackRect1):
                cardinalBlackRect1.centerx = screen_width-step*3
                cardinalBlackRect1.centery = step*2
            if cardinalWhiteRectCopy_1.colliderect(archbishopBlackRect1):
                archbishopBlackRect1.centerx = screen_width-step
                archbishopBlackRect1.centery = step*3
            if cardinalWhiteRectCopy_1.colliderect(plagueDoctorBlackRect1):
                plagueDoctorBlackRect1.centerx = screen_width-step*2
                plagueDoctorBlackRect1.centery = step*3
            if cardinalWhiteRectCopy_1.colliderect(legionaryBlackRect):
                legionaryBlackRect.centerx = screen_width-step*3
                legionaryBlackRect.centery = step*3
            if cardinalWhiteRectCopy_1.colliderect(warriorBlackRect):
                warriorBlackRect.centerx = screen_width-step
                warriorBlackRect.centery = step*4
            if cardinalWhiteRectCopy_1.colliderect(legionaryBlackRect1):
                legionaryBlackRect1.centerx = screen_width-step*2
                legionaryBlackRect1.centery = step*4
            if cardinalWhiteRectCopy_1.colliderect(warriorBlackRect1):
                warriorBlackRect1.centerx = screen_width-step*3
                warriorBlackRect1.centery = step*4
            if cardinalWhiteRectCopy_1.colliderect(legionaryBlackRect2):
                legionaryBlackRect2.centerx = screen_width-step
                legionaryBlackRect2.centery = step*5
            if cardinalWhiteRectCopy_1.colliderect(warriorBlackRect2):
                warriorBlackRect2.centerx = screen_width-step*2
                warriorBlackRect2.centery = step*5
            if cardinalWhiteRectCopy_1.colliderect(legionaryBlackRect3):
                legionaryBlackRect3.centerx = screen_width-step*3
                legionaryBlackRect3.centery = step*5
            if cardinalWhiteRectCopy_1.colliderect(warriorBlackRect3):
                warriorBlackRect3.centerx = screen_width-step
                warriorBlackRect3.centery = step*6
            if cardinalWhiteRectCopy_1.colliderect(cardinalBlackRectCopy):
                cardinalBlackRectCopy.centerx=screen_width-step*2
                cardinalBlackRectCopy.centery=step*6
            if cardinalWhiteRectCopy_1.colliderect(cardinalBlackRectCopy_1):
                cardinalBlackRectCopy_1.centerx=screen_width-step*3
                cardinalBlackRectCopy_1.centery=step*6

        else:
            if plagueDoctorBlackRect.colliderect(plagueDoctorWhiteRect):
                plagueDoctorWhiteRect.centerx = step
                plagueDoctorWhiteRect.centery = step
            if plagueDoctorBlackRect.colliderect(archbishopWhiteRect):
                archbishopWhiteRect.centerx = step*2
                plagueDoctorWhiteRect.centery = step
            if plagueDoctorBlackRect.colliderect(cardinalWhiteRect):
                cardinalWhiteRect.centerx = step*3
                cardinalWhiteRect.centery = step
            if plagueDoctorBlackRect.colliderect(hadesWhiteRect):
                hadesWhiteRect.centerx = step
                hadesWhiteRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if plagueDoctorBlackRect.colliderect(persephoneWhiteRect):
                persephoneWhiteRect.centerx = step*2
                persephoneWhiteRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user2_win=True
            if plagueDoctorBlackRect.colliderect(cardinalWhiteRect1):
                cardinalWhiteRect1.centerx = step*3
                cardinalWhiteRect1.centery = step*2
            if plagueDoctorBlackRect.colliderect(archbishopWhiteRect1):
                archbishopWhiteRect1.centerx = step
                archbishopWhiteRect1.centery = step*3
            if plagueDoctorBlackRect.colliderect(plagueDoctorWhiteRect1):
                plagueDoctorWhiteRect1.centerx = step*2
                plagueDoctorWhiteRect1.centery = step*3
            if plagueDoctorBlackRect.colliderect(legionaryWhiteRect):
                legionaryWhiteRect.centerx = step*3
                legionaryWhiteRect.centery = step*3
            if plagueDoctorBlackRect.colliderect(warriorWhiteRect):
                warriorWhiteRect.centerx = step
                warriorWhiteRect.centery = step*4
            if plagueDoctorBlackRect.colliderect(legionaryWhiteRect1):
                legionaryWhiteRect1.centerx = step*2
                legionaryWhiteRect1.centery = step*4
            if plagueDoctorBlackRect.colliderect(warriorWhiteRect1):
                warriorWhiteRect1.centerx = step*3
                warriorWhiteRect1.centery = step*4
            if plagueDoctorBlackRect.colliderect(legionaryWhiteRect2):
                legionaryWhiteRect2.centerx = step
                legionaryWhiteRect2.centery = step*5
            if plagueDoctorBlackRect.colliderect(warriorWhiteRect2):
                warriorWhiteRect2.centerx = step*2
                warriorWhiteRect2.centery = step*5
            if plagueDoctorBlackRect.colliderect(legionaryWhiteRect3):
                legionaryWhiteRect3.centerx = step*3
                legionaryWhiteRect3.centery = step*5
            if plagueDoctorBlackRect.colliderect(warriorWhiteRect3):
                warriorWhiteRect3.centerx = step
                warriorWhiteRect3.centery = step*6
            if plagueDoctorBlackRect.colliderect(cardinalWhiteRectCopy):
                cardinalWhiteRectCopy.centerx=step*2
                cardinalWhiteRectCopy.centery=step*6
            if plagueDoctorBlackRect.colliderect(cardinalWhiteRectCopy_1):
                cardinalWhiteRectCopy_1.centerx=step*3
                cardinalWhiteRectCopy_1.centery=step*6

            if archbishopBlackRect.colliderect(plagueDoctorWhiteRect):
                plagueDoctorWhiteRect.centerx = step
                plagueDoctorWhiteRect.centery = step
                archbishopBlackFiguresCount+=1
            if archbishopBlackRect.colliderect(archbishopWhiteRect):
                archbishopWhiteRect.centerx = step*2
                plagueDoctorWhiteRect.centery = step
                archbishopBlackFiguresCount+=1
            if archbishopBlackRect.colliderect(cardinalWhiteRect):
                cardinalWhiteRect.centerx = step*3
                cardinalWhiteRect.centery = step
                archbishopBlackFiguresCount+=1
            if archbishopBlackRect.colliderect(hadesWhiteRect):
                hadesWhiteRect.centerx = step
                hadesWhiteRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
                archbishopBlackFiguresCount+=1
            if archbishopBlackRect.colliderect(persephoneWhiteRect):
                persephoneWhiteRect.centerx = step*2
                persephoneWhiteRect.centery = step*2
                archbishopBlackFiguresCount+=1
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user2_win=True
            if archbishopBlackRect.colliderect(cardinalWhiteRect1):
                cardinalWhiteRect1.centerx = step*3
                cardinalWhiteRect1.centery = step*2
                archbishopBlackFiguresCount+=1
            if archbishopBlackRect.colliderect(archbishopWhiteRect1):
                archbishopWhiteRect1.centerx = step
                archbishopWhiteRect1.centery = step*3
                archbishopBlackFiguresCount+=1
            if archbishopBlackRect.colliderect(plagueDoctorWhiteRect1):
                plagueDoctorWhiteRect1.centerx = step*2
                plagueDoctorWhiteRect1.centery = step*3
                archbishopBlackFiguresCount+=1
            if archbishopBlackRect.colliderect(legionaryWhiteRect):
                legionaryWhiteRect.centerx = step*3
                legionaryWhiteRect.centery = step*3
                archbishopBlackFiguresCount+=1
            if archbishopBlackRect.colliderect(warriorWhiteRect):
                warriorWhiteRect.centerx = step
                warriorWhiteRect.centery = step*4
                archbishopBlackFiguresCount+=1
            if archbishopBlackRect.colliderect(legionaryWhiteRect1):
                legionaryWhiteRect1.centerx = step*2
                legionaryWhiteRect1.centery = step*4
                archbishopBlackFiguresCount+=1
            if archbishopBlackRect.colliderect(warriorWhiteRect1):
                warriorWhiteRect1.centerx = step*3
                warriorWhiteRect1.centery = step*4
                archbishopBlackFiguresCount+=1
            if archbishopBlackRect.colliderect(legionaryWhiteRect2):
                legionaryWhiteRect2.centerx = step
                legionaryWhiteRect2.centery = step*5
                archbishopBlackFiguresCount+=1
            if archbishopBlackRect.colliderect(warriorWhiteRect2):
                warriorWhiteRect2.centerx = step*2
                warriorWhiteRect2.centery = step*5
                archbishopBlackFiguresCount+=1
            if archbishopBlackRect.colliderect(legionaryWhiteRect3):
                legionaryWhiteRect3.centerx = step*3
                legionaryWhiteRect3.centery = step*5
                archbishopBlackFiguresCount+=1
            if archbishopBlackRect.colliderect(warriorWhiteRect3):
                warriorWhiteRect3.centerx = step
                warriorWhiteRect3.centery = step*6
                archbishopBlackFiguresCount+=1
            if archbishopBlackRect.colliderect(cardinalWhiteRectCopy):
                cardinalWhiteRectCopy.centerx=step*2
                cardinalWhiteRectCopy.centery=step*6
            if archbishopBlackRect.colliderect(cardinalWhiteRectCopy_1):
                cardinalWhiteRectCopy_1.centerx=step*3
                cardinalWhiteRectCopy_1.centery=step*6

            if cardinalBlackRect.colliderect(plagueDoctorWhiteRect):
                plagueDoctorWhiteRect.centerx = step
                plagueDoctorWhiteRect.centery = step
            if cardinalBlackRect.colliderect(archbishopWhiteRect):
                archbishopWhiteRect.centerx = step*2
                plagueDoctorWhiteRect.centery = step
            if cardinalBlackRect.colliderect(cardinalWhiteRect):
                cardinalWhiteRect.centerx = step*3
                cardinalWhiteRect.centery = step
            if cardinalBlackRect.colliderect(hadesWhiteRect):
                hadesWhiteRect.centerx = step
                hadesWhiteRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if cardinalBlackRect.colliderect(persephoneWhiteRect):
                persephoneWhiteRect.centerx = step*2
                persephoneWhiteRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user2_win=True
            if cardinalBlackRect.colliderect(cardinalWhiteRect1):
                cardinalWhiteRect1.centerx = step*3
                cardinalWhiteRect1.centery = step*2
            if cardinalBlackRect.colliderect(archbishopWhiteRect1):
                archbishopWhiteRect1.centerx = step
                archbishopWhiteRect1.centery = step*3
            if cardinalBlackRect.colliderect(plagueDoctorWhiteRect1):
                plagueDoctorWhiteRect1.centerx = step*2
                plagueDoctorWhiteRect1.centery = step*3
            if cardinalBlackRect.colliderect(legionaryWhiteRect):
                legionaryWhiteRect.centerx = step*3
                legionaryWhiteRect.centery = step*3
            if cardinalBlackRect.colliderect(warriorWhiteRect):
                warriorWhiteRect.centerx = step
                warriorWhiteRect.centery = step*4
            if cardinalBlackRect.colliderect(legionaryWhiteRect1):
                legionaryWhiteRect1.centerx = step*2
                legionaryWhiteRect1.centery = step*4
            if cardinalBlackRect.colliderect(warriorWhiteRect1):
                warriorWhiteRect1.centerx = step*3
                warriorWhiteRect1.centery = step*4
            if cardinalBlackRect.colliderect(legionaryWhiteRect2):
                legionaryWhiteRect2.centerx = step
                legionaryWhiteRect2.centery = step*5
            if cardinalBlackRect.colliderect(warriorWhiteRect2):
                warriorWhiteRect2.centerx = step*2
                warriorWhiteRect2.centery = step*5
            if cardinalBlackRect.colliderect(legionaryWhiteRect3):
                legionaryWhiteRect3.centerx = step*3
                legionaryWhiteRect3.centery = step*5
            if cardinalBlackRect.colliderect(warriorWhiteRect3):
                warriorWhiteRect3.centerx = step
                warriorWhiteRect3.centery = step*6
            if cardinalBlackRect.colliderect(cardinalWhiteRectCopy):
                cardinalWhiteRectCopy.centerx=step*2
                cardinalWhiteRectCopy.centery=step*6
            if cardinalBlackRect.colliderect(cardinalWhiteRectCopy_1):
                cardinalWhiteRectCopy_1.centerx=step*3
                cardinalWhiteRectCopy_1.centery=step*6

            if hadesBlackRect.colliderect(plagueDoctorWhiteRect):
                plagueDoctorWhiteRect.centerx = step
                plagueDoctorWhiteRect.centery = step
            if hadesBlackRect.colliderect(archbishopWhiteRect):
                archbishopWhiteRect.centerx = step*2
                plagueDoctorWhiteRect.centery = step
            if hadesBlackRect.colliderect(cardinalWhiteRect):
                cardinalWhiteRect.centerx = step*3
                cardinalWhiteRect.centery = step
            if hadesBlackRect.colliderect(hadesWhiteRect):
                hadesWhiteRect.centerx = step
                hadesWhiteRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if hadesBlackRect.colliderect(persephoneWhiteRect):
                persephoneWhiteRect.centerx = step*2
                persephoneWhiteRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user2_win=True
            if hadesBlackRect.colliderect(cardinalWhiteRect1):
                cardinalWhiteRect1.centerx = step*3
                cardinalWhiteRect1.centery = step*2
            if hadesBlackRect.colliderect(archbishopWhiteRect1):
                archbishopWhiteRect1.centerx = step
                archbishopWhiteRect1.centery = step*3
            if hadesBlackRect.colliderect(plagueDoctorWhiteRect1):
                plagueDoctorWhiteRect1.centerx = step*2
                plagueDoctorWhiteRect1.centery = step*3
            if hadesBlackRect.colliderect(legionaryWhiteRect):
                legionaryWhiteRect.centerx = step*3
                legionaryWhiteRect.centery = step*3
            if hadesBlackRect.colliderect(warriorWhiteRect):
                warriorWhiteRect.centerx = step
                warriorWhiteRect.centery = step*4
            if hadesBlackRect.colliderect(legionaryWhiteRect1):
                legionaryWhiteRect1.centerx = step*2
                legionaryWhiteRect1.centery = step*4
            if hadesBlackRect.colliderect(warriorWhiteRect1):
                warriorWhiteRect1.centerx = step*3
                warriorWhiteRect1.centery = step*4
            if hadesBlackRect.colliderect(legionaryWhiteRect2):
                legionaryWhiteRect2.centerx = step
                legionaryWhiteRect2.centery = step*5
            if hadesBlackRect.colliderect(warriorWhiteRect2):
                warriorWhiteRect2.centerx = step*2
                warriorWhiteRect2.centery = step*5
            if hadesBlackRect.colliderect(legionaryWhiteRect3):
                legionaryWhiteRect3.centerx = step*3
                legionaryWhiteRect3.centery = step*5
            if hadesBlackRect.colliderect(warriorWhiteRect3):
                warriorWhiteRect3.centerx = step
                warriorWhiteRect3.centery = step*6
            if hadesBlackRect.colliderect(cardinalWhiteRectCopy):
                cardinalWhiteRectCopy.centerx=step*2
                cardinalWhiteRectCopy.centery=step*6
            if hadesBlackRect.colliderect(cardinalWhiteRectCopy_1):
                cardinalWhiteRectCopy_1.centerx=step*3
                cardinalWhiteRectCopy_1.centery=step*6

            if persephoneBlackRect.colliderect(plagueDoctorWhiteRect):
                plagueDoctorWhiteRect.centerx = step
                plagueDoctorWhiteRect.centery = step
            if persephoneBlackRect.colliderect(archbishopWhiteRect):
                archbishopWhiteRect.centerx = step*2
                plagueDoctorWhiteRect.centery = step
            if persephoneBlackRect.colliderect(cardinalWhiteRect):
                cardinalWhiteRect.centerx = step*3
                cardinalWhiteRect.centery = step
            if persephoneBlackRect.colliderect(hadesWhiteRect):
                hadesWhiteRect.centerx = step
                hadesWhiteRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if persephoneBlackRect.colliderect(persephoneWhiteRect):
                persephoneWhiteRect.centerx = step*2
                persephoneWhiteRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user2_win=True
            if persephoneBlackRect.colliderect(cardinalWhiteRect1):
                cardinalWhiteRect1.centerx = step*3
                cardinalWhiteRect1.centery = step*2
            if persephoneBlackRect.colliderect(archbishopWhiteRect1):
                archbishopWhiteRect1.centerx = step
                archbishopWhiteRect1.centery = step*3
            if persephoneBlackRect.colliderect(plagueDoctorWhiteRect1):
                plagueDoctorWhiteRect1.centerx = step*2
                plagueDoctorWhiteRect1.centery = step*3
            if persephoneBlackRect.colliderect(legionaryWhiteRect):
                legionaryWhiteRect.centerx = step*3
                legionaryWhiteRect.centery = step*3
            if persephoneBlackRect.colliderect(warriorWhiteRect):
                warriorWhiteRect.centerx = step
                warriorWhiteRect.centery = step*4
            if persephoneBlackRect.colliderect(legionaryWhiteRect1):
                legionaryWhiteRect1.centerx = step*2
                legionaryWhiteRect1.centery = step*4
            if persephoneBlackRect.colliderect(warriorWhiteRect1):
                warriorWhiteRect1.centerx = step*3
                warriorWhiteRect1.centery = step*4
            if persephoneBlackRect.colliderect(legionaryWhiteRect2):
                legionaryWhiteRect2.centerx = step
                legionaryWhiteRect2.centery = step*5
            if persephoneBlackRect.colliderect(warriorWhiteRect2):
                warriorWhiteRect2.centerx = step*2
                warriorWhiteRect2.centery = step*5
            if persephoneBlackRect.colliderect(legionaryWhiteRect3):
                legionaryWhiteRect3.centerx = step*3
                legionaryWhiteRect3.centery = step*5
            if persephoneBlackRect.colliderect(warriorWhiteRect3):
                warriorWhiteRect3.centerx = step
                warriorWhiteRect3.centery = step*6
            if persephoneBlackRect.colliderect(cardinalWhiteRectCopy):
                cardinalWhiteRectCopy.centerx=step*2
                cardinalWhiteRectCopy.centery=step*6
            if persephoneBlackRect.colliderect(cardinalWhiteRectCopy_1):
                cardinalWhiteRectCopy_1.centerx=step*3
                cardinalWhiteRectCopy_1.centery=step*6

            if cardinalBlackRect1.colliderect(plagueDoctorWhiteRect):
                plagueDoctorWhiteRect.centerx = step
                plagueDoctorWhiteRect.centery = step
            if cardinalBlackRect1.colliderect(archbishopWhiteRect):
                archbishopWhiteRect.centerx = step*2
                plagueDoctorWhiteRect.centery = step
            if cardinalBlackRect1.colliderect(cardinalWhiteRect):
                cardinalWhiteRect.centerx = step*3
                cardinalWhiteRect.centery = step
            if cardinalBlackRect1.colliderect(hadesWhiteRect):
                hadesWhiteRect.centerx = step
                hadesWhiteRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if cardinalBlackRect1.colliderect(persephoneWhiteRect):
                persephoneWhiteRect.centerx = step*2
                persephoneWhiteRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user2_win=True
            if cardinalBlackRect1.colliderect(cardinalWhiteRect1):
                cardinalWhiteRect1.centerx = step*3
                cardinalWhiteRect1.centery = step*2
            if cardinalBlackRect1.colliderect(archbishopWhiteRect1):
                archbishopWhiteRect1.centerx = step
                archbishopWhiteRect1.centery = step*3
            if cardinalBlackRect1.colliderect(plagueDoctorWhiteRect1):
                plagueDoctorWhiteRect1.centerx = step*2
                plagueDoctorWhiteRect1.centery = step*3
            if cardinalBlackRect1.colliderect(legionaryWhiteRect):
                legionaryWhiteRect.centerx = step*3
                legionaryWhiteRect.centery = step*3
            if cardinalBlackRect1.colliderect(warriorWhiteRect):
                warriorWhiteRect.centerx = step
                warriorWhiteRect.centery = step*4
            if cardinalBlackRect1.colliderect(legionaryWhiteRect1):
                legionaryWhiteRect1.centerx = step*2
                legionaryWhiteRect1.centery = step*4
            if cardinalBlackRect1.colliderect(warriorWhiteRect1):
                warriorWhiteRect1.centerx = step*3
                warriorWhiteRect1.centery = step*4
            if cardinalBlackRect1.colliderect(legionaryWhiteRect2):
                legionaryWhiteRect2.centerx = step
                legionaryWhiteRect2.centery = step*5
            if cardinalBlackRect1.colliderect(warriorWhiteRect2):
                warriorWhiteRect2.centerx = step*2
                warriorWhiteRect2.centery = step*5
            if cardinalBlackRect1.colliderect(legionaryWhiteRect3):
                legionaryWhiteRect3.centerx = step*3
                legionaryWhiteRect3.centery = step*5
            if cardinalBlackRect1.colliderect(warriorWhiteRect3):
                warriorWhiteRect3.centerx = step
                warriorWhiteRect3.centery = step*6
            if cardinalBlackRect1.colliderect(cardinalWhiteRectCopy):
                cardinalWhiteRectCopy.centerx=step*2
                cardinalWhiteRectCopy.centery=step*6
            if cardinalBlackRect1.colliderect(cardinalWhiteRectCopy_1):
                cardinalWhiteRectCopy_1.centerx=step*3
                cardinalWhiteRectCopy_1.centery=step*6

            if archbishopBlackRect1.colliderect(plagueDoctorWhiteRect):
                plagueDoctorWhiteRect.centerx = step
                plagueDoctorWhiteRect.centery = step
                archbishopBlackFiguresCount_1+=1
            if archbishopBlackRect1.colliderect(archbishopWhiteRect):
                archbishopWhiteRect.centerx = step*2
                plagueDoctorWhiteRect.centery = step
                archbishopBlackFiguresCount_1+=1
            if archbishopBlackRect1.colliderect(cardinalWhiteRect):
                cardinalWhiteRect.centerx = step*3
                cardinalWhiteRect.centery = step
                archbishopBlackFiguresCount_1+=1
            if archbishopBlackRect1.colliderect(hadesWhiteRect):
                hadesWhiteRect.centerx = step
                hadesWhiteRect.centery = step*2
                archbishopBlackFiguresCount_1+=1
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if archbishopBlackRect1.colliderect(persephoneWhiteRect):
                persephoneWhiteRect.centerx = step*2
                persephoneWhiteRect.centery = step*2
                archbishopBlackFiguresCount_1+=1
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user2_win=True
            if archbishopBlackRect1.colliderect(cardinalWhiteRect1):
                cardinalWhiteRect1.centerx = step*3
                cardinalWhiteRect1.centery = step*2
                archbishopBlackFiguresCount_1+=1
            if archbishopBlackRect1.colliderect(archbishopWhiteRect1):
                archbishopWhiteRect1.centerx = step
                archbishopWhiteRect1.centery = step*3
                archbishopBlackFiguresCount_1+=1
            if archbishopBlackRect1.colliderect(plagueDoctorWhiteRect1):
                plagueDoctorWhiteRect1.centerx = step*2
                plagueDoctorWhiteRect1.centery = step*3
                archbishopBlackFiguresCount_1+=1
            if archbishopBlackRect1.colliderect(legionaryWhiteRect):
                legionaryWhiteRect.centerx = step*3
                legionaryWhiteRect.centery = step*3
                archbishopBlackFiguresCount_1+=1
            if archbishopBlackRect1.colliderect(warriorWhiteRect):
                warriorWhiteRect.centerx = step
                warriorWhiteRect.centery = step*4
                archbishopBlackFiguresCount_1+=1
            if archbishopBlackRect1.colliderect(legionaryWhiteRect1):
                legionaryWhiteRect1.centerx = step*2
                legionaryWhiteRect1.centery = step*4
                archbishopBlackFiguresCount_1+=1
            if archbishopBlackRect1.colliderect(warriorWhiteRect1):
                warriorWhiteRect1.centerx = step*3
                warriorWhiteRect1.centery = step*4
                archbishopBlackFiguresCount_1+=1
            if archbishopBlackRect1.colliderect(legionaryWhiteRect2):
                legionaryWhiteRect2.centerx = step
                legionaryWhiteRect2.centery = step*5
                archbishopBlackFiguresCount_1+=1
            if archbishopBlackRect1.colliderect(warriorWhiteRect2):
                warriorWhiteRect2.centerx = step*2
                warriorWhiteRect2.centery = step*5
                archbishopBlackFiguresCount_1+=1
            if archbishopBlackRect1.colliderect(legionaryWhiteRect3):
                legionaryWhiteRect3.centerx = step*3
                legionaryWhiteRect3.centery = step*5
                archbishopBlackFiguresCount_1+=1
            if archbishopBlackRect1.colliderect(warriorWhiteRect3):
                warriorWhiteRect3.centerx = step
                warriorWhiteRect3.centery = step*6
                archbishopBlackFiguresCount_1+=1
            if archbishopBlackRect1.colliderect(cardinalWhiteRectCopy):
                cardinalWhiteRectCopy.centerx=step*2
                cardinalWhiteRectCopy.centery=step*6
                archbishopBlackFiguresCount_1+=1
            if archbishopBlackRect1.colliderect(cardinalWhiteRectCopy_1):
                cardinalWhiteRectCopy_1.centerx=step*3
                cardinalWhiteRectCopy_1.centery=step*6
                archbishopBlackFiguresCount_1+=1

            if plagueDoctorBlackRect1.colliderect(plagueDoctorWhiteRect):
                plagueDoctorWhiteRect.centerx = step
                plagueDoctorWhiteRect.centery = step
            if plagueDoctorBlackRect1.colliderect(archbishopWhiteRect):
                archbishopWhiteRect.centerx = step*2
                plagueDoctorWhiteRect.centery = step
            if plagueDoctorBlackRect1.colliderect(cardinalWhiteRect):
                cardinalWhiteRect.centerx = step*3
                cardinalWhiteRect.centery = step
            if plagueDoctorBlackRect1.colliderect(hadesWhiteRect):
                hadesWhiteRect.centerx = step
                hadesWhiteRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if plagueDoctorBlackRect1.colliderect(persephoneWhiteRect):
                persephoneWhiteRect.centerx = step*2
                persephoneWhiteRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user2_win=True
            if plagueDoctorBlackRect1.colliderect(cardinalWhiteRect1):
                cardinalWhiteRect1.centerx = step*3
                cardinalWhiteRect1.centery = step*2
            if plagueDoctorBlackRect1.colliderect(archbishopWhiteRect1):
                archbishopWhiteRect1.centerx = step
                archbishopWhiteRect1.centery = step*3
            if plagueDoctorBlackRect1.colliderect(plagueDoctorWhiteRect1):
                plagueDoctorWhiteRect1.centerx = step*2
                plagueDoctorWhiteRect1.centery = step*3
            if plagueDoctorBlackRect1.colliderect(legionaryWhiteRect):
                legionaryWhiteRect.centerx = step*3
                legionaryWhiteRect.centery = step*3
            if plagueDoctorBlackRect1.colliderect(warriorWhiteRect):
                warriorWhiteRect.centerx = step
                warriorWhiteRect.centery = step*4
            if plagueDoctorBlackRect1.colliderect(legionaryWhiteRect1):
                legionaryWhiteRect1.centerx = step*2
                legionaryWhiteRect1.centery = step*4
            if plagueDoctorBlackRect1.colliderect(warriorWhiteRect1):
                warriorWhiteRect1.centerx = step*3
                warriorWhiteRect1.centery = step*4
            if plagueDoctorBlackRect1.colliderect(legionaryWhiteRect2):
                legionaryWhiteRect2.centerx = step
                legionaryWhiteRect2.centery = step*5
            if plagueDoctorBlackRect1.colliderect(warriorWhiteRect2):
                warriorWhiteRect2.centerx = step*2
                warriorWhiteRect2.centery = step*5
            if plagueDoctorBlackRect1.colliderect(legionaryWhiteRect3):
                legionaryWhiteRect3.centerx = step*3
                legionaryWhiteRect3.centery = step*5
            if plagueDoctorBlackRect1.colliderect(warriorWhiteRect3):
                warriorWhiteRect3.centerx = step
                warriorWhiteRect3.centery = step*6
            if plagueDoctorBlackRect1.colliderect(cardinalWhiteRectCopy):
                cardinalWhiteRectCopy.centerx=step*2
                cardinalWhiteRectCopy.centery=step*6
            if plagueDoctorBlackRect1.colliderect(cardinalWhiteRectCopy_1):
                cardinalWhiteRectCopy_1.centerx=step*3
                cardinalWhiteRectCopy_1.centery=step*6

            if legionaryBlackRect.colliderect(plagueDoctorWhiteRect):
                plagueDoctorWhiteRect.centerx = step
                plagueDoctorWhiteRect.centery = step
            if legionaryBlackRect.colliderect(archbishopWhiteRect):
                archbishopWhiteRect.centerx = step*2
                plagueDoctorWhiteRect.centery = step
            if legionaryBlackRect.colliderect(cardinalWhiteRect):
                cardinalWhiteRect.centerx = step*3
                cardinalWhiteRect.centery = step
            if legionaryBlackRect.colliderect(hadesWhiteRect):
                hadesWhiteRect.centerx = step
                hadesWhiteRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if legionaryBlackRect.colliderect(persephoneWhiteRect):
                persephoneWhiteRect.centerx = step*2
                persephoneWhiteRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user2_win=True
            if legionaryBlackRect.colliderect(cardinalWhiteRect1):
                cardinalWhiteRect1.centerx = step*3
                cardinalWhiteRect1.centery = step*2
            if legionaryBlackRect.colliderect(archbishopWhiteRect1):
                archbishopWhiteRect1.centerx = step
                archbishopWhiteRect1.centery = step*3
            if legionaryBlackRect.colliderect(plagueDoctorWhiteRect1):
                plagueDoctorWhiteRect1.centerx = step*2
                plagueDoctorWhiteRect1.centery = step*3
            if legionaryBlackRect.colliderect(legionaryWhiteRect):
                legionaryWhiteRect.centerx = step*3
                legionaryWhiteRect.centery = step*3
            if legionaryBlackRect.colliderect(warriorWhiteRect):
                warriorWhiteRect.centerx = step
                warriorWhiteRect.centery = step*4
            if legionaryBlackRect.colliderect(legionaryWhiteRect1):
                legionaryWhiteRect1.centerx = step*2
                legionaryWhiteRect1.centery = step*4
            if legionaryBlackRect.colliderect(warriorWhiteRect1):
                warriorWhiteRect1.centerx = step*3
                warriorWhiteRect1.centery = step*4
            if legionaryBlackRect.colliderect(legionaryWhiteRect2):
                legionaryWhiteRect2.centerx = step
                legionaryWhiteRect2.centery = step*5
            if legionaryBlackRect.colliderect(warriorWhiteRect2):
                warriorWhiteRect2.centerx = step*2
                warriorWhiteRect2.centery = step*5
            if legionaryBlackRect.colliderect(legionaryWhiteRect3):
                legionaryWhiteRect3.centerx = step*3
                legionaryWhiteRect3.centery = step*5
            if legionaryBlackRect.colliderect(warriorWhiteRect3):
                warriorWhiteRect3.centerx = step
                warriorWhiteRect3.centery = step*6
            if legionaryBlackRect.colliderect(cardinalWhiteRectCopy):
                cardinalWhiteRectCopy.centerx=step*2
                cardinalWhiteRectCopy.centery=step*6
            if legionaryBlackRect.colliderect(cardinalWhiteRectCopy_1):
                cardinalWhiteRectCopy_1.centerx=step*3
                cardinalWhiteRectCopy_1.centery=step*6

            if warriorBlackRect.colliderect(plagueDoctorWhiteRect):
                plagueDoctorWhiteRect.centerx = step
                plagueDoctorWhiteRect.centery = step
            if warriorBlackRect.colliderect(archbishopWhiteRect):
                archbishopWhiteRect.centerx = step*2
                plagueDoctorWhiteRect.centery = step
            if warriorBlackRect.colliderect(cardinalWhiteRect):
                cardinalWhiteRect.centerx = step*3
                cardinalWhiteRect.centery = step
            if warriorBlackRect.colliderect(hadesWhiteRect):
                hadesWhiteRect.centerx = step
                hadesWhiteRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if warriorBlackRect.colliderect(persephoneWhiteRect):
                persephoneWhiteRect.centerx = step*2
                persephoneWhiteRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user2_win=True
            if warriorBlackRect.colliderect(cardinalWhiteRect1):
                cardinalWhiteRect1.centerx = step*3
                cardinalWhiteRect1.centery = step*2
            if warriorBlackRect.colliderect(archbishopWhiteRect1):
                archbishopWhiteRect1.centerx = step
                archbishopWhiteRect1.centery = step*3
            if warriorBlackRect.colliderect(plagueDoctorWhiteRect1):
                plagueDoctorWhiteRect1.centerx = step*2
                plagueDoctorWhiteRect1.centery = step*3
            if warriorBlackRect.colliderect(legionaryWhiteRect):
                legionaryWhiteRect.centerx = step*3
                legionaryWhiteRect.centery = step*3
            if warriorBlackRect.colliderect(warriorWhiteRect):
                warriorWhiteRect.centerx = step
                warriorWhiteRect.centery = step*4
            if warriorBlackRect.colliderect(legionaryWhiteRect1):
                legionaryWhiteRect1.centerx = step*2
                legionaryWhiteRect1.centery = step*4
            if warriorBlackRect.colliderect(warriorWhiteRect1):
                warriorWhiteRect1.centerx = step*3
                warriorWhiteRect1.centery = step*4
            if warriorBlackRect.colliderect(legionaryWhiteRect2):
                legionaryWhiteRect2.centerx = step
                legionaryWhiteRect2.centery = step*5
            if warriorBlackRect.colliderect(warriorWhiteRect2):
                warriorWhiteRect2.centerx = step*2
                warriorWhiteRect2.centery = step*5
            if warriorBlackRect.colliderect(legionaryWhiteRect3):
                legionaryWhiteRect3.centerx = step*3
                legionaryWhiteRect3.centery = step*5
            if warriorBlackRect.colliderect(warriorWhiteRect3):
                warriorWhiteRect3.centerx = step
                warriorWhiteRect3.centery = step*6
            if warriorBlackRect.colliderect(cardinalWhiteRectCopy):
                cardinalWhiteRectCopy.centerx=step*2
                cardinalWhiteRectCopy.centery=step*6
            if warriorBlackRect.colliderect(cardinalWhiteRectCopy_1):
                cardinalWhiteRectCopy_1.centerx=step*3
                cardinalWhiteRectCopy_1.centery=step*6

            if legionaryBlackRect1.colliderect(plagueDoctorWhiteRect):
                plagueDoctorWhiteRect.centerx = step
                plagueDoctorWhiteRect.centery = step
            if legionaryBlackRect1.colliderect(archbishopWhiteRect):
                archbishopWhiteRect.centerx = step*2
                plagueDoctorWhiteRect.centery = step
            if legionaryBlackRect1.colliderect(cardinalWhiteRect):
                cardinalWhiteRect.centerx = step*3
                cardinalWhiteRect.centery = step
            if legionaryBlackRect1.colliderect(hadesWhiteRect):
                hadesWhiteRect.centerx = step
                hadesWhiteRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if legionaryBlackRect1.colliderect(persephoneWhiteRect):
                persephoneWhiteRect.centerx = step*2
                persephoneWhiteRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user2_win=True
            if legionaryBlackRect1.colliderect(cardinalWhiteRect1):
                cardinalWhiteRect1.centerx = step*3
                cardinalWhiteRect1.centery = step*2
            if legionaryBlackRect1.colliderect(archbishopWhiteRect1):
                archbishopWhiteRect1.centerx = step
                archbishopWhiteRect1.centery = step*3
            if legionaryBlackRect1.colliderect(plagueDoctorWhiteRect1):
                plagueDoctorWhiteRect1.centerx = step*2
                plagueDoctorWhiteRect1.centery = step*3
            if legionaryBlackRect1.colliderect(legionaryWhiteRect):
                legionaryWhiteRect.centerx = step*3
                legionaryWhiteRect.centery = step*3
            if legionaryBlackRect1.colliderect(warriorWhiteRect):
                warriorWhiteRect.centerx = step
                warriorWhiteRect.centery = step*4
            if legionaryBlackRect1.colliderect(legionaryWhiteRect1):
                legionaryWhiteRect1.centerx = step*2
                legionaryWhiteRect1.centery = step*4
            if legionaryBlackRect1.colliderect(warriorWhiteRect1):
                warriorWhiteRect1.centerx = step*3
                warriorWhiteRect1.centery = step*4
            if legionaryBlackRect1.colliderect(legionaryWhiteRect2):
                legionaryWhiteRect2.centerx = step
                legionaryWhiteRect2.centery = step*5
            if legionaryBlackRect1.colliderect(warriorWhiteRect2):
                warriorWhiteRect2.centerx = step*2
                warriorWhiteRect2.centery = step*5
            if legionaryBlackRect1.colliderect(legionaryWhiteRect3):
                legionaryWhiteRect3.centerx = step*3
                legionaryWhiteRect3.centery = step*5
            if legionaryBlackRect1.colliderect(warriorWhiteRect3):
                warriorWhiteRect3.centerx = step
                warriorWhiteRect3.centery = step*6
            if legionaryBlackRect1.colliderect(cardinalWhiteRectCopy):
                cardinalWhiteRectCopy.centerx=step*2
                cardinalWhiteRectCopy.centery=step*6
            if legionaryBlackRect1.colliderect(cardinalWhiteRectCopy_1):
                cardinalWhiteRectCopy_1.centerx=step*3
                cardinalWhiteRectCopy_1.centery=step*6

            if warriorBlackRect1.colliderect(plagueDoctorWhiteRect):
                plagueDoctorWhiteRect.centerx = step
                plagueDoctorWhiteRect.centery = step
            if warriorBlackRect1.colliderect(archbishopWhiteRect):
                archbishopWhiteRect.centerx = step*2
                plagueDoctorWhiteRect.centery = step
            if warriorBlackRect1.colliderect(cardinalWhiteRect):
                cardinalWhiteRect.centerx = step*3
                cardinalWhiteRect.centery = step
            if warriorBlackRect1.colliderect(hadesWhiteRect):
                hadesWhiteRect.centerx = step
                hadesWhiteRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if warriorBlackRect1.colliderect(persephoneWhiteRect):
                persephoneWhiteRect.centerx = step*2
                persephoneWhiteRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user2_win=True
            if warriorBlackRect1.colliderect(cardinalWhiteRect1):
                cardinalWhiteRect1.centerx = step*3
                cardinalWhiteRect1.centery = step*2
            if warriorBlackRect1.colliderect(archbishopWhiteRect1):
                archbishopWhiteRect1.centerx = step
                archbishopWhiteRect1.centery = step*3
            if warriorBlackRect1.colliderect(plagueDoctorWhiteRect1):
                plagueDoctorWhiteRect1.centerx = step*2
                plagueDoctorWhiteRect1.centery = step*3
            if warriorBlackRect1.colliderect(legionaryWhiteRect):
                legionaryWhiteRect.centerx = step*3
                legionaryWhiteRect.centery = step*3
            if warriorBlackRect1.colliderect(warriorWhiteRect):
                warriorWhiteRect.centerx = step
                warriorWhiteRect.centery = step*4
            if warriorBlackRect1.colliderect(legionaryWhiteRect1):
                legionaryWhiteRect1.centerx = step*2
                legionaryWhiteRect1.centery = step*4
            if warriorBlackRect1.colliderect(warriorWhiteRect1):
                warriorWhiteRect1.centerx = step*3
                warriorWhiteRect1.centery = step*4
            if warriorBlackRect1.colliderect(legionaryWhiteRect2):
                legionaryWhiteRect2.centerx = step
                legionaryWhiteRect2.centery = step*5
            if warriorBlackRect1.colliderect(warriorWhiteRect2):
                warriorWhiteRect2.centerx = step*2
                warriorWhiteRect2.centery = step*5
            if warriorBlackRect1.colliderect(legionaryWhiteRect3):
                legionaryWhiteRect3.centerx = step*3
                legionaryWhiteRect3.centery = step*5
            if warriorBlackRect1.colliderect(warriorWhiteRect3):
                warriorWhiteRect3.centerx = step
                warriorWhiteRect3.centery = step*6
            if warriorBlackRect1.colliderect(cardinalWhiteRectCopy):
                cardinalWhiteRectCopy.centerx=step*2
                cardinalWhiteRectCopy.centery=step*6
            if warriorBlackRect1.colliderect(cardinalWhiteRectCopy_1):
                cardinalWhiteRectCopy_1.centerx=step*3
                cardinalWhiteRectCopy_1.centery=step*6


            if legionaryBlackRect2.colliderect(plagueDoctorWhiteRect):
                plagueDoctorWhiteRect.centerx = step
                plagueDoctorWhiteRect.centery = step
            if legionaryBlackRect2.colliderect(archbishopWhiteRect):
                archbishopWhiteRect.centerx = step*2
                plagueDoctorWhiteRect.centery = step
            if legionaryBlackRect2.colliderect(cardinalWhiteRect):
                cardinalWhiteRect.centerx = step*3
                cardinalWhiteRect.centery = step
            if legionaryBlackRect2.colliderect(hadesWhiteRect):
                hadesWhiteRect.centerx = step
                hadesWhiteRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if legionaryBlackRect2.colliderect(persephoneWhiteRect):
                persephoneWhiteRect.centerx = step*2
                persephoneWhiteRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user2_win=True
            if legionaryBlackRect2.colliderect(cardinalWhiteRect1):
                cardinalWhiteRect1.centerx = step*3
                cardinalWhiteRect1.centery = step*2
            if legionaryBlackRect2.colliderect(archbishopWhiteRect1):
                archbishopWhiteRect1.centerx = step
                archbishopWhiteRect1.centery = step*3
            if legionaryBlackRect2.colliderect(plagueDoctorWhiteRect1):
                plagueDoctorWhiteRect1.centerx = step*2
                plagueDoctorWhiteRect1.centery = step*3
            if legionaryBlackRect2.colliderect(legionaryWhiteRect):
                legionaryWhiteRect.centerx = step*3
                legionaryWhiteRect.centery = step*3
            if legionaryBlackRect2.colliderect(warriorWhiteRect):
                warriorWhiteRect.centerx = step
                warriorWhiteRect.centery = step*4
            if legionaryBlackRect2.colliderect(legionaryWhiteRect1):
                legionaryWhiteRect1.centerx = step*2
                legionaryWhiteRect1.centery = step*4
            if legionaryBlackRect2.colliderect(warriorWhiteRect1):
                warriorWhiteRect1.centerx = step*3
                warriorWhiteRect1.centery = step*4
            if legionaryBlackRect2.colliderect(legionaryWhiteRect2):
                legionaryWhiteRect2.centerx = step
                legionaryWhiteRect2.centery = step*5
            if legionaryBlackRect2.colliderect(warriorWhiteRect2):
                warriorWhiteRect2.centerx = step*2
                warriorWhiteRect2.centery = step*5
            if legionaryBlackRect2.colliderect(legionaryWhiteRect3):
                legionaryWhiteRect3.centerx = step*3
                legionaryWhiteRect3.centery = step*5
            if legionaryBlackRect2.colliderect(warriorWhiteRect3):
                warriorWhiteRect3.centerx = step
                warriorWhiteRect3.centery = step*6
            if legionaryBlackRect2.colliderect(cardinalWhiteRectCopy):
                cardinalWhiteRectCopy.centerx=step*2
                cardinalWhiteRectCopy.centery=step*6
            if legionaryBlackRect2.colliderect(cardinalWhiteRectCopy_1):
                cardinalWhiteRectCopy_1.centerx=step*3
                cardinalWhiteRectCopy_1.centery=step*6

            if warriorBlackRect2.colliderect(plagueDoctorWhiteRect):
                plagueDoctorWhiteRect.centerx = step
                plagueDoctorWhiteRect.centery = step
            if warriorBlackRect2.colliderect(archbishopWhiteRect):
                archbishopWhiteRect.centerx = step*2
                plagueDoctorWhiteRect.centery = step
            if warriorBlackRect2.colliderect(cardinalWhiteRect):
                cardinalWhiteRect.centerx = step*3
                cardinalWhiteRect.centery = step
            if warriorBlackRect2.colliderect(hadesWhiteRect):
                hadesWhiteRect.centerx = step
                hadesWhiteRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if warriorBlackRect2.colliderect(persephoneWhiteRect):
                persephoneWhiteRect.centerx = step*2
                persephoneWhiteRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user2_win=True
            if warriorBlackRect2.colliderect(cardinalWhiteRect1):
                cardinalWhiteRect1.centerx = step*3
                cardinalWhiteRect1.centery = step*2
            if warriorBlackRect2.colliderect(archbishopWhiteRect1):
                archbishopWhiteRect1.centerx = step
                archbishopWhiteRect1.centery = step*3
            if warriorBlackRect2.colliderect(plagueDoctorWhiteRect1):
                plagueDoctorWhiteRect1.centerx = step*2
                plagueDoctorWhiteRect1.centery = step*3
            if warriorBlackRect2.colliderect(legionaryWhiteRect):
                legionaryWhiteRect.centerx = step*3
                legionaryWhiteRect.centery = step*3
            if warriorBlackRect2.colliderect(warriorWhiteRect):
                warriorWhiteRect.centerx = step
                warriorWhiteRect.centery = step*4
            if warriorBlackRect2.colliderect(legionaryWhiteRect1):
                legionaryWhiteRect1.centerx = step*2
                legionaryWhiteRect1.centery = step*4
            if warriorBlackRect2.colliderect(warriorWhiteRect1):
                warriorWhiteRect1.centerx = step*3
                warriorWhiteRect1.centery = step*4
            if warriorBlackRect2.colliderect(legionaryWhiteRect2):
                legionaryWhiteRect2.centerx = step
                legionaryWhiteRect2.centery = step*5
            if warriorBlackRect2.colliderect(warriorWhiteRect2):
                warriorWhiteRect2.centerx = step*2
                warriorWhiteRect2.centery = step*5
            if warriorBlackRect2.colliderect(legionaryWhiteRect3):
                legionaryWhiteRect3.centerx = step*3
                legionaryWhiteRect3.centery = step*5
            if warriorBlackRect2.colliderect(warriorWhiteRect3):
                warriorWhiteRect3.centerx = step
                warriorWhiteRect3.centery = step*6
            if warriorBlackRect2.colliderect(cardinalWhiteRectCopy):
                cardinalWhiteRectCopy.centerx=step*2
                cardinalWhiteRectCopy.centery=step*6
            if warriorBlackRect2.colliderect(cardinalWhiteRectCopy_1):
                cardinalWhiteRectCopy_1.centerx=step*3
                cardinalWhiteRectCopy_1.centery=step*6

            if legionaryBlackRect3.colliderect(plagueDoctorWhiteRect):
                plagueDoctorWhiteRect.centerx = step
                plagueDoctorWhiteRect.centery = step
            if legionaryBlackRect3.colliderect(archbishopWhiteRect):
                archbishopWhiteRect.centerx = step*2
                plagueDoctorWhiteRect.centery = step
            if legionaryBlackRect3.colliderect(cardinalWhiteRect):
                cardinalWhiteRect.centerx = step*3
                cardinalWhiteRect.centery = step
            if legionaryBlackRect3.colliderect(hadesWhiteRect):
                hadesWhiteRect.centerx = step
                hadesWhiteRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if legionaryBlackRect3.colliderect(persephoneWhiteRect):
                persephoneWhiteRect.centerx = step*2
                persephoneWhiteRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user2_win=True
            if legionaryBlackRect3.colliderect(cardinalWhiteRect1):
                cardinalWhiteRect1.centerx = step*3
                cardinalWhiteRect1.centery = step*2
            if legionaryBlackRect3.colliderect(archbishopWhiteRect1):
                archbishopWhiteRect1.centerx = step
                archbishopWhiteRect1.centery = step*3
            if legionaryBlackRect3.colliderect(plagueDoctorWhiteRect1):
                plagueDoctorWhiteRect1.centerx = step*2
                plagueDoctorWhiteRect1.centery = step*3
            if legionaryBlackRect3.colliderect(legionaryWhiteRect):
                legionaryWhiteRect.centerx = step*3
                legionaryWhiteRect.centery = step*3
            if legionaryBlackRect3.colliderect(warriorWhiteRect):
                warriorWhiteRect.centerx = step
                warriorWhiteRect.centery = step*4
            if legionaryBlackRect3.colliderect(legionaryWhiteRect1):
                legionaryWhiteRect1.centerx = step*2
                legionaryWhiteRect1.centery = step*4
            if legionaryBlackRect3.colliderect(warriorWhiteRect1):
                warriorWhiteRect1.centerx = step*3
                warriorWhiteRect1.centery = step*4
            if legionaryBlackRect3.colliderect(legionaryWhiteRect2):
                legionaryWhiteRect2.centerx = step
                legionaryWhiteRect2.centery = step*5
            if legionaryBlackRect3.colliderect(warriorWhiteRect2):
                warriorWhiteRect2.centerx = step*2
                warriorWhiteRect2.centery = step*5
            if legionaryBlackRect3.colliderect(legionaryWhiteRect3):
                legionaryWhiteRect3.centerx = step*3
                legionaryWhiteRect3.centery = step*5
            if legionaryBlackRect3.colliderect(warriorWhiteRect3):
                warriorWhiteRect3.centerx = step
                warriorWhiteRect3.centery = step*6
            if legionaryBlackRect3.colliderect(cardinalWhiteRectCopy):
                cardinalWhiteRectCopy.centerx=step*2
                cardinalWhiteRectCopy.centery=step*6
            if legionaryBlackRect3.colliderect(cardinalWhiteRectCopy_1):
                cardinalWhiteRectCopy_1.centerx=step*3
                cardinalWhiteRectCopy_1.centery=step*6

            if warriorBlackRect3.colliderect(plagueDoctorWhiteRect):
                plagueDoctorWhiteRect.centerx = step
                plagueDoctorWhiteRect.centery = step
            if warriorBlackRect3.colliderect(archbishopWhiteRect):
                archbishopWhiteRect.centerx = step*2
                plagueDoctorWhiteRect.centery = step
            if warriorBlackRect3.colliderect(cardinalWhiteRect):
                cardinalWhiteRect.centerx = step*3
                cardinalWhiteRect.centery = step
            if warriorBlackRect3.colliderect(hadesWhiteRect):
                hadesWhiteRect.centerx = step
                hadesWhiteRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if warriorBlackRect3.colliderect(persephoneWhiteRect):
                persephoneWhiteRect.centerx = step*2
                persephoneWhiteRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user2_win=True
            if warriorBlackRect3.colliderect(cardinalWhiteRect1):
                cardinalWhiteRect1.centerx = step*3
                cardinalWhiteRect1.centery = step*2
            if warriorBlackRect3.colliderect(archbishopWhiteRect1):
                archbishopWhiteRect1.centerx = step
                archbishopWhiteRect1.centery = step*3
            if warriorBlackRect3.colliderect(plagueDoctorWhiteRect1):
                plagueDoctorWhiteRect1.centerx = step*2
                plagueDoctorWhiteRect1.centery = step*3
            if warriorBlackRect3.colliderect(legionaryWhiteRect):
                legionaryWhiteRect.centerx = step*3
                legionaryWhiteRect.centery = step*3
            if warriorBlackRect3.colliderect(warriorWhiteRect):
                warriorWhiteRect.centerx = step
                warriorWhiteRect.centery = step*4
            if warriorBlackRect3.colliderect(legionaryWhiteRect1):
                legionaryWhiteRect1.centerx = step*2
                legionaryWhiteRect1.centery = step*4
            if warriorBlackRect3.colliderect(warriorWhiteRect1):
                warriorWhiteRect1.centerx = step*3
                warriorWhiteRect1.centery = step*4
            if warriorBlackRect3.colliderect(legionaryWhiteRect2):
                legionaryWhiteRect2.centerx = step
                legionaryWhiteRect2.centery = step*5
            if warriorBlackRect3.colliderect(warriorWhiteRect2):
                warriorWhiteRect2.centerx = step*2
                warriorWhiteRect2.centery = step*5
            if warriorBlackRect3.colliderect(legionaryWhiteRect3):
                legionaryWhiteRect3.centerx = step*3
                legionaryWhiteRect3.centery = step*5
            if warriorBlackRect3.colliderect(warriorWhiteRect3):
                warriorWhiteRect3.centerx = step
                warriorWhiteRect3.centery = step*6
            if warriorBlackRect3.colliderect(cardinalWhiteRectCopy):
                cardinalWhiteRectCopy.centerx=step*2
                cardinalWhiteRectCopy.centery=step*6
            if warriorBlackRect3.colliderect(cardinalWhiteRectCopy_1):
                cardinalWhiteRectCopy_1.centerx=step*3
                cardinalWhiteRectCopy_1.centery=step*6
            
            if cardinalBlackRectCopy.colliderect(plagueDoctorWhiteRect):
                plagueDoctorWhiteRect.centerx = step
                plagueDoctorWhiteRect.centery = step
            if cardinalBlackRectCopy.colliderect(archbishopWhiteRect):
                archbishopWhiteRect.centerx = step*2
                plagueDoctorWhiteRect.centery = step
            if cardinalBlackRectCopy.colliderect(cardinalWhiteRect):
                cardinalWhiteRect.centerx = step*3
                cardinalWhiteRect.centery = step
            if cardinalBlackRectCopy.colliderect(hadesWhiteRect):
                hadesWhiteRect.centerx = step
                hadesWhiteRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if cardinalBlackRectCopy.colliderect(persephoneWhiteRect):
                persephoneWhiteRect.centerx = step*2
                persephoneWhiteRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user2_win=True
            if cardinalBlackRectCopy.colliderect(cardinalWhiteRect1):
                cardinalWhiteRect1.centerx = step*3
                cardinalWhiteRect1.centery = step*2
            if cardinalBlackRectCopy.colliderect(archbishopWhiteRect1):
                archbishopWhiteRect1.centerx = step
                archbishopWhiteRect1.centery = step*3
            if cardinalBlackRectCopy.colliderect(plagueDoctorWhiteRect1):
                plagueDoctorWhiteRect1.centerx = step*2
                plagueDoctorWhiteRect1.centery = step*3
            if cardinalBlackRectCopy.colliderect(legionaryWhiteRect):
                legionaryWhiteRect.centerx = step*3
                legionaryWhiteRect.centery = step*3
            if cardinalBlackRectCopy.colliderect(warriorWhiteRect):
                warriorWhiteRect.centerx = step
                warriorWhiteRect.centery = step*4
            if cardinalBlackRectCopy.colliderect(legionaryWhiteRect1):
                legionaryWhiteRect1.centerx = step*2
                legionaryWhiteRect1.centery = step*4
            if cardinalBlackRectCopy.colliderect(warriorWhiteRect1):
                warriorWhiteRect1.centerx = step*3
                warriorWhiteRect1.centery = step*4
            if cardinalBlackRectCopy.colliderect(legionaryWhiteRect2):
                legionaryWhiteRect2.centerx = step
                legionaryWhiteRect2.centery = step*5
            if cardinalBlackRectCopy.colliderect(warriorWhiteRect2):
                warriorWhiteRect2.centerx = step*2
                warriorWhiteRect2.centery = step*5
            if cardinalBlackRectCopy.colliderect(legionaryWhiteRect3):
                legionaryWhiteRect3.centerx = step*3
                legionaryWhiteRect3.centery = step*5
            if cardinalBlackRectCopy.colliderect(warriorWhiteRect3):
                warriorWhiteRect3.centerx = step
                warriorWhiteRect3.centery = step*6
            if cardinalBlackRectCopy.colliderect(cardinalWhiteRectCopy):
                cardinalWhiteRectCopy.centerx=step*2
                cardinalWhiteRectCopy.centery=step*6
            if cardinalBlackRectCopy.colliderect(cardinalWhiteRectCopy_1):
                cardinalWhiteRectCopy_1.centerx=step*3
                cardinalWhiteRectCopy_1.centery=step*6
            
            if cardinalBlackRectCopy_1.colliderect(plagueDoctorWhiteRect):
                plagueDoctorWhiteRect.centerx = step
                plagueDoctorWhiteRect.centery = step
            if cardinalBlackRectCopy_1.colliderect(archbishopWhiteRect):
                archbishopWhiteRect.centerx = step*2
                plagueDoctorWhiteRect.centery = step
            if cardinalBlackRectCopy_1.colliderect(cardinalWhiteRect):
                cardinalWhiteRect.centerx = step*3
                cardinalWhiteRect.centery = step
            if cardinalBlackRectCopy_1.colliderect(hadesWhiteRect):
                hadesWhiteRect.centerx = step
                hadesWhiteRect.centery = step*2
                if not late_game:
                    lateGameMusic.play()
                    late_game=True
            if cardinalBlackRectCopy_1.colliderect(persephoneWhiteRect):
                persephoneWhiteRect.centerx = step*2
                persephoneWhiteRect.centery = step*2
                play_game=False
                show_main_menu=True
                pygame.mixer.pause()
                song = random.choice(songs)
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(1, 0)
                user2_win=True
            if cardinalBlackRectCopy_1.colliderect(cardinalWhiteRect1):
                cardinalWhiteRect1.centerx = step*3
                cardinalWhiteRect1.centery = step*2
            if cardinalBlackRectCopy_1.colliderect(archbishopWhiteRect1):
                archbishopWhiteRect1.centerx = step
                archbishopWhiteRect1.centery = step*3
            if cardinalBlackRectCopy_1.colliderect(plagueDoctorWhiteRect1):
                plagueDoctorWhiteRect1.centerx = step*2
                plagueDoctorWhiteRect1.centery = step*3
            if cardinalBlackRectCopy_1.colliderect(legionaryWhiteRect):
                legionaryWhiteRect.centerx = step*3
                legionaryWhiteRect.centery = step*3
            if cardinalBlackRectCopy_1.colliderect(warriorWhiteRect):
                warriorWhiteRect.centerx = step
                warriorWhiteRect.centery = step*4
            if cardinalBlackRectCopy_1.colliderect(legionaryWhiteRect1):
                legionaryWhiteRect1.centerx = step*2
                legionaryWhiteRect1.centery = step*4
            if cardinalBlackRectCopy_1.colliderect(warriorWhiteRect1):
                warriorWhiteRect1.centerx = step*3
                warriorWhiteRect1.centery = step*4
            if cardinalBlackRectCopy_1.colliderect(legionaryWhiteRect2):
                legionaryWhiteRect2.centerx = step
                legionaryWhiteRect2.centery = step*5
            if cardinalBlackRectCopy_1.colliderect(warriorWhiteRect2):
                warriorWhiteRect2.centerx = step*2
                warriorWhiteRect2.centery = step*5
            if cardinalBlackRectCopy_1.colliderect(legionaryWhiteRect3):
                legionaryWhiteRect3.centerx = step*3
                legionaryWhiteRect3.centery = step*5
            if cardinalBlackRectCopy_1.colliderect(warriorWhiteRect3):
                warriorWhiteRect3.centerx = step
                warriorWhiteRect3.centery = step*6
            if cardinalBlackRectCopy_1.colliderect(cardinalWhiteRectCopy):
                cardinalWhiteRectCopy.centerx=step*2
                cardinalWhiteRectCopy.centery=step*6
            if cardinalBlackRectCopy_1.colliderect(cardinalWhiteRectCopy_1):
                cardinalWhiteRectCopy_1.centerx=step*3
                cardinalWhiteRectCopy_1.centery=step*6
        # Tažení figurek

        #Opětovné deklarování pozic čtverců pro pohyb figurek, aby zůstaly na místě a nepohybovaly se společně s figurkou při jejím pohybu
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
        rectCardinalWhite4_1 = pygame.Rect(rectCardinalWhitex4_1 - 30, rectCardinalWhitey4_1 - 30, 60, 60)
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

        #Legionář bílý 1 abilita
        #rectLegionaryWhitexAbility=legionaryWhiteRect.centerx
        #rectLegionaryWhiteyAbility=legionaryWhiteRect.centery

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

        #Legionář bílý 2 abilita
        #rectLegionaryWhitexAbility_1=legionaryWhiteRect1.centerx
        #rectLegionaryWhiteyAbility_1=legionaryWhiteRect1.centery

        #Válečník bílý 2
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

        #Legionář bílý 3 abilita
        #rectLegionaryWhitexAbility_2=legionaryWhiteRect2.centerx
        #rectLegionaryWhiteyAbility_2=legionaryWhiteRect2.centery
        
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

        #Legionář bílý 4 abilita
        #rectLegionaryWhitexAbility_3=legionaryWhiteRect3.centerx
        #rectLegionaryWhiteyAbilita_3=legionaryWhiteRect3.centery 

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
        rectPlagueBlack16_1 = pygame.Rect(rectPlagueBlackx16_1 - 30, rectPlagueBlacky16_1 - 30, 60, 60)
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
        rectsWarriorBlackAbility.append(rectWarriorBlack3Ability)

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

        #Kardinál bílý kopie pro abilitu
        rectsCardinalWhiteCopy=[]
        
        rectCardinalWhiteCopyx1=cardinalWhiteRectCopy.centerx+step
        rectCardinalWhiteCopyy1=cardinalWhiteRectCopy.centery+step
        rectCardinalWhiteCopy1=pygame.Rect(rectCardinalWhiteCopyx1-30,rectCardinalWhiteCopyy1-30,60,60)
        rectsCardinalWhiteCopy.append(rectCardinalWhiteCopy1)

        rectCardinalWhiteCopyx2=cardinalWhiteRectCopy.centerx-step
        rectCardinalWhiteCopyy2=cardinalWhiteRectCopy.centery+step
        rectCardinalWhiteCopy2=pygame.Rect(rectCardinalWhiteCopyx2-30,rectCardinalWhiteCopyy2-30,60,60)
        rectsCardinalWhiteCopy.append(rectCardinalWhiteCopy2)

        rectCardinalWhiteCopyx3=cardinalWhiteRectCopy.centerx+step
        rectCardinalWhiteCopyy3=cardinalWhiteRectCopy.centery-step
        rectCardinalWhiteCopy3=pygame.Rect(rectCardinalWhiteCopyx3-30,rectCardinalWhiteCopyy3-30,60,60)
        rectsCardinalWhiteCopy.append(rectCardinalWhiteCopy3)

        rectCardinalWhiteCopyx4=cardinalWhiteRectCopy.centerx-step
        rectCardinalWhiteCopyy4=cardinalWhiteRectCopy.centery-step
        rectCardinalWhiteCopy4=pygame.Rect(rectCardinalWhiteCopyx4-30,rectCardinalWhiteCopyy4-30,60,60)
        rectsCardinalWhiteCopy.append(rectCardinalWhiteCopy4)

        #Kardinál bílý kopie 1 pro abilitu
        rectsCardinalWhiteCopy_1=[]
        
        rectCardinalWhiteCopyx1_1=cardinalWhiteRectCopy_1.centerx+step
        rectCardinalWhiteCopyy1_1=cardinalWhiteRectCopy_1.centery+step
        rectCardinalWhiteCopy1_1=pygame.Rect(rectCardinalWhiteCopyx1_1-30,rectCardinalWhiteCopyy1_1-30,60,60)
        rectsCardinalWhiteCopy_1.append(rectCardinalWhiteCopy1_1)

        rectCardinalWhiteCopyx2_1=cardinalWhiteRectCopy_1.centerx-step
        rectCardinalWhiteCopyy2_1=cardinalWhiteRectCopy_1.centery+step
        rectCardinalWhiteCopy2_1=pygame.Rect(rectCardinalWhiteCopyx2_1-30,rectCardinalWhiteCopyy2_1-30,60,60)
        rectsCardinalWhiteCopy_1.append(rectCardinalWhiteCopy2_1)

        rectCardinalWhiteCopyx3_1=cardinalWhiteRectCopy_1.centerx+step
        rectCardinalWhiteCopyy3_1=cardinalWhiteRectCopy_1.centery-step
        rectCardinalWhiteCopy3_1=pygame.Rect(rectCardinalWhiteCopyx3_1-30,rectCardinalWhiteCopyy3_1-30,60,60)
        rectsCardinalWhiteCopy_1.append(rectCardinalWhiteCopy3_1)

        rectCardinalWhiteCopyx4_1=cardinalWhiteRectCopy_1.centerx-step
        rectCardinalWhiteCopyy4_1=cardinalWhiteRectCopy_1.centery-step
        rectCardinalWhiteCopy4_1=pygame.Rect(rectCardinalWhiteCopyx4_1-30,rectCardinalWhiteCopyy4_1-30,60,60)
        rectsCardinalWhiteCopy_1.append(rectCardinalWhiteCopy4_1)

        #Kardinál černý kopie pro abilitu
        rectsCardinalBlackCopy=[]

        rectCardinalBlackCopyx1=cardinalBlackRectCopy.centerx+step
        rectCardinalBlackCopyy1=cardinalBlackRectCopy.centery+step
        rectCardinalBlackCopy1=pygame.Rect(rectCardinalBlackCopyx1-30,rectCardinalBlackCopyy1-30,60,60)
        rectsCardinalBlackCopy.append(rectCardinalBlackCopy1)

        rectCardinalBlackCopyx2=cardinalBlackRectCopy.centerx-step
        rectCardinalBlackCopyy2=cardinalBlackRectCopy.centery+step
        rectCardinalBlackCopy2=pygame.Rect(rectCardinalBlackCopyx2-30,rectCardinalBlackCopyy2-30,60,60)
        rectsCardinalBlackCopy.append(rectCardinalBlackCopy2)

        rectCardinalBlackCopyx3=cardinalBlackRectCopy.centerx+step
        rectCardinalBlackCopyy3=cardinalBlackRectCopy.centery-step
        rectCardinalBlackCopy3=pygame.Rect(rectCardinalBlackCopyx3-30,rectCardinalBlackCopyy3-30,60,60)
        rectsCardinalBlackCopy.append(rectCardinalBlackCopy3)

        rectCardinalBlackCopyx4=cardinalBlackRectCopy.centerx-step
        rectCardinalBlackCopyy4=cardinalBlackRectCopy.centery-step
        rectCardinalBlackCopy4=pygame.Rect(rectCardinalBlackCopyx4-30,rectCardinalBlackCopyy4-30,60,60)
        rectsCardinalBlackCopy.append(rectCardinalBlackCopy4)

        #Kardinál černý kopie pro abilitu 1
        rectsCardinalBlackCopy_1=[]

        rectCardinalBlackCopyx1_1=cardinalBlackRectCopy_1.centerx+step
        rectCardinalBlackCopyy1_1=cardinalBlackRectCopy_1.centery+step
        rectCardinalBlackCopy1_1=pygame.Rect(rectCardinalBlackCopyx1_1-30,rectCardinalBlackCopyy1_1-30,60,60)
        rectsCardinalBlackCopy_1.append(rectCardinalBlackCopy1_1)

        rectCardinalBlackCopyx2_1=cardinalBlackRectCopy_1.centerx-step
        rectCardinalBlackCopyy2_1=cardinalBlackRectCopy_1.centery+step
        rectCardinalBlackCopy2_1=pygame.Rect(rectCardinalBlackCopyx2_1-30,rectCardinalBlackCopyy2_1-30,60,60)
        rectsCardinalBlackCopy_1.append(rectCardinalBlackCopy2_1)

        rectCardinalBlackCopyx3_1=cardinalBlackRectCopy_1.centerx+step
        rectCardinalBlackCopyy3_1=cardinalBlackRectCopy_1.centery-step
        rectCardinalBlackCopy3_1=pygame.Rect(rectCardinalBlackCopyx3_1-30,rectCardinalBlackCopyy3_1-30,60,60)
        rectsCardinalBlackCopy_1.append(rectCardinalBlackCopy3_1)

        rectCardinalBlackCopyx4_1=cardinalBlackRectCopy_1.centerx-step
        rectCardinalBlackCopyy4_1=cardinalBlackRectCopy_1.centery-step
        rectCardinalBlackCopy4_1=pygame.Rect(rectCardinalBlackCopyx4_1-30,rectCardinalBlackCopyy4_1-30,60,60)
        rectsCardinalBlackCopy_1.append(rectCardinalBlackCopy4_1)

        #Persefona černá abilita
        rectsPersephoneBlackAbility = []

        rectPersephoneBlackx1Ability = persephoneBlackRect.centerx + step
        rectPersephoneBlacky1Ability = persephoneBlackRect.centery
        rectPersephoneBlack1Ability = pygame.Rect(rectPersephoneBlackx1Ability - 30, rectPersephoneBlacky1Ability - 30, 60, 60)
        rectsPersephoneBlackAbility.append(rectPersephoneBlack1Ability)

        rectPersephoneBlackx2Ability = persephoneBlackRect.centerx + step * 2
        rectPersephoneBlacky2Ability = persephoneBlackRect.centery
        rectPersephoneBlack2Ability = pygame.Rect(rectPersephoneBlackx2Ability - 30, rectPersephoneBlacky2Ability - 30, 60, 60)
        rectsPersephoneBlackAbility.append(rectPersephoneBlack2Ability)

        rectPersephoneBlackx3Ability = persephoneBlackRect.centerx + step * 3
        rectPersephoneBlacky3Ability = persephoneBlackRect.centery
        rectPersephoneBlack3Ability = pygame.Rect(rectPersephoneBlackx3Ability - 30, rectPersephoneBlacky3Ability - 30, 60, 60)
        rectsPersephoneBlackAbility.append(rectPersephoneBlack3Ability)

        rectPersephoneBlackx4Ability = persephoneBlackRect.centerx - step
        rectPersephoneBlacky4Ability = persephoneBlackRect.centery
        rectPersephoneBlack4Ability = pygame.Rect(rectPersephoneBlackx4Ability - 30, rectPersephoneBlacky4Ability - 30, 60, 60)
        rectsPersephoneBlackAbility.append(rectPersephoneBlack4Ability)

        rectPersephoneBlackx5Ability = persephoneBlackRect.centerx - step * 2
        rectPersephoneBlacky5Ability = persephoneBlackRect.centery
        rectPersephoneBlack5Ability = pygame.Rect(rectPersephoneBlackx5Ability - 30, rectPersephoneBlacky5Ability - 30, 60, 60)
        rectsPersephoneBlackAbility.append(rectPersephoneBlack5Ability)

        rectPersephoneBlackx6Ability = persephoneBlackRect.centerx - step * 3
        rectPersephoneBlacky6Ability = persephoneBlackRect.centery
        rectPersephoneBlack6Ability = pygame.Rect(rectPersephoneBlackx6Ability - 30, rectPersephoneBlacky6Ability - 30, 60, 60)
        rectsPersephoneBlackAbility.append(rectPersephoneBlack6Ability)

        rectPersephoneBlackx7Ability = persephoneBlackRect.centerx
        rectPersephoneBlacky7Ability = persephoneBlackRect.centery - step
        rectPersephoneBlack7Ability = pygame.Rect(rectPersephoneBlackx7Ability - 30, rectPersephoneBlacky7Ability - 30, 60, 60)
        rectsPersephoneBlackAbility.append(rectPersephoneBlack7Ability)

        rectPersephoneBlackx8Ability = persephoneBlackRect.centerx
        rectPersephoneBlacky8Ability = persephoneBlackRect.centery - step * 2
        rectPersephoneBlack8Ability = pygame.Rect(rectPersephoneBlackx8Ability - 30, rectPersephoneBlacky8Ability - 30, 60, 60)
        rectsPersephoneBlackAbility.append(rectPersephoneBlack8Ability)

        rectPersephoneBlackx9Ability = persephoneBlackRect.centerx
        rectPersephoneBlacky9Ability = persephoneBlackRect.centery - step * 3
        rectPersephoneBlack9Ability = pygame.Rect(rectPersephoneBlackx9Ability - 30, rectPersephoneBlacky9Ability - 30, 60, 60)
        rectsPersephoneBlackAbility.append(rectPersephoneBlack9Ability)

        rectPersephoneBlackx10Ability = persephoneBlackRect.centerx + step
        rectPersephoneBlacky10Ability = persephoneBlackRect.centery - step
        rectPersephoneBlack10Ability = pygame.Rect(rectPersephoneBlackx10Ability - 30, rectPersephoneBlacky10Ability - 30, 60, 60)
        rectsPersephoneBlackAbility.append(rectPersephoneBlack10Ability)

        rectPersephoneBlackx11Ability = persephoneBlackRect.centerx + step * 2
        rectPersephoneBlacky11Ability = persephoneBlackRect.centery - step * 2
        rectPersephoneBlack11Ability = pygame.Rect(rectPersephoneBlackx11Ability - 30, rectPersephoneBlacky11Ability - 30, 60, 60)
        rectsPersephoneBlackAbility.append(rectPersephoneBlack11Ability)

        rectPersephoneBlackx12Ability = persephoneBlackRect.centerx + step * 3
        rectPersephoneBlacky12Ability = persephoneBlackRect.centery - step * 3
        rectPersephoneBlack12Ability = pygame.Rect(rectPersephoneBlackx12Ability - 30, rectPersephoneBlacky12Ability - 30, 60, 60)
        rectsPersephoneBlackAbility.append(rectPersephoneBlack12Ability)

        rectPersephoneBlackx13Ability = persephoneBlackRect.centerx - step
        rectPersephoneBlacky13Ability = persephoneBlackRect.centery - step
        rectPersephoneBlack13Ability = pygame.Rect(rectPersephoneBlackx13Ability - 30, rectPersephoneBlacky13Ability - 30, 60, 60)
        rectsPersephoneBlackAbility.append(rectPersephoneBlack13Ability)

        rectPersephoneBlackx14Ability = persephoneBlackRect.centerx - step * 2
        rectPersephoneBlacky14Ability = persephoneBlackRect.centery - step * 2
        rectPersephoneBlack14Ability = pygame.Rect(rectPersephoneBlackx14Ability - 30, rectPersephoneBlacky14Ability - 30, 60, 60)
        rectsPersephoneBlackAbility.append(rectPersephoneBlack14Ability)

        rectPersephoneBlackx15Ability = persephoneBlackRect.centerx - step * 3
        rectPersephoneBlacky15Ability = persephoneBlackRect.centery - step * 3
        rectPersephoneBlack15Ability = pygame.Rect(rectPersephoneBlackx15Ability - 30, rectPersephoneBlacky15Ability - 30, 60, 60)
        rectsPersephoneBlackAbility.append(rectPersephoneBlack15Ability)

        rectPersephoneBlackx16Ability = persephoneBlackRect.centerx + step
        rectPersephoneBlacky16Ability = persephoneBlackRect.centery + step
        rectPersephoneBlack16Ability = pygame.Rect(rectPersephoneBlackx16Ability - 30, rectPersephoneBlacky16Ability - 30, 60, 60)
        rectsPersephoneBlackAbility.append(rectPersephoneBlack16Ability)

        rectPersephoneBlackx17Ability = persephoneBlackRect.centerx + step * 2
        rectPersephoneBlacky17Ability = persephoneBlackRect.centery + step * 2
        rectPersephoneBlack17Ability = pygame.Rect(rectPersephoneBlackx17Ability - 30, rectPersephoneBlackx17Ability - 30, 60, 60)
        rectsPersephoneBlackAbility.append(rectPersephoneBlack17Ability)

        rectPersephoneBlackx18Ability = persephoneBlackRect.centerx - step
        rectPersephoneBlacky18Ability = persephoneBlackRect.centery + step
        rectPersephoneBlack18Ability = pygame.Rect(rectPersephoneBlackx18Ability - 30, rectPersephoneBlacky18Ability - 30, 60, 60)
        rectsPersephoneBlackAbility.append(rectPersephoneBlack18Ability)

        rectPersephoneBlackx19Ability = persephoneBlackRect.centerx - step * 2
        rectPersephoneBlacky19Ability = persephoneBlackRect.centery + step * 2
        rectPersephoneBlack19Ability = pygame.Rect(rectPersephoneBlackx19Ability - 30, rectPersephoneBlacky19Ability - 30, 60, 60)
        rectsPersephoneBlackAbility.append(rectPersephoneBlack19Ability)

        #Persefona bílá abilita

        rectsPersephoneWhiteAbility = []

        rectPersephoneWhitex1Ability = persephoneWhiteRect.centerx
        rectPersephoneWhitey1Ability = persephoneWhiteRect.centery - step
        rectPersephoneWhite1Ability = pygame.Rect(rectPersephoneWhitex1Ability - 30, rectPersephoneWhitey1Ability - 30, 60, 60)
        rectsPersephoneWhiteAbility.append(rectPersephoneWhite1Ability)

        rectPersephoneWhitex2Ability = persephoneWhiteRect.centerx
        rectPersephoneWhitey2Ability = persephoneWhiteRect.centery - step * 2
        rectPersephoneWhite2Ability = pygame.Rect(rectPersephoneWhitex2Ability - 30, rectPersephoneWhitey2Ability - 30, 60, 60)
        rectsPersephoneWhiteAbility.append(rectPersephoneWhite2Ability)

        rectPersephoneWhitex3Ability = persephoneWhiteRect.centerx
        rectPersephoneWhitey3Ability = persephoneWhiteRect.centery - step * 3
        rectPersephoneWhite3Ability = pygame.Rect(rectPersephoneWhitex3Ability - 30, rectPersephoneWhitey3Ability - 30, 60, 60)
        rectsPersephoneWhiteAbility.append(rectPersephoneWhite3Ability)

        rectPersephoneWhitex4Ability = persephoneWhiteRect.centerx + step
        rectPersephoneWhitey4Ability = persephoneWhiteRect.centery - step
        rectPersephoneWhite4Ability = pygame.Rect(rectPersephoneWhitex4Ability - 30, rectPersephoneWhitey4Ability - 30, 60, 60)
        rectsPersephoneWhiteAbility.append(rectPersephoneWhite4Ability)

        rectPersephoneWhitex5Ability = persephoneWhiteRect.centerx + step * 2
        rectPersephoneWhitey5Ability = persephoneWhiteRect.centery - step * 2
        rectPersephoneWhite5Ability = pygame.Rect(rectPersephoneWhitex5Ability - 30, rectPersephoneWhitey5Ability - 30, 60, 60)
        rectsPersephoneWhiteAbility.append(rectPersephoneWhite5Ability)

        rectPersephoneWhitex6Ability = persephoneWhiteRect.centerx + step * 3
        rectPersephoneWhitey6Ability = persephoneWhiteRect.centery - step * 3
        rectPersephoneWhite6Ability = pygame.Rect(rectPersephoneWhitex6Ability - 30, rectPersephoneWhitey6Ability - 30, 60, 60)
        rectsPersephoneWhiteAbility.append(rectPersephoneWhite6Ability)

        rectPersephoneWhitex7Ability = persephoneWhiteRect.centerx + step
        rectPersephoneWhitey7Ability = persephoneWhiteRect.centery
        rectPersephoneWhite7Ability = pygame.Rect(rectPersephoneWhitex7Ability - 30, rectPersephoneWhitey7Ability - 30, 60, 60)
        rectsPersephoneWhiteAbility.append(rectPersephoneWhite7Ability)

        rectPersephoneWhitex8Ability = persephoneWhiteRect.centerx + step * 2
        rectPersephoneWhitey8Ability = persephoneWhiteRect.centery
        rectPersephoneWhite8Ability = pygame.Rect(rectPersephoneWhitex8Ability - 30, rectPersephoneWhitey8Ability - 30, 60, 60)
        rectsPersephoneWhiteAbility.append(rectPersephoneWhite8Ability)

        rectPersephoneWhitex9Ability = persephoneWhiteRect.centerx + step * 3
        rectPersephoneWhitey9Ability = persephoneWhiteRect.centery
        rectPersephoneWhite9Ability = pygame.Rect(rectPersephoneWhitex9Ability - 30, rectPersephoneWhitey9Ability - 30, 60, 60)
        rectsPersephoneWhiteAbility.append(rectPersephoneWhite9Ability)

        rectPersephoneWhitex10Ability = persephoneWhiteRect.centerx + step
        rectPersephoneWhitey10Ability = persephoneWhiteRect.centery + step
        rectPersephoneWhite10Ability = pygame.Rect(rectPersephoneWhitex10Ability - 30, rectPersephoneWhitey10Ability - 30, 60, 60)
        rectsPersephoneWhiteAbility.append(rectPersephoneWhite10Ability)

        rectPersephoneWhitex11Ability = persephoneWhiteRect.centerx + step * 2
        rectPersephoneWhitey11Ability = persephoneWhiteRect.centery + step * 2
        rectPersephoneWhite11Ability = pygame.Rect(rectPersephoneWhitex11Ability - 30, rectPersephoneWhitey11Ability - 30, 60, 60)
        rectsPersephoneWhiteAbility.append(rectPersephoneWhite11Ability)

        rectPersephoneWhitex12Ability = persephoneWhiteRect.centerx - step
        rectPersephoneWhitey12Ability = persephoneWhiteRect.centery - step
        rectPersephoneWhite12Ability = pygame.Rect(rectPersephoneWhitex12Ability - 30, rectPersephoneWhitey12Ability - 30, 60, 60)
        rectsPersephoneWhiteAbility.append(rectPersephoneWhite12Ability)

        rectPersephoneWhitex13Ability = persephoneWhiteRect.centerx - step * 2
        rectPersephoneWhitey13Ability = persephoneWhiteRect.centery - step * 2
        rectPersephoneWhite13Ability = pygame.Rect(rectPersephoneWhitex13Ability - 30, rectPersephoneWhitey13Ability - 30, 60, 60)
        rectsPersephoneWhiteAbility.append(rectPersephoneWhite13Ability)

        rectPersephoneWhitex14Ability = persephoneWhiteRect.centerx - step * 3
        rectPersephoneWhitey14Ability = persephoneWhiteRect.centery - step * 3
        rectPersephoneWhite14Ability = pygame.Rect(rectPersephoneWhitex14Ability - 30, rectPersephoneWhitey14Ability - 30, 60, 60)
        rectsPersephoneWhiteAbility.append(rectPersephoneWhite14Ability)

        rectPersephoneWhitex15Ability = persephoneWhiteRect.centerx - step
        rectPersephoneWhitey15Ability = persephoneWhiteRect.centery
        rectPersephoneWhite15Ability = pygame.Rect(rectPersephoneWhitex15Ability - 30, rectPersephoneWhitey15Ability - 30, 60, 60)
        rectsPersephoneWhiteAbility.append(rectPersephoneWhite15Ability)

        rectPersephoneWhitex16Ability = persephoneWhiteRect.centerx - step * 2
        rectPersephoneWhitey16Ability = persephoneWhiteRect.centery
        rectPersephoneWhite16Ability = pygame.Rect(rectPersephoneWhitex16Ability - 30, rectPersephoneWhitey16Ability - 30, 60, 60)
        rectsPersephoneWhiteAbility.append(rectPersephoneWhite16Ability)

        rectPersephoneWhitex17Ability = persephoneWhiteRect.centerx - step * 3
        rectPersephoneWhitey17Ability = persephoneWhiteRect.centery
        rectPersephoneWhite17Ability = pygame.Rect(rectPersephoneWhitex17Ability - 30, rectPersephoneWhitey17Ability - 30, 60, 60)
        rectsPersephoneWhiteAbility.append(rectPersephoneWhite17Ability)

        rectPersephoneWhitex18Ability = persephoneWhiteRect.centerx - step
        rectPersephoneWhitey18Ability = persephoneWhiteRect.centery + step
        rectPersephoneWhite18Ability = pygame.Rect(rectPersephoneWhitex18Ability - 30, rectPersephoneWhitey18Ability - 30, 60, 60)
        rectsPersephoneWhiteAbility.append(rectPersephoneWhite18Ability)

        rectPersephoneWhitex19Ability = persephoneWhiteRect.centerx - step * 2
        rectPersephoneWhitey19Ability = persephoneWhiteRect.centery + step * 2
        rectPersephoneWhite19Ability = pygame.Rect(rectPersephoneWhitex19Ability - 30, rectPersephoneWhitey19Ability - 30, 60, 60)
        rectsPersephoneWhiteAbility.append(rectPersephoneWhite19Ability)


        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
            print(event.pos)
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
                
                if plagueDoctorWhiteRect.collidepoint(event.pos) and not hadesWhiteAbilityActivated and plagueDoctorWhiteRect.centerx!=step:
                    if not plagueDoctorWhitePlaying:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                plagueDoctorWhitePlaying=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                plagueDoctorWhitePlaying=True
                elif plagueDoctorWhitePlaying:
                    plagueWhitexInit=plagueDoctorWhiteRect.centerx
                    plagueWhiteyInit = plagueDoctorWhiteRect.centery 
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
                    if (plagueDoctorWhiteRect.centerx <= 480 or plagueDoctorWhiteRect.centerx >= 1440) or (plagueDoctorWhiteRect.centery <= 60 or plagueDoctorWhiteRect.centery >= 1020):
                        plagueDoctorWhiteRect.centerx = plagueWhitexInit
                        plagueDoctorWhiteRect.centery = plagueWhiteyInit
                        plagueDoctorWhitePlaying=False
                        counter-=1
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
                if rectPlagueDoctorWhiteAbilityActivated:
                    if archbishopWhiteRect.collidepoint(event.pos) and archbishopWhiteRect.centerx==step*2:
                        archbishopWhiteRect.centerx=archbishopWhitexInit
                        archbishopWhiteRect.centery=archbishopWhiteyInit
                        counter += 1
                        plagueDoctorWhitePlaying=False
                        rectPlagueDoctorWhiteAbilityActivated=False
                        rectPlagueDoctorWhiteAbilityCounter-=1
                    elif cardinalWhiteRect.collidepoint(event.pos) and cardinalWhiteRect.centerx==step*3:
                        cardinalWhiteRect.centerx=cardinalWhitexInit
                        cardinalWhiteRect.centery=cardinalWhiteyInit
                        counter += 1
                        plagueDoctorWhitePlaying=False
                        rectPlagueDoctorWhiteAbilityActivated=False
                        rectPlagueDoctorWhiteAbilityCounter-=1
                    elif cardinalWhiteRect1.collidepoint(event.pos) and cardinalWhiteRect1.centerx==step*3:
                        cardinalWhiteRect1.centerx=cardinalWhitexInit1
                        cardinalWhiteRect1.centery=cardinalWhiteyInit1
                        counter += 1
                        plagueDoctorWhitePlaying=False
                        rectPlagueDoctorWhiteAbilityActivated=False
                        rectPlagueDoctorWhiteAbilityCounter-=1
                    elif archbishopWhiteRect1.collidepoint(event.pos) and archbishopWhiteRect1.centerx==step:
                        archbishopWhiteRect1.centerx=archbishopWhitexInit1
                        archbishopWhiteRect1.centery=archbishopWhiteyInit1
                        counter += 1
                        plagueDoctorWhitePlaying=False
                        rectPlagueDoctorWhiteAbilityActivated=False
                        rectPlagueDoctorWhiteAbilityCounter-=1
                    elif plagueDoctorWhiteRect1.collidepoint(event.pos) and plagueDoctorWhiteRect1.centerx==step*2:
                        plagueDoctorWhiteRect1.centerx=plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery=plagueWhiteyInit1
                        counter += 1
                        plagueDoctorWhitePlaying=False
                        rectPlagueDoctorWhiteAbilityActivated=False
                        rectPlagueDoctorWhiteAbilityCounter-=1
                    elif warriorWhiteRect.collidepoint(event.pos) and warriorWhiteRect.centerx==step:
                        warriorWhiteRect.centerx=warriorWhitexInit
                        warriorWhiteRect.centery=warriorWhiteyInit
                        counter += 1
                        plagueDoctorWhitePlaying=False
                        rectPlagueDoctorWhiteAbilityActivated=False
                        rectPlagueDoctorWhiteAbilityCounter-=1
                    elif legionaryWhiteRect.collidepoint(event.pos) and legionaryWhiteRect.centerx==step*3:
                        legionaryWhiteRect.centerx=legionaryWhitexInit
                        legionaryWhiteRect.centery=legionaryWhiteyInit
                        counter += 1
                        plagueDoctorWhitePlaying=False
                        rectPlagueDoctorWhiteAbilityActivated=False
                        rectPlagueDoctorWhiteAbilityCounter-=1
                    elif warriorWhiteRect1.collidepoint(event.pos) and warriorWhiteRect1.centerx==step*3:
                        warriorWhiteRect1.centerx=warriorWhitexInit1
                        warriorWhiteRect1.centery=warriorWhiteyInit1
                        counter += 1
                        plagueDoctorWhitePlaying=False
                        rectPlagueDoctorWhiteAbilityActivated=False
                        rectPlagueDoctorWhiteAbilityCounter-=1
                    elif legionaryWhiteRect1.collidepoint(event.pos) and legionaryWhiteRect1.centerx==step*2:
                        legionaryWhiteRect1.centerx=legionaryWhitexInit1
                        legionaryWhiteRect1.centery=legionaryWhiteyInit1
                        counter += 1
                        plagueDoctorWhitePlaying=False
                        rectPlagueDoctorWhiteAbilityActivated=False
                        rectPlagueDoctorWhiteAbilityCounter-=1
                    elif warriorWhiteRect2.collidepoint(event.pos) and warriorWhiteRect2.centerx==step*2:
                        warriorWhiteRect2.centerx=warriorWhitexInit2
                        warriorWhiteRect2.centery=warriorWhiteyInit2
                        counter += 1
                        plagueDoctorWhitePlaying=False
                        rectPlagueDoctorWhiteAbilityActivated=False
                        rectPlagueDoctorWhiteAbilityCounter-=1
                    elif legionaryWhiteRect2.collidepoint(event.pos) and legionaryWhiteRect2.centerx==step:
                        legionaryWhiteRect2.centerx=legionaryWhitexInit2
                        legionaryWhiteRect2.centery=legionaryWhiteyInit2
                        counter += 1
                        plagueDoctorWhitePlaying=False
                        rectPlagueDoctorWhiteAbilityActivated=False
                        rectPlagueDoctorWhiteAbilityCounter-=1
                    elif warriorWhiteRect3.collidepoint(event.pos) and warriorWhiteRect3.centerx==step:
                        warriorWhiteRect3.centerx=warriorWhitexInit3
                        warriorWhiteRect3.centery=warriorWhiteyInit3
                        counter += 1
                        plagueDoctorWhitePlaying=False
                        rectPlagueDoctorWhiteAbilityActivated=False
                        rectPlagueDoctorWhiteAbilityCounter-=1
                    elif legionaryWhiteRect3.collidepoint(event.pos) and legionaryWhiteRect3.centerx==step*3:
                        legionaryWhiteRect3.centerx=legionaryWhitexInit3
                        legionaryWhiteRect3.centery=legionaryWhiteyInit3
                        counter += 1
                        plagueDoctorWhitePlaying=False        
                        rectPlagueDoctorWhiteAbilityActivated=False
                        rectPlagueDoctorWhiteAbilityCounter-=1
                    elif cardinalWhiteRectCopy.collidepoint(event.pos) and cardinalWhiteRectCopy.centerx==step:
                        cardinalWhiteRectCopy.centerx=cardinalWhitexInitCopy
                        cardinalWhiteRectCopy.centery=cardinalWhiteyInitCopy
                        counter += 1
                        plagueDoctorWhitePlaying1=False  
                        rectPlagueDoctorWhiteAbilityActivated_1=False
                        rectPlagueDoctorWhiteAbilityCounter_1-=1
                    elif cardinalWhiteRectCopy_1.collidepoint(event.pos) and cardinalWhiteRectCopy_1.centerx==step:
                        cardinalWhiteRectCopy_1.centerx=cardinalWhitexInitCopy1
                        cardinalWhiteRectCopy_1.centery=cardinalWhiteyInitCopy1
                        counter += 1
                        plagueDoctorWhitePlaying1=False  
                        rectPlagueDoctorWhiteAbilityActivated_1=False
                        rectPlagueDoctorWhiteAbilityCounter_1-=1
                    else:
                        rectPlagueDoctorWhiteAbilityActivated_1=False
                        plagueDoctorWhitePlaying1=False  

                        

                        #plagueDoctorWhiteRect.centerx = event.pos[0]
                        #plagueDoctorWhiteRect.centery = event.pos[1]

                if archbishopWhiteRect.collidepoint(event.pos) and not hadesWhiteAbilityActivated and archbishopWhiteRect.centerx!=step*2:
                    if not archbishopWhitePlaying:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                archbishopWhitePlaying=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                archbishopWhitePlaying=True
                elif archbishopWhitePlaying:
                    archbishopWhitexInit=archbishopWhiteRect.centerx
                    archbishopWhiteyInit=archbishopWhiteRect.centery
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
                    if (archbishopWhiteRect.centerx <= 480 or archbishopWhiteRect.centerx >= 1440) or (archbishopWhiteRect.centery <= 60 or archbishopWhiteRect.centery >= 1020):
                        archbishopWhiteRect.centerx = archbishopWhitexInit
                        archbishopWhiteRect.centery = archbishopWhiteyInit
                        archbishopWhitePlaying=False
                        counter-=1
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
                if archbishopWhiteAbilityActivated and not hadesWhiteAbilityActivated:
                    if plagueDoctorBlackRect.collidepoint(event.pos):
                        plagueDoctorBlackRect.centerx = screen_width-step
                        plagueDoctorBlackRect.centery = step
                        archbishopWhiteFiguresCount+=1
                        archbishopWhitePlaying=False
                        archbishopWhiteAbilityActivated=False
                        archbishopWhiteAbilityCounter-=1
                        counter+=1
                    if archbishopBlackRect.collidepoint(event.pos):
                        archbishopBlackRect.centerx = screen_width-step*2
                        archbishopBlackRect.centery = step
                        archbishopWhiteFiguresCount+=1
                        archbishopWhitePlaying=False
                        archbishopWhiteAbilityActivated=False
                        archbishopWhiteAbilityCounter-=1
                        counter+=1
                    if cardinalBlackRect.collidepoint(event.pos):
                        cardinalBlackRect.centerx = screen_width-step*3
                        cardinalBlackRect.centery = step
                        archbishopWhiteFiguresCount+=1
                        archbishopWhitePlaying=False
                        archbishopWhiteAbilityActivated=False
                        archbishopWhiteAbilityCounter-=1
                        counter+=1
                    if hadesBlackRect.collidepoint(event.pos):
                        hadesBlackRect.centerx = screen_width-step
                        hadesBlackRect.centery = step*2
                        archbishopWhiteFiguresCount+=1
                        archbishopWhitePlaying=False
                        archbishopWhiteAbilityActivated=False
                        archbishopWhiteAbilityCounter-=1
                        counter+=1
                    if persephoneBlackRect.collidepoint(event.pos):
                        persephoneBlackRect.centerx = screen_width-step*2
                        persephoneBlackRect.centery = step*2
                        archbishopWhiteFiguresCount+=1
                        archbishopWhitePlaying=False
                        archbishopWhiteAbilityActivated=False
                        archbishopWhiteAbilityCounter-=1
                        counter+=1
                    if cardinalBlackRect1.collidepoint(event.pos):
                        cardinalBlackRect1.centerx = screen_width-step*3
                        cardinalBlackRect1.centery = step*2
                        archbishopWhiteFiguresCount+=1
                        archbishopWhitePlaying=False
                        archbishopWhiteAbilityActivated=False
                        archbishopWhiteAbilityCounter-=1
                        counter+=1
                    if archbishopBlackRect1.collidepoint(event.pos):
                        archbishopBlackRect1.centerx = screen_width-step
                        archbishopBlackRect1.centery = step*3
                        archbishopWhiteFiguresCount+=1
                        archbishopWhitePlaying=False
                        archbishopWhiteAbilityActivated=False
                        archbishopWhiteAbilityCounter-=1
                        counter+=1
                    if plagueDoctorBlackRect1.collidepoint(event.pos):
                        plagueDoctorBlackRect1.centerx = screen_width-step*2
                        plagueDoctorBlackRect1.centery = step*3
                        archbishopWhiteFiguresCount+=1
                        archbishopWhitePlaying=False
                        archbishopWhiteAbilityActivated=False
                        archbishopWhiteAbilityCounter-=1
                        counter+=1
                    if legionaryBlackRect.collidepoint(event.pos):
                        legionaryBlackRect.centerx = screen_width-step*3
                        legionaryBlackRect.centery = step*3
                        archbishopWhiteFiguresCount+=1
                        archbishopWhitePlaying=False
                        archbishopWhiteAbilityActivated=False
                        archbishopWhiteAbilityCounter-=1
                        counter+=1
                    if warriorBlackRect.collidepoint(event.pos):
                        warriorBlackRect.centerx = screen_width-step
                        warriorBlackRect.centery = step*4
                        archbishopWhiteFiguresCount+=1
                        archbishopWhitePlaying=False
                        archbishopWhiteAbilityActivated=False
                        archbishopWhiteAbilityCounter-=1
                        counter+=1
                    if legionaryBlackRect1.collidepoint(event.pos):
                        legionaryBlackRect1.centerx = screen_width-step*2
                        legionaryBlackRect1.centery = step*4
                        archbishopWhiteFiguresCount+=1
                        archbishopWhitePlaying=False
                        archbishopWhiteAbilityActivated=False
                        archbishopWhiteAbilityCounter-=1
                        counter+=1
                    if warriorBlackRect1.collidepoint(event.pos):
                        warriorBlackRect1.centerx = screen_width-step*3
                        warriorBlackRect1.centery = step*4
                        archbishopWhiteFiguresCount+=1
                        archbishopWhitePlaying=False
                        archbishopWhiteAbilityActivated=False
                        archbishopWhiteAbilityCounter-=1
                        counter+=1
                    if legionaryBlackRect2.collidepoint(event.pos):
                        legionaryBlackRect2.centerx = screen_width-step
                        legionaryBlackRect2.centery = step*5
                        archbishopWhiteFiguresCount+=1
                        archbishopWhitePlaying=False
                        archbishopWhiteAbilityActivated=False
                        archbishopWhiteAbilityCounter-=1
                        counter+=1
                    if warriorBlackRect2.collidepoint(event.pos):
                        warriorBlackRect2.centerx = screen_width-step*2
                        warriorBlackRect2.centery = step*5
                        archbishopWhiteFiguresCount+=1
                        archbishopWhitePlaying=False
                        archbishopWhiteAbilityActivated=False
                        archbishopWhiteAbilityCounter-=1
                        counter+=1
                    if legionaryBlackRect3.collidepoint(event.pos):
                        legionaryBlackRect3.centerx = screen_width-step*3
                        legionaryBlackRect3.centery = step*5
                        archbishopWhiteFiguresCount+=1
                        archbishopWhitePlaying=False
                        archbishopWhiteAbilityActivated=False
                        archbishopWhiteAbilityCounter-=1
                        counter+=1
                    if warriorBlackRect3.collidepoint(event.pos):
                        warriorBlackRect3.centerx = screen_width-step
                        warriorBlackRect3.centery = step*6
                        archbishopWhiteFiguresCount+=1
                        archbishopWhitePlaying=False
                        archbishopWhiteAbilityActivated=False
                        archbishopWhiteAbilityCounter-=1
                        counter+=1

                      

                        #archbishopWhiteRect.centerx = event.pos[0]
                        #archbishopWhiteRect.centery = event.pos[1]

                if cardinalWhiteRect.collidepoint(event.pos) and not hadesWhiteAbilityActivated and cardinalWhiteRect.centerx!=step*3:
                    if not cardinalWhitePlaying:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                cardinalWhitePlaying=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                cardinalWhitePlaying=True
                elif cardinalWhitePlaying:
                    cardinalWhitexInit=cardinalWhiteRect.centerx
                    cardinalWhiteyInit=cardinalWhiteRect.centery
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
                    if (cardinalWhiteRect.centerx <= 480 or cardinalWhiteRect.centerx >= 1440) or (cardinalWhiteRect.centery <= 60 or cardinalWhiteRect.centery >= 1020):
                        cardinalWhiteRect.centerx = cardinalWhitexInit
                        cardinalWhiteRect.centery = cardinalWhiteyInit
                        cardinalWhitePlaying=False
                        counter-=1
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
                if cardinalWhiteAbilityActivated and not hadesWhiteAbilityActivated:
                    if plagueDoctorBlackRect.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        plagueDoctorBlackxBefore=plagueDoctorBlackRect.centerx
                        plagueDoctorBlackyBefore=plagueDoctorBlackRect.centery
                        plagueDoctorBlackRect.centerx = screen_width-step
                        plagueDoctorBlackRect.centery = step
                        cardinalWhiteRectCopy.centerx=plagueDoctorBlackxBefore
                        cardinalWhiteRectCopy.centery=plagueDoctorBlackyBefore
                        cardinalWhiteAbilityActivated=False
                        cardinalWhiteAbilityCounter-=1
                    if archbishopBlackRect.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        archbishopBlackxBefore=archbishopBlackRect.centerx
                        archbishopBlackyBefore=archbishopBlackRect.centery
                        archbishopBlackRect.centerx = screen_width-step*2
                        archbishopBlackRect.centery = step
                        cardinalWhiteRectCopy.centerx=archbishopBlackxBefore
                        cardinalWhiteRectCopy.centery=archbishopBlackyBefore
                        cardinalWhiteAbilityActivated=False
                        cardinalWhiteAbilityCounter-=1
                    if cardinalBlackRect.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        cardinalBlackxBefore=cardinalBlackRect.centerx
                        cardinalBlackyBefore=cardinalBlackRect.centery
                        cardinalBlackRect.centerx = screen_width-step*3
                        cardinalBlackRect.centery = step
                        cardinalWhiteRectCopy.centerx=cardinalBlackxBefore
                        cardinalWhiteRectCopy.centery=cardinalBlackyBefore
                        cardinalWhiteAbilityActivated=False
                        cardinalWhiteAbilityCounter-=1
                    if cardinalBlackRect1.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        cardinalBlackxBefore_1=cardinalBlackRect1.centerx
                        cardinalBlackyBefore_1=cardinalBlackRect1.centery
                        cardinalBlackRect1.centerx = screen_width-step*3
                        cardinalBlackRect1.centery = step*2
                        cardinalWhiteRectCopy.centerx=cardinalBlackxBefore_1
                        cardinalWhiteRectCopy.centery=cardinalBlackyBefore_1
                        cardinalWhiteAbilityActivated=False
                        cardinalWhiteAbilityCounter-=1
                    if archbishopBlackRect1.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        archbishopBlackxBefore_1=archbishopBlackRect1.centerx
                        archbishopBlackyBefore_1=archbishopBlackRect1.centery
                        archbishopBlackRect1.centerx = screen_width-step
                        archbishopBlackRect1.centery = step*3
                        cardinalWhiteRectCopy.centerx=archbishopBlackxBefore_1
                        cardinalWhiteRectCopy.centery=archbishopBlackyBefore_1
                        cardinalWhitePlayingCopy=False
                        cardinalWhiteAbilityActivated=False
                        cardinalWhiteAbilityCounter-=1
                    if plagueDoctorBlackRect1.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        plagueDoctorBlackxBefore_1=plagueDoctorBlackRect1.centerx
                        plagueDoctorBlackyBefore_1=plagueDoctorBlackRect1.centery
                        plagueDoctorBlackRect1.centerx = screen_width-step*2
                        plagueDoctorBlackRect1.centery = step*3
                        cardinalWhiteRectCopy.centerx=plagueDoctorBlackxBefore_1
                        cardinalWhiteRectCopy.centery=plagueDoctorBlackyBefore_1
                        cardinalWhitePlayingCopy=False
                        cardinalWhiteAbilityActivated=False
                        cardinalWhiteAbilityCounter-=1
                    if legionaryBlackRect.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        legionaryBlackxBefore=legionaryBlackRect.centerx
                        legionaryBlackyBefore=legionaryBlackRect.centery
                        legionaryBlackRect.centerx = screen_width-step*3
                        legionaryBlackRect.centery = step*3
                        cardinalWhiteRectCopy.centerx=legionaryBlackxBefore
                        cardinalWhiteRectCopy.centery=legionaryBlackyBefore
                        cardinalWhitePlayingCopy=False
                        cardinalWhiteAbilityActivated=False
                        cardinalWhiteAbilityCounter-=1
                    if warriorBlackRect.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        warriorBlackxBefore=warriorBlackRect.centerx
                        warriorBlackyBefore=warriorBlackRect.centery
                        warriorBlackRect.centerx = screen_width-step
                        warriorBlackRect.centery = step*4
                        cardinalWhiteRectCopy.centerx=warriorBlackxBefore
                        cardinalWhiteRectCopy.centery=warriorBlackyBefore
                        cardinalWhitePlayingCopy=False
                        cardinalWhiteAbilityActivated=False
                        cardinalWhiteAbilityCounter-=1
                    if legionaryBlackRect1.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        legionaryBlackxBefore_1=legionaryBlackRect1.centerx
                        legionaryBlackyBefore_1=legionaryBlackRect1.centery
                        legionaryBlackRect1.centerx = screen_width-step*2
                        legionaryBlackRect1.centery = step*4
                        cardinalWhiteRectCopy.centerx=legionaryBlackxBefore_1
                        cardinalWhiteRectCopy.centery=legionaryBlackyBefore_1
                        cardinalWhitePlayingCopy=False
                        cardinalWhiteAbilityActivated=False
                        cardinalWhiteAbilityCounter-=1
                    if warriorBlackRect1.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        warriorBlackxBefore_1=warriorBlackRect1.centerx
                        warriorBlackyBefore_1=warriorBlackRect1.centery
                        warriorBlackRect1.centerx = screen_width-step*3
                        warriorBlackRect1.centery = step*4
                        cardinalWhiteRectCopy.centerx=warriorBlackxBefore_1
                        cardinalWhiteRectCopy.centery=warriorBlackyBefore_1
                        cardinalWhitePlayingCopy=False
                        cardinalWhiteAbilityActivated=False
                        cardinalWhiteAbilityCounter-=1
                    if legionaryBlackRect2.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        legionaryBlackxBefore_2=legionaryBlackRect2.centerx
                        legionaryBlackyBefore_2=legionaryBlackRect2.centery
                        legionaryBlackRect2.centerx = screen_width-step
                        legionaryBlackRect2.centery = step*5
                        cardinalWhiteRectCopy.centerx=legionaryBlackxBefore_2
                        cardinalWhiteRectCopy.centery=legionaryBlackyBefore_2
                        cardinalWhitePlayingCopy=False
                        cardinalWhiteAbilityActivated=False
                        cardinalWhiteAbilityCounter-=1
                    if warriorBlackRect2.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        warriorBlackxBefore_2=warriorBlackRect2.centerx
                        warriorBlackyBefore_2=warriorBlackRect2.centery
                        warriorBlackRect2.centerx = screen_width-step*2
                        warriorBlackRect2.centery = step*5
                        cardinalWhiteRectCopy.centerx=warriorBlackxBefore_2
                        cardinalWhiteRectCopy.centery=warriorBlackyBefore_2
                        cardinalWhitePlayingCopy=False
                        cardinalWhiteAbilityActivated=False
                        cardinalWhiteAbilityCounter-=1
                    if legionaryBlackRect3.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        legionaryBlackxBefore_3=legionaryBlackRect3.centerx
                        legionaryBlackyBefore_3=legionaryBlackRect3.centery
                        legionaryBlackRect3.centerx = screen_width-step*3
                        legionaryBlackRect3.centery = step*5
                        cardinalWhiteRectCopy.centerx=legionaryBlackxBefore_3
                        cardinalWhiteRectCopy.centery=legionaryBlackyBefore_3
                        cardinalWhiteAbilityActivated=False
                        cardinalWhiteAbilityCounter-=1
                    if warriorBlackRect3.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        warriorBlackxBefore_3=warriorBlackRect3.centerx
                        warriorBlackyBefore_3=warriorBlackRect3.centery
                        warriorBlackRect3.centerx = screen_width-step
                        warriorBlackRect3.centery = step*6
                        cardinalWhiteRectCopy.centerx=warriorBlackxBefore_3
                        cardinalWhiteRectCopy.centery=warriorBlackyBefore_3
                        cardinalWhiteAbilityActivated=False
                        cardinalWhiteAbilityCounter-=1

                if hadesWhiteRect.collidepoint(event.pos) and hadesWhiteRect.centerx!=step:
                    if not hadesWhitePlaying:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                hadesWhitePlaying=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                hadesWhitePlaying=True
                elif hadesWhitePlaying:
                    hadesWhitexInit=hadesWhiteRect.centerx
                    hadesWhiteyInit=hadesWhiteRect.centery
                    if rectHadesWhite1.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite1.centerx
                        hadesWhiteRect.centery = rectHadesWhite1.centery
                        if not hadesWhiteAbilityActivated:
                            counter += 1
                        else:
                            hadesWhiteAbilityCounter-=1
                        hadesWhitePlaying=False
                    elif rectHadesWhite2.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite2.centerx
                        hadesWhiteRect.centery = rectHadesWhite2.centery
                        if not hadesWhiteAbilityActivated:
                            counter += 1
                        else:
                            hadesWhiteAbilityCounter-=1
                        hadesWhitePlaying=False
                    elif rectHadesWhite3.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite3.centerx
                        hadesWhiteRect.centery = rectHadesWhite3.centery
                        if not hadesWhiteAbilityActivated:
                            counter += 1
                        else:
                            hadesWhiteAbilityCounter-=1
                        hadesWhitePlaying=False
                    elif rectHadesWhite4.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite4.centerx
                        hadesWhiteRect.centery = rectHadesWhite4.centery
                        if not hadesWhiteAbilityActivated:
                            counter += 1
                        else:
                            hadesWhiteAbilityCounter-=1
                        hadesWhitePlaying=False
                    elif rectHadesWhite5.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite5.centerx
                        hadesWhiteRect.centery = rectHadesWhite5.centery
                        if not hadesWhiteAbilityActivated:
                            counter += 1
                        else:
                            hadesWhiteAbilityCounter-=1
                        hadesWhitePlaying=False
                    elif rectHadesWhite6.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite6.centerx
                        hadesWhiteRect.centery = rectHadesWhite6.centery
                        if not hadesWhiteAbilityActivated:
                            counter += 1
                        else:
                            hadesWhiteAbilityCounter-=1
                        hadesWhitePlaying=False
                    elif rectHadesWhite7.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite7.centerx
                        hadesWhiteRect.centery = rectHadesWhite7.centery
                        if not hadesWhiteAbilityActivated:
                            counter += 1
                        else:
                            hadesWhiteAbilityCounter-=1
                        hadesWhitePlaying=False
                    elif rectHadesWhite8.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite8.centerx
                        hadesWhiteRect.centery = rectHadesWhite8.centery
                        if not hadesWhiteAbilityActivated:
                            counter += 1
                        else:
                            hadesWhiteAbilityCounter-=1
                        hadesWhitePlaying=False
                    elif rectHadesWhite9.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite9.centerx
                        hadesWhiteRect.centery = rectHadesWhite9.centery
                        if not hadesWhiteAbilityActivated:
                            counter += 1
                        else:
                            hadesWhiteAbilityCounter-=1
                        hadesWhitePlaying=False
                    elif rectHadesWhite10.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite10.centerx
                        hadesWhiteRect.centery = rectHadesWhite10.centery
                        if not hadesWhiteAbilityActivated:
                            counter += 1
                        else:
                            hadesWhiteAbilityCounter-=1
                        hadesWhitePlaying=False
                    elif rectHadesWhite11.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite11.centerx
                        hadesWhiteRect.centery = rectHadesWhite11.centery
                        if not hadesWhiteAbilityActivated:
                            counter += 1
                        else:
                            hadesWhiteAbilityCounter-=1
                        hadesWhitePlaying=False
                    elif rectHadesWhite12.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite12.centerx
                        hadesWhiteRect.centery = rectHadesWhite12.centery
                        if not hadesWhiteAbilityActivated:
                            counter += 1
                        else:
                            hadesWhiteAbilityCounter-=1
                        hadesWhitePlaying=False
                    elif rectHadesWhite13.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite13.centerx
                        hadesWhiteRect.centery = rectHadesWhite13.centery
                        if not hadesWhiteAbilityActivated:
                            counter += 1
                        else:
                            hadesWhiteAbilityCounter-=1
                        hadesWhitePlaying=False
                    elif rectHadesWhite14.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite14.centerx
                        hadesWhiteRect.centery = rectHadesWhite14.centery
                        if not hadesWhiteAbilityActivated:
                            counter += 1
                        else:
                            hadesWhiteAbilityCounter-=1
                        hadesWhitePlaying=False
                    elif rectHadesWhite15.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite15.centerx
                        hadesWhiteRect.centery = rectHadesWhite15.centery
                        if not hadesWhiteAbilityActivated:
                            counter += 1
                        else:
                            hadesWhiteAbilityCounter-=1
                        hadesWhitePlaying=False
                    elif rectHadesWhite16.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite16.centerx
                        hadesWhiteRect.centery = rectHadesWhite16.centery
                        if not hadesWhiteAbilityActivated:
                            counter += 1
                        else:
                            hadesWhiteAbilityCounter-=1
                        hadesWhitePlaying=False
                    elif rectHadesWhite17.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite17.centerx
                        hadesWhiteRect.centery = rectHadesWhite17.centery
                        if not hadesWhiteAbilityActivated:
                            counter += 1
                        else:
                            hadesWhiteAbilityCounter-=1
                        hadesWhitePlaying=False
                    elif rectHadesWhite18.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite18.centerx
                        hadesWhiteRect.centery = rectHadesWhite18.centery
                        if not hadesWhiteAbilityActivated:
                            counter += 1
                        else:
                            hadesWhiteAbilityCounter-=1
                        hadesWhitePlaying=False
                    elif rectHadesWhite19.collidepoint(event.pos):
                        hadesWhiteRect.centerx = rectHadesWhite19.centerx
                        hadesWhiteRect.centery = rectHadesWhite19.centery
                        if not hadesWhiteAbilityActivated:
                            counter += 1
                        else:
                            hadesWhiteAbilityCounter-=1
                        hadesWhitePlaying=False
                    else:
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        hadesWhitePlaying=False

                    if (hadesWhiteRect.centerx <= 480 or hadesWhiteRect.centerx >= 1440) or (hadesWhiteRect.centery <= 60 or hadesWhiteRect.centery >= 1020):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        if not hadesWhiteAbilityActivated:
                            counter-=1
                        else:
                            hadesWhiteAbilityCounter+=1
                        hadesWhitePlaying=False
                    if hadesWhiteRect.colliderect(plagueDoctorWhiteRect):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        if not hadesWhiteAbilityActivated:
                            counter-=1
                        else:
                            hadesWhiteAbilityCounter+=1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(archbishopWhiteRect):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        if not hadesWhiteAbilityActivated:
                            counter-=1
                        else:
                            hadesWhiteAbilityCounter+=1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(cardinalWhiteRect):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        if not hadesWhiteAbilityActivated:
                            counter-=1
                        else:
                            hadesWhiteAbilityCounter+=1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(persephoneWhiteRect):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        if not hadesWhiteAbilityActivated:
                            counter-=1
                        else:
                            hadesWhiteAbilityCounter+=1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(plagueDoctorWhiteRect1):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        if not hadesWhiteAbilityActivated:
                            counter-=1
                        else:
                            hadesWhiteAbilityCounter+=1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(cardinalWhiteRect1):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        if not hadesWhiteAbilityActivated:
                            counter-=1
                        else:
                            hadesWhiteAbilityCounter+=1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(archbishopWhiteRect1):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        if not hadesWhiteAbilityActivated:
                            counter-=1
                        else:
                            hadesWhiteAbilityCounter+=1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(warriorWhiteRect):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        if not hadesWhiteAbilityActivated:
                            counter-=1
                        else:
                            hadesWhiteAbilityCounter+=1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(legionaryWhiteRect):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        if not hadesWhiteAbilityActivated:
                            counter-=1
                        else:
                            hadesWhiteAbilityCounter+=1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(warriorWhiteRect1):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        if not hadesWhiteAbilityActivated:
                            counter-=1
                        else:
                            hadesWhiteAbilityCounter+=1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(legionaryWhiteRect1):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        if not hadesWhiteAbilityActivated:
                            counter-=1
                        else:
                            hadesWhiteAbilityCounter+=1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(warriorWhiteRect2):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        if not hadesWhiteAbilityActivated:
                            counter-=1
                        else:
                            hadesWhiteAbilityCounter+=1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(legionaryWhiteRect2):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        if not hadesWhiteAbilityActivated:
                            counter-=1
                        else:
                            hadesWhiteAbilityCounter+=1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(warriorWhiteRect3):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        if not hadesWhiteAbilityActivated:
                            counter-=1
                        else:
                            hadesWhiteAbilityCounter+=1
                        hadesWhitePlaying=False
                    elif hadesWhiteRect.colliderect(legionaryWhiteRect3):
                        hadesWhiteRect.centerx = hadesWhitexInit
                        hadesWhiteRect.centery = hadesWhiteyInit
                        if not hadesWhiteAbilityActivated:
                            counter-=1
                        else:
                            hadesWhiteAbilityCounter+=1
                        hadesWhitePlaying=False
                
                
                       
                if persephoneWhiteRect.collidepoint(event.pos) and not hadesWhiteAbilityActivated and persephoneWhiteRect.centerx!=step*2:
                    if not persephoneWhitePlaying:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                persephoneWhitePlaying=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                persephoneWhitePlaying=True
                elif persephoneWhitePlaying:
                    persephoneWhitexInit=persephoneWhiteRect.centerx
                    persephoneWhiteyInit=persephoneWhiteRect.centery
                    if persephoneWhiteAbilityActivated:
                        if rectPersephoneWhite1Ability.collidepoint(event.pos):
                            persephoneWhiteRect.centerx=rectPersephoneWhite1Ability.centerx
                            persephoneWhiteRect.centery=rectPersephoneWhite1Ability.centery
                            persephoneWhiteAbilityCounter-=1
                            persephoneWhitePlaying=False
                            counter+=1
                        elif rectPersephoneWhite2Ability.collidepoint(event.pos):
                            persephoneWhiteRect.centerx=rectPersephoneWhite2Ability.centerx
                            persephoneWhiteRect.centery=rectPersephoneWhite2Ability.centery
                            persephoneWhiteAbilityCounter-=1
                            persephoneWhitePlaying=False
                            counter+=1
                        elif rectPersephoneWhite3Ability.collidepoint(event.pos):
                            persephoneWhiteRect.centerx=rectPersephoneWhite3Ability.centerx
                            persephoneWhiteRect.centery=rectPersephoneWhite3Ability.centery
                            persephoneWhiteAbilityCounter-=1
                            persephoneWhitePlaying=False
                            counter+=1
                        elif rectPersephoneWhite4Ability.collidepoint(event.pos):
                            persephoneWhiteRect.centerx=rectPersephoneWhite4Ability.centerx
                            persephoneWhiteRect.centery=rectPersephoneWhite4Ability.centery
                            persephoneWhiteAbilityCounter-=1
                            persephoneWhitePlaying=False
                            counter+=1
                        elif rectPersephoneWhite5Ability.collidepoint(event.pos):
                            persephoneWhiteRect.centerx=rectPersephoneWhite5Ability.centerx
                            persephoneWhiteRect.centery=rectPersephoneWhite5Ability.centery
                            persephoneWhiteAbilityCounter-=1
                            persephoneWhitePlaying=False
                            counter+=1
                        elif rectPersephoneWhite6Ability.collidepoint(event.pos):
                            persephoneWhiteRect.centerx=rectPersephoneWhite6Ability.centerx
                            persephoneWhiteRect.centery=rectPersephoneWhite6Ability.centery
                            persephoneWhiteAbilityCounter-=1
                            persephoneWhitePlaying=False
                            counter+=1
                        elif rectPersephoneWhite7Ability.collidepoint(event.pos):
                            persephoneWhiteRect.centerx=rectPersephoneWhite7Ability.centerx
                            persephoneWhiteRect.centery=rectPersephoneWhite7Ability.centery
                            persephoneWhiteAbilityCounter-=1
                            persephoneWhitePlaying=False
                            counter+=1
                        elif rectPersephoneWhite8Ability.collidepoint(event.pos):
                            persephoneWhiteRect.centerx=rectPersephoneWhite8Ability.centerx
                            persephoneWhiteRect.centery=rectPersephoneWhite8Ability.centery
                            persephoneWhiteAbilityCounter-=1
                            persephoneWhitePlaying=False
                            counter+=1
                        elif rectPersephoneWhite9Ability.collidepoint(event.pos):
                            persephoneWhiteRect.centerx=rectPersephoneWhite9Ability.centerx
                            persephoneWhiteRect.centery=rectPersephoneWhite9Ability.centery
                            persephoneWhiteAbilityCounter-=1
                            persephoneWhitePlaying=False
                            counter+=1
                        elif rectPersephoneWhite10Ability.collidepoint(event.pos):
                            persephoneWhiteRect.centerx=rectPersephoneWhite10Ability.centerx
                            persephoneWhiteRect.centery=rectPersephoneWhite10Ability.centery
                            persephoneWhiteAbilityCounter-=1
                            persephoneWhitePlaying=False
                            counter+=1
                        elif rectPersephoneWhite11Ability.collidepoint(event.pos):
                            persephoneWhiteRect.centerx=rectPersephoneWhite11Ability.centerx
                            persephoneWhiteRect.centery=rectPersephoneWhite11Ability.centery
                            persephoneWhiteAbilityCounter-=1
                            persephoneWhitePlaying=False
                            counter+=1
                        elif rectPersephoneWhite12Ability.collidepoint(event.pos):
                            persephoneWhiteRect.centerx=rectPersephoneWhite12Ability.centerx
                            persephoneWhiteRect.centery=rectPersephoneWhite12Ability.centery
                            persephoneWhiteAbilityCounter-=1
                            persephoneWhitePlaying=False
                            counter+=1
                        elif rectPersephoneWhite13Ability.collidepoint(event.pos):
                            persephoneWhiteRect.centerx=rectPersephoneWhite13Ability.centerx
                            persephoneWhiteRect.centery=rectPersephoneWhite13Ability.centery
                            persephoneWhiteAbilityCounter-=1
                            persephoneWhitePlaying=False
                            counter+=1
                        elif rectPersephoneWhite14Ability.collidepoint(event.pos):
                            persephoneWhiteRect.centerx=rectPersephoneWhite14Ability.centerx
                            persephoneWhiteRect.centery=rectPersephoneWhite14Ability.centery
                            persephoneWhiteAbilityCounter-=1
                            persephoneWhitePlaying=False
                            counter+=1
                        elif rectPersephoneWhite15Ability.collidepoint(event.pos):
                            persephoneWhiteRect.centerx=rectPersephoneWhite15Ability.centerx
                            persephoneWhiteRect.centery=rectPersephoneWhite15Ability.centery
                            persephoneWhiteAbilityCounter-=1
                            persephoneWhitePlaying=False
                            counter+=1
                        elif rectPersephoneWhite16Ability.collidepoint(event.pos):
                            persephoneWhiteRect.centerx=rectPersephoneWhite16Ability.centerx
                            persephoneWhiteRect.centery=rectPersephoneWhite16Ability.centery
                            persephoneWhiteAbilityCounter-=1
                            persephoneWhitePlaying=False
                            counter+=1
                        elif rectPersephoneWhite17Ability.collidepoint(event.pos):
                            persephoneWhiteRect.centerx=rectPersephoneWhite17Ability.centerx
                            persephoneWhiteRect.centery=rectPersephoneWhite17Ability.centery
                            persephoneWhiteAbilityCounter-=1
                            persephoneWhitePlaying=False
                            counter+=1
                        elif rectPersephoneWhite18Ability.collidepoint(event.pos):
                            persephoneWhiteRect.centerx=rectPersephoneWhite18Ability.centerx
                            persephoneWhiteRect.centery=rectPersephoneWhite18Ability.centery
                            persephoneWhiteAbilityCounter-=1
                            persephoneWhitePlaying=False
                            counter+=1
                        elif rectPersephoneWhite19Ability.collidepoint(event.pos):
                            persephoneWhiteRect.centerx=rectPersephoneWhite19Ability.centerx
                            persephoneWhiteRect.centery=rectPersephoneWhite19Ability.centery
                            persephoneWhiteAbilityCounter-=1
                            persephoneWhitePlaying=False
                            counter+=1
                        else:
                            persephoneWhiteRect.centerx = persephoneWhitexInit
                            persephoneWhiteRect.centery = persephoneWhiteyInit
                            persephoneWhitePlaying=False
                    else:
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
                    if (persephoneWhiteRect.centerx <= 480 or persephoneWhiteRect.centerx >= 1440) or (persephoneWhiteRect.centery <= 60 or persephoneWhiteRect.centery >= 1020):
                        persephoneWhiteRect.centerx = persephoneWhitexInit
                        persephoneWhiteRect.centery = persephoneWhiteyInit
                        persephoneWhitePlaying=False
                        counter-=1
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
                     

                if cardinalWhiteRect1.collidepoint(event.pos) and not hadesWhiteAbilityActivated and cardinalWhiteRect.centerx!=step*3:
                    if not cardinalWhitePlaying1:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                cardinalWhitePlaying1=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                cardinalWhitePlaying1=True
                elif cardinalWhitePlaying1:
                    cardinalWhitexInit1=cardinalWhiteRect1.centerx
                    cardinalWhiteyInit1=cardinalWhiteRect1.centery
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
                    if (cardinalWhiteRect1.centerx <= 480 or cardinalWhiteRect1.centerx >= 1440) or (cardinalWhiteRect1.centery <= 60 or cardinalWhiteRect1.centery >= 1020):
                        cardinalWhiteRect1.centerx = cardinalWhitexInit1
                        cardinalWhiteRect1.centery = cardinalWhiteyInit1
                        cardinalWhitePlaying1=False
                        counter-=1
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
                if cardinalWhiteAbilityActivated_1:
                    if plagueDoctorBlackRect.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        plagueDoctorBlackxBefore=plagueDoctorBlackRect.centerx
                        plagueDoctorBlackyBefore=plagueDoctorBlackRect.centery
                        plagueDoctorBlackRect.centerx = screen_width-step
                        plagueDoctorBlackRect.centery = step
                        cardinalWhiteRectCopy_1.centerx=plagueDoctorBlackxBefore
                        cardinalWhiteRectCopy_1.centery=plagueDoctorBlackyBefore
                        counter+=1
                        cardinalWhiteAbilityActivated_1=False
                        cardinalWhiteAbilityCounter_1-=1
                    if archbishopBlackRect.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        archbishopBlackxBefore=archbishopBlackRect.centerx
                        archbishopBlackyBefore=archbishopBlackRect.centery
                        archbishopBlackRect.centerx = screen_width-step*2
                        archbishopBlackRect.centery = step
                        cardinalWhiteRectCopy_1.centerx=archbishopBlackxBefore
                        cardinalWhiteRectCopy_1.centery=archbishopBlackyBefore
                        counter+=1
                        cardinalWhiteAbilityActivated_1=False
                        cardinalWhiteAbilityCounter_1-=1
                    if cardinalBlackRect.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        cardinalBlackxBefore=cardinalBlackRect.centerx
                        cardinalBlackyBefore=cardinalBlackRect.centery
                        cardinalBlackRect.centerx = screen_width-step*3
                        cardinalBlackRect.centery = step
                        cardinalWhiteRectCopy_1.centerx=cardinalBlackxBefore
                        cardinalWhiteRectCopy_1.centery=cardinalBlackyBefore
                        counter+=1
                        cardinalWhiteAbilityActivated_1=False
                        cardinalWhiteAbilityCounter_1-=1
                    if cardinalBlackRect1.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        cardinalBlackxBefore_1=cardinalBlackRect1.centerx
                        cardinalBlackyBefore_1=cardinalBlackRect1.centery
                        cardinalBlackRect1.centerx = screen_width-step*3
                        cardinalBlackRect1.centery = step*2
                        cardinalWhiteRectCopy_1.centerx=cardinalBlackxBefore_1
                        cardinalWhiteRectCopy_1.centery=cardinalBlackyBefore_1
                        counter+=1
                        cardinalWhiteAbilityActivated_1=False
                        cardinalWhiteAbilityCounter_1-=1
                    if archbishopBlackRect1.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        archbishopBlackxBefore_1=archbishopBlackRect1.centerx
                        archbishopBlackyBefore_1=archbishopBlackRect1.centery
                        archbishopBlackRect1.centerx = screen_width-step
                        archbishopBlackRect1.centery = step*3
                        cardinalWhiteRectCopy_1.centerx=archbishopBlackxBefore_1
                        cardinalWhiteRectCopy_1.centery=archbishopBlackyBefore_1
                        counter+=1
                        cardinalWhiteAbilityActivated_1=False
                        cardinalWhiteAbilityCounter_1-=1
                    if plagueDoctorBlackRect1.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        plagueDoctorBlackxBefore_1=plagueDoctorBlackRect1.centerx
                        plagueDoctorBlackyBefore_1=plagueDoctorBlackRect1.centery
                        plagueDoctorBlackRect1.centerx = screen_width-step*2
                        plagueDoctorBlackRect1.centery = step*3
                        cardinalWhiteRectCopy_1.centerx=plagueDoctorBlackxBefore_1
                        cardinalWhiteRectCopy_1.centery=plagueDoctorBlackyBefore_1
                        counter+=1
                        cardinalWhiteAbilityActivated_1=False
                        cardinalWhiteAbilityCounter_1-=1
                    if legionaryBlackRect.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        legionaryBlackxBefore=legionaryBlackRect.centerx
                        legionaryBlackyBefore=legionaryBlackRect.centery
                        legionaryBlackRect.centerx = screen_width-step*3
                        legionaryBlackRect.centery = step*3
                        cardinalWhiteRectCopy_1.centerx=legionaryBlackxBefore
                        cardinalWhiteRectCopy_1.centery=legionaryBlackyBefore
                        cardinalWhiteAbilityActivated_1=False
                        cardinalWhiteAbilityCounter_1-=1
                    if warriorBlackRect.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        warriorBlackxBefore=warriorBlackRect.centerx
                        warriorBlackyBefore=warriorBlackRect.centery
                        warriorBlackRect.centerx = screen_width-step
                        warriorBlackRect.centery = step*4
                        cardinalWhiteRectCopy_1.centerx=warriorBlackxBefore
                        cardinalWhiteRectCopy_1.centery=warriorBlackyBefore
                        cardinalWhiteAbilityActivated_1=False
                        cardinalWhiteAbilityCounter_1-=1
                    if legionaryBlackRect1.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        legionaryBlackxBefore_1=legionaryBlackRect1.centerx
                        legionaryBlackyBefore_1=legionaryBlackRect1.centery
                        legionaryBlackRect1.centerx = screen_width-step*2
                        legionaryBlackRect1.centery = step*4
                        cardinalWhiteRectCopy_1.centerx=legionaryBlackxBefore_1
                        cardinalWhiteRectCopy_1.centery=legionaryBlackyBefore_1
                        cardinalWhiteAbilityActivated_1=False
                        cardinalWhiteAbilityCounter_1-=1
                    if warriorBlackRect1.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        warriorBlackxBefore_1=warriorBlackRect1.centerx
                        warriorBlackyBefore_1=warriorBlackRect1.centery
                        warriorBlackRect1.centerx = screen_width-step*3
                        warriorBlackRect1.centery = step*4
                        cardinalWhiteRectCopy_1.centerx=warriorBlackxBefore_1
                        cardinalWhiteRectCopy_1.centery=warriorBlackyBefore_1
                        cardinalWhiteAbilityActivated_1=False
                        cardinalWhiteAbilityCounter_1-=1
                    if legionaryBlackRect2.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        legionaryBlackxBefore_2=legionaryBlackRect2.centerx
                        legionaryBlackyBefore_2=legionaryBlackRect2.centery
                        legionaryBlackRect2.centerx = screen_width-step
                        legionaryBlackRect2.centery = step*5
                        cardinalWhiteRectCopy_1.centerx=legionaryBlackxBefore_2
                        cardinalWhiteRectCopy_1.centery=legionaryBlackyBefore_2
                        cardinalWhiteAbilityActivated_1=False
                        cardinalWhiteAbilityCounter_1-=1
                    if warriorBlackRect2.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        warriorBlackxBefore_2=warriorBlackRect2.centerx
                        warriorBlackyBefore_2=warriorBlackRect2.centery
                        warriorBlackRect2.centerx = screen_width-step*2
                        warriorBlackRect2.centery = step*5
                        cardinalWhiteRectCopy_1.centerx=warriorBlackxBefore_2
                        cardinalWhiteRectCopy_1.centery=warriorBlackyBefore_2
                        cardinalWhiteAbilityActivated_1=False
                        cardinalWhiteAbilityCounter_1-=1
                    if legionaryBlackRect3.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        legionaryBlackxBefore_3=legionaryBlackRect3.centerx
                        legionaryBlackyBefore_3=legionaryBlackRect3.centery
                        legionaryBlackRect3.centerx = screen_width-step*3
                        legionaryBlackRect3.centery = step*5
                        cardinalWhiteRectCopy_1.centerx=legionaryBlackxBefore_3
                        cardinalWhiteRectCopy_1.centery=legionaryBlackyBefore_3
                        cardinalWhiteAbilityActivated_1=False
                        cardinalWhiteAbilityCounter_1-=1
                    if warriorBlackRect3.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        counter+=1
                        warriorBlackxBefore_3=warriorBlackRect3.centerx
                        warriorBlackyBefore_3=warriorBlackRect3.centery
                        warriorBlackRect3.centerx = screen_width-step
                        warriorBlackRect3.centery = step*6
                        cardinalWhiteRectCopy_1.centerx=warriorBlackxBefore_3
                        cardinalWhiteRectCopy_1.centery=warriorBlackyBefore_3
                        cardinalWhiteAbilityActivated_1=False
                        cardinalWhiteAbilityCounter_1-=1

                if archbishopWhiteRect1.collidepoint(event.pos) and not hadesWhiteAbilityActivated and archbishopWhiteRect1.centerx!=step:
                    if not archbishopWhitePlaying1:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                archbishopWhitePlaying1=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                archbishopWhitePlaying1=True
                elif archbishopWhitePlaying1:
                    archbishopWhitexInit1=archbishopWhiteRect1.centerx
                    archbishopWhiteyInit1=archbishopWhiteRect1.centery
                    if rectArchbishopWhite1_1.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite1_1.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite1_1.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite2_1.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite2_1.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite2_1.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite3_1.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite3_1.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite3_1.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite4_1.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite4_1.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite4_1.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite5_1.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite5_1.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite5_1.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite6_1.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite6_1.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite6_1.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite7_1.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite7_1.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite7_1.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite8_1.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite8_1.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite8_1.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite9_1.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite9_1.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite9_1.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite10_1.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite10_1.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite10_1.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite11_1.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite11_1.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite11_1.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    elif rectArchbishopWhite12_1.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = rectArchbishopWhite12_1.centerx
                        archbishopWhiteRect1.centery = rectArchbishopWhite12_1.centery
                        counter += 1
                        archbishopWhitePlaying1=False
                    else:
                        archbishopWhiteRect1.centerx = archbishopWhitexInit1
                        archbishopWhiteRect1.centery = archbishopWhiteyInit1
                        archbishopWhitePlaying1=False
                    if (archbishopWhiteRect1.centerx <= 480 or archbishopWhiteRect1.centerx >= 1440) or (archbishopWhiteRect1.centery <= 60 or archbishopWhiteRect1.centery >= 1020):
                        archbishopWhiteRect1.centerx = archbishopWhitexInit1
                        archbishopWhiteRect1.centery = archbishopWhiteyInit1
                        archbishopWhitePlaying1=False
                        counter-=1
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
                if archbishopWhiteAbilityActivated_1:
                    if plagueDoctorBlackRect.collidepoint(event.pos):
                        plagueDoctorBlackRect.centerx = screen_width-step
                        plagueDoctorBlackRect.centery = step
                        archbishopWhiteFiguresCount_1+=1
                        archbishopWhitePlaying1=False
                        archbishopWhiteAbilityActivated_1=False
                        archbishopWhiteAbilityCounter_1-=1
                        counter+=1
                    if archbishopBlackRect.collidepoint(event.pos):
                        archbishopBlackRect.centerx = screen_width-step*2
                        archbishopBlackRect.centery = step
                        archbishopWhiteFiguresCount_1+=1
                        archbishopWhitePlaying1=False
                        archbishopWhiteAbilityActivated_1=False
                        archbishopWhiteAbilityCounter_1-=1
                        counter+=1
                    if cardinalBlackRect.collidepoint(event.pos):
                        cardinalBlackRect.centerx = screen_width-step*3
                        cardinalBlackRect.centery = step
                        archbishopWhiteFiguresCount_1+=1
                        archbishopWhitePlaying1=False
                        archbishopWhiteAbilityActivated_1=False
                        archbishopWhiteAbilityCounter_1-=1
                        counter+=1
                    if hadesBlackRect.collidepoint(event.pos):
                        hadesBlackRect.centerx = screen_width-step
                        hadesBlackRect.centery = step*2
                        archbishopWhiteFiguresCount_1+=1
                        archbishopWhitePlaying1=False
                        archbishopWhiteAbilityActivated_1=False
                        archbishopWhiteAbilityCounter_1-=1
                        counter+=1
                    if persephoneBlackRect.collidepoint(event.pos):
                        persephoneBlackRect.centerx = screen_width-step*2
                        persephoneBlackRect.centery = step*2
                        archbishopWhiteFiguresCount_1+=1
                        archbishopWhitePlaying1=False
                        archbishopWhiteAbilityActivated_1=False
                        archbishopWhiteAbilityCounter_1-=1
                        counter+=1
                    if cardinalBlackRect1.collidepoint(event.pos):
                        cardinalBlackRect1.centerx = screen_width-step*3
                        cardinalBlackRect1.centery = step*2
                        archbishopWhiteFiguresCount_1+=1
                        archbishopWhitePlaying1=False
                        archbishopWhiteAbilityActivated_1=False
                        archbishopWhiteAbilityCounter_1-=1
                        counter+=1
                    if archbishopBlackRect1.collidepoint(event.pos):
                        archbishopBlackRect1.centerx = screen_width-step
                        archbishopBlackRect1.centery = step*3
                        archbishopWhiteFiguresCount_1+=1
                        archbishopWhitePlaying1=False
                        archbishopWhiteAbilityActivated_1=False
                        archbishopWhiteAbilityCounter_1-=1
                        counter+=1
                    if plagueDoctorBlackRect1.collidepoint(event.pos):
                        plagueDoctorBlackRect1.centerx = screen_width-step*2
                        plagueDoctorBlackRect1.centery = step*3
                        archbishopWhiteFiguresCount_1+=1
                        archbishopWhitePlaying1=False
                        archbishopWhiteAbilityActivated_1=False
                        archbishopWhiteAbilityCounter_1-=1
                        counter+=1
                    if legionaryBlackRect.collidepoint(event.pos):
                        legionaryBlackRect.centerx = screen_width-step*3
                        legionaryBlackRect.centery = step*3
                        archbishopWhiteFiguresCount_1+=1
                        archbishopWhitePlaying1=False
                        archbishopWhiteAbilityActivated_1=False
                        archbishopWhiteAbilityCounter_1-=1
                        counter+=1
                    if warriorBlackRect.collidepoint(event.pos):
                        warriorBlackRect.centerx = screen_width-step
                        warriorBlackRect.centery = step*4
                        archbishopWhiteFiguresCount_1+=1
                        archbishopWhitePlaying1=False
                        archbishopWhiteAbilityActivated_1=False
                        archbishopWhiteAbilityCounter_1-=1
                        counter+=1
                    if legionaryBlackRect1.collidepoint(event.pos):
                        legionaryBlackRect1.centerx = screen_width-step*2
                        legionaryBlackRect1.centery = step*4
                        archbishopWhiteFiguresCount_1+=1
                        archbishopWhitePlaying1=False
                        archbishopWhiteAbilityActivated_1=False
                        archbishopWhiteAbilityCounter_1-=1
                        counter+=1
                    if warriorBlackRect1.collidepoint(event.pos):
                        warriorBlackRect1.centerx = screen_width-step*3
                        warriorBlackRect1.centery = step*4
                        archbishopWhiteFiguresCount_1+=1
                        archbishopWhitePlaying1=False
                        archbishopWhiteAbilityActivated_1=False
                        archbishopWhiteAbilityCounter_1-=1
                        counter+=1
                    if legionaryBlackRect2.collidepoint(event.pos):
                        legionaryBlackRect2.centerx = screen_width-step
                        legionaryBlackRect2.centery = step*5
                        archbishopWhiteFiguresCount_1+=1
                        archbishopWhitePlaying1=False
                        archbishopWhiteAbilityActivated_1=False
                        archbishopWhiteAbilityCounter_1-=1
                        counter+=1
                    if warriorBlackRect2.collidepoint(event.pos):
                        warriorBlackRect2.centerx = screen_width-step*2
                        warriorBlackRect2.centery = step*5
                        archbishopWhiteFiguresCount_1+=1
                        archbishopWhitePlaying1=False
                        archbishopWhiteAbilityActivated_1=False
                        archbishopWhiteAbilityCounter_1-=1
                        counter+=1
                    if legionaryBlackRect3.collidepoint(event.pos):
                        legionaryBlackRect3.centerx = screen_width-step*3
                        legionaryBlackRect3.centery = step*5
                        archbishopWhiteFiguresCount_1+=1
                        archbishopWhitePlaying1=False
                        archbishopWhiteAbilityActivated_1=False
                        archbishopWhiteAbilityCounter_1-=1
                        counter+=1
                    if warriorBlackRect3.collidepoint(event.pos):
                        warriorBlackRect3.centerx = screen_width-step
                        warriorBlackRect3.centery = step*6
                        archbishopWhiteFiguresCount_1+=1
                        archbishopWhitePlaying1=False
                        archbishopWhiteAbilityActivated_1=False
                        archbishopWhiteAbilityCounter_1-=1
                        counter+=1




                if plagueDoctorWhiteRect1.collidepoint(event.pos) and not hadesWhiteAbilityActivated and plagueDoctorWhiteRect1.centerx!=step*2:
                    if not plagueDoctorWhitePlaying1:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                plagueDoctorWhitePlaying1=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                plagueDoctorWhitePlaying1=True
                elif plagueDoctorWhitePlaying1:
                    plagueWhitexInit1=plagueDoctorWhiteRect1.centerx
                    plagueWhiteyInit1=plagueDoctorWhiteRect1.centery
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
                        plagueDoctorWhitePlaying1=False
                    if (plagueDoctorWhiteRect1.centerx <= 480 or plagueDoctorWhiteRect1.centerx >= 1440) or (plagueDoctorWhiteRect1.centery <= 60 or plagueDoctorWhiteRect1.centery >= 1020):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        plagueDoctorWhitePlaying1=False
                        counter-=1
                    if plagueDoctorWhiteRect1.colliderect(plagueDoctorWhiteRect):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                        plagueDoctorWhitePlaying1=False
                    elif plagueDoctorWhiteRect1.colliderect(archbishopWhiteRect):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                        plagueDoctorWhitePlaying1=False
                    elif plagueDoctorWhiteRect1.colliderect(cardinalWhiteRect):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                        plagueDoctorWhitePlaying1=False
                    elif plagueDoctorWhiteRect1.colliderect(hadesWhiteRect):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                        plagueDoctorWhitePlaying1=False
                    elif plagueDoctorWhiteRect1.colliderect(cardinalWhiteRect1):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                        plagueDoctorWhitePlaying1=False
                    elif plagueDoctorWhiteRect1.colliderect(persephoneWhiteRect):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                        plagueDoctorWhitePlaying1=False
                    elif plagueDoctorWhiteRect1.colliderect(archbishopWhiteRect1):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                        plagueDoctorWhitePlaying1=False
                    elif plagueDoctorWhiteRect1.colliderect(warriorWhiteRect):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                        plagueDoctorWhitePlaying1=False
                    elif plagueDoctorWhiteRect1.colliderect(legionaryWhiteRect):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                        plagueDoctorWhitePlaying1=False
                    elif plagueDoctorWhiteRect1.colliderect(warriorWhiteRect1):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                        plagueDoctorWhitePlaying1=False
                    elif plagueDoctorWhiteRect1.colliderect(legionaryWhiteRect1):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                        plagueDoctorWhitePlaying1=False
                    elif plagueDoctorWhiteRect1.colliderect(warriorWhiteRect2):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                        plagueDoctorWhitePlaying1=False
                    elif plagueDoctorWhiteRect1.colliderect(legionaryWhiteRect2):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                        plagueDoctorWhitePlaying1=False
                    elif plagueDoctorWhiteRect1.colliderect(warriorWhiteRect3):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                        plagueDoctorWhitePlaying1=False
                    elif plagueDoctorWhiteRect1.colliderect(legionaryWhiteRect3):
                        plagueDoctorWhiteRect1.centerx = plagueWhitexInit1
                        plagueDoctorWhiteRect1.centery = plagueWhiteyInit1
                        counter -= 1
                        plagueDoctorWhitePlaying1=False
                    if rectPlagueDoctorWhiteAbilityActivated_1:
                        if archbishopWhiteRect.collidepoint(event.pos) and archbishopWhiteRect.centerx==step*2:
                            archbishopWhiteRect.centerx=archbishopWhitexInit
                            archbishopWhiteRect.centery=archbishopWhiteyInit
                            counter += 1
                            plagueDoctorWhitePlaying1=False
                            rectPlagueDoctorWhiteAbilityActivated_1=False
                            rectPlagueDoctorWhiteAbilityCounter_1-=1
                        elif cardinalWhiteRect.collidepoint(event.pos) and cardinalWhiteRect.centerx==step*3:
                            cardinalWhiteRect.centerx=cardinalWhitexInit
                            cardinalWhiteRect.centery=cardinalWhiteyInit
                            counter += 1
                            plagueDoctorWhitePlaying1=False
                            rectPlagueDoctorWhiteAbilityActivated_1=False
                            rectPlagueDoctorWhiteAbilityCounter_1-=1
                        elif cardinalWhiteRect1.collidepoint(event.pos) and cardinalWhiteRect1.centerx==step*3:
                            cardinalWhiteRect1.centerx=cardinalWhitexInit1
                            cardinalWhiteRect1.centery=cardinalWhiteyInit1
                            counter += 1
                            plagueDoctorWhitePlaying1=False
                            rectPlagueDoctorWhiteAbilityActivated_1=False
                            rectPlagueDoctorWhiteAbilityCounter_1-=1
                        elif archbishopWhiteRect1.collidepoint(event.pos) and archbishopWhiteRect.centerx==step:
                            archbishopWhiteRect1.centerx=archbishopWhitexInit1
                            archbishopWhiteRect1.centery=archbishopWhiteyInit1
                            counter += 1
                            plagueDoctorWhitePlaying1=False
                            rectPlagueDoctorWhiteAbilityActivated_1=False
                            rectPlagueDoctorWhiteAbilityCounter_1-=1
                        elif warriorWhiteRect.collidepoint(event.pos) and warriorWhiteRect.centerx==step:
                            warriorWhiteRect.centerx=warriorWhitexInit
                            warriorWhiteRect.centery=warriorWhiteyInit
                            counter += 1
                            plagueDoctorWhitePlaying1=False
                            rectPlagueDoctorWhiteAbilityActivated_1=False
                            rectPlagueDoctorWhiteAbilityCounter_1-=1
                        elif legionaryWhiteRect.collidepoint(event.pos) and legionaryWhiteRect.centerx==step*3:
                            legionaryWhiteRect.centerx=legionaryWhitexInit
                            legionaryWhiteRect.centery=legionaryWhiteyInit
                            counter += 1
                            plagueDoctorWhitePlaying1=False
                            rectPlagueDoctorWhiteAbilityActivated_1=False
                            rectPlagueDoctorWhiteAbilityCounter_1-=1
                        elif warriorWhiteRect1.collidepoint(event.pos) and warriorWhiteRect1.centerx==step*3:
                            warriorWhiteRect1.centerx=warriorWhitexInit1
                            warriorWhiteRect1.centery=warriorWhiteyInit1
                            counter += 1
                            plagueDoctorWhitePlaying1=False
                            rectPlagueDoctorWhiteAbilityActivated_1=False
                            rectPlagueDoctorWhiteAbilityCounter_1-=1
                        elif legionaryWhiteRect1.collidepoint(event.pos) and legionaryWhiteRect1.centerx==step*2:
                            legionaryWhiteRect1.centerx=legionaryWhitexInit1
                            legionaryWhiteRect1.centery=legionaryWhiteyInit1
                            counter += 1
                            plagueDoctorWhitePlaying1=False
                            rectPlagueDoctorWhiteAbilityActivated_1=False
                            rectPlagueDoctorWhiteAbilityCounter_1-=1
                        elif warriorWhiteRect2.collidepoint(event.pos) and warriorWhiteRect2.centerx==step*2:
                            warriorWhiteRect2.centerx=warriorWhitexInit2
                            warriorWhiteRect2.centery=warriorWhiteyInit2
                            counter += 1
                            plagueDoctorWhitePlaying1=False
                            rectPlagueDoctorWhiteAbilityActivated_1=False
                            rectPlagueDoctorWhiteAbilityCounter_1-=1
                        elif legionaryWhiteRect2.collidepoint(event.pos) and legionaryWhiteRect2.centerx==step:
                            legionaryWhiteRect2.centerx=legionaryWhitexInit2
                            legionaryWhiteRect2.centery=legionaryWhiteyInit2
                            counter += 1
                            plagueDoctorWhitePlaying1=False
                            rectPlagueDoctorWhiteAbilityActivated_1=False
                            rectPlagueDoctorWhiteAbilityCounter_1-=1
                        elif warriorWhiteRect3.collidepoint(event.pos) and warriorWhiteRect3.centerx==step:
                            warriorWhiteRect3.centerx=warriorWhitexInit3
                            warriorWhiteRect3.centery=warriorWhiteyInit3
                            counter += 1
                            plagueDoctorWhitePlaying1=False
                            rectPlagueDoctorWhiteAbilityActivated_1=False
                            rectPlagueDoctorWhiteAbilityCounter_1-=1
                        elif legionaryWhiteRect3.collidepoint(event.pos) and legionaryWhiteRect3.centerx==step*3:
                            legionaryWhiteRect3.centerx=legionaryWhitexInit3
                            legionaryWhiteRect3.centery=legionaryWhiteyInit3
                            counter += 1
                            plagueDoctorWhitePlaying1=False  
                            rectPlagueDoctorWhiteAbilityActivated_1=False
                            rectPlagueDoctorWhiteAbilityCounter_1-=1
                        elif cardinalWhiteRectCopy.collidepoint(event.pos) and cardinalWhiteRectCopy.centerx==step:
                            cardinalWhiteRectCopy.centerx=cardinalWhitexInitCopy
                            cardinalWhiteRectCopy.centery=cardinalWhiteyInitCopy
                            counter += 1
                            plagueDoctorWhitePlaying1=False  
                            rectPlagueDoctorWhiteAbilityActivated_1=False
                            rectPlagueDoctorWhiteAbilityCounter_1-=1
                        elif cardinalWhiteRectCopy_1.collidepoint(event.pos) and cardinalWhiteRectCopy_1.centerx==step:
                            cardinalWhiteRectCopy_1.centerx=cardinalWhitexInitCopy1
                            cardinalWhiteRectCopy_1.centery=cardinalWhiteyInitCopy1
                            counter += 1
                            plagueDoctorWhitePlaying1=False  
                            rectPlagueDoctorWhiteAbilityActivated_1=False
                            rectPlagueDoctorWhiteAbilityCounter_1-=1
                        else:
                            rectPlagueDoctorWhiteAbilityActivated_1=False
                            plagueDoctorWhitePlaying1=False  

                if warriorWhiteRect.collidepoint(event.pos) and not hadesWhiteAbilityActivated and warriorWhiteRect.centerx!=step:
                    if not warriorWhitePlaying:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                warriorWhitePlaying=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                warriorWhitePlaying=True
                elif warriorWhitePlaying:
                    warriorWhitexInit=warriorWhiteRect.centerx
                    warriorWhiteyInit=warriorWhiteRect.centery
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
                    if (warriorWhiteRect.centerx <= 480 or warriorWhiteRect.centerx >= 1440) or (warriorWhiteRect.centery <= 60 or warriorWhiteRect.centery >= 1020):
                        warriorWhiteRect.centerx = warriorWhitexInit
                        warriorWhiteRect.centery = warriorWhiteyInit
                        warriorWhitePlaying=False
                        counter-=1
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
                            
                if legionaryWhiteRect.collidepoint(event.pos) and not hadesWhiteAbilityActivated and legionaryWhiteRect.centerx!=step*3:
                    if not legionaryWhitePlaying:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                legionaryWhitePlaying=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                legionaryWhitePlaying=True
                elif legionaryWhitePlaying:
                    legionaryWhitexInit=legionaryWhiteRect.centerx
                    legionaryWhiteyInit=legionaryWhiteRect.centery
                    if rectLegionaryWhite1.collidepoint(event.pos):
                        rectLegionaryWhitexAbility=legionaryWhiteRect.centerx
                        rectLegionaryWhiteyAbility=legionaryWhiteRect.centery
                        legionaryWhiteRect.centerx = rectLegionaryWhite1.centerx
                        legionaryWhiteRect.centery = rectLegionaryWhite1.centery
                        counter += 1
                        legionaryWhitePlaying=False
                    elif rectLegionaryWhite2.collidepoint(event.pos):
                        rectLegionaryWhitexAbility=legionaryWhiteRect.centerx
                        rectLegionaryWhiteyAbility=legionaryWhiteRect.centery
                        legionaryWhiteRect.centerx = rectLegionaryWhite2.centerx
                        legionaryWhiteRect.centery = rectLegionaryWhite2.centery
                        counter += 1
                        legionaryWhitePlaying=False
                    elif rectLegionaryWhite3.collidepoint(event.pos):
                        rectLegionaryWhitexAbility=legionaryWhiteRect.centerx
                        rectLegionaryWhiteyAbility=legionaryWhiteRect.centery
                        legionaryWhiteRect.centerx = rectLegionaryWhite3.centerx
                        legionaryWhiteRect.centery = rectLegionaryWhite3.centery
                        counter += 1
                        legionaryWhitePlaying=False
                    else:
                        legionaryWhiteRect.centerx = legionaryWhitexInit
                        legionaryWhiteRect.centery = legionaryWhiteyInit
                        legionaryWhitePlaying=False
                    if (legionaryWhiteRect.centerx <= 480 or legionaryWhiteRect.centerx >= 1440) or (legionaryWhiteRect.centery <= 60 or legionaryWhiteRect.centery >= 1020):
                        legionaryWhiteRect.centerx = legionaryWhitexInit
                        legionaryWhiteRect.centery = legionaryWhiteyInit
                        legionaryWhitePlaying=False
                        counter-=1
                    if legionaryWhiteRect.colliderect(plagueDoctorWhiteRect):
                        legionaryWhiteRect.centerx = legionaryWhitexInit
                        legionaryWhiteRect.centery = legionaryWhiteyInit
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect.colliderect(archbishopWhiteRect):
                        legionaryWhiteRect.centerx = legionaryWhitexInit
                        legionaryWhiteRect.centery = legionaryWhiteyInit
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect.colliderect(cardinalWhiteRect):
                        legionaryWhiteRect.centerx = legionaryWhitexInit
                        legionaryWhiteRect.centery = legionaryWhiteyInit
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect.colliderect(hadesWhiteRect):
                        legionaryWhiteRect.centerx = legionaryWhitexInit
                        legionaryWhiteRect.centery = legionaryWhiteyInit
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect.colliderect(cardinalWhiteRect1):
                        legionaryWhiteRect.centerx = legionaryWhitexInit
                        legionaryWhiteRect.centery = legionaryWhiteyInit
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect.colliderect(persephoneWhiteRect):
                        legionaryWhiteRect.centerx = legionaryWhitexInit
                        legionaryWhiteRect.centery = legionaryWhiteyInit
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect.colliderect(archbishopWhiteRect1):
                        legionaryWhiteRect.centerx = legionaryWhitexInit
                        legionaryWhiteRect.centery = legionaryWhiteyInit
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect.colliderect(plagueDoctorWhiteRect1):
                        legionaryWhiteRect.centerx = legionaryWhitexInit
                        legionaryWhiteRect.centery = legionaryWhiteyInit
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect.colliderect(warriorWhiteRect):
                        legionaryWhiteRect.centerx = legionaryWhitexInit
                        legionaryWhiteRect.centery = legionaryWhiteyInit
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect.colliderect(legionaryWhiteRect1):
                        legionaryWhiteRect.centerx = legionaryWhitexInit
                        legionaryWhiteRect.centery = legionaryWhiteyInit
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect.colliderect(warriorWhiteRect1):
                        legionaryWhiteRect.centerx = legionaryWhitexInit
                        legionaryWhiteRect.centery = legionaryWhiteyInit
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect.colliderect(warriorWhiteRect2):
                        legionaryWhiteRect.centerx = legionaryWhitexInit
                        legionaryWhiteRect.centery = legionaryWhiteyInit
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect.colliderect(legionaryWhiteRect2):
                        legionaryWhiteRect.centerx = legionaryWhitexInit
                        legionaryWhiteRect.centery = legionaryWhiteyInit
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect.colliderect(warriorWhiteRect3):
                        legionaryWhiteRect.centerx = legionaryWhitexInit
                        legionaryWhiteRect.centery = legionaryWhiteyInit
                        counter -= 1
                        legionaryWhitePlaying=False
                    elif legionaryWhiteRect.colliderect(legionaryWhiteRect3):
                        legionaryWhiteRect.centerx = legionaryWhitexInit
                        legionaryWhiteRect.centery = legionaryWhiteyInit
                        counter -= 1
                        legionaryWhitePlaying=False
                       
                if warriorWhiteRect1.collidepoint(event.pos) and not hadesWhiteAbilityActivated and warriorWhiteRect1.centerx!=step*3:
                    if not warriorWhitePlaying1:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                warriorWhitePlaying1=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                warriorWhitePlaying1=True
                elif warriorWhitePlaying1:
                    warriorWhitexInit1=warriorWhiteRect1.centerx
                    warriorWhiteyInit1=warriorWhiteRect1.centery
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
                    if (warriorWhiteRect1.centerx <= 480 or warriorWhiteRect1.centerx >= 1440) or (warriorWhiteRect1.centery <= 60 or warriorWhiteRect1.centery >= 1020):
                        warriorWhiteRect1.centerx = warriorWhitexInit1
                        warriorWhiteRect1.centery = warriorWhitexInit1
                        warriorWhitePlaying1=False
                        counter-=1
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

                if legionaryWhiteRect1.collidepoint(event.pos) and not hadesWhiteAbilityActivated and legionaryWhiteRect1.centerx!=step*2:
                    if not legionaryWhitePlaying1:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                legionaryWhitePlaying1=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                legionaryWhitePlaying1=True
                elif legionaryWhitePlaying1:
                    legionaryWhitexInit1=legionaryWhiteRect1.centerx
                    legionaryWhiteyInit1=legionaryWhiteRect1.centery
                    if rectLegionaryWhite1_1.collidepoint(event.pos):
                        rectLegionaryWhitexAbility_1=legionaryWhiteRect1.centerx
                        rectLegionaryWhiteyAbility_1=legionaryWhiteRect1.centery
                        legionaryWhiteRect1.centerx = rectLegionaryWhite1_1.centerx
                        legionaryWhiteRect1.centery = rectLegionaryWhite1_1.centery
                        counter += 1
                        legionaryWhitePlaying1=False
                    elif rectLegionaryWhite2_1.collidepoint(event.pos):
                        rectLegionaryWhitexAbility_1=legionaryWhiteRect1.centerx
                        rectLegionaryWhiteyAbility_1=legionaryWhiteRect1.centery
                        legionaryWhiteRect1.centerx = rectLegionaryWhite2_1.centerx
                        legionaryWhiteRect1.centery = rectLegionaryWhite2_1.centery
                        counter += 1
                        legionaryWhitePlaying1=False
                    elif rectLegionaryWhite3_1.collidepoint(event.pos):
                        rectLegionaryWhitexAbility_1=legionaryWhiteRect1.centerx
                        rectLegionaryWhiteyAbility_1=legionaryWhiteRect1.centery
                        legionaryWhiteRect1.centerx = rectLegionaryWhite3_1.centerx
                        legionaryWhiteRect1.centery = rectLegionaryWhite3_1.centery
                        counter += 1
                        legionaryWhitePlaying1=False
                    else:
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        legionaryWhitePlaying1=False
                    if (legionaryWhiteRect1.centerx <= 480 or legionaryWhiteRect1.centerx >= 1440) or (legionaryWhiteRect1.centery <= 60 or legionaryWhiteRect1.centery >= 1020):
                        legionaryWhiteRect1.centerx = legionaryWhitexInit1
                        legionaryWhiteRect1.centery = legionaryWhiteyInit1
                        legionaryWhitePlaying1=False
                        counter-=1
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
                    

                if warriorWhiteRect2.collidepoint(event.pos) and not hadesWhiteAbilityActivated and warriorWhiteRect2.centerx!=step*2:
                    if not warriorWhitePlaying2:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                warriorWhitePlaying2=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                warriorWhitePlaying2=True
                elif warriorWhitePlaying2:
                    warriorWhitexInit2=warriorWhiteRect2.centerx
                    warriorWhiteyInit2=warriorWhiteRect2.centery
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
                    if (warriorWhiteRect2.centerx <= 480 or warriorWhiteRect2.centerx >= 1440) or (warriorWhiteRect2.centery <= 60 or warriorWhiteRect2.centery >= 1020):
                        warriorWhiteRect2.centerx = warriorWhitexInit2
                        warriorWhiteRect2.centery = warriorWhiteyInit2
                        warriorWhitePlaying2=False
                        counter-=1
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


                if legionaryWhiteRect2.collidepoint(event.pos) and not hadesWhiteAbilityActivated and legionaryWhiteRect2.centerx!=step:
                    if not legionaryWhitePlaying2:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                legionaryWhitePlaying2=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                legionaryWhitePlaying2=True
                elif legionaryWhitePlaying2:
                    legionaryWhitexInit2=legionaryWhiteRect2.centerx
                    legionaryWhiteyInit2=legionaryWhiteRect2.centery
                    if rectLegionaryWhite1_2.collidepoint(event.pos):
                        rectLegionaryWhitexAbility_2=legionaryWhiteRect2.centerx
                        rectLegionaryWhiteyAbility_2=legionaryWhiteRect2.centery
                        legionaryWhiteRect2.centerx = rectLegionaryWhite1_2.centerx
                        legionaryWhiteRect2.centery = rectLegionaryWhite1_2.centery
                        counter += 1
                        legionaryWhitePlaying2=False
                    elif rectLegionaryWhite2_2.collidepoint(event.pos):
                        rectLegionaryWhitexAbility_2=legionaryWhiteRect2.centerx
                        rectLegionaryWhiteyAbility_2=legionaryWhiteRect2.centery
                        legionaryWhiteRect2.centerx = rectLegionaryWhite2_2.centerx
                        legionaryWhiteRect2.centery = rectLegionaryWhite2_2.centery
                        counter += 1
                        legionaryWhitePlaying2=False
                    elif rectLegionaryWhite3_2.collidepoint(event.pos):
                        rectLegionaryWhitexAbility_2=legionaryWhiteRect2.centerx
                        rectLegionaryWhiteyAbility_2=legionaryWhiteRect2.centery
                        legionaryWhiteRect2.centerx = rectLegionaryWhite3_2.centerx
                        legionaryWhiteRect2.centery = rectLegionaryWhite3_2.centery
                        counter += 1
                        legionaryWhitePlaying2=False
                    else:
                        legionaryWhiteRect2.centerx = legionaryWhitexInit2
                        legionaryWhiteRect2.centery = legionaryWhiteyInit2
                        legionaryWhitePlaying2=False
                    if (legionaryWhiteRect2.centerx <= 480 or legionaryWhiteRect2.centerx >= 1440) or (legionaryWhiteRect2.centery <= 60 or legionaryWhiteRect2.centery >= 1020):
                        legionaryWhiteRect2.centerx = legionaryWhitexInit2
                        legionaryWhiteRect2.centery = legionaryWhiteyInit2
                        legionaryWhitePlaying2=False
                        counter-=1
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

                if warriorWhiteRect3.collidepoint(event.pos) and not hadesWhiteAbilityActivated and warriorWhiteRect3.centerx!=step:
                    if not warriorWhitePlaying3:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                warriorWhitePlaying3=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                warriorWhitePlaying3=True
                elif warriorWhitePlaying3:
                    warriorWhitexInit3=warriorWhiteRect3.centerx
                    warriorWhiteyInit3=warriorWhiteRect3.centery
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
                    if (warriorWhiteRect3.centerx <= 480 or warriorWhiteRect3.centerx >= 1440) or (warriorWhiteRect3.centery <= 60 or warriorWhiteRect3.centery >= 1020):
                        warriorWhiteRect3.centerx = warriorWhitexInit3
                        warriorWhiteRect3.centery = warriorWhiteyInit3
                        warriorWhitePlaying3=False
                        counter-=1
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


                if legionaryWhiteRect3.collidepoint(event.pos) and not hadesWhiteAbilityActivated and legionaryWhiteRect3.centerx!=step*3:
                    if not legionaryWhitePlaying3:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                legionaryWhitePlaying3=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                legionaryWhitePlaying3=True
                elif legionaryWhitePlaying3:
                    legionaryWhitexInit3=legionaryWhiteRect3.centerx
                    legionaryWhiteyInit3=legionaryWhiteRect3.centery
                    if rectLegionaryWhite1_3.collidepoint(event.pos):
                        rectLegionaryWhitexAbility_3=legionaryWhiteRect3.centerx
                        rectLegionaryWhiteyAbility_3=legionaryWhiteRect3.centery
                        legionaryWhiteRect3.centerx = rectLegionaryWhite1_3.centerx
                        legionaryWhiteRect3.centery = rectLegionaryWhite1_3.centery
                        counter += 1
                        legionaryWhitePlaying3=False
                    elif rectLegionaryWhite2_3.collidepoint(event.pos):
                        rectLegionaryWhitexAbility_3=legionaryWhiteRect3.centerx
                        rectLegionaryWhiteyAbility_3=legionaryWhiteRect3.centery
                        legionaryWhiteRect3.centerx = rectLegionaryWhite2_3.centerx
                        legionaryWhiteRect3.centery = rectLegionaryWhite2_3.centery
                        counter += 1
                        legionaryWhitePlaying3=False
                    elif rectLegionaryWhite3_3.collidepoint(event.pos):
                        rectLegionaryWhitexAbility_3=legionaryWhiteRect3.centerx
                        rectLegionaryWhiteyAbility_3=legionaryWhiteRect3.centery
                        legionaryWhiteRect3.centerx = rectLegionaryWhite3_3.centerx
                        legionaryWhiteRect3.centery = rectLegionaryWhite3_3.centery
                        counter += 1
                        legionaryWhitePlaying3=False
                    else:
                        legionaryWhiteRect3.centerx = legionaryWhitexInit3
                        legionaryWhiteRect3.centery = legionaryWhiteyInit3
                        legionaryWhitePlaying3=False
                    if (legionaryWhiteRect3.centerx <= 480 or legionaryWhiteRect3.centerx >= 1440) or (legionaryWhiteRect3.centery <= 60 or legionaryWhiteRect3.centery >= 1020):
                        legionaryWhiteRect3.centerx = legionaryWhitexInit3
                        legionaryWhiteRect3.centery = legionaryWhiteyInit3
                        legionaryWhitePlaying3=False
                        counter-=1
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

                if cardinalWhiteRectCopy.collidepoint(event.pos) and counter%2==0 and not hadesWhiteAbilityActivated and cardinalWhiteRectCopy.centerx!=step*2:
                    if not cardinalWhitePlayingCopy:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                cardinalWhitePlayingCopy=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                cardinalWhitePlayingCopy=True
                elif cardinalWhitePlayingCopy:
                    cardinalWhitexInitCopy=cardinalWhiteRectCopy.centerx
                    cardinalWhiteyInitCopy=cardinalWhiteRectCopy.centery
                    if rectCardinalWhiteCopy1.collidepoint(event.pos):
                        cardinalWhiteRectCopy.centerx=rectCardinalWhiteCopy1.centerx
                        cardinalWhiteRectCopy.centery=rectCardinalWhiteCopy1.centery
                        counter += 1
                        cardinalWhitePlayingCopy=False
                    elif rectCardinalWhiteCopy2.collidepoint(event.pos):
                        cardinalWhiteRectCopy.centerx=rectCardinalWhiteCopy2.centerx
                        cardinalWhiteRectCopy.centery=rectCardinalWhiteCopy2.centery
                        counter += 1
                        cardinalWhitePlayingCopy=False
                    elif rectCardinalWhiteCopy3.collidepoint(event.pos):
                        cardinalWhiteRectCopy.centerx=rectCardinalWhiteCopy3.centerx
                        cardinalWhiteRectCopy.centery=rectCardinalWhiteCopy3.centery
                        counter += 1
                        cardinalWhitePlayingCopy=False
                    elif rectCardinalWhiteCopy4.collidepoint(event.pos):
                        cardinalWhiteRectCopy.centerx=rectCardinalWhiteCopy4.centerx
                        cardinalWhiteRectCopy.centery=rectCardinalWhiteCopy4.centery
                        counter += 1
                        cardinalWhitePlayingCopy=False
                    else:
                        cardinalWhiteRectCopy.centerx=cardinalWhitexInitCopy
                        cardinalWhiteRectCopy.centery=cardinalWhiteyInitCopy
                        cardinalWhitePlayingCopy=False
                    if (cardinalWhiteRectCopy.centerx <= 480 or cardinalWhiteRectCopy.centerx >= 1440) or (cardinalWhiteRectCopy.centery <= 60 or cardinalWhiteRectCopy.centery >= 1020):
                        cardinalWhiteRectCopy.centerx = cardinalWhitexInitCopy
                        cardinalWhiteRectCopy.centery = cardinalWhiteyInitCopy
                        cardinalWhitePlayingCopy=False
                        counter-=1
                
                if cardinalWhiteRectCopy_1.collidepoint(event.pos) and counter%2==0 and not hadesWhiteAbilityActivated and cardinalWhiteRectCopy_1!=step*3:
                    if not cardinalWhitePlayingCopy1:
                        for x,playing in enumerate(figuresWhitePlaying):
                            if playing==True:
                                playing=False
                                cardinalWhitePlayingCopy1=True
                                break
                            elif x==len(figuresWhitePlaying)-1:
                                cardinalWhitePlayingCopy1=True
                elif cardinalWhitePlayingCopy1:
                    cardinalWhitexInitCopy1=cardinalWhiteRectCopy_1.centerx
                    cardinalWhiteyInitCopy1=cardinalWhiteRectCopy_1.centery
                    if rectCardinalWhiteCopy1_1.collidepoint(event.pos):
                        cardinalWhiteRectCopy_1.centerx=rectCardinalWhiteCopy1_1.centerx
                        cardinalWhiteRectCopy_1.centery=rectCardinalWhiteCopy1_1.centery
                        counter += 1
                        cardinalWhitePlayingCopy1=False
                    elif rectCardinalWhiteCopy2_1.collidepoint(event.pos):
                        cardinalWhiteRectCopy_1.centerx=rectCardinalWhiteCopy2_1.centerx
                        cardinalWhiteRectCopy_1.centery=rectCardinalWhiteCopy2_1.centery
                        counter += 1
                        cardinalWhitePlayingCopy1=False
                    elif rectCardinalWhiteCopy3_1.collidepoint(event.pos):
                        cardinalWhiteRectCopy_1.centerx=rectCardinalWhiteCopy3_1.centerx
                        cardinalWhiteRectCopy_1.centery=rectCardinalWhiteCopy3_1.centery
                        counter += 1
                        cardinalWhitePlayingCopy1=False
                    elif rectCardinalWhiteCopy4_1.collidepoint(event.pos):
                        cardinalWhiteRectCopy_1.centerx=rectCardinalWhiteCopy4_1.centerx
                        cardinalWhiteRectCopy_1.centery=rectCardinalWhiteCopy4_1.centery
                        counter += 1
                        cardinalWhitePlayingCopy1=False
                    else:
                        cardinalWhiteRectCopy_1.centerx=cardinalWhitexInitCopy1
                        cardinalWhiteRectCopy_1.centery=cardinalWhiteyInitCopy1
                        cardinalWhitePlayingCopy1=False
                    if (cardinalWhiteRectCopy_1.centerx <= 480 or cardinalWhiteRectCopy_1.centerx >= 1440) or (cardinalWhiteRectCopy_1.centery <= 60 or cardinalWhiteRectCopy_1.centery >= 1020):
                        cardinalWhiteRectCopy_1.centerx = cardinalWhitexInitCopy1
                        cardinalWhiteRectCopy_1.centery = cardinalWhiteyInitCopy1
                        cardinalWhitePlayingCopy1=False
                        counter-=1


            else:
                if plagueDoctorBlackRect.collidepoint(event.pos) and not hadesBlackAbilityActivated and plagueDoctorBlackRect.centerx!=screen_width-step:
                    if not plagueDoctorBlackPlaying:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                plagueDoctorBlackPlaying=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                plagueDoctorBlackPlaying=True
                elif plagueDoctorBlackPlaying:
                    plagueBlackxInit=plagueDoctorBlackRect.centerx
                    plagueBlackyInit=plagueDoctorBlackRect.centery
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
                    if (plagueDoctorBlackRect.centerx <= 480 or plagueDoctorBlackRect.centerx >= 1440) or (plagueDoctorBlackRect.centery <= 60 or plagueDoctorBlackRect.centery >= 1020):
                        plagueDoctorBlackRect.centerx = plagueBlackxInit
                        plagueDoctorBlackRect.centery = plagueBlackyInit
                        plagueDoctorBlackPlaying=False
                        counter-=1
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
                if rectPlagueDoctorBlackAbilityActivated:
                    if archbishopBlackRect.collidepoint(event.pos) and archbishopBlackRect.centerx==screen_width-step*2:
                        archbishopBlackRect.centerx=archbishopBlackxInit
                        archbishopBlackRect.centery=archbishopBlackyInit
                        plagueDoctorBlackPlaying=False
                        counter+=1
                    elif cardinalBlackRect.collidepoint(event.pos) and cardinalBlackRect.centerx==screen_width-step*3:
                        cardinalBlackRect.centerx=cardinalBlackxInit
                        cardinalBlackRect.centery=cardinalBlackyInit
                        plagueDoctorBlackPlaying=False
                        counter+=1
                    elif cardinalBlackRect1.collidepoint(event.pos) and cardinalBlackRect1.centerx==screen_width-step*3:
                        cardinalBlackRect1.centerx=cardinalBlackxInit1
                        cardinalBlackRect1.centery=cardinalBlackyInit1
                        plagueDoctorBlackPlaying=False
                        counter+=1
                    elif archbishopBlackRect1.collidepoint(event.pos) and archbishopBlackRect1.centerx==screen_width-step:
                        archbishopBlackRect1.centerx=archbishopBlackxInit1
                        archbishopBlackRect1.centery=archbishopBlackyInit1
                        plagueDoctorBlackPlaying=False
                        counter+=1
                    elif plagueDoctorBlackRect1.collidepoint(event.pos) and plagueDoctorBlackRect1.centerx==screen_width-step*2:
                        plagueDoctorBlackRect1.centerx=plagueBlackxInit1
                        plagueDoctorBlackRect1.centery=plagueBlackyInit1
                        plagueDoctorBlackPlaying=False
                        counter+=1
                    elif legionaryBlackRect.collidepoint(event.pos) and legionaryBlackRect.centerx==screen_width-step*3:
                        legionaryBlackRect.centerx=legionaryBlackxInit
                        legionaryBlackRect.centery=legionaryBlackyInit
                        plagueDoctorBlackPlaying=False
                        counter+=1
                    elif warriorBlackRect.collidepoint(event.pos) and warriorBlackRect.centerx==screen_width-step:
                        warriorBlackRect.centerx=warriorBlackxInit
                        warriorBlackRect.centery=warriorBlackyInit
                        plagueDoctorBlackPlaying=False
                        counter+=1
                    elif legionaryBlackRect1.collidepoint(event.pos) and legionaryBlackRect1.centerx==screen_width-step*2:
                        legionaryBlackRect1.centerx=legionaryBlackxInit1
                        legionaryBlackRect1.centery=legionaryBlackyInit1
                        plagueDoctorBlackPlaying=False
                        counter+=1
                    elif warriorBlackRect1.collidepoint(event.pos) and warriorBlackRect1.centerx==screen_width-step*3:
                        warriorBlackRect1.centerx=warriorBlackxInit1
                        warriorBlackRect1.centery=warriorBlackyInit1
                        plagueDoctorBlackPlaying=False
                        counter+=1
                    elif legionaryBlackRect2.collidepoint(event.pos) and legionaryBlackRect2.centerx==screen_width-step:
                        legionaryBlackRect2.centerx=legionaryBlackxInit2
                        legionaryBlackRect2.centery=legionaryBlackyInit2
                        plagueDoctorBlackPlaying=False
                        counter+=1
                    elif warriorBlackRect2.collidepoint(event.pos) and warriorBlackRect2.centerx==screen_width-step*2:
                        warriorBlackRect2.centerx=warriorBlackxInit2
                        warriorBlackRect2.centery=warriorBlackyInit2
                        plagueDoctorBlackPlaying=False
                        counter+=1
                    elif legionaryBlackRect3.collidepoint(event.pos) and legionaryBlackRect3.centerx==screen_width-step*3:
                        legionaryBlackRect3.centerx=legionaryBlackxInit3
                        legionaryBlackRect3.centery=legionaryBlackyInit3
                        plagueDoctorBlackPlaying=False
                        counter+=1
                    elif warriorBlackRect3.collidepoint(event.pos) and warriorBlackRect3==screen_width-step:
                        warriorBlackRect3.centerx=warriorBlackxInit3
                        warriorBlackRect3.centery=warriorBlackyInit3
                        plagueDoctorBlackPlaying=False
                        counter+=1
                    elif cardinalBlackRectCopy.collidepoint(event.pos) and cardinalBlackRectCopy.centerx==screen_width-step*2:
                        cardinalBlackRectCopy.centerx=cardinalBlackxInitCopy
                        cardinalBlackRectCopy.centery=cardinalBlackyInitCopy
                        plagueDoctorBlackPlaying=False
                        counter+=1
                    elif cardinalBlackRectCopy_1.collidepoint(event.pos) and cardinalBlackRectCopy_1.centerx==screen_width-step*3:
                        cardinalBlackRectCopy_1.centerx=cardinalBlackxInitCopy1
                        cardinalBlackRectCopy_1.centery=cardinalBlackyInitCopy1
                        plagueDoctorBlackPlaying=False
                        counter+=1
                    else:
                        rectPlagueDoctorBlackAbilityActivated=False
                        plagueDoctorBlackPlaying=False

                if archbishopBlackRect.collidepoint(event.pos) and not hadesBlackAbilityActivated and archbishopBlackRect.centerx!=screen_width-step*2:
                    if not archbishopBlackPlaying:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                archbishopBlackPlaying=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                archbishopBlackPlaying=True
                elif archbishopBlackPlaying:
                    archbishopBlackxInit=archbishopBlackRect.centerx
                    archbishopBlackyInit=archbishopBlackRect.centery
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
                    if (archbishopBlackRect.centerx <= 480 or archbishopBlackRect.centerx >= 1440) or (archbishopBlackRect.centery <= 60 or archbishopBlackRect.centery >= 1020):
                        archbishopBlackRect.centerx = archbishopBlackxInit
                        archbishopBlackRect.centery = archbishopBlackyInit
                        archbishopBlackPlaying=False
                        counter-=1
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
                if archbishopBlackAbilityActivated:
                    if plagueDoctorWhiteRect.collidepoint(event.pos):
                        plagueDoctorWhiteRect.centerx = step
                        plagueDoctorWhiteRect.centery = step
                        archbishopBlackPlaying=False
                        archbishopBlackAbilityActivated=False
                        archbishopBlackAbilityCounter-=1
                        counter+=1
                    if archbishopWhiteRect.collidepoint(event.pos):
                        archbishopWhiteRect.centerx = step*2
                        archbishopWhiteRect.centery = step
                        archbishopBlackPlaying=False
                        archbishopBlackAbilityActivated=False
                        archbishopBlackAbilityCounter-=1
                        counter+=1
                    if cardinalWhiteRect.collidepoint(event.pos):
                        cardinalWhiteRect.centerx = step*3
                        cardinalWhiteRect.centery = step
                        archbishopBlackPlaying=False
                        archbishopBlackAbilityActivated=False
                        archbishopBlackAbilityCounter-=1
                        counter+=1
                    if hadesWhiteRect.collidepoint(event.pos):
                        hadesWhiteRect.centerx = step
                        hadesWhiteRect.centery = step*2
                        archbishopBlackPlaying=False
                        archbishopBlackAbilityActivated=False
                        archbishopBlackAbilityCounter-=1
                        counter+=1
                    if persephoneWhiteRect.collidepoint(event.pos):
                        persephoneWhiteRect.centerx = step*2
                        persephoneWhiteRect.centery = step*2
                        archbishopBlackPlaying=False
                        archbishopBlackAbilityActivated=False
                        archbishopBlackAbilityCounter-=1
                        counter+=1
                    if cardinalWhiteRect1.collidepoint(event.pos):
                        cardinalWhiteRect1.centerx = step*3
                        cardinalWhiteRect1.centery = step*2
                        archbishopBlackPlaying=False
                        archbishopBlackAbilityActivated=False
                        archbishopBlackAbilityCounter-=1
                        counter+=1
                    if archbishopWhiteRect1.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = step
                        archbishopWhiteRect1.centery = step*3
                        archbishopBlackPlaying=False
                        archbishopBlackAbilityActivated=False
                        archbishopBlackAbilityCounter-=1
                        counter+=1
                    if plagueDoctorWhiteRect1.collidepoint(event.pos):
                        plagueDoctorWhiteRect1.centerx = step*2
                        plagueDoctorWhiteRect1.centery = step*3
                        archbishopBlackPlaying=False
                        archbishopBlackAbilityActivated=False
                        archbishopBlackAbilityCounter-=1
                        counter+=1
                    if legionaryWhiteRect.collidepoint(event.pos):
                        legionaryWhiteRect.centerx = step*3
                        legionaryWhiteRect.centery = step*3
                        archbishopBlackPlaying=False
                        archbishopBlackAbilityActivated=False
                        archbishopBlackAbilityCounter-=1
                        counter+=1
                    if warriorWhiteRect.collidepoint(event.pos):
                        warriorWhiteRect.centerx = step
                        warriorWhiteRect.centery = step*4
                        archbishopBlackPlaying=False
                        archbishopBlackAbilityActivated=False
                        archbishopBlackAbilityCounter-=1
                        counter+=1
                    if legionaryWhiteRect1.collidepoint(event.pos):
                        legionaryWhiteRect1.centerx = step*2
                        legionaryWhiteRect1.centery = step*4
                        archbishopBlackPlaying=False
                        archbishopBlackAbilityActivated=False
                        archbishopBlackAbilityCounter-=1
                        counter+=1
                    if warriorWhiteRect1.collidepoint(event.pos):
                        warriorWhiteRect1.centerx = step*3
                        warriorWhiteRect1.centery = step*4
                        archbishopBlackPlaying=False
                        archbishopBlackAbilityActivated=False
                        archbishopBlackAbilityCounter-=1
                        counter+=1
                    if legionaryWhiteRect2.collidepoint(event.pos):
                        legionaryWhiteRect2.centerx = step
                        legionaryWhiteRect2.centery = step*5
                        archbishopBlackPlaying=False
                        archbishopBlackAbilityActivated=False
                        archbishopBlackAbilityCounter-=1
                        counter+=1
                    if warriorWhiteRect2.collidepoint(event.pos):
                        warriorWhiteRect2.centerx = step*2
                        warriorWhiteRect2.centery = step*5
                        archbishopBlackPlaying=False
                        archbishopBlackAbilityActivated=False
                        archbishopBlackAbilityCounter-=1
                        counter+=1
                    if legionaryWhiteRect3.collidepoint(event.pos):
                        legionaryWhiteRect3.centerx = step*3
                        legionaryWhiteRect3.centery = step*5
                        archbishopBlackPlaying=False
                        archbishopBlackAbilityActivated=False
                        archbishopBlackAbilityCounter-=1
                        counter+=1
                    if warriorWhiteRect3.collidepoint(event.pos):
                        warriorWhiteRect3.centerx = step
                        warriorWhiteRect3.centery = step*6
                        archbishopBlackPlaying=False
                        archbishopBlackAbilityActivated=False
                        archbishopBlackAbilityCounter-=1
                        counter+=1

                if cardinalBlackRect.collidepoint(event.pos) and not hadesBlackAbilityActivated and cardinalBlackRect.centerx!=screen_width-step*3:
                    if not cardinalBlackPlaying:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                cardinalBlackPlaying=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                cardinalBlackPlaying=True
                elif cardinalBlackPlaying:
                    cardinalBlackxInit=cardinalBlackRect.centerx
                    cardinalBlackyInit=cardinalBlackRect.centery
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
                    if (cardinalBlackRect.centerx <= 480 or cardinalBlackRect.centerx >= 1440) or (cardinalBlackRect.centery <= 60 or cardinalBlackRect.centery >= 1020):
                        cardinalBlackRect.centerx = cardinalBlackxInit
                        cardinalBlackRect.centery = cardinalBlackyInit
                        cardinalBlackPlaying=False
                        counter-=1
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
                if cardinalBlackAbilityActivated:
                    if plagueDoctorWhiteRect.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        plagueDoctorWhitexBefore=plagueDoctorWhiteRect.centerx
                        plagueDoctorWhiteyBefore=plagueDoctorWhiteRect.centery
                        plagueDoctorWhiteRect.centerx = step
                        plagueDoctorWhiteRect.centery = step
                        cardinalBlackRectCopy.centerx=plagueDoctorWhitexBefore
                        cardinalBlackRectCopy.centery=plagueDoctorWhiteyBefore
                        counter+=1
                        cardinalBlackAbilityActivated=False
                        cardinalBlackAbilityCounter-=1
                    if archbishopWhiteRect.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        archbishopWhitexBefore=archbishopWhiteRect.centerx
                        archbishopWhiteyBefore=archbishopWhiteRect.centery
                        archbishopWhiteRect.centerx = step*2
                        archbishopWhiteRect.centery = step
                        cardinalBlackRectCopy.centerx=archbishopWhitexBefore
                        cardinalBlackRectCopy.centery=archbishopWhiteyBefore
                        counter+=1
                        cardinalBlackAbilityActivated=False
                        cardinalBlackAbilityCounter-=1
                    if cardinalWhiteRect.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        cardinalWhitexBefore=cardinalWhiteRect.centerx
                        cardinalWhiteyBefore=cardinalWhiteRect.centery
                        cardinalWhiteRect.centerx = step*3
                        cardinalWhiteRect.centery = step
                        cardinalBlackRectCopy.centerx=cardinalWhitexBefore
                        cardinalBlackRectCopy.centery=cardinalWhiteyBefore
                        counter+=1
                        cardinalBlackAbilityActivated=False
                        cardinalBlackAbilityCounter-=1
                    if cardinalWhiteRect1.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        cardinalWhitexBefore_1=cardinalWhiteRect1.centerx
                        cardinalWhiteyBefore_1=cardinalWhiteRect1.centery
                        cardinalWhiteRect1.centerx = step
                        cardinalWhiteRect1.centery = step*2
                        cardinalBlackRectCopy.centerx=cardinalWhitexBefore_1
                        cardinalBlackRectCopy.centery=cardinalWhiteyBefore_1
                        counter+=1
                        cardinalBlackAbilityActivated=False
                        cardinalBlackAbilityCounter-=1
                    if archbishopWhiteRect1.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        archbishopWhitexBefore_1=archbishopWhiteRect1.centerx
                        archbishopWhiteyBefore_1=archbishopWhiteRect1.centery
                        archbishopWhiteRect1.centerx = step*2
                        archbishopWhiteRect1.centery = step*2
                        cardinalBlackRectCopy.centerx=archbishopWhitexBefore_1
                        cardinalBlackRectCopy.centery=archbishopWhiteyBefore_1
                        counter+=1
                        cardinalBlackAbilityActivated=False
                        cardinalBlackAbilityCounter-=1
                    if plagueDoctorWhiteRect1.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        plagueDoctorWhitexBefore_1=plagueDoctorWhiteRect1.centerx
                        plagueDoctorWhiteyBefore_1=plagueDoctorWhiteRect1.centery
                        plagueDoctorWhiteRect1.centerx = step*3
                        plagueDoctorWhiteRect1.centery = step*2
                        cardinalBlackRectCopy.centerx=plagueDoctorWhitexBefore_1
                        cardinalBlackRectCopy.centery=plagueDoctorWhiteyBefore_1
                        counter+=1
                        cardinalBlackAbilityActivated=False
                        cardinalBlackAbilityCounter-=1
                    if legionaryWhiteRect.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        legionaryWhitexBefore=legionaryWhiteRect.centerx
                        legionaryWhiteyBefore=legionaryWhiteRect.centery
                        legionaryWhiteRect.centerx = step
                        legionaryWhiteRect.centery = step*3
                        cardinalBlackRectCopy.centerx=legionaryWhitexBefore
                        cardinalBlackRectCopy.centery=legionaryWhitexBefore
                        counter+=1
                        cardinalBlackAbilityActivated=False
                        cardinalBlackAbilityCounter-=1
                    if warriorWhiteRect.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        warriorWhitexBefore=warriorWhiteRect.centerx
                        warriorWhiteyBefore=warriorWhiteRect.centery
                        warriorWhiteRect.centerx = step*2
                        warriorWhiteRect.centery = step*3
                        cardinalBlackRectCopy.centerx=warriorWhitexBefore
                        cardinalBlackRectCopy.centery=warriorWhiteyBefore
                        counter+=1
                        cardinalBlackAbilityActivated=False
                        cardinalBlackAbilityCounter-=1
                    if legionaryWhiteRect1.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        legionaryWhitexBefore_1=legionaryWhiteRect1.centerx
                        legionaryWhiteyBefore_1=legionaryWhiteRect1.centery
                        legionaryWhiteRect1.centerx = step*3
                        legionaryWhiteRect1.centery = step*3
                        cardinalBlackRectCopy.centerx=legionaryWhitexBefore_1
                        cardinalBlackRectCopy.centery=legionaryWhiteyBefore_1
                        counter+=1
                        cardinalBlackAbilityActivated=False
                        cardinalBlackAbilityCounter-=1
                    if warriorWhiteRect1.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        warriorWhitexBefore_1=warriorWhiteRect1.centerx
                        warriorWhiteyBefore_1=warriorWhiteRect1.centery
                        warriorWhiteRect1.centerx = step
                        warriorWhiteRect1.centery = step*4
                        cardinalBlackRectCopy.centerx=warriorWhitexBefore_1
                        cardinalBlackRectCopy.centery=warriorWhiteyBefore_1
                        counter+=1
                        cardinalBlackAbilityActivated=False
                        cardinalBlackAbilityCounter-=1
                    if legionaryWhiteRect2.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        legionaryWhitexBefore_2=legionaryWhiteRect2.centerx
                        legionaryWhiteyBefore_2=legionaryWhiteRect2.centery
                        legionaryWhiteRect2.centerx = step*2
                        legionaryWhiteRect2.centery = step*4
                        cardinalBlackRectCopy.centerx=legionaryWhitexBefore_2
                        cardinalBlackRectCopy.centery=legionaryWhiteyBefore_2
                        counter+=1
                        cardinalBlackAbilityActivated=False
                        cardinalBlackAbilityCounter-=1
                    if warriorWhiteRect2.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        warriorWhitexBefore_2=warriorWhiteRect2.centerx
                        warriorWhiteyBefore_2=warriorWhiteRect2.centery
                        warriorWhiteRect2.centerx = step*2
                        warriorWhiteRect2.centery = step*4
                        cardinalBlackRectCopy.centerx=warriorWhitexBefore_2
                        cardinalBlackRectCopy.centery=warriorWhiteyBefore_2
                        counter+=1
                        cardinalBlackAbilityActivated=False
                        cardinalBlackAbilityCounter-=1
                    if legionaryWhiteRect3.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        legionaryWhitexBefore_3=legionaryWhiteRect3.centerx
                        legionaryWhiteyBefore_3=legionaryWhiteRect3.centery
                        legionaryWhiteRect3.centerx = step*3
                        legionaryWhiteRect3.centery = step*4
                        cardinalBlackRectCopy.centerx=legionaryWhitexBefore_3
                        cardinalBlackRectCopy.centery=legionaryWhiteyBefore_3
                        counter+=1
                        cardinalBlackAbilityActivated=False
                        cardinalBlackAbilityCounter-=1
                    if warriorWhiteRect3.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        warriorWhitexBefore_3=warriorWhiteRect3.centerx
                        warriorWhiteyBefore_3=warriorWhiteRect3.centery
                        warriorWhiteRect3.centerx = step
                        warriorWhiteRect3.centery = step*5
                        cardinalBlackRectCopy.centerx=warriorWhitexBefore_3
                        cardinalBlackRectCopy.centery=warriorWhiteyBefore_3
                        counter+=1
                        cardinalBlackAbilityActivated=False
                        cardinalBlackAbilityCounter-=1


                if hadesBlackRect.collidepoint(event.pos) and hadesBlackRect.centerx!=screen_width-step:
                    if not hadesBlackPlaying:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                hadesBlackPlaying=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                hadesBlackPlaying=True
                elif hadesBlackPlaying:
                    hadesBlackxInit=hadesBlackRect.centerx
                    hadesBlackyInit=hadesBlackRect.centery
                    if rectHadesBlack1.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack1.centerx
                        hadesBlackRect.centery = rectHadesBlack1.centery
                        if not hadesBlackAbilityActivated:
                            counter += 1
                        else:
                            hadesBlackAbilityCounter-=1
                        hadesBlackPlaying=False
                    elif rectHadesBlack2.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack2.centerx
                        hadesBlackRect.centery = rectHadesBlack2.centery
                        if not hadesBlackAbilityActivated:
                            counter += 1
                        else:
                            hadesBlackAbilityCounter-=1
                        hadesBlackPlaying=False
                    elif rectHadesBlack3.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack3.centerx
                        hadesBlackRect.centery = rectHadesBlack3.centery
                        if not hadesBlackAbilityActivated:
                            counter += 1
                        else:
                            hadesBlackAbilityCounter-=1
                        hadesBlackPlaying=False
                    elif rectHadesBlack4.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack4.centerx
                        hadesBlackRect.centery = rectHadesBlack4.centery
                        if not hadesBlackAbilityActivated:
                            counter += 1
                        else:
                            hadesBlackAbilityCounter-=1
                        hadesBlackPlaying=False
                    elif rectHadesBlack5.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack5.centerx
                        hadesBlackRect.centery = rectHadesBlack5.centery
                        if not hadesBlackAbilityActivated:
                            counter += 1
                        else:
                            hadesBlackAbilityCounter-=1
                        hadesBlackPlaying=False
                    elif rectHadesBlack6.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack6.centerx
                        hadesBlackRect.centery = rectHadesBlack6.centery
                        if not hadesBlackAbilityActivated:
                            counter += 1
                        else:
                            hadesBlackAbilityCounter-=1
                        hadesBlackPlaying=False
                    elif rectHadesBlack7.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack7.centerx
                        hadesBlackRect.centery = rectHadesBlack7.centery
                        if not hadesBlackAbilityActivated:
                            counter += 1
                        else:
                            hadesBlackAbilityCounter-=1
                        hadesBlackPlaying=False
                    elif rectHadesBlack8.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack8.centerx
                        hadesBlackRect.centery = rectHadesBlack8.centery
                        if not hadesBlackAbilityActivated:
                            counter += 1
                        else:
                            hadesBlackAbilityCounter-=1
                        hadesBlackPlaying=False
                    elif rectHadesBlack9.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack9.centerx
                        hadesBlackRect.centery = rectHadesBlack9.centery
                        if not hadesBlackAbilityActivated:
                            counter += 1
                        else:
                            hadesBlackAbilityCounter-=1
                        hadesBlackPlaying=False
                    elif rectHadesBlack10.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack10.centerx
                        hadesBlackRect.centery = rectHadesBlack10.centery
                        if not hadesBlackAbilityActivated:
                            counter += 1
                        else:
                            hadesBlackAbilityCounter-=1
                        hadesBlackPlaying=False
                    elif rectHadesBlack11.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack11.centerx
                        hadesBlackRect.centery = rectHadesBlack11.centery
                        if not hadesBlackAbilityActivated:
                            counter += 1
                        else:
                            hadesBlackAbilityCounter-=1
                        hadesBlackPlaying=False
                    elif rectHadesBlack12.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack12.centerx
                        hadesBlackRect.centery = rectHadesBlack12.centery
                        if not hadesBlackAbilityActivated:
                            counter += 1
                        else:
                            hadesBlackAbilityCounter-=1
                        hadesBlackPlaying=False
                    elif rectHadesBlack13.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack13.centerx
                        hadesBlackRect.centery = rectHadesBlack13.centery
                        if not hadesBlackAbilityActivated:
                            counter += 1
                        else:
                            hadesBlackAbilityCounter-=1
                        hadesBlackPlaying=False
                    elif rectHadesBlack14.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack14.centerx
                        hadesBlackRect.centery = rectHadesBlack14.centery
                        if not hadesBlackAbilityActivated:
                            counter += 1
                        else:
                            hadesBlackAbilityCounter-=1
                        hadesBlackPlaying=False
                    elif rectHadesBlack15.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack15.centerx
                        hadesBlackRect.centery = rectHadesBlack15.centery
                        if not hadesBlackAbilityActivated:
                            counter += 1
                        else:
                            hadesBlackAbilityCounter-=1
                        hadesBlackPlaying=False
                    elif rectHadesBlack16.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack16.centerx
                        hadesBlackRect.centery = rectHadesBlack16.centery
                        if not hadesBlackAbilityActivated:
                            counter += 1
                        else:
                            hadesBlackAbilityCounter-=1
                        hadesBlackPlaying=False
                    elif rectHadesBlack17.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack17.centerx
                        hadesBlackRect.centery = rectHadesBlack17.centery
                        if not hadesBlackAbilityActivated:
                            counter += 1
                        else:
                            hadesBlackAbilityCounter-=1
                        hadesBlackPlaying=False
                    elif rectHadesBlack18.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack18.centerx
                        hadesBlackRect.centery = rectHadesBlack18.centery
                        if not hadesBlackAbilityActivated:
                            counter += 1
                        else:
                            hadesBlackAbilityCounter-=1
                        hadesBlackPlaying=False
                    elif rectHadesBlack19.collidepoint(event.pos):
                        hadesBlackRect.centerx = rectHadesBlack19.centerx
                        hadesBlackRect.centery = rectHadesBlack19.centery
                        if not hadesBlackAbilityActivated:
                            counter += 1
                        else:
                            hadesBlackAbilityCounter-=1
                        hadesBlackPlaying=False
                    else:
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        hadesBlackPlaying=False
                    if (hadesBlackRect.centerx <= 480 or hadesBlackRect.centerx >= 1440) or (hadesBlackRect.centery <= 60 or hadesBlackRect.centery >= 1020):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        hadesBlackPlaying=False
                        if not hadesBlackAbilityActivated:
                            counter -= 1
                        else:
                            hadesBlackAbilityCounter+=1
                    if hadesBlackRect.colliderect(plagueDoctorBlackRect):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        if not hadesBlackAbilityActivated:
                            counter -= 1
                        else:
                            hadesBlackAbilityCounter+=1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(archbishopBlackRect):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        if not hadesBlackAbilityActivated:
                            counter -= 1
                        else:
                            hadesBlackAbilityCounter+=1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(cardinalBlackRect):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        if not hadesBlackAbilityActivated:
                            counter -= 1
                        else:
                            hadesBlackAbilityCounter+=1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(persephoneBlackRect):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        if not hadesBlackAbilityActivated:
                            counter -= 1
                        else:
                            hadesBlackAbilityCounter+=1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(cardinalBlackRect1):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        if not hadesBlackAbilityActivated:
                            counter -= 1
                        else:
                            hadesBlackAbilityCounter+=1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(archbishopBlackRect1):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        if not hadesBlackAbilityActivated:
                            counter -= 1
                        else:
                            hadesBlackAbilityCounter+=1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(plagueDoctorBlackRect1):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        if not hadesBlackAbilityActivated:
                            counter -= 1
                        else:
                            hadesBlackAbilityCounter+=1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(legionaryBlackRect):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        if not hadesBlackAbilityActivated:
                            counter -= 1
                        else:
                            hadesBlackAbilityCounter+=1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(warriorBlackRect):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        if not hadesBlackAbilityActivated:
                            counter -= 1
                        else:
                            hadesBlackAbilityCounter+=1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(legionaryBlackRect1):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        if not hadesBlackAbilityActivated:
                            counter -= 1
                        else:
                            hadesBlackAbilityCounter+=1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(warriorBlackRect1):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        if not hadesBlackAbilityActivated:
                            counter -= 1
                        else:
                            hadesBlackAbilityCounter+=1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(legionaryBlackRect2):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        if not hadesBlackAbilityActivated:
                            counter -= 1
                        else:
                            hadesBlackAbilityCounter+=1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(warriorBlackRect2):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        if not hadesBlackAbilityActivated:
                            counter -= 1
                        else:
                            hadesBlackAbilityCounter+=1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(legionaryBlackRect3):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        if not hadesBlackAbilityActivated:
                            counter -= 1
                        else:
                            hadesBlackAbilityCounter+=1
                        hadesBlackPlaying=False
                    elif hadesBlackRect.colliderect(warriorBlackRect3):
                        hadesBlackRect.centerx = hadesBlackxInit
                        hadesBlackRect.centery = hadesBlackyInit
                        if not hadesBlackAbilityActivated:
                            counter -= 1
                        else:
                            hadesBlackAbilityCounter+=1
                        hadesBlackPlaying=False
                print(hadesBlackAbilityCounter)

                if persephoneBlackRect.collidepoint(event.pos) and not hadesBlackAbilityActivated and persephoneBlackRect.centerx!=screen_width-step*2:
                    if not persephoneBlackPlaying:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                persephoneBlackPlaying=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                persephoneBlackPlaying=True
                elif persephoneBlackPlaying:
                    persephoneBlackxInit=persephoneBlackRect.centerx
                    persephoneBlackyInit=persephoneBlackRect.centery
                    if persephoneBlackAbilityActivated:
                        if rectPersephoneBlack1Ability.collidepoint(event.pos):
                            persephoneBlackRect.centerx=rectPersephoneBlack1Ability.centerx
                            persephoneBlackRect.centery=rectPersephoneBlack1Ability.centery
                            persephoneBlackAbilityCounter-=1
                            persephoneBlackPlaying=False
                            counter+=1
                            print(f"rect {rectPersephoneBlack1Ability.center}")
                            print(f"na začátku {persephoneBlackRect.center}")
                        elif rectPersephoneBlack2Ability.collidepoint(event.pos):
                            persephoneBlackRect.centerx=rectPersephoneBlack2Ability.centerx
                            persephoneBlackRect.centery=rectPersephoneBlack2Ability.centery
                            persephoneBlackAbilityCounter-=1
                            persephoneBlackPlaying=False
                            counter+=1
                        elif rectPersephoneBlack3Ability.collidepoint(event.pos):
                            persephoneBlackRect.centerx=rectPersephoneBlack3Ability.centerx
                            persephoneBlackRect.centery=rectPersephoneBlack3Ability.centery
                            persephoneBlackAbilityCounter-=1
                            persephoneBlackPlaying=False
                            counter+=1
                        elif rectPersephoneBlack4Ability.collidepoint(event.pos):
                            persephoneBlackRect.centerx=rectPersephoneBlack4Ability.centerx
                            persephoneBlackRect.centery=rectPersephoneBlack4Ability.centery
                            persephoneBlackAbilityCounter-=1
                            persephoneBlackPlaying=False
                            counter+=1
                        elif rectPersephoneBlack5Ability.collidepoint(event.pos):
                            persephoneBlackRect.centerx=rectPersephoneBlack5Ability.centerx
                            persephoneBlackRect.centery=rectPersephoneBlack5Ability.centery
                            persephoneBlackAbilityCounter-=1
                            persephoneBlackPlaying=False
                            counter+=1
                        elif rectPersephoneBlack6Ability.collidepoint(event.pos):
                            persephoneBlackRect.centerx=rectPersephoneBlack6Ability.centerx
                            persephoneBlackRect.centery=rectPersephoneBlack6Ability.centery
                            persephoneBlackAbilityCounter-=1
                            persephoneBlackPlaying=False
                            counter+=1
                        elif rectPersephoneBlack7Ability.collidepoint(event.pos):
                            persephoneBlackRect.centerx=rectPersephoneBlack7Ability.centerx
                            persephoneBlackRect.centery=rectPersephoneBlack7Ability.centery
                            persephoneBlackAbilityCounter-=1
                            persephoneBlackPlaying=False
                            counter+=1
                        elif rectPersephoneBlack8Ability.collidepoint(event.pos):
                            persephoneBlackRect.centerx=rectPersephoneBlack8Ability.centerx
                            persephoneBlackRect.centery=rectPersephoneBlack8Ability.centery
                            persephoneBlackAbilityCounter-=1
                            persephoneBlackPlaying=False
                            counter+=1
                        elif rectPersephoneBlack9Ability.collidepoint(event.pos):
                            persephoneBlackRect.centerx=rectPersephoneBlack9Ability.centerx
                            persephoneBlackRect.centery=rectPersephoneBlack9Ability.centery
                            persephoneBlackAbilityCounter-=1
                            persephoneBlackPlaying=False
                            counter+=1
                        elif rectPersephoneBlack10Ability.collidepoint(event.pos):
                            persephoneBlackRect.centerx=rectPersephoneBlack10Ability.centerx
                            persephoneBlackRect.centery=rectPersephoneBlack10Ability.centery
                            persephoneBlackAbilityCounter-=1
                            persephoneBlackPlaying=False
                            counter+=1
                        elif rectPersephoneBlack11Ability.collidepoint(event.pos):
                            persephoneBlackRect.centerx=rectPersephoneBlack11Ability.centerx
                            persephoneBlackRect.centery=rectPersephoneBlack11Ability.centery
                            persephoneBlackAbilityCounter-=1
                            persephoneBlackPlaying=False
                            counter+=1
                        elif rectPersephoneBlack12Ability.collidepoint(event.pos):
                            persephoneBlackRect.centerx=rectPersephoneBlack12Ability.centerx
                            persephoneBlackRect.centery=rectPersephoneBlack12Ability.centery
                            persephoneBlackAbilityCounter-=1
                            persephoneBlackPlaying=False
                            counter+=1
                        elif rectPersephoneBlack13Ability.collidepoint(event.pos):
                            persephoneBlackRect.centerx=rectPersephoneBlack13Ability.centerx
                            persephoneBlackRect.centery=rectPersephoneBlack13Ability.centery
                            persephoneBlackAbilityCounter-=1
                            persephoneBlackPlaying=False
                            counter+=1
                        elif rectPersephoneBlack14Ability.collidepoint(event.pos):
                            persephoneBlackRect.centerx=rectPersephoneBlack14Ability.centerx
                            persephoneBlackRect.centery=rectPersephoneBlack14Ability.centery
                            persephoneBlackAbilityCounter-=1
                            persephoneBlackPlaying=False
                            counter+=1
                        elif rectPersephoneBlack15Ability.collidepoint(event.pos):
                            persephoneBlackRect.centerx=rectPersephoneBlack15Ability.centerx
                            persephoneBlackRect.centery=rectPersephoneBlack15Ability.centery
                            persephoneBlackAbilityCounter-=1
                            persephoneBlackPlaying=False
                            counter+=1
                        elif rectPersephoneBlack16Ability.collidepoint(event.pos):
                            persephoneBlackRect.centerx=rectPersephoneBlack16Ability.centerx
                            persephoneBlackRect.centery=rectPersephoneBlack16Ability.centery
                            persephoneBlackAbilityCounter-=1
                            persephoneBlackPlaying=False
                            counter+=1
                        elif rectPersephoneBlack17Ability.collidepoint(event.pos):
                            persephoneBlackRect.centerx=rectPersephoneBlack17Ability.centerx
                            persephoneBlackRect.centery=rectPersephoneBlack17Ability.centery
                            persephoneBlackAbilityCounter-=1
                            persephoneBlackPlaying=False
                            counter+=1
                        elif rectPersephoneBlack18Ability.collidepoint(event.pos):
                            persephoneBlackRect.centerx=rectPersephoneBlack18Ability.centerx
                            persephoneBlackRect.centery=rectPersephoneBlack18Ability.centery
                            persephoneBlackAbilityCounter-=1
                            persephoneBlackPlaying=False
                            counter+=1
                        elif rectPersephoneBlack19Ability.collidepoint(event.pos):
                            persephoneBlackRect.centerx=rectPersephoneBlack19Ability.centerx
                            persephoneBlackRect.centery=rectPersephoneBlack19Ability.centery
                            persephoneBlackAbilityCounter-=1
                            persephoneBlackPlaying=False
                            counter+=1
                        else:
                            persephoneBlackRect.centerx = persephoneBlackxInit
                            persephoneBlackRect.centery = persephoneBlackyInit
                            persephoneBlackPlaying=False
                            
                    else:
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
                            
                    if (persephoneBlackRect.centerx <= 480 or persephoneBlackRect.centerx >= 1440) or (persephoneBlackRect.centery <= 60 or persephoneBlackRect.centery >= 1020):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        persephoneBlackPlaying=False
                        counter-=1
                        print("kolize")
                    if persephoneBlackRect.colliderect(plagueDoctorBlackRect):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                        print("kolize")
                    elif persephoneBlackRect.colliderect(archbishopBlackRect):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                        print("kolize")
                    elif persephoneBlackRect.colliderect(cardinalBlackRect):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                        print("kolize")
                    elif persephoneBlackRect.colliderect(hadesBlackRect):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                        print("kolize")
                    elif persephoneBlackRect.colliderect(cardinalBlackRect1):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                        print("kolize")
                    elif persephoneBlackRect.colliderect(archbishopBlackRect1):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                        print("kolize")
                    elif persephoneBlackRect.colliderect(plagueDoctorBlackRect1):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                        print("kolize")
                    elif persephoneBlackRect.colliderect(legionaryBlackRect):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                        print("kolize")
                    elif persephoneBlackRect.colliderect(warriorBlackRect):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                        print("kolize")
                    elif persephoneBlackRect.colliderect(legionaryBlackRect1):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                        print("kolize")
                    elif persephoneBlackRect.colliderect(warriorBlackRect1):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                        print("kolize")
                    elif persephoneBlackRect.colliderect(legionaryBlackRect2):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                        print("kolize")
                    elif persephoneBlackRect.colliderect(warriorBlackRect2):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                        print("kolize")
                    elif persephoneBlackRect.colliderect(legionaryBlackRect3):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                        print("kolize")
                    elif persephoneBlackRect.colliderect(warriorBlackRect3):
                        persephoneBlackRect.centerx = persephoneBlackxInit
                        persephoneBlackRect.centery = persephoneBlackyInit
                        counter -= 1
                        persephoneBlackPlaying=False
                        print("kolize")
                    print(f"na konci {persephoneBlackRect.center}")

                if cardinalBlackRect1.collidepoint(event.pos) and not hadesBlackAbilityActivated and cardinalBlackRect1.centerx!=screen_width-step*3:
                    if not cardinalBlackPlaying1:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                cardinalBlackPlaying1=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                cardinalBlackPlaying1=True
                elif cardinalBlackPlaying1:
                    cardinalBlackxInit1=cardinalBlackRect1.centerx
                    cardinalBlackyInit1=cardinalBlackRect1.centery
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
                    if (cardinalBlackRect1.centerx <= 480 or cardinalBlackRect1.centerx >= 1440) or (cardinalBlackRect1.centery <= 60 or cardinalBlackRect1.centery >= 1020):
                        cardinalBlackRect1.centerx = cardinalBlackxInit1
                        cardinalBlackRect1.centery = cardinalBlackyInit1
                        cardinalBlackPlaying1=False
                        counter-=1
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
                if cardinalBlackAbilityActivated_1:
                    if plagueDoctorWhiteRect.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        plagueDoctorWhitexBefore=plagueDoctorWhiteRect.centerx
                        plagueDoctorWhiteyBefore=plagueDoctorWhiteRect.centery
                        plagueDoctorWhiteRect.centerx = step
                        plagueDoctorWhiteRect.centery = step
                        cardinalBlackRectCopy_1.centerx=plagueDoctorWhitexBefore
                        cardinalBlackRectCopy_1.centery=plagueDoctorWhiteyBefore
                        counter+=1
                        cardinalBlackAbilityActivated_1=False
                        cardinalBlackAbilityCounter_1-=1
                    if archbishopWhiteRect.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        archbishopWhitexBefore=archbishopWhiteRect.centerx
                        archbishopWhiteyBefore=archbishopWhiteRect.centery
                        archbishopWhiteRect.centerx = step*2
                        archbishopWhiteRect.centery = step
                        cardinalBlackRectCopy_1.centerx=archbishopWhitexBefore
                        cardinalBlackRectCopy_1.centery=archbishopWhiteyBefore
                        counter+=1
                        cardinalBlackAbilityActivated_1=False
                        cardinalBlackAbilityCounter_1-=1
                    if cardinalWhiteRect.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        cardinalWhitexBefore=cardinalWhiteRect.centerx
                        cardinalWhiteyBefore=cardinalWhiteRect.centery
                        cardinalWhiteRect.centerx = step*3
                        cardinalWhiteRect.centery = step
                        cardinalBlackRectCopy_1.centerx=cardinalWhitexBefore
                        cardinalBlackRectCopy_1.centery=cardinalWhiteyBefore
                        counter+=1
                        cardinalBlackAbilityActivated_1=False
                        cardinalBlackAbilityCounter_1-=1
                    if cardinalWhiteRect1.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        cardinalWhitexBefore_1=cardinalWhiteRect1.centerx
                        cardinalWhiteyBefore_1=cardinalWhiteRect1.centery
                        cardinalWhiteRect1.centerx = step
                        cardinalWhiteRect1.centery = step*2
                        cardinalBlackRectCopy_1.centerx=cardinalWhitexBefore_1
                        cardinalBlackRectCopy_1.centery=cardinalWhiteyBefore_1
                        counter+=1
                        cardinalBlackAbilityActivated_1=False
                        cardinalBlackAbilityCounter_1-=1
                    if archbishopWhiteRect1.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        archbishopWhitexBefore_1=archbishopWhiteRect1.centerx
                        archbishopWhiteyBefore_1=archbishopWhiteRect1.centery
                        archbishopWhiteRect1.centerx = step*2
                        archbishopWhiteRect1.centery = step*2
                        cardinalBlackRectCopy_1.centerx=archbishopWhitexBefore_1
                        cardinalBlackRectCopy_1.centery=archbishopWhiteyBefore_1
                        counter+=1
                        cardinalBlackAbilityActivated_1=False
                        cardinalBlackAbilityCounter_1-=1
                    if plagueDoctorWhiteRect1.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        plagueDoctorWhitexBefore_1=plagueDoctorWhiteRect1.centerx
                        plagueDoctorWhiteyBefore_1=plagueDoctorWhiteRect1.centery
                        plagueDoctorWhiteRect1.centerx = step*3
                        plagueDoctorWhiteRect1.centery = step*2
                        cardinalBlackRectCopy_1.centerx=plagueDoctorWhitexBefore_1
                        cardinalBlackRectCopy_1.centery=plagueDoctorWhiteyBefore_1
                        counter+=1
                        cardinalBlackAbilityActivated_1=False
                        cardinalBlackAbilityCounter_1-=1
                    if legionaryWhiteRect.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        legionaryWhitexBefore=legionaryWhiteRect.centerx
                        legionaryWhiteyBefore=legionaryWhiteRect.centery
                        legionaryWhiteRect.centerx = step
                        legionaryWhiteRect.centery = step*3
                        cardinalBlackRectCopy_1.centerx=legionaryWhitexBefore
                        cardinalBlackRectCopy_1.centery=legionaryWhitexBefore
                        counter+=1
                        cardinalBlackAbilityActivated_1=False
                        cardinalBlackAbilityCounter_1-=1
                    if warriorWhiteRect.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        warriorWhitexBefore=warriorWhiteRect.centerx
                        warriorWhiteyBefore=warriorWhiteRect.centery
                        warriorWhiteRect.centerx = step*2
                        warriorWhiteRect.centery = step*3
                        cardinalBlackRectCopy_1.centerx=warriorWhitexBefore
                        cardinalBlackRectCopy_1.centery=warriorWhiteyBefore
                        counter+=1
                        cardinalBlackAbilityActivated_1=False
                        cardinalBlackAbilityCounter_1-=1
                    if legionaryWhiteRect1.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        legionaryWhitexBefore_1=legionaryWhiteRect1.centerx
                        legionaryWhiteyBefore_1=legionaryWhiteRect1.centery
                        legionaryWhiteRect1.centerx = step*3
                        legionaryWhiteRect1.centery = step*3
                        cardinalBlackRectCopy_1.centerx=legionaryWhitexBefore_1
                        cardinalBlackRectCopy_1.centery=legionaryWhiteyBefore_1
                        counter+=1
                        cardinalBlackAbilityActivated_1=False
                        cardinalBlackAbilityCounter_1-=1
                    if warriorWhiteRect1.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        warriorWhitexBefore_1=warriorWhiteRect1.centerx
                        warriorWhiteyBefore_1=warriorWhiteRect1.centery
                        warriorWhiteRect1.centerx = step
                        warriorWhiteRect1.centery = step*4
                        cardinalBlackRectCopy_1.centerx=warriorWhitexBefore_1
                        cardinalBlackRectCopy_1.centery=warriorWhiteyBefore_1
                        counter+=1
                        cardinalBlackAbilityActivated_1=False
                        cardinalBlackAbilityCounter_1-=1
                    if legionaryWhiteRect2.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        legionaryWhitexBefore_2=legionaryWhiteRect2.centerx
                        legionaryWhiteyBefore_2=legionaryWhiteRect2.centery
                        legionaryWhiteRect2.centerx = step*2
                        legionaryWhiteRect2.centery = step*4
                        cardinalBlackRectCopy_1.centerx=legionaryWhitexBefore_2
                        cardinalBlackRectCopy_1.centery=legionaryWhiteyBefore_2
                        counter+=1
                        cardinalBlackAbilityActivated_1=False
                        cardinalBlackAbilityCounter_1-=1
                    if warriorWhiteRect2.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        warriorWhitexBefore_2=warriorWhiteRect2.centerx
                        warriorWhiteyBefore_2=warriorWhiteRect2.centery
                        warriorWhiteRect2.centerx = step*2
                        warriorWhiteRect2.centery = step*4
                        cardinalBlackRectCopy_1.centerx=warriorWhitexBefore_2
                        cardinalBlackRectCopy_1.centery=warriorWhiteyBefore_2
                        counter+=1
                        cardinalBlackAbilityActivated_1=False
                        cardinalBlackAbilityCounter_1-=1
                    if legionaryWhiteRect3.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        legionaryWhitexBefore_3=legionaryWhiteRect3.centerx
                        legionaryWhiteyBefore_3=legionaryWhiteRect3.centery
                        legionaryWhiteRect3.centerx = step*3
                        legionaryWhiteRect3.centery = step*4
                        cardinalBlackRectCopy_1.centerx=legionaryWhitexBefore_3
                        cardinalBlackRectCopy_1.centery=legionaryWhiteyBefore_3
                        counter+=1
                        cardinalBlackAbilityActivated_1=False
                        cardinalBlackAbilityCounter_1-=1
                    if warriorWhiteRect3.collidepoint(event.pos):
                        cardinalAbilitySound.play()
                        pygame.time.wait(5000)
                        warriorWhitexBefore_3=warriorWhiteRect3.centerx
                        warriorWhiteyBefore_3=warriorWhiteRect3.centery
                        warriorWhiteRect3.centerx = step
                        warriorWhiteRect3.centery = step*5
                        cardinalBlackRectCopy_1.centerx=warriorWhitexBefore_3
                        cardinalBlackRectCopy_1.centery=warriorWhiteyBefore_3
                        counter+=1
                        cardinalBlackAbilityActivated_1=False
                        cardinalBlackAbilityCounter_1-=1

               

                if archbishopBlackRect1.collidepoint(event.pos) and not hadesBlackAbilityActivated and archbishopBlackRect1.centerx!=screen_width-step:
                    if not archbishopBlackPlaying1:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                archbishopBlackPlaying1=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                archbishopBlackPlaying1=True
                elif archbishopBlackPlaying1:
                    archbishopBlackxInit1=archbishopBlackRect1.centerx
                    archbishopBlackyInit1=archbishopBlackRect1.centery
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
                    if (archbishopBlackRect1.centerx <= 480 or archbishopBlackRect1.centerx >= 1440) or (archbishopBlackRect1.centery <= 60 or archbishopBlackRect1.centery >= 1020):
                        archbishopBlackRect1.centerx = archbishopBlackxInit1
                        archbishopBlackRect1.centery = archbishopBlackyInit1
                        archbishopBlackPlaying1=False
                        counter-=1
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
                if archbishopBlackAbilityActivated_1:
                    if plagueDoctorWhiteRect.collidepoint(event.pos):
                        plagueDoctorWhiteRect.centerx = screen_width-step
                        plagueDoctorWhiteRect.centery = step
                        archbishopBlackPlaying1=False
                        archbishopBlackAbilityActivated_1=False
                        archbishopBlackAbilityCounter_1-=1
                        counter+=1
                    if archbishopWhiteRect.collidepoint(event.pos):
                        archbishopWhiteRect.centerx = screen_width-step*2
                        archbishopWhiteRect.centery = step
                        archbishopBlackPlaying1=False
                        archbishopBlackAbilityActivated_1=False
                        archbishopBlackAbilityCounter_1-=1
                        counter+=1
                    if cardinalWhiteRect.collidepoint(event.pos):
                        cardinalWhiteRect.centerx = screen_width-step*3
                        cardinalWhiteRect.centery = step
                        archbishopBlackPlaying1=False
                        archbishopBlackAbilityActivated_1=False
                        archbishopBlackAbilityCounter_1-=1
                        counter+=1
                    if hadesWhiteRect.collidepoint(event.pos):
                        hadesWhiteRect.centerx = screen_width-step
                        hadesWhiteRect.centery = step*2
                        archbishopBlackPlaying1=False
                        archbishopBlackAbilityActivated_1=False
                        archbishopBlackAbilityCounter_1-=1
                        counter+=1
                    if persephoneWhiteRect.collidepoint(event.pos):
                        persephoneWhiteRect.centerx = screen_width-step*2
                        persephoneWhiteRect.centery = step*2
                        archbishopBlackPlaying1=False
                        archbishopBlackAbilityActivated_1=False
                        archbishopBlackAbilityCounter_1-=1
                        counter+=1
                    if cardinalWhiteRect1.collidepoint(event.pos):
                        cardinalWhiteRect1.centerx = screen_width-step*3
                        cardinalWhiteRect1.centery = step*2
                        archbishopBlackPlaying1=False
                        archbishopBlackAbilityActivated_1=False
                        archbishopBlackAbilityCounter_1-=1
                        counter+=1
                    if archbishopWhiteRect1.collidepoint(event.pos):
                        archbishopWhiteRect1.centerx = screen_width-step
                        archbishopWhiteRect1.centery = step*3
                        archbishopBlackPlaying1=False
                        archbishopBlackAbilityActivated_1=False
                        archbishopBlackAbilityCounter_1-=1
                        counter+=1
                    if plagueDoctorWhiteRect1.collidepoint(event.pos):
                        plagueDoctorWhiteRect1.centerx = screen_width-step*2
                        plagueDoctorWhiteRect1.centery = step*3
                        archbishopBlackPlaying1=False
                        archbishopBlackAbilityActivated_1=False
                        archbishopBlackAbilityCounter_1-=1
                        counter+=1
                    if legionaryWhiteRect.collidepoint(event.pos):
                        legionaryWhiteRect.centerx = screen_width-step*3
                        legionaryWhiteRect.centery = step*3
                        archbishopBlackPlaying1=False
                        archbishopBlackAbilityActivated_1=False
                        archbishopBlackAbilityCounter_1-=1
                        counter+=1
                    if warriorWhiteRect.collidepoint(event.pos):
                        warriorWhiteRect.centerx = screen_width-step
                        warriorWhiteRect.centery = step*4
                        archbishopBlackPlaying1=False
                        archbishopBlackAbilityActivated_1=False
                        archbishopBlackAbilityCounter_1-=1
                        counter+=1
                    if legionaryWhiteRect1.collidepoint(event.pos):
                        legionaryWhiteRect1.centerx = screen_width-step*2
                        legionaryWhiteRect1.centery = step*4
                        archbishopBlackPlaying1=False
                        archbishopBlackAbilityActivated_1=False
                        archbishopBlackAbilityCounter_1-=1
                        counter+=1
                    if warriorWhiteRect1.collidepoint(event.pos):
                        warriorWhiteRect1.centerx = screen_width-step*3
                        warriorWhiteRect1.centery = step*4
                        archbishopBlackPlaying1=False
                        archbishopBlackAbilityActivated_1=False
                        archbishopBlackAbilityCounter_1-=1
                        counter+=1
                    if legionaryWhiteRect2.collidepoint(event.pos):
                        legionaryWhiteRect2.centerx = screen_width-step
                        legionaryWhiteRect2.centery = step*5
                        archbishopBlackPlaying1=False
                        archbishopBlackAbilityActivated_1=False
                        archbishopBlackAbilityCounter_1-=1
                        counter+=1
                    if warriorWhiteRect2.collidepoint(event.pos):
                        warriorWhiteRect2.centerx = screen_width-step*2
                        warriorWhiteRect2.centery = step*5
                        archbishopBlackPlaying1=False
                        archbishopBlackAbilityActivated_1=False
                        archbishopBlackAbilityCounter_1-=1
                        counter+=1
                    if legionaryWhiteRect3.collidepoint(event.pos):
                        legionaryWhiteRect3.centerx = screen_width-step*3
                        legionaryWhiteRect3.centery = step*5
                        archbishopBlackPlaying1=False
                        archbishopBlackAbilityActivated_1=False
                        archbishopBlackAbilityCounter_1-=1
                        counter+=1
                    if warriorWhiteRect3.collidepoint(event.pos):
                        warriorWhiteRect3.centerx = screen_width-step
                        warriorWhiteRect3.centery = step*6
                        archbishopBlackPlaying1=False
                        archbishopBlackAbilityActivated_1=False
                        archbishopBlackAbilityCounter_1-=1
                        counter+=1

                if plagueDoctorBlackRect1.collidepoint(event.pos) and not hadesBlackAbilityActivated and plagueDoctorBlackRect1.centerx!=screen_width-step*2:
                    if not plagueDoctorBlackPlaying1:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                plagueDoctorBlackPlaying1=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                plagueDoctorBlackPlaying1=True
                elif plagueDoctorBlackPlaying1:
                    plagueBlackxInit1=plagueDoctorBlackRect1.centerx
                    plagueBlackyInit1=plagueDoctorBlackRect1.centery
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
                    if (plagueDoctorBlackRect1.centerx <= 480 or plagueDoctorBlackRect1.centerx >= 1440) or (plagueDoctorBlackRect1.centery <= 60 or plagueDoctorBlackRect1.centery >= 1020):
                        plagueDoctorBlackRect1.centerx = plagueBlackxInit1
                        plagueDoctorBlackRect1.centery = plagueBlackyInit1
                        plagueDoctorBlackPlaying1=False
                        counter-=1
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
                if rectPlagueDoctorBlackAbilityActivated_1:
                    if archbishopBlackRect.collidepoint(event.pos) and archbishopBlackRect.centerx==screen_width-step*2:
                        archbishopBlackRect.centerx=archbishopBlackxInit
                        archbishopBlackRect.centery=archbishopBlackyInit
                        plagueDoctorBlackPlaying1=False
                        counter+=1
                        rectPlagueDoctorBlackAbilityCounter_1-=1
                    elif cardinalBlackRect.collidepoint(event.pos) and cardinalBlackRect.centerx==screen_width-step*3:
                        cardinalBlackRect.centerx=cardinalBlackxInit
                        cardinalBlackRect.centery=cardinalBlackyInit
                        plagueDoctorBlackPlaying1=False
                        counter+=1
                        rectPlagueDoctorBlackAbilityCounter_1-=1
                    elif cardinalBlackRect1.collidepoint(event.pos) and cardinalBlackRect1.centerx==screen_width-step*3:
                        cardinalBlackRect1.centerx=cardinalBlackxInit1
                        cardinalBlackRect1.centery=cardinalBlackyInit1
                        plagueDoctorBlackPlaying1=False
                        counter+=1
                        rectPlagueDoctorBlackAbilityCounter_1-=1
                        print("yes")
                    elif archbishopBlackRect1.collidepoint(event.pos) and archbishopBlackRect1.centerx==screen_width-step:
                        archbishopBlackRect1.centerx=archbishopBlackxInit1
                        archbishopBlackRect1.centery=archbishopBlackyInit1
                        plagueDoctorBlackPlaying1=False
                        counter+=1
                        rectPlagueDoctorBlackAbilityCounter_1-=1
                    elif plagueDoctorBlackRect1.collidepoint(event.pos) and plagueDoctorBlackRect1.centerx==screen_width-step*2:
                        plagueDoctorBlackRect1.centerx=plagueBlackxInit1
                        plagueDoctorBlackRect1.centery=plagueBlackyInit1
                        plagueDoctorBlackPlaying1=False
                        counter+=1
                        rectPlagueDoctorBlackAbilityCounter_1-=1
                    elif legionaryBlackRect.collidepoint(event.pos) and legionaryBlackRect.centerx==screen_width-step*3:
                        legionaryBlackRect.centerx=legionaryBlackxInit
                        legionaryBlackRect.centery=legionaryBlackyInit
                        plagueDoctorBlackPlaying1=False
                        counter+=1
                        rectPlagueDoctorBlackAbilityCounter_1-=1
                    elif warriorBlackRect.collidepoint(event.pos) and warriorBlackRect.centerx==screen_width-step:
                        warriorBlackRect.centerx=warriorBlackxInit
                        warriorBlackRect.centery=warriorBlackyInit
                        plagueDoctorBlackPlaying1=False
                        counter+=1
                        rectPlagueDoctorBlackAbilityCounter_1-=1
                    elif legionaryBlackRect1.collidepoint(event.pos) and legionaryBlackRect1.centerx==screen_width-step*2:
                        legionaryBlackRect1.centerx=legionaryBlackxInit1
                        legionaryBlackRect1.centery=legionaryBlackyInit1
                        plagueDoctorBlackPlaying1=False
                        counter+=1
                        rectPlagueDoctorBlackAbilityCounter_1-=1
                    elif warriorBlackRect1.collidepoint(event.pos) and warriorBlackRect1.centerx==screen_width-step*3:
                        warriorBlackRect1.centerx=warriorBlackxInit1
                        warriorBlackRect1.centery=warriorBlackyInit1
                        plagueDoctorBlackPlaying1=False
                        counter+=1
                        rectPlagueDoctorBlackAbilityCounter_1-=1
                    elif legionaryBlackRect2.collidepoint(event.pos) and legionaryBlackRect2.centerx==screen_width-step:
                        legionaryBlackRect2.centerx=legionaryBlackxInit2
                        legionaryBlackRect2.centery=legionaryBlackyInit2
                        plagueDoctorBlackPlaying1=False
                        counter+=1
                        rectPlagueDoctorBlackAbilityCounter_1-=1
                    elif warriorBlackRect2.collidepoint(event.pos) and warriorBlackRect2.centerx==screen_width-step*2:
                        warriorBlackRect2.centerx=warriorBlackxInit2
                        warriorBlackRect2.centery=warriorBlackyInit2
                        plagueDoctorBlackPlaying1=False
                        counter+=1
                        rectPlagueDoctorBlackAbilityCounter_1-=1
                    elif legionaryBlackRect3.collidepoint(event.pos) and legionaryBlackRect3.centerx==screen_width-step*3:
                        legionaryBlackRect3.centerx=legionaryBlackxInit3
                        legionaryBlackRect3.centery=legionaryBlackyInit3
                        plagueDoctorBlackPlaying1=False
                        counter+=1
                        rectPlagueDoctorBlackAbilityCounter_1-=1
                    elif warriorBlackRect3.collidepoint(event.pos) and warriorBlackRect3.centerx==screen_width-step:
                        warriorBlackRect3.centerx=warriorBlackxInit3
                        warriorBlackRect3.centery=warriorBlackyInit3
                        plagueDoctorBlackPlaying1=False
                        counter+=1
                        rectPlagueDoctorBlackAbilityCounter_1-=1
                    elif cardinalBlackRectCopy.collidepoint(event.pos) and cardinalBlackRectCopy.centerx==screen_width-step*2:
                        cardinalBlackRectCopy.centerx=cardinalBlackxInitCopy
                        cardinalBlackRectCopy.centery=cardinalBlackyInitCopy
                        plagueDoctorBlackPlaying1=False
                        counter+=1
                        rectPlagueDoctorBlackAbilityCounter_1-=1
                        
                    elif cardinalBlackRectCopy_1.collidepoint(event.pos) and cardinalBlackRectCopy_1.centerx==screen_width-step*3:
                        cardinalBlackRectCopy_1.centerx=cardinalBlackxInitCopy1
                        cardinalBlackRectCopy_1.centery=cardinalBlackyInitCopy1
                        plagueDoctorBlackPlaying1=False
                        counter+=1
                        rectPlagueDoctorBlackAbilityCounter_1-=1
                    else:
                        plagueDoctorBlackPlaying1=False
                        rectPlagueDoctorBlackAbilityActivated=False

                if legionaryBlackRect.collidepoint(event.pos) and not hadesBlackAbilityActivated and legionaryBlackRect.centerx!=screen_width-step*3:
                    if not legionaryBlackPlaying:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                legionaryBlackPlaying=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                legionaryBlackPlaying=True
                elif legionaryBlackPlaying:
                    legionaryBlackxInit=legionaryBlackRect.centerx
                    legionaryBlackyInit=legionaryBlackRect.centery
                    if rectLegionaryBlack1.collidepoint(event.pos):
                        rectLegionaryBlackxAbility=legionaryBlackRect.centerx
                        rectLegionaryBlackyAbility=legionaryBlackRect.centery
                        legionaryBlackRect.centerx = rectLegionaryBlack1.centerx
                        legionaryBlackRect.centery = rectLegionaryBlack1.centery
                        counter += 1
                        legionaryBlackPlaying=False
                    elif rectLegionaryBlack2.collidepoint(event.pos):
                        rectLegionaryBlackxAbility=legionaryBlackRect.centerx
                        rectLegionaryBlackyAbility=legionaryBlackRect.centery
                        legionaryBlackRect.centerx = rectLegionaryBlack2.centerx
                        legionaryBlackRect.centery = rectLegionaryBlack2.centery
                        counter += 1
                        legionaryBlackPlaying=False
                    elif rectLegionaryBlack3.collidepoint(event.pos):
                        rectLegionaryBlackxAbility=legionaryBlackRect.centerx
                        rectLegionaryBlackyAbility=legionaryBlackRect.centery
                        legionaryBlackRect.centerx = rectLegionaryBlack3.centerx
                        legionaryBlackRect.centery = rectLegionaryBlack3.centery
                        counter += 1
                        legionaryBlackPlaying=False
                    else:
                        legionaryBlackRect.centerx = legionaryBlackxInit
                        legionaryBlackRect.centery = legionaryBlackyInit
                        legionaryBlackPlaying=False
                    if (legionaryBlackRect.centerx <= 480 or legionaryBlackRect.centerx >= 1440) or (legionaryBlackRect.centery <= 60 or legionaryBlackRect.centery >= 1020):
                        legionaryBlackRect.centerx = legionaryBlackxInit
                        legionaryBlackRect.centery = legionaryBlackyInit
                        legionaryBlackPlaying=False
                        counter-=1
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

                if warriorBlackRect.collidepoint(event.pos) and not hadesBlackAbilityActivated and warriorBlackRect.centerx!=screen_width-step:
                    if not warriorBlackPlaying:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                warriorBlackPlaying=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                warriorBlackPlaying=True
                elif warriorBlackPlaying:
                    warriorBlackxInit=warriorBlackRect.centerx
                    warriorBlackyInit=warriorBlackRect.centery
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
                    if (warriorBlackRect.centerx <= 480 or warriorBlackRect.centerx >= 1440) or (warriorBlackRect.centery <= 60 or warriorBlackRect.centery >= 1020):
                        warriorBlackRect.centerx = warriorBlackxInit
                        warriorBlackRect.centery = warriorBlackyInit
                        warriorBlackPlaying=False
                        counter-=1
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
                        
                if warriorBlackRect1.collidepoint(event.pos) and not hadesBlackAbilityActivated and warriorBlackRect1.centerx!=screen_width-step*3:
                    if not warriorBlackPlaying1:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                warriorBlackPlaying1=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                warriorBlackPlaying1=True
                elif warriorBlackPlaying1:
                    warriorBlackxInit1=warriorBlackRect1.centerx
                    warriorBlackyInit1=warriorBlackRect1.centery
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
                    elif rectWarriorBlack2_1.collidepoint(event.pos):
                        warriorBlackRect1.centerx = rectWarriorBlack2_1.centerx
                        warriorBlackRect1.centery = rectWarriorBlack2_1.centery
                        counter += 1
                        warriorBlackPlaying1=False
                    elif rectWarriorBlack3_1.collidepoint(event.pos):
                        warriorBlackRect1.centerx = rectWarriorBlack3_1.centerx
                        warriorBlackRect1.centery = rectWarriorBlack3_1.centery
                        counter += 1
                        warriorBlackPlaying1=False
                    elif rectWarriorBlack4_1.collidepoint(event.pos):
                        warriorBlackRect1.centerx = rectWarriorBlack4_1.centerx
                        warriorBlackRect1.centery = rectWarriorBlack4_1.centery
                        counter += 1
                        warriorBlackPlaying1=False
                    else:
                        warriorBlackRect1.centerx = warriorBlackxInit1
                        warriorBlackRect1.centery = warriorBlackyInit1
                        warriorBlackPlaying1=False
                    if (warriorBlackRect1.centerx <= 480 or warriorBlackRect1.centerx >= 1440) or (warriorBlackRect1.centery <= 60 or warriorBlackRect1.centery >= 1020):
                        warriorBlackRect1.centerx = warriorBlackxInit1
                        warriorBlackRect1.centery = warriorBlackyInit1
                        warriorBlackPlaying1=False
                        counter-=1
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


                if legionaryBlackRect1.collidepoint(event.pos) and not hadesBlackAbilityActivated and legionaryBlackRect1.centerx!=screen_width-step*2:
                    if not legionaryBlackPlaying1:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                legionaryBlackPlaying1=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                legionaryBlackPlaying1=True
                elif legionaryBlackPlaying1:
                    legionaryBlackxInit1=legionaryBlackRect1.centerx
                    legionaryBlackyInit1=legionaryBlackRect1.centery
                    if rectLegionaryBlack1_1.collidepoint(event.pos):
                        rectLegionaryBlackxAbility_1=legionaryBlackRect1.centerx
                        rectLegionaryBlackyAbility_1=legionaryBlackRect1.centery
                        legionaryBlackRect1.centerx = rectLegionaryBlack1_1.centerx
                        legionaryBlackRect1.centery = rectLegionaryBlack1_1.centery
                        counter += 1
                        legionaryBlackPlaying1=False
                    elif rectLegionaryBlack2_1.collidepoint(event.pos):
                        rectLegionaryBlackxAbility_1=legionaryBlackRect1.centerx
                        rectLegionaryBlackyAbility_1=legionaryBlackRect1.centery
                        legionaryBlackRect1.centerx = rectLegionaryBlack2_1.centerx
                        legionaryBlackRect1.centery = rectLegionaryBlack2_1.centery
                        counter += 1
                        legionaryBlackPlaying1=False
                    elif rectLegionaryBlack3_1.collidepoint(event.pos):
                        rectLegionaryBlackxAbility_1=legionaryBlackRect1.centerx
                        rectLegionaryBlackyAbility_1=legionaryBlackRect1.centery
                        legionaryBlackRect1.centerx = rectLegionaryBlack3_1.centerx
                        legionaryBlackRect1.centery = rectLegionaryBlack3_1.centery
                        counter += 1
                        legionaryBlackPlaying1=False
                    else:
                        legionaryBlackRect1.centerx = legionaryBlackxInit1
                        legionaryBlackRect1.centery = legionaryBlackyInit1
                        legionaryBlackPlaying1=False
                    if (legionaryBlackRect1.centerx <= 480 or legionaryBlackRect1.centerx >= 1440) or (legionaryBlackRect1.centery <= 60 or legionaryBlackRect1.centery >= 1020):
                        legionaryBlackRect1.centerx = legionaryBlackxInit1
                        legionaryBlackRect1.centery = legionaryBlackyInit1
                        legionaryBlackPlaying1=False
                        counter-=1
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

                if warriorBlackRect2.collidepoint(event.pos) and not hadesBlackAbilityActivated and warriorBlackRect2.centerx!=screen_width-step*2:
                    if not warriorBlackPlaying2:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                warriorBlackPlaying2=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                warriorBlackPlaying2=True
                elif warriorBlackPlaying2:
                    warriorBlackxInit2=warriorBlackRect2.centerx
                    warriorBlackyInit2=warriorBlackRect2.centery
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
                    if (warriorBlackRect2.centerx <= 480 or warriorBlackRect2.centerx >= 1440) or (warriorBlackRect2.centery <= 60 or warriorBlackRect2.centery >= 1020):
                        warriorBlackRect2.centerx = warriorBlackxInit2
                        warriorBlackRect2.centery = warriorBlackyInit2
                        warriorBlackPlaying2=False
                        counter-=1
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


                if legionaryBlackRect2.collidepoint(event.pos) and not hadesBlackAbilityActivated and legionaryBlackRect2.centerx!=screen_width-step:
                    if not legionaryBlackPlaying2:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                legionaryBlackPlaying2=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                legionaryBlackPlaying2=True
                elif legionaryBlackPlaying2:
                    legionaryBlackxInit2=legionaryBlackRect2.centerx
                    legionaryBlackyInit2=legionaryBlackRect2.centery
                    if rectLegionaryBlack1_2.collidepoint(event.pos):
                        rectLegionaryBlackxAbility_2=legionaryBlackRect2.centerx
                        rectLegionaryBlackyAbility_2=legionaryBlackRect2.centery
                        legionaryBlackRect2.centerx = rectLegionaryBlack1_2.centerx
                        legionaryBlackRect2.centery = rectLegionaryBlack1_2.centery
                        counter += 1
                        legionaryBlackPlaying2=False
                    elif rectLegionaryBlack2_2.collidepoint(event.pos):
                        rectLegionaryBlackxAbility_2=legionaryBlackRect2.centerx
                        rectLegionaryBlackyAbility_2=legionaryBlackRect2.centery
                        legionaryBlackRect2.centerx = rectLegionaryBlack2_2.centerx
                        legionaryBlackRect2.centery = rectLegionaryBlack2_2.centery
                        counter += 1
                        legionaryBlackPlaying2=False
                    elif rectLegionaryBlack3_2.collidepoint(event.pos):
                        rectLegionaryBlackxAbility_2=legionaryBlackRect2.centerx
                        rectLegionaryBlackyAbility_2=legionaryBlackRect2.centery
                        legionaryBlackRect2.centerx = rectLegionaryBlack3_2.centerx
                        legionaryBlackRect2.centery = rectLegionaryBlack3_2.centery
                        counter += 1
                        legionaryBlackPlaying2=False
                    else:
                        legionaryBlackRect2.centerx = legionaryBlackxInit2
                        legionaryBlackRect2.centery = legionaryBlackyInit2
                        legionaryBlackPlaying2=False
                    if (legionaryBlackRect2.centerx <= 480 or legionaryBlackRect2.centerx >= 1440) or (legionaryBlackRect2.centery <= 60 or legionaryBlackRect2.centery >= 1020):
                        legionaryBlackRect2.centerx = legionaryBlackxInit2
                        legionaryBlackRect2.centery = legionaryBlackyInit2
                        legionaryBlackPlaying2=False
                        counter-=1
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

                if legionaryBlackRect3.collidepoint(event.pos) and not hadesBlackAbilityActivated and legionaryBlackRect3.centerx!=screen_width-step*3:
                    if not legionaryBlackPlaying3:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                legionaryBlackPlaying3=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                legionaryBlackPlaying3=True
                elif legionaryBlackPlaying3:
                    legionaryBlackxInit3=legionaryBlackRect3.centerx
                    legionaryBlackyInit3=legionaryBlackRect3.centery
                    if rectLegionaryBlack1_3.collidepoint(event.pos):
                        rectLegionaryBlackxAbility_3=legionaryBlackRect3.centerx
                        rectLegionaryBlackyAbility_3=legionaryBlackRect3.centery
                        legionaryBlackRect3.centerx = rectLegionaryBlack1_3.centerx
                        legionaryBlackRect3.centery = rectLegionaryBlack1_3.centery
                        counter += 1
                        legionaryBlackPlaying3=False
                    elif rectLegionaryBlack2_3.collidepoint(event.pos):
                        rectLegionaryBlackxAbility_3=legionaryBlackRect3.centerx
                        rectLegionaryBlackyAbility_3=legionaryBlackRect3.centery
                        legionaryBlackRect3.centerx = rectLegionaryBlack2_3.centerx
                        legionaryBlackRect3.centery = rectLegionaryBlack2_3.centery
                        counter += 1
                        legionaryBlackPlaying3=False
                    elif rectLegionaryBlack3_3.collidepoint(event.pos):
                        rectLegionaryBlackxAbility_3=legionaryBlackRect3.centerx
                        rectLegionaryBlackyAbility_3=legionaryBlackRect3.centery
                        legionaryBlackRect3.centerx = rectLegionaryBlack3_3.centerx
                        legionaryBlackRect3.centery = rectLegionaryBlack3_3.centery
                        counter += 1
                        legionaryBlackPlaying3=False
                    else:
                        legionaryBlackRect3.centerx = legionaryBlackxInit3
                        legionaryBlackRect3.centery = legionaryBlackyInit3
                        legionaryBlackPlaying3=False
                    if (legionaryBlackRect3.centerx <= 480 or legionaryBlackRect3.centerx >= 1440) or (legionaryBlackRect3.centery <= 60 or legionaryBlackRect3.centery >= 1020):
                        legionaryBlackRect3.centerx = legionaryBlackxInit3
                        legionaryBlackRect3.centery = legionaryBlackyInit3
                        legionaryBlackPlaying3=False
                        counter-=1
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

                if warriorBlackRect3.collidepoint(event.pos) and not hadesBlackAbilityActivated and warriorBlackRect3.centerx!=screen_width-step:
                    if not warriorBlackPlaying3:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                warriorBlackPlaying3=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                warriorBlackPlaying3=True
                elif warriorBlackPlaying3:
                    warriorBlackxInit3=warriorBlackRect3.centerx
                    warriorBlackyInit3=warriorBlackRect3.centery
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
                    elif rectWarriorBlack1_3.collidepoint(event.pos):
                        warriorBlackRect3.centerx = rectWarriorBlack1_3.centerx
                        warriorBlackRect3.centery = rectWarriorBlack1_3.centery
                        counter += 1
                        warriorBlackPlaying3=False
                    elif rectWarriorBlack2_3.collidepoint(event.pos):
                        warriorBlackRect3.centerx = rectWarriorBlack2_3.centerx
                        warriorBlackRect3.centery = rectWarriorBlack2_3.centery
                        counter += 1
                        warriorBlackPlaying3=False
                    elif rectWarriorBlack3_3.collidepoint(event.pos):
                        warriorBlackRect3.centerx = rectWarriorBlack3_3.centerx
                        warriorBlackRect3.centery = rectWarriorBlack3_3.centery
                        counter += 1
                        warriorBlackPlaying3=False
                    elif rectWarriorBlack4_3.collidepoint(event.pos):
                        warriorBlackRect3.centerx = rectWarriorBlack4_3.centerx
                        warriorBlackRect3.centery = rectWarriorBlack4_3.centery
                        counter += 1
                        warriorBlackPlaying3=False
                    else:
                        warriorBlackRect3.centerx = warriorBlackxInit3
                        warriorBlackRect3.centery = warriorBlackyInit3
                        warriorBlackPlaying3=False
                    if (warriorBlackRect3.centerx <= 480 or warriorBlackRect3.centerx >= 1440) or (warriorBlackRect3.centery <= 60 or warriorBlackRect3.centery >= 1020):
                        warriorBlackRect3.centerx = warriorBlackxInit3
                        warriorBlackRect3.centery = warriorBlackyInit3
                        warriorBlackPlaying3=False
                        counter-=1
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

                if cardinalBlackRectCopy.collidepoint(event.pos) and counter%2!=0 and cardinalBlackRectCopy.centerx!=screen_width-step*2:
                    if not cardinalBlackPlayingCopy:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                cardinalBlackPlayingCopy=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                cardinalBlackPlayingCopy=True
                elif cardinalBlackPlayingCopy:
                    cardinalBlackxInitCopy=cardinalBlackRectCopy.centerx
                    cardinalBlackyInitCopy=cardinalBlackRectCopy.centery
                    if rectCardinalBlackCopy1.collidepoint(event.pos):
                        cardinalBlackRectCopy.centerx=rectCardinalBlackCopy1.centerx
                        cardinalBlackRectCopy.centery=rectCardinalBlackCopy1.centery
                        counter+=1
                        cardinalBlackPlayingCopy=False
                    elif rectCardinalBlackCopy2.collidepoint(event.pos):
                        cardinalBlackRectCopy.centerx=rectCardinalBlackCopy2.centerx
                        cardinalBlackRectCopy.centery=rectCardinalBlackCopy2.centery
                        counter+=1
                        cardinalBlackPlayingCopy=False
                    elif rectCardinalBlackCopy3.collidepoint(event.pos):
                        cardinalBlackRectCopy.centerx=rectCardinalBlackCopy3.centerx
                        cardinalBlackRectCopy.centery=rectCardinalBlackCopy3.centery
                        counter+=1
                        cardinalBlackPlayingCopy=False
                    elif rectCardinalBlackCopy4.collidepoint(event.pos):
                        cardinalBlackRectCopy.centerx=rectCardinalBlackCopy4.centerx
                        cardinalBlackRectCopy.centery=rectCardinalBlackCopy4.centery
                        counter+=1
                        cardinalBlackPlayingCopy=False
                    else:
                        cardinalBlackRectCopy.centerx=cardinalBlackxInitCopy
                        cardinalBlackRectCopy.centery=cardinalBlackyInitCopy
                        cardinalBlackPlayingCopy=False
                    if (cardinalBlackRectCopy.centerx <= 480 or cardinalBlackRectCopy.centerx >= 1440) or (cardinalBlackRectCopy.centery <= 60 or cardinalBlackRectCopy.centery >= 1020):
                        cardinalBlackRectCopy.centerx = cardinalBlackxInitCopy
                        cardinalBlackRectCopy.centery = cardinalBlackyInitCopy
                        cardinalBlackPlayingCopy=False
                        counter-=1
                
                if cardinalBlackRectCopy_1.collidepoint(event.pos) and counter%2!=0 and cardinalBlackRectCopy_1.centerx!=screen_width-step*3:
                    if not cardinalBlackPlayingCopy1:
                        for x,playing in enumerate(figuresBlackPlaying):
                            if playing==True:
                                playing=False
                                cardinalBlackPlayingCopy1=True
                                break
                            elif x==len(figuresBlackPlaying)-1:
                                cardinalBlackPlayingCopy1=True
                elif cardinalBlackPlayingCopy1:
                    cardinalBlackxInitCopy1=cardinalBlackRectCopy_1.centerx
                    cardinalBlackyInitCopy1=cardinalBlackRectCopy_1.centery
                    if rectCardinalBlackCopy1_1.collidepoint(event.pos):
                        cardinalBlackRectCopy_1.centerx=rectCardinalBlackCopy1_1.centerx
                        cardinalBlackRectCopy_1.centery=rectCardinalBlackCopy1_1.centery
                        counter+=1
                        cardinalBlackPlayingCopy1=False
                    elif rectCardinalBlackCopy2_1.collidepoint(event.pos):
                        cardinalBlackRectCopy_1.centerx=rectCardinalBlackCopy2_1.centerx
                        cardinalBlackRectCopy_1.centery=rectCardinalBlackCopy2_1.centery
                        counter+=1
                        cardinalBlackPlayingCopy1=False
                    elif rectCardinalBlackCopy3_1.collidepoint(event.pos):
                        cardinalBlackRectCopy_1.centerx=rectCardinalBlackCopy3_1.centerx
                        cardinalBlackRectCopy_1.centery=rectCardinalBlackCopy3_1.centery
                        counter+=1
                        cardinalBlackPlayingCopy1=False
                    elif rectCardinalBlackCopy4_1.collidepoint(event.pos):
                        cardinalBlackRectCopy_1.centerx=rectCardinalBlackCopy4_1.centerx
                        cardinalBlackRectCopy_1.centery=rectCardinalBlackCopy4_1.centery
                        counter+=1
                        cardinalBlackPlayingCopy1=False
                    else:
                        cardinalBlackRectCopy_1.centerx=cardinalBlackxInitCopy1
                        cardinalBlackRectCopy_1.centery=cardinalBlackyInitCopy1
                        cardinalBlackPlayingCopy1=False
                    if (cardinalBlackRectCopy_1.centerx <= 480 or cardinalBlackRectCopy_1.centerx >= 1440) or (cardinalBlackRectCopy_1.centery <= 60 or cardinalBlackRectCopy_1.centery >= 1020):
                        cardinalBlackRectCopy_1.centerx = cardinalBlackxInitCopy1
                        cardinalBlackRectCopy_1.centery = cardinalBlackyInitCopy1
                        cardinalBlackPlayingCopy1=False
                        counter-=1

        if legionaryWhitePlaying and counter%4==0:
            screen.blit(ability_text,ability_text_rect)
        elif legionaryWhitePlaying1 and counter%4==0:
            screen.blit(ability_text,ability_text_rect)
        elif legionaryWhitePlaying2 and counter%4==0:
            screen.blit(ability_text,ability_text_rect)
        elif legionaryWhitePlaying3 and counter%4==0:
            screen.blit(ability_text,ability_text_rect)
        if legionaryBlackPlaying and (counter-1)%4==0:
            screen.blit(ability_text,ability_text_rect)
        elif legionaryBlackPlaying1 and (counter-1)%4==0:
            screen.blit(ability_text,ability_text_rect)
        elif legionaryBlackPlaying2 and (counter-1)%4==0:
            screen.blit(ability_text,ability_text_rect)
        elif legionaryBlackPlaying3 and (counter-1)%4==0:
            screen.blit(ability_text,ability_text_rect)
        if plagueDoctorWhitePlaying and rectPlagueDoctorWhiteAbilityCounter==1:
            screen.blit(ability_text,ability_text_rect)
        elif plagueDoctorWhitePlaying1 and rectPlagueDoctorBlackAbilityCounter_1==1:
            screen.blit(ability_text,ability_text_rect)
        elif plagueDoctorBlackPlaying and rectPlagueDoctorBlackAbilityCounter==1:
            screen.blit(ability_text,ability_text_rect)
        elif plagueDoctorBlackPlaying1 and rectPlagueDoctorBlackAbilityCounter_1==1:
            screen.blit(ability_text,ability_text_rect)
        if archbishopWhitePlaying and archbishopWhiteAbilityCounter==1:
            screen.blit(ability_text,ability_text_rect)
        elif archbishopWhitePlaying1 and archbishopWhiteAbilityCounter_1==1:
            screen.blit(ability_text,ability_text_rect)
        elif archbishopBlackPlaying and archbishopBlackAbilityCounter==1:
            screen.blit(ability_text,ability_text_rect)
        elif archbishopBlackPlaying1 and archbishopBlackAbilityCounter_1==1:
            screen.blit(ability_text,ability_text_rect)
        if cardinalWhitePlaying and cardinalWhiteAbilityCounter==1:
            screen.blit(ability_text,ability_text_rect)
        elif cardinalWhitePlaying1 and cardinalWhiteAbilityCounter_1==1:
            screen.blit(ability_text,ability_text_rect)
        elif cardinalBlackPlaying and cardinalBlackAbilityCounter==1:
            screen.blit(ability_text,ability_text_rect)
        elif cardinalBlackPlaying1 and cardinalBlackAbilityCounter_1==1:
            screen.blit(ability_text,ability_text_rect)
        if persephoneWhitePlaying and persephoneWhiteAbilityCounter!=0:
            screen.blit(ability_text,ability_text_rect)
        elif persephoneBlackPlaying and persephoneBlackAbilityCounter!=0:
            screen.blit(ability_text,ability_text_rect)
        if hadesWhitePlaying and hadesWhiteAbilityCounter!=0:
            screen.blit(ability_text,ability_text_rect)
        elif hadesBlackPlaying and hadesBlackAbilityCounter!=0:
            screen.blit(ability_text,ability_text_rect)
        
        keys=pygame.key.get_pressed()
        if keys[pygame.K_F9] and legionaryWhitePlaying and counter%4==0:
            legionaryWhiteRect.centerx=rectLegionaryWhitexAbility
            legionaryWhiteRect.centery=rectLegionaryWhiteyAbility
            counter+=1
            legionaryWhitePlaying=False
        elif keys[pygame.K_F9] and legionaryWhitePlaying1 and counter%4==0:
            legionaryWhiteRect1.centerx=rectLegionaryWhitexAbility_1
            legionaryWhiteRect1.centery=rectLegionaryWhiteyAbility_1
            counter+=1
            legionaryWhitePlaying1=False
        elif keys[pygame.K_F9] and legionaryWhitePlaying2 and counter%4==0:
            legionaryWhiteRect2.centerx=rectLegionaryWhitexAbility_2
            legionaryWhiteRect2.centery=rectLegionaryWhiteyAbility_2
            counter+=1
            legionaryWhitePlaying2=False
        elif keys[pygame.K_F9] and legionaryWhitePlaying3 and counter%4==0:
            legionaryWhiteRect3.centerx=rectLegionaryWhitexAbility_3
            legionaryWhiteRect3.centery=rectLegionaryWhiteyAbility_3
            counter+=1
            legionaryWhitePlaying3=False
        if keys[pygame.K_F9] and legionaryBlackPlaying and (counter-1)%4==0:
            legionaryBlackRect.centerx=rectLegionaryBlackxAbility
            legionaryBlackRect.centery=rectLegionaryBlackyAbility
            counter+=1
            legionaryBlackPlaying=False
        elif keys[pygame.K_F9] and legionaryBlackPlaying1 and (counter-1)%4==0:
            legionaryBlackRect1.centerx=rectLegionaryBlackxAbility_1
            legionaryBlackRect1.centery=rectLegionaryBlackyAbility_1
            counter+=1
            legionaryBlackPlaying1=False
        elif keys[pygame.K_F9] and legionaryBlackPlaying2 and (counter-1)%4==0:
            legionaryBlackRect2.centerx=rectLegionaryBlackxAbility_2
            legionaryBlackRect2.centery=rectLegionaryBlackyAbility_2
            counter+=1
            legionaryBlackPlaying2=False
        elif keys[pygame.K_F9] and legionaryBlackPlaying3 and (counter-1)%4==0:
            legionaryBlackRect3.centerx=rectLegionaryBlackxAbility_3
            legionaryBlackRect3.centery=rectLegionaryBlackyAbility_3
            counter+=1
            legionaryBlackPlaying3=False
        if keys[pygame.K_F9] and plagueDoctorWhitePlaying and rectPlagueDoctorWhiteAbilityCounter==1:
            rectPlagueDoctorWhiteAbilityActivated=True
        elif keys[pygame.K_F9] and plagueDoctorWhitePlaying1 and rectPlagueDoctorBlackAbilityCounter_1==1:
            rectPlagueDoctorWhiteAbilityActivated_1=True
        elif keys[pygame.K_F9] and plagueDoctorBlackPlaying and rectPlagueDoctorBlackAbilityCounter==1:
            rectPlagueDoctorBlackAbilityActivated=True
        elif keys[pygame.K_F9] and plagueDoctorBlackPlaying1 and rectPlagueDoctorBlackAbilityCounter_1==1:
            rectPlagueDoctorBlackAbilityActivated_1=True
        if keys[pygame.K_F9] and archbishopWhitePlaying and archbishopWhiteAbilityCounter==1:
            archbishopWhiteAbilityActivated=True
        elif keys[pygame.K_F9] and archbishopWhitePlaying1 and archbishopWhiteAbilityCounter_1==1:
            archbishopWhiteAbilityActivated_1=True
        elif keys[pygame.K_F9] and archbishopBlackPlaying and archbishopBlackAbilityCounter==1:
            archbishopBlackAbilityActivated=True
        elif keys[pygame.K_F9] and archbishopBlackPlaying1 and archbishopBlackAbilityCounter_1==1:
            archbishopBlackAbilityActivated_1=True
        if keys[pygame.K_F9] and cardinalWhitePlaying and cardinalWhiteAbilityCounter==1:
            cardinalWhiteAbilityActivated=True
        elif keys[pygame.K_F9] and cardinalWhitePlaying1 and cardinalWhiteAbilityCounter_1==1:
            cardinalWhiteAbilityActivated_1=True
        elif keys[pygame.K_F9] and cardinalBlackPlaying and cardinalBlackAbilityCounter==1:
            cardinalBlackAbilityActivated=True
        elif keys[pygame.K_F9] and cardinalBlackPlaying1 and cardinalBlackAbilityCounter_1==1:
            cardinalBlackAbilityActivated_1=True
        if keys[pygame.K_F9] and persephoneWhitePlaying and persephoneWhiteAbilityCounter!=0:
            persephoneWhiteAbilityActivated=True
        elif keys[pygame.K_F9] and persephoneBlackPlaying and persephoneBlackAbilityCounter!=0:
            persephoneBlackAbilityActivated=True
        if keys[pygame.K_F9] and hadesWhitePlaying and hadesWhiteAbilityCounter!=0:
            hadesWhiteAbilityActivated=True
        elif keys[pygame.K_F9] and hadesBlackPlaying and hadesBlackAbilityCounter!=0:
            hadesBlackAbilityActivated=True
        
        if persephoneWhiteAbilityCounter==0:
            persephoneWhiteAbilityActivated=False
        if persephoneBlackAbilityCounter==0:
            persephoneBlackAbilityActivated=False 
        
        if hadesBlackAbilityCounter==0:
            hadesBlackAbilityActivated=False
        if hadesWhiteAbilityCounter==0:
            hadesWhiteAbilityActivated=False

        if late_game:
            if hadesWhiteRect.centerx==step:
                persephoneWhiteAbilityActivated=True
                persephoneWhiteAbilityCounter=999
            else:
                persephoneBlackAbilityActivated=True
                persephoneBlackAbilityCounter=999

        
        if user1_win:
            conn = mysql.connector.connect(
                host="dbs.spskladno.cz",
                user="student3",
                password="spsnet",
                database="vyuka3"
            )
            cursor1 = conn.cursor()
            query = "UPDATE registracechess SET win_count=win_count+1 WHERE email=%s"
            cursor1.execute(query,(user_email_1,))
            conn.commit() 
            # cursor1.close() z nějakého důvodu to s tímto po přihlášení padá, AI nepomohlo
            conn.close()
            play_game=False
            show_main_menu=True
            #Opětovné získání dat pro leaderboard pro možnost obnovení počtu výher po ukončení hry
            db_connection = mysql.connector.connect(
                host="dbs.spskladno.cz",
                user="student3",
                password="spsnet",
                database="vyuka3"
            )

            cursor = db_connection.cursor()

            cursor.execute("SELECT DISTINCT(email),win_count FROM registracechess ORDER BY win_count DESC LIMIT 15")
            result = cursor.fetchall()

            cursor.close()
            db_connection.close()
            pygame.time.wait(1000)
        if user2_win:
            conn = mysql.connector.connect(
                        host="dbs.spskladno.cz",
                        user="student3",
                        password="spsnet",
                        database="vyuka3"
                    )
            cursor1 = conn.cursor()
            query = "UPDATE registracechess SET win_count=win_count+1 WHERE email=%s"
            cursor1.execute(query,(user_email_2,))
            conn.commit() 
            # cursor1.close() z nějakého důvodu to s tímto po přihlášení padá, AI nepomohlo
            conn.close()
            play_game=False
            show_main_menu=False
            #Opětovné získání dat pro leaderboard pro možnost obnovení počtu výher po ukončení hry
            db_connection = mysql.connector.connect(
                host="dbs.spskladno.cz",
                user="student3",
                password="spsnet",
                database="vyuka3"
            )

            cursor = db_connection.cursor()

            cursor.execute("SELECT DISTINCT(email),win_count FROM registracechess ORDER BY win_count LIMIT 15")
            result = cursor.fetchall()

            cursor.close()
            db_connection.close()
            pygame.time.wait(1000)
        
        if counter%2==0:
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
            if persephoneWhitePlaying and persephoneWhiteAbilityActivated:
                for ctverec in rectsPersephoneWhiteAbility:
                                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                                            ctverec.bottom < 850 or ctverec.top > 60):
                                        pygame.draw.rect(screen, black, ctverec, 5)
            elif persephoneWhitePlaying:
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
            if legionaryWhitePlaying3:
                for ctverec in rectsLegionaryWhite_3:
                        if (ctverec.right < 1440 or ctverec.left > 475) or (
                                ctverec.bottom < 850 or ctverec.top > 60):
                            pygame.draw.rect(screen, black, ctverec, 5)
            if cardinalWhitePlayingCopy:
                for ctverec in rectsCardinalWhiteCopy:
                        if (ctverec.right < 1440 or ctverec.left > 475) or (
                                ctverec.bottom < 850 or ctverec.top > 60):
                            pygame.draw.rect(screen, black, ctverec, 5)
            if cardinalWhitePlayingCopy1:
                for ctverec in rectsCardinalWhiteCopy_1:
                        if (ctverec.right < 1440 or ctverec.left > 475) or (
                                ctverec.bottom < 850 or ctverec.top > 60):
                            pygame.draw.rect(screen, black, ctverec, 5)
        else:
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
            if persephoneBlackAbilityActivated and persephoneBlackPlaying:
                for ctverec in rectsPersephoneBlackAbility:
                        if (ctverec.right < 1440 or ctverec.left > 475) or (
                                ctverec.bottom < 850 or ctverec.top > 60):
                            pygame.draw.rect(screen, black, ctverec, 5)
            elif persephoneBlackPlaying:
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
            if cardinalBlackPlayingCopy:
                for ctverec in rectsCardinalBlackCopy:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                            ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen, black, ctverec, 5)
            if cardinalBlackPlayingCopy1:
                for ctverec in rectsCardinalBlackCopy_1:
                    if (ctverec.right < 1440 or ctverec.left > 475) or (
                            ctverec.bottom < 850 or ctverec.top > 60):
                        pygame.draw.rect(screen, black, ctverec, 5)

            # todo: Kontrola kolize
            # Bude to fungovat tak, že jakmile dojde ke kolizi mezi dvěma figurkami, zkontroluje se hodnota counteru a v závislosti na jeho modulu bude odebrána figurka příslušné barvy
            # counter=0 odehrál bílý, tedy musí brát černou figurku
         

    pygame.display.update()

    clock.tick(60)

pygame.quit()