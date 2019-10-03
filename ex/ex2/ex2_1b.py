from netmiko import ConnectHandler

CISCO4 = {
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': '88newclass',
    'device_type': 'cisco_ios',
    'session_log': 'output.text'
}

net_connect = ConnectHandler(**CISCO4)

net_connect.send_command('ping',expect_string=r'ip')
net_connect.send_command('IP',expect_string=r'address')
net_connect.send_command('8.8.8.8',expect_string=r'5')
net_connect.send_command('5',expect_string=r'100')
net_connect.send_command('100',expect_string=r'2')
net_connect.send_command('2',expect_string=r'n')
net_connect.send_command('n',expect_string=r'n')
print(net_connect.send_command('n',expect_string=r'#'))

