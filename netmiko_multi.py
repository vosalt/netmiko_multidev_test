from getpass import getpass
from netmiko import ConnectHandler
import time

#-------------------------------------------------------------

# Define login variables
username = input('Username: ')
password = getpass()

# Open the device and command files, and set variables
with open('multiswitch_config.txt') as com:
    command_list = com.read().splitlines()

with open('multiswitch_ip_list.txt') as swi:
    switch_list = swi.read().splitlines()

#-------------------------------------------------------------

for switch in switch_list:
    print('Connecting to switch at: ' + switch + '...')
    ip_address_of_switch = switch # Define IP address variable

    # Create dictionary used by ConnectHandler
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_switch,
        'username': username,
        'password': password
    }

#-------------------------------------------------------------
# MAIN: Send commands to each switch in succession
#-------------------------------------------------------------

    net_connect = ConnectHandler(**ios_device)
    output = net_connect.send_config_set(command_list)
    print(output)

#-------------------------------------------------------------

# Complete!
time.sleep(1)
print('\n----------Complete!----------\n')
