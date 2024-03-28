# This program allows the Sales Manager to view the list of authorized vehicles, search for specific vehicles, and add new vehicles to the list.

# Initialize AllowedVehiclesList
class CarFinder:
  def __init__(self):
      self.AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

  # Printing authorized vehicles
  def print_authorized_vehicles(self):
      print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
      for vehicle in self.AllowedVehiclesList:
          print(vehicle)
        
# Searching a Vehicle
  def search_vehicle(self, search_query):
      if search_query in self.AllowedVehiclesList:
          print(f"{search_query} is an authorized vehicle.")
      else:
          print(f"{search_query} is not an authorized vehicle.")

# Adding a Vehicle
  def add_vehicle(self, new_vehicle):
      self.AllowedVehiclesList.append(new_vehicle)
      print(f"You have added \"{new_vehicle}\" as an authorized vehicle.")

# Running the Program
  def run(self):
      while True:
          print("********************************")
          print("AutoCountry Vehicle Finder v0.3")
          print("********************************")
          print("Please Enter the following number below from the following menu:")
          print("1. PRINT all Authorized Vehicles")
          print("2. SEARCH for Authorized Vehicle")
          print("3. ADD Authorized Vehicle")
          print("4. Exit")
          choice = input("Enter your choice: ")

          if choice == '1':
              self.print_authorized_vehicles()
          elif choice == '2':
              search_query = input("Enter the full Vehicle name you would like to search: ")
              self.search_vehicle(search_query)
          elif choice == '3':
              new_vehicle = input("Enter the full Vehicle name you would like to add: ")
              self.add_vehicle(new_vehicle)
          elif choice == '4':
              print("Exiting...")
              break
          else:
              print("Invalid choice. Please choose again.")


# Unit Test #1
car_finder = CarFinder()
car_finder.run()

# Unit Test #2
car_finder = CarFinder()
car_finder.add_vehicle("Rivian R1T")

# Unit Test #3
car_finder = CarFinder()
car_finder.add_vehicle("Ram 1500")

# Unit Test #4
car_finder = CarFinder()
car_finder.print_authorized_vehicles()