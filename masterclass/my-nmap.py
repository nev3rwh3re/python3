#Python script to run the NMAP script for log4j once per minute until stopped.
#* The script should use the following NMAP command
# .\nmap.exe --script "C:\Program Files\Rapid7\nexpose\plugins\nmap-config\scripts\sp-apache-log4j-rce-vuln.nse" -p 443 10.19.172.11
#* Run the script once per minute until the script is stopped or allow us to configure the number of times the script will run.



import subprocess
import os
from os import system
import sys

argProgram = []
nmap = '"C:\\Program Files (x86)\\Nmap\\nmap.exe" '
callscript = '--script "C:\\Program Files (x86)\\Nmap\scripts\\smb2-capabilities.nse" '
#callscript = '--script "C:\\Program Files\\Rapid7\\nexpose\\plugins\\nmap-config\\scripts\\sp-apache-log4j-rce-vuln.nse" '

portarg = '-p 443 '
outfile = '-oN nmap-log4j-results.txt '

argProgram.append(nmap)
argProgram.append(callscript)
argProgram.append(outfile)
argProgram.append(portarg)

if __name__ == "__main__":

    # Get arguments from input
    argCount = len(sys.argv)
    
    # Parse arguments
    for i in range(1, argCount):
        argProgram.append(sys.argv[i])

    print(argProgram)
    subprocess.call([argProgram], shell=True)

# output needs to look something like this
#   "C:\\Program Files (x86)\\Nmap\\nmap.exe" --script "C:\\Program Files (x86)\\Nmap\\scripts\\smb2-capabilities.nse" -p 443 192.168.10.77

