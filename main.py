import abc
from datetime import datetime
from collections import defaultdict


# Base Device Class (Template)
class Device(abc.ABC):
    def __init__(self, device_id, name, energy_usage=0):
        # Initialize device attributes
        self.__device_id = device_id
        self.__name = name
        self.__status = 'off'
        self.__energy_usage = energy_usage

    # Getter methods
    #get the id of the device
    def get_id(self):
        return self.__device_id  
    # ues private attribute to prevent unauthorized data modification

    def get_name(self):
        return self.__name

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_energy_usage(self):
        return self.__energy_usage

    def set_energy_usage(self, energy_usage):
        self.__energy_usage = energy_usage

    # Control methods
    #turn on the device
    def turn_on(self):
        self.__status = "on"

    #turn off the device
    def turn_off(self):
        self.__status = "off"
    
    #print device information
    def __str__(self):
        return f"Device: {self.__name}, ID: {self.__device_id}, Status: {self.__status}, Energy Usage: {self.__energy_usage}kWh"


# Subclasses for devices
#we will define the light class, thermostat class and camera class by inheriting from the 'Device' class.
class Light(Device):
    def __init__(self, device_id, name, brightness=100):
        super().__init__(device_id, name) #initialization
        self.brightness = brightness


class Thermostat(Device):
    def __init__(self, device_id, name, temperature=22):
        super().__init__(device_id, name)
        self.temperature = temperature


class Camera(Device):
    def __init__(self, device_id, name, resolution='1080p'):
        super().__init__(device_id, name)
        self.resolution = resolution


# Device Controller 
# which is used to manage all the devices
class DeviceController:
    def __init__(self):
        self.devices = {} 
        #the dictionary is used for storing devices
        #and the key is the device's id

    #use the device's id as the key to store the device in the dictionary.
    def add_device(self, device):
        device_id = device.get_id()
        self.devices[device_id] = device

    #use the device's id as the key to remove the device in the dictionary.
    def remove_device(self, device_id):
        if device_id in self.devices:
            del self.devices[device_id]

    def list_devices(self):
        if not self.devices:
            print("Oops! No devices added to the controller yet. Add some first.") 
            # if the dictionary is empty
        else:
            print("list of devices:")
            for device in self.devices.values():
                print(device)

    def execute_command(self, device_id, command):
        if device_id in self.devices:
            device = self.devices[device_id]
            if command == "on":
                device.turn_on()
            elif command == "off":
                device.turn_off()
            else:
                print("please check your command")
                 # if the command is invalid


# Smart Home Hub (Singleton)
class SmartHomeHub:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SmartHomeHub, cls).__new__(cls)
            cls._instance.controller = DeviceController()
        return cls._instance

    #print the working information of a specific device.
    def schedule_task(self, device_id, command, time):
        print(f"scheduled task: device {device_id} will obey '{command}' command,at {time}")

    def display_status(self):
        print("status of all devices:")
        self.controller.list_devices()

    def total_energy_usage(self):
        #create a iterator which will allow us to iterate through each device one by one.
        devices_iterator = iter(self.controller.devices.values())
    
        def recursive_calculate(devices_iterator):
            try:
                #recursively call function get total energy usage of each device and sum them up
                device = next(devices_iterator)
                return device.get_energy_usage() + recursive_calculate(devices_iterator)
            except StopIteration: # if all devices have been processed
                return 0

        return recursive_calculate(devices_iterator)


# Main Execution (Template)
if __name__ == "__main__":
    hub = SmartHomeHub()

    # Add devices
    # create light, thermostat, and camera devices
    light = Light("L1", "Living Room Light")
    thermostat = Thermostat("T1", "Home Thermostat")
    camera = Camera("C1", "Front Door Camera")

    # Display devices
    hub.display_status()

    # Execute commands
    # Execute 'on' commands for the light
    hub.controller.execute_command("L1", "on") 
    # Execute off commands for thermostat
    hub.controller.execute_command("T1", "off")

    # Schedule tasks
    # Get the current time
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hub.schedule_task("C1", "on", time)

    # Calculate and print total energy usage
    print(f"Total Energy Usage: {hub.total_energy_usage()} kWh")