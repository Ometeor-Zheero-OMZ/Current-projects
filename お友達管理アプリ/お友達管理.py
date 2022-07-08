from datetime import date
import sqlite3
import tkinter as tk
import tkinter.messagebox as msg


conn = sqlite3.connect('friend_management.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users(名前, ふりがな, 性別, 生年月日, 人間, 
             関係度合い, 記録日)''')

conn.close()


def import_SQL():
    friend_name = name_entry.get()  # 名前
    furigana = furigana_entry.get()  # ふりがな
    gender = gender_entry.get()  # 性別
    birthday = birthday_entry.get()  # 生年月日
    relationship = relationship_entry.get()  # 人間関係
    percent_of_relationship = percent_of_relationship_entry.get()  # 関係度合い
    made_profile_date = made_profile_date_entry.get()  # 記録日

    conn = sqlite3.connect('friend_management.db')
    c = conn.cursor()

    data = [
        (friend_name, furigana, gender, birthday, relationship, percent_of_relationship, made_profile_date), ]
    try:
        c.executemany('INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?)', data)
        conn.commit()

        for i in data:
            msg.showinfo('登録完了', '{0}を入力しました。'.format(i))

        conn.close()
    except:
        pass


root = tk.Tk()
root.title(u'お友達管理アプリ')
root.minsize(500, 380)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

name_label = tk.Label(text=u'名前')
name_label.pack()
name_entry = tk.Entry()
name_entry.pack()
friend_name = name_entry.get()

furigana_label = tk.Label(text=u'ふりがな')
furigana_label.pack()
furigana_entry = tk.Entry()
furigana_entry.pack()
furigana = furigana_entry.get()

gender_label = tk.Label(text=u'性別')
gender_label.pack()
gender_entry = tk.Entry()
gender_entry.pack()
gender = gender_entry.get()

birthday_label = tk.Label(text=u'生年月日')
birthday_label.pack()
birthday_entry = tk.Entry()
birthday_entry.pack()
birthday = birthday_entry.get()

relationship_label = tk.Label(text=u'人間関係')
relationship_label.pack()
relationship_entry = tk.Entry()
relationship_entry.pack()
relationship = relationship_entry.get()

percent_of_relationship_label = tk.Label(text=u'関係度合い')
percent_of_relationship_label.pack()
percent_of_relationship_entry = tk.Entry()
percent_of_relationship_entry.pack()
percent_of_relationship = percent_of_relationship_entry.get()

day = str(date.today())
made_profile_date_label = tk.Label(text=u'記録日')
made_profile_date_label.pack()
made_profile_date_entry = tk.Entry()
made_profile_date_entry.insert(tk.END, day)
made_profile_date_entry.pack()
made_profile_date = made_profile_date_entry.get()

# ボタン
button1 = tk.Button(
    root, text='登録',
    command=import_SQL)
button1.pack()

root.mainloop()