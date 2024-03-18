# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 09:01:20 2020

@author: Suraj
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 09:01:20 2020

@author: AbdulShaikh
"""
'''
@author: Suraj
'''
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import logging as logger
import time
import pyperclip

import logging

# =============================================================================
# Logging Initializer
# =============================================================================
#log_path = os.path.join(os.getcwd(), 'log')
#if not os.path.exists(log_path):
#        os.mkdir(log_path)
#timestr = time.strftime("%Y%m%d-%H%M%S")
#log_file = os.path.join(log_path, 'inputhandler.log')
#
#logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)
#handler = logging.FileHandler(log_file)
#handler.setLevel(logging.INFO)
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#handler.setFormatter(formatter)
#logger.addHandler(handler)


# =============================================================================
# Function to check for errors
# ----------------------------
# if click leads to exception, checks for errors like server error, network error etc
# Also checks whether any validation or warning displays are there
# In case of warnings, closes the event display and tries again
# And if any validation error is present, raises exception with the description of validation
# =============================================================================
def check_error(driver):
    #-----------------------------------
    #xpaths for checking errors
    #-----------------------------------
    NETWORK_ERROR_XPATH = "//a[text()='Retry']"
    NETWORK_ERROR_OK_XPATH = "//a[text()='Retry']"
    SERVER_ERROR_XPATH = "//a[text()='Restart']"
#    CLIENT_ERROR_XPATH = "//div[text()='Fehler im Client']"
    SERVER_ERROR_OK_XPATH = "//a[text()='Restart']"
    EVENT_DISPLAY_XPATH = "//div[@testid = 'dw_1']/div[1]/div[1]"
    CLOSE_BUTTON_XPATH = "//div[@testid='cb_2']"
    QUIT_APPLICATION = "//div[text()='Quit application!']"
    #----------------------------------
    #check for network error
    if is_xpath_displayed(driver, NETWORK_ERROR_XPATH, 0.5):
         mouse_click(driver, NETWORK_ERROR_OK_XPATH)

    #Check for server error
    if is_xpath_displayed(driver, SERVER_ERROR_XPATH, 0.5):
         mouse_click(driver, SERVER_ERROR_OK_XPATH)
         raise Exception("Server Error")
         
    if is_xpath_displayed(driver, QUIT_APPLICATION, 0.5):
         mouse_click(driver, QUIT_APPLICATION)
         raise Exception("Application Crashed")

    #check warnings and validations
    if not is_xpath_displayed(driver, EVENT_DISPLAY_XPATH, 0.5):
        logging.info("<Check error> - No Event display detected")
        return #noevent box displayed so return
    table = driver.find_element_by_xpath(EVENT_DISPLAY_XPATH)
    for row in table.find_elements_by_tag_name('div'):
            elements = []
            elements =  row.find_elements_by_tag_name('div')
            description = ''
            if elements:
                try:
                    title = elements[5].find_element_by_tag_name('div').text
                except Exception as e:
                    continue
                try:
                    description = elements[8].find_element_by_tag_name('div').text
                    #print(description)
                except Exception as e:
                    try:
                        description = elements[7].find_element_by_tag_name('div').text
                    except Exception as e:
                        pass
                logging.info("<checkError> - %s  - %s", title, description)
                if title.strip().lower() in ["invalid input", "attention", 'info abs', 'validation', 'validation error', 'save document']:
                    #print(title, description)
                    logging.info("<checkError> - raised exception")
                    mouse_click(driver, CLOSE_BUTTON_XPATH)
                    msg = "RAP Validation : "+description 
                    raise Exception(msg)   
                
    # close the event box
    if is_xpath_displayed(driver, CLOSE_BUTTON_XPATH, 4):
        mouse_click(driver, CLOSE_BUTTON_XPATH)
        logging.info("<checkError> - Closed event display")


def send(driver, keys):
    try:
        actions = ActionChains(driver)
        time.sleep(1)
        actions.send_keys(keys).perform()
    except Exception as timout:
        try:
            actions = ActionChains(driver)
            time.sleep(1)
            actions.send_keys(keys).perform()
        except Exception as timout:
            logger.info('%s - %s', "Unable to find the Xpath in Click ",timout)

# =============================================================================
# Get the values of the attribute eg: value of a textbox,
# =============================================================================
def get_attribute(driver, xpath, attribute_name):
    try:
        controlClick = driver.find_element_by_xpath(xpath)
        return controlClick.get_attribute(attribute_name)
        # logger.info('Successfull - %s - Xpath : %s',
        #             "get_attribute".ljust(30), xpath)
    except Exception as e:
        # logger.info('Exception - %s - Xpath : %s',
        #             "getAttributess".ljust(30), xpath)
        logger.exception(e)


# =============================================================================
# Send keys without clicking
# =============================================================================
def send_key(driver, xpath, value, no_of_tries=20):
    while True:
        try:
            no_of_tries -= 1
            #element=driver.find_element_by_xpath(xpath)
            element=driver.find_element("xpath", xpath)
            element.clear()
            time.sleep(0.5)
            element.send_keys(value)
            time.sleep(0.5)
            if value.lower()==element.get_attribute('value').lower():
                # logger.info('Successfull - %s - Xpath : %s',
                #             "send_key".ljust(30), xpath)
                return

            if no_of_tries == 0:
                # logger.info('Tries Exceeded - %s - Xpath : %s',
                #             "send_key".ljust(30), xpath)
                raise Exception('Entering Value failed. Value : ' + value)

        except Exception as e:
            if no_of_tries == 0:
                # logger.info('Exception - %s - Xpath : %s',
                #             "send_key".ljust(30), xpath)
                # logger.exception(e)
                raise

# =============================================================================
# Send keys without checking
# =============================================================================
def send_key_no_check(driver, xpath, value, no_of_tries=10):
    while True:
        try:
            no_of_tries -= 1
            #element=driver.find_element_by_xpath(xpath)
            element=driver.find_element("xpath", xpath)
            element.send_keys(value)
            logger.info('Successfull - %s - Xpath : %s',
                            "send_key".ljust(30), xpath)
            return
        except Exception as e:
            if no_of_tries == 0:
                logger.info('Exception - %s - Xpath : %s',
                            "send_key".ljust(30), xpath)
                logger.exception(e)
                raise

# =============================================================================
# clear an input filed
# =============================================================================
def clear(driver, xpath):
    try:
        element=driver.find_element_by_xpath(xpath)
        element.clear()
        logger.info('Successfull - %s - Xpath : %s',
                    "clear".ljust(30), xpath)
    except Exception as e:
        logger.info('Exception - %s - Xpath : %s',
                    "clear".ljust(30), xpath)
        logger.exception(e)

def clear_all(driver, xpath):
    try:
        element=driver.find_element_by_xpath(xpath)
        element.clear()
        element.send_keys(Keys.CONTROL+"a")
        element.send_keys(Keys.DELETE)
        logger.info('Successfull - %s - Xpath : %s',
                    "clear".ljust(30), xpath)
    except Exception as e:
        logger.info('Exception - %s - Xpath : %s',
                    "clear".ljust(30), xpath)
        logger.exception(e)


# =============================================================================
# if click leads to exception, checks for errors like server error
# Also checks whether any validation or warning displays are there
# I case of warnings close the event display and tries again
# And if any validation error raises exception
# =============================================================================
def mouse_click(driver, xpath, no_of_tries=5):
    while True:
        try:

            no_of_tries -= 1
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            #element=driver.find_element_by_xpath(xpath)
            element=driver.find_element("xpath", xpath)
            element.click()

            # logger.info('Successfull - %s - Xpath : %s',
            #             "mouse_click".ljust(30), xpath)
            return

        except Exception as e:
            check_error(driver)

            if no_of_tries == 0:
                # logger.info('Exception - %s - Xpath : %s',
                #             "mouse_click".ljust(30), xpath)
                # logger.exception(e)
                raise



# =============================================================================
# Mouse click and send value to the field with given xpath
# checks whether the right value is entered in the field
# if not then the field is cleared and value is re entered
# =============================================================================
def mouse_click_send_keys(driver, xpath, value, no_of_tries=20):
    while True:
        try:
            no_of_tries -= 1
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            #element=driver.find_element_by_xpath(xpath)
            element=driver.find_element('xpath', xpath)
            element.click()
            element.clear()
            time.sleep(0.5)
            element.send_keys(value)
#            element.send_keys(Keys.CONTROL, 'a')
#            element.send_keys(Keys.DELETE)
            time.sleep(0.5)
            value = (element.get_attribute('value').lower())
            #print(value, "value")
            if value.lower()==element.get_attribute('value').lower():
                # logger.info('Successfull - %s - Xpath : %s',
                #             "mouse_click_send_keys".ljust(30), xpath)
                return

            if no_of_tries == 0:
                # logger.info('Tries Exceeded - %s - Xpath : %s',
                #             "mouse_click_send_keys".ljust(30), xpath)
                raise Exception('Entering Value failed. Value : ' + value)

        except Exception as e:
            check_error(driver)

            if no_of_tries == 0:
                # logger.info('Exception - %s - Xpath : %s', 
                #             "mouse_click_send_keys", xpath)
                # logger.exception(e)
                raise



# =============================================================================
# Enter date in the rap portal and check date is correctly entered
# Send date without any special charactors
# =============================================================================
def enter_date(driver, xpath, value, no_of_tries=10):
    while True:
        try:
            value = value.replace('/', '').replace('-', '')
            no_of_tries -= 1
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            #element=driver.find_element_by_xpath(xpath)
            element=driver.find_element("xpath", xpath)
            element.click()
            element.clear()
            time.sleep(0.5)
            element.send_keys('0')
            time.sleep(0.5)
            element.send_keys(value)

            if value==element.get_attribute('value').replace('/',''):
                # logger.info('Successfull - %s - Xpath : %s',
                #             "enter_date".ljust(30), xpath)
                return             #if the value in the field is same as the value entered return

            if no_of_tries == 0:   #if the value is not same even after specified tries raise error
                # logger.info('Tries Exceeded - %s - Xpath : %s',
                #             "enter_date".ljust(30), xpath)
                raise Exception('Entering Date failed : ' + value)

        except Exception as e:
            check_error(driver)

            if no_of_tries == 0:
                # logger.info('Exception - %s - Xpath : %s', 
                #             "enter_date".ljust(30), xpath)
                # logger.exception(e)
                raise




# =============================================================================
#  Use for entering values in fields with autocomplete
#  This function copies the required value to clipboard and pastes it in the field
# =============================================================================
def mouse_click_paste_1(driver, xpath, value, no_of_tries = 10):
    while True:
        try:
            no_of_tries -= 1
            WebDriverWait(driver, 0.5).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            #element=driver.find_element_by_xpath(xpath)
            element=driver.find_element("xpath", xpath)
            element.click()
            element.clear()
            time.sleep(0.5)
            pyperclip.copy(value)
            element.send_keys(Keys.CONTROL+"v")
            element.send_keys(Keys.ARROW_DOWN)
            element.send_keys(Keys.TAB)
            time.sleep(0.5)
            if value.lower() in element.get_attribute('value').lower():
                # logger.info('Successfull - %s - Xpath : %s',
                #             "mouse_click_paste".ljust(30), xpath)
                return  #if the value in the field is same as the value entered return

            if no_of_tries == 0:   #if the value is not same even after specified tries raise error
                # logger.info('Tries Exceeded - %s - Xpath : %s',
                #             "mouse_click_paste".ljust(30), xpath)
                raise Exception('Entering value failed. Value : ' + value)

        except Exception as e:
            check_error(driver)
            if no_of_tries == 0:
                # logger.info('Exception - %s - Xpath : %s',
                #             "mouse_click_paste".ljust(30), xpath)
                # logger.exception(e)
                raise
                
def mouse_click_paste_2(driver, xpath, value, no_of_tries = 10):
    while True:
        try:
           
            if no_of_tries == 0:   #if the value is not same even after specified tries raise error
                # logger.info('Tries Exceeded - %s - Xpath : %s',
                #             "mouse_click_paste".ljust(30), xpath)
                raise Exception('Entering value failed. Value : ' + value)

        except Exception as e:
            check_error(driver)
            if no_of_tries == 0:
                # logger.info('Exception - %s - Xpath : %s',
                #             "mouse_click_paste".ljust(30), xpath)
                # logger.exception(e)
                raise
                
def mouse_click_paste(driver, xpath, value, no_of_tries = 10):
    while True:
        try:
            no_of_tries -= 1
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            #element=driver.find_element_by_xpath(xpath)
            element=driver.find_element("xpath", xpath)
            element.click()
            element.clear()
            time.sleep(0.5)
            pyperclip.copy(value)
            element.send_keys(Keys.CONTROL+"v")
            element.send_keys(Keys.TAB)
            time.sleep(1)
            #print(element.get_attribute('value').lower(), "Value")
            if value.lower()==element.get_attribute('value').lower():
                # logger.info('Successfull - %s - Xpath : %s',
                #             "mouse_click_paste".ljust(30), xpath)
                return  #if the value in the field is same as the value entered return

            if no_of_tries == 0:   #if the value is not same even after specified tries raise error
                # logger.info('Tries Exceeded - %s - Xpath : %s',
                #             "mouse_click_paste".ljust(30), xpath)
                raise Exception('Entering value failed. Value : ' + value)

        except Exception as e:
            check_error(driver)
            if no_of_tries == 0:
                logger.info('Exception - %s - Xpath : %s',
                            "mouse_click_paste".ljust(30), xpath)
                logger.exception(e)
                raise


# =============================================================================
# send value to input field without checking
# =============================================================================
def mouse_click_send_key_no_check(driver,xpath,value, no_of_tries=10):
    while True:
        try:
            no_of_tries -= 1
            #controlClick=driver.find_element_by_xpath(xpath)
            controlClick=driver.find_element("xpath", xpath)
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            controlClick.click()
            controlClick.clear()
            time.sleep(0.5)
            controlClick.send_keys(value)
            # logger.info('Successfull - %s - Xpath : %s',
            #             "mouse_click_send_key_no_check".ljust(30), xpath)
            return
        except Exception as e:
            check_error(driver)
            if no_of_tries == 0:
                # logger.info('Exception - %s - Xpath : %s',
                #             "mouse_click_send_key_no_check".ljust(30), xpath)
                logger.exception(e)
                raise


# =============================================================================
# mouse click using action chain
# =============================================================================
def click_action_chain(driver, xpath):
    try:
        element = driver.find_element_by_xpath(xpath)
        actions = ActionChains(driver)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        actions.click(element).perform()
        logger.info('Successfull - %s - Xpath : %s',
                    "click_action_chain".ljust(30), xpath)
    except Exception as e:
        actions.click(element).perform()
        logger.info('Exception - %s - Xpath : %s',
                    "click_action_chain".ljust(30), xpath)
        logger.exception(e)

# =============================================================================
# mouse click using mouse hover
# =============================================================================
def mouse_hover(driver, xpath, no_of_tries=20):
    while True:
        try:
            no_of_tries -= 1
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element = driver.find_element_by_xpath(xpath)
            hov = ActionChains(driver).move_to_element(element)
            hov.perform()
            return
        except Exception as e:
            hov.perform()
            # logger.info('Exception - %s - Xpath : %s',
            #             "click_action_chain".ljust(30), xpath)
            # logger.exception(e)
            raise


# =============================================================================
# send keys without xpath
# Value is entered where the cursor is currently active
# =============================================================================
def send_without_xpath(driver, keys):
    try:
        actions = ActionChains(driver)
        actions.send_keys(keys).perform()
        #logger.info('Successfull - %s ', "send_without_xpath".ljust(30))
    except Exception as timout:
        print(timout)
        # logger.info('Exception - %s', "send_without_xpath".ljust(30))
        # logger.exception(timout)



# =============================================================================
# send SHIFT+TAB without xpath
# Value is entered where the cursor is currently active
# =============================================================================
def send_shift_tab(driver):
    try:
        actions = ActionChains(driver)
        actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()
        logger.info('Successfull - %s ', "send_shift_tab".ljust(30))
    except Exception as e:
        logger.info('Exception - %s ', "send_shift_tab".ljust(30))
        logger.exception(e)


#
# =============================================================================
# double click on the xpath
# =============================================================================
def double_click(driver, xpath):
    try:
        #element = driver.find_element_by_xpath(xpath)
        element=driver.find_element("xpath", xpath)
        actions = ActionChains(driver)
        actions.double_click(element).perform()
        # logger.info('Successfull - %s ',
        #             "double_click".ljust(30))
    except Exception as e:
        # logger.info('Exception - %s - Xpath : %s',
        #             "double_click".ljust(30), xpath)
        logger.exception(e)


def scroll(driver, offset):
    driver.execute_script("window.scrollBy(0,"+ str(offset)+");")


# =============================================================================
# Reads the inner text of the xpath given
# =============================================================================
def read_text(driver, xpath):
    try:
        element = driver.find_element_by_xpath(xpath)
        # logger.info('Successfull - %s - Xpath : %s - value : %s',
        #             "read_text".ljust(30), xpath, element.text)
        return element.text
    except Exception as e:
        # logger.info('Exception - %s - Xpath : %s',
        #             "read_text".ljust(30), xpath)
        logger.exception(e)


def scroll_to_element(driver, xpath):
    try:
        element = driver.find_element_by_xpath(xpath)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
    except Exception as timout:
        logger.info('%s - %s - %s', "Unable to find the Xpath in scroll to element ",xpath,timout)

'''
---------------------------------------------------------------------------
Important methods to wait until loading done
---------------------------------------------------------------------------
'''
# =============================================================================
# Waits for timeout sec for the element with the xpath to be displayed
# =============================================================================
def processing_check_wait(driver, xpath, timeout):
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        # logger.info('Successfull - %s - Xpath : %s',
        #             "processing_check_wait".ljust(30), xpath)
        return True
    except Exception as e:
        #check_error(driver)
        # logger.info('Exception   - %s - Xpath : %s',
        #             "processing_check_wait".ljust(30), xpath)
        #logger.exception(e)
        return False



# =============================================================================
# Checks whether the xpath is displayed.
# If xpath is displayed returns true.
# =============================================================================
def is_xpath_displayed(driver, xpath, timeout):
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
        #logger.info('Found       - %s - %s', "is_xpath_displayed".ljust(30), xpath)
        return True
    except Exception as e:
        #check_error(driver)
        # logger.info('Not Found   - %s - Xpath : %s',
        #             "is_xpath_displayed".ljust(30), xpath)
        return False



# =============================================================================
# clicks a button if it is clickable else return false
# =============================================================================
def is_clickable(driver, xpath, timeout):
    try:
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        element=driver.find_element_by_xpath(xpath)
        element.click()
        return True
    except Exception as e:
        #check_error(driver)
        # logger.info('Exception   - %s - Xpath : %s',
        #             "is_clickable".ljust(30), xpath)
        logger.exception(e)
        return False

def switch_iframe(driver, xpath):
    try:
        iframe = driver.find_element_by_xpath(xpath)
        #iframe=driver.find_element("xpath", xpath)
        driver.switch_to.frame(iframe)
        #logger.info('Successfull %s - %s',"Switched Iframe".ljust(30), xpath)
    except Exception as e:
        # logger.info('Exception - %s - Xpath : %s', "switch_iframe".ljust(30), xpath)
        logger.exception(e)

      
def switch_iframe_2(driver, xpath):
    try:
        iframe_locator = (By.XPATH, xpath)
        iframe_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(iframe_locator))

        # Step 2: Switch to the iframe
        driver.switch_to.frame(iframe_element)

        # Now you are inside the iframe. Perform any actions or interact with elements inside it.
        # If you need to switch back to the default content, you can use:
        #driver.switch_to.default_content()
    except Exception as e:
        # logger.info('Exception - %s - Xpath : %s', "switch_iframe".ljust(30), xpath)
        logger.exception(e)
        
def switch_iframe_3(driver, xpath):
    try:
        frame = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'container-frame')))
        driver.switch_to.frame(frame) 
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()

        # Step 2: Switch to the iframe
        #driver.switch_to.frame(iframe_element)

        # Now you are inside the iframe. Perform any actions or interact with elements inside it.
        # If you need to switch back to the default content, you can use:
        #driver.switch_to.default_content()
    except Exception as e:
        # logger.info('Exception - %s - Xpath : %s', "switch_iframe".ljust(30), xpath)
        logger.exception(e)

def keyboardarrowdown(driver,xpath):
    #driver.find_element_by_xpath(xpath).send_keys(u'\ue015') 
    driver.find_element("xpath", xpath).send_keys(u'\ue015') 

def keyboardarrowdown_2(driver,xpath):    
    #driver.find_element_by_tag_name('body').send_keys(Keys.END)
    driver.find_element("xpath", xpath).send_keys(Keys.END)

def keyboardEnter(driver):
    try:
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER).perform()
        logger.info('Successfull - %s ', "Enter".ljust(30))
    except Exception as timout:
        logger.info('Exception - %s', "Enter".ljust(30))
        logger.exception(timout)


def KeybordEnd(driver,xpath):
    driver.find_element_by_xpath(xpath).send_keys(Keys.END) 

def keybordTab(driver, xpath):
     driver.find_element_by_xpath(xpath).send_keys(Keys.TAB)
     
def press_tab(driver):
     
     actions = ActionChains(driver)
     actions.send_keys(Keys.TAB).perform()
     
def mouse_click_paste_no_check(driver, xpath, value):
        try:
            
            WebDriverWait(driver, 0.5).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element=driver.find_element_by_xpath(xpath)
            element.click()
            element.clear()
            time.sleep(0.5)
            pyperclip.copy(value)
            element.send_keys(Keys.CONTROL+"v")
            element.send_keys(Keys.ARROW_DOWN)
            element.send_keys(Keys.TAB)
            time.sleep(0.5)

        except Exception as e:
            check_error(driver)
            # logger.info('Exception - %s - Xpath : %s',
            #                 "mouse_click_paste".ljust(30), xpath)
            logger.exception(e)
            raise
                