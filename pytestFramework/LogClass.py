import inspect
import logging


class LogClass:
    def getLogger(self):

        # This takes the name of the test case dynamically at run for that current test case that uses
        # logger object
        loggerName = inspect.stack()[1][3]
        # creating a logger object, __name__ automativally takes the current file/testcase.py name
        logger = logging.getLogger(loggerName)

        # this >Formatter() is used to define the format of the log file and the varicale should be passed
        # as part of Filehandler
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

        # fileHandler consists the path to the file ligfile.log (if not present then creates one)
        fileHandler = logging.FileHandler('logfile.log')
        # .setFormatter() is how we actually invoke the format defined previosuly
        fileHandler.setFormatter(formatter)

        # .addHandler() is what pushes all the log details of the automation script
        logger.addHandler(fileHandler)

        # we need to set level as it follows an order and everything including DEBUG and below will be
        # printed in the output
        logger.setLevel(logging.DEBUG)

        return logger