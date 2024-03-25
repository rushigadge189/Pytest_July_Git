# import inspect
# import logging
# class LogGenerator():
#     @staticmethod
#     def loggen():
#         name=inspect.stack()[1][3] ;
#         logger=logging.getLogger(name) ;
#         log_file=logging.FileHandler("D:\\PYTEST_JULY\\logs\\parabank.log") ;
#         log_format=logging.Formatter(" %(levelname)s : %(name)s : %(funcName)s : %(lineno)d : %(message)s ") ;
#         log_file.setFormatter(log_format) ;
#         logger.addHandler(log_file) ;
#         logger.setLevel(logging.INFO) ;
#         return logger ;
# import inspect
# import logging
#
#
# class LogGenerator() :
#     @staticmethod
#     def loggen():
#         name=inspect.stack()[1][3];
#         logger=logging.getLogger(name) ;
#         log_file=logging.FileHandler("D:\\PYTEST_JULY\\logs\\swaglabs.log") ;
#         log_format=logging.Formatter("%(levelname)s : %(name)s : %(funcName)s : %(lineno)d : %(message)s") ;
#         log_file.setFormatter(log_format) ;
#         logger.addHandler(log_file) ;
#         logger.setLevel(logging.INFO) ;
#         return logger ;

import inspect
import logging
class LogGenerator() :
    @staticmethod
    def loggen():
        name=inspect.stack()[1][3];
        logger=logging.getLogger(name) ;
        log_file=logging.FileHandler("D:\\PYTEST_JULY\\logs\\heroku.log") ;
        log_format=logging.Formatter("%(levelname)s : %(name)s : %(funcName)s : %(lineno)d : %(message)s") ;
        log_file.setFormatter(log_format) ;
        logger.addHandler(log_file) ;
        logger.setLevel(logging.INFO) ;
        return logger ;

