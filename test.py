# -*- coding: utf-8 -*-

import pyautogui

# カーソルを移動させる
pyautogui.moveTo(840, 525)
pyautogui.click()

# 矢印ボタン
pyautogui.press("left")
pyautogui.keyDown('left')
pyautogui.keyUp('left')

# print(pyautogui.KEYBOARD_KEYS)
