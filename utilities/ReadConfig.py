# import configparser
#
# config=configparser.RawConfigParser() ;
#
# filepath="D:\\PYTEST_JULY\\configuration\\config.ini" ;
#
# config.read(filepath) ;
#
# class Readconfig():
#     @staticmethod
#     def getUserName():
#         username=config.get('common data' ,'Username') ;
#         return username ;
#
#     @staticmethod
#     def getPasssWord():
#         password=config.get('common data', 'Password') ;
#         return password ;
# import configparser
#
# config=configparser.RawConfigParser();
# filepath="D:\\PYTEST_JULY\\configuration\\config.ini" ;
# config.read(filepath) ;
#
# class Readconfig():
#     @staticmethod
#     def getUserName():
#         username=config.get('common data', 'Username') ;
#         return username ;
#     @staticmethod
#     def getPassWord():
#         password=config.get('common data', 'Password') ;
#         return password ;
import configparser

config=configparser.RawConfigParser();

filepath="D:\PYTEST_JULY\configuration\config.ini" ;

config.read(filepath) ;

class Readconfig():
    @staticmethod
    def getUserName():
        username=config.get('common data', 'Username') ;
        return username ;

    @staticmethod
    def getPassWord():
        password=config.get('common data', 'Password') ;
        return password ;