import win32api
import win32con
##from ctypes import windll
import time
import serial

##def m_move(x,y):
##    windll.user32.SetCursorPos(x,y)
def l_click(x,y):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y)
def r_click(x,y):
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y)
        time.sleep(0.05)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y)

port = serial.Serial("COM7", baudrate=9600, timeout=3.0)

while 1:
    data = port.readline()[:-2]
    if data=='L':
        l_click(500,500)
        print('Left mouse button clicked!!')

    elif data=='R':
        r_click(500,500)
        print('Right mouse button clicked!!')

    else:
        print('Unknown data sequence received!!')

    time.sleep(0.5)
    print(str(data))
        
port.close()
