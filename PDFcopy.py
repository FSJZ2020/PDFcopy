import win32clipboard
from pynput import mouse,keyboard
import time
def on_press(key):
    pass
def on_release(key):
    if str(key)==r"'\x03'":
        time.sleep(0.1)
        win32clipboard.OpenClipboard()
        a=win32clipboard.GetClipboardData()
        win32clipboard.EmptyClipboard()
        a=a.replace('\n','')
        a=a.replace('\r','')
        a=a.replace(' ','')
        win32clipboard.SetClipboardText(a)
        win32clipboard.CloseClipboard()
def listen_key_nblock():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start() 

if __name__=="__main__":
    listen_key_nblock()
    while True:
        pass