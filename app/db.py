import configparser

config = configparser.ConfigParser()
config.read('config.ini')

username = config['mysql']['username']
password = config['mysql']['password']

print(username, password)

