from netmiko import ConnectHandler
# username = input('Vvedite vawego polzovatela \n')
# password = input('Vvedite vaw parol \n')
class Router:
    def __init__(self, ip):
        self.ip = ip
        # print(self.ipler)
        self.device = {
            'device_type': 'cisco_ios',
            'host': self.ip,
            'username': 'admmirkamran.zeynalo',
            'password': 'DnrHsderti45!',
            'port': 2579
        }
        self.netconnection = ConnectHandler(**self.device)

    def get_os_version(self):
        self.os_version = self.netconnection.send_command('show version ')
        return self.os_version.split('\n')[0]

    #Config dynamic routing if neccesary
    def dynamic_routing(self):
        self.routing = self.netconnection.send_command('show run | sec router')
        if self.routing == (''):
            print('Dynamic routing havent been configured ')

        else :
            return self.routing


    def error_cause(self):

        self.errors = self.netconnection.send_command('sh interfaces status err-disabled')

        if self.errors == (''):
            return f'No Err-disabled interfaces have been found on {self.ip}'
        else:
            return self.errors

# class Routers:
#     def __init__(self, *ips):
#         self.devices = [Router(ip) for ip in ips]
#
#     def get_versions(self):
#
#         for d in self.devices:
#
#         return test
#
#
#     def dynamic_routing(self):
#         for d in self.devices:
#             d.dynamic_routing()
#
#     def error_cause(self):
#         for d in self.devices :
#              d.error_cause()





