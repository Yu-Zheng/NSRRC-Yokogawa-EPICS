from subprocess import check_output
import os.path

def Get_IP():
    #s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #s.connect(("8.8.8.8", 80))
    #IP = s.getsockname()[0]
    
    ips = check_output(['hostname', '--all-ip-addresses'])
    IP = ips.decode('UTF-8').replace(" \n","")
    return IP

def IP_Check(IP_Last):
    if int(IP_Last) < 10:
        return ("0"+IP_Last)
    else:
        return IP_Last

base_path = os.path.dirname(os.path.realpath(__file__))
Raw_path = os.path.join(base_path, "FE_EPICS_List_Raw.db")
Run_path = os.path.join(base_path, "FE_EPICS_List_Run.db")

# Read in the file
with open(Raw_path, 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('{Number}', IP_Check(Get_IP().split(".")[3]))

# Write the file out again
with open(Run_path, 'w') as file:
  file.write(filedata)
