import napalm

def main():
   # Load the Driver and create the device instance
   driver = napalm.get_network_driver('ios')
   device = driver('10.0.0.5', 'ignw', 'ignw')
   device.open()
   # Load the candidate merge file
   device.load_merge_candidate(filename='./csr_undo_config')
   # Compare the files and print the differences - closing the connection
   diffs = device.compare_config()
   print(diffs)

   # Code to choose whether to commit or not.
   try:
       choice = raw_input("\nWould you like to commit these changes? [yN]: ")
   except NameError:
       choice = input("\nWould you like to commit these changes? [yN]: ")
   if choice == "y":
       print("Committing ...")
       device.commit_config()
       # Revert to the original config..
       try:
           choice = raw_input("\nWould you like to roll back the changes? [yN]: ")
       except NameError:
           choice = input("\nWould you like to roll back these changes? [yN]: ")
       if choice == "y":
           print("Rolling Back ...")
           device.rollback()
   else:
        print("Discarding...")
        device.discard_config()
   device.close()
   print("Done...")

if __name__ == "__main__":
   main()