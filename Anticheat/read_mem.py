import psutil
import ctypes

# Define address to read
address = 0x213D870AF38

# Get process ID of Minecraft.Windows.exe
for process in psutil.process_iter(['pid', 'name']):
    if process.info['name'] == 'Minecraft.Windows.exe':
        pid = process.info['pid']
        break
else:
    print("Minecraft.Windows.exe is not running!")
    exit()

# Open process handle
process_handle = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, pid)

# Read memory address
value = ctypes.c_ulonglong()
ctypes.windll.kernel32.ReadProcessMemory(process_handle, ctypes.c_void_p(address), ctypes.byref(value), ctypes.sizeof(value), None)

# Close process handle
ctypes.windll.kernel32.CloseHandle(process_handle)

print(f"Value at address {hex(address)} is {value.value}")
