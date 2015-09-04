#!/usr/bin/env python
import nmap
nm = nmap.PortScanner()         # Creates your nmap.PortScanner object
nm.scan(hosts='10.0.0.0/24', arguments='-v -O -A') #Scanning your internal network range, in this case 10.0.0.0 /24 Subnetwork
nm.command_line() 
nm.all_hosts()                      # get all hosts that were scanned


print('----------------------------------------------------')
 # If you want to do a pingsweep on network 192.168.1.0/24:

hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
for host, status in hosts_list:
     print('{0}:{1}'.format(host, status))

