import math, re

def validate_address(address):
    str_address = ".".join(str(octet) for octet in address)
    if re.search("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", str_address):
        address_valid = True
    else:
        address_valid = False
    
    return address_valid

def validate_netmask(netmask):
    if 0 < netmask < 33:
        netmask_valid = True
    else:
        netmask_valid = False

    return netmask_valid

def increment_address(address, increment, working_octet=3):
    remainder = (address[working_octet] + increment) % 256
    increment = math.floor((address[working_octet] + increment) / 256)

    address[working_octet] = remainder

    if working_octet > 0:
        working_octet -= 1
        return increment_address(address, increment, working_octet)
    else:
        return address

def get_number_of_addresses(netmask):
    return 2 ** (32 - netmask)

def get_smallest_network(number_of_addresses):
    host_bits = 1
    while 2 ** host_bits < number_of_addresses:
        host_bits += 1

    return 32 - host_bits

def get_broadcast_address(network_id, netmask):
    number_of_adresses = get_number_of_addresses(netmask)

    return increment_address(network_id[:], number_of_adresses -1)

def get_useable_range(network_id, netmask):
    first_useable_address = increment_address(network_id[:], 1)

    number_of_adresses = get_number_of_addresses(netmask)
    last_useable_address = increment_address(network_id[:], number_of_adresses -2)

    return first_useable_address, last_useable_address