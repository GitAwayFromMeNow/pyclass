from netmiko import ConnectHandler

CISCO4 = {
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': '88newclass',
    'device_type': 'cisco_ios',

}

net_connect = ConnectHandler(**CISCO4)

net_connect.send_command_timing('ping')
net_connect.send_command_timing('IP')
net_connect.send_command_timing('8.8.8.8')
net_connect.send_command_timing('5')
net_connect.send_command_timing('100')
net_connect.send_command_timing('2')
net_connect.send_command_timing('n')
print(net_connect.send_command_timing('n'))

