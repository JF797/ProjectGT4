import os
import subprocess


networkAddress="192.168.69."
ipStartRange=120
ipEndRange=122


# def runPingCheck(ipAddress):
#     result = subprocess.call(['ping', '-c', '1', '-q', ipAddress])
#     if result == 1:
#         return False
#     elif result == 2:
#         return True
    

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
    


print(runPingCheck("192.168.69.121"))




# for hostAddress in range(ipStartRange, ipEndRange+1):
#     ipAddress = networkAddress+str(hostAddress)
#     if runPingCheck(ipAddress) == True:
#         print(ipAddress+" is alive")
#     elif runPingCheck(ipAddress) == False:
#         print(ipAddress+" is dead")
#     else:
#         print("dunno")