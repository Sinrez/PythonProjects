import configparser

parser = configparser.ConfigParser()

parser.read("config.cfg")

print(parser.sections())
print(parser.has_section("Section 2"))

UseTheLightSaber = bool(parser['DEFAULT']['UseTheLightSaber'])
print(UseTheLightSaber)
print(type(UseTheLightSaber))

use_the_force = parser['DEFAULT'].getboolean('UseTheForce')
print(use_the_force)
# light_saber_power = parser['DEFAULT'].getfloat('LightSaberPower')
# print(light_saber_power)

light_saber_power = parser['DEFAULT'].getint('LightSaberPower')
print(light_saber_power)

try:
    title = parser['Section 3']['Title']
    print(title)
except KeyError as err:
    print("No such thing as ", err)