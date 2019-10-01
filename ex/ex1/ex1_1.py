from netmiko import ConnectHandler

username = 'pyclass'
password = '88newclass'
device_type = 'cisco_ios'


cisco3 = {
    'host': 'cisco3.lasthop.io',
    'username': username,
    'password': password,
    'device_type': device_type

}

cisco4 = {
    'host': 'cisco4.lasthop.io',
    'username': username,
    'password': password,
    'device_type': device_type,
}


for gear in (cisco3, cisco4):
    net_connect = ConnectHandler(**gear)
    output = net_connect.send_command('show version')
    filename = gear['host']

    with open(filename, 'w') as file_object:
        file_object.write(output)