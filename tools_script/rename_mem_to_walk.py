import os
import shutil

# 元のフォルダのパス
root_path = "/Users/hinase/Downloads/oko"

# 新しいフォルダのパス
new_path = "/Users/hinase/CodeChord/サンプリング周波数推定/my_walk_data(100Hz15minutes)"
#new_path2 = "/Users/hinase/CodeChord/サンプリング周波数推定/my_walk_data"

# "mem"から"walk"に変換してファイルを新しいフォルダに移動
for foldername, subfolders, filenames in os.walk(root_path):
    for filename in filenames:
        if filename.startswith("mem-") and filename.endswith(".csv"):
            new_filename = filename.replace("mem-", "walk")
            src_path = os.path.join(foldername, filename)
            dst_path = os.path.join(new_path, new_filename)
            #dst_path2 = os.path.join(new_path2, new_filename)
            shutil.move(src_path, dst_path)
            #shutil.move(src_path, dst_path2)
            shutil.rmtree(os.path.join(root_path, foldername))
