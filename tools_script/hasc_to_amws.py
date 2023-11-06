import os
import csv

# 入力ディレクトリと出力ディレクトリを指定します
input_directory = 'hasc(walk)'
output_directory = 'new_hasc(walk)'

# 出力ディレクトリが存在しない場合は作成します
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# 入力ディレクトリ内のCSVファイルを処理します
for filename in os.listdir(input_directory):
    if filename.endswith(".csv"):
        input_file_path = os.path.join(input_directory, filename)
        output_file_path = os.path.join(output_directory, filename)

        # CSVファイルを読み取りモードで開き、新しいCSVファイルを書き込みモードで作成します
        with open(input_file_path, 'r', newline='') as input_file, open(output_file_path, 'w', newline='') as output_file:
            reader = csv.reader(input_file)
            writer = csv.writer(output_file)

            for row in reader:
                # 0列目はそのまま、1列目、2列目、3列目を10,000倍して書き込みます
                new_row = [row[0], str(float(row[1]) * 10000), str(float(row[2]) * 10000), str(float(row[3]) * 10000)]
                writer.writerow(new_row)

print("処理が完了しました。")
