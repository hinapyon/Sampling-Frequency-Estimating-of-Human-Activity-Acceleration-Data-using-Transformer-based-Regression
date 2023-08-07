import os
import csv

# ディレクトリを取得する
directory = "setback(walk)"

# ディレクトリ内のすべてのcsvファイルを取得する
files = os.listdir(directory)

# csvファイルをループ処理する
for file in files:

    # csvファイルを開く
    with open(os.path.join(directory, file), "r") as f:

        # csvファイルの最後の行を削除する
        reader = csv.reader(f)
        lines = list(reader)
        lines.pop()

        # csvファイルを書き込む
        with open(os.path.join(directory, file), "w") as f:
            writer = csv.writer(f)
            writer.writerows(lines)
