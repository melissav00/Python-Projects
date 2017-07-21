class Vehicles:
  """Class for vehicles"""

  def __init__(self,name):
    self.name = name
    self.wheels = 0
    self.doors = 0
    self.seats = 0
    self.passengers = []

  def num_wheels(self, wheels):
      self.wheels = wheels
      print(self.wheels)

  def num_doors(self, doors):
      self.doors = doors
      print(self.doors)

  def num_seats(self,seats):
      self.seats =  seats
      print(self.seats)

  def add_passenger(self, passenger):
      self.passengers.append(passenger)
      print(self.passengers)

v1 = Vehicles("car")
v1.num_wheels(4)
v1.num_doors(4)
v1.num_seats(8)
Names = ["Jose","Cassie","Joseph","Steph","Cuda","Bam"] #Names of passengers!
v1.add_passenger(Names)
