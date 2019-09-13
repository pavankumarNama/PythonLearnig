# read the contents of configuration files
import configparser


# TODO: Create the configuration parser
cfg_parser = configparser.ConfigParser()

# TODO: Read the configuration file
cfg_parser.read('config.cfg')

# TODO: print the sections
# print(cfg_parser.sections())
# print(cfg_parser.has_section('Section 4'))

# TODO: Access one of the default values
# print(cfg_parser['DEFAULT']['UseTimeTravel'])
# print(cfg_parser['DEFAULT'].getboolean('UseTimeTravel'))
# print(type(cfg_parser['DEFAULT']['UseTimeTravel']))
# print(bool(cfg_parser['DEFAULT']['UseTimeTravel']))

# TODO: Demonstrate the getXXX convenience functions
# opd = cfg_parser['DEFAULT'].getboolean('ObeyPrimeDirective')
# print(opd)
# speed = cfg_parser['DEFAULT'].getfloat('Ship speed')
# print(speed)
# TODO: Access a non-existent value
try:
    title = cfg_parser['Section 3']['Title']
    print(title)
except KeyError as err:
    print(err)
