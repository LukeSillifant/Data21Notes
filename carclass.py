class Car:

    def __init__(self, name, top_speed):
        self.__top_speed = top_speed
        self.__name = name
        self.__current_speed = 0

    def set_top_speed(self, top):
        self.__top_speed = top

    def get_top_speed(self):
        return self.__top_speed

    def get_name(self):
        return self.__name

    def get_current_speed(self):
        return self.__current_speed

    def accelerate_pedal(self, time_pressed: float = 1.0):
        self.__current_speed += min(5 * time_pressed, self.__top_speed - self.__current_speed)

    def brake_pedal(self, time_pressed: float = 1.0):
        self.__current_speed -= min(5 * time_pressed, self.__current_speed)


def car_journey(car_name: str = "Vauxhall Corsa", car_top_speed: float = 150.0):
    my_car = Car(car_name, car_top_speed)

    journey_string = input("Enter your car journey: ")

    def journey_instructions():
        print(ord("a")-96)
        string_char = 0
        while True:
            if journey_string[string_char: string_char + 1] == "a" or "b":
                for time_check in range(string_char + 1, len(journey_string)):
                    if journey_string[time_check: time_check + 1] == " ":
                        break

            string_char += 1
            # if string_char ==

    journey_instructions()

    print(f'\nYour {my_car.get_name()}, (Top speed: {my_car.get_top_speed()} km/h) is ready to go.\n'
          f'The car is currently at rest ({my_car.get_current_speed()} km/h), enjoy your drive!')
    my_car.accelerate_pedal(29.9)
    print(f'Current speed: {my_car.get_current_speed()}')


car_journey()
