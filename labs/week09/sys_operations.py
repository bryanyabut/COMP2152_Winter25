import os 
import platform
import socket

# Lab 9 - Q3 a.a .. 3a.b
# Getting machine type and processor type 
print(platform.machine())
print(platform.architecture())

# Lab 9 - Q3 a.c .. 3a.d
# Getting and setting socket timeout
print(socket.getdefaulttimeout())
socket.setdefaulttimeout(50)
print(socket.getdefaulttimeout())

# Lab 9 - Q3 a.e
# OS name
print(os.name)
print(platform.system())

# Lab 9 - Q3 a.f
# Process ID
print("Parent Process ID:", os.getpid())

# Lab 9 - Q3 b.a
# File descriptors
f_name = "fdpractice.txt"
f = os.open(f_name, os.O_RDWR | os.O_CREAT)
print("File Descriptor:", f)

# Open file descriptor as file object
f_obj = os.fdopen(f, mode="a+")
print("File Object:", f_obj)
f_obj.close()

print()

# Lab 9 - Q3 b.e
# Forking (Unix-based systems only)
if hasattr(os, "fork"):  # Check if fork() is available
    print("Before fork:", os.getpid())
    p = os.fork()  # Fork the process

    if p == 0:
        print("Child process")
        print("Parent process PID:", os.getppid())
    else:
        print("Parent process")
        os.wait()  # Wait for child process to complete
        print("Child process PID:", p)
    print("Last line")
else:
    print("Fork not supported on this system.")