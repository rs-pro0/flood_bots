import pyautogui,time
import pyperclip
pyautogui.PAUSE=0.05
def a(b,c):
    time.sleep(c)
    while True:
        pyperclip.copy(b)
        pyautogui.hotkey("ctrl","v")
        pyautogui.press("enter")
if __name__=="__main__":
    a(input("Flood text:"),int(input("Seconds to start:")))