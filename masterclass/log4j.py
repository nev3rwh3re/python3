import subprocess
import sys

argProgram = []
nmap = '"C:\\Program Files\\Rapid7\\nexpose\\nmap.exe" '
callscript = '--script "C:\\Program Files\\Rapid7\\nexpose\\plugins\\nmap-config\\scripts\\sp-apache-log4j-rce-vuln.nse" '

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