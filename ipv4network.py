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

        subnet["prefix"] = ".".join(str(octet) for octet in subnet_id) + "/" + str(subnet_mask)
        subnet["first_useable_address"] = ".".join(str(octet) for octet in first_useable_address)
        subnet["last_useable_address"] = ".".join(str(octet) for octet in last_useable_address)
        subnet["broadcast_address"] = ".".join(str(octet) for octet in broadcast_address)
        subnet["number_of_addresses"] = str(number_of_addresses)
        subnet["number_of_useable_addresses"] = str(number_of_useable_addresses)

        self.subnets.append(subnet)
        self.required_addresses += int(subnet["number_of_addresses"])
        ipv4utils.increment_address(self.start_of_free_address_space, number_of_addresses)

    def display_subnets(self):
        i = 1
        for subnet in self.subnets:
            print(f"\nSubnet {i}")
            print("--------")

            for k, v in subnet.items():
                print(f"{k}: {v}")
            
            i += 1
