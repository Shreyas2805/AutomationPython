from passwordpackage import passwordsecurity
import config_file
config = config_file.get_config()
encr_aes = passwordsecurity.Passwordsecurity()
'''
-------------------------------------
To get the password in encrypted form
-------------------------------------
'''
passwd = 'Scanner1@vil2019'#input('Please inter your original password--->')
try:
    en_password = encr_aes.encrypt(passwd)
    #password = encr_aes.decrypt(config.get('urls', 'password'))
    print('Your encrypted password is--->', en_password)
except Exception as error:
    print("Wrong password attempted, Error is-->" + error)
    
    
 