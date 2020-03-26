import napalm

def main():
   # Load the Driver and create the device instance
   driver = napalm.get_network_driver('ios')
   device = driver('10.0.0.5', 'ignw', 'ignw')

   device.open()
   # Get the 'facts' about the system and print them
   facts = device.get_facts()
   device.close()
   print(json.dumps(facts, indent=4))

if __name__ == "__main__":

   main()
