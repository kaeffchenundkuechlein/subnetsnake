import argparse
import ipv4utils, ipv4network

parser = argparse.ArgumentParser(prog="subnetsnake", description="Helps you to quickly segment an IPv4 network using VLSM")
parser.add_argument("-n", "--network", help="The CIDR prefix of the network you want to segment")
parser.add_argument("-s", "--subnets", nargs="*", help="The sizes of the subnets you want to create, seperated by spaces")
args = parser.parse_args()

network_id, network_mask = args.network.split("/")
network_id = [int(octet) for octet in network_id.split(".")]
network_mask = int(network_mask)

wanted_subnets = [int(subnet) for subnet in args.subnets]
wanted_subnets.sort(reverse=True)

if not ipv4utils.validate_address(network_id):
    raise ValueError("The network ID you provided is invalid")

if not ipv4utils.validate_netmask(network_mask):
    raise ValueError("The network mask you provided is invalid")

network = ipv4network.Network(network_id, network_mask)

for wanted_subnet in wanted_subnets:
    network.create_subnet(wanted_subnet)


if network.required_addresses > network.available_addresses:
    message = f"The subnets you want to create require {network.required_addresses} addresses,\n"
    message +=  f"but there are only {network.available_addresses} addresses available in the network you provided"
    raise ValueError(message)
else:
    network.display_subnets()
