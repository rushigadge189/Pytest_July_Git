from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_18_02_swag():
    username_tf=(By.XPATH, '//input[@placeholder="Username"]') ;
    password_tf=(By.XPATH, '//input[@placeholder="Password"]');
    login_button=(By.XPATH, '// input[ @ name = "login-button"]') ;
    ham_burger_icon=(By.XPATH, '//button[@id="react-burger-menu-btn"]') ;
    logout_link=(By.XPATH, '//a[text()="Logout"]') ;

    def __init__(self,driver):
        self.driver=driver ;

    def test_open_page(self,url):
        self.driver.get(url) ;

    def test_enter_username(self,username):
        self.driver.find_element(*Test_18_02_swag.username_tf).send_keys(username) ;

    def test_enter_password(self,password):
        self.driver.find_element(*Test_18_02_swag.password_tf).send_keys(password) ;

    def test_login_click(self):
        self.driver.find_element(*Test_18_02_swag.login_button).click() ;

    def test_burger_click(self):
        self.driver.find_element(*Test_18_02_swag.ham_burger_icon).click()  ;

    def test_logout_click(self):
        self.driver.find_element(*Test_18_02_swag.logout_link).click() ;

    def test_status(self):
        try:
            self.driver.find_element(By.XPATH, '//span[@class="title"]') ;
            return True ;
        except :
            return False ;