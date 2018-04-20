import json

import requests


def http_post():

    try:
        url = "http://127.0.0.1:8000/art/art_post/"
        d = {'key1':'value1','key2':'value2'}
        r = requests.post(url, data=d)
        return (r.status_code,r.text)
    except Exception as e:
        print(e)

def http_get():
    url = 'http://127.0.0.1:8000/art/art_ed_post/'
    r = requests.get(url)
    return r



import logging


# 一般python使用日志功能(非django框架)
def loggint_init():
    app_name = "Appname" # app名
    log_file_name = "/home/sun/PycharmProjects/artproject/myapp_test.log" # 日志文件名
    logger = logging.getLogger(app_name) # app名打印
    format_str = "[%(asctime)s][%(levelname)s] > %(message)s" # 日志消息格式
    formatter = logging.Formatter(format_str) # 格式注册
    file_handler = logging.FileHandler(log_file_name) # 日志文件注册
    file_handler.setFormatter(formatter) # 文件格式设置
    logger.addHandler(file_handler) # 添加文件
    logger.setLevel(logging.INFO) # 设置优先级


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls,*args,**kwargs)

        return cls._instance


app_name = "appname"
log_file = "./test.log"


class SingletonLogger(Singleton):

    def __init__(self):
        super(SingletonLogger, self).__init__()
        self.logger = logging.getLogger(app_name)
        format_str = "[%(asctime)s][%(levelname)s]> %(message)s"
        formatter = logging.Formatter(format_str)
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.INFO)

    def debug(self, data):
        self.logger.debug(data)

    def info(self, data):
        self.logger.info(data)

    def warning(self, data):
        self.logger.warning(data)

    def error(self, data):
        self.logger.error(data)


def test_log():
   logger = SingletonLogger()
   #output the log msg
   logger.debug("this is the debug message")
   logger.info("this is the info message")
   logger.warning("this is the warning message")
   logger.error("this is the error message")

if __name__ == '__main__':
    # test_log()
    # loggint_init()




    test = http_post()
    print(test)
    # t = http_get()
    # print(json.loads(t.text))
