# Pyautogui_screenshot

Pyautoguiを使用して、Macのスクリーンショットを自動化＋pdf変換+1つのpdfにまとめる

## 使い方

```
#python book_screenshot_full.py 右か左か ページ数 保存先のパス

% python book_screenshot_full.py left 10 /Users/yamada/SS/Pyautogui_SS/test_dir
```

## 使用した主なライブラリ

- Pyautogui
- img2pdf
- PyPDF2

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
