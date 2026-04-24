import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(),"Configurations", "config.ini"))

class ReadConfig:

  @staticmethod
  def getBrowser():
    return config.get("common info", "browser")
    
  @staticmethod
  def getBaseURL():
    return config.get("common info", "browser")
    
  @staticmethod
  def getUsername():
    return config.get("common info", "browser")
    
  @staticmethod
  def getPassword():  
    return config.get("common info", "browser")
    
    
    

