# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 19:07:46 2023

@author: SurajPrasadPatel
"""
import pyppeteer
import inputhandler
import time
from datetime import datetime, timedelta

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
            
    

def your_details(driver, logger, screenshot_dir): 
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
        driver.save_screenshot(screenshot_dir + 'ss.png')
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
        click_search_xp = "//input[@data-domselect='searchInput']"
        inputhandler.processing_check_wait(driver, click_search_xp, 30)
        inputhandler.mouse_click_send_key_no_check(driver, click_search_xp, 'safe')
        time.sleep(2)
        driver.save_screenshot(screenshot_dir + 'Safe_Check.png')
        time.sleep(2)
    except Exception as error:
        # print(error)
        logger.info(f"login_flow function Error is : {str(error)}")
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
        click_search_xp = "//input[@data-domselect='searchInput']"
        inputhandler.processing_check_wait(driver, click_search_xp, 30)
        inputhandler.mouse_click_send_key_no_check(driver, click_search_xp, 'safe')
        time.sleep(2)
        driver.save_screenshot(screenshot_dir + 'Safe_Check.png')
        time.sleep(2)
    except Exception as error:
        # print(error)
        logger.info(f"login_flow function Error is : {str(error)}")
        raise error
        
    # driver.save_screenshot(screenshot_dir + 'logged_in_page.png')
    
    # driver.quit()