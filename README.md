# Pyautogui_screenshot

Pyautoguiを使用して、Macのスクリーンショットを自動化＋pdf変換+1つのpdfにまとめる

## 使い方

screenshot_pos.py

```bash
% python screenshot_pos.py --help
usage: screenshot_pos.py [-h] [-pos] [-lr LR] [-p PAGES] [-dir PATH_DIR]
                         [-time TIME_SLEEP] [-title TITLE]

optional arguments:
  -h, --help            show this help message and exit
  -pos, --position
  -lr LR
  -p PAGES, --pages PAGES
  -dir PATH_DIR, --path_dir PATH_DIR
  -time TIME_SLEEP, --time_sleep TIME_SLEEP
  -title TITLE

#exsample
% python screenshot_pos.py -pos -lr left -p 10 -dir ./test -time 0.2 -title test
```



<旧ver>

screenshot_full.pyを使う。

```bash
#python screenshot_full.py 右か左か ページ数 保存先のパス

% python screenshot_full.py left 10 /Users/yamada/SS/Pyautogui_SS/test_dir
```



## 更新履歴

2020.1.10

レポジトリ作成

2020.1.12

・スクリーンショットの範囲選択ができるように

・オプションをわかりやすく

2020.1.15  

・pdfの保存先のディレクトリを選択可能に
・travisCIでpep8に従っているか確認


## 使用した主なライブラリ

- Pyautogui

- img2pdf

- PyPDF2

  

## 必要なライブラリのinstall(condaにて)

```
conda install -c conda-forge pyautogui -y
conda install -c conda-forge pillow -y
conda install -c conda-forge img2pdf -y
conda install -c conda-forge pypdf2 -y
```



## ポイント

- Pyautoguiにて、キーボード操作を行い、ページの移動も可能
- Pyautoguiにて、スクリーンショットがとれる
- 最終的には、まとめたpdf以外のディレクトリ、ファイル類は全て削除



## 流れ

1. 保存先のディレクトリを作成
2. Pyautoguiにて、ページ移動＋スクリーンショット撮影＋一定時間sleepで待つ
3. png→jpgに変換（Macではimg2pdfがpngではできなかったため）
4. jpg→pdfに変換
5. 複数のpdfを1枚に結合
6. いらないファイル類を削除



## 参考

[Python is the Perfect Tool for any Problem - Towards Data Science](https://towardsdatascience.com/python-is-the-perfect-tool-for-any-problem-f2ba42889a85)
