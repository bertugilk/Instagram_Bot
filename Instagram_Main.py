from selenium import webdriver
import time

oku = open("users.txt", "r")
user = oku.readlines()
oku.close()
usrnm=user[0]
pswrd=user[1]
class Main():
    def __init__(self):
        self.browser = webdriver.Chrome(r"C:\Users\bertug\Downloads\chromedriver85.exe")
        time.sleep(3)
    def Login(self):
        self.browser.get('https://www.instagram.com/accounts/login/?hl=tr')
        self.browser.fullscreen_window()
        time.sleep(3)
        username = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(usrnm)
        time.sleep(2)
        password = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(pswrd)
        time.sleep(4)
        login = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
        login.click()
        time.sleep(3)
        self.browser.fullscreen_window()
    def Home_Page(self):
        home=self.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]')
        home.click()
        time.sleep(3)
        notNow = self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        notNow.click()
        time.sleep(3)
        self.browser.fullscreen_window()
        y = 1000
        for timer in range(0, 50):
            self.browser.execute_script("window.scrollTo(0, " + str(y) + ")")
            y += 700
            time.sleep(4)
    def DirectMessage_Page(self):
        direct = self.browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]')
        direct.click()
        time.sleep(3)
        self.browser.fullscreen_window()
        for i in range(1, 3):
            self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)
    def Discover_Page(self):
        discover = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[1]/div/div[3]/div/div[3]')
        discover.click()
        time.sleep(3)
        self.browser.fullscreen_window()
        y = 1000
        for timer in range(0, 50):
            self.browser.execute_script("window.scrollTo(0, " + str(y) + ")")
            y += 600
            time.sleep(5)
    def mePage(self):
        me=self.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]')
        me.click()
        time.sleep(3)
        myaccount=self.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]')
        myaccount.click()
        time.sleep(3)
        self.browser.fullscreen_window()
    def followers(self):
        time.sleep(2)
        followersButton = self.browser.find_element_by_xpath( '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]')
        followersButton.click()
        self.browser.execute_script('arguments[0].scrollIntoView()', followersButton)
        time.sleep(2)
        scroll_box = self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        time.sleep(2)
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(1)
            ht = self.browser.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        sayac=0
        with open("followers.txt", "a", encoding="UTF-8") as file:
            for follower in names:
                sayac+=1
                file.write(str(sayac)+"- "+follower+"\n")
        return names
    def Logout(self):
        X=self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]')
        X.click()
        time.sleep(3)
        myaccount = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]')
        myaccount.click()
        time.sleep(3)
        exit=self.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/div')
        exit.click()
        time.sleep(3)