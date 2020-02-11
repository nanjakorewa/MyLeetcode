"""
2020/02/11 Yk
各問題ごとにディレクトリを作成して, その下にファイルを移動する.
"""
import os, sys
import shutil

for f in [f for f in os.listdir("./") if "." in f]:
    dirname = ""

    # 複数の解法があるものはまとめる
    if "_" in f:
        dirname = f.split("_")[0]
    else:
        dirname = f.split(".")[0]

    # problemがファイル名に含まれない場合は無視する
    if not "problem" in dirname:
        continue

    # ディレクトリ作成して移動する
    os.makedirs(dirname, exist_ok=True)
    shutil.move(f, os.path.join(dirname, f))