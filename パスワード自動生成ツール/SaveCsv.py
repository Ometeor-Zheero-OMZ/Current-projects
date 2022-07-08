import random
import string
import tkinter as tk
import tkinter.messagebox as msg
import pandas as pd


alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*")


def save_data_to_csv_file():
    """
    Return:
        str: ご利用のサービス名と自動生成されたパスワードを用意した保存します。
    """

    service_name = str_service_name.get()
    # TODO: (Ituski Kajiya) 下記に連なる変数に(1)数値以外のデータを入力した場合、ValueError: invalid literal for int() with base 10が表示され、
    #  異なるデータ構造のため、整合性のあるデータ構造と一致させる。(2)空欄のまま保存しようとすると、パスワードは生成されず保存もされないが、
    #  ユーザーに対してポップアップで入力案内をする方法を考える。
    length_password = int(length_password_user_request.get())
    number_of_alphabets = int(alphabets_count.get())
    number_of_digits = int(digits_count.get())
    number_of_special_char = int(special_characters_count.get())

    characters_count = number_of_alphabets + number_of_digits + number_of_special_char

    if characters_count > length_password:
        msg.showinfo("お知らせ", "ご希望の長さを越えてしまいます。"
                             "\nご希望の長さに合う数の文字・数値・特殊文字"
                             "\nをそれぞれ入力してください。")
        return

    saved_password = []

    for i in range(number_of_alphabets):
        saved_password.append(random.choice(alphabets))

    for i in range(number_of_digits):
        saved_password.append(random.choice(digits))

    for i in range(number_of_special_char):
        saved_password.append(random.choice(special_characters))

    if characters_count < length_password:
        random.shuffle(characters)
        for i in range(length_password - characters_count):
            saved_password.append(random.choice(characters))

    random.shuffle(saved_password)
    total_saved_password = "".join(saved_password)

    if service_name == '':
        msg.showinfo("お知らせ", "サービス名が入力されていません。")
    elif length_password == '':
        msg.showinfo("お知らせ", "ご希望の長さが入力されていません。")
    elif number_of_alphabets == '':
        msg.showinfo("お知らせ", "アルファベットの長さが入力されていません。")
    elif number_of_digits == '':
        msg.showinfo("お知らせ", "数値の長さが入力されていません。")
    elif number_of_special_char == '':
        msg.showinfo("お知らせ", "特殊文字の長さが入力されていません。")
    else:
        df = pd.DataFrame({'Service Name':[service_name], 'Generated Password':[total_saved_password]})
        df.to_csv("PasswordManagement.csv", mode='a', header=False, index=False)
        msg.showinfo("お知らせ", "パスワードがPasswordManagement.csv内に保存されました。")


"""
Tkinterの操作画面は下記からです。
"""
base = tk.Tk()
base.title("パスワード管理ツール")
canvas = tk.Canvas(base, width=300, height=400, bd=0, highlightthickness=0)
canvas.pack()

str_service_name = tk.StringVar()
length_password_user_request = tk.StringVar()
alphabets_count = tk.StringVar()
digits_count = tk.StringVar()
special_characters_count = tk.StringVar()


label_service_name = tk.Label(base, text="サービス名：")
label_service_name.place(x=30, y=18)

txtbox_service_name = tk.Entry(base, width=20, textvariable=str_service_name)
txtbox_service_name.place(x=100, y=20)

label_length = tk.Label(base, text="ご希望の長さ：")
label_length.place(x=20, y=60)

txtbox_length = tk.Entry(base, width=10, textvariable=length_password_user_request)
txtbox_length.place(x=100, y=60)

label_alphabets = tk.Label(base, text="アルファベット：")
label_alphabets.place(x=17, y=100)

txtbox_alphabets = tk.Entry(base, width=10, textvariable=alphabets_count)
txtbox_alphabets.place(x=100, y=100)

label_digits = tk.Label(base, text="数値：")
label_digits.place(x=63, y=140)

txtbox_digits = tk.Entry(base, width=10, textvariable=digits_count)
txtbox_digits.place(x=100, y=140)

label_special_char = tk.Label(base, text="特殊文字：")
label_special_char.place(x=40, y=180)

txtbox_special_char = tk.Entry(base, width=10, textvariable=special_characters_count)
txtbox_special_char.place(x=100, y=180)


btn_seldata = tk.Button(base, text="パスワードを保存", command=save_data_to_csv_file)
btn_seldata.place(x=100, y=220)

base.mainloop()