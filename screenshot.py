#使い方
#python screenshot.py 右か左か ページ数 保存先のパス
#python screenshot.py right 342 /Users/yamada/SS/Pyautogui_SS/test_dir

import pyautogui
import time
import sys

right_left = sys.argv[1]
num_pages = int(sys.argv[2])
path_dir = sys.argv[3]

# Sleep for 5 seconds to allow me to open book
time.sleep(5)
# Range can be changed depending on the number of pages
for i in range(num_pages):
    # Turn page
    #pyautogui.keyDown('right')
    #pyautogui.keyUp('right')
    pyautogui.press(right_left)
    # Take and save a screenshot
    pyautogui.screenshot(path_dir + '/page_{}.png'.format(i))
    time.sleep(0.5)
