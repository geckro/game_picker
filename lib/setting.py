def log():
    from logging import basicConfig,DEBUG,Formatter
    FORMAT = ' %(name)s :: %(levelname)-8s :: %(message)s'
    basicConfig(filename='./log.log', format=FORMAT, encoding='utf-8', level=DEBUG)