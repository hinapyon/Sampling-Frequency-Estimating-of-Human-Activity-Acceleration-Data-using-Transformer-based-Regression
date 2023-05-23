import csv

# 読み込むcsvファイルのパス
csv_file_path = "my_walk_data(100Hz15minutes)/walk100Hz-20230509-210827196.csv"

# 出力するcsvファイルのディレクトリ
output_directory = "my_walk_data(100Hz15minutesTo20seconds)"

# csvファイルを開く
with open(csv_file_path, "r") as csv_file:

  # csvファイルのreaderオブジェクトを取得する
  reader = csv.reader(csv_file)

  # 最初の2000行を取得する
  first_2000_rows = list(reader)

  # 最初の2000行をcsvファイルに出力する
  with open(f"{output_directory}/first_2000_rows.csv", "w") as output_file:
    writer = csv.writer(output_file)
    writer.writerows(first_2000_rows)

  # 残りの行を2000行ずつ取得する
  for i in range(len(reader) // 2000):
    current_2000_rows = reader[i * 2000:(i + 1) * 2000]

    # 現在の2000行をcsvファイルに出力する
    with open(f"{output_directory}/part_{i + 1}.csv", "w") as output_file:
      writer = csv.writer(output_file)
      writer.writerows(current_2000_rows)
