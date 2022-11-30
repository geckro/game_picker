import json
with open('./conf/settings.json') as settings:
    data = json.load(settings)
    print(data)
    global ll
    if data["logging_level"] == 1:
        # info
        ll = 1
    elif data["logging_level"] == 2:
        # warn
        ll = 2
    elif data["logging_level"] == 3:
        # debug
        ll = 3
    elif data["logging_level"] == 0:
        # null
        ll = 0
def log():
    from logging import basicConfig,DEBUG,Formatter
    FORMAT = ' %(name)s :: %(levelname)-8s :: %(message)s'
    basicConfig(filename='./log.log', format=FORMAT, encoding='utf-8', level=DEBUG)