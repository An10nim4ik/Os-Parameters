import platform
import psutil
import socket
from colorama import init, Fore, Style
import getpass

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

