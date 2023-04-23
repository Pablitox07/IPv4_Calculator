class Ip_class:
    def __init__(self, ip_address, network_mask):
        self.ip_address = ip_address.split(".")
        self.network_mask = network_mask.split(".")

        if self.verify_ip(self.ip_address, self.network_mask):
            self.ip_address_binary = self.get_binary(self.ip_address)
            self.network_mask_binary = self.get_binary(self.network_mask)
            self.number_of_usable_ips = self.get_usable_ips(self.network_mask_binary)
            self.network_address = self.get_address_and_broadcast(network_mask = self.network_mask_binary, ip = self.ip_address_binary, key='a')
            self.broadcast_address = self.get_address_and_broadcast(network_mask = self.network_mask_binary, ip = self.ip_address_binary, key='b')
            self.first_usable_ip = self.get_first_and_last(ip = self.network_address, network = self.network_mask_binary, key = 'f')
            self.last_usable_ip = self.get_first_and_last(ip = self.broadcast_address, network = self.network_mask_binary, key = 'l')
            self.get_results()

    def verify_ip(self, ip_list, network):
        for each_octet in ip_list:
            try:
                for each_octet in range(len(ip_list)):
                    if int(ip_list[each_octet]) > 255 or int(ip_list[each_octet]) <= -1 or int(network[each_octet]) > 255 or int(network[each_octet]) <= -1:
                        print("Problem ragarding IP address or networks mask range")
                        return False
            except ValueError:
                print("Error regarding IP address")
                return False
        return True

    def get_binary(self, item):
        ip_binary_list = []
        for each_octet in item:
            binary_num = bin(int(each_octet))[2:]
            if len(binary_num) < 8:
                difference = 8 - len(binary_num)
                new_str = "0"
                new_str = new_str * difference + binary_num
                ip_binary_list.append(new_str)
        
            elif len(binary_num) == 8:
                ip_binary_list.append(binary_num)
        
            else:
                print("error")
        return ip_binary_list

    def get_usable_ips (self, network_mask):
        newtwork_without_points = "".join(network_mask)
        first_0 = newtwork_without_points.find("0")
        return (pow(2, 32 - first_0) - 2)

    def get_address_and_broadcast(self, network_mask, ip, key):
        result = []
        for each_octet in range(4):
            new_octet = ""
            for bit in range(len(network_mask[each_octet])):
                if network_mask[each_octet][bit] == "0":
                    if key == 'a':
                        new_octet += "0"
                    elif key == 'b':
                        new_octet += "1"
                else:
                    new_octet += ip[each_octet][bit]
            result.append(str(int(new_octet, 2)))
            
        return ".".join(result)
    
    def get_first_and_last(self, ip, network, key):
        ip = ip.split(".")
        if key == 'f':
            index_first_0 = 0
            for octet in range(len(network)):
                if '0' in network[octet]:
                    index_first_0 = octet
            ip[index_first_0] = str(int(ip[index_first_0]) + 1)
            return '.'.join(ip)
        elif key == 'l':
            ip[3] = str(int(ip[3]) -1)
            return '.'.join(ip)

    def get_results(self):
        print(f"Network Address: {self.network_address}")
        print(f"Broadcast Address: {self.broadcast_address}") 
        print(f"First Usable IP: {self.first_usable_ip}")
        print(f"Last Usable IP: {self.last_usable_ip}")
        print(f"Number of usable IPs: {self.number_of_usable_ips} ")
        print(f"IP Address binary: {'.'.join(self.ip_address_binary)}")
        print(f"Network mask binary: {'.'.join(self.network_mask_binary)}")

ip = str(input("IP Address: "))
net = str(input("Network Mask: "))
ip = Ip_class(ip_address=ip, network_mask=net)