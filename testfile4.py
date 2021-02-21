import configparser
config = configparser.ConfigParser()
config['heading'] = {'type': 'taco'}
config['heading']['tuple'] = '(223, 1230)'
filepath = r'H:\Aero\Python\\' + 'testconfig.ini'
with open(filepath, mode='w', encoding='utf-8') as cf:
    config.write(cf)

config.read(filepath)
print(config.sections())