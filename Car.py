# Logan H's Car Simulation Program

# 1) DEFINE the Car class with attributes and methods
class Car:
    # Constructor method to initialize year model, make, and speed
    def __init__(self, year_model, make):
        self.__year_model = year_model   # Private attribute for car's year model
        self.__make = make               # Private attribute for car's make
        self.__speed = 0                 # Private attribute for car's speed, starts at 0

    # Method to increase the car's speed by 5
    def accelerate(self):
        self.__speed += 5

    # Method to decrease the car's speed by 5
    def brake(self):
        self.__speed -= 5

    # Method to return the current speed
    def get_speed(self):
        return self.__speed

# 2) CREATE a Car object with year model and make
my_car = Car(2023, "Toyota")  # Car starts at speed 0

# 3) CALL the accelerate method 5 times and display the speed each time
print("Accelerating...")
for i in range(5):
    my_car.accelerate()  # Increase speed by 5
    print(f"Speed after acceleration {i+1}: {my_car.get_speed()} mph")  # Show current speed

# 4) CALL the brake method 5 times and display the speed each time
print("\nBraking...")
for i in range(5):
    my_car.brake()  # Decrease speed by 5
    print(f"Speed after brake {i+1}: {my_car.get_speed()} mph")  # Show current speed
