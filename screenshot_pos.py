# 使い方
# python screenshot_full.py 右か左か ページ数 保存先のパス
# python screenshot.py_full right 342 /Users/yamada/SS/Pyautogui_SS/test_dir

import argparse
import pyautogui
import time
import os
# マウスのクリック取得
from pynput import mouse
# pdfへ変換
import glob
from PIL import Image
import img2pdf
# pdfをまとめる
import re
import PyPDF2
# ディレクトリの削除、移動
import shutil

# コマンドライン引数の取得
parser = argparse.ArgumentParser()
parser.add_argument('-pos', '--position', action='store_true')
parser.add_argument('-lr')
parser.add_argument('-p', '--pages')
parser.add_argument('-dir', '--path_dir')
parser.add_argument('-time', '--time_sleep')
parser.add_argument('-title')
args = parser.parse_args()

right_left = args.lr
num_pages = int(args.pages)
path_dir = args.path_dir
time_sleep = float(args.time_sleep)
title = args.title
# 保存先のディレクトリを作成
os.makedirs("./" + title)

# 座標取得かどうか場合分け
if args.position is True:
    list_point = []

    class Monitor:
        def __init__(self):
            self.counter = 0
            # マウスクリック取得は2回
            self.over_count = 2

        def count(self):
            self.counter += 1
            print('Count:{0}'.format(self.counter))

        def is_over(self):
            return True if self.counter >= self.over_count else False

        def call(self):
            self.count()
            if self.is_over():
                print('Done')
                self.listener.stop()  # 規定回数過ぎたら終了

        def on_click(self, x, y, button, pressed):
            # print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x,y)))
            list_point.append((x, y))
            if pressed:
                self.call()

        def start(self):
            with mouse.Listener(on_click=self.on_click) as self.listener:
                self.listener.join()

    monitor = Monitor()
    print("mouse click start")
    monitor.start()

    # 座標計算
    x1 = list_point[0][0]
    y1 = list_point[0][1]
    x2 = list_point[2][0]
    y2 = list_point[2][1]
    width = x2 - x1
    hight = y2 - y1

    # スクリーンショット
    for i in range(num_pages):
        time.sleep(time_sleep)
        # Take and save a screenshot
        sc = pyautogui.screenshot(
            region=(x1 * 2, y1 * 2, width * 2, hight * 2))
        sc.save("./" + title + '/page_{}.png'.format(i))
        # Turn page
        pyautogui.press(right_left)

else:
    # Sleep for 5 seconds to allow me to open book
    time.sleep(5)
    # スクリーンショット
    for i in range(num_pages):
        time.sleep(time_sleep)
        # Take and save a screenshot
        sc = pyautogui.screenshot()
        sc.save("./" + title + '/page_{}.png'.format(i))
        # Turn page
        pyautogui.press(right_left)

print("Converting...")

# png→jpg
path_ = "./" + title + '/*.png'
# 保存先のディレクトリを作成
os.makedirs("./" + title + "/jpg")

list_png = glob.glob(path_)
for i in list_png:
    name, ext = os.path.splitext(i)
    name_png = name.split("/")[-1] + ".jpg"
    # 変換
    im = Image.open(i)
    rgb_im = im.convert('RGB')
    rgb_im.save("./" + title + "/jpg/" + name_png)

# jpg→pdf
path_jpg = "./" + title + "/jpg/*.jpg"
list_jpg = glob.glob(path_jpg)
# 保存先のディレクトリを作成
os.makedirs("./" + title + "/pdf")

for i in list_jpg:
    name, ext = os.path.splitext(i)
    name_pdf = name.split("/")[-1] + ".pdf"
    # 変換
    # Pillowモジュールを使用し画像の読み込み
    img = Image.open(i)
    # 画像→pdfファイルに変換
    cov_pdf = img2pdf.convert(i)
    # pdfファイルを読み込み（pdf_nameで指定したpdfがない場合、pdf_nameをファイル名として新規にpdfファイルを作成）
    file = open("./" + title + "/pdf/" + name_pdf, "wb")
    # pdfファイルを書き込み
    file.write(cov_pdf)

    # 開いているファイルを閉じる
    img.close()
    file.close()

# 複数のpdfファイルを結合する
pdf_path = "./" + title + "/pdf/"

merge = PyPDF2.PdfFileMerger()
for j in sorted(os.listdir(pdf_path), key=lambda s: int(re.search(r'\d+', s).group())):
    merge.append(pdf_path + "/" + j)
merge.write("./" + title + '/' + title + '.pdf')
merge.close()
print("変換終了")

# すべて終了後、all.pdf以外のファイル、ディレクトリを削除する
shutil.move("./" + title + '/' + title + '.pdf', path_dir)
shutil.rmtree("./" + title)
