import os
import csv

# ディレクトリを取得する
directory = "walk_mod"

# ディレクトリ内のすべてのcsvファイルを取得する
files = os.listdir(directory)

# csvファイルをループ処理する
for file in files:

    # csvファイルを開く
    with open(os.path.join(directory, file), "r") as f:

        # csvファイルのヘッダー行を削除する
        reader = csv.reader(f)
        next(reader)

        # csvファイルを書き込む
        with open(os.path.join(directory, file), "w") as f:
            writer = csv.writer(f)
            writer.writerows(reader)
