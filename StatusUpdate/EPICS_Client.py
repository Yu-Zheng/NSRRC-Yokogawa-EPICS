from subprocess import check_output
import os.path
import time
import pandas as pd
import ctypes

def Get_IP():    
    ips = check_output(['hostname', '--all-ip-addresses'])
    IP = ips.decode('UTF-8').replace(" \n","")
    return IP

def IP_Check(IP_Last):
    if int(IP_Last) < 10:
        return ("0"+IP_Last)
    else:
        return IP_Last

def Gen_PVs(Host_IP):
    #base_path = os.path.dirname(os.path.realpath(__file__))
    #PV_CSV_Path = os.path.join(base_path, "FE_Digital_PV.csv")
    PV_CSV_Path = "FE_Digital_PV.csv"
    DF = pd.read_csv(PV_CSV_Path, header = None)
    for idx, i in enumerate(DF[0]):
        DF[0][idx]=i.replace("00", IP_Check(Host_IP.split(".")[3]))
    return DF

def F3RP70(Register):
    libc = ctypes.cdll.LoadLibrary("/usr/local/lib/libm3.so.1")
    c_no = ctypes.c_int(1)
    c_num = ctypes.c_int(1)
    c_data = ctypes.pointer(ctypes.c_ushort())
    error=libc.readM3SharedRelay(c_no, c_num,c_data)
    Status=list(bin(c_data.contents.value))
    return [Status,error]

def main():
    DF = Gen_PVs(Get_IP())
    EPICS_PV_List = DF[0]
    Register_List = DF[1]
    while True:
        for idx, i in enumerate(EPICS_PV_List):
            #caput(i, F3RP70(Register_List[idx])) #Single Put
            #caput_many(DF[0],DF[1])
            print(i + "   " + Register_List[idx])
        time.sleep(1)

if __name__ == '__main__':
    main()
