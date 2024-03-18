# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 05:46:31 2020

@author: AbdulShaikh
"""

import os
import inspect
import configparser
# import logging
# from logging.handlers import RotatingFileHandler

PATH = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))

def get_config(name='config.ini'):

    CONFIGURATION = configparser.RawConfigParser()
    config_file = os.path.join(PATH, 'resources', name)
   

    r = CONFIGURATION.read(config_file)

    if not r:
        print(f"could not find the config file '{name}'")
        raise Exception (f"could not find the config file '{name}'")
    else:
        return CONFIGURATION

