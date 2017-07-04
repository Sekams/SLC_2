class Car(object):
    """
        This class describes a class Car that can be used to instantiate various vehicles
    """
    num_of_doors = 4
    num_of_wheels = 4
    speed = 0

    def __init__(self, name="General", model="GM", car_type="saloon"):
        self.speed = Car.speed
        self.name = name
        self.model = model
        self.car_type = car_type

        if name == "Porshe" or name == "Koenigsegg":
            self.num_of_doors = 2
        else:
            self.num_of_doors = Car.num_of_doors
        if car_type == 'trailer':
            self.num_of_wheels = 8

    def is_saloon(self):
        if self.car_type == 'trailer':
            return False
        return True

    def drive(self, speed):
        if self.name == 'Mercedes':
            self.speed = speed * (1000 / 3)
        elif self.car_type == 'trailer':
            self.speed = speed * 11
        return self
