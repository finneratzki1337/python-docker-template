from configparser import ConfigParser
import os
from dotenv import load_dotenv

#importing own modules
from module_template import module_class

#MY_ENV_VAR = os.getenv('MY_ENV_VAR')

#reading potential config
config = ConfigParser()
config.read("config/conf.conf")

if 'AM_I_IN_A_DOCKER_CONTAINER' not in os.environ:
    load_dotenv()
    
user_name = os.environ['USER_NAME']
password = os.environ['USER_PASSWORD']
my_setting = config['GENERAL']['MY_SETTING']


if __name__ == "__main__":
    print(f"{user_name}/{password}")
    print(my_setting)
    my_class = module_class.sample_class()
    my_class.sample_method()