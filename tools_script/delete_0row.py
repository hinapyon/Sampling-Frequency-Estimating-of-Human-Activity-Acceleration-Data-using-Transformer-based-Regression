import os
import pandas as pd

# ディレクトリ内のCSVファイルを取得
directory_path = 'new_data'  # ディレクトリのパスを指定してください
output_directory = 'my_walk_data(100Hz15minutesTo20seconds)'  # 出力ディレクトリのパスを指定してください

# ディレクトリ内のCSVファイルをリストアップ
csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]

# 各CSVファイルに対して処理を実行
for csv_file in csv_files:
    # CSVファイルのフルパス
    file_path = os.path.join(directory_path, csv_file)

    # CSVファイルを読み込み
    df = pd.read_csv(file_path)

    # 0列目を削除
    df = df.iloc[:, 1:]

    # 出力ファイルのパス
    output_file_path = os.path.join(output_directory, csv_file)

    # 新しいCSVファイルに保存
    df.to_csv(output_file_path, index=False)

print("処理が完了しました。")
