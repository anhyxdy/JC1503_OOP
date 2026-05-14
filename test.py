import unittest
from datetime import datetime
from main import Light, Thermostat, Camera, DeviceController, SmartHomeHub
# test Framework and Core Class Import
class TestSmartHomeSystem(unittest.TestCase):

    def setUp(self):
        self.light = Light('L1', 'Living Room Light')
        self.thermostat = Thermostat('T1', 'Home Thermostat')
        self.camera = Camera('C1', 'Front Door Camera')
        self.controller = DeviceController()
        self.hub = SmartHomeHub()
        self.hub.controller.add_device(self.light)
        self.hub.controller.add_device(self.thermostat)
        self.hub.controller.add_device(self.camera)

    def test_device_operations(self):
        self.assertEqual(self.light.get_status(), 'off')
        self.light.turn_on()
        self.assertEqual(self.light.get_status(), 'on') #status assertion
        self.light.turn_off()
        self.assertEqual(self.light.get_status(), 'off') #status assertion

    def test_controller_add_remove_device(self):
        self.controller.add_device(self.light)
        self.assertIn('L1', self.controller.devices)
        self.controller.remove_device('L1')
        self.assertNotIn('L1', self.controller.devices)

    def test_controller_execute_command(self): #Verify the result of command execution
        self.controller.add_device(self.light)
        self.controller.execute_command('L1', 'on')
        self.assertEqual(self.controller.devices['L1'].get_status(), 'on') 
        self.controller.execute_command('L1', 'off')
        self.assertEqual(self.controller.devices['L1'].get_status(), 'off')

    def test_hub_schedule_task_and_energy_usage(self):
        task_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.hub.schedule_task('L1', 'on', task_time)
        total_energy = self.hub.total_energy_usage()
        self.assertEqual(total_energy, sum(device.get_energy_usage() for device in self.hub.controller.devices.values()))

    def test_device_inheritance_and_methods(self):
        self.assertIsInstance(self.light, Light)  #Check inheritance relationship
        self.assertIsInstance(self.thermostat, Thermostat)
        self.assertIsInstance(self.camera, Camera)
        self.light.turn_on()
        self.assertEqual(self.light.get_status(), 'on')
        self.thermostat.turn_off()
        self.assertEqual(self.thermostat.get_status(), 'off')

if __name__ == '__main__':
    unittest.main()