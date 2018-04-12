import sys
import os

def green(message):
   print("\033[1;32;40m " + message + " \n")
   finish()

def red(message):
   print("\033[1;31;40m [ERROR] " + message + " \n")
   finish()

def blue(message):
   print("\033[1;34;40m [WARN] " + message + " \n")
   finish()

def finish():
    """
    reset the color of windows/terminal before exit
    """
    if os.name == "posix":
        sys.stdout.write("\033[0m")
    else:
        import ctypes
        std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)
        handle = std_out_handle
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, 7)
