import pygame
import pymsgbox
import time

pygame.init()

width=600
height=600
size=(width,height)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("INSTAGRAM BOT")

icon=pygame.image.load("C:/Users/bertug/PycharmProjects/Instagram_Bot/Images/instagram.png")
pygame.display.set_icon(icon)

#colors:
black=(0,0,0)
chocalate=(210,105,30)
white=(255,255,255)
green=(0,128,0)
red=(255,0,0)
blue=(0,0,255)
aqua=(0,255,255)
yellow=(255,255,0)
purple=(255,0,255)
orange=(255,165,0)
lime=(0,255,0)
gold=(255,215,0)
salmon=(250,128,114)
deepPink=(255,0,127)
brown=(204,102,0)

loginIMG=pygame.image.load("C:/Users/bertug/PycharmProjects/Instagram_Bot/Images/login.png")
loginBG=pygame.image.load("C:/Users/bertug/PycharmProjects/Instagram_Bot/Images/bgLogin.jpg")
singninBTN=pygame.image.load("C:/Users/bertug/PycharmProjects/Instagram_Bot/Images/btn1.jpg")
loginBTN=pygame.image.load("C:/Users/bertug/PycharmProjects/Instagram_Bot/Images/btn2.jpg")

font = pygame.font.SysFont(None, 30)

def save(username,password):
    users = open("users.txt", "a")
    users.write(username+"\n"+password)
    users.close()

def delete():
    users=open("users.txt")
    lines=users.readlines()
    for i in lines:
        del lines[i]
    users.close()
    y=open("users.txt","w")
    y.writelines(lines)
    y.close()

class texts():
    def write(self, message, color, x, y, size):
        self.message = message
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        font = pygame.font.SysFont(None, size)
        text = font.render(message, True, color)
        screen.blit(text, [x, y])

class login_main_class():
    def login_main_function(self):
        self.user_text = ""
        self.pass_text = ""
        user_rect = pygame.Rect(260, 335, 250, 32)
        pass_rect = pygame.Rect(260, 415, 250, 32)

        inputbox1Color=aqua
        inputbox2Color=aqua

        signinBTNactive=False
        signinBTNactive1 = False

        pygame.key.set_repeat(100, 50)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    active1 = user_rect.collidepoint(event.pos)
                    active2 = pass_rect.collidepoint(event.pos)
                    if active1:
                        inputbox1Color = red
                        inputbox2Color = aqua
                    elif active2:
                        inputbox1Color = aqua
                        inputbox2Color = red
                    else:
                        inputbox1Color = aqua
                        inputbox2Color = aqua

                if event.type == pygame.KEYDOWN:
                    try:
                        if active1:
                            if event.key == pygame.K_BACKSPACE:
                                self.user_text = self.user_text[:-1]
                                if self.pass_text == "" or self.user_text == "":
                                    signinBTNactive = False
                                    signinBTNactive1 = False
                            else:
                                self.user_text += event.unicode
                                signinBTNactive=True
                        elif active2:
                            if event.key == pygame.K_BACKSPACE:
                                self.pass_text = self.pass_text[:-1]
                                if self.pass_text == "" or self.user_text == "":
                                    signinBTNactive = False
                                    signinBTNactive1 = False
                            else:
                                self.pass_text += event.unicode
                                signinBTNactive1=True
                        else:
                            pymsgbox.alert('LÜTFEN BİR VERİ GİRİŞ ÇUBUĞU SEÇİN...', 'UYARI!')
                    except:
                        pymsgbox.alert('LÜTFEN BİR VERİ GİRİŞ ÇUBUĞU SEÇİN...', 'UYARI!')

            screen.fill(black)
            screen.blit(loginBG,(0,0))
            txt=texts()

            textSurfaceNum = font.render(self.user_text, True, white)
            textSurfacePass = font.render(self.pass_text, True, white)

            screen.blit(textSurfaceNum, [270, 342])
            screen.blit(textSurfacePass, [270, 422])

            txt.write("USERNAME: ",yellow,40,335,45)
            txt.write("PASSWORD: ",yellow,40,415,45)

            pygame.draw.rect(screen, inputbox1Color, user_rect, 4)
            pygame.draw.rect(screen, inputbox2Color, pass_rect, 4)

            screen.blit(loginIMG,(200,10))

            mousePosition = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if signinBTNactive==True and signinBTNactive1==True:
                if 50 + 250 > mousePosition[0] > 50 and 495 + 70 > mousePosition[1] > 495:
                    screen.blit(singninBTN, (50, 495))
                    txt.write("KAYIT OL", lime, 90, 515, 50)
                    if click[0] == 1:
                        time.sleep(2)
                        delete()
                        save(self.user_text,self.pass_text)
                        pygame.quit()
                        import Bot_Start
                        Bot_Start.Bot_Start()
                else:
                    screen.blit(singninBTN, (50, 495))
                    txt.write("KAYIT OL", lime, 90, 515, 50)
            else:
                if 50 + 250 > mousePosition[0] > 50 and 495 + 70 > mousePosition[1] > 495:
                    screen.blit(singninBTN, (50, 495))
                    txt.write("KAYIT OL", lime, 90, 515, 50)
                    if click[0] == 1:
                        pymsgbox.alert('LÜTFEN KULLANICI BİLGİLERİNİ GİRİNİZ!!!', 'UYARI!')
                else:
                    screen.blit(singninBTN, (50, 495))
                    txt.write("KAYIT OL", lime, 90, 515, 50)


            if 320 + 250 > mousePosition[0] > 320 and 495 + 70 > mousePosition[1] > 495:
                screen.blit(loginBTN, (320, 495))
                txt.write("KAYDIM VAR", white, 350, 518, 45)
                if click[0] == 1:
                    pygame.quit()
                    time.sleep(1)
                    import Bot_Start
                    Bot_Start.Bot_Start()
            else:
                screen.blit(loginBTN, (320, 495))
                txt.write("KAYDIM VAR", white, 350, 518, 45)
            pygame.display.update()