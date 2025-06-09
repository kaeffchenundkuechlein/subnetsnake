import ipv4utils 

class Network():
    def __init__(self, network_id, network_mask):
        self.network_id = network_id
        self.network_mask = network_mask
        self.subnets = list()
        self.available_addresses = ipv4utils.get_number_of_addresses(self.network_mask)
        self.required_addresses = int()
        self.start_of_free_address_space = network_id

    def create_subnet(self, subnet_size):
        subnet = dict()

        subnet_id = self.start_of_free_address_space
        subnet_mask  = ipv4utils.get_smallest_network(subnet_size)
        first_useable_address, last_useable_address = ipv4utils.get_useable_range(subnet_id, subnet_mask)
        broadcast_address = ipv4utils.get_broadcast_address(subnet_id, subnet_mask)
        number_of_addresses = ipv4utils.get_number_of_addresses(subnet_mask)
        number_of_useable_addresses = number_of_addresses -2

        subnet["Prefix"] = ".".join(str(octet) for octet in subnet_id) + "/" + str(subnet_mask)
        subnet["First useable address"] = ".".join(str(octet) for octet in first_useable_address)
        subnet["Last useable address"] = ".".join(str(octet) for octet in last_useable_address)
        subnet["Broadcast address"] = ".".join(str(octet) for octet in broadcast_address)
        subnet["Number of addresses"] = str(number_of_addresses)
        subnet["Number of useable addresses"] = str(number_of_useable_addresses)

        self.subnets.append(subnet)
        self.required_addresses += int(subnet["Number of addresses"])
        ipv4utils.increment_address(self.start_of_free_address_space, number_of_addresses)

    def display_subnets(self):
        header = "\nSubnet prefix            First useable address    Last useable address     "
        header += "Broadcast address        Number of addresses      Number of useable addresses"
        line = "----------------------------------------------------------------------------"
        line += "----------------------------------------------------------------------------"
        print(header)
        print(line)
        for subnet in self.subnets:
            content = f"{subnet["Prefix"]:24} {subnet["First useable address"]:24} {subnet["Last useable address"]:24} "
            content += f"{subnet["Broadcast address"]:24} {subnet["Number of addresses"]:24} {subnet["Number of useable addresses"]}"
            print(content)