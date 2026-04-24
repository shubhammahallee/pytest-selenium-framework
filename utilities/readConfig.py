import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(),"Configurations", "config.ini"))

