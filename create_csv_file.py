import os
import pandas as pd

# Hàm tạo dataframe từ thư mục (train/test)
def create_dataframe_from_dir(base_path):
    data = []
    # duyệt qua các folder con (neg, pos)
    for label_dir in os.listdir(base_path):
        label_path = os.path.join(base_path, label_dir)
        if not os.path.isdir(label_path):
            continue
        for fname in os.listdir(label_path):
            if fname.endswith(".txt"):
                file_path = os.path.join(label_path, fname)
                with open(file_path, "r", encoding="utf-8") as f:
                    text = f.read().strip()
                # Lấy score từ tên file: [id]_[score].txt
                try:
                    score = int(fname.split("_")[1].split(".")[0])
                except:
                    score = None
                # Lấy đường dẫn tương đối (ví dụ: neg/0_2.txt)
                rel_path = os.path.relpath(file_path, base_path)
                data.append([rel_path, text, score])
    return pd.DataFrame(data, columns=["dir", "text", "score"])


if __name__ == "__main__":
    # Tạo train.csv
    print("Đang tạo train.csv...")
    train_base = os.path.join("data", "train")
    train_df = create_dataframe_from_dir(train_base)
    train_df.to_csv("train.csv", index=False, encoding="utf-8")

    # Tạo test.csv
    print("Đang tạo test.csv...")
    test_base = os.path.join("data", "test")
    test_df = create_dataframe_from_dir(test_base)
    test_df.to_csv("test.csv", index=False, encoding="utf-8")

    print("Done! train.csv và test.csv đã được tạo")
