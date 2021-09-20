import pyautogui,time
import pyperclip
pyautogui.PAUSE=0
def a(b,c,d):
    time.sleep(c)
    while True:
        pyperclip.copy(b)
        pyautogui.hotkey("ctrl","v")
        pyautogui.press("enter")
        time.sleep(d)
if __name__=="__main__":
    a(input("Flood text:"),int(input("Seconds to start:")),float(input("Interval:")))