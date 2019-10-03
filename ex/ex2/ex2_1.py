from netmiko import ConnectHandler

CISCO4 = {
    'host': 'cisco4.lasthop.io',
    'username': 'pyclass',
    'password': '88newclass',
    'device_type': 'cisco_ios',

}

net_connect = ConnectHandler(**CISCO4)


