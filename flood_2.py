import pyautogui,time
import pyperclip
pyautogui.PAUSE=0
def a(b,c,d):
    time.sleep(c)
    text=open(b,encoding="utf-8").read()
    text=text.split("\n")
    for i in text:
        if i=="":continue
        pyperclip.copy(i)
        pyautogui.hotkey("ctrl","v")
        pyautogui.press("enter")
        time.sleep(d)
if __name__=="__main__":
    a(input("File of text:"),int(input("Seconds to start:")),float(input("Interval to sleep:")))