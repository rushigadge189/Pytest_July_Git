from selenium.webdriver.common.by import By


class Test_18_login_pages():
    username_tf=(By.XPATH, '//input[@name="username"]') ;
    password_tf=(By.XPATH, '//input[@name="password"]') ;
    login_button=(By.XPATH, '//input[@value="Log In"]') ;
    logout_link=(By.XPATH, '//a[text()="Log Out"]') ;

    def __init__(self,driver):
        self.driver=driver;

    def test_enter_url(self,url):
        self.driver.get(url) ;

    def test_enter_username(self,username):
        self.driver.find_element(*Test_18_login_pages.username_tf).send_keys(username) ;

    def test_enter_password(self,password):
        self.driver.find_element(*Test_18_login_pages.password_tf).send_keys(password) ;

    def test_click_login(self) :
        self.driver.find_element(*Test_18_login_pages.login_button).click() ;

    def test_click_logout(self):
        self.driver.find_element(*Test_18_login_pages.logout_link).click();

    def test_login_status(self):
        if(self.driver.title=='ParaBank | Accounts Overview') :
            return True ;
        else:
            return False ;
