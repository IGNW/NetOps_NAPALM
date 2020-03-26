import napalm

def main():
   # Load the Driver and create the device instance
   driver = napalm.get_network_driver('ios')
   device = driver('10.0.0.5', 'ignw', 'ignw')

   device.open()

   # Get the current running config and print it
   config = device.get_config(retrieve="running")
   device.close()
   running_config = config['running']
   print(running_config, sep = "\n")

if __name__ == "__main__":

   main()
