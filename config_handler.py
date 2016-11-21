import configparser
import os
import sys

class ConfigHandler():

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config_path = 'config.ini'

        if not os.path.isfile('config.ini'):
            self.create_default_config()
        else:
            self.config.read('config.ini')

    def create_default_config(self):
        self.config['DEFAULT'] = {'PhoneIp':    '127.0.0.1',
                                  'UserName':   'Nick'}
        self.config['user'] = {}

        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)

    def get_config(self):
        return self.config['user']

    def save_config(self):
        with open(self.config_path, 'w') as configfile:
            self.config.write(configfile)

    def reset_config(self):
        for key in self.config['user']:
            try:
                self.config['user'].pop(key, None)
            except KeyError:
                pass
        self.save_config()

    def menu(self):
        print('Choose setting to change')
        print('\nConfig menu:')
        print('1) Phone IP: {}\n2) Username: {}\n'
              '3) Reset to default\n4) Exit'
              .format(self.config['user']['PhoneIP'],
                      self.config['user']['UserName']))

        u_input = input('Menu: ')
        if u_input == '1':
            self.config['user']['PhoneIp'] = input('Phone IP: ')
            self.save_config()
            sys.exit('Config saved.')
        elif u_input == '2':
            self.config['user']['UserName'] = input('User name: ')
            self.save_config()
            sys.exit('Config saved.')
        elif u_input == '3':
            self.reset_config()
            self.save_config()
            sys.exit('Config saved.')
        elif u_input == '4':
            self.save_config()
            sys.exit('Config saved.')
        else:
            print('Invalid input')
