'''
logging study 2.py
Set program to output logs in an external log file with a certain threshold
Print a message with levels below and above that threshold
	Any differences?
Reference:
	https://docs.python.org/2/howto/logging.html
'''
import logging
logging.basicConfig(filename='Output files/alog.log', level=logging.INFO)
logging.debug("Printing a log message of debug level") # Will not print because level was set to INFO, which is above DEBUG
logging.info("Printing a log message of info level")
logging.basicConfig(level=logging.INFO)

