import inspect
# use print in realtime code is not a good practice, we can use logs to track your activity.
# logs--> logs are nothing but whatever activity you perform, to track that activity.
# it tracks date,time, which class and method are used, line number, message etc. activities are tracked in logs.
# report and logs are different.
# we create logger.py file in utilities.

import logging


class LogGenerator:

    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]  # in log report replace root with class name
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("D:\\OrangeHRMrevision\\Logs\\OrangeHrmLogs.log")  # give a path of Logs folder.
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        # search logging format on Google, on python web side it will show format

        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        # in logger file we set level as logger.setLevel(logging.INFO), mean after info warning,error and critical is
        # there(standard level) so log maintain dwarning,error and critical.If we set level as error then only
        # critical take in log file.
        # below code use in test case
        # self.log.debug("debug")
        # self.log.info("info")
        # self.log.warning("warning")
        # self.log.error("error")
        # self.log.critical("critical")
        return logger

# get log --> logging.getLogger()
# log file --> path and name
# format --> define logs format
# setformatter --> link file and format
# add handler --> maintain log file

# create this log file is one time activity, you can use this log in multiple projects
# when we create html reports that log also shown in that html reports
