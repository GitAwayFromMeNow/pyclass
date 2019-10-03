from netmiko import ConnectHandler

USERNAME = 'pyclass'
PASSWORD = '88newclass'
DEVICE_TYPE = 'cisco_ios'


CISCO3 = {
    'host': 'cisco3.lasthop.io',
    'username': USERNAME,
    'password': PASSWORD,
    'device_type': DEVICE_TYPE,

}

CISCO4 = {
    'host': 'cisco4.lasthop.io',
    'username': USERNAME,
    'password': PASSWORD,
    'device_type': DEVICE_TYPE,
}


for device in (CISCO3, CISCO4):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command('show version')
    filename = device['host']

    with open(filename, 'w') as file_object:
        file_object.write(output)

    net_connect.disconnect()
