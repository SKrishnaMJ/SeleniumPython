import logging

def test_loggingDemo():

# creating a logger object, __name__ automativally takes the current file/testcase.py name
    logger = logging.getLogger(__name__)

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
    logger.debug("This is just a debug")
    logger.info("This is just for information")
    logger.warning("Just a warning")
    logger.error("This is the error")
    logger.critical("This is critical")