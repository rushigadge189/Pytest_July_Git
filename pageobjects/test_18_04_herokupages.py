from selenium.webdriver.common.by import By


class Test_18_herkoku():
    username_tf=(By.XPATH, '//input[@name="username"]') ;
    password_tf=(By.XPATH, '//input[@name="password"]') ;
    login_button=(By.XPATH, '//button[@type="submit"]') ;
    get_text=(By.XPATH, '//h4[@class="subheader"]') ;
    logout_link=(By.XPATH, ' //i[text()=" Logout"]') ;

    def __init__(self,driver):
        self.driver=driver ;

    def test_enter_url(self,url):
        self.driver.get(url) ;
    def test_enter_username(self,username):
        self.driver.find_element(*Test_18_herkoku.username_tf).send_keys(username) ;

    def test_enter_password(self,password):
        self.driver.find_element(*Test_18_herkoku.password_tf).send_keys(password) ;

    def test_login_click(self):
        self.driver.find_element(*Test_18_herkoku.login_button).click() ;

    def test_print_text(self):
        self.driver.find_element(*Test_18_herkoku.get_text).text ;

    def test_status(self):
        if(self.driver.title=='The Internet') :
            return True ;
        else:
            return False ;

    def test_logout_click(self):
        self.driver.find_element(*Test_18_herkoku.logout_link).click() ;