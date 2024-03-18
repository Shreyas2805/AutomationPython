# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 12:25:02 2020

@author: Suraj
"""
import inputhandler
import time
from datetime import datetime, timedelta

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y_%m_%d-%H_%M_%S")
#print("Current date and time:", formatted_datetime)

day_1 = datetime.now() + timedelta(days=1)
day_1 = day_1.strftime('%m-%d-%Y')   

def login_flow(driver, logger, user_id, password):
    """login part"""
   
    user_name_xp = "//input[@class='required login-username']"
    if inputhandler.is_xpath_displayed(driver, user_name_xp, 5):
        try:
            inputhandler.processing_check_wait(driver, user_name_xp, 30)
            inputhandler.mouse_click_send_key_no_check(driver, user_name_xp, user_id)
            time.sleep(1)
        except Exception as error:
            # print(error)
            logger.info(f"login_flow function Error is : {str(error)}")
            raise error
            
    password_xp = "//input[@class='required login-password']"
    if inputhandler.is_xpath_displayed(driver, password_xp, 5):
        try:
            inputhandler.processing_check_wait(driver, password_xp, 30)
            inputhandler.mouse_click_send_key_no_check(driver, password_xp, password)
            time.sleep(1)
        except Exception as error:
            # print(error)
            logger.info(f"login_flow function Error is : {str(error)}")
            raise error
            
            
    signin_xp = "//button[text()='Sign In']"
    if inputhandler.is_xpath_displayed(driver, signin_xp, 5):
        try:
            inputhandler.processing_check_wait(driver, signin_xp, 30)
            inputhandler.mouse_click(driver, signin_xp)
            time.sleep(1)
        except Exception as error:
            # print(error)
            logger.info(f"login_flow function Error is : {str(error)}")
            raise error
     
    time.sleep(2)
    continue_xp = "//a[text()='Continue']"
    if inputhandler.is_xpath_displayed(driver, continue_xp, 5):
        try:
            inputhandler.processing_check_wait(driver, continue_xp, 30)
            inputhandler.mouse_click(driver, continue_xp)
            time.sleep(1)
        except Exception as error:
            # print(error)
            logger.info(f"login_flow function Error is : {str(error)}")
            raise error

def setting_details(driver, logger, screenshot_dir): 
    """function"""
    try:
        click_setting_xp = "//a[@class='topnav-menu']"
        inputhandler.processing_check_wait(driver, click_setting_xp, 30)
        inputhandler.mouse_click(driver, click_setting_xp)
        time.sleep(1)
    except Exception as error:
        # print(error)
        logger.info(f"your_details function Error is : {str(error)}")
        raise error
        
    try:
        clk_pas_mgmt_xp = "//span[text()='Password Mgmt']"
        inputhandler.processing_check_wait(driver, clk_pas_mgmt_xp, 30)
        inputhandler.mouse_click(driver, clk_pas_mgmt_xp)
        time.sleep(2)
        driver.save_screenshot(screenshot_dir + f'SS_{formatted_datetime}.jpg') #
        time.sleep(2)
    except Exception as error:
        # print(error)
        logger.info(f"your_details function Error is : {str(error)}")
        raise error
        
        
    try:
        click_advance_xp = "//span[text()='Advanced']"
        inputhandler.processing_check_wait(driver, click_advance_xp, 30)
        inputhandler.mouse_click(driver, click_advance_xp)
        time.sleep(1)
    except Exception as error:
        # print(error)
        logger.info(f"your_details function Error is : {str(error)}")
        raise error
           
    try:
        click_safe_xp = "//input[@data-domselect='searchInput']"
        inputhandler.processing_check_wait(driver, click_safe_xp, 30)
        inputhandler.mouse_click_send_key_no_check(driver, click_safe_xp, 'safe')
        time.sleep(2)
        driver.save_screenshot(screenshot_dir + f'Safe_Check_{formatted_datetime}.jpg')
        time.sleep(2)
    except Exception as error:
        # print(error)
        logger.info(f"login_flow function Error is : {str(error)}")
        raise error
         
    try:
        click_user_xp = "//input[@data-domselect='searchInput']"
        inputhandler.processing_check_wait(driver, click_user_xp, 30)
        inputhandler.mouse_click_send_key_no_check(driver, click_user_xp, 'user')
        time.sleep(2)
        driver.save_screenshot(screenshot_dir + f'user_{formatted_datetime}.jpg')
        time.sleep(2)
    except Exception as error:
        # print(error)
        logger.info(f"login_flow function Error is : {str(error)}")
        raise error
          
    try:
        click_tls_xp = "//input[@data-domselect='searchInput']"
        inputhandler.processing_check_wait(driver, click_tls_xp, 30)
        inputhandler.mouse_click_send_key_no_check(driver, click_tls_xp, 'tls')
        time.sleep(2)
        driver.save_screenshot(screenshot_dir + f'tls_{formatted_datetime}.jpg')
        time.sleep(2)
    except Exception as error:
        # print(error)
        logger.info(f"login_flow function Error is : {str(error)}")
        raise error


    try:
        click_cipher_xp = "//input[@data-domselect='searchInput']"
        inputhandler.processing_check_wait(driver, click_cipher_xp, 30)
        inputhandler.mouse_click_send_key_no_check(driver, click_cipher_xp, 'cipher')
        time.sleep(2)
        driver.save_screenshot(screenshot_dir + f'cipher_{formatted_datetime}.jpg')
        time.sleep(2)
    except Exception as error:
        # print(error)
        logger.info(f"login_flow function Error is : {str(error)}")
        raise error


    try:
        click_webserver_xp = "//input[@data-domselect='searchInput']"
        inputhandler.processing_check_wait(driver, click_webserver_xp, 30)
        inputhandler.mouse_click_send_key_no_check(driver, click_webserver_xp, 'webserver')
        time.sleep(2)
        driver.save_screenshot(screenshot_dir + f'webserver_{formatted_datetime}.jpg')
        time.sleep(2)
    except Exception as error:
        # print(error)
        logger.info(f"login_flow function Error is : {str(error)}")
        raise error
        
    try:
        click_post_xp = "//input[@data-domselect='searchInput']"
        inputhandler.processing_check_wait(driver, click_post_xp, 30)
        inputhandler.mouse_click_send_key_no_check(driver, click_post_xp, 'post')
        time.sleep(2)
        driver.save_screenshot(screenshot_dir + f'post_size_{formatted_datetime}.jpg')
        time.sleep(2)
    except Exception as error:
        # print(error)
        logger.info(f"login_flow function Error is : {str(error)}")
        raise error

def scan_details(driver, logger, screenshot_dir):
    
    try:
        click_scan_xp = "//a[@class='topnav-menu']"
        inputhandler.processing_check_wait(driver, click_scan_xp, 30)
        inputhandler.mouse_click(driver, click_scan_xp)
        time.sleep(1)
    except Exception as error:
        # print(error)
        logger.info(f"your_details function Error is : {str(error)}")
        raise error
      
    try:
        click_Policies_xp = "//span[text()='Policies']"
        inputhandler.processing_check_wait(driver, click_Policies_xp, 30)
        inputhandler.mouse_click(driver, click_Policies_xp)
        time.sleep(1)
    except Exception as error:
        # print(error)
        logger.info(f"your_details function Error is : {str(error)}")
        raise error
        
    try:
        click_Advanced_scan_xp = "//td[@data-search='Advanced Scan']"
        inputhandler.processing_check_wait(driver, click_Advanced_scan_xp, 30)
        inputhandler.mouse_click(driver, click_Advanced_scan_xp)
        time.sleep(1)
    except Exception as error:
        # print(error)
        logger.info(f"your_details function Error is : {str(error)}")
        raise error
        
        
    try:
       click_Discovery_xp = "//span[text()='Discovery ']"
       inputhandler.processing_check_wait(driver, click_Discovery_xp, 30)
       inputhandler.mouse_click(driver, click_Discovery_xp)
       time.sleep(1)
    except Exception as error:
       # print(error)
       logger.info(f"your_details function Error is : {str(error)}")
       raise error
     

    try:
       click_Port_Scanning_xp = "//li[text()=' Port Scanning']"
       inputhandler.processing_check_wait(driver, click_Port_Scanning_xp, 30)
       inputhandler.mouse_click(driver, click_Port_Scanning_xp)
       
       time.sleep(2)
       driver.save_screenshot(screenshot_dir + f'port_scan_{formatted_datetime}.jpg')
       time.sleep(2)
      
       # inputhandler.keyboardarrowdown_2(driver, click_Port_Scanning_xp)
      
       # time.sleep(2)
       # driver.save_screenshot(screenshot_dir + f'port_scan2_{formatted_datetime}.jpg')
       # time.sleep(2)
    except Exception as error:
       # print(error)
       logger.info(f"your_details function Error is : {str(error)}")
       raise error      
    
    try:
        click_Service_Discovery_xp = "//li[text()=' Service Discovery']"
        inputhandler.processing_check_wait(driver, click_Service_Discovery_xp, 30)
        inputhandler.mouse_click(driver, click_Service_Discovery_xp)
        time.sleep(2)
        driver.save_screenshot(screenshot_dir + f'Service_Disc_{formatted_datetime}.jpg')
        time.sleep(2)
        
        #driver.close()
    except Exception as error:
        # print(error)
        logger.info(f"login_flow function Error is : {str(error)}")
        raise error
        
    try:
        click_advnc_xp = "//span[text()='Advanced ']"
        inputhandler.processing_check_wait(driver, click_advnc_xp, 30)
        inputhandler.mouse_click(driver, click_advnc_xp)
        time.sleep(2)
        driver.save_screenshot(screenshot_dir + f'tcp_udp_{formatted_datetime}.jpg')
        
        time.sleep(2)
       
        # inputhandler.keyboardarrowdown_2(driver, click_advnc_xp)
        # time.sleep(1)
        # driver.save_screenshot(screenshot_dir + f'tcp_udp2_{formatted_datetime}.jpg')
       
        # time.sleep(2)
        
        driver.close()
    except Exception as error:
        # print(error)
        logger.info(f"login_flow function Error is : {str(error)}")
        raise error
                

        
def login_flow_2(driver, logger, user_id, password_1):
    """login part"""
    
    Reuse_my_xp = "//label[text()='Reuse my password for privileged tasks']"
    if inputhandler.is_xpath_displayed(driver, Reuse_my_xp, 5):
        try:
            inputhandler.processing_check_wait(driver, Reuse_my_xp, 30)
            inputhandler.mouse_click(driver, Reuse_my_xp)
            time.sleep(1)
        except Exception as error:
            # print(error)
            logger.info(f"login_flow function Error is : {str(error)}")
            raise error                        
    
   
    user_name_xp = "//input[@id='login-user-input']"
    if inputhandler.is_xpath_displayed(driver, user_name_xp, 5):
        try:
            inputhandler.processing_check_wait(driver, user_name_xp, 30)
            inputhandler.mouse_click_send_key_no_check(driver, user_name_xp, user_id)
            time.sleep(1)
        except Exception as error:
            # print(error)
            logger.info(f"login_flow function Error is : {str(error)}")
            raise error
            
    password_xp = "//input[@id='login-password-input']"
    if inputhandler.is_xpath_displayed(driver, password_xp, 5):
        try:
            inputhandler.processing_check_wait(driver, password_xp, 30)
            inputhandler.mouse_click_send_key_no_check(driver, password_xp, password_1)
            time.sleep(1)
        except Exception as error:
            # print(error)
            logger.info(f"login_flow function Error is : {str(error)}")
            raise error
            
            
    signin_xp = "//span[text()='Log In']"
    if inputhandler.is_xpath_displayed(driver, signin_xp, 5):
        try:
            inputhandler.processing_check_wait(driver, signin_xp, 30)
            inputhandler.mouse_click(driver, signin_xp)
            time.sleep(1)
        except Exception as error:
            # print(error)
            logger.info(f"login_flow function Error is : {str(error)}")
            raise error
     
    time.sleep(2)
    continue_xp = "//a[text()='Continue']"
    if inputhandler.is_xpath_displayed(driver, continue_xp, 5):
        try:
            inputhandler.processing_check_wait(driver, continue_xp, 30)
            inputhandler.mouse_click(driver, continue_xp)
            time.sleep(1)
        except Exception as error:
            # print(error)
            logger.info(f"login_flow function Error is : {str(error)}")
            raise error

def setting_details_2(driver, logger, screenshot_dir): 
    """function"""
    try:
        click_setting_xp = "//span[text()='System Log']"
        inputhandler.processing_check_wait(driver, click_setting_xp, 30)
        inputhandler.mouse_click(driver, click_setting_xp)
        time.sleep(5)
        driver.save_screenshot(screenshot_dir + f'Audit_Logs_{formatted_datetime}.jpg') #
        time.sleep(2)
    except Exception as error:
        # print(error)
        logger.info(f"your_details function Error is : {str(error)}")
        raise error
        
    try:
        clk_pas_mgmt_xp = "//span[text()='Update Management']"
        inputhandler.processing_check_wait(driver, clk_pas_mgmt_xp, 30)
        inputhandler.mouse_click(driver, clk_pas_mgmt_xp)
        time.sleep(5)
        driver.save_screenshot(screenshot_dir + f'Automatic_Updates_{formatted_datetime}.jpg') #
        time.sleep(2)
    except Exception as error:
        # print(error)
        logger.info(f"your_details function Error is : {str(error)}")
        raise error
        
        
    try:
        click_advance_xp = "//span[text()='System']"
        inputhandler.processing_check_wait(driver, click_advance_xp, 10)
        inputhandler.mouse_click(driver, click_advance_xp)
        time.sleep(1)
    except Exception as error:
        # print(error)
        logger.info(f"your_details function Error is : {str(error)}")
        raise error
           
    try:
        #click_ntp_xp = "//a[@id='system_information_systime_button']"
        click_ntp_xp = "//span[@id='systime-tooltip']"
        #inputhandler.switch_iframe(driver, click_search_xp)
        #inputhandler.switch_iframe_2(driver, click_search_xp)
        print('a')
        inputhandler.switch_iframe_3(driver, click_ntp_xp)
        print('b')
        inputhandler.processing_check_wait(driver, click_ntp_xp, 5)
        print('c')
        inputhandler.double_click(driver, click_ntp_xp)
        time.sleep(5)
        # inputhandler.mouse_click(driver, click_ntp_xp,5)
        # time.sleep(5)
        print('d')
        driver.save_screenshot(screenshot_dir + f'NTP_{formatted_datetime}.jpg')
        time.sleep(2)
        print('e')
        #driver.switch_to.default_content()
        driver.close()
        print('f')
    except Exception as error:
        # print(error)
        logger.info(f"login_flow function Error is : {str(error)}")
        raise error
         
                   
                        
def browser_datetime(driver, logger, screenshot_dir): 
    """function"""
    
    textarea_xp = "//textarea[@id='APjFqb']"
    if inputhandler.is_xpath_displayed(driver, textarea_xp, 5):
        try:
            inputhandler.processing_check_wait(driver, textarea_xp, 30)
            inputhandler.mouse_click_send_key_no_check(driver, textarea_xp, 'what is time and date')
            time.sleep(1)
        except Exception as error:
            # print(error)
            logger.info(f"login_flow function Error is : {str(error)}")
            raise error
    
    click_setting_xp = "(//input[@class='gNO89b'])[last()-1]"
    if inputhandler.is_xpath_displayed(driver, click_setting_xp, 5):
        try:  
            inputhandler.processing_check_wait(driver, click_setting_xp, 30)
            inputhandler.mouse_click(driver, click_setting_xp)
            
            time.sleep(2)
            driver.save_screenshot(screenshot_dir + f'Google_Datetime_{formatted_datetime}.jpg')
            time.sleep(2)
            driver.close()
        except Exception as error:
            # print(error)
            logger.info(f"your_details function Error is : {str(error)}")
            raise error
        
  