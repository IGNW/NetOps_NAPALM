from netmiko import ConnectHandler
import csv
import json

def main():
    # Open the CSV file - use 'csr', 'asa', or 'nxos' as needed
    f = open('csr.csv', 'r')

    # Change each filename to the field name (csr fields below)
    reader = csv.DictReader(f, fieldnames=('hostname','os','ipv4_address','username','password','enable'))

    # Parse the CSV into JSON
    csv_str = json.dumps([row for row in reader])
    csv_output = json.loads(csv_str)


   # Loop through the csr devices and get a lit of interfaces
    for i in range(len(csv_output)):
        hname = csv_output[i]["hostname"]
        device_os = csv_output[i]["os"]
        address = csv_output[i]["ipv4_address"]
        uname = csv_output[i]["username"]
        pword = csv_output[i]["password"]
        enable = csv_output[i]["enable"]
        # Call a function to connect and get interfaces, pass it the required fields
        error = connect_to_device(hname,device_os,address,uname,pword,enable)
        print(error)
        # loop


def connect_to_device(hn,dt,ipaddr,un,pw,se):
    # Set error_note to collect any connection errors
    error_note = "no_error"
    # Initialize the list for interfaces
    interface_list = []
    # Connect to the device
    net_connect = ConnectHandler(device_type=dt, ip=ipaddr, username=un, password=pw, secret=se)
    print("Connected to device " + hn + " at ip address " + ipaddr)

    # Enter Enable Mode for sending commands later
    net_connect.enable()
    checkerror = net_connect.find_prompt()
    if not '#' in checkerror:
        print("Not in Enable Mode!!!")
        error_note = "no_enable"
        exit()
    else:
        print("You are in Enable Mode!!!")

    # Get list of interfaces, split, pull interface names into interfacelist list
    # cmdoutput = net_connect.send_command('show ip int brief | include up')
    cmdoutput = net_connect.send_command('show ip int brief')
    outputlist = cmdoutput.split()
    for eachword in outputlist:
        interface_list.append(eachword)
    print(interface_list)
    net_connect.disconnect()
    return(error_note)

if __name__ == "__main__":
   main()
