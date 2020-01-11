#使い方
#python screenshot_full.py 右か左か ページ数 保存先のパス
#python screenshot.py_full right 342 /Users/yamada/SS/Pyautogui_SS/test_dir

import pyautogui
import time
import sys
import os
#pdfへ変換
import glob
from PIL import Image
import img2pdf
#pdfをまとめる
import re
import PyPDF2
#ディレクトリの削除、移動
import shutil

right_left = sys.argv[1]
num_pages = int(sys.argv[2])
path_dir = sys.argv[3]
#保存先のディレクトリを作成
os.makedirs(path_dir)

# Sleep for 5 seconds to allow me to open book
time.sleep(5)
# Range can be changed depending on the number of pages
for i in range(num_pages):
    time.sleep(0.5)
    # Turn page
    pyautogui.press(right_left)
    # Take and save a screenshot
    pyautogui.screenshot(path_dir + '/page_{}.png'.format(i))
    time.sleep(0.5)
    
#png→jpg
path_ = path_dir + '/*.png'
#保存先のディレクトリを作成
os.makedirs(path_dir + "/jpg")

list_png = glob.glob(path_)

for i in list_png:
    name, ext = os.path.splitext(i)
    name_png = name.split("/")[-1] + ".jpg"
    
    #変換
    im = Image.open(i)
    rgb_im = im.convert('RGB')
    rgb_im.save(path_dir + "/jpg/" + name_png)

#jpg→pdf
path_jpg = path_dir + "/jpg/*.jpg"
list_jpg = glob.glob(path_jpg)
#保存先のディレクトリを作成
os.makedirs(path_dir + "/pdf")

for i in list_jpg:
    name, ext = os.path.splitext(i)
    name_pdf = name.split("/")[-1] + ".pdf"
    
    #変換
    #Pillowモジュールを使用し画像の読み込み
    img = Image.open(i)
    #画像→pdfファイルに変換
    cov_pdf = img2pdf.convert(i)
    #pdfファイルを読み込み（pdf_nameで指定したpdfがない場合、pdf_nameをファイル名として新規にpdfファイルを作成）
    file = open(path_dir + "/pdf/" + name_pdf, "wb")
    #pdfファイルを書き込み
    file.write(cov_pdf)

    #開いているファイルを閉じる
    img.close()
    file.close()
    
#複数のpdfファイルを結合する
pdf_path = path_dir + "/pdf/"

merge = PyPDF2.PdfFileMerger()
for j in sorted(os.listdir(pdf_path), key=lambda s: int(re.search(r'\d+', s).group())):
    merge.append(pdf_path + "/" + j)
merge.write(path_dir + "/" + "all.pdf")
merge.close()
print("変換終了")

#すべて終了後、all.pdf以外のファイル、ディレクトリを削除する
shutil.move(path_dir + '/all.pdf', path_dir + '/../')
shutil.rmtree(path_dir)
