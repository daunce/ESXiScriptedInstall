#!/usr/bin/python
import os, commands, csv, subprocess

MAC=subprocess.check_output("esxcli network ip interface list |grep MAC",shell=True)

MACADDR = MAC.split()

print "MAC = " + MACADDR[2]

with open('ListOfHosts.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
                print "Line " + row[0] + " " + row[1]
                print "Comparing '%r' and '%r' " % (MACADDR[2], row[1])
                if MACADDR[2] == row[1]:
                        print "MATCHED + row[1]"
                        os.system("esxcli system hostname set --fqdn=" + row[0])
                        os.system("esxcli network ip interface ipv4 set --interface-name=vmk0 --ipv4=" + row[2] + " --netmask=" + row[3] + " --type=static")
print "End of loop"
print "Hostname is: "
os.system("esxcli system hostname get")

print MACADDR
print MACTEST
print "'%r'" % (MACTEST)
