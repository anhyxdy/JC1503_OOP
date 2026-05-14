# JC1503_OOP

A Python Object-Oriented Programming (OOP) course project example. It implements a simplified smart home system using an abstract base class (`Device`) plus concrete device subclasses (`Light` / `Thermostat` / `Camera`). Devices are managed through a controller (`DeviceController`), and a singleton hub (`SmartHomeHub`) provides a single entry point for scheduling/status/energy usage calculation.

> Entry point: `main.py`  
> Unit tests: `test.py`

## Features

- **Abstract base class `Device`**: common fields and behaviors (`id`, `name`, `status`, `energy_usage`, `turn_on`, `turn_off`, etc.)
- **Device subclasses**
  - `Light`: has `brightness`
  - `Thermostat`: has `temperature`
  - `Camera`: has `resolution`
- **`DeviceController`**: add/remove/list devices; execute `on/off` commands by `device_id`
- **`SmartHomeHub` (Singleton)**
  - `display_status()`: prints the current device list
  - `schedule_task()`: prints scheduling info (demo behavior)
  - `total_energy_usage()`: recursively calculates total energy usage across devices

## Requirements

- Python 3.10+ (tested with Python 3.12)
- No third-party dependencies

## Run

From the project directory:

```bash
python main.py
```

You should see output such as:

- The device list (initially all `off`)
- Executed `on/off` commands
- A scheduled task message
- Total energy usage

## Run tests

From the project directory:

```bash
python -m unittest -v
```

Or run the test file directly:

```bash
python test.py
```

## Project structure

- `main.py`
  - `Device`: abstract base device class
  - `Light` / `Thermostat` / `Camera`: concrete device implementations
  - `DeviceController`: device registry + command execution
  - `SmartHomeHub`: singleton hub wrapping controller + status/scheduling/aggregation
- `test.py`
  - `unittest` test cases covering on/off operations, controller add/remove/execute, and hub energy aggregation

## Notes / Known behavior

- `DeviceController.execute_command(device_id, command)` currently supports only `command in {"on", "off"}`; other values print an error message.
- `SmartHomeHub.schedule_task(...)` only prints a “scheduled” message and does not actually run delayed execution (sufficient for a course demo).
- Each device’s `energy_usage` defaults to `0`. To make the total usage meaningful, pass a value during initialization or call `set_energy_usage()` later.
