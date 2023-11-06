import os
import csv

# ディレクトリを取得する
directory = "Protocol"

# ディレクトリ内のすべての.datファイルを取得する
dat_files = [file for file in os.listdir(directory) if file.endswith(".dat")]

# .datファイルをループ処理する
for dat_file in dat_files:
    # .datファイルのパス
    dat_file_path = os.path.join(directory, dat_file)

    # 対応する.csvファイルのパス
    csv_file_path = os.path.splitext(dat_file_path)[0] + ".csv"

    # .datファイルを開いて内容を読み取り、スペースをカンマに置き換えて.csvファイルに書き込む
    with open(dat_file_path, "r") as dat_file, open(csv_file_path, "w", newline='') as csv_file:
        reader = csv.reader(dat_file, delimiter=' ')
        writer = csv.writer(csv_file, delimiter=',')
        for row in reader:
            writer.writerow(row)

    # .datファイルを削除
    os.remove(dat_file_path)

print("変換が完了しました。.datファイルは削除されました。")
