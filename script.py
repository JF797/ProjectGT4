import os
import subprocess


networkAddress="192.168.69."
ipStartRange=120
ipEndRange=122
aliveDevices={}


def runPingCheck(ipAddress):
    with open(os.devnull, 'w') as DEVNULL:
        try:
            subprocess.check_call(
                ['ping', '-c', '1', '-q', ipAddress],
                stdout=DEVNULL,
                stderr=DEVNULL
            )
            return True
        except subprocess.CalledProcessError:
            return False




for hostAddress in range(ipStartRange, ipEndRange+1):
    ipAddress = networkAddress+str(hostAddress)
    if runPingCheck(ipAddress) == True:
        print(ipAddress+" is alive")
        aliveDevices.update({''})
    elif runPingCheck(ipAddress) == False:
        print(ipAddress+" is dead")
    else:
        print("dunno")

print(aliveDevices)