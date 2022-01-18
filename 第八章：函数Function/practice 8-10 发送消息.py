def show_messages(texts):
    """展示列表中的文本信息"""
    for text in texts:
        print(text)


def send_message(texts, sent_messages):
    while texts:
        current_text = texts.pop()
        print(f'printing text:{current_text}')
        sent_messages.append(current_text)
    print(sent_messages)
    print(texts)


ts = ['tanayo', 'cml']
sent_messages = []
# send_message(ts, sent_messages)
# print(ts)
# print("~~~~~~~~~~~~~~~~~~~~~")
send_message(ts[:], sent_messages)       # 切片表示法[:]创建列表副本，从而保护原列表不被修改。
print(ts)





