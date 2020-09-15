import configparser
from pathlib import Path
class Configuration:

    def __init__(cls):
        cls.section = None


    @classmethod
    def initConfig(cls,section):
        cls.section=section
        cls.Config = configparser.ConfigParser()
        print(Path(__file__).parent / "./configuration/configuration.ini")
        cls.Config.read(Path(__file__).parent / "./configuration/configuration.ini")


    @classmethod
    def getProperty(cls,key):
        return cls.Config.get(cls.section,key)
