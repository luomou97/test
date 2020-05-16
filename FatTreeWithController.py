#!/usr/bin/python

from mininet.node import Controller, RemoteController, OVSController
from mininet.net import Mininet
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet(topo=None,
                  build=False,
                  ipBase='10.0.0.0/8')
    info('Adding controller\n')
    c0 = net.addController(name='c0',
                           controller=RemoteController,
                           protocol='tcp',
                           port=6633)

    info('Adding switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch)
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch)
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch)
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch)
    s12 = net.addSwitch('s12', cls=OVSKernelSwitch)
    s13 = net.addSwitch('s13', cls=OVSKernelSwitch)
    s14 = net.addSwitch('s14', cls=OVSKernelSwitch)
    s15 = net.addSwitch('s15', cls=OVSKernelSwitch)
    s16 = net.addSwitch('s16', cls=OVSKernelSwitch)
    s17 = net.addSwitch('s17', cls=OVSKernelSwitch)
    s18 = net.addSwitch('s18', cls=OVSKernelSwitch)
    s19 = net.addSwitch('s19', cls=OVSKernelSwitch)
    s20 = net.addSwitch('s20', cls=OVSKernelSwitch)

    info('Adding Hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.1.2', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.1.3', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.1.0.2', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.1.0.3', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.1.1.2', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.1.1.3', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.2.0.2', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.2.0.3', defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='10.2.1.2', defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.2.1.3', defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='10.3.0.2', defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='10.3.0.3', defaultRoute=None)
    h15 = net.addHost('h15', cls=Host, ip='10.3.1.2', defaultRoute=None)
    h16 = net.addHost('h16', cls=Host, ip='10.3.1.3', defaultRoute=None)

    info('Adding Links\n')
    # hosts <-> edges
    net.addLink(s1, h1)
    net.addLink(s1, h2)
    net.addLink(s2, h3)
    net.addLink(s2, h4)
    net.addLink(s5, h5)
    net.addLink(s5, h6)
    net.addLink(s6, h7)
    net.addLink(s6, h8)
    net.addLink(s9, h9)
    net.addLink(s9, h10)
    net.addLink(s10, h11)
    net.addLink(s10, h12)
    net.addLink(s13, h13)
    net.addLink(s13, h14)
    net.addLink(s14, h15)
    net.addLink(s14, h16)
    # edges <-> aggregations
    net.addLink(s3, s1)
    net.addLink(s3, s2)
    net.addLink(s4, s1)
    net.addLink(s4, s2)
    net.addLink(s7, s5)
    net.addLink(s7, s6)
    net.addLink(s8, s5)
    net.addLink(s8, s6)
    net.addLink(s11, s9)
    net.addLink(s11, s10)
    net.addLink(s12, s9)
    net.addLink(s12, s10)
    net.addLink(s15, s13)
    net.addLink(s15, s14)
    net.addLink(s16, s13)
    net.addLink(s16, s14)
    # aggregations <-> cores
    net.addLink(s17, s3)
    net.addLink(s17, s7)
    net.addLink(s17, s11)
    net.addLink(s17, s15)
    net.addLink(s18, s3)
    net.addLink(s18, s7)
    net.addLink(s18, s11)
    net.addLink(s18, s15)
    net.addLink(s19, s4)
    net.addLink(s19, s8)
    net.addLink(s19, s12)
    net.addLink(s19, s16)
    net.addLink(s20, s4)
    net.addLink(s20, s8)
    net.addLink(s20, s12)
    net.addLink(s20, s16)

    info('Starting network\n')
    net.build()

    info('Starting controller\n')
    for controller in net.controller:
        controller.start()

    info('Starting switches\n')
    for i in range(1, 21):
        switchname = 's' + str(i)
        net.get(switchname).start([c0])

    info('Post configure switches and hosts\n')
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLoglevel('info')
    myNetwork()