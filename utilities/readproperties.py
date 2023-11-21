import configparser

configuration = configparser.RawConfigParser()
# RawConfigParser is used to read files from config.ini file.we can also write in config file through RawConfigParser.

configuration.read("D:\\OrangeHRMrevision\\Configuration\\config.ini")


# here we give a path of config file which we need to read.

class Readconfig():

    @staticmethod  # when we use this decorator self in method is not mandatory, we can call method when we call class.
    def geturl():
        url = configuration.get('common info', 'Url')
        return url

    @staticmethod
    def getusername():
        username = configuration.get('common info', 'Username')
        return username

    @staticmethod
    def getpassword():
        password = configuration.get('common info', 'Password')
        return password
