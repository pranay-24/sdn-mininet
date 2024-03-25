##sudo apt-get install mininet

import os
import subprocess

from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def create_network():
    # Create an instance of Mininet
    net = Mininet(controller=Controller, switch=OVSSwitch)

    # Add a controller
    net.addController('c0')

    # Add hosts
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')

    # Add a switch
    s1 = net.addSwitch('s1')

    # Add links
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    # Start the network
    net.start()

    # Open a file to write the network information
    with open('network_info.txt', 'w') as file:
        # Write the network topology
        file.write(f"Network Topology:\n{net.topo}\n\n")

        # Write the list of hosts
        file.write("Hosts:\n")
        for host in net.hosts:
            file.write(f"Host: {host.name}, IP: {host.IP()}\n")
        file.write("\n")

        # Write the list of switches
        file.write("Switches:\n")
        for switch in net.switches:
            file.write(f"Switch: {switch.name}\n")
        file.write("\n")

        # Write the list of links
        file.write("Links:\n")
        for link in net.links:
            file.write(f"Link: {link.intf1.name} <-> {link.intf2.name}\n")
        file.write("\n")

    # Run the CLI
    CLI(net)

    # Stop the network
    net.stop()


def push_to_github():
    # Change to the directory of your GitHub repository
    os.chdir('https://github.com/pranay-24/sdn-mininet.git')

    # Add the network_info.txt file to the Git repository
    subprocess.run(['git', 'add', 'network_info.txt'])

    # Commit the changes with a message
    subprocess.run(['git', 'commit', '-m', 'Update network_info.txt'])

    # Push the commit to GitHub
    subprocess.run(['git', 'push'])


if __name__ == '__main__':
    setLogLevel('info')
    create_network()
    push_to_github()
    