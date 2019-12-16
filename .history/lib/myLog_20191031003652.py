import logging,os

def mkdir(path):
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        os.makedirs(path) 
    else:
        # 如果目录存在则不创建，并提示目录已存在
        return False

def loggert(logger_name):
    # create logger
    logger_name = logger_name
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # create file handler
    mkdir('./log/')
    logFile = os.path.join(logger_name,'.log')
    print(logFile)
    log_path = os.path.join('./log/',logFile)
    print(log_path)
    fh = logging.FileHandler(log_path)
    fh.setLevel(logging.INFO)

    # create formatter
    fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(funcName)s %(message)s"
    datefmt = "%a %d %b %Y %H:%M:%S"
    formatter = logging.Formatter(fmt, datefmt)

    # add handler and formatter to logger
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger
