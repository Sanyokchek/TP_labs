import os
import json
import platform
import psutil

os_name = platform.system()
if os_name == "Darwin":
    os_name = "macOS"

memory = psutil.virtual_memory()
ram_gb = (memory.total)/(1024**3)

os_info = {
    "name": platform.system(),
    "release": platform.release(),
    "version": platform.version(),
    "architecture": platform.machine()
 }
disks = []
for partition in psutil.disk_partitions():
    usage = psutil.disk_usage(partition.mountpoint)

    disk = {
        "device": partition.device,
        "total memory": f"{usage.total / (1024 ** 3):.2f} GB"
    }

    disks.append(disk)

pc_info = {
    "processor": platform.processor(),
    "cpu_count": os.cpu_count(),
    "ram": f"{ram_gb:.2f} GB",
    "disks": disks
}

data = {
    "os": os_info,
    "computer": pc_info
}
with open("pc_info.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)


    