import platform
import psutil
import socket
from colorama import init, Fore
import getpass
import os

# Retrieve OS Name and Version
os_name = platform.system()
os_version = platform.version()

# Processor Information
processor_info = platform.processor()

# Memory (GB)
memory_info = round(psutil.virtual_memory().total / (1024.0 ** 3), 2)

# Available Disk Space (GB)
disk_info = psutil.disk_usage('/').free / (2**30)  # Convert bytes to gigabytes

# Current User
current_user = getpass.getuser()

# Initialize colorama
init()

# Print colored output
ip_address = socket.gethostbyname(socket.gethostname())
print(Fore.RED + "IP Address: {}".format(ip_address))
print(Fore.BLUE + "Operating System: {} {}".format(os_name, os_version))
print(Fore.GREEN + "Processor Information: {}".format(processor_info))
print(Fore.MAGENTA + "Memory (GB): {} GB".format(memory_info))
print(Fore.CYAN + "Available Disk Space (GB): {:.2f} GB".format(disk_info))
print(Fore.YELLOW + "Current User: {}".format(current_user))

try:
    # Attempt to retrieve memory information
    memory_info = round(psutil.virtual_memory().total / (1024.0 ** 3), 2)
    print(Fore.LIGHTBLACK_EX + "Memory (GB): {} GB".format(memory_info))
except Exception as e:
    print("Error retrieving memory information:", e)

# Retrieve and display environmental variables
env_vars = os.environ
print(Fore.LIGHTYELLOW_EX + "Environment Variables:")
for var, value in env_vars.items():
    print(f"{var}: {value}")

# Retrieve CPU Usage
cpu_usage = psutil.cpu_percent(interval=1)
print(Fore.LIGHTCYAN_EX + "CPU Usage: {}%".format(cpu_usage))
