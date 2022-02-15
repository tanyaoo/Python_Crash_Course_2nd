def count_words(file_name):
    """计算一个文件夹包含多少个单词"""
    try:
        with open(file_name, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print("The file is not exist.")
        pass    # 静默失败，什么也不做
    else:
        words = contents.split()
        number_word = len(words)
        print(f"The file {file_name} has about {number_word} words.")


filenames = ["The Husband’s Story.txt.rtf", "Gedichte.rtf",
             "alice in wonderland.txt", "Woman in the   Golden Ages.txt.rtf"]

for filename in filenames:
    count_words(filename)
