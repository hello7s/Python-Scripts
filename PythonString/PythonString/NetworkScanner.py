#!/usr/bin/env python
import nmap
nm = nmap.PortScanner()         # Creates your nmap.PortScanner object
nm.scan(hosts='10.0.0.0/24', arguments='-v -O -A') #Scanning your internal network range, in this case 10.0.0.0 /24 Subnetwork
nm.command_line()                   # Gets command line information for the scan
nm.all_hosts()                      # Identifies all hosts which were scanned

print('----------------------------------------------------')


hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

for host, status in hosts_list:
     print('{0}:{1}'.format(host, status))
