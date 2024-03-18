# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 09:01:20 2020
@author: Suraj
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from loggerpackage import getlogger
from passwordpackage import passwordsecurity
import config_file
import time,os
import mbss_main_flow


logger = getlogger.getLogger('')
config = config_file.get_config()
encr_aes = passwordsecurity.Passwordsecurity()
password = encr_aes.decrypt(config.get('urls', 'password'))
password_1 = encr_aes.decrypt(config.get('urls', 'password_1'))
user_id = config.get('urls', 'user_id')

screenshot_dir = os.getcwd() + '\\input_data\\' #'C:\All_important_files\Kyndryl Use Cases\MBSS_Automation\input_data'

'''
-------------------------------------------------------------
To load the driver and also ignore unnecessary popup windows
-------------------------------------------------------------
'''
def load_browser(url):
    """Loading Browser"""
    options = Options()
    #options.add_argument("--headless")
    options.add_argument('--disable-infobars')
    options.add_argument("--start-fullscreen")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-running-insecure-content")
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option(
        'prefs', {
            'credentials_enable_service': False,
            'profile': {
                'password_manager_enabled': False
            }
        }
    )
    driver = webdriver.Chrome(options=options)
    return driver

'''
----------------------------------------------------------------------------------
In this the main function in which calling all the functions from imported modules
----------------------------------------------------------------------------------
'''
def main_bot():
    
    #while True:
    try:
        url = config.get('urls','mbss_url_1st')
        driver = load_browser(url)
        driver.get(url)
        time.sleep(2)
        #driver.maximize_window()
        '''
        ------------------------------
        To login mbss portal
        ------------------------------
        '''
        
        mbss_main_flow.login_flow(driver, logger, user_id, password)
        logger.info("ssl_login_flow is successfully completed")
        print('ssl_login_flow flow completed successfully')
        
        '''
        ------------------------------------------------------
        To execute main flow of setting_details 
        ------------------------------------------------------
        '''
        mbss_main_flow.setting_details(driver, logger, screenshot_dir)
        logger.info("mbss_main_flow is successfully completed")
        print("mbss_main_flow is successfully completed")

        '''
        ------------------------------------------------------
        To execute main flow of scan_details 
        ------------------------------------------------------
        '''
        mbss_main_flow.scan_details(driver, logger, screenshot_dir)
        logger.info("mbss_main_flow is successfully completed")
        print("mbss_main_flow is successfully completed")
        
        '''
        ------------------
        To quit the driver
        ------------------
        '''
        driver.quit()
        time.sleep(1)
        #break
    except Exception as error:
        print(error)
       
            
def main_bot_2():
   
    #while True:
    try:
        url = config.get('urls','mbss_url_2nd')
        driver = load_browser(url)
        driver.get(url)
        time.sleep(2)
        #driver.maximize_window()
        '''
        ------------------------------
        To login mbss portal
        ------------------------------
        '''
        
        mbss_main_flow.login_flow_2(driver, logger, user_id, password_1)
        logger.info("ssl_login_flow is successfully completed")
        print('ssl_login_flow flow completed successfully')
        
        '''
        ------------------------------------------------------
        To execute main flow of setting_details 
        ------------------------------------------------------
        '''
        mbss_main_flow.setting_details_2(driver, logger, screenshot_dir)
        logger.info("mbss_main_flow is successfully completed")
        print("mbss_main_flow is successfully completed")
        
        '''
        ------------------
        To quit the driver
        ------------------
        '''
       
        driver.quit()
        time.sleep(1)
        #break
    except Exception as error:
        print(error)
            
            
def main_bot_3():
    
    #while True:
    try:
        url = config.get('urls','mbss_url_3rd')
        driver = load_browser(url)
        driver.get(url)
        time.sleep(2)
        #driver.maximize_window()
        '''
        ------------------------------
        To chrome login 
        ------------------------------
        '''
        
        mbss_main_flow.browser_datetime(driver, logger, screenshot_dir)
        logger.info("ssl_login_flow is successfully completed")
        print('ssl_login_flow flow completed successfully')
        
        '''
        ------------------
        To quit the driver
        ------------------
        '''
        
        driver.quit()
        time.sleep(1)
        #break
    except Exception as error:
        print(error)
        
'''
--------------------------------------------
Main method in python to call the functions.
--------------------------------------------
'''    
if __name__ == "__main__":
    """Main method"""
    try:
        # main_bot()
        # time.sleep(2)
        main_bot_2()
        time.sleep(2)
        #main_bot_3()
    except Exception as error:
        print('error is---- ', error)
    
