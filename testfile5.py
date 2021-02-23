import configparser
config = configparser.ConfigParser()
filepath = r'H:\Aero\Python\\' + 'testconfig.ini'
config2 = config
config2.read(filepath)

with open(r'H:\Aero\Python\testconfig2.ini', mode='w', encoding='utf-8') as f:
    config2.write(f)
    print('data written')