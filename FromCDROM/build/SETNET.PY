#!/usr/bin/python
import os, commands, csv, subprocess

MAC=subprocess.check_output("esxcli network ip interface list |grep MAC",shell=True)

MACADDR = MAC.split()

with open('/vmfs/volumes/datastore1/HOSTS.CSV', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
                if MACADDR[2] == row[1]:
                        os.system("esxcli system hostname set --fqdn=" + row[0])
                        os.system("esxcli network ip interface ipv4 set --interface-name=vmk0 --ipv4=" + row[2] + " --netmask=" + row[3] + " --type=static")
print "End of loop"

