class Test__Credence_002 () :
    def test_CredKart_Login_008 ( self ) :
        import time

        from selenium import webdriver;
        from selenium.webdriver.common.by import By;
        from selenium.common import NoSuchElementException;

        driver = webdriver.Chrome();
        time.sleep(1);

        driver.get('https://automation.credence.in/shop');
        time.sleep(1);

        driver.maximize_window();
        time.sleep(1)

        driver.find_element(By.LINK_TEXT, 'Login').click();
        time.sleep(1);

        driver.find_element(By.XPATH, '//input[@id="email"]').send_keys('Credencetest@test.com');
        time.sleep(1);

        driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('Credence@123');
        time.sleep(1);

        driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click();
        time.sleep(1);

        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']");
            print('Login Test Case Is Passed') ;
            assert True ;
            driver.close() ;
        except NoSuchElementException:
            print('Login Tese Case Is Failed');
            driver.close() ;
            assert False ;

    def test_Ammount_Verification (self) :
        import time

        from selenium import webdriver;
        from selenium.webdriver.common.by import By;
        from selenium.webdriver.support.select import Select

        driver = webdriver.Chrome();
        time.sleep(1);

        driver.get('https://automation.credence.in/shop');
        time.sleep(1);

        driver.maximize_window();
        time.sleep(1)

        driver.find_element(By.LINK_TEXT, 'Login').click();
        time.sleep(1);

        driver.find_element(By.XPATH, '//input[@id="email"]').send_keys('Credencetest@test.com');
        time.sleep(1);

        driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('Credence@123');
        time.sleep(1)

        driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click();
        time.sleep(1);

        driver.find_element(By.XPATH, '//html//body//div[2]//div[3]//div[1]//div[1]//a[2]//h3').click();
        time.sleep(1);

        driver.find_element(By.XPATH, '//input[@value="Add to Cart"]').click();
        time.sleep(1);

        driver.find_element(By.XPATH, '//a[@class="btn btn-primary btn-lg"]').click();
        time.sleep(1);

        driver.find_element(By.XPATH, '//a[@href="https://automation.credence.in/shop/headphones"][2]').click();
        time.sleep(1);

        driver.find_element(By.XPATH, '//input[@value="Add to Cart"]').click();
        time.sleep(1);

        driver.find_element(By.XPATH, '//a[@class="btn btn-primary btn-lg"]').click();
        time.sleep(1);

        driver.find_element(By.XPATH, '//a[@href="https://automation.credence.in/shop/ipad-retina"][2]').click();
        time.sleep(1);

        driver.find_element(By.XPATH, '//input[@value="Add to Cart"]').click();
        time.sleep(1);

        product_quantity1 = Select(driver.find_element(By.XPATH, '//tbody//tr[1]//td[3]/select'));
        product_quantity1.select_by_index(3)
        time.sleep(1);

        product_quantity2 = Select(driver.find_element(By.XPATH, '//tbody//tr[2]//td[3]/select'));
        product_quantity2.select_by_index(3);
        time.sleep(1);

        product_quantity3 = Select(driver.find_element(By.XPATH, '//tbody//tr[3]//td[3]/select'));
        product_quantity3.select_by_index(2);
        time.sleep(1);

        l = len(driver.find_elements(By.XPATH, '//tbody//tr/td[4]'));

        product_price_list = [];

        for r in range(1, l - 2):
            var1 = driver.find_element(By.XPATH, '//tbody//tr[' + str(r) + ']//td[4]').text;
            product_price = var1[1:];
            product_price_list.append(float(product_price));

        print(product_price_list);

        Exp_subtotal = round(sum(product_price_list), 2);
        print('Exp_subtotal = ', str(Exp_subtotal));

        System_Value = [];
        for i in range(l - 2, l + 1):
            var2 = driver.find_element(By.XPATH, '//tbody//tr[' + str(i) + ']//td[4]').text;
            var3 = var2.replace(',', '');
            system_price = var3[1:];
            system_price = float(system_price);
            System_Value.append(float(system_price));

        print('System Value = ', System_Value);

        if (Exp_subtotal == System_Value[0]):
            print('Value Is Match');
            assert True
        else:
            print('Value Is Not Match');
            assert False ;

        Bill = (Exp_subtotal * 0.13);
        Bill = round(Bill, 2);
        print('Final Ammount = ', Bill);

        print('Discount = ', System_Value[1]);

        if (Bill == System_Value[1]):
            print('Discount Is Matched');
            assert True ;
        else:
            print('Discount Value Is Unmatched') ;
            assert False ;

        driver.find_element(By.XPATH, '//a[@class="btn btn-success btn-lg"]').click();
        time.sleep(1);

        driver.find_element(By.XPATH, '//input[@name="first_name"]').send_keys('Credence');
        time.sleep(1);

        driver.find_element(By.XPATH, '//input[@name="last_name"]').send_keys('Pune');
        time.sleep(1);

        driver.find_element(By.XPATH, '//input[@id="phone"]').send_keys('1234567890');
        time.sleep(1);

        driver.find_element(By.XPATH, '//textarea[@name="address"]').send_keys('Dhankawadi');
        time.sleep(1);

        driver.find_element(By.XPATH, '//input[@name="zip"]').send_keys('411006');
        time.sleep(1);

        state = Select(driver.find_element(By.XPATH, '//select[1]'));
        state.select_by_visible_text('Pune');
        time.sleep(1);

        driver.find_element(By.XPATH, '//input[@id="owner"]').send_keys('Credence Pune Dhankawadi');
        time.sleep(1);

        driver.find_element(By.XPATH, '//input[@id="cvv"]').send_keys('043');
        time.sleep(1);

        driver.find_element(By.ID, 'cardNumber').send_keys('5281');
        driver.find_element(By.ID, 'cardNumber').send_keys('0370');
        driver.find_element(By.ID, 'cardNumber').send_keys('4891');
        driver.find_element(By.ID, 'cardNumber').send_keys('6168');
        time.sleep(1);

        year = Select(driver.find_element(By.XPATH, '//select[@name="exp_year"]'));
        year.select_by_index(3);
        time.sleep(1);

        month = Select(driver.find_element(By.XPATH, '//select[@name="exp_month"]'));
        month.select_by_value('06');
        time.sleep(1)

        driver.find_element(By.XPATH, '//button[@id="confirm-purchase"]').click();
        time.sleep(1);

        driver.close();
